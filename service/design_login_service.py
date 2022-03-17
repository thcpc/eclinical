import cjen

from environment.environment import Environment
from service._study_login_service import _StudyLoginService


class DesignLoginService(_StudyLoginService):
    @cjen.context.add(content=dict(system="DESIGN"))
    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.study_auth()

    @cjen.http.post_mapping(uri="design/auth")
    @cjen.jwt(key="Authorization", json_path="$.payload.jwtAuthenticationResponse.token")
    def study_auth(self, resp=None, **kwargs):
        ...
