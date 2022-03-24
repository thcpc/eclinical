import argparse
import os

from scaffold.files.gen_service import Service, GenService
from scaffold.inputs.application import Application
from scaffold.inputs.ecl.module_name import ModuleName
from scaffold.inputs.ecl.module_service import ModuleService
from scaffold.inputs.ecl.module_type import ModuleType
from scaffold.template.file_operate import FileOperate

parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化一个module，包括生成environment.yaml，全局的conftest")
parser.add_argument("-ns", action='store_true', help="执行初始化module时，如果带这个参数，表明创建Module 同时创建 service")
args = parser.parse_args()


class Ecl:

    def __init__(self, name=None, module_type=None):
        self.name = name
        self.module_type = module_type
        self.ecl_folder = os.path.join(os.getcwd(), f'{self.name}_{self.module_type}')

    def init_module(self):
        if os.path.exists(self.ecl_folder): raise Exception("请勿重复创建")
        os.mkdir(self.ecl_folder)
        os.mkdir(os.path.join(self.ecl_folder, "services"))
        os.mkdir(os.path.join(self.ecl_folder, "meta"))
        os.mkdir(os.path.join(self.ecl_folder, "ext"))
        FileOperate(self.ecl_folder).new_file("", "__init__.py", "")
        if self.module_type == "testcase":
            FileOperate(self.ecl_folder).new_file("", "conftest.py", Service.output_conftest_header_py())

    # def add_service(self, service_names: str, app: str):
    #     for service_name in service_names.split(","):
    #         service = Service(service_name, app)
    #         # 输出到service.py
    #         if not os.path.exists(os.path.join(self.ecl_folder, "services")): os.mkdir(
    #             os.path.join(self.ecl_folder, "services"))
    #         self.rewrite_file("services", service.file_name + ".py", service.output_service_py()) \
    #         or self.new_file("services", service.file_name + ".py", service.output_service_py())
    #         # 输出到 __init__.py
    #         self.append_file("services", "__init__.py", service.output_init_py()) \
    #         or self.new_file("services", "__init__.py", service.output_init_py())
    #         # 输出到 conftest.py
    #         self.append_file("", "conftest.py", service.output_conftest_py()) \
    #         or self.new_file("", "conftest.py", service.output_conftest_py())
    #
    # def rewrite_file(self, sub_folder, file_name, content):
    #     if self.file_exist(sub_folder, file_name):
    #         re_write = input(f"{file_name} 已存在,是否覆盖(Y/N)")
    #         if re_write.lower() == 'Y':
    #             with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'w', encoding="utf-8") as f:
    #                 f.write(content)
    #         return True
    #     return False
    #
    # def new_file(self, sub_folder, file_name, content):
    #     with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'w', encoding="utf-8") as f:
    #         f.write(content)
    #     return True
    #
    # def append_file(self, sub_folder, file_name, content):
    #     if self.file_exist(sub_folder, file_name):
    #         with open(os.path.join(self.ecl_folder, sub_folder, file_name), 'a', encoding="utf-8") as f:
    #             f.write(content)
    #         return True
    #     return False
    #
    # def file_exist(self, sub_folder, file_name):
    #     return os.path.exists(os.path.join(self.ecl_folder, sub_folder, file_name))

# TODO 增加Meta的命令
def ecl_command():
    if args.init:
        ecl = Ecl(ModuleName.input(), ModuleType.input())
        ecl.init_module()
        if args.ns:
            for service_name in ModuleService.input():
                gen = GenService(ecl.ecl_folder)
                gen.add_service(service_name, Application.input(msg=f"{service_name}是什么系统"))
                # ecl.add_service(service_name, Application.input(msg=f"{service_name}是什么系统"))


if __name__ == '__main__':
    ecl_command()
