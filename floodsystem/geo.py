# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.utils import sorted_by_key, first_N_with_ties

from haversine import haversine, Unit


def stations_by_distance(stations,p):
    """Given a list of station objects and a coordinate, the function returns a list of tuples
    (station, distance)"""
    distances = []
    for station in stations:
        coordinate = station.coord
        distance = haversine(coordinate, p)
        distances.append((station, distance))

    sorted_distances = sorted_by_key(distances,1)

    return sorted_distances


def stations_by_river(stations):
    """Returns a dictionary containing rivers (keys), and the stations on each river (values)"""
    rivers = {}
    for station in stations:
        # only add the river if station.river has been set
        river = station.river
        if river is not None:
            # add the station to the river key in the dictionary
            # if the key is not in the dictionary, add it
            if river in rivers:
                rivers[river].append(station)
            else:
                rivers[river] = [station]

    return rivers


def rivers_with_station(stations):
    """Returns the names of rivers on which a station is situated"""
    return set(stations_by_river(stations).keys())


def rivers_by_station_number(stations, N):
    """Returns a list of tuples
    (river, number of stations on that river)"""
    river_counts = []
    river_dict = stations_by_river(stations)
    for (river, river_stations) in river_dict.items():
        river_counts.append((river, len(river_stations)))

    # sort the list of rivers by number of stations, then by alphabetical
    # removes any ambiguity for tied rivers
    sorted_rivers = sorted_by_key(river_counts, 0)
    sorted_rivers = sorted_by_key(sorted_rivers, 1, reverse=True)

    return list(first_N_with_ties(sorted_rivers, N, i=1))