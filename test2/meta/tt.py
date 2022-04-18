import cjen
from cjen import MetaMysql


class Tt(MetaMysql):
	@cjen.operate.common.value
	def a(self): ...

	@cjen.operate.common.value
	def b(self): ...

