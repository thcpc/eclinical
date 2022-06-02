from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.portal.user_groups import UserGroups
from eclinical.standard.steps.portal.user_groups.portal_find_usergroup import PortalFindUserGroup
from eclinical.standard.steps.portal.user_groups.portal_get_company_envs import PortalGetCompanyEnvs


class PortalCreateUserGroup(StandardStep):
    Name = "portal_create_user_group"

    def __init__(self, service: UserGroups, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        PortalFindUserGroup(self.service, self.scenario).run()
        PortalGetCompanyEnvs(self.service, self.scenario).run()

    def ignore(self): return self.service.context["user_group_id"] is not None

    def code(self): return self.scenario.get("user_groups").get("userGroup")

    def _execute(self):
        if self.service.context["user_group_id"] is None:
            self.service.create_user_group(data=self.data())

    def data(self): return {"code": self.code(), "active": True, "envIds": self.service.context["envIds"]}
