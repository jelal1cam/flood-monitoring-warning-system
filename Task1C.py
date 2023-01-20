from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    '''
    Using function geo.stations_within_radius to build a list of stations within 10 km of the Cambridge city centre.
    Name of stations are listed in alphabetical order.
    '''

    stations_within = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    alphabetical_order = sorted([station.name for station in stations_within])
    print(alphabetical_order)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
