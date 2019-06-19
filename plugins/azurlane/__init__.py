# 碧蓝航线上头模拟器
from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_GROUP

from plugins.azurlane.CardData import NormalLightShipData


@on_command('azlight', aliases=['轻型舰建造'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurOneLight(session: CommandSession):
    data = NormalLightShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '建造出: ' + data.singleDrawing())


@on_command('azten', aliases=['轻型舰十连'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurTenLight(session: CommandSession):
    data = NormalLightShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的[轻型舰建造]十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n')
