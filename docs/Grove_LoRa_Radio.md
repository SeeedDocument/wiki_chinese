---
name: Grove - LoRa Radio
category: Communication
bzurl: https://www.seeedstudio.com
oldwikiname: Grove - LoRa Radio
prodimagename: cover.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_LoRa_Radio
sku:  113060006/113060007
tags: grove_uart, io_3v3, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/cover.jpg)

Grove是由Seeed Studio开发的一个非常强大的平台，可以简化您的物联网项目。我们已经将grove连接器集成到Seeed生产的大多数主板上，以使它们成为一个系统。 这一次，我们将Grove与LoRa相结合，为您提供超远距离无线模块。

Grove-LoRa Radio 433MHz的主要功能模块是RFM98，它是一款采用LoRa远程调制解调器的收发器，可提供超长距离扩频通信且高抗干扰性，同时消耗微量电流。 Grove-LoRa Radio 433MHz的核心处理器是ATmega168，这是一种广泛使用的芯片，具有很高的性能和低功耗，特别适用于这个Grove模块。

我们已经集成了一个简单的线天线来接收信号，如果信号太弱，不用担心，天线旁边的MHF连接器可以用来增加一个带有MHF接口的天线，双天线可以获得更多的信号。

这是433MHz版本，可用于433MHz通信。 您还可以在Grove - LoRa Radio 868MHz上找到868MHz的版本。

|版本|发售日期|购买途径|
|--------|-----------|-----------|
|Grove-LoRa Radio 433 MHz |11月10日, 2016|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=686.1000925.0.0.17ccbf9eiIl3j2&id=548555603514)|
|Grove-LoRa Radio 868 MHz|11月10日, 2016|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ba5ddb14Dilnd&id=548157053504)|




##  产品特性
---
- 使用基于 SX1276 LoRa® 的 RFM95 模块
- 工作电压:5V/3.3V
- ~28mA(Avg) @+20dBm 持续传输模式
- ~8.4mA(Avg)@待机模式
- ~20mA(Avg) @接收模式, BW-500kHz
- 工作温度:-20 – 70℃
- 接口: Grove - UART(RX,TX,VCC,GND)
- 简易线天线或者带 MHF 连接头的高增益天线
- 工作频率:868MHz/433MHz
- 电源输出能力 +20dBm 100 mW
- 尺寸:20*40mm
- 速率:0.3kps~50kps
- 简单易用的 Arduino 库
- 备用可扩展 MHF 天线接头

!!!Tip
    更多关于 Grove 系统的资料请点击 [这里](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported


## 硬件概述
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/hardware.png)

1. ATMega168 MCU ([数据手册](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/Atmel-2545-8-bit-AVR-Microcontroller-ATmega48-88-168_Datasheet.pdf))
2. MHF 连接器
3. 板载线天线
4. RFM95 模块 ([数据手册](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/RFM95_96_97_98_DataSheet.pdf))
5. Grove 接口

|引脚|名字|功能|
|-------|--------|--------|
|1      |TX |TX of UART|
|2      |RX |RX of UART|
|3      |VCC|电源输入, 3.3V or 5V|
|4      |GND|连接到地|

## 创意应用
---
- Internet of Things
- 智能家居
- 传感器Hub
- 远距离无线通信

## 入门指导

在这一小节中您可以通过几步简单的设置来运行您的 **Grove - LoRa Radio**。

### 准备工作

现在我们使用 Grove - Lora Radio 433MHz 制作了一个P2P(点对点)通信的例程（Grove - Lora Radio 868MHz 同样适用于此例程）

!!!Tip
    Grove - LoRa Radio 433MHz 不能和 Grove - LoRa Radio 868MHz 进行通信.


|项目|数量|购买链接|
|----|---|----|
|Seeeduino Lotus|2|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.2e3cf570Y040Gb&id=555795386924)|
|Grove - LoRa Radio 433MHz|2|[点击购买](https://item.taobao.com/item.htm?spm=686.1000925.0.0.17ccbf9eiIl3j2&id=548555603514)|
|Micro USB 数据线|2|[点击购买](https://item.taobao.com/item.htm?spm=686.1000925.0.0.36f9b4ceokjr0U&id=45774308858)|

如果这是您第一次使用 [Seeeduino Lotus](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.2e3cf570Y040Gb&id=555795386924), 请参考阅读 [Seeeduino Lotus's 中文 wiki](http://wiki.seeedstudio.com/cn/Seeeduino_Lotus/).

Seeeduino Lotus 完全兼容 Arduino， 并且和 Arduino 一样简单易用.

如果这是您第一次使用 Arduino, 请点击 [这里](http://arduino.cc) 查阅相关资料。

### 硬件连接

Seeeduino Lotus 是 Seeeduino 和 Base Shield 的完美融合。我们可以通过 **D5** 端口直接将 LoRa Radio 模块和开发板相连。如下图所示:

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/demo.jpg)


### 库文件下载

点击下面橙色框条下载并安装库文件，如果您不清楚怎么安装，请参考 ([Arduino 库安装指南](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/))

[![](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/library.png)](https://github.com/Seeed-Studio/Grove_LoRa_433MHz_and_915MHz_RF/archive/master.zip)

### 打开示例程序

打开您的 Arduino IDE, 点击 **File(文件)> Examples（示例）>Grove_LoRa_433MHz_and_915MHz_RF-master** 您将看到数个关于这个模块的示例程序。

![](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/library_2.png)

|节点|示例名称|功能|
|----|------------|--------|
|发送器|rf95_client|每秒一次发送 "Hello World"|
|接收器|rf95_server|接收数据并且打印出来|

点击 **Tools（工具）>Board（开发板）** 选择 **Seeeduino Lotus** ,然后选择当前对应的串行端口。选择完成之后点击 **Upload** 按钮，至此完成，您可以享受自己的程序了。


!!!Tip
    如果您使用的是 **Grove - LoRa Radio 868MHz** 模块，请修改下列代码。

```c
//rf95.setFrequency(434.0);
rf95.setFrequency(868.0);
```

### 查看结果

当上传完成后，您就可以打开串口监视器来查看您传输的数据了。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/result.jpg)

### 数据传输速率

下图显示了带宽信号带宽扩展因子和灵敏度之间的关系。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_LoRa_Radio/master/img/DateRate.png)


## 资源下载
---

* **原理图**
    *   [Grove - LoRa Radio 433MHz v1.0 Schematics (Eagle files)](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/433_eagle.zip)
    *   [Grove - LoRa Radio 433MHz v1.0 Schematics (PDF files)](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/433_sch.pdf)
    *   [Grove - LoRa Radio 868MHz v1.0 Schematics (Eagle files)](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/868_eagle.zip)
    *   [Grove - LoRa Radio 868MHz v1.0 Schematics (PDF files)](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/868_sch.pdf)

* **数据手册**
    *   [RFM95/96/97 Datasheet](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/RFM95_96_97_98_DataSheet.pdf)
    *   [Atmega168 Datasheet](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/Atmel-2545-8-bit-AVR-Microcontroller-ATmega48-88-168_Datasheet.pdf)

* **参考资源**
    *   [LoRa Alliance](https://www.lora-alliance.org/)

* **库文件**
    *   [Grove - LoRa Radio Library and Examples](https://github.com/Seeed-Studio/Grove_LoRa_433MHz_and_915MHz_RF/)

* [**上面的我都要下载**](https://github.com/SeeedDocument/Grove_LoRa_Radio/blob/master/res/res.zip)
