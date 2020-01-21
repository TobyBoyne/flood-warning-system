# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa

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
            if river in rivers:
                rivers[river].append(station)
            else:
                rivers[river] = []

    return rivers

def rivers_with_station(stations):
    """Returns the names of rivers on which a station is situated"""
    return set(stations_by_river(stations).keys())