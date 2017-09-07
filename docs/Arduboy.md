---
title: Arduboy
category: MakerPro
bzurl: https://www.seeedstudio.com/Arduboy-p-2728.html
oldwikiname:  Arduboy
prodimagename:  
wikiurl: http://seeed.wiki/Arduboy
sku:   114990348
---
##  1.	简介

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/Arduboy.png)

Arduboy是一个小型游戏系统，信用卡的大小。 它配备了一个经典的8位游戏，可以从在线的开源游戏库下载重新编程。 Arduboy是开源的，所以你可以学习编写和创建自己的游戏。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.3ff19e11bek4of&id=538077610061)

##   2.	如何下载新的游戏

本指南将教您如何设置您的计算机将游戏上传到您的Arduboy。

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/chipcloseup.jpg)

Arduboy右下角的小方块黑色芯片称为微控制器，它是设备的大脑。这个微小的8位计算机包含所有的指令，图形和声音，以产生在设备上播放的游戏。

### a. 下载Arduino IDE

我们可以对Arduboy重新编程，并使用USB电缆和Arduino软件来更改游戏。请点击[这里](https://www.arduino.cc/en/Main/Software#download)下载并安装Arduino IDE.

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/arduinocloseup.png)

### b. 管理库文件

- 在我们重新编程Arduboy之前，我们需要首先设置一些事情， 我们要下载一些需要编译Arduboy库文件。
- 编译代码意味着将人类可读的C ++代码转换为微控制器可以理解的二进制机器语言。
- 为了使芯片与OLED显示屏，按钮和扬声器一起工作，我们需要下载一些库。

请按照一下流程选择库管理器：

项目-->加载库-->管理库

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/librarycloseup.png)


### c. 下载库文件

找到它们的最简单的方法是搜索“Arduboy”

以下是我们建议安装的库文件列表：

- Arduboy
- Arduboy2
- ArduboyTones
- ArduboyPlaytune
- ArdBitmap
- ArdVoice
- ATMlib
- Arduboy-TinyFont

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/libraryinstall.PNG)

### d. 选择正确的板和端口

- 将Micro-USB电缆插入Arduboy并将其连接到PC。
- 使用顶部的电源开关打开Arduboy。
- 选择Arduino Leonardo板型（Arduboy基于Leonardo）

    工具-->开发板--> Arduino Leonardo

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/boardselection.png)

- 选择正确的端口号,每个计算机的端口号可以不同

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/portselection.png)

### e. 下载程序

首先我们选择一个Arduboy2库里面的程序， 大多数库包括几个程序，演示一些功能。

- 请根据一下流程进行选择，

    文件>示例> Arduboy2> Hello World

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/helloworld.png)

- 使用上传按钮上传程序

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/Uploading.png)

Arduino将尝试编译代码，并通过USB电缆将其传输到Arduboy。你就可以玩游戏了！


## 3. 游戏资源

![](https://github.com/SeeedDocument/Arduboy/raw/master/image/games.png)

你可以游览[Arduboy游戏网站](https://community.arduboy.com/c/games/demos)，来下载程序。网站是英文，可以通过类似Chome的在线翻译插件来预览。



