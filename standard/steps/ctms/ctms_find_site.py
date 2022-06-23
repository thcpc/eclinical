from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.ctms_scenario import CtmsScenario


class CtmsFindSite(StandardStep):
    Name = "ctms_find_site.py"
    Info = "ctms_site_entyties_id"
    NoFill = -1

    def __init__(self, service, scenario: CtmsScenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def sites(self):
        return self.scenario.sites()

    def _post_processor(self):
        print(self.service.context[self.Info])

    def need_fill(self, site_entity):
        return self.service.context[self.Info].get(site_entity.siteName()) is not None \
               and self.service.context[self.Info].get(site_entity.siteName()) == self.NoFill

    def call_back(self, **kwargs):
        self.service.context[self.Info] = dict.fromkeys(self.sites(), self.NoFill)
        for site_entity in kwargs.get("site_entities").list():
            if self.need_fill(site_entity):
                self.service.context[self.Info][site_entity.siteName()] = site_entity.id()

    def _execute(self):
        self.service.entity_management_site_list(path_variable=self.path_variable())

    def path_variable(self):
        return dict(pageNo=1)
