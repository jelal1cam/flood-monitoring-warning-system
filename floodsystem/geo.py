# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit

try:
    from .utils import sorted_by_key  # noqa
except ImportError:
    from utils import sorted_by_key


def two_point_distance(point_1, point_2):
    '''
    Using the haversine module to calculate the distance between two stations.
    '''
    return haversine(point_1, point_2)

def stations_by_distance(stations, p):
    '''
    Function that, given a list of station objects and a coordinate p, returns a list of (station, distance) tuples, where distance(float) is the distance of the station (MonitoringStation) from the coordinate p is a tuple of floats of the coordinate p.
    '''
    station_distance_list = sorted_by_key([(s.name, s.town, two_point_distance(s.coord, p)) for s in stations], 2)

    return station_distance_list

def stations_within_radius(stations, centre, r):
    '''
    Returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x.
    '''
    within_radius = [within for within in stations if two_point_distance(within.coord, centre) < r]

    return within_radius

def rivers_with_stations(stations):
    '''
    Function that, given a list of station objects, returns a container (list/tuple/set) with the names of the rivers with a monitoring station.
    '''
    return set(station.river for station in stations)

def stations_by_river(stations):
    '''
    Function that returns a dictionary that maps river names (the 'key') to a list of station objects on a given river. 
    '''

    rivers_to_stations = {}
    for x in stations:
        station = []
        for y in stations:
            if x.river == y.river:
                station.append(y.name)
        rivers_to_stations[x.river] = station
    return rivers_to_stations

