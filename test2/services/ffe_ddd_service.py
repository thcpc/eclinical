
import cjen
from eclinical import EdcLoginService, Environment


class FfeDddService(EdcLoginService):
    def __init__(self, environment: Environment):
        super().__init__(environment)
