import cjen
from cjen import MetaJson


class Rrr(MetaJson):
	@cjen.operate.common.value
	@cjen.operate.json.one(json_path="请填写jsonpath")
	def id(self): ...

	@cjen.operate.common.value
	@cjen.operate.json.one(json_path="请填写jsonpath")
	def df(self): ...

