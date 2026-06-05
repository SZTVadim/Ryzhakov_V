# ЗАДАНИЕ 1: Декоратор

def log_execution(func):
    def wrapper(a, b):
        print('Функция запущена')
        result = func(a, b)
        print('Функция завершена')
        return result
    return wrapper


@log_execution
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 3))


# ЗАДАНИЕ 2: @property и @classmethod

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.__price = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Ошибка: цена не может быть отрицательной!")
        elif value > 10000:
            print("Ошибка: максимальная цена 10000 рублей!")
        else:
            self.__price = value

    @classmethod
    def create_from_string(cls, book_str):
        title, author = book_str.split('|')
        return cls(title, author)

    def get_info(self):
        return f"Книга '{self.title}' автор {self.author}, цена {self.price} руб."


book1 = Book("1984", "Оруэлл")
book2 = Book.create_from_string("Мастер и Маргарита|Булгаков")
book1.price = 500
book2.price = 750
book1.price = -100
book1.price = 15000
print(book1.get_info())
print(book2.get_info())


def find_log_entries(type_mistake: str):
    with open("data_test/application.log") as file:
        for line in file:
            if type_mistake in line:
                print(line)


find_log_entries("ERROR")
