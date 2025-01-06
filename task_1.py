# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.


import logging


logger1 = logging.getLogger('logger1')
logger2 = logging.getLogger('logger2')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler1 = logging.FileHandler('log/debug_info.log')
file_handler2 = logging.FileHandler('log/warnings_errors.log')

file_handler1.setFormatter(formatter)
file_handler2.setFormatter(formatter)

logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.WARNING)

logger1.addHandler(file_handler1)
logger2.addHandler(file_handler2)

logger1.info("Все пучком")
logger1.debug("Нужно отдебажить код")

logger2.warning("Есть недочетность, но работать будет")
logger2.error("Нужно исправить код, имеются ошибки")
logger2.critical("Программа сломана")
