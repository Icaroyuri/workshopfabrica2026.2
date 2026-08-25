import requests

pokemon = input("Diga o nome do seu pokemon para saber o tipo primário: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
dados = requests.get(url).json()

print(dados['types'][0]['type']['name'])

