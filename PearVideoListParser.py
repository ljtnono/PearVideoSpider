import requests

from pearvideo import BaseParser


class PearVideoListParser(BaseParser):
    """
    梨视频爬虫List解析器，从网址获取梨视频的数据列表
    这里爬取的是HTML内容，需要进一步解析
    """

    url = ("https://www.pearvideo.com/popular_loading.jsp", "https://www.pearvideo.com/category_loading.jsp")

    def __init__(self, next=None, level=None, **kwargs):
        """
        :param next: 下一个解析器
        :param level: 解析等级
        :param headers: 解析的请求头
        :param params: 解析的参数
        """
        BaseParser.__init__(self, next=next, level=level, kwargs=kwargs)

    def doParse(self, parserRequest):
        """
        :param parserRequest:解析请求参数
        :return:
        """
        headers = parserRequest.params["headers"]
        reqType = parserRequest.params["reqType"]
        start = parserRequest.params["start"]
        categoryId = parserRequest.params["categoryId"]
        params = {
            "reqType": reqType,
            "start": start,
            "categoryId": categoryId
        }
        try:
            response = requests.get(url=self.url[0], params=params, headers=headers)
            text = response.text
        except Exception as e:
            print("爬取失败！原因：" + str(e))
        else:
            parserRequest.params["text"] = text
            parserRequest.level = 2





