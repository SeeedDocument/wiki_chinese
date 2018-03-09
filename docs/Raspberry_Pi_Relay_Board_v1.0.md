---
title: Raspberry Pi Relay Board v1.0
category: Raspberry Pi
bzurl: https://seeedstudio.com/Raspberry-Pi-Relay-Board-v1.0-p-2409.html
oldwikiname: Raspberry_Pi_Relay_Board_v1.0
prodimagename: Raspberry_Pi_Relay_Board_v1.0.jpg
wikiurl: http://seeed.wiki/Raspberry_Pi_Relay_Board_v1_0
sku: 103030029
---

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/master/img/Raspberry_Pi_Relay_Board_v1.0.jpg)

Raspberry Pi Relay Board v1.0 搭载四个高质量继电器，并提供控制高电流负载的 NO/NC 接口。这意味着它是用于控制那些无法直接由 I2C 总线控制的设备一个极好的解决方案。标准化扩展板外形使其能和树莓派完美连接。扩展板还有四个显示每个继电器的开/关状态的指示灯。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=521183992607)



## 产品特性
--------
-   Raspberry Pi 兼容
-   接口 : I2C，三个硬件SW1 ( 1, 2, 3) 选择固定的 I2C 总线地址
-   继电器螺丝端子
-   标准化扩展板的形状和设计
-   对应每个继电器的 LED 工作状态指示灯
-   每个继电器上留有 COM，NO (常开) 和 NC (常闭) 引脚
-   高品质的继电器

## 规格参数
--------------

<table border="1" cellspacing="0" width="800">
<tr>
<th scope="col">
参数
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
Unit
</th>
</tr>
<tr align="center">
<th scope="row">
电源电压
</th>
<td>
4.75
</td>
<td>
5
</td>
<td>
5.5
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
工作电流
</th>
<td>
10
</td>
<td>
/
</td>
<td>
360
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
开关电压
</th>
<td>
/
</td>
<td>
/
</td>
<td>
30/250
</td>
<td>
VDC/VAC
</td>
</tr>
<tr align="center">
<th scope="row">
开关电流
</th>
<td>
/
</td>
<td>
/
</td>
<td>
15
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
频率
</th>
<td>
/
</td>
<td>
1
</td>
<td>
/
</td>
<td>
HZ
</td>
</tr>
<tr align="center">
<th scope="row">
开关电源
</th>
<td>
/
</td>
<td>
/
</td>
<td>
2770VA/240
</td>
<td>
W
</td>
</tr>
<tr align="center">
<th scope="row">
继电器寿命
</th>
<td>
100,000
</td>
<td>
/
</td>
<td>
/
</td>
<td>
Cycle
</td>
</tr>
<tr align="center">
<th scope="row">
外形尺寸
</th>
<td colspan="3">
91.20 × 56.15 × 32
</td>
<td>
mm
</td>
</tr>
</table>


!!!Caution
    在 Arduino 的 USB 接口顶部捆绑 2 层电工胶带。这将防止继电器扩展版发生接触。请勿操作超过 35V DC 的电压。

## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/master/img/Raspberry_Pi_Relay_Board_v1.0_p3.jpg)

