from cjen import BigTangerine


class StandardStep:
    def __int__(self, name, service: BigTangerine):
        self.name = name
        self.service = service

    def depend_step_names(self) ->list[str]: ...

    def _execute(self): ...

    def run(self):
        self._execute()
        return self.service
