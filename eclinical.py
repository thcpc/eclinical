import os
import argparse
from typing import IO

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


class Service:
    def __init__(self, service_name, app):
        self.service_name = service_name
        self.app = app

    @property
    def name(self): return f"{self.service_name}_service"

    @property
    def application(self): return self.app

    def output_conftest_py(self, f: IO):
        f.write(f"from service.{self.name} import {clazz_name(self.name)}\n\n\n")
        f.write("@pytest.fixture \n")
        f.write(f"def {self.name}(ef, st):\n")
        f.write(f"\treturn {clazz_name(self.name)}(Environment(envir=st, file_path=ef))\n\n\n")

    def output_init_py(self, f: IO):
        f.write(f"from {self.name} import {clazz_name(self.name)}\n")

    def output_service_py(self, f: IO):
        f.write("""
import cjen
from eclinical import {application_service}, Environment


class {service_name}({application_service}):
    def __init__(self, environment: Environment):
        super().__init__(environment)
""".format(service_name=clazz_name(self.name),
           application_service=login_service(self.application)))

    @classmethod
    def factory(cls, services: str, application: str) -> list:
        if services and len(services) != 0:
            return [Service(service, application) for service in services.split(",")]
        return []


class InitPy:
    def __init__(self, services: list[Service]):
        self.services = services

    def output(self, f: IO):
        for service in self.services:
            service.output_init_py(f)


class ConfTest:
    def __init__(self, services: list[Service]):
        self.services = services

    def output(self, f: IO, action: str):
        if action == "w":
            f.write("import pytest\n")
            f.write("from eclinical import Environment\n")
        for service in self.services:
            service.output_conftest_py(f)


