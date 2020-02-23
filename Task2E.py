import matplotlib.pyplot as plt
import datetime

from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():

    stations = build_station_list()
    dt = 10
    greatest_relative_level_stations = stations_highest_rel_level(stations, 5)

    for station in greatest_relative_level_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

        plt.show()

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()