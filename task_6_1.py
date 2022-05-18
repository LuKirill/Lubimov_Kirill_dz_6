# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

# my_file = open("nginx_log.txt", "w")
# my_file.close()

def my_tuple(file):
    with open("nginx_log.txt", "r", encoding="utf-8") as f:
        for line in f:
            remote_addr = line.split(" - - ")[0]
            request_typ_ = line.split(' "')[1]
            request_typ = request_typ_.split(" /")[0]
            requested_resource = request_typ_.split()[1]
            yield (remote_addr, request_typ, requested_resource)

a = my_tuple("nginx_log.txt")
for s in a:
    print(s)
    print(type(s))