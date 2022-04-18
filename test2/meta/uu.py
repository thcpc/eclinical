import cjen
from cjen import MetaMysql


class Uu(MetaMysql):
	@cjen.operate.common.value
	def id(self): ...

	@cjen.operate.common.value
	def name(self): ...

