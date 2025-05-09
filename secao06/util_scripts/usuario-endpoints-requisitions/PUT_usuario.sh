#!/bin/bash

# trocando o nsobrenome da felicity

curl -i -X PUT http://192.168.1.112:8000/api/v1/usuarios/2 \
  -H "Content-Type: application/json" \
  -d '{
    "sobrenome": "Sychev",
    "eh_admin": true
}'

