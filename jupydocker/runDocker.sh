#!/bin/bash

docker run \
-it \
--name jupy \
--net=sk \
-p 18888:8888 \
-v /opt/sanickube/shdir/:/opt/sanickube/shdir/ \
jupycentos:1.5 \
/bin/bash

