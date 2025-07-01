import json

with open("voos.json") as f:
    data = json.load(f)

top_voos = data["best_flights"]

print("-"*10 + "top voos" + "-"*10)
print(top_voos)
