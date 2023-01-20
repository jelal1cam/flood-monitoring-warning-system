from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    '''
    This uses geo.stations_by_distance and prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from the Cambridge cirty centre.
    '''

    list = stations_by_distance(build_station_list(), (52.2053, 0.1218))
    print("Closest 10 stations: " + str(list[:10]))
    print("Furthest 10 stations: " + str(list[-10:]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()