---
title: Grove - 2-Coil Latching Relay
category: Actuator
bzurl: https://seeedstudio.com/Grove-2-Coil-Latching-Relay-p-1446.html
oldwikiname: Grove_-_2-Coil_Latching_Relay
prodimagename: 2Coil_Latching_Relay_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-2-Coil_Latching_Relay
sku: 103020010
tags: grove_digital, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-2-Coil_Latching_Relay/master/img/2Coil_Latching_Relay_01.jpg)

该模块基于 2 线圈锁定继电器。与普通继电器相比，该锁存继电器不需要连续电力来保持状态，只需要一个上升/下降脉冲来改变工作状态。甚至电源可以在工作状态不需要改变的情况下被移除，这使得该模块特别适用于低功率项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.886f2405BtSNn&id=45571928583)

## 产品特性
-------

-   Grove 连接器
-   低功耗
-   双开关

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
-------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
4.7
</td>
<td>
5.0
</td>
<td>
5.3
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
设置/复位电压(最大)
</th>
<td colspan="3">
4.0
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
线圈电阻
</th>
<td>
151
</td>
<td>
167
</td>
<td>
183
</td>
<td>
Ω
</td>
</tr>
<tr align="center">
<th scope="row">
开关电压(最大)
</th>
<td colspan="3">
35VAC/35VDC
</td>
<td>
/
</td>
</tr>
<tr align="center">
<th scope="row">
开关电流(最大)
</th>
<td colspan="3">
3
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
设置时间(锁存)
</th>
<td colspan="3">
4.5(max)
</td>
<td>
ms
</td>
</tr>
<tr align="center">
<th scope="row">
重置时间(锁存)
</th>
<td colspan="3">
3.5(max)
</td>
<td>
ms
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 开始之前
------------

### 相关阅读

我们建议您在使用气体传感器之前阅读这些知识，这将有助于您了解有关 Arduino 和我们的产品的更多信息，还可以让您更轻松地使用开源硬件。

-   [ Arduino 入门指导](/Getting_Started_with_Seeeduino)
-   [什么是 Grove 系统](/Grove_System)
-   [为什么我需要一个 Base shield ?](/Base_Shield_V2)

阅读完之后，您就知道如何使用 Grove 产品的 Base Shield 与 Arduino 良好地协作。让我们开始吧!

### 准备工作

本教程将包括以下必要的产品 :

-   [Arduino UNO R3](http://www.seeedstudio.com/depot/Arduino-Uno-Rev3-p-694.html) 或 [Seeeduino v4](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.1d26c07ekK3ndr&id=45721222112)
-   [Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.21.1d26c07ekK3ndr&id=520233320144)
-   Grove - 2-Coil Latching Relay


## 入门指导
-----

### 与 Arduino 一起使用

Grove - 2-Coil Latching Relay 只在更换状态期间开光电源。信号引脚上的上升/下降电压脉冲改变其工作状态。这将在要求能源效率，以及需要继电器记录其状态的情况下非常有用。

开始使用吧。

-   将该模块连接到 [Grove - Base Shield](/Base_Shield_V2 "Grove - Base Shield") 的 **D3** 端口
-   当 SIG 引脚上有一个上升沿时，继电器由保持默认的"设置"状态 (**Comm** 和 **NO** 连接)变成"复位"状态 (**Comm** 和 **NC** 连接)。参考代码如下所示 :

```c
#define LatchingRelay 3
void setup()
{
    pinMode(LatchingRelay,OUTPUT);

    digitalWrite(LatchingRelay,LOW);
    delay(1000);
    digitalWrite(LatchingRelay,HIGH);
    delay(1000);
}
void loop()
{

}
```

-   当 SIG 引脚上有一个下降沿时，继电器由保持"复位"状态 (**Comm** 和 **NC** 连接)变成"设置"状态 (**Comm** 和 **NO** 连接)。参考代码如下所示 :

```c
#define LatchingRelay 3
void setup()
{
    pinMode(LatchingRelay,OUTPUT);

    digitalWrite(3,HIGH);
    delay(1000);
    digitalWrite(3,LOW);
    delay(1000);
}
void loop()
{

}
```

-   工作状态不变时，此模块消耗的功率不大。设置继电器状态后，不再需要为锁存继电器供电，这使得功耗特别低。

<div class="admonition note">
<p class="admonition-title">Note</p>
**当从库存中释放时，继电器处于"复位"状态。Relay is on the "reset" status when being released from stock.**
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-2-Coil_Latching_Relay/master/img/Latching_Relay_Diagram.jpg)


<div class="admonition note">
<p class="admonition-title">Notes</p>
<p> 1. 双向继电器同时被控制。</p>
<p> 2. 切换到"设置" ("复位")状态时，**NO** (**NC**) 指示灯将闪烁一次。</p>
</div>


### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.完成配置开发环境，否则请遵循 [here](/GrovePiPlus)。

3.连接

-   将继电器用 Grove 线缆插入  Grovepi 插口 **D4**。

4.跳转到演示目录 :

```
cd yourpath/GrovePi/Software/Python/
```
-   演示代码如下 :

```
nano grove_2_coil_latching_relay.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi

# Connect the Grove 2-Coil Latching Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4

grovepi.pinMode(relay,"OUTPUT")

while True:
    try:
        # switch on for 5 seconds
        grovepi.digitalWrite(relay,1)
        print "on"
        time.sleep(5)

        # switch off for 5 seconds
        grovepi.digitalWrite(relay,0)
        print "off"
        time.sleep(5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print "Error"
```

5.运行代码。
```
sudo python grove_2_coil_latching_relay.py
```

## 资源下载
--------

- **[Eagle文件]** [Grove - 2-Coil Latching Relay Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-2-Coil_Latching_Relay/master/res/Grove-2-Coil_Latching_Relay_Eagle_File.zip)
- **[芯片数据手册]** [Latching_Relay_Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-2-Coil_Latching_Relay/master/res/Latching_Relay_Datesheet.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_2-Coil_Latching_Relay -->
