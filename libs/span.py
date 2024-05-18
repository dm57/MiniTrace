from __future__ import annotations

import time
from uuid import uuid4


class Span:
    """span 类"""

    def __init__(self, name: str, trace_uuid: str = "", parent_span_uuid: str = ""):
        """创建span，需要指定名称、归属trace的uuid、父级span的uuid"""
        self.name = name
        self.trace_uuid = trace_uuid
        self.parent_span_uuid = parent_span_uuid
        self.uuid = uuid4().hex
        self.tags = []
        self.start_time = None
        self.end_time = None
        self.is_started = False
        self.is_finished = False

    def set_tags(self, tags: dict = None, **kwargs):
        """为span增加tags，可使用key-word方式传递tag，也可以直接使用字典通过tags字段传递"""
        self.__append_tags(tags)
        self.__append_tags(kwargs)

    def __append_tags(self, tags: dict = None):
        self.tags.extend([{k: v} for k, v in (tags or {}).items()])

    def start(self):
        """开启span"""
        self.start_time = time.time()
        self.is_started = True
        return self

    def end(self):
        """结束span"""
        self.end_time = time.time()
        self.is_finished = True
