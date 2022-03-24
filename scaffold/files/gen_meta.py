import os

from scaffold.template.file_operate import FileOperate
from scaffold.template.meta import Meta


class GemMeta:
    def __init__(self, folder): self.folder = folder

    def add_meta(self, meta_name: str, meta_type: str, props: str):
        meta = Meta(meta_name, props.split(","))
        if not os.path.exists(os.path.join(self.folder, "meta")):
            os.mkdir(os.path.join(self.folder, "meta"))
        fop = FileOperate(self.folder)
        body = meta.json() if meta_type == 'json' else meta.mysql()
        fop.rewrite_file("meta", meta.name + ".py", body) \
        or fop.new_file("meta", meta.name + ".py", body)
        # 输出到 __init__.py TODO 输出meta下的__init__
