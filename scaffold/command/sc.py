import argparse
import os


from scaffold.files.gen_service import Service, GenService
from scaffold.inputs.application import Application
from scaffold.template.file_operate import FileOperate

parser = argparse.ArgumentParser()
parser.add_argument("-name", help="创建或更新的 service 名")
args = parser.parse_args()


class Sc:
    def __init__(self, name):
        self.name = name
        self.folder = os.getcwd()

    def path_right(self):
        if not os.path.exists(os.path.join(self.folder, "services")):
            raise Exception("无法找到services文件夹")


def sc_command():
    sc = Sc(args.name)
    sc.path_right()
    GenService(sc.folder).add_service(args.name, Application.input(msg=f"{args.name}是什么系统"))


if __name__ == '__main__':
    sc_command()
