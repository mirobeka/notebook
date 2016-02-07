#!/usr/bin/env bash

apt-get update

# install python 2.7.10
# there is problem when making hardlinks on virtualbox shared folder
# In order to be able to package with fabric, we need to use python > 2.7.9
apt-get install -y gcc-multilib g++-multilib libffi-dev libffi6 libffi6-dbg python-crypto python-mox3 python-pil python-ply libssl-dev zlib1g-dev libbz2-dev libexpat1-dev libbluetooth-dev libgdbm-dev dpkg-dev quilt autotools-dev libreadline-dev libtinfo-dev libncursesw5-dev tk-dev blt-dev libssl-dev zlib1g-dev libbz2-dev libexpat1-dev libbluetooth-dev libsqlite3-dev libgpm2 mime-support netbase net-tools bzip2
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
tar xvf Python-2.7.10.tgz
cd Python-2.7.10/
./configure --prefix /usr/local/lib/python2.7.10 --enable-ipv6
make
make install

ln -s /usr/local/lib/python2.7.10/bin/python /usr/bin/python2.7.10

# install packages for development and building python packages
apt-get install -y git python-dev

# install pip - latest version
wget https://bootstrap.pypa.io/get-pip.py
python2.7.10 get-pip.py
python get-pip.py

# install python virtualenv
pip install virtualenv

# create virtual env and install requirements
su - vagrant -c "virtualenv -p /usr/local/lib/python2.7.10/bin/python /vagrant/venv"
su - vagrant -c "/vagrant/venv/bin/pip install -r /vagrant/requirements.txt"


#TODO: fix annoying locale message
