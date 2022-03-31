from scaffold.inputs.component.text import Text


class MetaAttrs:
    @classmethod
    def input(cls, msg="请输入对象属性，多个属性以','分割", default=None, default_key=None):
        text = Text(msg, default, default_key)
        return text.get(input(f"{text}\n")).split(",")