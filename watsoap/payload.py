from json import loads


def get_payload(record, generic):
    output = None
    try:
        if record == "GENERIC":
            output = generic["payload"]
        else:
            output = record

        if len(output) > 1:
            output = loads(output)
    except:
        raise
    return output
