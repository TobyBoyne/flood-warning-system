from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    water_level_stations = stations_highest_rel_level(stations, 10)

    station_names = []

    for station in water_level_stations:
        details = (station.name, station.relative_water_level())
        station_names.append(details)

    print(station_names)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()