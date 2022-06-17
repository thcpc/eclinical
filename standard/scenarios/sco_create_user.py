import os.path
from eclinical import Environment
from eclinical.standard.portal.user import User
from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.user.portal_associated_usergroup import PortalAssociatedUserGroup
from eclinical.standard.steps.portal.user.portal_create_user import PortalCreateUser
from eclinical.standard.steps.portal.user.portal_find_user import PortalFindUser
from eclinical.standard.steps.portal.user.portal_find_user_role import PortalFindUserRole
from eclinical.standard.steps.portal.user.portal_study_title import PortalStudyTitle
from eclinical.standard.steps.portal.user.portal_user_access import PortalUserAccess
from eclinical.standard.steps.portal.user.portal_user_append_usergroup import PortalUserAppendUserGroup


class ScoCreateUser:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = PortalScenario(scenario_dir)
        service = User(environment)
        self.scenario.append_step(PortalFindUser, service)
        self.scenario.append_step(PortalCreateUser, service)
        self.scenario.append_step(PortalFindUserRole, service)
        self.scenario.append_step(PortalAssociatedUserGroup, service)
        self.scenario.append_step(PortalUserAppendUserGroup, service)
        self.scenario.append_step(PortalUserAccess, service)
        self.scenario.append_step(PortalStudyTitle, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment.loader("AWS_Test")
    sco = ScoCreateUser(sco_dir, envir)
    sco.run()
