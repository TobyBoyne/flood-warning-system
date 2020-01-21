from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print("Number of rivers: {}".format(len(rivers)))
    print("First ten rivers: {}".format(sorted(rivers)[:10]))

if __name__ == "__main__":
    run()