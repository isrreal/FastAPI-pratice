#!/bin/bash
URL=$1
JSON=$2
curl -X POST "$URL" -H "Content-Type: application/json" -d @$JSON

