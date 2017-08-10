---
title: CAN-BUS Shield V1.2
category: Shield
bzurl: https://www.seeedstudio.com/CAN-BUS-Shield-V1.2-p-2256.html
oldwikiname: CAN-BUS_Shield_V1.2
prodimagename: Can_bus_shield_all.jpg
wikiurl: http://seeed.wiki/CAN-BUS_Shield_V1.2
sku: 113030021
---

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/Can_bus_shield_all.jpg?raw=true)

**CAN-BUS** 是一种普通的工业总线，由于其长距离，中等通信速度和高可靠性。它通常在现代机床上应用，例如汽车诊断总线。


该CAN总线扩展板采用MCP2515 CAN总线控制器与SPI接口和MCP2551 CAN收发器，为您提供Arduino / Seeeduino CAN-BUS函数。通过添加OBD-II转换器电缆并导入OBD-II库，就可以构建板载诊断设备或数据记录器。


**版本**

本文档适用于以下版本的产品：:

|版本|发布日期|购买链接|
|--------|-----------|-----------|
|CAN BUS Shield V1.0 |Oct 14, 2012|![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/EOL.png) 不再销售|
|CAN BUS Shield V1.1 |Aug 10, 2013|![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/EOL.png) 不再销售|
|CAN BUS Shield V1.2|Jan 5, 2015|[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/get_one_now_small.png)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797KqZcJC&id=520132781380)点击购买|

**CAN BUS Shield V1.2的新特性**


- 在PCB背面焊接
- 将端子电阻更改为120欧姆

**如果我想将这个扩展板连接到我的车，该怎么办？**

如果您想要读取数据或控制汽车，则可以使用OBD> DB9电缆，该电缆将轻松完成OBD连接器到DB9连接器的转换。该电缆也可以连接到具有OBD连接器的任何东西。我们在电缆上添加了一个开关，方便您的控制。您可以点击下面的图标购买该电缆。


[![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/obd_cable.jpg)](https://www.seeedstudio.com/DB9-to-OBD2-Cable-With-Switch-p-2872.html)

**USB-CAN分析仪**

如果您需要一个CAN总线分析仪来检测您的CAN总线，我们推荐下面的 [USB-CAN Analyzer](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.5e478797cERG2R&id=554216240108) 。(同样您可以点击下面的图片购买)

[![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/usb_can.jpg)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.5e478797cERG2R&id=554216240108)



## 产品特性
-----

  - CAN V2.0B速度高达1 Mb / s
  - SPI接口速度高达10 MHz
  - 支持标准（11位）和扩展（29位）数据以及远程帧
  - 两个具有优先消息存储的接收缓冲区
  - 工业标准DB-9连接器
  - LED指示灯


!!!Note
    CAN BUS 可以良好地兼容Arduino UNO (ATmega328), Arduino Mega (ATmega1280/2560) 、 Arduino Leonardo (ATmega32U4).

## 硬件概述
-----

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/hardware_overview_1.png?raw=true)

1. **DB9 Interface** - to connect to OBDII Interface via a DBG-OBD Cable.
2. **V_OBD** - It gets power from OBDII Interface (from DB9)
3. **Led Indicator**:
    - **PWR**: power
    - **TX**: blink when the data is sending
    - **RX**: blink when there's data receiving
    - **INT**: data interrupt
4. **Terminal** - CAN_H and CAN_L
5. **Arduino UNO pin out**
6. **Serial Grove connector**
7. **I2C Grove connector**
8. **ICSP pins**
9. **IC** - MCP2551, a high-speed CAN transceiver ([datasheet](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/Mcp2551.pdf))
10. **IC** - MCP2515, stand-alone CAN controller with SPI interface ([datasheet](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/MCP2515.pdf))


!!!warning
    - 当您在一个网络中使用两个以上的CAN总线扩展板时，应考虑阻抗。您应该用刀切割PCB中的P1，或者干脆取下PCB上的R3。

**管脚图**

![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/PINMAP.png)

!!!note
    - 空闲针可用于其他用途。

**DB9&OBDii 接口**

![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/OBD.png)

**CS 引脚**

默认情况下，V1.2的SPI_CS引脚连接到D9。如果要更改为D10，请按照以下说明进行操作。

