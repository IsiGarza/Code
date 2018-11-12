#Escribe un iterador (for loop) que haga interpolación o concatenación de strings por la totalidad
#de los posts (son 100 posts). Debes concatenar el URL de index más los números del 1 al 100
#y haz un request para cada uno, e imprime el título del post.
import requests
import json

my_request = requests.get('https://jsonplaceholder.typicode.com/posts/')

parsed = json.loads(my_request.text)

for request in parsed:
    id = str(request['id'])
    url_id = 'https://jsonplaceholder.typicode.com/posts/' + id
    print((request['id']),':',url_id)
    print(request['title'])
