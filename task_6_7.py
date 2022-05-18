# 7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

def rewrite(file, n, str_new):
    with open(file, "r", encoding="utf-8") as read_file:
        line = read_file.readlines()
        try:
            line[n-1] = str_new +'\n'
        except IndexError:
            print("Такой строки нет!")
    with open(file, "w", encoding="utf=8") as save_changes:
        save_changes.writelines(line)
rewrite("bakery.scv", 1, "11")
