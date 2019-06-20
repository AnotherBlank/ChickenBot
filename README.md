# ChickenBot
## 简介
个人娱乐用的机器人，基于[nonebot]，鉴于对python半生不熟的状态，里面的代码并不怎么好看。  
目前包含两个简单的抽卡功能。

[nonebot]: https://github.com/richardchien/nonebot
## 已有功能
1. 上头模拟 (碧蓝航线，明日方舟)
2. 幸运抽签

## 使用
+ 确保你已经安装了酷Q和[coolq-http-api]插件并处于打开状态，否则无法正确运行本项目。
+ 安装nonebot，如果没有你可以键入如下命令：
```
pip install nonebot
```
+ clone本项目或下载zip包
+ 在根目录下创建config.py
+ 键入如下代码
```
# 设置超级用户，这里填写你的QQ，不是你机器人的QQ
SUPERUSERS = {你的QQ}

# 设置命令前缀，我这么设置就是 /命令 触发
COMMAND_START = {'/', '／'}
```
+ 阅读Nonebot的[文档],配置好coolq-http-api插件(IP为127.0.0.1,端口为8888)
+ 打开控制台，切换到项目根目录下
+ 输入如下命令
```
python Main.py
```
[coolq-http-api]: https://github.com/richardchien/coolq-http-api
[文档]: https://none.rclab.tk/guide/installation.html

## 可用命令
1. draw ——抽签命令，可抽到大凶，凶，小吉，中吉和大吉。
2. arkone | arkten ——明日方舟单抽|十连命令，目前定向为【强力干员】UP池。
3. azlight | azlightten ——碧蓝航线【轻型舰】单抽|十连指令。
4. azheavy | azheavyten ——碧蓝航线【重型舰】单抽|十连指令。
5. sleep ——随机禁言时长大礼包。


## 其他
所有的功能均在plugins文件夹下。 