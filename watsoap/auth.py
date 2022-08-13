from json import loads

from requests.auth import HTTPBasicAuth


def get_auth_details(auth_type, auth_env_name, env):
    output = None
    try:
        if auth_type == "BASIC":
            auth_detials = loads(env[auth_env_name])
            output = HTTPBasicAuth(auth_detials["user_name"], auth_detials["password"])
    except:
        raise
    return output