## 使用方法
-----
本节由 John M. Wargo 撰写，在此我们要感谢 John 的贡献。我们已经对原文进行了一些修改，使之更适合 Seeed 的文档格式。请点击 [这里](http://johnwargo.com/microcontrollers-single-board-computers/using-the-seeed-studio-raspberry-pi-relay-board.html) 访问原始文档。

安装电路板并检验其是否正常工作包括以下步骤 :

- **步骤 1** : 将扩展板堆叠在树莓派上。
- **步骤 2** : 启用 Raspbian I2C 软件界面。
- **步骤 3** : 验证 Raspberry Pi 识别扩展板。
- **步骤 4** : 运行一些 Python 代码来使用扩展板。

### 步骤 1. 安装扩展板

安装扩展板很容易，您需要将它的排母堆叠到 Raspberry Pi 板的引脚上。注意 : 您必须添加排公到 Raspberry Pi Zero 才能使用该扩展板。

在安装扩展板之前，我们建议您在 Raspberry Pi 以太网端口的顶部捆绑放置一些电工胶带。如果您在不使用支架的情况下安装扩展板 (正如我在下面的示例中所做的那样)，则扩展板有可能会与以太网端口外壳发生接触并产生问题。

![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-01.png)
**图 1**

对于生产项目，我们推荐使用支架来保持板的位置。

扩展板最初和较老的 Raspberry Pi 搭配使用，它带有 26 个针头，所以当你将它和带有 40 针头的 Raspberry Pi 搭配使用时，你需要将引脚数字对齐。如果没有正确对齐引脚，后期会出现问题，因为它无法正常工作。


### 启用 I2C

扩展板通过 [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) 接口与 Raspberry Pi 通信。Raspbian 操作系统默认禁用该接口，因此在使用该板之前必须先将其打开。启动 Raspberry Pi 到图形界面。打开 Pi 菜单，选择 **Preferences**，然后选择 **Raspberry Pi Configuration**，如下图所示 :

![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-02.png)

**图 2**

在打开的窗口中，选择 **Interfaces** 选项卡，如下图所示。如图所示，启用 I2C 选项，然后单击 **OK** 按钮继续。当你重启电脑时，Raspberry Pi 可以识别到扩展板。在下一节中，我们将验证。

![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-03.png)

**图 3**

### 验证识别

启用 I2C 接口后，就可以确定 Raspberry Pi 是否识别到扩展板。打开终端窗口并执行以下命令 :
```
i2cdetect -y -r 1
```
程序显示已识别 I2C 设备，如下图所示。在本例中，系统上只有一个 I2C 板，扩展板地址配置为 20。后文将展示这个值的重要性。

![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-04.png)

**图 4**

您可以使用扩展板上的开关来设置 I2C 地址，板上有 4 个 DIP 开关，让我们看看当更改它们时会发生什么。

有四个开关，三个标记为 **A0** 到 **A2**，一个标记为 **NC**。NC 表示未连接未使用。每个开关都有一个高电平和一个低电平的设置，下面的表格介绍了如何使用它们为扩展板设置一个 I2C 地址 :

|A0| A1 |A2 |地址|
|---|---|---|---|
|高电平|高电平|高电平|20|
|低电平|高电平|高电平|21|
|高电平|低电平|高电平|22|
|高电平|高电平|低电平|24|
|高电平|低电平|低电平|26|
|低电平|低电平|低电平|27|

### 运行测试程序

请使用 [github repository](https://github.com/johnwargo/Seed-Studio-Relay-Board) 中的测试代码。抓取代码后，您将轻松完成以下步骤。

欲运行测试程序，请打开一个终端窗口，导航到您已经提取示例程序的位置，然后使用以下命令运行程序 :

```
python ./seeed_relay_test.py
```
![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-05.png)

**图 5**

当提示输入时，您需要输入命令以启动和关闭继电器 :

- 键入 1on，2on，3on 或 4on，然后按回车将使指定的继电器启动。
- 输入 1off，2off，3off 或 4off，然后按回车将使指定的继电器关闭。
- 键入 allon 或 alloff 将启动或关闭所有继电器。


### 使用 Python 模块
要在您自己的 Python 程序中使用该模块，请将模块 (relay_lib_seeed.py) 复制到您的项目文件夹中，然后通过将以下行添加到程序的开头，将模块导入到 Python 程序中 :

>from relay_lib_seeed import *

这为您的程序提供了一系列功能 :

- relay_on(int_value) - 启动一个继电器。将 1 至 4 之间的整数值赋给函数，指定要启动的继电器。例如：relay_on(1) 将启动第一个继电器 (实际上是内部继电器 0)。
- relay_off（int_value） - 关闭一个继电器。将 1 至 4 之间的整数值赋给函数，指定要关闭的继电器。例如：relay_on(4) 将关闭第四个继电器 (实际上是内部继电器 3)。
- relay_all_on()  - 同时启动所有继电器。
- relay_all_off() - 同时关闭所有的继电器。

这里涉及一个前文提及非常重要的配置值:

```
# 7 bit address (will be left shifted to add the read write bit)
DEVICE_ADDRESS = 0x20
```

还记得这个值吗 ? 这可是该板的默认地址。如果要改变开发板上的开关，则需要相应更新此变量。

要查看该模块，请在 Raspberry Pi 上打开一个终端窗口，导航到解压该存储库文件的文件夹，然后执行以下命令 :
```
python ./relay_lib_seeed_test.py
```
程序将会 :

- 启动所有的继电器一秒
- 关闭所有的继电器
- 循环启动每个继电器 (1 到 4) 一秒

该模块将向控制台写入指示符，执行每个步骤，如下图所示 :

![](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/img2/seed-figure-06.png)

**图 6**

继电器启动时，扩展板上的 LED (每个继电器对应一个 LED)将点亮。

代码如下所示 :

```
# turn all of the relays on
relay_all_on()
# wait a second
time.sleep(1)
# turn all of the relays off
relay_all_off()
# wait a second
time.sleep(1)
# now cycle each relay every second in an infinite loop
while True:
for i in range(1, 5):
   relay_on(i)
   time.sleep(1)
   relay_off(i)
```

## 资源下载
---------
- **[Eagle 文件]** [Raspberry_Pi_Relay_Board_v1.0_sch_pcb](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/master/res/Raspberry_Pi_Relay_Board_v1.0_sch_pcb.zip)
- **[原理图 PDF]** [Raspberry_Pi_Relay_Board_v1.0_PDF](https://github.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/raw/master/res/Raspberry%20Pi%20Relay%20Board%20v1.0.pdf)
- **[芯片数据手册]** [HLS8L Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/master/res/HLS8L.pdf)
- **[芯片数据手册]** [PCAL9535A Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Relay_Board_v1.0/master/res/PCAL9535A.pdf)
- **[其他资源]** [Test Code](https://github.com/johnwargo/Seed-Studio-Relay-Board)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Relay_Board_v1.0 -->
