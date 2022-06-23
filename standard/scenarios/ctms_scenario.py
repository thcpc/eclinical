from cjen.sco.scenario import Scenario


class CtmsScenario(Scenario):
    def __init__(self, scenario_dir):
        super().__init__(scenario_dir)

    def sponsor(self):
        return self.get("sponsor").get("name")

    def study(self):
        return self.get("study").get("name")

    def life_cycle(self):
        return self.get("life_cycle").get("env")

    def sites(self):
        return self.get("user_groups").get("sites")