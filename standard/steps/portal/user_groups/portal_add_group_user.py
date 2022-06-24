
from cjen.sco.standard_step import StandardStep


from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.user_groups.portal_find_un_added_user import PortalFindUnAddedUser


class PortalAddGroupUser(StandardStep):
    Name = "portal_add_group_user.py"

    def __init__(self, service, scenario: PortalScenario):
        super().__init__(service, scenario)


    def _pre_processor(self):
        PortalFindUnAddedUser(self.service, self.scenario).run()

    def ignore(self): return self.service.context["user_id"] is None

    def _execute(self):
        super()._execute()
        self.service.usergroups_api_add_group_user(path_variable=self.path_variable(), data=self.data())

    def path_variable(self): return dict(userGroup_id=self.service.context["user_group_id"])

    def data(self):
        return [dict(userGroupId=self.service.context["user_group_id"], userId=self.service.context["user_id"])]
