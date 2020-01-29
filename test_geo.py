import floodsystem.geo as geo
from example_data import gen_stations

def test_stations_by_distance():
    stations = gen_stations()
    distances = geo.stations_by_distance(stations, (0, 0))

    assert distances[0][0] == stations[2]
    assert round(distances[0][1] - 5674.419005723288) == 0

    assert distances[4][0] == stations[1]
    assert round(distances[4][1] - 5876.221687663879) == 0

def test_stations_within_radius():
    stations = gen_stations()
    within_radius = geo.stations_within_radius(stations, (0, 0), 5800)

    assert within_radius == [stations[0], stations[2]]

