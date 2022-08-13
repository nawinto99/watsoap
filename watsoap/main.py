#!/usr/bin/python
import yaml

from watsoap.auth import get_auth_details
from watsoap.headers import get_headers
from watsoap.params import get_params
from watsoap.payload import get_payload
from watsoap.report import create_report
from watsoap.rest_api import call_api


def load_requests(config_dir):
    response = None
    try:
        with open(config_dir + "/requests.yml") as file:
            try:
                response = yaml.safe_load(file)
            except:
                raise
    except:
        raise
    return response


def load_requests_data(config_dir):
    response = None
    try:
        with open(config_dir + "/requests_data.yml") as file:
            try:
                response = yaml.safe_load(file)
            except:
                raise
    except:
        raise
    return response


def start(config_dir, env, app_config):
    try:
        final_response = []
        requests = load_requests(config_dir)
        requests_data = load_requests_data(config_dir)
        endpoints = requests["endpoints"]
        for endpoint in endpoints:
            data = requests_data[endpoint]
            base_url = data["base_url"]
            method = data["method"]
            headers = get_headers(data["headers"], requests_data["GENERIC"])
            auth = get_auth_details(data["auth_type"], data["auth_env_name"], env)
            querystring = get_params(data["params"], requests_data["GENERIC"])
            payload = get_payload(data["payload"], requests_data["GENERIC"])
            response = call_api(method, base_url, payload, headers, querystring, auth)
            final_response.append(response)
        create_report(
            final_response,
            app_config["HEALTH_REPORT_LOCATION"],
            app_config["HEALTH_REPORT_TYPE"],
        )
    except:
        raise
