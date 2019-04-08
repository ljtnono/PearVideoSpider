"""
    用来存储梨视频爬取的实体
"""


class PearVideo(object):
    """
    梨视频爬虫存储实体
    """
    # 请求类型的id
    categoryId = {
        "社会" : "1",
        "新知" : "10",
        "世界" : "2",
        "体育" : "9",
        "生活" : "5",
        "科技" : "8",
        "娱乐" : "4",
        "财富" : "3",
        "汽车" : "31",
        "美食" : "6",
        "音乐" : "59"
    }

    # 初始化函数
    def __init__(self, id, img, duration, title, author, fav, video):
        # 全部控制为私有变量
        self._id = id
        self._img = img
        self._duration = duration
        self._title = title
        self._author = author
        self._fav = fav
        self._video = video

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        self._img = img

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def fav(self):
        return self._fav

    @fav.setter
    def fav(self, fav):
        self._fav = fav

    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, video):
        self._video = video

    def __str__(self):

        return "id：{id}\n" \
                "img: {img}\n" \
                "duration: {duration}\n" \
                "title: {title}\n" \
                "author: {author}\n" \
               "video: {video}\n" \
               "fav: {fav}\n".format(id=self._id, img=self._img, duration=self._duration, title=self._title, author=self._author, fav=self._fav, video=self._video)



