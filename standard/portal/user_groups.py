import cjen

from eclinical import PortalLoginService, Environment
from eclinical.standard.base.ok_response import OkResponse
from eclinical.standard.base.step_definitions import StepDefinitions
from eclinical.standard.portal.dto.company_envs import CompanyEnvs
from eclinical.standard.portal.dto.query_user_groups import QueryUserGroups
from eclinical.standard.portal.dto.user_group_info import UserGroupInfo


class UserGroups(PortalLoginService):
    def __init__(self, environment: Environment = None):
        super().__init__(environment)
        self.step_definitions = StepDefinitions()

    @cjen.http.post_mapping(uri="admin/userGroup/query?pageNo={pageNo}&pageSize=25", json_clazz=QueryUserGroups)
    def get_user_group(self, path_variable, query: QueryUserGroups = None, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_find_usergroup import PortalFindUserGroup
        self.step_definitions.call_back(PortalFindUserGroup.Name, query=query)
        if not self.context["user_group_id"]:
            if not query.nextPage() == 0:
                self.get_user_group(path_variable=dict(pageNo=query.nextPage()))

    @cjen.http.get_mapping(uri="admin/userGroup/{userGroup_id}", json_clazz=UserGroupInfo)
    def user_group_info(self, path_variable, query: UserGroupInfo = None, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_get_user_group_info import PortalGetUserGroupInfo
        self.step_definitions.call_back(PortalGetUserGroupInfo.Name, query=query)

    @cjen.http.post_mapping(uri="admin/userGroup", json_clazz=OkResponse)
    @cjen.operate.asserts.validation_meta(meta_name="ok", fields="procCode")
    def create_user_group(self, data, ok: OkResponse = None, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_create_usergroup import PortalCreateUserGroup
        self.step_definitions.call_back(PortalCreateUserGroup.Name)

    @cjen.http.post_mapping(uri="admin/user")
    def create_user(self, data, resp=None, **kwargs): ...

    @cjen.http.get_mapping(uri="admin/company/envs", json_clazz=CompanyEnvs)
    def api_company_envs(self, company_envs: CompanyEnvs = None, resp=None, **kwargs):
        from eclinical.standard.steps.portal.portal_get_company_envs import PortalGetCompanyEnvs
        self.step_definitions.call_back(PortalGetCompanyEnvs.Name, company_envs=company_envs)


if __name__ == '__main__':
    ug = UserGroups(
        environment=Environment(envir="AWS_Test2", file_path="D:\\github\\eclinical\\eclinical\\environment.yaml"))
    ug.api_company_envs()
    # ug.create_user_group(data={"code": "UserGroup2", "active": True, "envIds": [105, 106, 107]})
    # ug.create_user_group(data={"code": "UserGroup3", "active": True, "envIds": [105, 106, 107]})
