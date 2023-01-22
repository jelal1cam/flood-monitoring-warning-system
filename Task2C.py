from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    station_list = build_station_list()
    update_water_levels(station_list)
    
    for x in stations_highest_rel_level(station_list, 10):
        print(x)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
