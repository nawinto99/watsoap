# WATSOAP
[![CodeQL](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml)


WATSOAP (What's The Status Of API) is a API health-checking monitoring tool

![gitoxy](./docs/assets/watsoap.png)


# Purpose
Manually monitoring the health of APIs is a time-consuming and painful task. This tool purpose is to automatically monitor the health of APIs.

# Features
- Collects the current health status of configured APIs.
- Generates the health status reports in a variety of file formats.

# Prerequisite

- Install [git](https://git-scm.com/), If it is already installed, ignore it.
- Install [Python](https://www.python.org/), If it is already installed, ignore it.
- If [Poetry](https://python-poetry.org/docs/) is not already installed on your local machine, proceed as follows.
```
    $ python -m pip install --upgrade pip
    $ pip install poetry
```

# Setup 

## With GIT

1. Clone this repository to your local machine.

```
    $ git https://github.com/nawinto99/watsoap.git
```

2. Change the working directory as follows.
```
    $ cd watsoap
```
3. Run following command which will install the necessary dependencies.

```
    $ poetry install
```
4. Rename the .env.dummy file in the config folder to .env.

# Usage

## Update the below configuration files in the config folder

1. requests.yml -> Stores the list of requests to perform health checks.
2. requests_data.yml -> Stores the information needed to trigger the API
3. .env -> Stores the senstive information like 



1. Modify the requests configuration file, add list of endpoint names to mintor the health.

   > /config/requests.yml

#### Example:

```
    endpoints: [ 
      "MOCKBIN", "JSON_PLACE_HOLDER"
    ]
```
2. Modify the requests data configuration file. Make sure to match the endpoint names as mentioned in step #1. For each endpoint, create following list of keys. If you have common data for multiple endpoints, declare the GENERIC path and mention value as GENERIC to refer the value from GENERIC for each endpoint.

   > /config/requests_data.yml

- **base_url:** _Endpoint URL._
- **method:** _Request method type._
- **payload:** _Request Payload._
- **params:** _Request Query Strings._
- **auth_type:** _Authentication types, select one from following list **['NO-AUTH','BASIC', 'API-KEY'].**_
- **auth_env_name:** _Authentication Environment Variable name, refer step #3 for more details._

#### Example:

```
GENERIC:
  doc: >
    This is generic section where endpoints picks the common information for all the API endpoints
  payload: |
    {
    "body": "bar",
    "userId": 1
    }
  headers: |
    {
    "Content-Length": "253",
    "Content-Type": "application/json",
    "x-pretty-print": "2"
    }

JSON_PLACE_HOLDER:
  base_url: "https://jsonplaceholder.typicode.com/posts"
  method: "POST"
  headers: |
    {
      "Content-type": "application/json; charset=UTF-8"
    }
  payload: |
    {
    "title": "foo",
    "body": "bar",
    "userId": 1
    }
  params: ""
  auth_type: "BASIC"
  auth_env_name: "BASIC_AUTH_GENERIC"

MOCKBIN:
  base_url: "http://mockbin.com/request"
  method: "POST"
  headers: "GENERIC"
  payload: |
    {
    "foo": "bar"
    }
  params: |
    {
    "foo":["bar","baz"]
    }
  auth_type: "BASIC"
  auth_env_name: "MOCKBIN"
```
3. Modify the environmental configuration file, create the environmental variable name as same as mentioned in step #2, auth_env_name .
    > /config/.env
    
#### Example:

```
DOMAIN=example.org
ADMIN_EMAIL=admin@${DOMAIN}
ROOT_URL=${DOMAIN}/app
BASIC_AUTH_GENERIC= { "user_name":"ddvdv", "password":"pppp"}
MOCKBIN= { "user_name":"ddvdv", "password":"pppp"}

```

## Run the application

```
$ cd watsoap
$ chmod +x run.sh
$ ./run.sh
```

