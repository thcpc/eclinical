from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.scenarios.ctms_scenario import CtmsScenario
from eclinical.standard.steps.ctms.ctms_find_study import CtmsFindStudy


class CtmsSubmitStudyBasicInfo(StandardStep):
    Name = "ctms_submit_study_basic_info.py"

    def __init__(self, service, scenario: CtmsScenario):
        self.service = service
        self.scenario = scenario
        self.service.step_definitions[self.Name] = self

    def _pre_processor(self):
        CtmsFindStudy(self.service, self.scenario).run()

    def data(self):
        return {
            "blindMethods": 0,
            "craReview": False,
            "daysToResolveQuery": 100,
            "endDate": 2519827200000,
            "id": self.service.context[CtmsFindStudy.Info].get("id"),
            "intervalDays": 10000,
            "isDraft": False,
            "mainPurpose": 1,
            "mandatoryForAttachments": 0,
            "name": self.service.context[CtmsFindStudy.Info].get("name"),
            "numOfSite": 3,
            "numOfSubject": 100,
            "randomize": True,
            "saftyReview": False,
            "startDate": 1655971679755,
            "studyPhase": 1,
            "studyType": 0
        }

    def _execute(self): self.service.study_management_submit_info(data=self.data())
