#!/usr/bin/python3
"""
Here is some documentation
"""
import json
def load_from_json_file(filename):
    """Here is some more documentation"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.loads(f.read())