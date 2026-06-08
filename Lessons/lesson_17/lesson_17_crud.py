import requests

BASE_URL = 'https://petstore.swagger.io/'
ENDPOINT_1 = 'v2/pet'
HEADERS = {"accept": "application/json"}


def receive_json_for_create(id_pet, category_id_pet, category_name_pet, pet_name, photo_pet, tags_id, personality_pet, status):
    return {"id": id_pet,
            "category": {"id": category_id_pet, "name": category_name_pet},
            "name": pet_name, "photoUrls": [photo_pet],
            "tags": [{"id": tags_id, "name": personality_pet}],
            "status": status
            }


photo_pet_1 = "https://avatars.mds.yandex.net/i?id=754577ce633ab29ea7ccdbd056f1dc28ffaed6c7-16467138-images-thumbs&ref=rim&n=33&w=120&h=180"
photo_pet_2 = "https://avatars.mds.yandex.net/i?id=6d1c911b8dc680c20870908e9549c45c89489102-5858835-images-thumbs&n=13"

data = receive_json_for_create(24051989, 7, "Cat", "Tishka", photo_pet_1, 7, "friendly", "pending")


def create_pet():
    response_create_pet = requests.post(url=f"{BASE_URL}{ENDPOINT_1}", headers=HEADERS, json=data)
    return response_create_pet


def get_pet(id_pet):
    response_get_pet = requests.get(url=f"{BASE_URL}{ENDPOINT_1}/{id_pet}", headers=HEADERS)
    return response_get_pet


def put_pet(id_pet):
    update_pet_data = receive_json_for_create(id_pet, 6, "Cat", "Cat", photo_pet_2, 6, "agressive", "available")
    response_put_pet = requests.put(url=f"{BASE_URL}{ENDPOINT_1}", headers=HEADERS, json=update_pet_data)
    return response_put_pet


def delete_pet(id_pet):
    response_del_pet = requests.delete(url=f"{BASE_URL}{ENDPOINT_1}/{id_pet}", headers=HEADERS)
    return response_del_pet
