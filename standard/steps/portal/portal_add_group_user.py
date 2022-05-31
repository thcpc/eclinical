from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.base.scenario import Scenario
from eclinical.standard.portal.user_groups import UserGroups
from eclinical.standard.steps.portal.portal_find_un_added_user import PortalFindUnAddedUser


class PortalAddGroupUser(StandardStep):
    Name = "portal_add_group_user.py"

    def __init__(self, service: UserGroups, scenario: Scenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        PortalFindUnAddedUser(self.service, self.scenario).run()

    def ignore(self): return self.service.context["user_id"] is None

    def _execute(self):
        self.service.api_add_group_user(path_variable=self.path_variable(), data=self.data())

    def path_variable(self): return dict(userGroup_id=self.service.context["user_group_id"])

    def data(self):
        return [dict(userGroupId=self.service.context["user_group_id"], userId=self.service.context["user_id"])]
