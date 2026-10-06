import math

def get_station_data(filename: str):
    dictionary={}
    with open(filename) as stationsfile:
        for line in stationsfile:
            parts=line.split(";")
            if parts[0]=="Longitude":
                continue
            else:
                coordinates=(float(parts[0]),float(parts[1]))
                dictionary[parts[3]]=coordinates
    return dictionary

def distance(stations: dict, station1: str, station2: str):
    longitude1,latitude1=stations[station1]
    longitude2,latitude2=stations[station2]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    distances_list={}
    for key1 in stations:
        for key2 in stations:
            mydistance=distance(stations,key1,key2)
            mytuple=(key1,key2)
            distances_list[mytuple]=mydistance
    max_key=max(distances_list, key=distances_list.get)
    return (max_key[0],max_key[1],distances_list[max_key])