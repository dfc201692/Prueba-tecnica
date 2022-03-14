
from base64 import decode
import requests
import json

result = requests.get('https://www.googleapis.com/books/v1/volumes?q=harry+potter')


#print(result.status_code) #muestra el estado de la conexion a la api
#print(result.text) #muestra la data en formato json 

book =  result.json()
items = book["items"]
encoded = json.dumps(items)
decoded = json.loads(encoded)
print(decoded[0]["volumeInfo"]["title"])
print(decoded[0]["volumeInfo"]["infoLink"])


# Con esta api hace consulta en el json de titulo y url del libro 