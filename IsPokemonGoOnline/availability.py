import json

a = json.loads(open("available.json","r").read().replace('\'','"'))
print a["timeout"]
