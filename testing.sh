#! /bin/bash
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requiretest.txt


python3 -m pytest --cov=. --cov-report=missing-term