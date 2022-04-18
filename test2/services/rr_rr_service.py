
import cjen
from eclinical import EdcLoginService, Environment


class RrRrService(EdcLoginService):
    def __init__(self, environment: Environment):
        super().__init__(environment)
