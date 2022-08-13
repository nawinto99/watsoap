# WATSOAP
[![CodeQL](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml)


WATSOAP (What's The Status Of API) is a API health-checking monitoring tool

![gitoxy](./docs/assets/watsoap.png)

# Getting started

## Prerequisites

- Install [git](https://git-scm.com/)
- Install [Python](https://www.python.org/)

## Installation

### with git

1. Clone repository to your local

```
    $ git https://github.com/nawinto99/watsoap.git
```

1. Ensure [poetry](https://python-poetry.org/docs/) is installed, if not follow below.

```
    $ cd watsoap
    $ python -m pip install --upgrade pip
    $ pip install poetry
```

1. Install dependencies and start your virtualenv:

```
    $ poetry install
    $ poetry shell
```

# Usage

## Modify Configuration Files

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
    > rename the .env.dummy to .env 
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

