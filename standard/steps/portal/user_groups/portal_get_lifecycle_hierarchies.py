from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.portal.user_groups import UserGroups
from eclinical.standard.steps.portal.user_groups.portal_get_company_envs import PortalGetCompanyEnvs


class PortalGetLifeCycleHierarchies(StandardStep):
    Name = "portal_get_lifecycle_hierarchies.py"

    def __init__(self, service: UserGroups, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        PortalGetCompanyEnvs(self.service, self.scenario).run()

    def life_cycle(self): return self.scenario.get("user_groups").get("lifeCycle")

    def user_group(self): return self.scenario.get("user_groups").get("userGroup")

    def data(self): ...

    def path_variable(self):
        return {"life_cycle_id" : self.service.context["envObjects"].get(self.life_cycle())}


    def _execute(self): ...
