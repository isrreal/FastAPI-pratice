#!/bin/bash

curl -i -X POST http://192.168.1.112:8000/api/v1/usuarios/signup \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Israel",
    "sobrenome": "Souza",
    "email": "israel@gmail.com",
    "senha": "12345",
    "eh_admin": false 
}'

