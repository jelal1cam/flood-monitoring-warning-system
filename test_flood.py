from floodsystem.flood import *
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
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
                                     typical_range=(0., 1.),
                                     river='river 2',
                                     town='town 2')
    station3 = MonitoringStation(station_id='test-s-id3',
                                     measure_id='test-m-id3',
                                     label='some station 3',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='river 3',
                                     town='town 3')

    station1.latest_level = 0.5
    station2.latest_level = 0.6
    station3.latest_level = 0.7
    stations = [station1, station2, station3]

    assert stations_level_over_threshold(stations, 0.5) == [(station3, 0.7), (station2, 0.6)]
    
def test_stations_highest_rel_level():
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
                                    typical_range=(0., 1.),
                                    river='river 2',
                                    town='town 2')
    station3 = MonitoringStation(station_id='test-s-id3',
                                     measure_id='test-m-id3',
                                     label='some station 3',
                                    coord=(1., 1.),
                                    typical_range=(0., 1.),
                                    river='river 3',
                                    town='town 3')

    station1.latest_level = 0.5
    station2.latest_level = 0.6
    station3.latest_level = 0.7
    stations = [station1, station2, station3]

    assert stations_highest_rel_level(stations, 3) == [station3, station2, station1]
    assert stations_highest_rel_level(stations, 2) == [station3, station2]
    assert stations_highest_rel_level(stations, 1) == [station3]
    
    station1.latest_level = 0.5
    station2.latest_level = 0.6
    station3.latest_level = 0.2

    assert stations_highest_rel_level(stations, 3) == [station2, station1, station3]
    assert stations_highest_rel_level(stations, 2) == [station2, station1]