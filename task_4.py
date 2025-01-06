# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.


import argparse


def main():

    parser = argparse.ArgumentParser(description='Скрипт для обработки числа и строки.')

    parser.add_argument('number', type=int, help='Введите целое число')
    parser.add_argument('string', type=str, help='Введите строку')

    parser.add_argument('--verbose', action='store_true', help='Показать подробную информацию')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')

    args = parser.parse_args()

    number = args.number
    string = args.string
    verbose = args.verbose
    repeat = args.repeat

    if verbose:
        print(f'Вы ввели число {number}')
        print(f'Вы ввели строку "{string}"')

    for _ in range(repeat):
        print(string)


if __name__ == "__main__":
    main()
