"""
爬虫解析器基类定义
"""
from abc import abstractmethod


class BaseParser(object):
    """
    爬虫解析器的基类，定义了解析的基本方法
    """

    def __init__(self, next=None, level=None, **kwargs):
        """
        初始化的时候设置下一个解析器
        :param next: 可能为None，如果为None那么说明只有一个解析器
        :param kwargs 其他额外的参数
        """
        self.nextParser = next
        self.level = level

    def parse(self, parserRequest):
        """
        :param parserRequest 解析请求参数
        :return: 如果是最后一个解析器，那么直接返回解析结果，如果不是，解析后返回下一个解析器的parse函数的返回值
        """
        if self.nextParser is None:
            # 如果是最后一个解析器，那么直接返回解析的结果
            return self.doParse(parserRequest)
        else:
            # 如果不是最后一个解析器，首先自己解析，然后调用下一个的parse函数
            if self.level == parserRequest.getLevel():
                self.doParse(parserRequest)
                return self.nextParser.parse(parserRequest)
            else:
                return None

    def setNextParser(self, next):
        """
        设置下一个解析器
        :param next: 下一个解析器
        """
        self.nextParser = next

    @abstractmethod
    def doParse(self, parserRequest):
        """
        解析逻辑
        :param parserRequest:解析的参数
        :return:最后一个解析器必须返回一个parserResponse类型的返回值
        """
