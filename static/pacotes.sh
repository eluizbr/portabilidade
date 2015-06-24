#!/bin/bash

# Copyright (C) 2014 CDR-port
# cdr-port@cdr-port.net



apt-get -y update -y
apt-get -y upgrade -y
apt-get remove ajenti -y
apt-get install build-essential  -y
apt-get install python-virtualenv python-mysqldb python-dev python-imaging unzip git gunicorn mc supervisor rabbitmq-server -y
apt-get install nginx -y
export DEBIAN_FRONTEND=noninteractive
apt-get install -q -y mysql-server mysql-client libmysqlclient-dev -y
mysqladmin -u root password
apt-get clean

abbitmqctl add_user teste teste
rabbitmqctl add_vhost beta
rabbitmqctl set_permissions -p beta teste ".*" ".*" ".*"



cd /usr/share
git clone -b devel https://github.com/eluizbr/portabilidade.git
virtualenv  --no-site-packages portabilidade
cd portabilidade/
rm -rf .git*
source bin/activate
pip install -r requirements.txt
cd /usr/share/portabilidade/lib/python2.7/site-packages/registration/templates
mv registration/ registration.save





