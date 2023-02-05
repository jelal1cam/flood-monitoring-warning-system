from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    '''
    Use of geo.rivers_with_station to print how many rivers have at least one monitoring station and prints the first 10 of these rivers in alphabetical order.
    Use of geo.stations_by_river to print the names of the stations located on the River Aire, River Cam and the River Thames.
    '''
    station_list = build_station_list()
    rivers_stations = rivers_with_station(station_list)
    print(str(len(rivers_stations)) + " stations.")
    print("First 10 - " + str(sorted(rivers_stations)[:10]))

    stations_river = stations_by_river(station_list)
    river_list = ["River Aire", "River Cam", "River Thames"]
    for river in river_list:
        print(river + ': ')
        print(sorted(stations_river[river]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()