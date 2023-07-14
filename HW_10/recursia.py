#возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
#Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

import os
import json
import csv
import pickle


class DirectoryInfo:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.results = []
        self.json_path = os.path.join(directory_path, "results.json")
        self.csv_path = os.path.join(directory_path, "results.csv")
        self.pickle_path = os.path.join(directory_path, "results.pickle")

    def analyze_directory(self):
        for root, dirs, files in os.walk(self.directory_path):
            dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
            dir_size += sum(os.path.getsize(os.path.join(root, dir)) for dir in dirs)

            for file in files:
                file_path = os.path.join(root, file)
                file_info = {
                    "filename": file,
                    "type": "file",
                    "size": os.path.getsize(file_path)
                }
                self.results.append(file_info)

            for dir in dirs:
                dir_info = {
                    "dirname": dir,
                    "type": "directory",
                    "size": dir_size
                }
                self.results.append(dir_info)

    def save_results_to_files(self):
        #сохранение в json
        with open(self.json_path, "w") as file:
            json.dump(self.results, file, indent=4)

        #сохранение в csv
        with open(self.csv_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Type", "Size (bytes)"])
            for item in self.results:
                if item["type"] == "file":
                    writer.writerow([item["filename"], item["type"], item["size"]])
                else:
                    writer.writerow([item["dirname"], item["type"], item["size"]])

        #сохранение в pickle
        with open(self.pickle_path, "wb") as file:
            pickle.dump(self.results, file)