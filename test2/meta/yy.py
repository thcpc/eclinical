import cjen
from cjen import MetaJson


class Yy(MetaJson):
    """
    相关使用详情可查询:
    装饰器: https://github.com/thcpc/cjen#42-metajson-%E8%A3%85%E9%A5%B0%E5%99%A8
    """

    @cjen.operate.common.value
    @cjen.operate.json.one(json_path="请填写jsonpath")
    def id(self): ...

    @cjen.operate.common.value
    @cjen.operate.json.one(json_path="请填写jsonpath")
    def name(self): ...

