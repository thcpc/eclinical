import sys
from multiprocessing import Process
from mitmproxy.tools.main import mitmdump


class MitmProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self) -> None:
        sys.argv = ['mitmdump', '-s', 'record\\mitm_addons.py', '-p', '9999']
        mitmdump()

    def stop(self) -> None:
        if self.is_alive():
            self.kill()


mitm_process = MitmProcess()
