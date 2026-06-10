import pytest

from Lessons.lesson_17.lesson_17_crud import create_pet


@pytest.fixture
def id_pet():
    return create_pet().json()["id"]
