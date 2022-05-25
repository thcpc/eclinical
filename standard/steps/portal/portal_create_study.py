from eclinical.standard.base.scenario import Scenario
from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.portal.hierarchies import Hierarchies
from eclinical.standard.steps.portal.portal_find_sponsor import PortalFindSponsor


class PortalCreateStudy(StandardStep):
    Name = "portal_create_study"

    def __init__(self, service: Hierarchies, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.add_step(self.Name, self)




    def _pre_processor(self):
        PortalFindSponsor(self.service, self.scenario).run()

    def _execute(self):
        self.service.new_study(data=self.data())

    def study(self): return self.scenario.get("study").get("name")

    def sponsor(self): return self.scenario.get("study").get("sponsor")

    def data(self):
        return dict(active=True, description="", name=self.study(),
                    sponsorId=self.service.context[f"sponsor_{self.sponsor()}"],
                    subjectManagement=5)
