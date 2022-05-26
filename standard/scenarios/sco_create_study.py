import os.path

from eclinical import Environment
from eclinical.standard.base.scenario import Scenario
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.steps.portal.portal_create_study import PortalCreateStudy
from eclinical.standard.steps.portal.portal_startup_study import PortalStartupStudy


class ScoCreateStudy:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = Scenario(scenario_dir)
        service = Hierarchies(environment)
        self.scenario.append_step(PortalCreateStudy, service)
        self.scenario.append_step(PortalStartupStudy, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment(envir="AWS_Test", file_path="D:\\github\\eclinical\\eclinical\\environment.yaml")
    sco = ScoCreateStudy(sco_dir, envir)
    sco.run()
