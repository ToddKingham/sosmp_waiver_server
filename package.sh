#!/bin/bash

mkdir temp && cp *.py temp
pip3 install -r requirements.txt -t ./temp
cd temp && zip -r -X "../../sosmp_waiver_server.zip" .
cd ../ && rm -rf temp