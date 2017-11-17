---
title: Arduino Breakout for LinkIt Smart 7688 Duo
category: LinkIt
bzurl: https://www.seeedstudio.com/Arduino-Breakout-for-LinkIt-Smart-7688-Duo-p-2576.html
oldwikiname: Arduino Breakout for LinkIt Smart 7688 Duo
prodimagename: Arduino_Breakout_for_LinkIt_Smart_7688_Duo_product_view.jpg
wikiurl: http://seeed.wiki/Arduino_Breakout_for_LinkIt_Smart_7688_Duo
sku: 103030033
---


**Arduino Breakout for LinkIt Smart 7688 Duo** 是 LinkIt Smart 7688 Duo 的扩展板。和 Seeed 生产的其他扩展板一样，该主板集成了 12 个 Grove 接口，可以让您轻松连接更多的 Grove 模块。这个扩展板简化了麻烦的接线过程，能够让初学者快速入门。更重要的是，这块板子与 Arduino 共用同一个 MUC，这意味着您不仅可以使用 LinkIt Smart 7688 的功能，而且可以使用 ArduinoYún 的功能，这使您可以使用强大的 Arduino IDE 编译丰富的 IoT 应用程序。在主板上有 LinkIt Smart 7688 Duo 的预留接口，除此之外，它还支持 I2C，UART 等串行总线，并带有 USB 和以太网接口。

![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/Arduino_Breakout_for_LinkIt_Smart_7688_Duo_product_view.jpg)

LinkIt Smart 7688 Duo是基于 OpenWrt Linux 开发板，MT7688 和 ATmega32u4 的开源扩展板。 该板设计用于实现智能家居的丰富应用。 如果你想了解更多关于 LinkIt Smart 7688 Duo 的信息，请点击 [这里](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688_Duo)。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.7c809e6dpB5VGB&id=524889454698)

## 产品特性

- 兼容 Arduino Shield
- 可以连接互联网
- USB 2.0 支持更多外设
- Grove 接口：I2C × 2, 模拟接口 × 3, 数字接口× 6, UART × 1
- 4-pin 调试接口 × 1, ICSP × 1

## 创意应用

- 物联网/网关应用
- 机器人
- 智能多媒体设备
- 教学

## 规格参数

- **输入电压** ：5.0V (使用 USB 接口供电)
- **工作电压** ：3.3V

!!!Note
    调试引脚连接到 MT7688, 其他引脚连接到 ATmega32U4.

## 硬件概述

![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/Arduino_Breakout_for_LinkIt_Smart_7688_Duo_components_with_text_1200_s.jpg)

|项目|数量|项目|数量|
|---|---|---|---|
|Arduino Shield|1|USB Port(Type-A)|1|
|MT7688 UART2|1|USB Port(Micro type-B)|1|
|ICSP port|1|Ethernet Port|1|
|Reset Button(ATmega32u4)|1|连接 LinkIt Smart 7688 Duo 的端口|1|


## 开始使用

在这个简单的应用中，您将使用蜂鸣器来发出不同的声音。开始之前，除了 Arduino Breakout for LinkIt Smart 7688 Duo 之外，请检查下面是否有以下材料。你可以在我们的商城里购买它们。

|LinkIt Smart 7688 Duo|USB cable|UARTBee |Jumper wires x 3|Grove - Buzzer
|---|---|---|---|---|
|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/102110017%206.jpg)|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/48cmUSBc.jpg)|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/UartSBee%20V5_01.jpg)|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/jw100n.jpg)|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/107020000%201.jpg)
|[**点击购买**](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.19ca325f3hsHgc&id=524898724024)|[**点击购买**](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.20.236d7a2eFXj0XP&id=45774308858)|[**点击购买**](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.273fab14FtSbos&id=45486590205)|[**点击购买**](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.7c22550dnnDU6v&id=45783422315)|[**点击购买**](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.41a783f1qVIxqP&id=520245748676)

- 第一步：请参考 [这里](http://seeed.wiki/LinkIt_Smart_7688_Duo/) 把你的 LinkIt Smart 7688 Duo 连接到互联网。

!!!Note
    * 您可以在连接 LinkIt Smart 7688 的端口附近找到 8，9 和 GND 引脚。
    * 您可以用跳线连接 MT7688 UART2 端口，而不是将其焊接到引脚 8，引脚 9 和引脚 GND。

- 第二步：将 USB to Serial adapter 连接到 LinkIt Smart 7688 Duo 后打开控制台。
- 第三步：按下图所示连接各部件：

![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/Arduino_Breakout_for_LinkIt_Smart_7688_Duo_demo_connection_view_1200_s.jpg)

- 第四步：把 Grove - Buzzer 插在 **D4** 口上。

- 第五步：这一步是在主机上为 LinkIt Smart 7688 Duo 平台搭建 Arduino 开发环境。由于本教程已经在 LinkIt Smart 7688 的 Wiki 中编写，如有需要请参阅 [这里](http://seeed.wiki/LinkIt_Smart_7688_Duo/#arduino)。
- 第六步：下载 firmata.
- 第七步：参考 [这里](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688_Duo#Installing_Arduino_programming_environment) 安装 Arduino IDE 的 LinkIt Smart 7688 平台，然后把文件 firmata 保存到开发板。

!!!Note
    以下步骤应在嵌入式操作系统（OpenWRT）上执行。 请确保你的系统中有 Python，并且安装了 pip。

- 第八步：在控制台输入 pip 安装 pyfirmata，然后按 Enter 安装 python 库 pyfirmata。
- 第九步：在控制台中输入 **vi buzzer.py** 创建一个名为 **buzzer.py** 的文件，将下面的代码复制过去。

```python
from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyS0')
print "Start blinking D4"
while True:
  board.digital[4].write(1)
  sleep(0.5)
  board.digital[4].write(0)
  sleep(0.5)
```

- 第十步：保存 **buzzer.py** 并输入 **python buzzer.py** 来运行示例代码。
- 第十一步：现在你会听到蜂鸣器的声音。

## Make It Now
Have you successfully make the buzzer to buzz? Here are 2 more awesome projects that use LinkIt Smart 7688 Duo. Let's make them now!


|Smart Router With <br>WiFi Connection Visualization|Facebook Like Monitor|
|:---:|:---:|
|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/F9SCHIKIPH4SPTP.MEDIUM.jpg)|![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/F9MQJJOIHQOBV4Q.MEDIUM.jpg)|
|[![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/200px-Wiki_makeitnow_logo.png)](http://www.instructables.com/id/ReRouter-Make-an-Extensible-IoT-Router/)|[![](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/images/200px-Wiki_makeitnow_logo.png)](http://www.instructables.com/id/Facebook-Like-Monitor/)|


## 资源下载

- **[原理图]**[Schematic files](https://github.com/SeeedDocument/Arduino_Breakout_for_LinkIt_Smart_7688_Duo/raw/master/resources/Schematic_files_for_Arduino_Breakout_for_LinkIt_Smart_7688_Duo.zip)
- **[Wiki]**[Wiki link for LinkIt Smart 7688 Duo](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688_Duo)
- **[指南]**[OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
