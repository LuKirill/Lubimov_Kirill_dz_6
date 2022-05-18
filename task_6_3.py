# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

# создать 2 файла: ФИО и хобби
# формируем словарь из строк 2х файлов ФИО и хобби
# сделать записть с помощью json в новый файл ФИО: {хобби}
# если хобби закончились раньше вывод None, если ФИО вывод "1"

def create_txt(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        f.writelines(text)

if __name__ == "__main__":
    create_txt("full_names.txt",
    """Иванов, Иван, Иванович
Петров, Петр, Петрович
Сидоров, Александр, Сидоров
Третьяков, Алексей, Юрьевич
Седов, Владимир, Ильич""")

    create_txt("hobbies.txt",
    """скалолазание, охота
горные лыжи
мтб, бег""")


# def read_txt(name):
#     with open(name, "r", encoding="utf-8") as some_txt:
#         f = some_txt.read()
#         line = f.splitlines()
#         return line
# read_txt("full_names.txt")
# read_txt("hobbies.txt")

# из функции read_txt вытащить аргумент line для отдельного файла не получается,
# поэтому переписал скрипт на открытие файлов "full_names.txt" и "hobbies.txt" без функции
    with open("full_names.txt", 'r', encoding="utf-8") as full_name:
        f = full_name.read()
        line_1 = f.splitlines()
    with open("hobbies.txt", 'r', encoding="utf-8") as hobby:
        h = hobby.read()
        line_2 = h.splitlines()

    from itertools import zip_longest
    dict_names = dict(zip_longest(line_1, line_2, fillvalue=None)) if len(line_1) >= len(line_2) else dict(zip_longest(line_1, line_2, fillvalue="1"))
    print(dict_names)

    import json
    with open("users.json", "w") as users:
        json.dump(dict_names, users)
    with open("users.json") as users:
        f = json.load(users)
    print(f)