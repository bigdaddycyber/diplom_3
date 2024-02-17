import requests
import random
import string
import json


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_email():
    email = generate_random_string(10)
    return email


def generate_new_data():
    email = generate_email()
    user = generate_random_string(10)
    password = generate_random_string(10)
    return email, user, password


def generate_random_number(min_int, max_int):
    return random.randint(min_int, max_int)


def create_user():
    email, user, password = generate_new_data()
    payload = {
        "email": email,
        "password": password,
        "name": user
    }
    response = requests.post('https://stellarburgers.nomoreparties.site//api/auth/register', data=payload)
    token = response.json()["accessToken"]
    return token, email, user, password


def get_ingredients_hash():
    response = requests.get('https://stellarburgers.nomoreparties.site//api/ingredients')
    ingredients_id = []
    ingredients_data = response.json()["data"]
    for ingredient in ingredients_data:
        ingredients_id.append(ingredient["_id"])
    return ingredients_id


def get_3_random_ingredients_from_list(ingredients_id):
    ingredients = []
    for i in range(3):
        while True:
            n = generate_random_number(0, len(ingredients_id)-1)
            if ingredients_id[n] not in ingredients:
                ingredients.append(ingredients_id[n])
                break
    return ingredients


def get_incorrect_ingredient_hash(ingredients_id):
    ingredients = []
    n = generate_random_number(0, len(ingredients_id) - 1)
    ingredients.append(ingredients_id[n] + 'nnn')
    return ingredients


def create_order_for_authorized_user(token):
    ingredients_id = get_ingredients_hash()
    ingredients = get_3_random_ingredients_from_list(ingredients_id)
    payload = {"ingredients": ingredients}
    response = requests.post('https://stellarburgers.nomoreparties.site//api/orders', headers={"Authorization": token}, data=payload)
    return response.json()['order']['number']


def create_two_orders(token):
    order_numbers = [create_order_for_authorized_user(token), create_order_for_authorized_user(token)]
    return order_numbers


def login_user(access_token):
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', headers={"Authorization": access_token})
    return response.json()['refreshToken']