- 步骤1：查看PCB的背面，你会发现一个名为CS的焊盘。

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/hardware_overview_pins_setting.png?raw=true)

 - 步骤2: 割断焊盘9和中间焊盘之间的导线

![](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/image/cut%20this%20wire%20with%20box%20cutter.png)

 - 步骤3: 将中间焊盘和焊盘10焊接在一起。

![](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/image/sodder%20the%20middle%20pad%20and%20pad%2010.png)


!!!warning
    - 切割的时候请您小心，不要伤到自己或者割坏PCB板子。

**SPI 引脚**

默认情况下，SPI引脚（SCK，MISO，MOSI）被连接到ICSP引脚。但是对于某些核心板，SPI引脚位于D11〜D13。如果发生这种情况，您需要对PCB进行一些更改。看看PCB的背面，有三个焊盘，MOSI，MISO和SCK，它们默认连接到A。如果需要，您可以将它们更改为B。


!!!note
    - 对于Arduino UNO, Arduino Mega, Arduino Leonardo 以及任何其他基于AVR 的Arduino 核心板, 我们推荐初始设置。

!!!warning
    - 切割的时候请您小心，不要伤到自己或者割坏PCB板子。


## 入门指南
-----
以下是一个简单的例子来说明CAN-BUS Shield的工作原理。在这个例子中，我们需要2块CAN-BUS扩展板以及Arduino或Seeeduino。

