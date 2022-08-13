### **WATSOAP**

_WATSOAP (What's The Status Of API) is a API health-checking monitoring tool._

![alt text](./assets/watsoap.png){ align=right }

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

## Modify Configuration

1. Modify the configuration file

   > watsoap/config/requests.yml

## Run the application

```
$ cd watsoap
$ ./run.sh
```
