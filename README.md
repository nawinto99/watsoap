# WATSOAP
[![CodeQL](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/nawinto99/gitoxy/actions/workflows/codeql-analysis.yml)


WATSOAP (What's The Status Of API) is a API health-checking monitoring tool

![gitoxy](./docs/assets/watsoap.png)


# Purpose
The purpose of this tool is to automatically monitor the health of APIs. Manually monitoring the health of APIs is a time-consuming and painful task.

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
1. **config.yml**: This file contains information about the application configuration.
2. **.env**: This file contains the Tokens, API keys, usernames and passwords, and other sensitive information.
3. **requests.yml** : This file contains a list of requests, and the request's name should be unique in the list.
4. **requests_data.yml** : This file contains the data required to initiate each request. Create one dictionary object for each request, and the name should exactly match the name mentioned in step one.

### Update **config.yml**
1. The names of the keys must be distinct.
2. It is recommended to use capital letters and underscores for separate words.
3. The following keys should be updated
   - ***HEALTH_REPORT_LOCATION***: The location where the health status reports will be stored.
   - ***HEALTH_REPORT_TYPE***: Health status report format. Select one of the following options.
        - CSV
        - JSON

###### Sample:
```
LOG_FILE_LOCATION: ~/logs/watsoap/
HEALTH_REPORT_LOCATION: ~/logs/watsoap/
HEALTH_REPORT_TYPE: CSV
```

### Update **.env**
1. The names of the environmental variables must be distinct.
2. It is recommended to use capital letters and underscores for separate words.

###### Sample:
```
DOMAIN=example.org
ADMIN_EMAIL=admin@${DOMAIN}
BASIC_AUTH_GENERIC= { "user_name":"dummy_user", "password":"dummypassword"}
MOCKBIN= { "user_name":"sample", "password":"sample"}

```
### Update **requests.yml**
1. Create the list and map key name as **endpoints** .
2. The name of the request should be unique in the list.
3. It is recommended to use capital letters and underscores for separate words.

###### Sample:

```
endpoints:
  - MOCKBIN
  - JSON_PLACE_HOLDER
```
### Update **requests_data.yml**
1. Create one dictionary object for each request, and the map key name should exactly match with the request name.
2. For each dictionary object create following keys
    - **base_url[MANDATORY]**: Complete API URL Path.
    - **method[MANDATORY]**: The HTTP request method to perform the desired action on a given resource. [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
    - **headers[OPTIONAL]**: Custom HTTP headers.
    - **payload[OPTIONAL]** Request payload.
    - **params[OPTIONAL]**: Request query strings.
    - **auth_type[MANDATORY]**: To access the resources, choose one of the following authentication types. 
            - NO-AUTH
            - BASIC
            - API-KEY
    - **auth_env_name[OPTIONAL]**: The name of the authentication environment variable should exactly match the name of the environment variable created in the.env file.


###### Sample:

```
GENERIC:
  doc: >
    This is the generic section where requests fetch the common data for all APIs.
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


# Run the application

```
$ chmod +x run.sh
$ ./run.sh
```


