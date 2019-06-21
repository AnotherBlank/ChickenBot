# 这是对话内容
from typing import Optional

from nonebot import *
from nonebot.helpers import render_expression
from nonebot.permission import PRIVATE, GROUP
import random

from util.SqlHelper import SqlHelper

# -------------这是私聊部分
EXPR_DONT_UNDERSTAND = (
    '??????',
    '……你想表达什么？',
    '你得明白你对面是机器人，请用机器人的语言来说！',
    '……人类的语言好深奥',
    'ERROR: 无法理解',
    '虽然不明白你说的意思，但这个时候卖萌就对了！(<ゝω·)☆~',
    '我！听！不！懂！',
    '……我需要一个人来教教我怎么回答这句'
)


@on_command('study', permission=GROUP | PRIVATE, only_to_me=False)
async def study(session: CommandSession):
    # 加一个限定
    if session.ctx['group_id'] != 572013667:
        return
    question = session.state.get('question')  # 从会话状态里尝试获取
    if question is None:
        question = session.get('question', prompt='你需要我学习应答什么句子？', at_sender=True)
        session.state['question'] = question  # 修改会话状态
    answer = session.get('answer', prompt='那么我该怎么回答这个句子？')
    user_id = session.ctx['sender']['user_id']
    sqlHelper = SqlHelper()
    sqlHelper.insertQuestionAndAnswer(question, answer, user_id)
    reply = f'添加成功！\n询问:\n{question}\n回答:\n{answer}'
    session.finish(reply)


@study.args_parser
async def _(session: CommandSession):
    if session.is_first_run and session.current_arg_text.strip():
        # 第一次运行，如果有参数，则设置给 question
        session.state['question'] = session.current_arg_text.strip()

    # 如果不需要对参数进行特殊处理，则不用再手动加入 state，NoneBot 会自动放进去


@on_natural_language(permission=PRIVATE)
async def _(session: NLPSession):
    return IntentCommand(60, 'justspeak', args={'message': session.msg_text})


@on_command('justspeak')
async def justSpeak(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
    message = session.state.get('message')

    # 获取回复
    reply = await call_response(str(message), 0)
    if reply:
        await session.send(reply)
    else:
        # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))
        # return


# 回复的api方法，返回一个字符串
async def call_response(text: str, number: int) -> Optional[str]:
    if not text:
        return None

    # 从数据库查询
    sqlHelper = SqlHelper()
    if number == 0:
        values = sqlHelper.selectQuestion(text)
    else:
        values = sqlHelper.selectQuestionForGroup(text)
    randomresult = 0

    # 如果不存在
    if not values:
        return None
    else:
        # 如果很不只有一个
        if len(values) != 1:
            randomresult = random.randint(0, len(values) - 1)
        return str(values[randomresult][2])


# -------------这是群聊部分
@on_natural_language(permission=GROUP,only_to_me=False)
async def _(session: NLPSession):
    return IntentCommand(60, 'justspeakgroup', args={'message': session.msg_text})


@on_command('justspeakgroup')
async def justspeakgroup(session: CommandSession):
    message = session.state.get('message')
    reply = await call_response(str(message), 1)
    if reply:
        await session.send(reply)
    else:
        return
