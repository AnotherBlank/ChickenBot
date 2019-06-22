# 禁言相关插件
from nonebot import CommandSession, on_command
import random

from nonebot.permission import GROUP

from util.SqlHelper import SqlHelper

from nonebot.log import logger


@on_command('sleep', aliases='管理员我要睡觉', only_to_me=False)
async def sleep(session: CommandSession):
    group_id = session.ctx['group_id']
    user_id = session.ctx['sender']['user_id']
    nickname = session.ctx['sender']['nickname']
    role = session.ctx['sender']['role']
    logger.debug('----------------------role=' + str(role))

    # 如果是管理员
    if role == 'admin' or role == 'owner':
        session.finish('emmmmm我好像没有办法哄你睡觉呢')
    else:
        duration = random.randint(1, 24) * 3600
        sqlHelper = SqlHelper()
        sqlHelper.addUserSleep(user_id, duration / 3600)
        sqlHelper.updateUserNickName(user_id, nickname)
        await session.send('晚安哦' + nickname)
        await session.bot.set_group_ban(group_id=group_id,
                                        user_id=user_id,
                                        duration=duration)


@on_command('sleeprank', aliases=['睡眠排行'], permission=GROUP, only_to_me=False)
async def sleeprank(session: CommandSession):
    sqlHelper = SqlHelper()
    group_id = session.ctx['group_id']
    logger.error('Group_id 是' + str(group_id))
    values = sqlHelper.selectUserSleepRank(group_id)
    logger.error(values)
    if not values:
        await session.send('这个群还没有人使用这个功能哦')
    elif len(values) <= 3:
        await session.send('至少三个人使用sign指令才能用哦')
    else:
        await session.send('本群睡眠排行榜：\n' +
                           '冠军: ' + values[0][1] + '(' + str(values[0][0]) + ')  ' + str(values[0][2]) + '小时\n' +
                           '亚军: ' + values[1][1] + '(' + str(values[1][0]) + ')  ' + str(values[1][2]) + '小时\n' +
                           '季军: ' + values[2][1] + '(' + str(values[2][0]) + ')  ' + str(values[2][2]) + '小时')