!!!note
    此示例基于 [Arduino IDE version 1.6.9](https://www.arduino.cc/download_handler.php?f=/arduino-1.6.9-windows.zip).


**步骤1: 我们需要准备些啥**

|名称|功能|数量|购买链接|
|----|--------|---|----|
|CAN-BUS Shield|CAN 总线通信 | 2 | [购买链接](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797KqZcJC&id=520132781380) |
|Seeeduino V4.2|控制器|2|[购买链接](https://item.taobao.com/item.htm?spm=a1z10.3-c.w5001-14920381017.3.5e478797hZabJu&id=45721222112&qq-pf-to=pcqq.c2c&scene=taobao_shop)|
|跳线|连接|2|[购买链接](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797wrngf4&id=520686147319)|

**步骤2: 硬件连接**

将每块CAN-BUS 扩展板都插在Seeeduino V4.2上，然后如下图所示使用两根跳线将两块CAN-BUS 扩展板连接起来。

![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/connection.png)

!!!note
    - CAN_H 连接到 CAN_H, CAN_L 连接到 CAN_L

**步骤3: 软件**

 请遵循 [如何安装Arduino库](http://wiki.seeed.cc/How_to_install_Arduino_Library/) 来安装 CAN BUS shield library.


点击下面图标来下载CAN BUS shield library

[![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/download_library.png)](https://github.com/Seeed-Studio/CAN_BUS_Shield)

下载完成后安装库文件到您的Arduino。

一个节点(此处代表Seeeduino + CAN_BUS 扩展板) 作为主机，另外一个节点作为从机。 主机将持续地向从机发送数据。

!!!note
    在上传代码前，每一个节点都可以作为主机。

打开发送示例（文件>示例> CAN_BUS_Shield-master>发送）并上传到主机。


![](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/image/send%20example.png)


打开receive_check示例（文件>示例> CAN_BUS_Shield-master> receive_check）并上传到从机。

![](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/image/receive%20check%20example.png)

**步骤4: 查看结果**

打开Arduino IDE（从机）的串行监视器，您将获得从主机发送的数据。

![](https://raw.githubusercontent.com/SeeedDocument/CAN_BUS_Shield/master/image/serial_monitor.png)

## APIs
-----

### 1. 设置波特率

该函数用于初始化CAN总线系统的波特率。

可用的波特率列表如下：

	#define CAN_5KBPS    1
	#define CAN_10KBPS   2
	#define CAN_20KBPS   3
	#define CAN_25KBPS   4
	#define CAN_31K25BPS 5
	#define CAN_33KBPS   6
	#define CAN_40KBPS   7
	#define CAN_50KBPS   8
	#define CAN_80KBPS   9
	#define CAN_83K3BPS  10
	#define CAN_95KBPS   11
	#define CAN_100KBPS  12
	#define CAN_125KBPS  13
	#define CAN_200KBPS  14
	#define CAN_250KBPS  15
	#define CAN_500KBPS  16
	#define CAN_666kbps  17
	#define CAN_1000KBPS 18

### 2. 设置接收屏蔽寄存器和过滤寄存器

控制器芯片上有2个接收屏蔽寄存器和5个滤波器寄存器，用于保证从目标设备获取数据。它们特别适用于由许多节点组成的大型网络。

我们提供两种函数来利用这些屏蔽寄存器和滤波器寄存器。他们是：


**Mask:**

	init_Mask(unsigned char num, unsigned char ext, unsigned char ulData);

**Filter:**

	init_Filt(unsigned char num, unsigned char ext, unsigned char ulData);


- **num** num表示要使用哪个寄存器。您可以设置0或1选择屏蔽寄存器，0至5选择过滤寄存器。
- **ext** 表示帧的状态。0表示它是标准帧。1表示它是一个扩展帧。
- **ulData** 代表屏蔽帧或过滤帧的内容。

###3. 校验接收
MCP2515可以在轮询模式下工作，其中软件检查接收到的帧，或使用附加引脚来发信号通知帧已被接收或发送完成。

使用以下函数轮询接收到的帧。

    INT8U MCP_CAN::checkReceive(void);

如果帧到达，该函数将返回1，如果没有到达，则返回0。

###4. 获取 CAN ID
当某些数据到达时，您可以使用以下函数获取“发送”节点的CAN ID。

    INT32U MCP_CAN::getCanId(void)

###5. 发送数据

    CAN.sendMsgBuf(INT8U id, INT8U ext, INT8U len, data_buf);

这是将数据发送到总线上的函数。其中：
* **id** 表示数据来源
* **ext** 表示帧的状态。'0'表示标准帧。'1'表示扩展帧。
* **len** 表示此帧的长度。
* **data_buf** 是此消息的内容。

例如，在“发送”示例中，我们有：

    unsigned char stmp[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    CAN.sendMsgBuf(0x00, 0, 8, stmp); //send out the message 'stmp' to the bus and tell other devices this is a standard frame from 0x00.

###6. 接收数据

以下函数用于在“接收”节点上接收数据：

    CAN.readMsgBuf(unsigned char len, unsigned char buf);

在屏蔽器和过滤器都设置好的条件下，这个函数只会接收满足屏蔽器和过滤器筛选条件的数据帧。

* **len** 表示数据长度。
* **buf** 是存储数据的位置。


## 生成一个新的波特率

我们提供了许多频繁使用的波特率，如下所示：

	#define CAN_5KBPS    1
	#define CAN_10KBPS   2
	#define CAN_20KBPS   3
	#define CAN_25KBPS   4
	#define CAN_31KBPS   5
	#define CAN_33KBPS   6
	#define CAN_40KBPS   7
	#define CAN_50KBPS   8
	#define CAN_80KBPS   9
	#define CAN_83KBPS   10
	#define CAN_95KBPS   11
	#define CAN_100KBPS  12
	#define CAN_125KBPS  13
	#define CAN_200KBPS  14
	#define CAN_250KBPS  15
	#define CAN_500KBPS  16
	#define CAN_666KBPS  17
	#define CAN_1000KBPS 18

然而，您仍然可能找不到所需的波特率。在这里，我们提供一个软件来帮助您计算所需的波特率。

点击 [这里](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/CAN_Baudrate_CalcV1.3.zip) 来下载该软件。

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/CAN_BUS_Shield_SetBaud.jpg?raw=true)

!!!note
    这个软件仅仅支持Windows系统，如果您无法打开它，欢迎随时通过邮件联系 loovee@seeed.cc 来获取技术支持。

打开软件，你需要做的就是设置你想要的波特率，然后做一些简单的设置，然后点击计算。

然后，您将获得一些数据，cfg1，cfg2和cfg3。

您需要在库中添加一些代码。

打开 **mcp_can_dfs.h**, 你需要将下列代码添加到第272行左右。

	#define MCP_16MHz_xxxkBPS_CFG1 (cfg1)    // xxx is the baud rate you need
	#define MCP_16MHz_xxxkBPS_CFG2 (cfg2)
	#define MCP_16MHz_xxxkBPS_CFG3 (cfg2)

然后让我们跳转到第390行, 添加如下代码：

	#define CAN_xxxKBPS NUM       // xxx is the baudrate you need, and NUM is a number, you need to get a different from the other rates.

打开 **mcp_can.cpp**, 跳转到函数**mcp2515_configRate**(大致在第190行), 然后添加如下代码:

	case (CAN_xxxKBPS):
	    cfg1 = MCP_16MHz_xxxkBPS_CFG1;
	    cfg2 = MCP_16MHz_xxxkBPS_CFG2;
	    cfg3 = MCP_16MHz_xxxkBPS_CFG3;
	    break;

然后，您就可以使用您需要的波特率了。当您使用的波特率时，请给我们一个github的请求，这样我可以添加到库来帮助其他人。感谢！



## 项目工程
-----

如果您想使用CAN-BUS 扩张板做一些酷炫的项目，这里有一些项目可供参考。

### 大众 CAN BUS 游戏

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/project1.JPG?raw=true)

Ever wanted to play a car/truck simulator with a real dashboard on your PC? Me too! I'm trying to control a VW Polo 6R dashboard via CAN Bus with an Arduino Uno and a Seeed CAN Bus Shield. Inspired by Silas Parker. Thanks Sepp and Is0-Mick for their great support!

[![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/Wiki_makeitnow_logo.png?raw=true)](http://www.seeed.cc/project_detail.html?id=291)

### 黑进车载 CAN-BUS

![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/project2.jpg?raw=true)

Modern Vehicles all come equipped with a CAN-BUS Controller Area Network, Instead of having a million wires running back and forth from various devices in your car to the battery, its making use of a more clever system.

All electronic functions are connected to the TIPM, (Totally integrated Power Module), such as solenoids/relays to lock the doors or mini motors to wind the windows etc.

From each node (IE Switch pod that controls your windows or electric door locks) it broadcasts a message across the CAN. When the TIPM detects a valid message it will react accordingly like, lock the doors, switch on lights and so on.


[![](https://github.com/SeeedDocument/CAN_BUS_Shield/blob/master/image/Wiki_makeitnow_logo.png?raw=true)](http://www.instructables.com/id/Hack-your-vehicle-CAN-BUS-with-Arduino-and-Seeed-C/)

## FAQ
------
**Q1: 我无法从其他CAN设备获取数据。**

* 检查连接是否正确
* 检查波特率设置是否正确

**Q2: 串行监视器打印失败。**

*检查CS引脚设置是否与代码匹配。对于CAN总线扩展板V1.1 / 1.2，CS引脚连接到D9，其他则为D10。

**Q3. 如果我有其他问题，我在哪里可以找到技术支持。**

* 您可以在 Seeed 论坛 [Seeed Forum](http://www.seeed.cc/discover.html?t=Arduino) 留言或者or 给下列邮箱发送邮件至 **techsupport@seeed.cc**.

## 资源下载
-----

* **【PDF】**[CAN-BUS Shield V1.2 Schmatics](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/CAN-BUS_Shield_v1.2.pdf)
* **【Eagle原理图】**[Schematic of CAN-BUS Shield V1.2](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/CAN-BUS_Shield_v1.2_sch_pcb.zip)
* **【CAN_BUS_Shield库】**[Arduino Library for CAN-BUS Shield](https://github.com/Seeed-Studio/CAN_BUS_Shield)
* **【MCP2515数据手册】**[MCP2515 datasheet](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/MCP2515.pdf)
* **【MCP2551数据手册】**[MCP2551 datasheet](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/Mcp2551.pdf)
* **【示例程序】**[An OBD Demo](https://github.com/Seeed-Studio/CANBUS_SHIELD_OBD_RECIPLE)
* **【MCP2515波特率计算工具】**[MCP2515 Baud Rate Tool](https://github.com/SeeedDocument/CAN_BUS_Shield/raw/master/resource/CAN_Baudrate_CalcV1.3.zip)
* **【USB-CAN分析器】**[USB-CAN Analyzer](https://www.seeedstudio.com/USB-CAN-Analyzer-p-2888.html)
* **【线缆DB9转OBD2】**[DB9 to OBD2 Cable](https://www.seeedstudio.com/DB9-to-OBD2-Cable-With-Switch-p-2872.html)
