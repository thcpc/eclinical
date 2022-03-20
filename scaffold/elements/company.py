from scaffold.elements.component.text import Text


class Company:
    @classmethod
    def input(cls, msg: str = "请输入公司名", default=None, default_key=None):
        text = Text(msg, default, default_key)
        user_input = text.get(input(f"{text}\n"))
        company = "" if user_input == default else user_input
        return company
