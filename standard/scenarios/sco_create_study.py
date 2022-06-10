import os.path
from eclinical import Environment
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.hierarchies.portal_create_study import PortalCreateStudy
from eclinical.standard.steps.portal.hierarchies.portal_startup_study import PortalStartupStudy


class ScoCreateStudy:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = PortalScenario(scenario_dir)
        service = Hierarchies(environment)
        self.scenario.append_step(PortalCreateStudy, service)
        self.scenario.append_step(PortalStartupStudy, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment.loader("AWS_Test")
    sco = ScoCreateStudy(sco_dir, envir)
    sco.run()
