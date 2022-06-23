from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.steps.ctms.ctms_find_site import CtmsFindSite
from eclinical.standard.steps.ctms.ctms_find_study import CtmsFindStudy


class CtmsStudySetSite(StandardStep):
    Name = "ctms_set_site.py"

    def __init__(self, service, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self): ...

    def data(self):
        return {"siteId": self.service.context[CtmsFindSite.Info],
         "siteName": site[1],
         "siteCode": site[1],
         "timezoneId": '0',
         "languageId": '2',
         "expectedSubject": '100',
         "studyId": self.service.context[CtmsFindStudy.Id],
         "menuId": '5080', }

    def _execute(self): self.service.study_management_add_site(data=self.data())
