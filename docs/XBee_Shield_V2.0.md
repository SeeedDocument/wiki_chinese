---
title: XBee Shield V2.0
category: Shield
bzurl: https://www.seeedstudio.com/XBee-Shield-V2.0-p-1375.html
oldwikiname:  XBee Shield V2.0
prodimagename:  Xbeeshield_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/XBee_Shield_V2.0
sku:   103030004
---

![](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/img/Xbeeshield_01.jpg)

新版本的 XBee Shield 是与 Arduino 兼容的标准化和可堆叠的 shield。您可以轻松地将 Bee 系列中的任何模块堆叠到其上，并为您的项目构建无线网络。不仅如此，它还具有可实现高与低电平之间的双向转换的电平转换功能；低 IO 级别，保留的数字引脚方便用户使用跳线帽选择 TX/RX 端口。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1e9c18bEiH4xQ&id=520300891576)

##   产品特性
---
-  标准化形状设计
-  可以通过由 UartSBee 模块连接到 USB 进行配置
-  **DIN** 和 **DOUT** 引脚可以连接 **UART** 和其他数字引脚( **D2**~**D12** )
-  为您的项目增加可使用空间
-  LED 指示灯

## 兼容性
---

我们已经生产了大量扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里使用表格来说明扩展板和平台板之间的兼容性。

!!!note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。 如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc. 联系。

**点击查看全图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 硬件概述
---
![](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/img/XBee_Shield_Interface%202.jpg)

- U2：[CJT1117 芯片](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/CJT1117_datasheet.pdf) 为 XBee 模块提供 3.3V 的电压。
- U3：[SN74LVC1G125 芯片](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/SN74LVC1G125DCKR.pdf) 实现板上 Xbee RX 管脚和 Arduino 管脚的电平转换。

##   入门指导
---

这里我们将向您展示这款 XBee Shield V2.0 与 RF Bee 的配合。也可以使用 Bluetooth Bee 或其他模块来配合。

| XBee Shield V2.0 | RF Bee |
|----------------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/img/XBee%20Shield%20V2.0_s.jpg)|![enter image description here](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/img/rfbee1_s.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1e9c18bEiH4xQ&id=520300891576)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.469ff229ySUUdU&id=45673535399)|

- 将 RF Bee 插入 Xbee Sheild V2.0。

 ![](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/img/XBee_Shield_connect_RF_XBee.jpg)

- 使用跳线帽**连接 XB_TX 和数字 4**。另外，使用跳线帽连接**XB_RX 和数字 5**。当然，您可以根据需要更改数字端口。但是不要忘了在演示代码的定义中同时更改端口号。

!!!note
        以下是已知的限制 :

        1. 如果使用多个软件串行端口，同一时间只有一个端口能接收数据。
        2. 并非所有 Mega 和 Mega 2560 的引脚都支持更改中断，因此只有以下可用于 RX : 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69。
        3. 并不是所有 Leonardo 上的引脚都支持更改中断，只有以下可以用于 RX : 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI)。

如果您需要有关如何通信的更多信息，请参阅相关模块的 Wiki 页面。

##   Resource
---
- **[Eagle文件]** [XBee Shield V2.0 Eagle File](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/XBee_Shield_Eagle_file.zip)
- **[原理图PDF]** [XBee Shield V2.0b Schematics File](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/XBee_Shield_v2.0b.pdf)
- **[PCB图PDF]** [XBee Shield V2.0b PCB File](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/XBee%20Shield%20v2.0b%20PCB.pdf)
- **[芯片数据手册]** [CJT1117 Datasheet](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/CJT1117_datasheet.pdf)
- **[芯片数据手册]** [SN74LVC1G125 Datasheet](https://github.com/SeeedDocument/XBee_Shield_V2.0/raw/master/res/SN74LVC1G125DCKR.pdf)
