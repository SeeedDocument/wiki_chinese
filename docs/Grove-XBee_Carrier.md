---
title: Grove - XBee Carrier
category: Shield
bzurl: https://www.seeedstudio.com/grove-xbee-carrier-p-905.html?cPath=132_134
oldwikiname:  Grove - XBee Carrier
prodimagename: Bee_Stem.jpg
wikiurl: http://seeed.wiki/Grove-XBee_Carrier
sku:  113020004
---
![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Bee_Stem.jpg)

Grove - XBee Carrier 是为 Bee 系列和 Grove 部件设计的无线传感器网络 (WSN) 基板。它主要适用于独立的 Bee Nodes ，如其中有 ATMega328 板载和 XBee (Zigbee) 模块的 RFBee，Wifi Bee 。它与 [RFBee](/RFbee_V1.1-Wireless_Arduino_compatible_node "RFbee V1.1 - Wireless Arduino compatible node"), [Wifi Bee](/Wifi_Bee "Wifi Bee"), [XBee](http://garden.seeedstudio.com/index.php?title=Bee_series#ZigBee "Bee_series#ZigBee") 和 [Bluetooth Bee](/Bluetooth_Bee "Bluetooth Bee") 兼容。除了 Bee 插座，还有两个 Grove 连接器。该板可以由锂电池或 USB 线缆供电。您可以使用无线充电器，太阳能电池板或 USB 线缆为电池充电。FT232RL 芯片有助于将程序直接下载到 Bee 模块中。

没有 ATMega328 的 Bees (如 Bluetooth Bee ) 只能通过使用板载 FT232RL ( USB 至 UART ) 进行配置。 这些 Bees 不适合单独应用。

板载 FT232RL 可以像任何其他 3.3V USB 至 UART 接口一样使用，不连接到任何蜂模块。这对于通过串行端口编程 3.3V MCU 非常有用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.432d11a8wsyYvT&id=45507246404&ns=1&abbucket=1#detail)

##  产品特性
---
*   Bees 兼容插座

*   两个 Grove 连接器

*   两个 Grove 双排插座

*   用于 PWR，充电指示和 UART 传输的 LED。

*   电源开关

*   复位按钮

##  创意应用
---
*   带有像 [Wifi Bee](/Wifi_Bee "Wifi Bee") 的独立 Bee Node 的无线传感器网络。

*   为基于 FT232RL 的 Bees 组件做辅助配置。

*   使用车载充电控制器为锂离子电池充电。

*   作为基于 FT232RL 芯片的 3.3v USB转UART适配器。

##  警告
---
<font color="red">
</font>

*   将 Bees 插入正确的方向，您可以通过丝印层上的信息来判定。

##  规格参数
---
<table  cellspacing="0" width="80%">
<tr>
<th scope="col"> 项目
</th>
<th scope="col"> 最小值
</th>
<th scope="col"> 典型值
</th>
<th scope="col"> 最大值
</th>
<th scope="col"> 单位
</th></tr>
<tr>
<th scope="row"> 电压
</th>
<td> 3.0
</td>
<td> 3.3
</td>
<td> 3.6
</td>
<td> VDC
</td></tr>
<tr>
<th scope="row"> 控制器
</th>
<td colspan="4"> CN3063
</td></tr>
<tr>
<th scope="row"> 充电器 ( LiPo 电池充电电压)
</th>
<td colspan="4"> 4.4V to 6V (根据 CN3063 规格)
</td></tr>
<tr>
<th scope="row"> 充电电流
</th>
<td colspan="4"> 最大 500mA
</td></tr>
<tr>
<th scope="row">  3.3V LDO
</th>
<td colspan="4"> 低噪声和微功率型。适用于电池应用。
</td></tr>
<tr>
<th scope="row"> I/O Logic
</th>
<td colspan="4"> 3.3V Logic
</td></tr></table>

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Xbee_Carrier_Interface.jpg)

- **U2:** RT9167A_33PB IC, 3.3V LDO 低噪微功率稳压器
- **U3:** CN3083 IC，锂电池充电控制器 ( 使用太阳能电池板充电 )
- **U4:** FT232RL IC，USB 到串行 UART 接口

##  使用方法
---
使用 RFBee 时，RFBee 上的 ATmage168 的以下引脚排列请求使用Arduino IDE

- 引脚 5 是用于 I/O 的 Grove 连接器 - 黄线
- 引脚 6 是用于 I/O 的 Grove 连接器 - 白线
- 引脚 16 可能需要被低电平驱动以向 I/O Grove 提供足够的功率[通过 mosfet]
- 引脚 17 可能需要被低电平驱动以向 I2C Grove 提供足够的功率[通过 mosfet]

!!!Note
    您可以使用白色和黄色导线二合一的 x2 Grove 线缆以访问这两个 I/O。

###  硬件安装

####  充电

