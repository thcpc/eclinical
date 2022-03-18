import argparse
import os
import shutil
from ruamel import yaml


class EdkInit:
    def __init__(self):
        self.environment_path = os.path.join(os.getcwd(), "environment.yaml")

    def init_environment(self): shutil.copyfile("init_environment.yaml", self.environment_path)

    def add_envir(self, envir: str, envir_data: dict):
        with open(self.environment_path, 'r', encoding="utf-8") as f:
            data = yaml.load(f.read(), Loader=yaml.Loader)
            data["ENV"][envir] = envir_data
        with open(self.environment_path, 'w', encoding="utf-8") as f:
            yaml.dump(data, f, Dumper=yaml.RoundTripDumper)


parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化整个项目，包括生成environment.yaml，全局的conftest")
parser.add_argument("-new", action='store_true', help="新增加 environment 到 environment.yaml中 ")
args = parser.parse_args()


def edk():
    if args.init:
        EdkInit().init_environment()
    if args.new:
        data = dict()
        data["uri"] = input("请输入访问环境")
        data["user"] = input("请输入用户名")
        data["password"] = input("请输入用户名密码(如使用默认密码[Admin@123]请直接按'回车')")
        data["publick_key"] = input("加密公钥，请联系CPC或LXD索取")
        data["company"] = input("请输入公司名，如'非Cross账号' 请直接按'回车'")
        data["sponsor"] = input("请输入申办方名")
        data["study"] = input("请输入实验名，如不需要 请直接按'回车'")
        data["life_cycle"] = input("请输入项目阶段")
