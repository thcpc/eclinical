class Service:
    def __init__(self, service_name, app):
        self.service_name = service_name
        self.app = app

    @property
    def file_name(self): return f"{self.service_name}_service"

    @property
    def clazz_name(self): return "".join([elem.capitalize() for elem in self.file_name.split("_")])

    @property
    def application(self): return self.app

    @property
    def application_clazz(self):
        clazz = dict(etmf="ETMFLoginService", pv="PVLoginService", ctms="CTMSLoginService", edc="EdcLoginService",
                     iwrs="IWRSLoginService", design="DesignLoginService", portal="PortalLoginService",
                     portaladmin="PortalAdministratorLoginService").get(self.application.lower(), "BigTangerine")
        return clazz

    def output_conftest_py(self):
        return "import pytest\n\n" + \
               "from environment.environment import Environment\n\n" + \
               f"from .service.{self.file_name} import {self.clazz_name}\n\n\n" + \
               f"@pytest.fixture\n" + f"def {self.file_name}(ef, st):\n" + \
               f"\treturn {self.clazz_name}(Environment(envir=st, file_path=ef))\n\n\n"

    def output_init_py(self): return f"from .{self.file_name} import {self.clazz_name}\n"

    def output_service_py(self):

        if self.application_clazz == "BigTangerine":
            import_str = "import cjen\n\nfrom cjen import BigTangerine,DatabasePool\nfrom eclinical import Environment\n\n\n"
        else:
            import_str = f"import cjen\n\nfrom cjen import DatabasePool\nfrom eclinical import {self.application_clazz}, Environment\n\n\n"
        return import_str + \
               f"class {self.clazz_name}({self.application_clazz}):\n" + \
               f"\tdef __init__(self, environment: Environment):\n" + \
               f"\t\tsuper().__init__(environment)\n" + \
               f"\t\tself.context['cursor'] = DatabasePool.cursor(host=environment.db.get(\"host\"), user=environment.db.get(\"user\"), pwd=environment.db.get(\"pwd\"), port=environment.db.get(\"port\"), database=environment.db.get(\"database\"))\n\n"
