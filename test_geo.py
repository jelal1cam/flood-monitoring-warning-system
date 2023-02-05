import floodsystem.geo as geo
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
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

    stations = [station1, station2]
    sorted_stations = geo.stations_by_distance(stations, (0., 0.))
    assert sorted_stations[0][0:2] == ('some station 1', 'town 1')
    assert sorted_stations[1][0:2] == ('some station 2', 'town 2')

def test_stations_within_radius():
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
                                     coord=(10., 10.),
                                     typical_range=(0., 1.),
                                     river='river 3',
                                     town='town 3')
    stations = [station1, station2, station3]
    stations_within = sorted([i.name for i in geo.stations_within_radius(stations, (0., 0.), 200)])
    assert len(stations_within) == 2
    assert stations_within[0] == "some station 1"
    assert stations_within[1] == "some station 2"

def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "river 1"
    town = "rown"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "river 2"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s, s1]
    dict = geo.stations_by_river(stations)

    assert len(dict["river 1"]) == 1
    assert len(dict["river 2"]) == 1

def test_rivers_with_station():
    stations = [
        MonitoringStation('id0', 'm_id0', 'Bourton Dickler', (51.874767, -1.740083), (0.068, 0.42), 'River Glen',
                          'Little Rissington'),
        MonitoringStation('id1', 'm_id1', 'Surfleet Sluice', (52.845991, -0.100848), None, 'River Glen',
                          'Surfleet Seas End'),
        MonitoringStation('id2', 'm_id2', 'Gaw Bridge', (50.976043, -2.793549), (0.231, 0.231), 'River Parrett',
                          'Kingsbury Episcopi'),
        MonitoringStation('id3', 'm_id3', 'Hemingford', (52.323618, -0.101287), (10, 5), 'River Parrett',
                          'Hemingford Grey'),
        MonitoringStation('id4', 'm_id4', 'Swindon', (52.51274, -2.205945), (1.044, 1.336), 'Smestow Brook', 'Swindon')
        ]

    rivers = geo.rivers_with_station(stations)

    assert rivers == {"River Glen", "River Parrett", "Smestow Brook"}

def test_rivers_by_station_number():
    station1 = MonitoringStation(station_id='test-s-id1',
                                     measure_id='test-m-id1',
                                     label='some station 1',
                                     coord=(0, 1),
                                     typical_range=(0.1, 0.4),
                                     river='river 1',
                                     town='town 1')
    station2 = MonitoringStation(station_id='test-s-id2',
                                     measure_id='test-m-id2',
                                     label='some station 2',
                                     coord=(1, 1),
                                     typical_range=(0.3, 0.8),
                                     river='river 2',
                                     town='town 2')
    station3 = MonitoringStation(station_id='test-s-id3',
                                     measure_id='test-m-id3',
                                     label='some station 3',
                                     coord=(0, 3),
                                     typical_range=(0.43, 0.88),
                                     river="river 2",
                                     town="town 3")
    station4 = MonitoringStation(station_id='test-s-id4',
                                     measure_id='test-m-id4',
                                     label='some station 4',
                                     coord=(8, 3),
                                     typical_range=(0.1, 0.9),
                                     river="river 3",
                                     town="town 4")
    assert geo.rivers_by_station_number([station1], 1) == [("river 1", 1)]
    assert geo.rivers_by_station_number([station1, station2, station3], 1) == [("river 2", 2)]
    assert geo.rivers_by_station_number([station1, station2, station3], 2) == [("river 2", 2), ("river 1", 1)]
    assert geo.rivers_by_station_number([station1, station2, station3, station4], 2) == [("river 2", 2), ("river 1", 1),
                                                                                         ("river 3", 1)]
    assert geo.rivers_by_station_number([station1, station2, station3, station4], 3) == [("river 2", 2), ("river 1", 1),
                                                                                         ("river 3", 1)]
    assert geo.rivers_by_station_number([station1, station2, station3, station4], 4) == [("river 2", 2), ("river 1", 1),
                                                                                         ("river 3", 1)]
    assert geo.rivers_by_station_number([station1, station2, station3, station4], 5) == [("river 2", 2), ("river 1", 1),
                                                                                         ("river 3", 1)]
def test_rivers_by_station_number():
    stations = [
        MonitoringStation('id0', 'm_id0', 'Bourton Dickler', (51.874767, -1.740083), (0.068, 0.42), 'River Glen',
                          'Little Rissington'),
        MonitoringStation('id1', 'm_id1', 'Surfleet Sluice', (52.845991, -0.100848), None, 'River Glen',
                          'Surfleet Seas End'),
        MonitoringStation('id2', 'm_id2', 'Gaw Bridge', (50.976043, -2.793549), (0.231, 0.231), 'River Parrett',
                          'Kingsbury Episcopi'),
        MonitoringStation('id3', 'm_id3', 'Hemingford', (52.323618, -0.101287), (10, 5), 'River Parrett',
                          'Hemingford Grey'),
        MonitoringStation('id4', 'm_id4', 'Swindon', (52.51274, -2.205945), (1.044, 1.336), 'Smestow Brook', 'Swindon')
        ]
    rivers = geo.rivers_by_station_number(stations, 1)

    assert rivers == [("River Glen", 2), ("River Parrett", 2)]