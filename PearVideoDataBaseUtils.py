import configparser

import pymysql

from pearvideo.PearVideo import PearVideo


class PearVideoSaveUtil(object):
    """
    梨视频存储工具类
    """
    def __init__(self, config):
        """
        梨视频数据库存储工具
        """
        cf = configparser.ConfigParser()
        cf.read(config)
        self.host = cf.get("mysql-database", "host")
        self.user = cf.get("mysql-database", "user")
        self.password = cf.get("mysql-database", "password")
        self.db = cf.get("mysql-database", "db")
        self.charset = cf.get("mysql-database", "charset")
        self.port = cf.get("mysql-database", "port")
        self.table = cf.get("mysql-database", "table")

    def save(self, pearVideo):
        """
        存储信息
        :param pearVideo:
        :return:
        """
        con = self.getConnection()
        cursor = con.cursor()
        table = self.table
        data = {
            "id" : str(pearVideo.id),
            "img" : str(pearVideo.img),
            "duration" : str(pearVideo.duration),
            "title" : str(pearVideo.title),
            "author" : str(pearVideo.author),
            "fav" : str(pearVideo.fav),
            "video" : str(pearVideo.video)
        }
        keys = ",".join(data.keys())
        values = ",".join(['%s'] * len(data))
        sql = "insert into {table}({keys}) values ({values})".format(table=table, keys=keys, values=values)
        try:
            cursor.execute(sql, tuple(data.values()))
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
        else:
            con.close()

    def getConnection(self):
        """
        获取mysql连接，获取失败返回None
        :return: mysql连接
        """
        con = pymysql.connect(host=self.host, user=self.user, password=self.password, port=int(self.port), db=self.db, charset=self.charset)
        return con

    def update(self, pearVideo):
        """
        根据id更新数据
        :param pearVideo: 更新的video对象
        :param id: 更新的video对象的id值
        :return:
        """
        con = self.getConnection()
        cursor = con.cursor()
        data = {
            "id" : str(pearVideo.id),
            "img" : str(pearVideo.img),
            "duration" : str(pearVideo.duration),
            "title" : str(pearVideo.title),
            "author" : str(pearVideo.author),
            "fav" : str(pearVideo.fav),
            "video" : str(pearVideo.video)
        }
        table = "pearvideo"
        keys = ",".join(data.keys())
        values = ",".join(['%s'] * len(data))
        sql = "insert into {table}({keys}) values ({values}) ON DUPLICATE KEY UPDATE".format(table=table, keys=keys, values=values)
        update = ",".join([" {key} = %s".format(key=key) for key in data])
        sql += update
        try:
            if cursor.execute(sql, tuple(data.values()) * 2):
                print("Successful")
                con.commit()
        except:
            print("Failed")
            con.rollback()
        con.close()

    def getById(self, id):
        """
        根据id获取一个pearVideo的实体
        :param id: 需要获取的id
        :return: pearVideo实体
        """
        table = "pearVideo"
        sql = "select * from {table} where id = {id}".format(table=table, id=id)
        con = self.getConnection()
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            one = cursor.fetchone()
            video = PearVideo(one[0], one[1], one[2], one[3], one[4], one[5], one[6])
        except Exception as e:
            print("Failed 原因：" + str(e))
            return None
        return video


    def deleteById(self, id):
        """
        根据id删除一个记录
        :param id:
        :return:
        """
        table = "pearvideo"
        sql = "delete  from {table} where id = {id} ".format(table=table, id=id)
        con = self.getConnection()
        try:
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            print("Delete Successful!")
        except Exception as e:
            print("Failed 原因：" + str(e))
            con.rollback()
        con.close()