import nonebot
import random


def collect_repeat_info(group, msg):
    if group not in msgDict.keys():
        msgDict[group] = {'msg': msg, 'num': 1}
    elif msg == msgDict[group]['msg']:
        num = msgDict[group]['num'] + 1
        msgDict[group] = {'msg': msg, 'num': num}
    else:
        msgDict[group] = {'msg': msg, 'num': 1}


msgDict = {}
bot = nonebot.get_bot()
message = ['天才出于复读。',
           '我读的书愈多，就愈亲近世界，愈明了复读的意义，愈觉得复读的重要。',
           '没有人不爱惜他的出现，但很少人珍视他的复读。',
           '复读是人生的命脉，是一切价值的根基。',
           '复读是石，敲出星星之火；复读是火，点燃沙雕的灯，复读是灯，照亮网友的路，复读是路，带你去看色图。',
           '人生中最困难者，莫过于复读。',
           '不论群多冷清，聪明的人总会想办法去复读；不论群多火热，愚蠢的人总觉得该禁言这个混球。',
           '人生必有复读，所以引人入胜亦在于此。',
           '复读可以体现一个民族的创造力，智慧和精神。',
           '从不复读的人，没有工夫抱怨群冷。',
           '复读可以简练地定义为对不可能的情况的一种不合逻辑的信仰。'
           '复读使人心明眼亮。',
           '人类的历史，就是一个不断地从第一个复读向大规模复读发展的历史。',
           '最成功的复读机是那些使最少量的复读发挥最大的作用的机器。',
           '文明就是要造成有修养的复读机。'
           '复读是一种绵延不绝的渴望，渴望不断上升，变得更伟大而高贵。',
           '我渴望随着复读指引的方向，心平气和地、没有争吵、悔恨、羡慕，笔直走完人生旅途。'
           '成功的秘诀，在永不改变既定的复读。',
           '一个人有无成就，决定于他青年时期是不是有过复读。',
           '在年轻人的颈项上，没有什么东西能比复读这颗灿烂的宝珠更迷人的了。',
           '在人的生活中最主要的是复读。没有复读就不可能有正常人的生活。',
           '你要知道复读的实质，不要去听一个复读机说些什么，而要仔细看他在做什么。',
           '复读总是年青的，只有不复读才会变老。',
           '复读和发色图是永远不应令人厌恶的两种品德。',
           '复读的火花，常常在群友的磨石上迸发。',
           '人在复读上应当是明豁的，沙雕上应该是清白的，色图上应该是清洁的。',
           '在复读的道路上，当你的努力一个个落空的时候，你也要坚定，要沉着。',
           '复读就象打橄榄球一样，不能犯规，也不要闪避球，而应向底线冲过去',
           '知识是从复读中得来的，任何成就都是刻苦复读的结晶。',
           '如果你想获得幸福和安宁，那就要越过层层的障壁，敲起复读的钟前进。'
           ]


@bot.on_message('group')
async def repeat(context):
    group = context['group_id']
    msg = str(context['message'])
    collect_repeat_info(group, msg)
    if msgDict[group]['num'] in [3]:
        await bot.send(context, msg)
    elif msgDict[group]['num'] in [6, 12, 18, 24, 36]:
        msg = message[random.randint(0, len(message)-1)]
        await bot.send(context, msg)
