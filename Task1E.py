from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    print(rivers_by_station_number(build_station_list(), 9))
    #print(str(build_station_list()))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
