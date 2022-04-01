class Meta:

    def __init__(self, name, props=[]):
        self.props = props
        self.name = name

    @property
    def clazz_name(self):
        return "".join([elem.capitalize() for elem in self.name.split("_")])

    def json(self):
        content = "import cjen\nfrom cjen import MetaJson\n\n\n" + f"class {self.clazz_name}(MetaJson):\n"
        for prop in self.props:
            content += f"\t@cjen.operate.common.value\n"
            content += f"\t@cjen.operate.json.one(json_path=\"请填写jsonpath\")\n"
            content += f"\tdef {prop}(self): ...\n\n"
        return content

    def mysql(self):
        content = "import cjen\nfrom cjen import MetaMysql\n\n\n" + f"class {self.clazz_name}(MetaMysql):\n"
        for prop in self.props:
            content += f"\t@cjen.operate.common.value\n"
            content += f"\tdef {prop}(self): ...\n\n"
        return content
