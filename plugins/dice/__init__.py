from nonebot import on_command, CommandSession,logger
from nonebot.permission import GROUP, PRIVATE
import random


@on_command('roll', permission=GROUP | PRIVATE, only_to_me=False)
async def roll(session: CommandSession):
    data = session.state.get('data')  # 属于为xdy的形式
    nickname = session.ctx['sender']['nickname']
    randomresult = 0
    if data is None:  # 默认就1d100
        randomresult = random.randint(1, 100)
        await session.finish(nickname + '投掷出: ' + str(randomresult))
    else:
        datas = str(data).split('d')
        i = 0
        while i < int(datas[0]):
            randomresult += random.randint(1, int(datas[1]))
            i += 1
        await session.finish(nickname + '掷' + datas[0] + '次' + datas[1] + '面骰的总点: ' + str(randomresult))


@roll.args_parser
async def _(session: CommandSession):
    if session.is_first_run and session.current_arg_text.strip():
        session.state['data'] = session.current_arg_text.strip()
