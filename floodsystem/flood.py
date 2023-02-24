from floodsystem.utils import sorted_by_key
try:
    from .analysis import polyfit  # noqa
except ImportError:
    from analysis import polyfit

def stations_level_over_threshold(stations, tol):
    '''
    Function that returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station. The returned list is sorted by the relative levl in descending order.
    '''
    list = []

    for x in stations:
        latest_relative_water_level = x.relative_water_level()

        if latest_relative_water_level is not None and latest_relative_water_level > tol :
            
            list.append((x, latest_relative_water_level))

    sorted_list = sorted_by_key(list, 1, True)        
    
    return sorted_list

def stations_highest_rel_level(stations, N):
    '''
    Function that returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest. The returned list is sorted by descending order by relative level.
    '''
    at_risk = []
    for x in stations:
        if x.relative_water_level() is not None:
            at_risk.append((x, x.relative_water_level()))
    
    sorted_at_risk = sorted_by_key(at_risk, 1, True)
    
    final = [x[0] for x in sorted_at_risk]
    
    return final[:N]

def risk_allocation_town(stations, N):
    risk_level = []
    for town in stations:
        risk = "Low"
        if town.relative_water_level() > 1:
            risk = "Severe"
        elif x.relative_water_level()<1 and x.relative_water_level()>0.75 and gradient>0:
            risk = "high"
        elif x.relative_water_level()<1 and x.relative_water_level()>0.75 and gradient<0:
            risk = "moderate"
        risk_level.append((town, risk))
    return risk_level