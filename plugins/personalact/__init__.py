# 这是对话内容
from typing import Optional

from jieba import posseg

from nonebot import *
from nonebot import logger
from nonebot.helpers import render_expression
from nonebot.permission import PRIVATE, GROUP
from nonebot.command.argfilter import validators, extractors, ValidateError
import random

from util.SqlHelper import SqlHelper

# 无法回答指令时候的表达
EXPR_DONT_UNDERSTAND = (
    'emmmmmm……你在说什么？',
    '??????',
    '听！不！懂！',
    '这条信息可能超出了我的理解范围',
    '跟机器人对话要用机器人语！用help来查！',
    'ERROR: 我没听懂'
    '(。_。)糟糕，触及到了我的知识盲区...',
)


@on_command('study', permission=GROUP, only_to_me=False)
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

    # 通过封装的函数获取图灵机器人的回复
    reply = await call_response(message)
    if reply:

        await session.send(reply)
    else:
        # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))


# 回复的api方法，返回一个字符串
async def call_response(text: str) -> Optional[str]:
    if not text:
        return None

    # 从数据库查询
    sqlHelper = SqlHelper()
    values = sqlHelper.selectQuestion(text)
    randomresult = 0

    # 如果不存在
    if not values:
        return None
    else:
        # 如果很不知有一个
        if len(values) != 1:
            randomresult = random.randint(0, len(values) - 1)
        return str(values[randomresult][2])
