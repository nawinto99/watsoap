#!/usr/bin/python
from requests import request


def call_api(method, base_url, payload, headers, querystring, auth):
    """Call the API endpoint"""
    res = {}
    res["base_url"] = base_url

    try:
        response = request(
            method,
            base_url,
            data=payload,
            headers=headers,
            params=querystring,
            auth=auth,
        )

        res["status"] = response.reason
        res["status_code"] = response.status_code
        res["response_time_seconds"] = response.elapsed.total_seconds()

    except:
        res["status"] = "Not Found"
        res["status_code"] = 404
        res["response_time_seconds"] = 0
        pass

    return res
