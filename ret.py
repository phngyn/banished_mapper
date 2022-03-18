# source ./.env/Scripts/active
# Screenshots: C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots
# ls 'C:\Program Files (x86)\Steam\userdata\86585210\760\remote\242920\screenshots\' > fn.txt
# ls ./map > fn.txt

import os
import json

def mapper(filename):
    mapped = {}
    with open(filename) as f:
        lines = f.read().splitlines()
        mapped = dict(zip(lines[::2],lines[1::2]))
    return mapped

def export_json(dictionary):
    json_object = json.dumps(dictionary,indent=4)
    with open('mappings.json', 'w') as outfile:
        json.dump(json_object, outfile)

if __name__ == '__main__':

    with open('mappings.json', 'r+') as file:
        mapping = json.load(file)
        # print(len(mapping))
        new_maps = mapper('fn.txt')
        new_mapping = mapping | new_maps
        # print(len(new_mapping))
        json.dump(new_mapping, file)
