#!/bin/bash

curl -i -X POST http://192.168.1.112:8000/api/v1/usuarios/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=israel@gmail.com&password=12345"
