#!/usr/bin/python3

"""
IO module
"""

import sys

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
items = []

# Create the file if it doesn't exist
with open(filename, 'a') as f:
    pass

with open(filename, 'r') as f:
    content = f.read()
    if content != "":
        items = load(filename)

items += sys.argv[1:]

save(items, filename)
