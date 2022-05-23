import cjen

from eclinical import Environment
from eclinical.service.portal_login_service import PortalLoginService
from eclinical.standard.base.ok_response import OkResponse
from eclinical.standard.portal.dto.envs import Envs
from eclinical.standard.portal.dto.hierarchies import Hierarchies
from eclinical.standard.portal.dto.query_studies import QueryStudies
from eclinical.standard.portal.dto.systems import Systems


class Hierarchies(PortalLoginService):
    def __init__(self, environment: Environment = None):
        super().__init__(environment)

    @cjen.http.get_mapping(uri="admin/company/envs", json_clazz=Envs)
    @cjen.operate.asserts.validation_meta(meta_name="envs")
    def get_env_list(self, life_cycle: str, envs: Envs = None, resp=None, **kwargs):
        for env in envs.payload():
            if env.name() == life_cycle: self.context[life_cycle] = env.id()

    @cjen.http.get_mapping(uri="admin/company/env/{env_id}/hierarchies", json_clazz=Hierarchies)
    @cjen.operate.asserts.validation_meta(meta_name="hierarchies")
    def get_sponsor(self, name, path_variable, hierarchies: Hierarchies, resp=None, **kwargs):
        for sponsor in hierarchies.sponsorExtDtoList():
            if sponsor.name() == name: self.context[f'sponsor_{name}'] = sponsor.id()
        print(self.context[f'sponsor_{name}'])

    @cjen.http.post_mapping(uri="admin/study/query?pageNo={pageNo}&pageSize=25", json_clazz=QueryStudies)
    def get_study(self, name, path_variable, data, query: QueryStudies = None, resp=None, **kwargs):
        self.context["study_id"] = None
        for study in query.studies():
            if study.name() == name:
                self.context["study_id"] = study.id()
        if not self.context["study_id"]:
            if query.nextPage() == 0: raise Exception(f'can not find the study {name}')
            self.get_study(name, path_variable=dict(pageNo=query.nextPage()), data=data)

    def new_sponsor(self):
        ...

    @cjen.http.post_mapping(uri="admin/study", json_clazz=OkResponse)
    @cjen.operate.asserts.validation_meta(meta_name="ok")
    def new_study(self, data, ok: OkResponse, resp=None, **kwargs):
        ...

    @cjen.http.get_mapping(uri="admin/study/{study_id}/env/{env_id}/systems", json_clazz=Systems)
    def system_systems(self, path_variable, systems: Systems = None, resp=None, **kwargs):
        self.context["startup_studies"] = [app.id() for app in systems.no_rel_apps()]

    @cjen.http.post_mapping(uri="admin/study/{study_id}/env/{env_id}/database", json_clazz=OkResponse)
    @cjen.operate.asserts.validation_meta(meta_name="ok")
    def study_startup(self, path_variable, data, ok: OkResponse, resp=None, **kwargs):
        ...


if __name__ == '__main__':
    cs = Hierarchies(
        environment=Environment(envir="AWS_Test", file_path="D:\\github\\eclinical\\eclinical\\environment.yaml"))
    cs.get_env_list(life_cycle="dev")
    cs.get_sponsor(name="chenpengcheng", path_variable=dict(env_id=cs.context[cs.environment.life_cycle]))
    cs.get_study(name="CPC033", data=dict(sponsorId=cs.context[f'sponsor_chenpengcheng']), path_variable=dict(pageNo=1))
    print(cs.context["study_id"])
    # for i in range(2, 100):
    #     cs.new_study(data=dict(active=True, description="", name=f'CPC0{i}',
    #                            sponsorId=cs.context[f"sponsor_chenpengcheng"],
    #                            subjectManagement=5))
    # cs.system_systems(path_variable=dict(study_id=820, env_id=cs.context[cs.environment.life_cycle]))
    # cs.study_startup(data=cs.context["startup_studies"],
    #                  path_variable=dict(study_id=820, env_id=cs.context[cs.environment.life_cycle]))
