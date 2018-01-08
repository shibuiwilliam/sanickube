#!/bin/bash

docker run \
-it \
--name sanic \
--net=sk \
-p 18000:8000 \
-v /opt/sanickube/shdir/:/opt/sanickube/shdir/ \
sanicentos:1.2 \
python /opt/sanickube/shdir/webserver/sanicbase.py

