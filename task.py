#
# Вам предлагается задача на умение отлаживать данные и предоставлять результат в человеко-понятном виде.
# Задание
#
# В архиве есть две папки
#
# Одна с JSON файлами.
# Вторая папка с JSON схемами для файлов из первой. Часть схем 100% правильных, часть нет.
#
# Необходимо написать скрипт, который сможет найти максимальное количество ошибок структуры и данных в первой папке.
#
# Примечание: часть ошибок может быть связано с JSON схемой, может с самими данными и ключами для них.
#
# В результате работы скрипта, надо показать какие файлы не валидны, какие там ошибки
# и для каждой ошибки на человеко-понятном языке указать как данные исправить.
# Вывод скрипта положить в файл (логом или html таблицей), который сможет прочитать не разработчик.
# Ожидаемый результат
#
# В результате тестового задания ожидается:
#
# Ссылка на gitlab/github репозиторий с реализацией скрипта, в котором будет содержать README файл с результатом
# работы скрипта в виде, пригодном для прочтения не-разработчиками.
#

import os
from schema import Schema, And, Use, Optional
import json
from pprint import pprint
import io


class StreamIt:
    def __init__(self):


        # контейнер для жсонов и относительный путь к папке с JSON
        self.event_path = "task_folder\\event"
        self.json_names_list = []

        self.json_dicts = {}

        # список для ключей жсонов
        self.list_json_keys = []

        # список для имен схем и относительный путь к SCHEMA
        self.storage_schema_names = []
        self.schema_path = "task_folder\\schema"

        # шаблоны
        self.storage_schema_content = []
        # файл для вывода
        self.output_filename = 'README.txt'

        # добываем имена файлов
        for dir_path, subdir_list, name_list in os.walk(self.event_path):
            self.json_names_list = name_list
        for dir_path, subdir_list, name_list in os.walk(self.schema_path):
            self.storage_schema_names = name_list

    def json_0(self):
        file = open(file=self.output_filename, mode='w', encoding='utf-8')
        file.close()

        for i in self.json_names_list:
            json_name = str(i)
            im_here = os.getcwd()
            path_loco = os.path.join(self.event_path, json_name)
            path = os.path.join(im_here, path_loco)
            with open(path) as file:
                    data = json.load(file)
                    type_loco = str(type(data))
                    x = "<class 'NoneType'>"
                    if type_loco == x:
                        """перед continue добавить запись об ошибке типа, не читается json"""
                        file = open(file=self.output_filename, mode='a', encoding='utf-8')
                        text_0 = str(i)
                        file.write(text_0)
                        text = " - данный JSON не читается"
                        file.write(text)
                        text_1 = "\n"
                        file.write(text_1)
                        file.close()
                        continue

                    keys_loco = []
                    for key, value in data.items():
                        print(key)
                        keys_loco.append(key)

                    a = []
                    if keys_loco == a:
                        """нет ключей, записать в лог"""
                        file = open(file=self.output_filename, mode='a', encoding='utf-8')
                        text_0 = str(i)
                        file.write(text_0)
                        text = " - в данном JSON ключей не обнаружено"
                        file.write(text)
                        text_1 = "\n"
                        file.write(text_1)
                        file.close()
                        continue

                    print(keys_loco)
                    self.json_dicts.update({i: keys_loco})

        #
        # len_0 = len(self.json_dicts)
        # len_1 = len(self.json_names_list)
        # print(len_0, self.json_dicts)
        # print(len_1, self.json_names_list)

    def schema_0(self):
        for i in self.storage_schema_names:
            name = str(i)
            im_here = os.getcwd()
            path_loco = os.path.join(self.schema_path, name)
            path = os.path.join(im_here, path_loco)
            with open(path) as file:
                for data in file:
                    data = Schema(data)
                    # print(type(data))
                    # print(data)
                    result = [name, data]
                    self.storage_schema_content.append(result)

        # for i in self.storage_schema_content:
        #     pprint(i)

    def printer(self):
        pass

    def go(self):
        self.json_0()
        self.schema_0()



test = StreamIt()
test.go()
