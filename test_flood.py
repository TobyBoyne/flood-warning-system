from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from example_data import gen_stations


def test_stations_highest_rel_level():
    stations = gen_stations()
    # Latest levels are chosen such that only 'id4' station will be above 0.5 tol
    # assign each level in turn to one of the stations
    latest_levels = [0.07, 0.21, 0.45, 0.1, 1.332]
    for i, station in enumerate(stations):
        station.latest_level = latest_levels[i]

    above_tol = stations_level_over_threshold(stations, 0.5)
    assert len(above_tol)
    assert above_tol[0][0] == stations[4]

def test_stations_level_over_threshhold():
    pass

test_stations_highest_rel_level()