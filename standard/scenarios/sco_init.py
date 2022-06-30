import os

from eclinical import Environment

# 初始化整个公司账号的内容
from eclinical.standard.scenarios.sco_create_role import ScoCreateRole
from eclinical.standard.scenarios.sco_create_sponsor import ScoCreateSponsor
from eclinical.standard.scenarios.sco_create_study import ScoCreateStudy
from eclinical.standard.scenarios.sco_create_user import ScoCreateUser
from eclinical.standard.scenarios.sco_ctms_study import ScoCtmsStudy
from eclinical.standard.scenarios.sco_user_group import ScoUserGroup


class ScoInit:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario_dir = scenario_dir
        self.environment = environment
        self.sco_clazz = []

    def run(self):
        # 创建 Sponsor
        ScoCreateSponsor(self.scenario_dir, self.environment).run()
        # 创建 Study
        ScoCreateStudy(self.scenario_dir, self.environment).run()
        # 创建 Role
        ScoCreateRole(self.scenario_dir, self.environment).run()
        # 创建 UserGroup
        ScoUserGroup(self.scenario_dir, self.environment).run()
        # 创建 User
        ScoCreateUser(self.scenario_dir, self.environment).run()
        # 创建 CTMS SITE
        ScoCtmsStudy(self.scenario_dir, self.environment).run()
        # Portal 中分配Site
        ScoUserGroup(self.scenario_dir, self.environment).run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment.loader("DEV_01")
    sco = ScoInit(sco_dir, envir)
    sco.run()
