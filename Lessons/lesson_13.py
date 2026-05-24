# ЗАДАНИЕ: Система управления животными в зоопарке

# ЧАСТЬ 1: Абстракция - Абстрактный класс Animal

from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        """Простая система управления животными"""
        pass


# ЧАСТЬ 2: Наследование - Классы Dog и Cat

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} говорит: Гав-гав!')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} говорит: Мяу!')


# ЧАСТЬ 3: Инкапсуляция - Класс Zoo (Зоопарк)


class Zoo:
    def __init__(self, name):
        self.__animals = []
        self.name = name

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)


# ЧАСТЬ 4: Полиморфизм - Работа с разными животными


def animal_sound(animal):
    animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)


zoo = Zoo("Городской зоопарк")

zoo.add_animal(Dog("Бобик", 3))
zoo.add_animal(Dog("Шарик", 5))
zoo.add_animal(Cat("Мурка", 2))

print(zoo.get_animals_count())

for animal in zoo._Zoo__animals:
    animal.make_sound()

animal_sound(Dog('Рекс', 6))

# Наш объект Animal попадает в функцию animal_sound
# После, он инициализируется в классе Animal
# Далее идёт вызов функции make_cound в классе Animal
# Затем, в зависимости от животного выполняется наследованный класс
