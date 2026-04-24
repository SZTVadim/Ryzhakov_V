"""ЗАДАНИЕ 1: Работа с типами данных"""
hello = 'Привет'
num_int = 42
num_float = 3.14
my_list = [1, 2, 3]

print()
print(type(hello))
print(type(num_int))
print(type(num_float))
print(type(my_list))

"""ЗАДАНИЕ 2: Преобразование регистра строк """

st = 'python PROGRAMMING'

st_1 = st.lower()
st_2 = st.upper()
st_3 = st.capitalize()
st_4 = st.title()

print()
print(st_1)
print(st_2)
print(st_3)
print(st_4)

"""ЗАДАНИЕ 3: Удаление пробелов"""

st_space = "  Hello World  "

stsp_1 = st_space.strip()
stsp_2 = st_space.lstrip()
stsp_3 = st_space.rstrip()

print()
print(stsp_1)
print(stsp_2)
print(stsp_3)

"""ЗАДАНИЕ 4: Разделение и объединение строк"""

fruits = "яблоко,банан,апельсин,груша"

fruits_l = fruits.split(",")
fruits_s = " | ".join(fruits_l)

print()
print(fruits_l)
print(fruits_s)

"""ЗАДАНИЕ 5: Замена подстрок"""

st_py = "Я изучаю Python. Python - это круто!"
st_ja = st_py.replace("Python", "Java")

print()
print(st_ja)

"""ЗАДАНИЕ 6: Поиск и подсчет"""

st_p = "Python программирование на Python"

print()
print(st_p.find('Python'))
print(st_p.count('Python'))
print(st_p.find('Java'))

"""ЗАДАНИЕ 7: Проверка типа символов"""

print()
print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

"""ЗАДАНИЕ 8: Срезы строк"""

pvg = "Python very good"

print()
print(pvg[:3])
print(pvg[-3:])
print(pvg[1::2])
print(pvg[::-1])

"""ЗАДАНИЕ 9: Экранирование символов"""

print()
print("Он сказал: \"Привет\"")
print("Первая строка \nВторая строка")
