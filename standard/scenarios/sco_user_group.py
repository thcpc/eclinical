import os.path

from cjen.sco.scenario import Scenario

from eclinical import Environment

from eclinical.standard.portal.user_groups import UserGroups
from eclinical.standard.steps.portal.user_groups.portal_add_group_user import PortalAddGroupUser


class ScoUserGroup:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = Scenario(scenario_dir)
        service = UserGroups(environment)
        # self.scenario.append_step(PortalCreateUserGroup, service)
        # self.scenario.append_step(PortalGetUserGroupInfo, service)
        self.scenario.append_step(PortalAddGroupUser, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment(envir="AWS_Test", file_path="D:\\github\\eclinical\\eclinical\\environment.yaml")
    sco = ScoUserGroup(sco_dir, envir)
    sco.run()
