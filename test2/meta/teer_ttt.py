import cjen
from cjen import MetaJson


class TeerTtt(MetaJson):
	@cjen.operate.common.value
	@cjen.operate.json.one(json_path="请填写jsonpath")
	def id(self): ...

	@cjen.operate.common.value
	@cjen.operate.json.one(json_path="请填写jsonpath")
	def name(self): ...

