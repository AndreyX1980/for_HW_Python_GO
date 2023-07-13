#Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
#Результаты обхода сохраните в файлы json, csv и pickle.
#Для дочерних объектов указывайте родительскую директорию.
#Для каждого объекта укажите файл это или директория.
#Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle

def get_directory_info(directory_path):
    results = []

    for root, dirs, files in os.walk(directory_path):
        #определяем размер директории и всех вложенных файлов и папок
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        dir_size += sum(os.path.getsize(os.path.join(root, dir)) for dir in dirs)

        #Обход файлов
        for file in files:
            file_path = os.path.join(root, file)
            file_info = {
                "filename": file,
                "type": "file",
                "size": os.path.getsize(file_path)
            }
            results.append(file_info)

        #Обход директорий
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_info = {
                "dirname": dir,
                "type": "directory",
                "size": dir_size
            }
            results.append(dir_info)

    return results

def save_results_to_files(results, directory_path):
    #Сохранение в JSON
    json_path = os.path.join(directory_path, "results.json")
    with open(json_path, "w") as file:
        json.dump(results, file, indent=4)

    #Сохранение в CSV
    csv_path = os.path.join(directory_path, "results.csv")
    with open(csv_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Type", "Size (bytes)"])
        for item in results:
            if item["type"] == "file":
                writer.writerow([item["filename"], item["type"], item["size"]])
            else:
                writer.writerow([item["dirname"], item["type"], item["size"]])

    #Сохранение в pickle
    pickle_path = os.path.join(directory_path, "results.pickle")
    with open(pickle_path, "wb") as file:
        pickle.dump(results, file)

directory_path = "/path/to/directory"  #укажите путь к целевой директории
results = get_directory_info(directory_path)
save_results_to_files(results, directory_path)