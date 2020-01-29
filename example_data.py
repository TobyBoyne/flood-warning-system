from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list




def gen_stations():
    stations = [
        MonitoringStation('id0', 'm_id0', 'Bourton Dickler', (51.874767, -1.740083), (0.068, 0.42), 'River Glen',
                          'Little Rissington'),
        MonitoringStation('id1', 'm_id1', 'Surfleet Sluice', (52.845991, -0.100848), None, 'River Glen',
                          'Surfleet Seas End'),
        MonitoringStation('id2', 'm_id2', 'Gaw Bridge', (50.976043, -2.793549), (0.231, 0.231), 'River Parrett',
                          'Kingsbury Episcopi'),
        MonitoringStation('id3', 'm_id3', 'Hemingford', (52.323618, -0.101287), (10, 5), 'River Parrett',
                          'Hemingford Grey'),
        MonitoringStation('id4', 'm_id4', 'Swindon', (52.51274, -2.205945), (1.044, 1.336), 'Smestow Brook', 'Swindon')
        ]

    return stations


if __name__ == "__main__":
    stations = build_station_list()
    # (self, station_id, measure_id, label, coord, typical_range,
    #             river, town):
    print(stations[:5])
    for i, s in enumerate(stations[:5]):
        print(
            f"MonitoringStation('id{i}', 'm_id{i}', '{s.name}', {s.coord}, {s.typical_range}, '{s.river}', '{s.town}')")