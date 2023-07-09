#Напишите функцию группового переименования файлов
#принимать в качестве аргумента желаемое конечное имя файлов
#При переименовании в конце имени добавляется порядковый номер
#принимать в качестве аргумента расширение исходного файла
#принимать в качестве аргумента расширение конечного файла

import os

def batch_rename_files(directory, new_name, extension, new_extension):
    counter = 1  # Порядковый номер
    for filename in os.listdir(directory):
        if filename.endswith(extension):  # Проверка на расширение исходного файла
            original_name = os.path.splitext(filename)[0]  # Получение оригинального имени файла (без расширения)
            new_filename = f"{original_name}_{new_name}_{counter}.{new_extension}"
            counter += 1  # Увеличение порядкового номера
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# тест
directory = 'путь_к_директории'
new_name = 'новое_имя'
extension = 'исходное_расширение'
new_extension = 'конечное_расширение'
batch_rename_files(directory, new_name, extension, new_extension)