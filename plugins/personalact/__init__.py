# 这是对话内容
from nonebot import on_natural_language, CommandSession


@on_natural_language(keywords={'嫁给我', '嫁我', '娶你', '结婚'})
async def _(session: CommandSession):
    await session.send('绝！对！不！行！')


@on_natural_language(keywords={'你是谁', '是谁', '谁'})
async def _(session: CommandSession): await session.send('我可是超绝可爱的十一姬。')


@on_natural_language(keywords={'主人是谁', '谁是你的主人'})
async def _(session: CommandSession): await session.send('是十三姬前辈。')
