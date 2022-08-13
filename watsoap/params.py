#!/usr/bin/python
from json import loads


def get_params(record, generic):
    output = None
    try:
        if record == "GENERIC":
            output = generic["params"]
        else:
            output = record

        if len(output) > 1:
            output = loads(output)
    except:
        raise
    return output
