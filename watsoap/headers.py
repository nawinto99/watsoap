from json import loads


def get_headers(record, generic):
    output = None
    try:
        if record == "GENERIC":
            output = generic["headers"]
        else:
            output = record

        if len(output) > 1:
            output = loads(output)
    except:
        raise
    return output
