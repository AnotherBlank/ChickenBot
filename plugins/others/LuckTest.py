# 测试运气命令

from nonebot import CommandSession, on_command
import random


@on_command('draw', aliases='抽签', only_to_me=False)
async def draw(session: CommandSession):
    nickname = session.ctx['sender']['nickname']
    randomResult = random.randint(1, 5)
    result = ''
    if randomResult == 1:
        result = '大凶'
    elif randomResult == 2:
        result = '凶'
    elif randomResult == 3:
        result = '小吉'
    elif randomResult == 4:
        result = '中吉'
    elif randomResult == 5:
        result = '大吉'
    await session.send(nickname + '今天抽的是: ' + result)
