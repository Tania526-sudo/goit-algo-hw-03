import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.

    :param min: Мінімальне значення діапазону (не менше 1)
    :param max: Максимальне значення діапазону (не більше 1000)
    :param quantity: Кількість чисел для генерації
    :return: Відсортований список унікальних випадкових чисел або порожній список, якщо параметри некоректні
    """
    # Перевірка вхідних параметрів
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортування результату
    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)