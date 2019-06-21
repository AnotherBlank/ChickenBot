# from attr import validators
# from nonebot import on_command, CommandSession
# from nonebot.command.argfilter import extractors
# from nonebot.permission import PRIVATE
#
# from plugins.personalact import my_custom_validator
#
#
# @on_command('demo', permission=PRIVATE, only_to_me=False)
# async def demo(session: CommandSession):
#     question = session.state.get('arg1_derived')  # 从会话状态里尝试获取
#     if question is None:
#         arg1: int = session.get(
#             'arg1',
#             prompt='请输入参数1',
#             arg_filters=[
#                 extractors.extract_text,  # 提取纯文本部分
#                 str.strip,  # 去掉两边的空白
#                 validators.not_empty(),
#                 validators.match_regex(r'[0-9a-zA-Z]{6,20}', '必须为6~20位字符'),
#                 my_custom_validator,  # 自定义验证器
#                 int,  # 转换成 int
#                 validators.ensure_true(lambda x: x > 20000000, '必须大于2000000')
#             ],
#             at_sender=True,
#         )
#         question = arg1 + 42
#         session.state['arg1_derived'] = question  # 修改会话状态
#
#     arg3 = session.get('arg3', prompt='你的arg3是什么呢？')
#
#     reply = f'arg1_derived:\n{question}\narg3:\n{arg3}'
#     session.finish(reply)
#
#
# @demo.args_parser
# async def _(session: CommandSession):
#     if session.is_first_run and session.current_arg_text.strip():
#         # 第一次运行，如果有参数，则设置给 arg3
#         session.state['arg3'] = session.current_arg_text.strip()