class ReadMe:

    def __init__(self):
        self.content = """
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

    def output(self, f: IO):
        f.write(self.content)


class Scaffold(object):

    def __init__(self, name: str, services: list[Service], append_action: bool = False):
        self.name = name
        self.services = services
        self.init_py = InitPy(self.services)
        self.conftest = ConfTest(self.services)
        self.read_me = ReadMe()

        self.append_action = append_action

    def generate_read_me(self):
        with open(os.path.join(self.name, "README.md"), "w", encoding="utf-8") as f:
            self.read_me.output(f)

    def generate_meta(self):
        os.mkdir(os.path.join(self.name, "meta"))
        with open(os.path.join(self.name, "meta", "ok_response.py"), "w") as f:
            f.write(OK_RESPONSE)

    def init_conftest(self):
        with open(os.path.join(self.name, "conftest.py"), "w") as f:
            self.conftest.output(f, "w")

    def append_conftest(self):
        with open(os.path.join(self.name, "conftest.py"), "a") as f:
            self.conftest.output(f, "a")

    def generate_test_case(self):
        os.mkdir(self.name)
        self.generate_meta()
        self.init_service()
        self.generate_read_me()
        self.init_conftest()

    def init_service(self):
        if not os.path.exists(os.path.join(self.name, "service")):
            os.mkdir(os.path.join(self.name, "service"))
        self.write_init(mode="w")
        for service in self.services:
            self.write_service(service, 'w')

    def write_service(self, service: Service, mode: str):
        with open(os.path.join(self.name, "service", f"{service.name}.py"), mode) as f:
            service.output_service_py(f)

    def write_init(self, mode: str):
        with open(os.path.join(self.name, "service", "__init__.py"), mode) as f:
            self.init_py.output(f)

    def append_service(self):
        if not os.path.exists(self.name): raise Exception(f" 无用例{self.name} 的目录")
        for service in self.services:
            if os.path.exists(os.path.join(self.name, "service", f"{service.name}.py")):
                action = input(f"{service.name}已存在,是否覆盖(y/n)?")
                if 'y' != action.lower() and 'n' != action.lower(): raise Exception("非法输入,请输入y/n")
                if 'n' == action: continue
            else:
                self.write_init(mode='a')
                self.append_conftest()
            self.write_service(service, mode='w')

    def execute(self):
        if self.append_action:
            self.append_service()
        else:
            self.generate_test_case()


class ScaffoldGM(object):
    def __init__(self, name: str, service: str, meta_type: str, meta_name: str, props: list[str]):
        self.name = name
        self.service = service
        self.meta_type = meta_type
        self.meta_name = meta_name
        self.props = props

    def write_json(self):
        with open("ff", mode="w") as f:
            f.write("import cjen\nfrom cjen import MetaJson\n\n\n")
            f.write(f"class {clazz_name(self.meta_name)}(MetaJson):\n")
            for prop in self.props:
                f.write(f"@cjen.operate.common.value\n")
                f.write(f"@cjen.operate.json.one(json_path=\"请填写jsonpath\")\n")
                f.write(f"def {prop}(self): ...\n\n\n")

    def write_mysql(self):
        with open("ff", mode="w") as f:
            f.write("import cjen\nfrom cjen import MetaMysql\n\n\n")
            f.write(f"class {clazz_name(self.meta_name)}(MetaMysql):\n")
            for prop in self.props:
                f.write(f"@cjen.operate.common.value\n")
                f.write(f"def {prop}(self): ...\n\n\n")

    def execute(self):
        # 在用例文件夹中 或 在用例文件夹的父文件夹中
        if os.path.dirname(os.getcwd()) == self.name and os.path.exists(os.path.join(os.getcwd(),self.name)): pass



parser = argparse.ArgumentParser()
parser.add_argument("--t", type=str, required=True, help="用例的名字,必须指定")
parser.add_argument("-a", action='store_true', help="在已有的用例中,增加service,需添加该参数")
parser.add_argument("--app", type=str,
                    help="service为哪个系统[edc,design,etmf,pv,ctms,portal,portaladmin,iwrs]")
parser.add_argument("--ss", type=str,
                    help="创建的service文件, 命名规则'xx_service', 如果有多个的话,以','间隔\n "
                         "例子: --ss crf_page_service,dataset_page_service",
                    default="")

parser.add_argument("--gm", action="store_true", help="是否在meta文件夹中创建service文件夹， 必须通过--s 指定service")
parser.add_argument("--mn", help="meta名字, 配合 --gm命令, 例子: ok_response", default="")
parser.add_argument("--mt", help="meta类型,[mysql/json], 配合 --gm命令, 例子: ok_response", default="")
parser.add_argument("--s", type=str,
                    help="添加meta 的 service文件, 配合 --gm命令",
                    default="")

parser.add_argument("--props", type=str,
                    help="设置meta 的属性, 如果有多个的话,以','间隔, 配合 --gm命令 \n"
                         "例子: --props id,name",
                    default="")

args = parser.parse_args()


def init_test_case(cmd_options):
    if not args.gm:
        services = cmd_options.ss if cmd_options.ss else input("请输入你想创建的service,命名方式'xx_yy',多个以','分割\n")
        application = cmd_options.app if cmd_options.app else input(
            "请输入service属于哪个系统[edc,design,etmf,pv,ctms,portal,portaladmin,iwrs]?\n")
        services = Service.factory(services=services, application=application)
        return Scaffold(name=cmd_options.t, services=services, append_action=cmd_options.a)
    return None


def init_meta(cmd_options):
    if args.gm:
        service = cmd_options.s if cmd_options.s else input("请输入你想为哪个service 增加meta:\n")
        meta_name = cmd_options.mn if cmd_options.mn else input("请输入meta文件名,命名方式'xx_yy':\n")
        meta_type = cmd_options.mt if cmd_options.mt else input("请输入meta对象类型[mysql/json]:\n")
        return ScaffoldGM(name=cmd_options.t, service=cmd_options.service, meta_type=meta_type, meta_name=meta_name)


if __name__ == '__main__':
    # try:
    scaffold = init_test_case(args) or init_meta(args)
    scaffold.execute()
    # except Exception as e:
    #     print(e)
