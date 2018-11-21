#!/bin/bash

VIRTUAL_ENV="env"

echo "Checking for existing virtual environment"
if [[ ! -d "$VIRTUAL_ENV" ]]; then
    echo 'No virtual environment found!'
    echo "creating virtual environment $VIRTUAL_ENV "
    python3 -m venv env
else
    echo "virtual environment found!"
fi

echo "activating virtual environment"
source env/bin/activate
pip install --upgrade setuptools
echo "installing requirements"
pip install -r requirements.txt
echo "Running tests"
python -m unittest discover tests/ "test_*.py"
echo "Running sim"
python main.py 123456
echo "deactivating virtual environment"
deactivate
