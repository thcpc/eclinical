from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.base.scenario import Scenario
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.steps.portal.portal_find_study import PortalFindStudy


class PortalStudyNoStart(StandardStep):
    Name = "portal_study_no_start.py"

    def __init__(self, service: Hierarchies, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        if not self.service.context["study_id"]:
            PortalFindStudy(self.service, self.scenario)

    def _execute(self):
        self.service.system_systems(path_variable=self.path_variable())

    def life_cycle(self):
        return self.scenario.get("study").get("lifeCycle")

    def call_back(self, **kwargs):
        self.service.context["startup_studies"] = [app.id() for app in kwargs.get("systems").no_rel_apps()]

    def path_variable(self):
        return dict(study_id=self.service.context["study_id"], env_id=self.service.context[self.life_cycle()])
