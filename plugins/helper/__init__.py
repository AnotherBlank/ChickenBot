# 帮助界面

from nonebot import on_command, CommandSession,on_request, RequestSession,on_notice, NoticeSession


@on_command('whoami', aliases='你是谁', only_to_me=False)
async def whoami(session: CommandSession):
    await session.send('屈作妓，苦食篒，可怜无助十一姬')


@on_command('help', aliases='帮助', only_to_me=False)
async def help(session: CommandSession):
    await session.send('目前可使用的指令: \narkone | arkten——干员寻访\nazlight | '
                       'azlightten——舰B轻型建建造\nazheavy | azheavyten——舰b重型舰建造\nazspecial | '
                       'azspecialten——舰b特型舰建造\njrrp——人品\ndraw——抽签\nhelp——帮助\nwhoami '
                       '——我是谁\nsleep——禁言礼包\nsign | 签到——签到功能 签到后可享受精致睡眠在线记录 (被选中的人会出现BUG)\nsleeprank——精致睡眠排行榜')


# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    await session.approve()
    return

# 验证消息加好友
@on_request('friend')
async def makefrind(session: RequestSession):
    if session.ctx['comment'] == '19137':
        await session.approve()
        return
    await session.reject('验证消息不对哦')


# 新成员入群消息
@on_notice('group_increase')
async def joingroup(session: NoticeSession):
    # 发送消息
    await session.send('什么？你群竟然有新人了！')

# 有人退群
@on_notice('group_decrease')
async def exitgroup(session: NoticeSession):
    user_id = session.ctx['user_id']
    await session.send(str(user_id) + '因为不可名状事件永远的消失了。')

