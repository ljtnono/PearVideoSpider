"""
梨视频视频下载地址解析
"""
import re

import requests

from pearvideo import BaseParser
from pearvideo.ParserResponse import ParserResponse


class PearVideoUrlParser(BaseParser):
    """
    解析出来梨视频的视频下载地址
    """
    url = "https://www.pearvideo.com/video_"

    def __init__(self, next=None, level=None, **kwargs):
        """
        :param next: 下一个解析器
        :param url: 解析的url地址
        :param headers: 解析的请求头
        :param params: 解析的参数
        """
        BaseParser.__init__(self, next=next, level=level, kwargs=kwargs)

    def parse(self, parserRequest):
        """
        解析出来梨视频的视频下载地址,并且返回地址
        """
        videos = parserRequest.params["videos"]
        headers = parserRequest.params["headers"]
        try:
            for video in videos:
                url = self.url + video.id
                response = requests.get(url=url, headers=headers)
                content = response.text
                pattern = re.compile("https://video.pearvideo.com/.*\.mp4")
                video_url = re.search(pattern, content)
                video.video = video_url.group()
        except Exception as e:
            print(e)
        else:
            return ParserResponse(videos=videos)



