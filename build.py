#!/usr/bin/env python

import json
import os

gcode_dictionary = []

for deffile in os.listdir('files/'):
  if deffile.endswith(".json") and not deffile.startswith('template'):
    with open('files/' + deffile) as f:
      gcode_definition = json.load(f)
      gcode_dictionary.append(gcode_definition)

with open('gcode_dictionary.json', 'w') as f:
  f.write(json.dumps(gcode_dictionary,
                     sort_keys=True,
                     indent=2,
                     separators=(',', ': ')))
