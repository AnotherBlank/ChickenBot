# 数据库内容封装
import mysql.connector


class SqlHelper:
    # 数据库连接
    conn = mysql.connector.connect(user='root', password='123456', database='ChickenBotDataBase')
    cursor = conn.cursor()

    # 查询指定 user_id 是否存在，不存在返回false，存在返回true
    def selectUserId(self, userId):
        sql = 'SELECT * FROM user_info WHERE User_Id =' + str(userId)
        self.cursor.execute(sql)
        value = self.cursor.fetchone()
        if value is None:
            return False
        else:
            return True

    # 签到用的方法，给User_Sign+1
    def updateUserSign(self, userId):
        sql = 'UPDATE user_info SET User_Sign = User_Sign + 1 WHERE User_Id = ' + str(userId)
        self.cursor.execute(sql)
        self.conn.commit()

    # 更新用户昵称
    def updateUserNickName(self,userId,nickName):
        sql = 'UPDATE user_info SET User_NickName = \'' + str(nickName) + '\'WHERE User_Id =' + str(userId)
        self.cursor.execute(sql)
        self.conn.commit()

    # 添加新用户
    def addNewUser(self, userId, groupId, nickName):
        sql = 'INSERT INTO user_info VALUE (' + str(userId) + ',1,0,1,' + str(groupId) + '\'' + str(nickName) + '\')'
        self.cursor.execute(sql)
        self.conn.commit()

    # 查询用户签到和被封禁信息
    def selectUserInfo(self, userId):
        sql = 'SELECT * FROM user_info WHERE User_Id = ' + str(userId)
        self.cursor.execute(sql)
        values = self.cursor.fetchone()
        return values

    # 增加用户的sleep时间
    def addUserSleep(self, userId, number):
        sql = 'UPDATE user_info SET User_Sleep = User_Sleep + ' + str(number) + ' WHERE User_Id = ' + str(userId)
        self.cursor.execute(sql)
        self.conn.commit()

    # 查看sleep排行
    # TODO 有BUG，到时候再说
    def selectUserSleepRank(self, groupId):
        sql = 'SELECT User_Id,User_NickName,User_SignedToday FROM user_info WHERE Group_id = ' + str(groupId) + 'ORDER BY User_Sleep DESC '
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values
