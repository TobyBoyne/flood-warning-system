from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    stations_in_r = stations_within_radius(stations, centre, r)
    station_names = []
    for station in stations_in_r:
        station_names.append(station.name)
    station_names.sort()
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()