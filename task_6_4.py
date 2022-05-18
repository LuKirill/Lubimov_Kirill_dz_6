# 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

with open("full_names.txt", 'r', encoding="utf-8") as full_name:
    f = full_name.read()
    line_1 = f.splitlines()
with open("hobbies.txt", 'r', encoding="utf-8") as hobby:
    h = hobby.read()
    line_2 = h.splitlines()

u_h = [i +": "+ j for i, j in zip(line_1, line_2)]
for n in u_h:
    print(n)

import pickle
with open("users_hobby.txt", "wb") as users_hobby:
    pickle.dump(u_h, users_hobby)
# with open ("users_hobby.txt", "rb") as users_hobby:
#     u = pickle.load(users_hobby)
#     print(u) # проверка