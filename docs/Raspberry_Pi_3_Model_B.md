---
title: Raspberry Pi 3 Model B
category: Raspberry
bzurl: https://www.seeedstudio.com/Raspberry-Pi-3-Model-B-p-2625.html
oldwikiname:  Raspberry Pi 3 Model B
prodimagename:  Raspberry_Pi3_What_is_New.png
wikiurl: http://wiki.seeedstudio.com/cn/Raspberry_Pi_3_Model_B
sku:     114990584
---

**Raspberry Pi®** 是 [Raspberry Pi Foundation](http://www.raspberrypi.org) 基于 **ARM** 制造的信用卡大小的 **SBC**（单板计算机）。树莓派运行基于 Debian 的 **GNU / Linux** 操作系统 [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)，并且具有很多其他系统上上的端口。

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/Raspberry_Pi3_What_is_New.png)

Raspberry Pi Foundation 宣布了新版本 **Raspberry Pi 3**，详情请查阅 [这里](https://www.raspberrypi.org/blog/raspberry-pi-3-on-sale/)。随着板载 **WiFi** / **Bluetooth** 的支持和新的 64 位处理器，**Raspberry Pi v3** 将会成为制造商，工程师和学生最喜爱的开发板。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.2a6a4c472NbhKT&id=528322046763)

##  Raspberry Pi 3 更新内容
---
<table>
<tr>
<th scope="col"> 开发板
</th>
<td> Raspberry Pi 2 Model B
</td>
<th> **Raspberry Pi 3 Model B**
</th></tr>
<tr>
<th scope="col"> 处理器
</th>
<td> Broadcom BCM2836
</td>
<td> Broadcom **BCM2837**
</td></tr>
<tr>
<th scope="row"> CPU 核心
</th>
<td> Quadcore ARM Cortex-A7, 32Bit
</td>
<td> Quadcore **ARM Cortex-A53, 64Bit**
</td></tr>
<tr>
<th scope="row"> 时钟频率
</th>
<td> 900 MHz
</td>
<td> 1.2GHz (估计比 Pi2 快 50%)
</td></tr>
<tr>
<th scope="row"> RAM
</th>
<td> 1 GB
</td>
<td> 1 GB
</td></tr>
<tr>
<th scope="row"> GPU
</th>
<td> 250 MHz 显示核心 IV®
</td>
<td> **400 MHz** 显示核心 IV®
</td></tr>
<tr>
<th scope="row"> 网络接口
</th>
<td> 1 x 10 / 100 以太网 (RJ45 接口)
</td>
<td> 1 x 10 / 100 以太网 (RJ45 接口)
</td></tr>
<tr>
<th scope="row"> 无线 Wifi
</th>
<td> 无
</td>
<td> **802.11n wireless LAN (WiFi) 和 Bluetooth 4.1**
</td></tr>
<tr>
<th scope="row"> USB 接口
</th>
<td> 4 x USB 2.0
</td>
<td> 4 x USB 2.0
</td></tr>
<tr>
<th scope="row"> GPIOs
</th>
<td> 2 x 20 Pin
</td>
<td> 2 x 20 Pin
</td></tr>
<tr>
<th scope="row"> 相机接口
</th>
<td> 15-pin MIPI
</td>
<td> 15-pin MIPI
</td></tr>
<tr>
<th scope="row"> 显示器接口
</th>
<td> DSI 15 Pin / HDMI 输出 / Composite RCA
</td>
<td> DSI 15 Pin / HDMI 输出 / Composite RCA
</td></tr>
<tr>
<th scope="row"> 电源输入 (电流大小)
</th>
<td> 1.8 A
</td>
<td> **2.5 A**
</td></tr>
</table>

##  开发板
---
*   Pi 2 和 Pi 3 的尺寸相同。

*   元件位置略有变化，来容纳 WiFi / Bluetooth SoC。增加了芯片天线。

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_2_Vs_RaspberryPi_3_Top.JPG)

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_2_Vs_RaspberryPi_3_Bottom.JPG)

##  系统芯片 (SoC)
---
**Broadcom BCM2837 SoC**

*   应用处理器

    *   64 bit

        *   四核

        *   1.2 GHz

        *   ARM Cortex-A53 处理器 (ARM V8 ISA)

*   GPU

    *   400 MHz
    *   图形核心 IV 多媒体协处理器

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_3_BCM2837_ARM_Cortex_A53-64Bit_ARM_V8-VideoCore_IV_Multimedia.jpg)

##  芯片天线
---
WiFi 和蓝牙4.1 SoC BCM43438 使用陶瓷芯片天线。为了容纳芯片天线，将 Pi 2 中的指示 LED 移动到 PCB 的下侧。

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_3_Chip_Antenna.jpg)

##  LED 改变位置
---
与 Pi 2 相比，ACT 和电源 LED 移动了位置，具体如下图所示。

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_3_LEDs_Position.jpg)

##  RUN 引脚更换位置
---
RUN 引脚的位置也被改变了

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/RaspberryPi_3_LEDs_RUN_PinHeader.jpg)

##  WiFi / Bluetooth SoC BCM43438
---
WiFi 和 蓝牙 4.1 (Classic 和 LE) 由 Broadcom BCM43438 芯片提供。

![](https://github.com/SeeedDocument/Raspberry_Pi_3_Model_B/raw/master/img/Raspberry_Pi_3_WiFi_Bluetooth_SoC_BCM43438.jpg)

购买链接：

*   [Raspberry Pi 3 Preorder](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.2a6a4c472NbhKT&id=528322046763)


所有商标均为其各自所有者的财产。

树莓派和它的标志是树莓派基金会的商标。
