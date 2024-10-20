import os
import time

for root, dirs, files in os.walk('.'):
    # print(roots)
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)

        # print(file)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, '
            f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
