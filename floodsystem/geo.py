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

def rivers_with_station(stations):
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

def rivers_by_station_number(stations, N):
    '''
    Function returns the N with the greatest number of monitoring stations
    '''
    number_of_stations = []
    river_station_dictionary = stations_by_river(stations)
    for (river_name, station_list) in river_station_dictionary.items():
        number_of_stations.append((river_name, len(station_list)))
    sorted_number_of_stations = sorted_by_key(number_of_stations, 1, reverse = True)
    top_rivers = []
    counter = 0
    final_entry = None
    while counter < len(sorted_number_of_stations):
        if counter >= N and sorted_number_of_stations[counter][1] != final_entry:
            break
        top_rivers.append(sorted_number_of_stations[counter])
        final_entry = sorted_number_of_stations[counter][1]
        counter += 1
    return(top_rivers)
