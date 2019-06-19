from nonebot import CommandSession


def to_number(arg: str, session: CommandSession):
    """ 转换成数字
    """
    try:
        return int(arg)
    except:
        session.pause('说人话！')
