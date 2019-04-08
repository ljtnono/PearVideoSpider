"""
定义了解析器解析之后的结果
"""


class ParserResponse(object):
    """
    解析器解析之后的结果
    """
    def __init__(self, **kwargs):
        """
        封装解析之后的结果
        """
        self.content = kwargs

