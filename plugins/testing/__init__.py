# -*-coding:utf-8-*-
# 测试用文件主要测试各种的功能命令
from nonebot import on_command, CommandSession


@on_command('testing', aliases=['测试'], only_to_me=False)
async def tess(session: CommandSession):
    bot = session.bot
    nickname = session.ctx['sender']['nickname']
    group_id = session.ctx['group_id']
    await bot.send_group_msg(group_id=group_id, message=nickname + '?')
