---
title: Seeeduino Lotus
category: Arduino
bzurl: https://www.seeedstudio.com/Seeeduino-Lotus-ATMega328-Board-with-Grove-Interface-p-1942.html
oldwikiname: Seeeduino_Lotus_v1.0
prodimagename: Seeeduino_Lotus_Cover.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Seeeduino_Lotus
sku: 102020001
---

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/Seeeduino_Lotus_Cover.jpg)

Seeeduino Lotus 是一款 ATMEGA328 微控制器开发板。它是 Seeeduino 和 Base Shield 的组合。它使用了 Atmel ATMEGA328P-MU 芯片和 CH340 芯片。ATMEGA328P-MU 是一款高性能，低功耗的 AVR 8 位微控制器。CH340 是可以实现 USB 到串行接口的 USB 总线转换器芯片。Seeeduino Lotus有 14 个数字输入/输出（其中 6 个可以输出 PWM）和 7 个模拟输入/输出，一个 micro USB 接口，一个 ICSP 接口，12 个 Grove 接口和一个复位按钮。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.44.5acce809o3Zgtt&id=555795386924)



!!!Warning
  Seeeduino Lotus 1.0 支持 Windows 操作系统。Seeeduino Lotus 1.1 支持 Window 和 Mac系统。

## 版本
---
| 版次 | 说明                                              | 发布时间      |购买链接|
|----------|-----------------------------------------------------------|--------------|--------------|
| v1.0   | 初次公开发布（测试版）                             | 七月 22, 2014  |不再销售|
| v1.1   | 用 CP2102 替换了 CH340 ，支持 MAC |十二月 22,2016   |[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/get_one_now_small.png)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.47ef4a7485JMQt&id=555795386924)|

## 创意应用

* DIY
* IoT 和智能家居
* 机器人
* 学习
* 玩具

这里有一些有趣的案例跟您参考。

|Car Controlled by Track Ball|FM Receiver|Make a Wooden Gun|
|-------|-------|-------|
|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/example_1.png)|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/Fm%20demo.jpg)|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/gun.jpg)|
|[Make it Now](http://www.seeed.cc/A-Car-Controlled-by-Track-Ball-p-1132.html)|[Make it Now](/FM_Receiver/)|[Make it Now](http://www.instructables.com/id/DIY-a-Wooden-Laser-Gun-As-a-Xmas-Present-for-Your-/)|


## 产品特性

* 与 Arduino UNO 完全兼容
* ATmega328 微控制器
* 板载 12 个 Grove 接口
* 14 个数字 I/O 引脚 (6 路 PWM 输出)
* 6 模拟输入
* 有 ISP 接口
* 与 Arduino UNO-R3 Shield 兼容
* 使用 Micro USB 上传代码和供电
* 5V 工作电压


## 规格参数

|项目|参数|
|------------|-----------|
|微控制器|ATmega328P-MU|
|工作电压|5V|
|数字 I/O 引脚|14|
|PWM 通道|6|
|模拟输入通道|7|
|每个 I/O 引脚最大直流电流|40 mA|
|Flash 存储|32 KB|
|RAM|2 KB|
|EEPROM|1 KB|
|时钟频率|16 MHz|


## 硬件概述

下图显示了 Seeeduino Lotus 硬件功能的概述。 Seeeduino Lotus 的各种引脚的主要功能和复用功能如引脚图所示。这可以作为快速参考。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/seeeduino_lotus_hardware_overview.jpg)


- **LED-D13**
这个 LED 连接到板子的 D13 引脚，这可以作为程序或项目的板载 LED 指示灯。
- **USB Input**
USB 端口用于将电路板连接到 PC 进行编程和供电。Micro USB 是大多数 Android 手机和其他设备常用的 USB 接口。 你可能有几十根这些电缆散落在你家附近。
- **Reset**
为了方便使用，重置按钮被放置在板子侧面，这样即使把其他扩展板放在 Seeeduino 上时也能轻松按下。在其他 Arduino 板上并不是这样，按钮放在顶部，使其在某些情况下很难按下。
- **Power Pins & Analog Pins**
就像哪些额外的数字接口一样，当人们在做某些项目需要用不止一个传感器或执行器时，他可能需要不止一个电源接口，有这些额外的接口就避免了使用扩展板的麻烦。
- **Grove Connectors**
SeeedStudio 具有可以利用这些模拟，数字，I2C和 UART 连接的各种传感器/设备。 此外，我们销售独立的 Grove 连接线，以帮助您制作我们自己的传感器连接。
- **ICSP**
这是 ATmega328P 的 ICSP 接口，它位于可以使用此连接器的 Arduino Uno，Due，Mega 和 Leonardo 兼容硬件（例如扩展板）的标准 ICSP / SPI 位置。 该端口的 SPI 引脚： MISO，SCK 和 MOSI 也分别连接到数字引脚 12,13 和 11，就像 Arduino Uno 那样。
- **USB 2 Uart**
通过将板载 ATmega328 置于复位模式，这些焊盘可用于与其他 UART 器件交互。 这使得 Seeeduino Lotus 可以使用 USB2UART 扩展板。

!!!Warning
    使用 micro USB 时要小心操作，否则可能会使插座脱落。



## 安装驱动

首先，你需要：

* **找到一根 Micro-USB 线**
首先你需要一根 Micro-USB 线。Android 手机的数据线就再好不过了。
如果你找不到，请在 [这里](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.51.1a5d16b7OzmgfO&id=45774308858) 购买。

* **连接电路板**
使用 USB 线把电路板连接到电脑上。绿色的电源 LED (标志是 **PWR**) 应该会亮起来。


