import argparse
import os

from scaffold.files.service import Service
from scaffold.inputs.application import Application
from scaffold.inputs.ecl.module_name import ModuleName
from scaffold.inputs.ecl.module_service import ModuleService
from scaffold.inputs.ecl.module_type import ModuleType

parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化一个module，包括生成environment.yaml，全局的conftest")
args = parser.parse_args()


class Ecl:

    def __init__(self, name, module_type):
        self.name = name
        self.module_type = module_type
        self.ecl_folder = os.path.join(os.getcwd(), f'{self.name}_{self.module_type}')

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


# TODO 增加单独增加Service的命令
# TODO 增加Meta的命令
def ecl_command():
    if args.init:
        ecl = Ecl(ModuleName.input(), ModuleType.input())
        ecl.init_module()
        for service_name in ModuleService.input():
            ecl.add_service(service_name, Application.input(msg=f"{service_name}是什么系统"))
