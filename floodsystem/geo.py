# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

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