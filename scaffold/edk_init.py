import argparse
import os
import shutil
from ruamel import yaml

from elements.life_cycle import LifeCycle
from scaffold.elements.pass_word import PassWord


class EdkInit:
    def __init__(self):
        self.environment_path = os.path.join(os.getcwd(), "environment.yaml")

    def init_environment(self):
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "init_environment.yaml"), self.environment_path)

    def add_envir(self, envir: str, envir_data: dict):
        with open(self.environment_path, 'r', encoding="utf-8") as f:
            data = yaml.load(f.read(), Loader=yaml.Loader)
            data["ENV"][envir] = envir_data
        with open(self.environment_path, 'w', encoding="utf-8") as f:
            yaml.dump(data, f, Dumper=yaml.RoundTripDumper)


parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化整个项目，包括生成environment.yaml，全局的conftest")
parser.add_argument("-new", action='store_true', help="新增加 environment 到 environment.yaml中 ")
parser.add_argument("-no_db", action='store_true', help="不需要配置数据库")
args = parser.parse_args()


def default_by_enter(*, value):
    def __wrapper__(func):
        def __inner__(msg: str):
            user_input = func(msg)
            return value if user_input == "" else user_input

        return __inner__

    return __wrapper__


@default_by_enter(value="Admin@123")
def password_input(msg: str): return input(msg)


@default_by_enter(value="")
def company_input(msg: str): return input(msg)


@default_by_enter(value="")
def study_input(msg: str): return input(msg)


@default_by_enter(value=3306)
def db_port_input(msg: str): return input(msg)


def edk():
    if args.init:
        # TODO 在已有environment.yaml 提示已生成，命令非法
        EdkInit().init_environment()
    if args.new:
        data = dict()
        # TODO environment 非空 且 位移
        envir = input("请输入 environment 名\n")
        # TODO 内置环境
        data["uri"] = input("请输入访问环境\n")
        # TODO 非空
        data["user"] = input("请输入用户名\n")
        data["password"] = PassWord.input("请输入用户名密码", "Admin@123", "回车")
        # password_input("请输入用户名密码(如使用默认密码[Admin@123]请直接按'回车')\n")
        data["publick_key"] = input("加密公钥，请联系CPC或LXD索取\n")
        data["company"] = company_input("请输入公司名，如'非Cross账号' 请直接按'回车'\n")
        # TODO 非空
        data["sponsor"] = input("请输入申办方名\n")
        data["study"] = study_input("请输入实验名，如不需要 请直接按'回车'\n")
        data["life_cycle"] = LifeCycle.input()
        if not args.no_db:
            data["db"] = dict()
            # TODO 内置环境
            data["db"]["host"] = input("请输入数据库主机\n")
            # TODO 非空
            data["db"]["user"] = input("请输入访问数据库的用户名\n")
            data["db"]["pwd"] = PassWord.input("请输入数据库密码")
            # input("请输入访问密码\n")
            # TODO 非空
            data["db"]["database"] = input("请输入访问数据库的schema\n")
            data["db"]["port"] = db_port_input("请输入访问端口号，如使用默认端口(3306), 请按'回车'\n")
            EdkInit().add_envir(envir, data)


if __name__ == '__main__':
    edk()
