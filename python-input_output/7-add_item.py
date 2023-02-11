#!/usr/bin/python3
"""comment Module"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
