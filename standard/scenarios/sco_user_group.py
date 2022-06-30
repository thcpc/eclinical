import os.path


from eclinical import Environment
from eclinical.standard.portal.portal_api import PortalApi


from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.user_groups.portal_add_group_user import PortalAddGroupUser
from eclinical.standard.steps.portal.user_groups.portal_create_usergroup import PortalCreateUserGroup
from eclinical.standard.steps.portal.user_groups.portal_get_lifecycle_hierarchies import PortalGetLifeCycleHierarchies
from eclinical.standard.steps.portal.user_groups.portal_get_user_group_info import PortalGetUserGroupInfo


#  创建UserGroup, 并且分配User, Sponsor, Study, Site.
from eclinical.standard.steps.portal.user_groups.portal_set_lifecycle_hierarchies import PortalSetLifeCycleHierarchies


class ScoUserGroup:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = PortalScenario(scenario_dir)
        service = PortalApi(environment)
        # 创建用户组
        self.scenario.append_step(PortalCreateUserGroup, service)
        # 获取未添加到User Group中的 User
        self.scenario.append_step(PortalGetUserGroupInfo, service)
        # 把用户添加到User Group中
        # self.scenario.append_step(PortalAddGroupUser, service)
        # 选择lifecycle, 获取对应lifecycle的sponsor, study, site 信息
        self.scenario.append_step(PortalGetLifeCycleHierarchies, service)
        # 分配 Sponsor, Study, Site
        self.scenario.append_step(PortalSetLifeCycleHierarchies, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    sco = ScoUserGroup(sco_dir,  Environment.loader("DEV_03"))
    sco.run()
    # a = "a"
    # print(f'{{a}}')
