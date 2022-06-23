from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.ctms_scenario import CtmsScenario


class CtmsFindStudy(StandardStep):
    Name = "ctms_find_study.py"
    Info = "ctms_study_dto"

    def __init__(self, service, scenario: CtmsScenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def call_back(self, **kwargs):
        self.service.context[self.Info] = None
        for study in kwargs.get("studies").list():
            if study.name() == self.scenario.study():
                self.service.context[self.Info] = dict(id=study.id(), name=study.name())

    def _execute(self):
        self.service.study_management_get_study()
