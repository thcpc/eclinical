from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.base.scenario import Scenario
from eclinical.standard.portal.user_groups import UserGroups
from eclinical.standard.steps.portal.portal_find_usergroup import PortalFindUserGroup


class PortalGetUserGroupInfo(StandardStep):
    Name = "portal_get_user_group_info"

    def __init__(self, service: UserGroups, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        PortalFindUserGroup(self.service, self.scenario).run()

    def call_back(self, **kwargs):
        for company_multiple_env in kwargs.get("query").company_multiple_envs():
            if company_multiple_env.name() == self.life_cycle():
                self.service.context["company_multiple_env_id"] = company_multiple_env.id()

    def _post_processor(self): print(self.service.context["company_multiple_env_id"])

    def _execute(self): self.service.user_group_info(path_variable=self.path_variable())

    def path_variable(self): return dict(userGroup_id=self.service.context["user_group_id"])