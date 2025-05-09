#!/bin/bash

curl -i -X GET http://192.168.1.112:8000/api/v1/usuarios/logado \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ3MzQwMzc4LCJpYXQiOjE3NDY3MzU1NzgsInN1YiI6IjEifQ.JeMyEHvSEZAkAFhWFSzNkJp5R734phty50DOpN7Ue3o"

