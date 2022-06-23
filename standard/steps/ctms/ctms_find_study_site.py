from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.ctms_scenario import CtmsScenario
from eclinical.standard.steps.ctms.ctms_find_site import CtmsFindSite
from eclinical.standard.steps.ctms.ctms_find_study import CtmsFindStudy


class CtmsFindStudySite(StandardStep):
    Name = "ctms_find_study_site.py"
    Info = "ctms_sites_of_study"

    def __init__(self, service, scenario: CtmsScenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self
        self.service.context[self.Info] = []

    def _pre_processor(self):
        CtmsFindStudy(self.service, self.scenario).run()

    def _post_processor(self):
        print(len(self.service.context[self.Info]))

    def ignore(self): return self.service.context[CtmsFindStudy.Info] is None

    def call_back(self, **kwargs):
        self.service.context[self.Info].extend(kwargs.get("query").list())

    def path_variable(self): return dict(pageNo=1)

    def data(self): return dict(studyId=self.service.context[CtmsFindStudy.Info].get("id"))

    def _execute(self): self.service.study_management_site_list(path_variable=self.path_variable(), data=self.data())
