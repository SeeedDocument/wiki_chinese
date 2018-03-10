---
title: RFbee V1.1 - Wireless Arduino compatible node
category: Wireless
bzurl: https://seeedstudio.com/RFbee-V1.1-Wireless-arduino-compatible-node-p-614.html
oldwikiname: RFbee_V1.1_-_Wireless_Arduino_compatible_node
prodimagename: rfbee1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/RFbee_V1.1-Wireless_Arduino_compatible_node
sku: 113050002
---

![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/rfbee1.jpg)

 RF Bee 是一款给设备之间提供简便、灵活的无线数据传输的射频模块。其基于 AVR Atmega168，可以使用 **Arduino** 的全部功能工作并通过 SPI 连接到 TI CC1101 射频收发器。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=45673535399
)

## 版本日志
---------------

| 版本 | 描述             | 发布日期      |
|----------|-------------------------|--------------|
| v1.0     | 首发版本         | 2010 年 3 月 5 日 |
| v1.1     | 修订版本         | 2010 年 8 月 27 日 |
| v1.2     | 将 MCU 改为 ATmega328 | 2015 年 10 月 10 日 |

## 产品特性
--------

-   通信距离 : 室内 / 城市最远 50 米；室外在视野内最远 120 米
-   接收机灵敏度 : -95dBm
-   射频数据传送速率 : 4800bps；76800bps
-   工作频率 : 868MHz & 915MHz
-   通信类型 : 点对点，或一对多
-   方便使用的串型接口以及丰富的可扩展接口
-   方便使用的 AT 指令 : 设定工作模式，串口波特率等
-   开源的硬件和固件
-   与 XBee 接口兼容，可将用于快速替换

!!!Note
    只有 RX，TX，VCC，GND 引脚与 XBee 模块相同。RFBee 不能与 XBee 通信，故 RFBee 被用于两端都是无线连接的场合

## 创意应用
-----------------

-   远程射频控制
-   易用的 WSN (无线传感器网络)

## 规格参数
--------------

| 项            | 参数                                                      |
|--------------------------|------------------------------------------------------------|
| 微处理器           | ATmega168 (V1.2 版本以前), ATmega328 (1.2以后版本) |
| PCB 尺寸                 | 24.38mmx32.94mmx0.8mm                                      |
| 指示灯               | 无                                                         |
| 电源             | 3.3V                                                       |
| IO 口                | 9                                                          |
| ADC 输入                | 7 (其中 6 个 与 IO 复用)                                  |
| 编程接口        | USB                                                        |
| 连接性             | XBee 兼容插座                                |
| 通行协议   | Uart(TTL)                                                  |
| 工作频段 | ISM 868MHz & 915MHz                                        |
| 外形尺寸        | 24.38mmx32.94mmx15mm                                       |

### 电气特性

| 参数         | 最小值 | 典型值 | 最大值 | 单位 |
|-----------------------|-----|------|-----|------|
| 输入电压         | 3.0 | 3.3  | 3.6 | VDC  |
| 传输电流      |     | 34.5 |     | mA   |
| 接收电流       |     | 18.1 |     | mA   |
| 待机电流          |     | 5.2  |     | mA   |
| 掉电电流    |     | <0.3 |     | mA   |
| 工作温度 | -50 |      | 125 | °C   |

## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-pin.jpg)

| 引脚     |  #  | 类型     | 描述                        | Arduino 引脚号      |
|---------|-----|--------------|------------------------------------|-------------------------|
| 3V3     | 1   | 电源输入 | VCC, +3.3V                         | -                       |
| TX      | 2   | 输出       | Uart Tx 引脚                       | 1(DIO)                  |
| RX      | 3   | 输入        | Uart Rx 引脚                       | 0(DIO)                  |
| PD4     | 4   | 输入/输出 | ATmega168 PD4                      | 4(DIO)                  |
|  !RESET | 5   | 输入        | ATmega168 重置引脚              |                         |
| PB1     | 6   | 输入/输出 | ATmega168 PB1                      | 9(DIO)                  |
| PB0     | 7   | 输入/输出 | ATmega168 PB0                      | 8(DIO)                  |
| PD7     | 8   | 输入/输出 | ATmega168 PD7                      | 7(DIO)                  |
|  DTR    | 9   | 输入        | 用于为 ATmega168 编程 | -                       |
| GND     | 10  | GND          | GND                                | -                       |
| PC3     | 11  | 输入/输出 | ATmega168 PC3                      | 3(Analog input)/17(DIO) |
| PC2     | 12  | 输入/输出 | ATmega168 PC2                      | 2(Analog input)/16(DIO) |
| PC1     | 13  | 输入/输出 | ATmega168 PC1                      | 1(Analog input)/15(DIO) |
| VREF    | 14  | 输入        | ATmega168 AREF 引脚                | -                       |
| PC0     | 15  | 输入/输出 | ATmega168 PC0                      | 0(Analog input)/14(DIO) |
| ADC7    | 16  | 输入        | ATmega168 ADC7                     | 7(Analog input)         |
| PD5     | 17  | 输入/输出 | ATmega168 PD5                      | 5(DIO)                  |
| PD6     | 18  | 输入/输出 | ATmega168 PD6                      | 6(DIO)                  |
| PC5     | 19  | 输入/输出 | ATmega168 PC5                      | 5(Analog input)/19(DIO) |
| PC4     | 20  | 输入/输出 | ATmega168 PC4                      | 4(Analog input)/18(DIO) |

