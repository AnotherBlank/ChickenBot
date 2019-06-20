# 禁言相关插件
from nonebot import CommandSession, on_command
import random
from plugins.others.tools import to_number
from util.SqlHelper import SqlHelper


@on_command('sleep', aliases='管理员我要睡觉', only_to_me=False)
async def sleep(session: CommandSession):
    group_id = session.ctx['group_id']
    user_id = session.ctx['sender']['user_id']
    duration = random.randint(1, 12) * 60 * 60
    sqlHelper = SqlHelper()
    sqlHelper.addUserSleep(user_id, duration)
    await session.bot.set_group_ban(group_id=group_id,
                                    user_id=user_id,
                                    duration=duration)


@sleep.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['duration'] = to_number(stripped_arg, session)
        return

    if not stripped_arg:
        session.pause('说人话')

    session.state[session.current_key] = to_number(stripped_arg, session)
