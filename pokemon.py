import requests

pokemon = input("Diga o nome do seu pokemon para saber o tipo primário: ")
try:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    dados = requests.get(url).json()

    print(dados['types'][0]['type']['name'])
    print(dados['types'][1]['type']['name'])

except:
    print("Pokemon não encontrado")

