from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між заданою датою та поточною датою.
    
    :param date: Рядок у форматі 'РРРР-ММ-ДД', наприклад '2025-08-30'
    :return: Ціле число — кількість днів між поточною датою та заданою
             (від’ємне значення, якщо задана дата в майбутньому)
    :raises: ValueError, якщо формат дати неправильний
    """
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Очікується 'РРРР-ММ-ДД'.")


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))  