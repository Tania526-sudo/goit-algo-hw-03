import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до стандартного міжнародного формату для SMS-розсилки.
    
    :param phone_number: Номер телефону в довільному форматі
    :return: Нормалізований номер у форматі +380XXXXXXXXX
    """
    # Видаляємо всі символи, крім цифр і +
    cleaned = re.sub(r'[^\d+]', '', phone_number)

    # Якщо починається з '+', перевіряємо чи це український номер
    if cleaned.startswith('+'):
        if not cleaned.startswith('+38'):
            # Якщо міжнародний, але не український — залишаємо як є
            return cleaned
        return cleaned  # вже у форматі +380...

    # Якщо починається з '380' — додаємо лише '+'
    if cleaned.startswith('380'):
        return '+' + cleaned

    # Якщо починається з 0 або просто 9 цифр — додаємо '+38'
    if cleaned.startswith('0') or len(cleaned) == 9:
        return '+38' + cleaned.lstrip('0')  # забираємо 0, якщо є

    # Якщо не відповідає жодному з умов — додаємо просто '+38' перед числом
    return '+38' + cleaned


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
