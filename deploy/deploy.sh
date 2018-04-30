#!/bin/bash

cp nginx.conf /etc/nginx/conf.d/bits-server.conf
cp nginx.conf /etc/nginx/sites-available/bits-server

cp supervisord.conf /etc/supervisor/conf.d/bits-server.conf
