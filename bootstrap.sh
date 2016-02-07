#!/usr/bin/env bash

# install required packages
apt-get update
apt-get install git

# install pip - latest version
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

# install python virtualenv
pip install virtualenv

# create virtual env and install requirements
# virtualenv /vagrant

