#!/usr/bin/python3
"""
Here is some documentation
"""
import json
def save_to_json_file(my_obj, filename):
    """Here is some more documentation"""
    with open(filename, "w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))