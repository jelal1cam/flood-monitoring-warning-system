from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def test_plot_water_levels():
    station1 = MonitoringStation(station_id='test-s-id1',
                                     measure_id='test-m-id1',
                                     label='some station 1',
                                     coord=(-2.2, 3.8),
                                     typical_range=(0.20, 1.00),
                                     river='river 1',
                                     town='town 1')
    dates = [datetime(2017, 12, 30), datetime(2017, 12, 31), datetime(2018, 1, 1), datetime(2018, 1, 2), datetime(2018, 1, 3), datetime(2018, 1, 4), datetime(2018, 1, 5)]
    levels = [0.25, 0.58, 0.94, 0.99, 0.56, 0.76, 0.33]

    plot_water_levels(station1, dates, levels)
    
    assert station1.name == "some station 1"
    assert len(dates) == 7
    assert len(levels) == 7
    assert plt.title('date') != None
    assert plt.ylabel('water level (m)') != None
