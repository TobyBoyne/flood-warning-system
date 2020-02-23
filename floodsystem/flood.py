from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each holding a station at which the latest relative
    water level is over tol and the relative water level at that station"""
    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            details = (station, relative_level)
            water_level_stations.append(details)

    sorted_stations = sorted_by_key(water_level_stations, 1, True)

    return sorted_stations


def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations at which the water level, relative to the typical
    range, is highest"""
    update_water_levels(stations)

    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            details = (station, relative_level)
            water_level_stations.append(details)

    sorted_by_water_level = sorted_by_key(water_level_stations, 1, True)
    sorted_stations = [i[0] for i in sorted_by_water_level]

    return sorted_stations[:N]