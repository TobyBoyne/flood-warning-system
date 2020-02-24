# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from example_data import gen_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():
    stations = gen_stations()
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert inconsistent_stations == [stations[1], stations[3]]

def test_relative_water_level():
    """For a given set of levels and their expected relative value, assert that the calculated relative value
    is the same as expected"""
    station = gen_stations()[0]
    levels = (
        (0.068, 0),
        (0.3, 0.659090909),
        (0.42, 1),
        (0.01, -0.16477272),
        (None, None)
    )
    for level, rel in levels:
        station.latest_level = level
        if level is not None:
            assert round(station.relative_water_level() - rel, 6) == 0
        else:
            assert station.relative_water_level() is None