# with open('hello.txt', "r", encoding="utf-8") as file_1:
# # a = file_1.readline()
# # while a:
# #     print(a)
# #     a = file_1.readline()
# # file_1.close()
#
#     for i in file_1:
#         print(i)
# # file_1.close()
#
# txt_lines = ["Пробуем записать текст в файл.",
# "Используем метод .writelines()."]
# with open("writelines_method.txt", "w", encoding="utf-8") as f:
#     f.writelines(txt_lines)
#
# with open("writelines_method.txt", "r", encoding="utf-8") as f:
#     for i in f:
#         print(i)

# txt = """Пробуем записать текст в файл.
# Используем метод "а"
# """
# with open("append_text.txt", "a", encoding="utf-8") as f:
#     f.write(txt)

# txt = """Пробуем записать текст в файл.
# Используем МЕТОД
# """
# with open("replace_text_1.txt", "r+", encoding="utf-8") as f:
#     f.write(txt)
# #
# txt = """Пробуем дозаписать файл в текст.
# Режим доступа 'r+'
# """
# with open("replace_text_2.txt", "r+", encoding="utf-8") as f:
#     f.write(txt)
#
# txt = """Пробуем дозаписать файл в текст.
# Режим ДОСТуПа в файл
# """
# with open("replace_text_2.txt", "r+", encoding="utf-8") as f:
#     f.write(txt)

# txt = """Учимся читать файлы.
# Можем установить указатель в нужную позицию.
# Начало - 0.
# Можно отсчитывать от конца файла.
# """

# with open("hello_2.txt", "r", encoding="utf-8") as f:
#     # f.write(txt)
#     print(f.tell())
#     line = f.readline()
#     while line:
#         print(line.strip(), f.tell(), sep="\n")
#         line = f.readline()


# import json
# import requests
#
# response = requests.get("http://jsonplaceholder.typicode.com/todos")
# todos = json.load(response.text)
#
# print(todos[:10])
# data = {
#     "president": {
#         "name": "Donald Trump"
#     }
# }
# with open('data_file.json') as write_file:
#     f = write_file.read()
#     data_file = json.loads(f)
# print(data_file)
s = "Python is interesting"
a = bytes(s, "utf-8")
print(a)

size = 5
a = bytes(size)
print(a)

rlist = [1, 2, 3, 4, 5]
a = bytes(rlist)
print(a)