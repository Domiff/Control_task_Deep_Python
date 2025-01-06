# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.


from datetime import datetime, timedelta


def calculate_days(count_days):

    future_date = datetime.now() + timedelta(days=count_days)
    return future_date.strftime('%Y-%m-%d')

def main():
    days = int(input("Введите количество дней: "))
    future_date = calculate_days(days)
    print(f"Дата через {days} дней: {future_date}")

main()