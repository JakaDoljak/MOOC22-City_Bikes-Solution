
import math

def read_file(file_name:str):
    lines = []
    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.strip()
            lines.append(line)
        return lines

def get_station_data(file_name:str):
    stations_data = read_file(file_name)
    stations = {} #save it in a dict
    for station in stations_data[1:]: #skip the first line because they are str headers
        data = station.split(";") #break string, to access individual element using indexing
        name = data[3]
        longitude = float(data[0])
        latitude = float(data[1])
        stations[name] = (longitude, latitude)
    return stations

def distance(stations:dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km
    
def all_distances(file_name: str):
    stations = get_station_data(file_name)
    distances = {}
    station_names = list(stations.keys())#convert keys of dict to regular list, in order to loop through

    for i in range(len(station_names)): # loop through every station
        for j in range(i + 1, len(station_names)):#loop from index after i, to avoid pairing with the same station and repeating pairs.
            name1 = station_names[i]
            name2 = station_names[j]
            dist = distance(stations, name1, name2)
            distances[(name1, name2)] = dist

    return distances

def greatest_distance(stations: dict):
    station_names = list(stations.keys())
    max_dist = 0
    farthest_pair = ("", "")

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            name1 = station_names[i]
            name2 = station_names[j]
            dist = distance(stations, name1, name2)
            if dist > max_dist:
                max_dist = dist
                farthest_pair = (name1, name2)

    return farthest_pair[0], farthest_pair[1], max_dist

if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    print(greatest_distance(stations))


