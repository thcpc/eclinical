
import cjen
from cjen import MetaJson


class OKResponse(MetaJson):
    @cjen.operate.asserts.equal(value=200)
    @cjen.operate.json.one(json_path="$.procCode")
    def procCode(self): ...
