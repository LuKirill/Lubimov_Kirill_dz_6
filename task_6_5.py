# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

import sys
import os
def create_txt(old_name, new_name):
    os.rename(old_name, new_name)

command = sys.argv[1]
if command == "write_txt":
    old_name = sys.argv[2]
    new_name = sys.argv[3]
    create_txt(old_name, new_name)
# не уверен, что правильно понял условие, сделал скрипт с возможностью менять имя файлов в командной строке