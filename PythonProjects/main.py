import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ca562380f315b8ee6829cfd402008925'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

# боди создания покемона
body_create = {
    "name": "Бульбазавр",
    "photo_id": 3
}

# боди смены имени покемона
body_new_name = {
    "pokemon_id": "171351",
    "name": "Новое имя",
    "photo_id": 3
}

#боди поимки покемона
body_ad_pokebol = {
    "pokemon_id": "171351"
}

# создаем покемона
response_create = requests.post(url= f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.json())

# смена имени покемона
pesponse_put_name = requests.put(url= f'{URL}/pokemons', headers=HEADER, json=body_new_name)
print(pesponse_put_name.json())

# моймать покемона
response_ad_pokebol = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_ad_pokebol)
print(response_ad_pokebol.json())
