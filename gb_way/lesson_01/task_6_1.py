"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но отерыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""

with open("test_file.txt", "w", encoding="utf-8") as t_f:
    t_f.write("сетевое программирование\n")
    t_f.write("сокет\n")

with open("test_file.txt", encoding="utf-8") as t_f:
    for each_line in t_f:
        print(each_line, end="")
