---
title: Grove - Bee Socket
category: Communication
bzurl: https://www.seeedstudio.com/Grove-Bee-Socket-p-1449.html
oldwikiname:  Grove - Bee Socket
prodimagename: LFUUlWtcc3wNmrxDp3yjPy7I.jpg
surveyurl: https://www.research.net/r/Grove_Bee_Socket
sku:  103020002
---

![](https://github.com/SeeedDocument/Grove-Bee_Socket/raw/master/img/Bee_Socket_01.jpg)

Grove - Bee Socket 是 Xbee 系列的适配器，其无线模块可以与Arduino连接，如 WIFI Bee，RF Bee，Bluetooth Bee 等。它与 Arduino 兼容且能更有效地通过无线网络进行对网状网络的运行。 稳压器 CJT1117 保证了 Xbee 稳定的 3.3 电压。 LED 可以清楚地显示 grove 的工作模式。
Grove-Bee Socket 与 [XBee Shield](/XBee_Shield_V2.0) 具有相同的功能。 Grove-Bee Socket和 Arduino 通过连接线连接，XB Shield 是可以连接到 Arduino 的标准适配器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2571febF8DwHR&id=526471153414)


##  产品特性
---
* 标准 Bee Socket 引脚和 Grove 接口

* 板载 3.3V 稳压器为 XBee 供电

* 电平转换电路

* Bee Socket 具有复位按钮

* 具有 Bee Socket 显示的 LED

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-Bee_Socket/raw/master/img/Bee_Socket_Interface.jpg)

**J1:** Grove 接口，用于连接 Arduino / Seeeduino 的 UART 接口。

**J2,J3:** 针对 Xbee 的每个引脚的连接接口。

**J4,J5:** Bee 引脚

**U1:** CJT1117 IC，低压差线性稳压器。 用于 XBee 模块的 3.3V 电源。

**U2,U3:**  SN74LVC1G125 IC，保护您的 XBee 免受 5V 电压，并转换为 3.3V。


**RSSI indicator:** XBee RX 信号强度指示。

**PWR LED:** 电源指示灯

**ASSOC indicator:**  Xbee 相关指标.

**ON/SLEEP LED:** XBee 模块状态指示灯.

##  使用方式
---
使用 Grove - Bee Socket，可以很容易地控制 Arduino / Seeeduino 的 Bee Socket 。 这里以 RF bee 为例，我们将告诉您如何使用它。

* 将 XBee 模块连接到 bee 引脚。

* 使用 Grove 连接线将 Grove - Bee Socket 连接到 Arduino / Seeeduino 的 **UART接口**。 并将您的 Arduino / Seeeduino 通过 USB 数据线连接到计算机。

![](https://github.com/SeeedDocument/Grove-Bee_Socket/raw/master/img/Grove-Bee_Socket.jpg)

* 现在，您可以发送一些简单的 AT 命令，为 RF bee 和发送/接收数据做一些基本配置。 当然，您可以在不更改硬件连接的情况下更新固件。

如果您需要有关如何通信的更多信息，请参阅相关 bee 模块的 WIKI 页面。

##  资源下载
---
[Bee Socket Eagle File](https://github.com/SeeedDocument/Grove-Bee_Socket/raw/master/res/Bee_Socket_Eagle_File.zip)
