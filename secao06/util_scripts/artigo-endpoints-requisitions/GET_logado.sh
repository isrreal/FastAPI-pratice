#!/bin/bash

curl -i -X GET http://192.168.1.112:8000/api/v1/usuarios/logado \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ3MzMxNjQ2LCJpYXQiOjE3NDY3MjY4NDYsInN1YiI6IjE4In0.pVydeh66CC7lembyYV8Uwqq_eeSaSjv0BIvo1ruen1M"

