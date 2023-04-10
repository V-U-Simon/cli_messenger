"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

VAR_1_STR = "разработка"
VAR_2_STR = "администрирование"
VAR_3_STR = "protocol"
VAR_4_STR = "standard"

STR_LIST = [VAR_1_STR, VAR_2_STR, VAR_3_STR, VAR_4_STR]

ELEMS_B = []
for el in STR_LIST:
    el_b = el.encode("utf-8")
    ELEMS_B.append(el_b)

print(ELEMS_B)
print()

ELEMS_STR = []
for el in ELEMS_B:
    el_str = el.decode("utf-8")
    ELEMS_STR.append(el_str)

print(ELEMS_STR)


STR_LIST = [VAR_1_STR, VAR_2_STR, VAR_3_STR, VAR_4_STR]


res_encoded = [var.encode("utf-8") for var in STR_LIST]
print(res_encoded)

res_decoded = [var.decode("utf-8") for var in res_encoded]
print(res_decoded)
