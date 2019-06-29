from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_GROUP

from plugins.arknights.StaffData import StaffData, NormalStaffData


@on_command('arkone', aliases=['干员寻访'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def arkRandom(session: CommandSession):
    data = NormalStaffData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '抽到了: ' + data.singleDrawing())


@on_command('arkten', aliases=['十连寻访'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def arkRandomTen(session: CommandSession):
    data = NormalStaffData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing())

