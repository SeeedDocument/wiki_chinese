---
title: Xadow GSM+BLE
category: Rephone
bzurl: https://www.seeedstudio.com/Xadow-GSM-BLE-p-2560.html
oldwikiname: Xadow_GSM+BLE
prodimagename: Xadow_GSM%2BBLE_shangjiatu.JPG
wikiurl: http://wiki.seeedstudio.com/cn/Xadow_GSMPlusBLE
sku: 102040005
---

![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Xadow_GSM%2BBLE_shangjiatu.JPG)

无论是使用外部扬声器和麦克风拨打和接听电话，还是使用蓝牙短距离传输数据，您都可以使用 Xadow GSM + BLE 来实现。

作为 RePhone kit Create 的核心，Xadow GSM + BLE 采用功能强大的 System-On-Chip (SOC) MT2502，提供丰富的通信协议 - GSM，GPRS 和蓝牙（v4.0 和 2.1 双模式）。它支持覆盖全球任何 GSM 网络的四频 850/900/1800/1900MHz。使用时只需插入一张 2G Nano SIM 卡，然后您就可以使用蜂窝网络通信了。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1fee2d3feMUo15&id=527722013021)


## 产品特性  

- 基于最小的商业系统级芯片
- 市场上最小的尺寸（5.4mm x 6.2mm）
- 开源和模块化设计
- 质量轻，体积小
- 内置 Xadow 连接器，便于插拔 FPC 电缆  
- 可与其他 Xadow 模块和开发板联合使用
- 大多数 RePhone 套件的核心模块
- 长途和短距离通信的完美选择

## 规格参数

|微控制器	|MT2502                                                                                  |
|-------------------|----------------------------------------------------------------------------------------|
|MCU 核心	        |32-bit ARM7EJ-STM RISC 处理器                                                        |
|RAM	            |4 MB                                                                                    |
|Flash Memory	    |16 MB                                                                                   |
|电源要求	    |3.3 ~ 4.2V(无 SIM)/3.5 ~ 4.2V(有  SIM)                                                 |
|功耗	|20mW/30mW/52mW @ 待机(无通信)/待机(GSM)/待机(BT)                             |
|频段	        |850/900/1800/1900 MHz                                                                   |
|GPRS	            |Class 12 modem                                                                          |
|时钟频率	    |260 MHz                                                                                 |
|接口     	|35 PIN 接口 & 11 PIN Xadow 模块接口; JST 1.0 电池接口|
|通信接口	        |LCD, Audio, I2C, SPI, UART, 和 GPIOs 等                                               |
|尺寸       	|25.37mm × 20.30mm / 1” × 0.8”                                                           |  

## 硬件概述

![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Xadow_GSM%2BBLE_Overview.png)


下面的图片以 **从左到右** 的顺序说明了 11 针 Xadow 接口，可焊接引脚和 35 针 Xadow 接口的针脚定义。

![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Xadow-connector-Pin-definitions-06.jpg)  

## 充电  

给 RePhone/Xadow GSM+BLE 供电可以使用 **3.5V ~ 4.2V** 的电池，使用 **JST 1.0 公头** 连接，或者用电线连接 **引脚3(VCC)** 和 **引脚6(GND)** 进行供电，接口如上图所示。

## 电池充电  

Xadow GSM+BLE 使用 JST 1.0 母头(淘宝无此产品) 连接电池，使用一根 USB 电缆连接板子即可为电池充电。

## 操作模式

Xadow GSM + BLE 有两种工作模式，当您开机并连接电脑时，**按住电源键2秒钟** 将模块 **ON** 或 **OFF** 进入 **大容量存储模式** 或 **闪存/调试模式**。
![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Operating_mode.png)  

## 大容量存储模式

当 Xadow GSM + BLE 为 **OFF** 时，通过 Micro USB 电缆将电路板（连接电池）连接到 PC，即可在 PC 上访问板载 5MB “大容量存储模式”。所有应用程序（vxp 文件）和系统设置都存储在这个 5MB 存储器中。
![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Mass_Storage_Mode.png)  

