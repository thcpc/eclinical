from cjen.sco.step_definitions import StepDefinitions

from eclinical import PortalLoginService, Environment


class User(PortalLoginService):
    def __init__(self, environment: Environment = None):
        super().__init__(environment)
        self.step_definitions = StepDefinitions()

