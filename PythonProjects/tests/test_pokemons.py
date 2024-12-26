import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ca562380f315b8ee6829cfd402008925'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12625'

def test_status_code_and_trainer_id():
    # Выполнение запроса
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    
    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Преобразование ответа в JSON
    response_json = response.json()
    
    # Проверка, что ответ содержит данные
    assert "data" in response_json, "Response does not contain 'data' field"
    
    # Проверка, что trainer_id присутствует в data
    trainers = [item.get("trainer_id") for item in response_json.get("data", [])]
    assert TRAINER_ID in trainers, f"Expected 'trainer_id' to be {TRAINER_ID}, but got {trainers}"