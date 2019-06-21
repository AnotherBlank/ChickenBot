# 签到系统
from nonebot import CommandSession, on_command
from nonebot.permission import GROUP, PRIVATE_GROUP
import mysql.connector

from util.SqlHelper import SqlHelper


@on_command('sign', aliases=['签到'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def sign(session: CommandSession):
    sqlHelper = SqlHelper()
    user_id = session.ctx['sender']['user_id']
    nickname = session.ctx['sender']['nickname']
    group_id = session.ctx['group_id']
    judge = sqlHelper.selectUserId(user_id)
    if judge is True:
        values = sqlHelper.selectUserInfo(user_id)
        # 判断是否已经签到了
        if values[3] == 1:
            await session.send('一天不能签到两次哦！')
        else:
            sqlHelper.updateUserSign(user_id)
            sqlHelper.updateUserNickName(user_id, nickname)
            await session.send('签到成功！' + nickname + '已经累计签到' + str(values[1] + 1) + '天!')
    else:
        await session.send('看起来' + nickname + '是第一次签到呢')
        sqlHelper.addNewUser(user_id, group_id, nickname)


