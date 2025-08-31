import re

def normalize_phone(phone_number: str) -> str:
    """
    Повертає номер у форматі: +380XXXXXXXXX
    Правила:
    - лишаємо лише цифри (усі інші символи прибираємо)
    - якщо номер починається з 380 -> просто додаємо '+'
    - якщо номер починається з 0 (локальний) -> додаємо префікс '+38'
    - інакше (наприклад '50...' без нуля) -> теж додаємо '+38'
    """
    digits = re.sub(r"\D", "", phone_number or "")

    if digits.startswith("380"):
        return f"+{digits}"
    elif digits.startswith("0"):
        return f"+38{digits}"
    else:
        return f"+38{digits}"


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
