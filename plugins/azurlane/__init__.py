# 碧蓝航线上头模拟器
from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_GROUP

from plugins.azurlane.CardData import NormalLightShipData, HeavyShipData, SpecialShipData


@on_command('azlight', aliases=['轻型舰建造'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurOneLight(session: CommandSession):
    data = NormalLightShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '建造出: ' + data.singleDrawing())


@on_command('azlightten', aliases=['轻型舰十连'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurTenLight(session: CommandSession):
    data = NormalLightShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的[轻型舰建造]十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n')


@on_command('azheavy', aliases=['重型舰建造'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurOneHeavy(session: CommandSession):
    data = HeavyShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '建造出: ' + data.singleDrawing())


@on_command('azheavyten', aliases=['重型舰十连'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurTenHeavy(session: CommandSession):
    data = HeavyShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的[重型舰建造]十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n')


@on_command('azspecial', aliases=['特型舰建造'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurOneSpecial(session: CommandSession):
    data = SpecialShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '建造出: ' + data.singleDrawing())


@on_command('azspecialten', aliases=['特型舰十连'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def azurTenHeavy(session: CommandSession):
    data = SpecialShipData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的[特型舰建造]十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n')
