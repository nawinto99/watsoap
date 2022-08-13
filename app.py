#!/usr/bin/python
import json

import yaml
from dotenv import dotenv_values

from watsoap.main import start


def load_env(config_dir):
    response = None
    try:
        env_config = dotenv_values(config_dir+"/.env")
        response = json.loads(json.dumps(env_config, indent=4))
    except:
        raise
    return response

def load_app_config(config_dir):
    response = None
    try:
        with open(config_dir+"/config.yml") as file:
            try:
                response = yaml.safe_load(file)
            except:
                raise
    except:
        raise
    return response


if __name__ == "__main__":
    config_dir = "config"
    env = load_env(config_dir)
    app_config = load_app_config(config_dir)
    start(config_dir, env, app_config)
