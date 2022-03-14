from email import header
from urllib import request, response
import requests
import json

if __name__ == '__main__':
    url = 'https://www.googleapis.com/auth/books'  
    payload ={'nombre': 'David','curso':'python','nivel':'intermedio'}
    header = {'Content-Type': 'aplication/json','access-token': '12345'}

    response = requests.post(url, data=json.dumps(payload), headers=header)

    print(response)

    if response.status_code == 200:
       print(response.content)
      # headers_response = response.headers #Diccionario
      # server =  headers_response['Server']
      # print(server)


