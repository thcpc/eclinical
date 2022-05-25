from eclinical.standard.base.scenario import Scenario
from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.steps.portal.portal_find_study import PortalFindStudy


class PortalStartupStudy(StandardStep):
    Name = "portal_startup_study"

    def __init__(self, service: Hierarchies, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.add_step(self.Name, self)

    def _pre_processor(self):
        PortalFindStudy(self.service, self.scenario).run()

    def _execute(self):
        self.service.study_startup(
            data=self.data(),
            path_variable=self.path_variable())

    def life_cycle(self): return self.scenario.get("study").get("lifeCycle")

    def data(self): return [self.service.context["startup_studies"]]

    def path_variable(self):
        return dict(study_id=self.service.context["study_id"],
                    env_id=self.service.context[self.life_cycle()])
