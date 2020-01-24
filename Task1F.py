from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    station_names = []

    for station in inconsistent_stations:
        station_names.append(station.name)
    station_names.sort()

    print(station_names)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
