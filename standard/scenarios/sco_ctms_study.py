import os

from eclinical import Environment
from eclinical.standard.ctms.ctms_api import CtmsApi
from eclinical.standard.scenarios.ctms_scenario import CtmsScenario
from eclinical.standard.steps.ctms.ctms_find_site import CtmsFindSite
from eclinical.standard.steps.ctms.ctms_find_study import CtmsFindStudy
from eclinical.standard.steps.ctms.ctms_find_study_site import CtmsFindStudySite
from eclinical.standard.steps.ctms.ctms_submit_study_basic_info import CtmsSubmitStudyBasicInfo


class ScoCtmsStudy:
    def __init__(self, scenario_dir, environment: Environment):
        self.scenario = CtmsScenario(scenario_dir)
        service = CtmsApi(environment)
        self.scenario.append_step(CtmsFindStudy, service)
        self.scenario.append_step(CtmsSubmitStudyBasicInfo, service)
        self.scenario.append_step(CtmsFindSite, service)
        self.scenario.append_step(CtmsFindStudySite, service)
        # self.scenario.append_step(PortalFindUserRole, service)
        # self.scenario.append_step(PortalAssociatedUserGroup, service)
        # self.scenario.append_step(PortalUserAppendUserGroup, service)
        # self.scenario.append_step(PortalUserAccess, service)
        # self.scenario.append_step(PortalStudyTitle, service)

    def run(self): self.scenario.run()


if __name__ == '__main__':
    sco_dir = os.path.join("new_study")
    envir = Environment.loader("DEV_03")
    sco = ScoCtmsStudy(sco_dir, envir)
    sco.run()
