import matplotlib.pyplot as plt
import datetime

from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

def run():
    N = 5
    DT = 2
    P = 4

    stations = build_station_list()
    at_risk_stations = stations_highest_rel_level(stations, N)

    for station in at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=DT))
        plot_water_level_with_fit(station, dates, levels, P)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()