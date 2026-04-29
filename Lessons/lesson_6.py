print()
print("ЗАДАНИЕ 1: Работа со словарями и перебор элементов")

data = {"имя": "Иван", "возраст": 20, "курс": 2, "город": "Москва"}
print()

print(data)
all_keys = list(data.keys())
print(all_keys)
all_values = list(data.values())
print(all_values)
print()

for key, value in data.items():
    print(f"{key}:", value)

print()

for value in data.values():
    print(value)

print()

print("ЗАДАНИЕ 2: Удаление элементов и генератор словарей")
print()
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}

del prices["груша"]
print(prices)
price_grape = prices.pop("виноград")
print(price_grape)
print()

prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}

prices2 = {key: value * 0.9 for key, value in prices.items()}
print(prices2)
print()

print("ЗАДАНИЕ 3: Объединение словарей")
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

student1.update(student2)
print(student1)
print(student2)
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}

student3 = {key: value for key, value in student1.items()}

for key, value in student2.items():
    if key not in student3:
        student3[key] = value
    else:
        old_value = student3[key]
        student3[key] = [old_value, value]
print(student3)
