import cjen

from cjen import DatabasePool
from eclinical import PortalLoginService, Environment


class TtService(PortalLoginService):
    """
    相关使用详情可查询:
    http 装饰器: https://github.com/thcpc/cjen#432-http-%E8%A3%85%E9%A5%B0%E5%99%A8
    数据构造 装饰器: https://github.com/thcpc/cjen#433-factory-%E8%A3%85%E9%A5%B0%E5%99%A8
     """

    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.context['cursor'] = DatabasePool.cursor(host=environment.db.get("host"), user=environment.db.get("user"), pwd=environment.db.get("pwd"), port=environment.db.get("port"), database=environment.db.get("database"))

