import argparse

from scaffold.files.gen_meta import GemMeta
from scaffold.inputs.mc.meta_attrs import MetaAttrs
from scaffold.inputs.mc.meta_name import MetaName
from scaffold.inputs.mc.meta_type import MetaType

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="创建meta 对象")
parser.add_argument("--type", help="meta 对象类型,mysql 或 json")
parser.add_argument("--attrs", help="对象属性，多个属性以,分割")

args = parser.parse_args()


class Mc:

    def meta(self, meta_name, meta_type, meta_attrs):
        GemMeta().add_meta(meta_name, meta_type, meta_attrs)


def mc_command():
    try:
        mc = Mc()
        mc.meta(args.name or MetaName().input(),
                args.type or MetaType().input(),
                args.attrs or MetaAttrs().input())

    except Exception as e:
        print(e)
