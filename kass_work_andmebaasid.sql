import json

json_data = '{"nimi":"David Lennuk", "vanus":100, "prillid":true}'
data=json.loads(json_data)

print(data)
print(data["nimi"])
for id_,dat in enumerate(data):
    print(id_,"-",dat)


for key, value in data.items():
    print(key,":",value)

data2={
    "nimi":"Mark",
    "vanus":25,
    "abielus":True,
    "lapsed":("Mark","Alina"),
    "koduloomad":None,
    "autod":
    [
        {"muudel":"BMW","varv":"punane","joud":500,"number":"123ABC"},
        {"muudel":"Ford","varv":"must","joud":300,"number":"321CBA"}
     ]
    }
print(json.dumps(data2))
print(json.dumps(data2,indent=2,separators=(".","="),sort_keys=True))
with open("data_file.json","w") as w_file:
    json.dump(data2,w_file)

print("Andmed failist:")
with open("data_file.json","r") as r_file:
    data2=json.load(r_file)

print(data2)
