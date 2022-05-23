from eclinical.standard.base.standard_step import StandardStep
from eclinical.standard.portal.hierarchies import Hierarchies


class CreateStudy(StandardStep):
    def __int__(self, name, service: Hierarchies):
        super(CreateStudy, self).__int__(name, service)

    def run(self): ...
