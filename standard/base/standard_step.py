class StandardStep:
    @property
    def name(self): raise Exception("name need override")

    def data(self): ...

    def path_variable(self): ...

    def call_back(self, **kwargs): ...

    def _pre_processor(self): ...

    def _post_processor(self): ...

    def _execute(self): ...

    def run(self):
        self._pre_processor()
        self._execute()
        self._post_processor()
