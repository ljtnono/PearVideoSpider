from pearvideo import BaseRequestHeaderFactory
from pearvideo.ParserRequest import ParserRequest
from pearvideo.PearVideoInfoParser import PearVideoInfoParser
from pearvideo.PearVideoListParser import PearVideoListParser
from pearvideo.PearVideoUrlParser import PearVideoUrlParser


if __name__ == '__main__':

    headers = BaseRequestHeaderFactory.get_headers()
    reqType = "1"
    start = 1
    categoryId = 1
    request = ParserRequest(level=1, reqType=reqType, start=start, categoryId=categoryId, headers=headers)
    pearVideoListParser = PearVideoListParser(level=1)
    pearVideoInfoParser = PearVideoInfoParser(level=2)
    pearVideoUrlParser = PearVideoUrlParser(level=3)
    pearVideoListParser.setNextParser(pearVideoInfoParser)
    pearVideoInfoParser.setNextParser(pearVideoUrlParser)
    s = pearVideoListParser.parse(request)
    for video in s.content["videos"]:
        print(video)


