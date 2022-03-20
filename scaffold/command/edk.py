import argparse
import os
import shutil

from ruamel import yaml

from scaffold.elements.account import Account
from scaffold.elements.company import Company
from scaffold.elements.db_host import DBHost
from scaffold.elements.eclinical_uri import EclinicalUri
from scaffold.elements.environment_name import EnvironmentName
from scaffold.elements.life_cycle import LifeCycle
from scaffold.elements.pass_word import PassWord
from scaffold.elements.port import Port
from scaffold.elements.schema import Schema
from scaffold.elements.sponsor import Sponsor
from scaffold.elements.study import Study

parser = argparse.ArgumentParser()
parser.add_argument("-init", action='store_true', help="初始化整个项目，包括生成environment.yaml，全局的conftest")
parser.add_argument("-new", action='store_true', help="新增加 environment 到 environment.yaml中 ")
parser.add_argument("-no_db", action='store_true', help="不需要配置数据库")
args = parser.parse_args()


class Edk:
    def __init__(self):
        self.environment_path = os.path.join(os.getcwd(), "environment.yaml")

    def init(self):
        shutil.copyfile(os.path.join(os.path.dirname(__file__), "resource", "init_environment.yaml"), self.environment_path)
        self.generate_conftest()

    # TODO 生成 conftest
    def generate_conftest(self): pass

    def add_environment(self, name: str, environment: dict):
        with open(self.environment_path, 'r', encoding="utf-8") as f:
            environments = yaml.load(f.read(), Loader=yaml.Loader)
            environments["ENV"][name] = environment
        with open(self.environment_path, 'w', encoding="utf-8") as f:
            yaml.dump(environments, f, Dumper=yaml.RoundTripDumper)

    def environment_exist(self, name):
        with open(self.environment_path, 'r', encoding="utf-8") as f:
            environments = yaml.load(f.read(), Loader=yaml.Loader)
            return environments["ENV"].get(name) is not None

    def exist(self): return os.path.exists(self.environment_path)

    @property
    def eclinical_serve(self):
        return {"113": "http://200.200.101.113/api",
                "97": "http://200.200.101.97/api",
                "115": "http://200.200.101.115/api",
                "38": "http://200.200.101.38/api",
                "us_dev": "https://ec.eclinical-dev.edetekapps.com/api",
                "us_prod": "https://ec.eclinical.edetekapps.com/api",
                "us_demo4": "",#TODO 添加地址
                "shenkang_prod": "https://crip-ec.shdc.org.cn/api"}


def edk_command():
    edk = Edk()
    if args.init:
        if edk.exist(): raise Exception("已初始化，请勿重复初始化")
        edk.init()
    if args.new:
        if not edk.exist(): raise Exception("请先执行-init 初始化，再执行-new")
        data = dict()
        environment_name = EnvironmentName.input(edk)
        data["uri"] = EclinicalUri.input(edk)
        data["user"] = Account.input()
        data["password"] = PassWord.input("请输入用户名密码", "Admin@123", "回车")
        data["publick_key"] = input("加密公钥\n")
        data["company"] = Company.input("请输入公司名", "非Cross账号", "回车")

        data["sponsor"] = Sponsor.input()
        data["study"] = Study.input("请输入实验名", "ctms, pv, etmf", "回车")
        data["life_cycle"] = LifeCycle.input()
        if not args.no_db:
            data["db"] = dict()

            data["db"]["host"] = DBHost.input()
            data["db"]["user"] = Account.input()
            data["db"]["pwd"] = PassWord.input("请输入数据库密码")

            data["db"]["database"] = Schema.input()
            data["db"]["port"] = Port.input("请输入访问端口号", 3306, "回车")
            edk.add_environment(environment_name, data)


if __name__ == '__main__':
    edk_command()