from cjen.sco.scenario import Scenario
from cjen.sco.standard_step import StandardStep

from eclinical.standard.design.design_api import Versioning
from eclinical.standard.steps.design.versioning.design_fileids import DesignFileIDS


class DesignDownloadPublishSql(StandardStep):
    Name = "design_download_publish_sql.py"

    def __init__(self, service: Versioning, scenario: Scenario):
        super().__init__(service, scenario)


    def _pre_processor(self):
        DesignFileIDS(self.service, self.scenario).run()

    def _execute(self):
        super()._execute()
        self.service.download_file(data=self.data())

    def data(self):
        sql_file_id = self.service.context["archives"].db_spec().get("fileId") - 1
        return {"fileIds": [sql_file_id]}

    def call_back(self, **kwargs):
        with open("publish_sql.zip", 'wb') as f:
            f.write(kwargs.get("file_bytes"))
