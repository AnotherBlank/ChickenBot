# 帮助界面

from nonebot import on_command, CommandSession


@on_command('whoami', aliases='你是谁', only_to_me=False)
async def whoami(session: CommandSession):
    await session.send('屈作妓，苦食篒，可怜无助十一姬')


@on_command('help', aliases='帮助', only_to_me=False)
async def help(session: CommandSession):
    await session.send('目前可使用的指令: \narkone | arkten——干员寻访\nazlight | '
                       'azten——舰B轻型建建造\njrrp——人品\ndraw——抽签\nhelp——帮助\nwhoami——我是谁')
