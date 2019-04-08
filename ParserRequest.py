"""
对爬虫解析器的封装
"""


class ParserRequest(object):
    """
    封装了解析器的请求参数
    """

    def __init__(self, level, **kwargs):
        """
        :param level: 请求的等级
        :param kwargs: 请求的参数，可能包括上一个解析器传递过来的结果和一些其他的参数
        """
        self.level = level
        self.params = kwargs

    def getLevel(self):
        """
        获取请求的级别
        :return: 返回请求的级别,级别默认是0，根据请求的级别来做出反应
        """
        return self.level
