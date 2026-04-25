"""ЗАДАНИЕ 1: Добавление элементов в список"""
fruits = ["яблоко"]

print()
fruits.append("банан")
print(fruits)
fruits.extend(["апельсин", "груша"])
print(fruits)
fruits.insert(1, "виноград")
print(fruits)

"""ЗАДАНИЕ 2: Удаление элементов из списка"""
fruits = ["яблоко", "банан", "апельсин", "банан"]

print()
fruits.remove("банан")
print(fruits)

fruits = ["яблоко", "банан", "апельсин", "банан"]
fruit = fruits.pop()
print(fruit)

"""ЗАДАНИЕ 3: Поиск элементов в списке"""
fruits = ["яблоко", "банан", "апельсин", "банан"]

print()
print(fruits.index("банан"))
print(fruits.count("банан"))

"""ЗАДАНИЕ 4: Сортировка и реверс списка"""
numbers = [3, 1, 4, 1, 5, 9, 2]

print()
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

"""ЗАДАНИЕ 5:"""

print()
print(min([n ** 3 for n in range(1, 8)]))
print(max([n ** 3 for n in range(1, 8)]))

"""ЗАДАНИЕ 6:"""
numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]

print()
print([n for n in numbers if n > 10])
print(sum([n for n in numbers if n > 10]))

"""ЗАДАНИЕ 7:"""
cites = ["москва", "санкт-петербург", "казань"]

ci = [city.capitalize() for city in cites]
print()
print(ci)
