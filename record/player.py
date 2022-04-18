import mitmproxy
import wx.xrc
import yaml

from record.ext.memcached import memcached
from view.record_ui import RecordUi
import multiprocessing


class Player:

    def ui(self, envirs: dict):
        app = wx.App()
        multiprocessing.freeze_support()
        ui = RecordUi(None, envirs)
        ui.Show()
        app.MainLoop()

    # TODO 根据顺序生成yaml文件，文件名为序号
    # TODO url,method, 请求体，响应体
    # TODO url 中的数字替换为 id ,或 page
    # TODO 请求体中的 id 处理
    # TODO 文件的上传
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if memcached.get("host") in flow.request.pretty_url:
            if "user/permissions" in flow.request.pretty_url:
                with open(flow.request.path.replace("/", "_"), 'w') as f:
                    f.write(str(flow.response.content, 'utf-8'))


if __name__ == "__main__":
    with open("environment.yaml", "r", encoding="utf-8") as f:
        envirs = {name: env.get("uri") for name, env in yaml.load(f.read(), Loader=yaml.FullLoader).get("ENV").items()}
    # print(envirs)
    # envirs = {"1111111111111111111111111111111111111111111111111111111111111111111111111":"2222"}
    Player().ui(envirs)
