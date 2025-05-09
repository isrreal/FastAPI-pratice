#!/bin/bash
URL="http://10.4.1.1:8000"
CONTENT=$1   
JSON=$2    
curl -X PUT "${URL}/${CONTENT}" -H "Content-Type: application/json" -d "$JSON"

