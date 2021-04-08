#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requiretest.txt


python3 -m pytest --cov=Service1 --cov-report=term-missing
python3 -m pytest --cov=Service2 --cov-report=term-missing
python3 -m pytest --cov=Service3 --cov-report=term-missing
python3 -m pytest --cov=Service4 --cov-report=term-missing