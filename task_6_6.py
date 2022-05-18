# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
# скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# ● просто запуск скрипта — выводить все записи;
# ● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
# этому числу, до конца;
# ● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
# первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

# скрипт записи файла
def create_txt(name1, text=None):
    with open(name1, "a", encoding="utf-8") as f:
        f.writelines(text)

import sys

command1 = sys.argv[1]
if command1 == "create_txt":
    name1 = sys.argv[2]
    txt = sys.argv[3]
    create_txt(name1, txt + "\n")

# скрипт вывода данных на экран
def read_txt1(name2):
    with open(name2, "r", encoding="utf-8") as sums:
            print(sums.read())

from itertools import islice
def read_txt2(name3, n):
    with open(name3, "r", encoding="utf-8") as fu:
        a = fu.readlines()
        for line in islice(a, n - 1, None):
            print(line.replace("\n", ""))
# read_txt2("bakery.scv", 5)  #проверка через командную строку

def read_txt3(name4, n, m):
    with open(name4, "r", encoding="utf-8") as fu:
        a = fu.readlines()
        for line in islice(a, n - 1, m):
            print(line.replace("\n", ""))
# read_txt3("bakery.scv", 5, 7)  #проверка через командную строку

command2 = sys.argv[1]
if command2 == "read_txt1":
    name2 = sys.argv[2]
    read_txt1(name2)
elif command2 == "read_txt2":
    name3 = sys.argv[2]
    n = int(sys.argv[3])
    read_txt2(name3, n)
elif command2 == "read_txt3":
    name4 = sys.argv[2]
    n = int(sys.argv[3])
    m = int(sys.argv[4])
    read_txt3(name4, n, m)