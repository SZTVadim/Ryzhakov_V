# ЗАДАНИЕ 1: Класс Book (Книга)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"Название книги: {self.title} \nАвтор книги: {self.author} \nКоличество страниц в книге: {self.pages}"

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


Book1 = Book("Никогда не говори Никогда", "Рыжаков Вадим Анатольевич", 300)
print(Book1.get_info())
print(Book1.is_long())

Book2 = Book("Война и Мир", "Толстой Лев Николаевич", 301)
print(Book2.get_info())
print(Book2.is_long())

Book3 = Book("Мёртвые Души", "Гоголь Николай Васильевич", 350)
print(Book3.get_info())
print(Book3.is_long())

# ЗАДАНИЕ 2: Класс BankAccount (Банковский счёт)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Ваш депозит пополнен на сумму {amount}'

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return "Недостаточно средств"

    def get_balance(self):
        return self.balance


Account = BankAccount('Вадим Рыжаков', 100000)
print(Account.deposit(100))
print(Account.get_balance())
print(Account.withdraw(100000))
print(Account.withdraw(100100))
print(Account.get_balance())
