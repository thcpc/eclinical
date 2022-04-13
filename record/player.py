import mitmproxy
import wx.xrc
from view.record_ui import RecordUi
import multiprocessing


class Player:
    def __init__(self):
        self.params = dict()

    def ui(self):
        app = wx.App()
        multiprocessing.freeze_support()
        ui = RecordUi(None)
        ui.Show()
        app.MainLoop()

    def response(self, flow:mitmproxy.http.flow): pass