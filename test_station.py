# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


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
    stations = [
        MonitoringStation("a0", "a1", "a2", (0, 0), (1, 10), "a3", "a4"),
        MonitoringStation("b0", "b1", "b2", (0, 0), (10, 1), "b3", "b4"),
        MonitoringStation("c0", "c1", "c2", (0, 0), None, "c3", "c4")
    ]

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert inconsistent_stations == [stations[1], stations[2]]