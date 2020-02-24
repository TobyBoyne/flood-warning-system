import datetime

from floodsystem.analysis import projected_level_after_dt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.geo import towns_with_station


def run():
    """Find the trendline of the water level data for the last 2 days, and extrapolate DT_future days in the future.
    Assign the risk level based on the relative water level at this point in the future.

    TOL is the basic risk threshold - any station that has a relative level below TOL is automatically low risk.
    risk_threshold is then used to clasify the level of risk of a station that is above the typical range

    The projection approach is only taken for the top N_projected stations, as the fetch_measure_levels function
    takes a long time to retrieve the data

    The town takes the risk level of the HIGHEST risk station in that town"""

    DT = 2
    DT_future = 1
    TOL = 2.5
    N_projected = 25
    risk_threshold = (
        (5, 'Severe'),
        (3, 'High')
    )

    stations = build_station_list(use_cache=False)
    update_water_levels(stations)

    # Create a dict of all towns with a default risk of Low
    towns = towns_with_station(stations)
    risk_towns = {town: "Low" for town in towns}

    # Get a list of all stations that could potentially be "at risk"
    at_risk = stations_level_over_threshold(stations, TOL)
    at_risk_stations = [s[0] for s in at_risk]

    # Any station that is not in the top 25 of relative level has the "Moderate" label applied to its town
    stations_to_project = at_risk_stations[:N_projected]
    for station in at_risk_stations[N_projected:]:
        risk_towns[station.town] = "Moderate"

    print("Fetching data...")
    for station in stations_to_project:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=DT))
        proj_level = projected_level_after_dt(dates, levels, DT_future)
        station.latest_level = proj_level
        rel = station.relative_water_level()

        for tol, label in risk_threshold:
            if rel >= tol:
                risk_towns[station.town] = label
                break

        # the following else clause will only run if there is no break, meaning rel is not above any risk threshold
        # this means that the risk is moderate
        else:
            risk_towns[station.town] = "Moderate"

    # Reorganise town dict into another dictionary where the key is risk level
    by_risk = {
        "Severe":   [],
        "High":     [],
        "Moderate": [],
        "Low":      []
    }

    for town, risk_level in risk_towns.items():
        by_risk[risk_level].append(town)

    print("There are " + ", ".join(str(len(s)) + " " + label + " towns" for label, s in by_risk.items()))

    for risk in ("Severe", "High", "Moderate"):
        text_output = ["Towns with a risk of " + risk + ":"]
        text_output += by_risk[risk]
        print("\n> ".join(text_output) + "\n")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()