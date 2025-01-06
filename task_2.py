# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году


from datetime import datetime


time = datetime.now()
format_time = time.strftime("Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года")
print(time)
print(format_time)