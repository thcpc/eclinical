import cjen
from cjen import MetaMysql


class Rr(MetaMysql):
	@cjen.operate.common.value
	def f(self): ...

