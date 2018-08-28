---
title: Grove - Solid State Relay V2
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 103020137
tags:
---

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/main.jpg)

固态继电器不使用线圈，而是使用功率半导体器件，如晶闸管和晶体管，其开关速度相较于机械式继电器快得多。Grove - 固态继电器 V2 基于高品质的 **G3MC-202P** 模块所设计，可以使用5VDC控制最大240VAV。在Grove接口的帮助下,与Arduino一起使用固态继电器将变的十分简便。 


根据不同的使用场景，我们为您提供了一系列的固态继电器。
Grove - 固态继电器 V2

[Grove - 2-通道 固态继电器](http://wiki.seeedstudio.com/Grove-2-Channel_Solid_State_Relay)

[Grove - 4-通道 固态继电器](http://wiki.seeedstudio.com/Grove-4-Channel_Solid_State_Relay)

[Grove - 8-通道 固态继电器](http://wiki.seeedstudio.com/Grove-8-Channel_Solid_State_Relay)

<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-2-Channel-SPDT-Relay-p-3118.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>

## 产品特点

- 相对于机械式继电器的优点：

    - 相较于机电继电器，固态继电器具有更快的开关速度，并且没有物理接触磨损
    - 全静音操作
    - 没有物理接触意味着没有火花，在开关过程中没有火花产生使得其可以被应用于易爆环境中
    - 使用寿命增加
    - 整体结构紧凑



- 缺点：

    - 当关闭时，阻抗较高（发热），电噪声较大
    - 当打开时，阻抗较低，存在漏电流
    - 只能使用在AC电路中



## 产品规格

|**项目**|**参数**|
|:----:|:----:|
|工作输入电压|4~6V|
|额定输入电压|5V|
|额定负载电压|100 ~  240 VAC 50/60 Hz|
|负载电压范围|75 ~  264 VAC 50/60 Hz||
|负载电流|0.1 ~ 2 A|
|漏电流|1.5 mA max. (at 200 VAC)|
|绝缘电阻|1,000 MΩ min. (at 500 VDC)|
|存储温度|-30°C ~ 100°C (无结冰、结露)|
|工作温度|-30°C ~  80°C (无结冰、结露)|
|工作湿度| 45% ~  85%RH|
|输入接口|数字|
|输出接口|2引脚直插式蓝色端子 |

!!!**注意**

您也许注意到了 **漏电流** , 1.5mA 足以驱动一个低功耗的LED，所以当继电器处于关闭状态时，LED也许仍然会发出微弱的光。

## 产品应用

- 需要低延迟切换的操作，例如， 舞台灯光控制
- 要求高稳定性的设备，例如 医疗设备，交通信号
- 防爆，防腐，防潮的情况，例如： 煤炭，化学工业


## 硬件概述

### 引脚映射

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/pin_map_.jpg)

### 原理图

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/schematic_.jpg)

**K1** 是继电器模块，当在 **INT+** 和 **INT-** 之间施加5V时，继电器将打开。然后 **LOAD1**将会连接到 **LOAD2**。我们使用一个NPN型三极管 **Q1**(BC817-40)来控制 **INT+** 和 **INT-** 之间的电压。


 **CTR** 是来自Arduino或者其他板子的控制信号。它通过一个10K电阻R2被拉低，如果没有信号，**Q1**的基极为0V，Q1处于关闭状态，那么K1将被关断。如果 **CTR** 为 5v, Q1将会开启。K1的 **INT-** 将会被连接到系统的GND， **INT+** 和 **INT-** 之间会产生5V压降，因此K1将被打开，**LOAD1** 与 **LOAD2**连接。

!!!**注意**


在该部分我们仅提供部分原理图，完整的文档请您参考[资源下载](/#resources)


## 兼容平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|:-:|:-:|:-:|:-:|:-:|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo.jpg)  |

!!!**注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。




## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**

| Seeeduino V4.2 | Base Shield| Grove - 固态继电器 V2 |
|:-:|:-:|:-:|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-2-Channel-SPDT-Relay-p-3118.html" target="_blank">点击购买</a>|


!!!**注**

  **1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。
    
  **2**  购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。

  **3** 您需要自己准备两个风扇。


- **步骤 1.** 将Grove - 固态继电器 连接到Base Shield的 **D7** 接口。

- **步骤 2.** 将线缆切断，一端连接到 **LOAD1**，另一端连接到 **LOAD2**。

- **步骤 3.** 将 **LOAD1** 连接到电源,  **LOAD2** 连接到风扇。

- **步骤 4.** 将Base Shield插到Seeeduino上。

- **步骤 5.** 通过USB线缆将Seeeduino连接到PC端。


![](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/connect.jpg)


#### 软件代码

!!!**注意**

如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/).


- **步骤 1.** 打开Arduino IDE 并创建一个新文件,您可以仅仅点击这个位于代码块右上方的图标 ![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg) 将以下代码拷贝进Arduino IDE。

```c++
#include <Arduino.h>
uint8_t pin = 7;
void setup() {
  pinMode(pin, OUTPUT);}
void loop() {
  digitalWrite(pin, HIGH);
  delay(5000);
  digitalWrite(pin, LOW);
  delay(5000);
}
```

- **步骤 2.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。


!!!**成功**

您将会看到每隔5秒，风扇关断一次。



## 资源下载

- **[Zip]** [Grove - 固态继电器 V2 eagle 文件](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/res/Grove-Solid_State_Relay_V2_Eagle.zip)
- **[PDF]** [G3MC-202P 芯片手册](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/res/G3MC202p.pdf)


## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！