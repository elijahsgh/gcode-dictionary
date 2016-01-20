# Gcode Dictionary

The goal is to create a dictionary of gcode used by various fabrication machines in a common format that may be used by web applications, desktop applications, IRC bots, etc.

Contributions are welcome but please mind the scope.

Project link: https://github.com/tamarintech/gcode-dictionary

## Scope
Currently, the scope is only the Marlin, Smoothieware and Redeem platforms.

## Files
`files/` Location of each gcode item as a separate json file.

`files/Instruction.template` Basic JSON template for instructions.

`build.py` Simple python script to compile (and test validity of) each .json file in files/

`gcode_dictionary.json` The compiled dictionary.
