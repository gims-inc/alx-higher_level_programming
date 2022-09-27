#!/usr/bin/python3
"""JSON to Object function."""
import json



def from_json_string(my_str):
    """Return python object Representationof a JSON string."""
    return json.loads(my_str)
