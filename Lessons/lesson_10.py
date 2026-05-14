# ЗАДАНИЕ 1: Функции и условия

def calculate_total(price, tax_percent):
    if tax_percent > 20 or price < 0:
        return f"Ошибка! {tax_percent} > 20 % или возможно {price} < 0"
    else:
        return price, tax_percent


print((calculate_total(10, 21)))


def get_level(points):
    if type(points) is int or type(points) is float:
        if points >= 100:
            print("Эксперт")
        elif points >= 50:
            print("Продвинутый")
        elif points >= 20:
            print("Начинающий")
        else:
            print("Новичок")
    else:
        print(f"Ошибка! {points} не является числом")


get_level('17.2')


# ЗАДАНИЕ 2: Функции с условиями и match/case

def process_status(status):
    match status:
        case "active":
            print("Статус активен")
        case "inactive":
            print("Статус неактивен")
        case "pending":
            print("Статус в ожидании")
        case "blocked":
            print("Статус заблокирован")
        case _:
            print("Неизвестный статус")


process_status("status")