## 闪存/调试模式

 Xadow GSM + BLE 是 **ON** 时，通过 Micro USB 电缆将电路板（连接电池）连接到 PC，您可以在 **设备管理器** 里找到两个 **COM端口**：

- **MTK USB Debug Port(COM4)**  
- **MTK USB Modem Port(COM5)**  

COM 端口号可能与您 PC 上看到的不同。 每个 COM 端口根据您使用的开发环境具有不同的功能，请参阅入门指导部分了解更多详细信息。

打开 **设备管理器**：在桌面上右键点击 **我的电脑**，选择 **管理**，在左侧列表中 **设备管理器**，单击打开，找到 **端口（COM 和 LPT）**，点开看到如下所示：
![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Check_ports.png)  


## 入门指导

我们开发了丰富的 Arduino IDE 库，Lua 库和 JavaScript 库，并附有详细的示例代码，帮助入门级程序员轻松快速地开发 RePhone 模块。

我们还提供了一个基于 Eclipse IDE 的功能强大的 SDK，使 C/C ++开发人员能够开发更智能的应用程序。
[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Arduino_IDE-17.png)  ](/Platform/RePhone/RePhone/)  
[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Eclipse_IDE-13.png) ](http://www.seeedstudio.com/wiki/Eclipse_IDE_for_RePhone_Kit)   
[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/Lua-14.png)](http://www.seeedstudio.com/wiki/Lua_for_RePhone#Use_Lua_Shellt)  
[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/JS-15.png) ](http://www.seeedstudio.com/wiki/JavaScript_for_RePhone)

有关更多信息，请参阅 RePhone 主页上的 [RePhone Development Environment](http://www.seeedstudio.com/wiki/Rephone#Development_Environment)  。

## Related Projects  

Check on awesome RePhone projects that has been achieved with RePhone.  
**A Traceable Dog Collar**  
5 steps to make a traceable dog collar for your lovely puppy.   
[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/450px-Dog_Collar.png.jpeg)  ](http://www.seeedstudio.com/recipe/424-rephone-traceable-dog-collar.html)

## RePhone Community  

[![](https://raw.githubusercontent.com/SeeedDocument/Xadow_GSM-BLE/master/image/300px-RePhone_Community-2.png) ](http://www.seeedstudio.com/forum/viewforum.php?f=71&sid=b70f8138c89becf7701260bb41faf9f4)   
We’ve been looking for a better place where our backers (RePhone Users) can sit together, warmly and comfortably, have conversations about RePhone, discuss technical problems, share ideas/projects, and give feedback on the modules’ development in the future. And then here we go, the RePhone Community.

Now join us in the [RePhone Community](http://www.seeed.cc/discover.html?t=rephone)! Together we seek answers, make interesting stuff, care about each other, and share our experiences.

### Frequently Asked Questions  

Some frequently asked questions in RePhone Community are collected and answered to the topic "[Frequently Asked Questions of RePhone (FAQ)](http://www.seeed.cc/topic_detail.html?id=5170#p23753)" , the topic will be kept updating whenever a new FAQ comes out.  

## 资源下载  

**[Eagle 文件]**[Xadow_GSM+BLE eagle files ](https://github.com/SeeedDocument/Xadow_GSM-BLE/blob/master/resource/Xadow_GSM%2BBLE.rar)  

**[数据手册]**[Datasheet for eagle files](https://github.com/SeeedDocument/Xadow_GSM-BLE/blob/master/resource/Datasheet_for_MT2502.rar)  

**[兼容性]**[Compatibility between GSM+BLE and Xadow 1.0 modules  ](https://github.com/SeeedDocument/Xadow_GSM-BLE/blob/master/resource/Compatibility_between_GSM%2BBLE_and_Xadow_1.0_modules.xlsx)
