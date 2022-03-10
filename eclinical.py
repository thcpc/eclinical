import os
import argparse

SERVICE_CLASS = """
import cjen
from eclinical import {application_service}, Environment
class {service_name}({application_service}):
    def __init__(self, environment: Environment):
        super().__init__(environment)
"""

READ_ME = """
# 用例描述
描述该用例测试内容
# 实现
描述如何实现该用例
# 注意
执行用例中需要注意点
# 启动
启动的py文件
# 是否加入Jenkins 自动执行
"""

OK_RESPONSE = """
import cjen
from cjen import MetaJson


class OKResponse(MetaJson):
    @cjen.operate.asserts.equal(value=200)
    @cjen.operate.json.one(json_path="$.procCode")
    def procCode(self): ...
"""


def clazz_name(name: str):
    return "".join([elem.capitalize() for elem in name.split("_")])


def login_service(name: str):
    login = dict(etmf="ETMFLoginService", pv="PVLoginService", ctms="CTMSLoginService", edc="EdcLoginService",
                 iwrs="IWRSLoginService", design="DesignLoginService", portal="PortalLoginService",
                 portaladmin="PortalAdministratorLoginService").get(name.lower())
    if login is None: raise Exception(f"不支持 {name} ")
    return login


class Scaffold(object):

    def __init__(self, name: str, services: list[str], application: str, append_action:bool=False):
        self.name = name
        self.services = services
        self.application = application
        self.append_action = append_action

    def generate_read_me(self):
        with open(os.path.join(self.name, "README.md"), "w") as f:
            f.write(READ_ME)

    def generate_meta(self):
        os.mkdir(os.path.join(self.name, "meta"))
        with open(os.path.join(self.name, "meta", "ok_response"), "w") as f:
            f.write(OK_RESPONSE)

    def generate_conftest(self):
        with open(os.path.join(self.name, "conftest.py"), "w") as f:
            f.write("import pytest\n")
            f.write("from eclinical import Environment\n")
            for service_name in self.services:
                f.write(f"from service.{service_name} import {clazz_name(service_name)}\n")
                f.write("@pytest.fixture \n")
                f.write(f"def {service_name}(ef,st)\n")
                f.write(f"\treturn {clazz_name(service_name)}(Environment(envir=st, file_path=ef)))")

    def generate_test_case(self):
        os.mkdir(self.name)
        self.generate_meta()
        self.generate_services()
        self.generate_read_me()
        self.generate_conftest()

    def init(self):
        os.mkdir(os.path.join(self.name, "service"))
        with open(os.path.join(self.name, "service", "__init__.py"), "w") as f:
            for service_name in self.services:
                f.write(f"from {service_name} import {clazz_name(service_name)}\n")
                with open(os.path.join(self.name, "service", f"{service_name}.py"), "w") as sf:
                    sf.write(SERVICE_CLASS.format(service_name=service_name, application_service=login_service()))
    def append_service(self): pass

    def execute(self):
        if not self.append_action: pass
        else: self.init()

parser = argparse.ArgumentParser()
parser.add_argument("--t", type=str, required=True, help="用例的名字")
parser.add_argument("-a", action='store_true', help="在已有的用例中,增加service,需添加该参数")
parser.add_argument("-m", action="store_true", help="是否在meta文件夹中创建service文件夹")
parser.add_argument("--app", type=str, required=True,
                    help="service为哪个系统[edc,design,etmf,pv,ctms,portal,portaladmin,iwrs]")
parser.add_argument("--s", type=str,
                    help="创建的service文件, 命名规则'xx_service', 如果有多个的话,以','间隔\n "
                         "例子: crf_page_service,dataset_page_service",
                    default="")
args = parser.parse_args()

if __name__ == '__main__':
    print(args.t)
    print(args.s)
    print(args.app)
    print(args.a)
