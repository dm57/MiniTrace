from __future__ import annotations

import time
from uuid import uuid4

from libs.span import Span


class Trace:
    """trace 类"""

    def __init__(self, name: str):
        self.name = name
        self.uuid = uuid4().hex
        self.start_time = None
        self.end_time = None
        self.is_started = False
        self.is_finished = False
        self.spans = []
        self.traces = []

    def begin(self) -> Trace:
        """开启trace"""
        self.start_time = time.time()
        self.is_started = True
        return self

    def end(self):
        """结束trace"""
        self.end_time = time.time()
        self.is_finished = True

    def create_child_trace(self, child_name: str):
        """创建子trace"""
        child_trace = self.__class__(child_name)
        self.traces.append(child_trace)
        return child_trace

    def create_span(self, name: str, start_span: bool = True):
        """创建一个span, 默认自动开启"""
        span = Span(name, trace_uuid=self.uuid)
        if start_span:
            span.start()
        self.spans.append(span)
        return span

    def delete_span(self, name: str):
        """删除一个span，"""
        pass
