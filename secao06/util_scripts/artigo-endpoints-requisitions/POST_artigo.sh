curl -i -X POST http://192.168.1.112:8000/api/v1/artigos/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzQ3MzQxMTIwLCJpYXQiOjE3NDY3MzYzMjAsInN1YiI6IjEifQ.4yC5CT2zzgxyr5QpKuoVzEAepqPxG0QZLEoWWipeXVA" \
  -d '{
    "titulo": "Primeiro Artigo",
    "descricao": "Somente um artigo",
    "url_fonte": "https://www.geekuniversity.com.br"
}'
