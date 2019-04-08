"""
梨视频爬虫的视频信息解析类
"""
import re

from pearvideo import BaseParser
from pearvideo.PearVideo import PearVideo


class PearVideoInfoParser(BaseParser):
    """
    解析出来梨视频的有用的信息类
    """

    def __init__(self, next=None, level=None, **kwargs):
        """
        :param next: 下一个解析器
        :param url: 解析的url地址
        :param headers: 解析的请求头
        :param params: 解析的参数
        """
        BaseParser.__init__(self, next=next, level=level, kwargs=kwargs)

    def doParse(self, parserRequest):
        """
        :param parserRequest: 请求参数
        :return:
        """
        text = parserRequest.params.get("text")
        # 获取每个li
        pattern_item = re.compile('<li\s\w+=".*?">(.*?)</li>', re.S)
        items = re.findall(pattern_item, text)
        # 遍历每个li 中的元素，获取有用的信息
        videos = []
        for item in items:
            pattern_id = re.compile('<.*?=\"video_(\w+)\"', re.S)
            id = re.search(pattern_id, item).group(1)
            pattern_img = re.compile('url\((.*?)\)', re.S)
            img = re.search(pattern_img, item).group(1)
            pattern_duration = re.compile('<.*?\sclass="cm-duration">(.*?)</.*?>', re.S)
            duration = re.search(pattern_duration,item).group(1)
            pattern_title = re.compile('<.*?=".*?-title">(.*?)</.*?>', re.S)
            title = re.search(pattern_title,item).group(1)
            pattern_author = re.compile('<.*?="author.*?".*?>(.*?)</.*?>', re.S)
            author = re.search(pattern_author, item).group(1)
            pattern_fav = re.compile('<.*?\sclass="fav".*?>(.*?)</.*?>',re.S)
            fav = re.search(pattern_fav, item).group(1)
            video = PearVideo(id, img, duration, title, author, fav, None)
            videos.append(video)
        parserRequest.params["videos"] = videos
        parserRequest.level = 3

