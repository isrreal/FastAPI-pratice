#!/bin/bash

ADDRESS="http://10.4.1.1:8000"
ENDPOINT=$1
curl -X GET "${ADDRESS}/${ENDPOINT}"
