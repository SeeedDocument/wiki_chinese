---
title: Grove - Digital Distance Interrupter 0.5 to 5cm(GP2Y0D805Z0F)
category: 传感器
bzurl:
oldwikiname:
prodimagename:
surveyurl:
sku: 101020533
tags:
---


![](https://github.com/SeeedDocument/Grove-Digital_Distance_Interrupter_0.5_to_5cm-GP2Y0D805Z0F/raw/master/img/main.JPG)

Grove - 数字距离中断器0.5至5cm是基于GP2Y0D805Z0F的红外距离感应模块。 通常，此传感器的输出为1（高），当物体进入传感器的测量范围时，它将被触发并输出0（低）。同时，板载LED将亮起。 顾名思义，测量范围为0.5cm至5cm。

该传感器有两种 Grove - Digital Distance Interrupter 0.5 to 5cm(GP2Y0D805Z0F)  和 [Grove - Digital Distance Interrupter 0.5 to 5cm(GP2Y0D805Z0F)(P)](https://www.seeedstudio.com/Grove-Digital-Distance-Interrupter-0.5-to-5cm%28GP2Y0D805Z0F%29%28P%29-p-3085.html) 对于没有字母P的版本，镜头和树丛接口位于同一侧; 对于带字母P的版本，镜头和树丛界面位于不同的侧面。


GP2Y0D805Z0F是一款距离测量传感器单元，由PD（光电二极管），IRED（红外发光二极管）和信号处理电路的集成组合而成。 由于采用三角测量方法，物体的反射率，环境温度和操作持续时间的变化不易受到距离检测的影响。

<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-Digital-Distance-Interrupter-0.5-to-5cm%28GP2Y0D805Z0F%29-p-3084.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特性

- 易用
- 集成指示灯LED
- 数字输出


## 规格参数

|Item|Value|
|---|---|
|工作电压|3.3v/5v|
|触发范围|0.5cm - 5cm |
|工作温度|-10℃ -- 60℃|



## 应用

- 无触摸开关（卫生设备，照明控制等）
- 扫地机器人


## 支持平台

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |

!!!Caution
  上面提到的支持的平台是模块的硬件或理论兼容性的指示。 在大多数情况下，我们仅为Arduino平台提供软件库或代码示例。 无法为所有可能的MCU平台提供软件库/演示代码。 因此，用户必须编写自己的软件库。




## 入门指导

!!!Note
    如果这是您第一次使用Arduino，我们强烈建议您在开始前阅读[Getting Started with Arduino](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)



###  Arduino示例

#### 硬件

**物品准备**

| Seeeduino V4.2 | Base Shield| Grove - Digital Distance Interrupter 0.5 to 5cm |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Digital_Distance_Interrupter_0.5_to_5cm-GP2Y0D805Z0F/raw/master/img/thumnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Grove-Digital-Distance-Interrupter-0.5-to-5cm%28GP2Y0D805Z0F%29-p-3084.html" target="_blank">Get One Now</a>|

!!!note
    **1** 请轻轻插入USB电缆，否则可能会损坏端口。 请使用4线内的USB线，2线电缆不能传输数据。 如果您不确定自己的电线，可以点击 [here](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) to buy

    **2** 购买时，每个Grove模块都配有Grove电缆。 如果您丢失了Grove电缆，可以单击 [here](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) 购买

- **Step 1.** 将 Grove - Digital Distance Interrupter 0.5 to 5cm 插到 Grove-Base Shield 的 **D2**
口

- **Step 2.** 将 Plug Grove - Base Shield 与seeeduino 拼接

- **Step 3.** 将seeeduino和PC通过micro-USB连接.



![](https://github.com/SeeedDocument/Grove-Digital_Distance_Interrupter_0.5_to_5cm-GP2Y0D805Z0F/raw/master/img/connect.jpg)




!!!Note
如果我们没有Grove Base Shield，我们也可以直接将该传感器连接到Seeeduino，如下所示。

| Seeeduino     | Grove - Digital Distance Interrupter 0.5 to 5cm|
|---------------|-------------------------|
| 5V            | 红                     |
| GND           | 黑                   |
| Not Conencted | 白                   |
| D2            | 黄                  |



#### 软件

- **Step 1.** 打开Arduino IDE并创建一个新文件，然后将以下代码复制到新文件中。

```c++
/*
 *  
 * Copyright (c) 2018 Seeed Technology Co., Ltd.
 * Website    : www.seeed.cc
 * Author     : downey
 * Create Time: May 2018
 * Change Log :
 *
 * The MIT License (MIT)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#define SENSOR  2

void setup()
{
	Serial.begin(115200);
	pinMode(SENSOR,INPUT);
}


void loop()
{
	short val=0;
	val=digitalRead(SENSOR);
	Serial.print("val=");
	Serial.println((int)val);
	if(0==val)
	{
		Serial.println("Sensor is triggered!!");
	}
	delay(1000);
}

```

- **Step 2.** Upload the demo. If you do not know how to upload the code, please check [How to upload code](http://wiki.seeedstudio.com/Upload_Code/).

- **Step 3.** Open the **Serial Monitor** of Arduino IDE by click **Tool-> Serial Monitor**. Or tap the ++ctrl+shift+m++ key at the same time. Change the baud rate to **115200**.
if every thing goes well, you will get the output of this module.

The result should be something like that:

```
val=1
val=1
val=1
val=1
val=1
val=1
val=0
Sensor is triggered!!
val=0
Sensor is triggered!!
val=0
Sensor is triggered!!
val=1
val=1
val=1
val=1
```
通常，此传感器的输出为1（高），当物体进入传感器的测量范围时，它将被触发并输出0（低）


## 资源下载

- **[Zip]** [Grove - Digital Distance Interrupter 0.5 to 5cm eagle file](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/res/Grove-Round_Force_Sensor_FSR402.zip)
- **[PDF]** [GP2Y0D805Z0F Datasheet](https://github.com/SeeedDocument/Grove-Digital_Distance_Interrupter_0.5_to_5cm-GP2Y0D805Z0F/raw/master/res/GP2Y0D805Z0F.pdf)



## 技术支持
如果有问题请发邮件到 [techsupport@seeed.cc](techsupport@seeed.cc) 或者到论坛去提问 [forum](https://forum.seeedstudio.com/).
