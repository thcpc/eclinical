import os

from eclinical import Environment
from eclinical.standard.portal.role import Role
from eclinical.standard.scenarios.portal_scenario import PortalScenario
from eclinical.standard.steps.portal.role.portal_create_role import PortalCreateRole
from eclinical.standard.steps.portal.role.portal_find_role import PortalFindRole
from eclinical.standard.steps.portal.role.portal_get_permission_tree import PortalGetPermissionTree
from eclinical.standard.steps.portal.role.portal_set_permissions import PortalSetPermissions


class ScoCreateRole:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = PortalScenario(scenario_dir)
        service = Role(environment)
        self.scenario.append_step(PortalFindRole, service)
        self.scenario.append_step(PortalCreateRole, service)
        self.scenario.append_step(PortalGetPermissionTree, service)
        self.scenario.append_step(PortalSetPermissions, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment.loader("AWS_Test")
    sco = ScoCreateRole(sco_dir, envir)
    sco.run()