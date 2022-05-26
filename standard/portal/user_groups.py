import cjen

from eclinical import PortalLoginService, Environment
from eclinical.standard.base.step_definitions import StepDefinitions
from eclinical.standard.portal.dto.query_user_groups import QueryUserGroups
from eclinical.standard.portal.dto.user_group_info import UserGroupInfo


class UserGroups(PortalLoginService):
    def __init__(self, environment: Environment = None):
        super().__init__(environment)
        self.step_definitions = StepDefinitions()

    @cjen.http.get_mapping(uri="admin/userGroup/query?pageNo={pageNo}&pageSize=25", json_clazz=QueryUserGroups)
    def get_user_group(self, path_variable, query: QueryUserGroups = None, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_find_usergroup import PortalFindUserGroup
        self.step_definitions.call_back(PortalFindUserGroup.Name, query=query)
        if not self.context["user_group_id"]:
            if not query.nextPage() == 0:
                self.get_user_group(path_variable=dict(pageNo=query.nextPage()))

    @cjen.http.get_mapping(uri="admin/userGroup/{userGroup_id}")
    def user_group_info(self, path_variable, query: UserGroupInfo, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_get_user_group_info import PortalGetUserGroupInfo
        self.step_definitions.call_back(PortalGetUserGroupInfo.Name, query=query)

    @cjen.http.post_mapping(uri="admin/userGroup")
    def create_user_group(self, data, resp=None, **kwargs):
        print(resp)

    @cjen.http.post_mapping(uri="admin/user")
    def create_user(self, data, resp=None, **kwargs): print(resp)


if __name__ == '__main__':
    ug = UserGroups(
        environment=Environment(envir="AWS_Test2", file_path="D:\\github\\eclinical\\eclinical\\environment.yaml"))
    ug.create_user_group(data={"code": "UserGroup2", "active": True, "envIds": [105, 106, 107]})
    ug.create_user_group(data={"code": "UserGroup3", "active": True, "envIds": [105, 106, 107]})
