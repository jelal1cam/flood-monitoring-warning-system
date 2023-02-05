# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *


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

def test_typical_range_consistent():
    assert MonitoringStation("test-s-id", "test-m-id", "some station", (0., 1.), (1., 4.), "River X",
                                 "My Town").typical_range_consistent() == True
    assert MonitoringStation("test-s-id", "test-m-id", "some station", (0., 1.), None, "River X",
                                 "My Town").typical_range_consistent() == False
    assert MonitoringStation("test-s-id", "test-m-id", "some station", (0., 1.), (1, -4), "River X",
                                 "My Town").typical_range_consistent() == False
    assert MonitoringStation("test-s-id", "test-m-id", "some station", (0., 1.), (0.5, 0.2), "River X",
                                 "My Town").typical_range_consistent() == False

def test_inconsistent_typical_range_stations():
    station1 = MonitoringStation(station_id="test-s-id1",
                                     measure_id="test-m-id1",
                                     label="some station 1",
                                     coord=(0, 1),
                                     typical_range=(1., 4.),
                                     river="River 1",
                                     town="My Town 1")
    station2 = MonitoringStation(station_id="test-s-id2",
                                     measure_id="test-m-id2",
                                     label="some station 2",
                                     coord=(1, 1),
                                     typical_range=None,
                                     river="River 2",
                                     town="My Town 2")
    station3 = MonitoringStation(station_id="test-s-id3",
                                     measure_id="test-m-id3",
                                     label="some station 3",
                                     coord=(0, 3),
                                     typical_range=(1, -4),
                                     river="River 2",
                                     town="My Town 3")
    station4 = MonitoringStation(station_id="test-s-id4",
                                     measure_id="test-m-id4",
                                     label="some station 4",
                                     coord=(8, 3),
                                     typical_range=(0.5, 0.2),
                                     river="River 3",
                                     town="My Town 4")
    assert inconsistent_typical_range_stations([station1]) == []
    assert inconsistent_typical_range_stations([station1, station2]) == [station2.name]
    assert inconsistent_typical_range_stations([station2, station3]) == [station2.name, station3.name]
    assert inconsistent_typical_range_stations([station4, station2, station3]) == [station2.name, station3.name,
                                                                                       station4.name]

    def test_relative_water_level():
        station1 = MonitoringStation(station_id='test-s-id1',
                                     measure_id='test-m-id1',
                                     label='some station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='river 1',
                                     town='town 1')
        station2 = MonitoringStation(station_id='test-s-id2',
                                     measure_id='test-m-id2',
                                     label='some station 2',
                                     coord=(1., 1.),
                                     typical_range=(1., 0.),
                                     river='river 2',
                                     town='town 2')
        assert station1.relative_water_level() is None
        station1.latest_level = 0.
        assert station1.relative_water_level() == 0.
        station1.latest_level = 1.
        assert station1.relative_water_level() == 1.
        station1.latest_level = 0.5
        assert station1.relative_water_level() == 0.5
        station1.latest_level = 2.
        assert station1.relative_water_level() == 2.

        station2.latest_level = 0.5
        assert station2.relative_water_level() is None