您可以从 **SeeedStudio** [Batteries and Chargers](/w/index.php?title=Batteries_and_Chargers&amp;action=edit&amp;redlink=1 "Batteries_and_Chargers&amp;action=edit&amp;redlink=1")为您的应用选择合适的电池。

*   将 3.7v LiPo 电池连接到 **BAT** JST-socket。

*   将电源如太阳能电池板连接到 **CHARGER** JST-Socket。

*   电池将持续充电。充电结束将由标有 'OK' 的 LED 指示。

![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Bee_Stem_with_LiPOBattery_Being_Charged_By_SolarCell.jpg)

####  与独立 Bee Nodes 一起使用

Bee Nodes 是独立的 Arduino 兼容无线节点。**SeeedStudio** 有两个这样的节点 [Wifi Bee](/Wifi_Bee "Wifi Bee") 和 [RFBee](/RFbee_V1.1-Wireless_Arduino_compatible_node "RFbee V1.1 - Wireless Arduino compatible node")。

*   以下图片说明了 [WiFi Bee](/Wifi_Bee "Wifi Bee") 与 **Grove - XBee Carrier** 的连接。

*   任何 Grove 都可以连接到提供的 Grove 插座。

*   WiFi Bee 的板载 **AtMega328P** 的编程是通过 USB 端口连接到 PC 进行的。( 使用 FT232RL )

![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Bee_Stem_Connected_to_Wifi_BEE_and_A_Grove.jpg)

*   参阅 [Wifi Bee 使用方法的编程示例文档](http://garden.seeedstudio.com/index.php?title=Wifi_Bee#Usage "Wifi_Bee#Usage")

![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Bee_Stem_Connected_To_RFBee_And_TwoTwigs.jpg)

####  与 Bee Modules 一起使用

这部分是关于没有通过 Arduino 引导程序预编程的 MCU 的 Bee 模块。它们大多数的行为就像一个无线接收器。 这些 **Bee Modules** 像 Bluetooth Bee 等可以与 PC 通信。 在这种情况下， **Grove - XBee Carrier** 作为这些为 Bees 提供必要电源的载体，通过 FT232RL USB 至 UART 连接 PC 的通信接口。

*   在下面的例子中，[Bluetooth Bee](/Bluetooth_Bee "Bluetooth Bee") 使用 USB-UART 连接到 **Grove - XBee Carrier**。

![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Stem_XBee_Carrier_Connected_to_BluetoothBee.jpg)

*   通过串口终端应用程序捕获 Bluetooth Bee 和 PC 的通信。

*   您可以在下面的屏幕截图中看到命令及其回复。

*   Bluetooth Bee 被置于 INQ 模式，甚至已经在附近检测到蓝牙设备。

![](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/img/Stem_XBee_Carrier_BluetoothBee_Commands.png)

*   关于使用 [Bluetooth Bee](/Bluetooth_Bee "Bluetooth Bee") 的更多信息, 请参阅 [Bluetooth Bee Commands documentation](/Bluetooth_Bee#Commands_to_change_default_configuration "Bluetooth Bee")。

###  编程
```
/*
  Test code for use with an XBee Carrier & an RF Bee

  Turns on PD5 (eg: grove relay) on for one second, then off for one second, repeatedly.
*/

void setup()
{
    // initialize the digital pin as an output [Pin 5 is the Grove connector for I/O
    pinMode(5, OUTPUT);

    // These lines are needed to ensure that the relay will pull in [provides power to the Grove]
    pinMode(16, OUTPUT);
    digitalWrite(16, LOW);
}

void loop() {
    digitalWrite(5, HIGH);   // set the LED on
    delay(1000);              // wait for a second
    digitalWrite(5, LOW);    // set the LED off
    delay(1000);              // wait for a second
}
```

##  更新日志
---
<table>
<tr>
<th> 修订版
</th>
<th> 说明
</th>
<th> 发布日期
</th></tr>
<tr>
<td width="300px"> v0.9b
</td>
<td width="500px"> 首次公开发行
</td>
<td width="200px"> 2011 年 7 月 13 日
</td></tr></table>

##  资源下载
---
*   **[Eagle 文件]** [Grove - XBee Carrier  Eagle Files](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/res/PCBA-Grove%20XBee%20Carrier_Eagle.rar)

*   **[原理图 PDF]** [Grove - XBee Carrier PDF schematics file](https://github.com/SeeedDocument/Grove-XBee_Carrier/raw/master/res/Bee_Stem_v0.9b.pdf)

*   **[芯片数据手册]** [CN3063](http://www.consonance-elec.com/pdf/%E6%8A%80%E6%9C%AF%E8%AF%B4%E6%98%8E%E4%B9%A6/DSC-CN3063.pdf)

*   **[其他资源]** [RT9167A_33PB](http://www.richtek.com/download_ds.jsp?s=238)
