import json
from functools import reduce

f = open("aquerium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def pick_animal_type(animal):
    return animal["type"], 1

def reducer(acc, val):
    print(val)
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = 0 + val[1] + val[1]
    print(acc)

type_animals = list(map(pick_animal_type, animals))
print(type_animals)
reduce(reducer, type_animals, {})