from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print("Number of rivers: {}".format(len(rivers)))
    print("First ten rivers: {}".format(sorted(rivers)[:10]))

    rivers_dict = stations_by_river(stations)
    test_rivers = ("River Aire", "River Cam", "River Thames")
    for river in test_rivers:
        stations_on_river = rivers_dict.get(river)
        station_names = [s.name for s in stations_on_river]
        print("Stations on {}: {}".format(river, station_names))

if __name__ == "__main__":
    run()