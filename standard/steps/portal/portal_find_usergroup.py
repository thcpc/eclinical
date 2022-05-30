from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.base.scenario import Scenario
from eclinical.standard.portal.user_groups import UserGroups


class PortalFindUserGroup(StandardStep):
    Name = "portal_find_user_group"

    def __init__(self, service: UserGroups, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def user_group(self): return self.scenario.get("user_groups").get("userGroup")

    def _post_processor(self):
        print('user_group_id', self.service.context["user_group_id"])

    def call_back(self, **kwargs):
        self.service.context["user_group_id"] = None
        for user_group in kwargs.get("query").user_groups():
            if user_group.code() == self.user_group():
                self.service.context["user_group_id"] = user_group.id()

    def _execute(self): self.service.get_user_group(path_variable=dict(pageNo=1))
