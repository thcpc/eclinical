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
            # TODO 输出到 service.py
            # TODO 输出到 conftest
            # TODO 输出到 init.py
            with open(os.path.join(self.ecl_folder, service.file_name), 'w', encoding="utf-8") as f:
                service.output_service_py()
