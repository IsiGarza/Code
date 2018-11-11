#Construye un iterador (for Loop) que consuma el índice de
#los posts https://jsonplaceholder.typicode.com/posts/ e imprima todos los títulos de los posts.
import requests
import json

my_request = requests.get('https://jsonplaceholder.typicode.com/posts/')

parsed = json.loads(my_request.text)

for request in parsed:
    print((request['id']),':',(request['title']))
