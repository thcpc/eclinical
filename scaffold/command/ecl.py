import argparse
import os
import shutil

from scaffold.files.service import Service

parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化一个module，包括生成environment.yaml，全局的conftest")


class Ecl:

    def __init__(self, name):
        self.name = name
        self.ecl_folder = os.path.join(os.getcwd(), self.name)

    def init_module(self):
        if os.path.exists(self.ecl_folder): raise Exception("请勿重复创建")
        os.mkdir(self.ecl_folder)

    def add_service(self, service_names: str, app: str):
        for service_name in service_names.split(","):
            service = Service(service_name, app)
            # 输出到service.py
            self.rewrite_file("services", service.file_name, service.output_service_py()) \
            or self.new_file("services", service.file_name, service.output_service_py())
            # 输出到 __init__.py
            self.append_file("services", "__init__.py", service.output_init_py()) \
            or self.new_file("services", "__init__.py", service.output_init_py())
            # 输出到 conftest.py
            self.append_file("", "conftest.py", service.output_conftest_py()) \
            or self.new_file("", "conftest.py", service.output_conftest_py())

    def rewrite_file(self, sub_folder, file_name, content):
        if self.file_exist(sub_folder, file_name):
            re_write = input(f"{file_name} 已存在,是否覆盖(Y/N)")
            if re_write.lower() == 'Y':
                with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'w', encoding="utf-8") as f:
                    f.write(content)
            return True
        return False

    def new_file(self, sub_folder, file_name, content):
        with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'w', encoding="utf-8") as f:
            f.write(content)
        return True

    def append_file(self, sub_folder, file_name, content):
        if self.file_exist(sub_folder, file_name):
            with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'a', encoding="utf-8") as f:
                f.write(content)
            return True
        return False

    def file_exist(self, sub_folder, file_name):
        return os.path.exists(os.path.join(self.ecl_folder, sub_folder, file_name))