## 使用方法
-----

### 硬件连接

RFBee 可以以多种方式连接，例如 :

-   使用 UartSBee 设备通过 USB 连接到 PC。
-   通过 XbeeShield 连接到 Seeeduino (或 Arduino)。
-   连接到具有 Uart 端口的任何其他设备。

!!!Note
    UartSBee 产品和 XbeeShield 是分开销售的。

#### 图 1: 使用 UartSBee 设备 (下图用旧版 UartSBee 演示)

![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-figure1.jpg)

#### 图 2: 通过 XbeeShield 连接到 Seeeduino

![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-figure2.jpg)

#### 任何具有 Uart 端口的设备

![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-figure3.jpg)

### 示例

下面是一个教程，介绍 RFBee 收发器如何同 RF Explorer 频谱分析仪一起使用。

#### RFBee 由 RF Explorer 监控

RFBee 能接受一些简单的 AT ASCII 命令字符串来做一些基本的配置，是数字 RF 传输实验的理想工具。

示例代码在 [此处](http://micro.arocholl.com/download/RFBeeTutorial/Test_RFBee.pde) 可用，并在 Arduino IDE v0022 中进行了测试。

|                                                                              |                                                                              |                                                                              |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-Exam1.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-Exam2.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/img/RFBee-Exam3.jpg) |

##### 要求

您可以使用 Seeeduino Stalker v02b 搭载 RFBee。只需将 RFBee 插入 XBee 插槽。您还需要将您的 Stalker 连接到 PC 以上传代码，我个人使用了 CP2102 USB 桥接器，您可以使用包括 Seeed 推荐的 UartSBee 等其他 USB 桥接器。

或者，您也可以使用 Arduino 兼容板，但是必须使用 XBee 2mm 连接器将 RFBee 与 CPU 的 RX/TX 连接，这在当地的商店中可能不易买到。

最后，您需要跳线将 Stalker 串口端口 **2** 连接到 **GND**，端口 **3** 连接到 **VCC**。我们将用它们作为简易开关，以不同的方式配置 RFBee。

用户需要熟悉一下 RF Explorer 和 RFBee 用户手册。

##### 设置 RFBee 工作

在 Stalker 中上传脚本之后，请完全关闭设备，使 Stalker 和 RFBee 的 ATMega 同时重置。

上电，在 Stalker 的 LED 指示灯闪烁 6 次后，开始传输。

RFExplorer 将显示接收功率和频率。调试天线方向，直到获得最好的功率响应。在本教程中，我们将以 915Mhz 使用 RFBee，但在 868Mhz 中将获得相同的结果。

**更多详情请点击** [这里](http://micro.arocholl.com/index.php?option=com_content&view=article&id=53:tutorial-how-to-use-rf-explorer-to-monitor-a-rfbee&catid=40:article&Itemid=61).

## 技术支持
-------

### 更新固件

您可以通过以下步骤使用 Arduino IDE 更新 RFbee 的固件。此过程使用 UartSB，因为这是将 RFBee 连接到 PC 的最简单方法，请参阅 **硬件连接** 节中的不同连接方法。

1.  将 RFBee 连接到 UartSB，将开关切换到 XBee 和 3.3v，然后通过 USB 线缆将其连接到计算机。
2.  将 RFBee 固件的源代码下载到 Arduino IDE 文件夹中。
3. 打开 Arduino IDE 并打开 RFBee_vx_x 项目。然后选择 Tools->Board->Arduino Pro or Pro Mini (3.3v, 8MHz) w/ATmega168 (当版本 >= V1.2 时为 ATmega328)。从工具菜单中选择正确的串行端口。现在可以上传的 RFBee 固件了。
4.  如果在更新过程中丢失配置，请重新应用 RFBee 中的配置更改。
5.  您可以根据您的需求添加或修改固件。

**RFBee firmware** : [点击下载](https://github.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/tree/master/res)

## 资源下载
---------

-   **[用户手册]** [RFBee User Manual](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/res/rfbee-manual.pdf)
-   **[其他资源]** [RFbee firmware for Arduino 1.0](https://raw.githubusercontent.com/SeeedDocument/RFbee_V1.1-Wireless_Arduino_compatible_node/master/res/RFbee_for_arduino1.0.zip)
-   **[其他资源]** [RFbee firmware 1.1 (latest)](https://github.com/Seeed-Studio/RFBee)
-   **[其他资源]** [Forum](http://www.seeedstudio.com/forum/viewtopic.php?f=10&t=682&sid=7a9b1bed4f9fd10a9b1003ca1e48e756)
