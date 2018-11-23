# page-replacer
[![Build Status](https://semaphoreci.com/api/v1/projects/7626629a-e7c6-405b-beaa-07a487b13fb2/2353908/badge.svg)](https://semaphoreci.com/grantslape-61/page-replacer)
[![CodeFactor](https://www.codefactor.io/repository/github/grantslape/page-replacer/badge)](https://www.codefactor.io/repository/github/grantslape/page-replacer)

Implementation and comparison of several page replacement algorithms:
* FIFO: First in, first out
* LRU: Least recently used
* OPT: Optimal Replacement

[![Plot Image](https://i.imgur.com/QP978ez.png)]

## Dependencies
* Python \>=3.4

## Usage

```shell
$ ./run.sh
``` 

Please note that installation of requirements packages can take some time, so go grab a coffee.

## Advanced Usage

1) Create virtual environment
    
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
    
2) Install requirements (Takes some time)
    
    ```shell
    $ pip install --upgrade setuptools
    $ pip install -r requirements.txt
    ```

1) Run tests
    ```shell
    $ python -m unittest discover tests/ "test_*.py"
    ```
3) Run simulation
    ```shell
    $ python main.py <SEED> [--frames <MAX_FRAMES]
    ```
4) Deactivate environment
    ```shell
    $ deactivate
    ```