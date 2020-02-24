from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from example_data import gen_stations


def test_stations_highest_rel_level():
    # Create a list of stations with two copies of each station
    stations = gen_stations() + gen_stations()
    # Assign levels to each of the stations
    latest_levels = [1, 0.21, 0.45, 0.1, 1.332] + [0.08, 0.5, 0.9, 0.6, 4]
    for i, station in enumerate(stations):
        station.latest_level = latest_levels[i]

    highest_rel_level = stations_highest_rel_level(stations, 3)
    assert highest_rel_level == [stations[j] for j in (9, 0, 4)]

def test_stations_level_over_threshhold():
    stations = gen_stations()
    # Latest levels are chosen such that only 'id4' station will be above 0.5 tol
    # assign each level in turn to one of the stations
    latest_levels = [0.07, 0.21, 0.45, 0.1, 1.332]
    for i, station in enumerate(stations):
        station.latest_level = latest_levels[i]

    above_tol = stations_level_over_threshold(stations, 0.5)
    assert len(above_tol)
    assert above_tol[0][0] == stations[4]