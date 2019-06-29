import random

from nonebot import logger


class StaffData:
    # 下面都是活动 '强力干员的'
    # 闪灵/塞雷亚占50%
    # 真理/幽灵鲨/红占50%
    sixList = ['推进之王', '能天使', '星熊', '伊芙利特', '银灰', '夜莺', '艾雅法拉', '安洁莉娜', '斯卡蒂']
    fiveList = ['芙兰卡', '德克萨斯', '凛冬', '白面鸮', '蓝毒', '普罗旺斯', '赫默', '雷蛇', '临光', '夜魔', '天火', '初雪', '拉普兰德', '华法琳',
                '守林人', '狮蝎', '白金', '陨星', '梅尔', '可颂', '崖心', '食铁兽', '空']
    fourList = ['深海色', '杜宾', '白雪', '远山', '夜烟', '流星', '蛇屠箱', '末药', '猎蜂', '慕斯', '砾', '暗索', '调香师', '地灵', '霜叶', '清道夫', '古米',
                '角峰', '缠丸', '阿消', '红豆', '杰西卡']
    threeList = ['芬', '克洛丝', '炎熔', '米格鲁', '芙蓉', '卡缇', '史都华德', '香草', '玫兰莎', '安赛尔', '梓兰', '翎羽', '空爆', '月见夜']

    fiveListUp = ['真理', '幽灵鲨', '红']
    sixListUp = ['闪灵', '塞雷亚']

    # 区间算法
    def singleDrawing(self):
        # 保存随机值,毕竟这是单抽算法
        randomResult = random.randint(1, 10000)
        # 随机值判断
        if randomResult <= 200:
            # 抽到了六星干员.
            randomResult = random.randint(1, 10000)
            # 判断是否抽到了up干员
            if randomResult <= 5000:
                return '【★★★★★★UP!】——' + self.sixListUp[random.randint(0, 1)]
            else:
                return '【★★★★★★】——' + self.sixList[random.randint(0, 8)]
        elif randomResult <= 1000:
            # 抽到了五星干员
            randomResult = random.randint(1, 10000)
            if randomResult <= 5000:
                return '[★★★★★UP!]——' + self.fiveListUp[random.randint(0, 1)]
            else:
                return '[★★★★★]——' + self.fiveList[random.randint(0, 22)]
        elif randomResult <= 6000:
            # 抽到了四星干员.
            return '☆☆☆☆——' + self.fourList[random.randint(0, 21)]
        else:
            # 抽到了三星干员.
            return '☆☆☆——' + self.threeList[random.randint(0, 13)]


# 常驻池
class NormalStaffData:
    sixList = ['推进之王', '能天使', '星熊', '伊芙利特', '艾雅法拉', '安洁莉娜', '斯卡蒂', '闪灵', '塞雷亚', '斯卡蒂']
    fiveList = ['芙兰卡', '德克萨斯', '凛冬', '普罗旺斯', '赫默', '雷蛇', '临光', '夜魔', '天火', '初雪', '拉普兰德', '华法琳',
                '守林人', '狮蝎', '白金', '陨星', '梅尔', '可颂', '崖心', '食铁兽', '真理', '幽灵鲨', '红']
    fourList = ['深海色', '杜宾', '白雪', '远山', '夜烟', '流星', '蛇屠箱', '末药', '猎蜂', '慕斯', '砾', '暗索', '调香师', '地灵', '霜叶', '清道夫', '古米',
                '角峰', '缠丸', '阿消', '红豆', '杰西卡']
    threeList = ['芬', '克洛丝', '炎熔', '米格鲁', '芙蓉', '卡缇', '史都华德', '香草', '玫兰莎', '安赛尔', '梓兰', '翎羽', '空爆', '月见夜']

    fiveListUp = ['空', '蓝毒', '白面鸮']
    sixListUp = ['银灰', '夜莺']

    # 区间算法
    # 六星：10
    # 五星： 23
    # 四星 22
    # 三星：14
    def singleDrawing(self):
        # 保存随机值,毕竟这是单抽算法
        randomResult = random.randint(1, 10000)
        # 随机值判断
        if randomResult <= 200:
            # 抽到了六星干员.
            randomResult = random.randint(1, 10000)
            # 判断是否抽到了up干员
            if randomResult <= 5000:
                return '【★★★★★★UP!】——' + self.sixListUp[random.randint(0, 1)]
            else:
                return '【★★★★★★】——' + self.sixList[random.randint(0, 9)]
        elif randomResult <= 1000:
            # 抽到了五星干员
            randomResult = random.randint(1, 10000)
            if randomResult <= 5000:
                return '[★★★★★UP!]——' + self.fiveListUp[random.randint(0, 1)]
            else:
                return '[★★★★★]——' + self.fiveList[random.randint(0, 22)]
        elif randomResult <= 6000:
            # 抽到了四星干员.
            return '☆☆☆☆——' + self.fourList[random.randint(0, 21)]
        else:
            # 抽到了三星干员.
            return '☆☆☆——' + self.threeList[random.randint(0, 13)]
