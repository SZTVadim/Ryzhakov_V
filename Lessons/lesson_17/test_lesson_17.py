from Lessons.lesson_17.lesson_17_crud import create_pet, get_pet, put_pet, delete_pet


def test_create_pet():
    try:
        pet = create_pet()
        assert pet.status_code == 200, f"Ожидали статус код 200, получили {pet.status_code}"
        assert "id" in pet.json(), f"Ожидали, что ключ id находится внутри {pet.json()} "
        assert isinstance(pet.json()["id"], int), f"Ожидали получить Id питомца в виде int а, получили {pet.json()['id']}"
    finally:
        delete_pet(pet.json()["id"])


def test_get_pet(id_pet):
    pet = get_pet(id_pet)
    assert pet.status_code == 200, f"Ожидали статус код 200, получили {pet.status_code}"
    assert "id" in pet.json(), f"Ожидали, что ключ id находится внутри {pet.json()} "
    assert isinstance(pet, int), f"Ожидали получить Id питомца в виде int а, получили {pet.json()['id']}"


def test_put_pet(id_pet):
    pet = put_pet(id_pet)
    assert pet.status_code == 200, f"Ожидали статус код 200, получили {pet.status_code}"
    assert isinstance(pet.json(), dict)
    assert "Cat" == pet.json()["category"]["name"], f"Ожидали получить Cat, получили {pet.json()["category"]["name"]}"


def test_delete_pet(id_pet):
    response = delete_pet(id_pet)
    assert response.status_code == 200, f"Ожидали статус код 200, получили {response.status_code}"
    response_get_pet = get_pet(id_pet)
    assert response_get_pet.status_code == 404, f"Ожидали статус код 404, получили {response_get_pet}"
