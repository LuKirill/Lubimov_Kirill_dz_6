# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

# Нужен список из IP
# найти большее число повторений IP
# найти количество IP

id_list = []
with open("nginx_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        remote_addr = line.split(" - - ")[0]
        id_list.append(remote_addr)
    # print(id_list)

set_id_list = set(id_list)
spammer_id = None
qty_requests = 0
for item in set_id_list:
    qty = id_list.count(item)
    if qty > qty_requests:
        qty_requests = qty
        spammer_id = item
print(spammer_id)
print(qty_requests)