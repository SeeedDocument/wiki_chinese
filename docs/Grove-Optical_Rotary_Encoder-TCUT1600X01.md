---
title: Grove - Optical Rotary Encoder(TCUT1600X01)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020587
tags:
---

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/main.jpg)

Grove - Optical Rotary Encoder(TCUT1600X01) 是包含一个红外发射器和两个光电晶体管探测器的透射传感器。通常情况下，红外线发射器发射红外线，光电晶体管探测器接收红外线，紧接着光电晶体管被打开，两个输出都处于高电平，板上的 LED 指示灯亮起。当中间出现障碍物时，光电晶体管无法接收红外线，因此光电晶体管被关闭且两个输出变为低电平，板上的 LED 指示灯熄灭。

您可以将此传感器作为旋转编码器来探测物体的转速。因为传感器拥有两个光电晶体管传感器，您也可以检测旋转的方向。

<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-Optical-Rotary-Encoder%28TCUT1600X01%29-p-3142.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特性

+ 双光电晶体管探测器，可检测旋转的方向
+ 板上 LED 指示灯
+ Grove 接口


## 规格参数

|项目|数值|
|---|---|
|工作电压|3.3V / 5V|
|工作温度|-40°C 到 +105°C|
|存储温度范围|-40°C 到 +125°C|
|发射器波长| 950 nm|
|间隙|3 mm|
|接口|数字型|


## 应用场景

- 汽车光学传感器
- 为编码器提供精确的位置感应
- 感应运动、速度和方向
- 用于 “turn and push” 编码的传感器


## 硬件概述

### 引脚图

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/pin_map_cn.png)


### 原理图

**电源**
![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/schematic.jpg)


TCUT1600X01 的电压典型值为 5V，所以我们使用 [MP3120](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/res/MP3120.pdf) 电流模式升压转换器来提供稳定的 5V 电压。MP3120 的输入电压在 0.8V 到 5V 之间，所以您的 Arduino 在 3.3V 和 5V 条件下都可使用此模块。

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/schematic_1.jpg) 


当光电晶体管探测器接受到红外信号时，输出应为高电平，当有障碍物遮挡了红外线时，OUT1 和 OUT2 输出皆为低。但由于漏电流的存在，输出不会为 0V。随输入电压的不同，漏电压也不同。

### 机械制图

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/Mechanical.jpg)


### 方向检测

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/principle.jpg)


!!!Tip
    因为有两个光电晶体管探测器的存在，我们可以检测到物体的移动方向。若物体从左向右移动，输出状态的变化为 **11 --> 01 --> 00 --> 10**；同样的，若物体从右向左运动，输出状态变化为 **11 --> 10 --> 00 -->01**.




## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg)  |


!!!Caution
    以上列出的支持平台仅代表硬件和理论的兼容性。大部分情况下我们仅提供 Arduino 平台的软件库和代码示例。为所有的MCU平台提供软件库和示例代码是不可能的。因此，使用者可能需要写出自己使用的软件库。



## 入门指导


### 搭配 Arduino 一起使用


#### 硬件连线

**硬件清单**

| Seeeduino V4.2 | Base Shield | Grove - Optical Rotary Encoder|
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-Optical-Rotary-Encoder%28TCUT1600X01%29-p-3142.html" target="_blank">点击购买</a>|


!!!note
    **1** 请小心插入USB线缆，否则您可能会损坏端口。请使用4线的USB线缆，2线的USB线缆无法传输数据。若果您不确定您拥有的是哪种USB线缆，可以 [点击此处](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) 购买。
    
    **2** 在您购买时，每个 Grove 模块都附带一根 Grove 线缆。若您丢失了该线缆，可以 [点击此处](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) 购买。



- **步骤一** 将 Grove - Optical Rotary Encoder 连接到 Base Shield（扩展板）的 **D5** 端口

- **步骤二** 将 Grove - Base Shield 插在 Seeeduino 上

- **步骤三** 通过 USB 线缆将 Seeeduino 连接到 PC 上


![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/connect.jpg)

!!!Note
        如果您没有 Grove Base Shield，您也可以按照以下方式将此模块连接到 Seeeduino 上


| Seeeduino     |  Grove - Optical Rotary Encoder         |
|---------------|-------------------------|
| 5V            | 红色                    |
| GND           | 黑色                    |
| D6            | 白色                    |
| D5            | 黄色                    |




#### 软件运行

!!!Note
        如果这是您第一次使用 Arduino， 我们强烈推荐您在开始之前阅读 [Arduino 入门](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。


- **步骤一** 将 **Encoder Library** 安装至 Arduino IDE。您可按照此路径： **Sketch-->Include Library-->Manage Libraries** 找到软件库

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/path.jpg)

然后在弹出窗口搜索 **encoder**。找到 **Encoder by Paul Stoffregen**，选择 **Version1.4.1**，点击 **Install**

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/path_1.jpg)

在软件库安装好后您会看到 <font style="font-weight:bold;color:#00C3CE">INSTALLED</font>，然后点击 **Close**.

![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/path_2.jpg)


> 感谢 Paul 提供的超棒软件库

    
- **步骤二** 重启 Arduino IDE。 打开示例，您可按照以下三种方式打开：
    1.通过以下路径在 Arduino IDE 中直接打开： **File --> Examples --> Encoder --> Basic**. 
    ![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/path_3.jpg)

    2. 在 **xxxx\Arduino\libraries\Encoder\examples\Basic** 中找到 **Basic.pde** 并打开， **XXXX** 是您安装 Arduino IDE 的目录。
    ![](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/img/path_4.jpg)

    3. 又或者，您可点击代码块右上角的图标 ![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg) 将代码复制到 Arduino IDE 的新文件中去。

```C++
/* Encoder Library - Basic Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 *
 * This example code is in the public domain.
 */

#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(5, 6);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
}

long oldPosition  = -999;

void loop() {
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    Serial.println(newPosition);
  }
}
```


!!!Tip
    您可以改变两个连接到编译器的引脚个数，为获得最佳性能：两个引脚都能中断。因此您可将代码的第13行改为 <mark>Encoder myEnc(2, 3);</mark>，同时，您应该将此传感器连接到扩展板的 **D2** 端口。

- **步骤四** 上传您的代码。若您不知道如何上传，请阅读文章 [如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤五** 点击 **Tool-> Serial Monitor** 打开 Arduino IDE 中的 **Serial Monitor**。或同时按下 ++ctrl+shift+m++ 键。将波特率设为 **9600**.


!!!success
     若一切顺利，您将得到结果。当您将物体从左到右移动时，计数值将逐 1 上升；当您将物体从右到左移动时，计数值将逐 1 递减。


```C++
Basic Encoder Test:
0
1
2
3
4
3
2
1
0
-1
-2
-3
-4
```

## 资源下载

- **[Zip]** [Grove - Optical Rotary Encoder 原理图](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/res/Grove-Optical_Rotary_Encoder-TCUT1600X01.zip)

- **[PDF]** [TCUT1600X01 数据手册](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/res/Optical_Sensor.pdf)

- **[PDF]** [MP3120 数据手册](https://github.com/SeeedDocument/Grove-Optical_Rotary_Encoder-TCUT1600X01/raw/master/res/MP3120.pdf)


## 项目

这是本产品的介绍视频，有简单代码展示，您可以一试。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ds7kBVdeY4U?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


## 技术支持
欢迎您将您的问题提交至我们的 [论坛](https://forum.seeedstudio.com/)。