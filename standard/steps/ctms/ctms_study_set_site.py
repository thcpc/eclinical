from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.ctms_scenario import CtmsScenario
from eclinical.standard.steps.ctms.ctms_find_site import CtmsFindSite
from eclinical.standard.steps.ctms.ctms_find_study import CtmsFindStudy
from eclinical.standard.steps.ctms.ctms_find_study_site import CtmsFindStudySite


class CtmsStudySetSite(StandardStep):
    Name = "ctms_set_site.py"

    def __init__(self, service, scenario: CtmsScenario):
        super().__init__(service, scenario)

    def sites(self): return self.scenario.sites()

    def _pre_processor(self):
        CtmsFindSite(self.service, self.scenario).run()
        CtmsFindStudySite(self.service, self.scenario).run()

    def data(self):
        return [{"siteId": self.service.context[CtmsFindSite.Info].get(site_name),
                 "siteName": site_name,
                 "siteCode": site_name,
                 "timezoneId": '0',
                 "languageId": '2',
                 "expectedSubject": '100',
                 "studyId": self.service.context[CtmsFindStudy.Id],
                 "menuId": '5080', } for site_name in self.sites()]

    def _execute(self):
        super()._execute()
        for site_data in self.data():
            self.service.study_management_add_site(data=site_data)
