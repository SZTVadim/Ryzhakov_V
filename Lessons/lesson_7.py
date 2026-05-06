print('ЗАДАНИЕ 1: Работа с множествами')

fruits = {"яблоко", "банан"}

fruits.add("апельсин")
print(fruits)
fruits.update(["груша", "виноград"])
print(fruits)
fruits.discard("банан")
print(fruits)
fruits.discard("киви")
print(fruits)
# fruits.remove("киви")
fru = fruits.pop()
print(fru)

print('ЗАДАНИЕ 2: Работа с кортежами')

coordinates = (10, 20, 30, 20, 10, 20, 40)

print(coordinates[0])
print(coordinates[-1])
print(*(coordinates[2:5]))
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))

print('ЗАДАНИЕ 3: Операции с кортежами')

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]

tuple3 = tuple1 + tuple2
print(tuple3)
tuple3 = tuple1 * 3
print(tuple3)
a, b, c = tuple1
print(a, b, c)
first, *middle, last = tuple(numbers)
print(first, middle, last)
print(tuple(numbers))
print(tuple(x for x in range(11) if x % 2 == 0))
print(tuple(x ** 2 for x in range(1, 6)))
ty = 42,
print(ty)
