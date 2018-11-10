import requests
import json

my_request = requests.get('https://jsonplaceholder.typicode.com/posts/3')

# con esta opción podemos ver qué contiene el request que hicimos
print(my_request.text)

# aunque parece un diccionario de python, como verás, el tipo del objeto es un string, es decir, tenemos que parsearlo
print(type(my_request.text))
