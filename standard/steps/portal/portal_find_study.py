from eclinical.standard.base.scenario import Scenario
from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.steps.portal.portal_find_sponsor import PortalFindSponsor


class PortalFindStudy(StandardStep):
    Name = "portal_find_study"

    def __init__(self, service: Hierarchies, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        PortalFindSponsor(self.service, self.scenario).run()

    def sponsor(self):
        return self.scenario.get("study").get("sponsor")

    def study(self):
        return self.scenario.get("study").get("name")

    def call_back(self, **kwargs):
        self.service.context["study_id"] = None
        for study in kwargs.get("query").studies():
            if study.name() == self.study():
                self.service.context["study_id"] = study.id()

    def _execute(self):
        self.service.get_study(
            data=self.data(),
            path_variable=self.path_variable())

    def _post_processor(self): print(self.service.context["study_id"])

    def data(self):
        return dict(sponsorId=self.service.context['sponsor_id'])

    def path_variable(self):
        return dict(pageNo=1)
