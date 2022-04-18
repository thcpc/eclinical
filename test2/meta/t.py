import cjen
from cjen import MetaMysql


class T(MetaMysql):
	@cjen.operate.common.value
	def d(self): ...

	@cjen.operate.common.value
	def r(self): ...

