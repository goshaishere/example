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


class StreamIt:

    def __init__(self):
        self.event_path = "task_folder\\event"
        self.schema_path = "task_folder\\schema"

        # это список жсонов
        self.storage_json_names = []
        # это содержимое жсонов
        self.storage_json_content = []

        # это список схем
        self.storage_schema_names = []
        # это содержимое схем
        self.storage_schema_content = []

    def get_names(self):
        for dir_path, subdir_list, name_list in os.walk(self.event_path):
            self.storage_json_names = name_list

    def collect_content(self):
        for i in self.storage_json_names:
            json_name = str(i)
            im_here = os.getcwd()
            path_loco = os.path.join(self.event_path, json_name)
            path = os.path.join(im_here, path_loco)
            with open(path) as file:
                data = json.load(file)
                result = [json_name, data]
                self.storage_json_content.append(result)


    def get_names_0(self):
        for dir_path, subdir_list, name_list in os.walk(self.schema_path):
            self.storage_schema_names = name_list

    def collect_content_0(self):
        for i in self.storage_schema_names:
            name = str(i)
            im_here = os.getcwd()
            path_loco = os.path.join(self.schema_path, name)
            path = os.path.join(im_here, path_loco)
            with open(path) as file:
                for data in file:
                    data = Schema(data)
                    result = [name, data]
                    self.storage_schema_content.append(result)

    def analyse(self):
        for name_schema, data_schema in self.storage_schema_content:
            for name_json, data_json in self.storage_json_content:
                validated = data_schema.is_valid(data_json)
                data_json = dict(data_json)
                for key, value in data_json.items():
                    print(key)
                    print(value)



    def go(self):
        self.get_names()
        self.collect_content()

        self.get_names_0()
        self.collect_content_0()

        self.analyse()


test = StreamIt()
test.go()
