import json

f = open("aquerium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]