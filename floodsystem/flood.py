<<<<<<< HEAD
#from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    #station = build_station_list()
    water_level_stations = []
    for station in stations:
        latest_level = station.latest_level
        if latest_level is not None and latest_level > tol:
            details = (station, station.relative_water_level())
            water_level_stations.append(details)

    sorted_stations = sorted_by_key(water_level_stations, 1, True)

    return(sorted_stations)
=======
#TODO: replace this with the intended function
# This function is temporary to carry out Task2F

def stations_highest_rel_level(stations, N):
    return stations[:N]
>>>>>>> c82d16daa1d09e69a3575dc8648584f0af78cbbd
