#!/bin/bash

cp /srv/bits-server/deploy/nginx.conf /etc/nginx/sites-available/bits-server
cp /srv/bits-server/deploy/supervisord.conf /etc/supervisor/conf.d/bits-server.conf
