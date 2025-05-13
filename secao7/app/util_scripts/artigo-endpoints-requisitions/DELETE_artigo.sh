#!/bin/bash

# trocando o nsobrenome da felicity

curl -i -X DELETE http://192.168.1.112:8000/api/v1/usuarios/$1 \
  -H "Content-Type: application/json" \
