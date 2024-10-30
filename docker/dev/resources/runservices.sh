#!/bin/bash

/usr/sbin/nginx -g 'daemon off;' &
gunicorn -c /resources/gunicorn.py wsgi:api
