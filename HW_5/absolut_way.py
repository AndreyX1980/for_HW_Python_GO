import os

def split_filepath(filepath):
    path, full_filename = os.path.split(filepath)
    filename, ext = os.path.splitext(full_filename)
    return path, filename, ext

result = split_filepath('вставьте сюда полный путь')

print(result)