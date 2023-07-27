#Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК
#Соберите информацию о содержимом в виде объектов namedtuple
#Каждый объект хранит:
#имя файла без расширения или название каталога,
#расширение, если это файл,
#флаг каталога,
#название родительского каталога.
#вести log сбора и сохранить его в текстовый файл.

import os
from collections import namedtuple

def gather_directory_info(directory):
    DirectoryItem = namedtuple('DirectoryItem', ['name', 'extension', 'is_directory', 'parent_directory'])

    items = []

    for item in os.scandir(directory):
        name = os.path.splitext(item.name)[0]
        extension = os.path.splitext(item.name)[1][1:] if not item.is_dir() else None
        is_directory = item.is_dir()
        parent_directory = os.path.basename(os.path.dirname(item.path))

        dir_item = DirectoryItem(name, extension, is_directory, parent_directory)
        items.append(dir_item)

    return items

def save_directory_info(directory, output_file):
    items = gather_directory_info(directory)

    with open(output_file, 'w') as file:
        for item in items:
            file.write(f"Name: {item.name}\n")
            file.write(f"Extension: {item.extension}\n") if item.extension else None
            file.write(f"Is Directory: {item.is_directory}\n")
            file.write(f"Parent Directory: {item.parent_directory}\n")
            file.write("\n")

if __name__ == "__main__":
    directory_path = input("Введите путь до директории: ")
    log_file_path = input("Введите путь до файла лога: ")

    save_directory_info(directory_path, log_file_path)