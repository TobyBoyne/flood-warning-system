from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            details = (station, relative_level)
            water_level_stations.append(details)

    sorted_stations = sorted_by_key(water_level_stations, 1, True)

    return sorted_stations


def stations_highest_rel_level(stations, N):
    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            water_level_stations.append(station)
    sorted_stations = sorted_by_key(water_level_stations, 1, True)

    return sorted_stations[:N]

