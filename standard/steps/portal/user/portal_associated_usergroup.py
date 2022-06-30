from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.user.portal_find_user import PortalFindUser


class PortalAssociatedUserGroup(StandardStep):
    Name = "portal_associate_user_group.py"
    ExistsRels = "exists_user_rels"

    def __init__(self, service, scenario: PortalScenario):
        super().__init__(service, scenario)

    def _pre_processor(self):
        PortalFindUser(self.service, self.scenario).run()

    def path_variable(self):
        return dict(user_id=self.service.context[PortalFindUser.Id])

    def _execute(self):
        super()._execute()
        self.service.user_api_user_group_role_rel(path_variable=self.path_variable())

    def call_back(self, **kwargs):
        rels = [dict(roleId=rel.roleId(), userGroupId=rel.userGroupId(), userId=rel.userId()) for rel in kwargs.get("rel").list()]
        self.service.context[PortalAssociatedUserGroup.ExistsRels] = rels