!!!Note
    CH340 的驱动 (Seeeduino_Lotus V1.0) 支持 Windows XP, Windows Vista, Windows 7, Windows 8/8.1 和 Windows 10.

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/download_driver_for_seeeduino_lotus.png)](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/CH341SER.EXE)

双击打开驱动并安装。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/driver_install.png)

!!!Note
    CP2102N 驱动 (Seeeduino_Lotus V1.1) 支持 Windows XP, Windows Vista, Windows 7, Windows 8/8.1, Windows 10 and Mac.

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/download_driver_for_seeeduino_lotus.png)](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)  

## 入门指导

!!!Note
    这部分基于 Windows 10 下的 Arduino 1.6.9。

首先，你需要安装 Arduino 软件

[![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Stalker_V3_1/master/images/Download_IDE.png)](https://www.arduino.cc/en/Main/Software)


**启动 Arduino 应用程序**

双击下载好的 Arduino 应用 (arduino.exe) 。

!!!Note
    如果 Arduino 软件以不同的语言加载，您可以在 Preferences 对话框中进行更改。更多详细信息，请参阅 [Arduino Software (IDE) page](https://www.arduino.cc/en/Guide/Environment#languages) 。


**打开 Blink 示例**

打开 LED blink 示例目录 **File（文件） > Examples（示例） >01.Basics > Blink**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_GPRS/master/img/select_blink.png)

**把 Seeeduino Lite 添加到 Arduino IDE**

Arduino IDE 的开发板中没有 *Seeeduino Lite* 选项, 打开用法说明 [如何把 Seeed 开发板添加进 Arduino IDE](http://wiki.seeed.cc/Seeed_Arduino_Boards/) 操作。

**选择你的板子**
打开目录菜单 **Tools（工具） > Board（开发板）** 并选择你的 Arduino 型号。
这次请选择 **Seeeduino Lotus**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/select_seeeduino_lotus.jpg)

**选择使用的串口**
从 **Tools（工具） | Serial Port（端口）** 中选择 Arduino 板的串口号。 这可能是 COM3 或数字更大的串口（**COM1** 和 **COM2** 通常为硬件串行端口保留）。如果您不知道是哪个，您可以断开 Arduino 板并重新打开菜单; 消失的条目应该是 Arduino 板。重新连接电路板并选择该串行端口。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/select_com.jpg)


**上传代码**
现在，你只需要点击页面中的 "**Upload（上传）**"按钮。等待数秒，如果上传成功，状态栏中就会显示 "Done uploading"。
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_GPRS/master/img/upload_image.png)

上传结束后，你会看到板子上的引脚 13 LED 开始闪烁（橘黄色）。如果是的，按恭喜你！你已经学会了 Arduino 的下载和运行。如果您遇到问题，请参考文末的 **常见问题**。


## 资源下载

* **原理图**
    * **[Eagle 文件]**[Seeeduino Lotus Eagle file V1.0](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino_Lotus_v1.0_Sch.zip)
    * **[Eagle 文件]**[Seeeduino Lotus Eagle file V1.1](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino_Lotus_v1.1.zip)
    * **[PDF 文件]**[Seeeduino Lotus SCH PDF file V1.0](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino_Lotus_v1.0_SCH.pdf)
    * **[PDF 文件]**[Seeeduino Lotus SCH PDF file V1.1](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino%20Lotus%20v1.1%20SCH.pdf)
    * **[PDF 文件]**[Seeeduino Lotus PCB PDF file V1.0](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino_Lotus_v1.0_PCB.pdf)
    * **[PDF 文件]**[Seeeduino Lotus PCB PDF file V1.1](https://github.com/SeeedDocument/Seeeduino_Lotus/raw/master/res/Seeeduino%20Lotus%20v1.1%20PCB.pdf)

* **数据手册**
    * [ATmega328P](https://github.com/SeeedDocument/SeeeduinoV4/raw/master/res/ATmega328.pdf)
    * [ATmega16U2](https://github.com/SeeedDocument/SeeeduinoV4/raw/master/res/ATmega16u2.pdf)

* **引导装在程序**    
    * [Seeeduino Lotus Bootloader](https://github.com/SeeedDocument/Seeeduino_Lotus/blob/master/res/Seeeduino_Lotus_v1.0_pdf.pdf)

* **相关参考**
    * [Getting Started with Arduino](https://www.arduino.cc/en/Guide/HomePage)
    * [Arduino Language Reference](https://www.arduino.cc/en/Reference/HomePage)
    * [Download the Arduino Software(IDE)](https://www.arduino.cc/en/Main/Software)
    * [Arduino FAQ](https://www.arduino.cc/en/Main/FAQ)
    * [Arduino Introduction](https://www.arduino.cc/en/guide/introduction)
    * [Wikipedia page for Arduino](https://en.wikipedia.org/wiki/Arduino)
    * [Seeeduino Lotus V1.1 USB Driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)

## 常见问题

**Q1.  Arduino UNO 和 Seeeduino Lotus 之间有什么区别。**

Seeeduino Lotus 是 Arduino UNO的完全兼容开发版。 并且 Seeeduino Lotus 有 12 个 Grove 接口，这就使使用 Seeed Studio Grove 模块搭建项目变得非常容易。并且 Seeeduino Lotus 使用 Micro USB 来编程和供电。

**Q2. 我不能向 Seeeduino Lotus 上传代码。**

请检查，

* 电源指示 LED 是否亮着
* 你是否选择了正确的端口和板子(Seeeduino Lotus)
* 重新打开 Arduino IDE 并再试一次

**Q3. 如果我有了新想法，我在哪儿可以得到更多的技术支持。**

你可以在 [Seeed Forum](http://www.seeed.cc/discover.html?t=Arduino) 中发帖或发送邮件到 **techsupport@seeed.cc**。
