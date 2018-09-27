---
title: Grove - 12 Key Capacitive I2C Touch Sensor V2 (MPR121)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020534
tags:
---

![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/main.jpg)


 **Grove - 12 Key Capacitive I2C Touch Sensor V2 (MPR121)** 是一个多通道电容式接近触摸传感器。它是一个三合一模块，具有以下三项功能：电容感应，触摸感应和接近感应。

**电容感应**: 此模块使用恒值直流电电容感应方案。它能感应从 10pF 到超过 2000pF 的电容，感应精度为 0.01pF。

**触摸感应**: 一旦得到了电极的电容数据，就可以通过和电容基准值比较来判断电极是处于触摸还是释放状态。

**接近感应**: MPR121的一个新的功能就是能够感知接近。这意味着系统中所有的电极可以总和起来成为一个单独的大电极。


基于 Freescale 的 MPR121，此传感器拥有12个完全独立的拥有内置自动配置功能的电极。因为它拥有 I2C 接口，您只需一个 Grove 端口就可以检测到所有12个电极的信号变化，并且I2C 的地址从 0X5B 到 0X5D 是硬件可配置的。因此也使得在单个系统中同时使用多个 **Grove - 12 Key Capacitive I2C Touch Sensor V2 (MPR121)** 成为可能，您最多可以用36个电极来制造一个触摸系统。


此传感器是 [Grove - I2C Touch Sensor](https://www.seeedstudio.com/Grove-I2C-Touch-Sensor-p-840.html) 的升级版。最初为了适应 Matsuzawa Takashi（我们的一位顾客）的需求，我们制造了这个拥有 I^2^C 个可变地址，且价格更为低廉的新版本。所以若您有任何关于 Grove 系列产品的建议，请与我们联系。我们期待您的声音，这可能会帮助已有 Grove 产品升级，甚至能帮助我们创造出新的 Grove 产品。希望您能在 [此页面](https://www.seeedstudio.com/grove_100) 写下您的建议。


<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-12-Key-Capacitive-I2C-Touch-Sensor-V2-%28MPR121%29-p-3141.html
" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 版本对照

|项目| Grove - 12 Key Capacitive I2C Touch Sensor V2 | Grove - I2C Touch Sensor |
|---|---|---|
|主芯片|MPR121|MPR121|
|I^2^C 地址|可变(0X5B ~ 0X5D)|不可变(0X5A)|
|触摸传感器|x|√|
|输入接口|鳄鱼夹|DIP 2Pin 母头|
|性价比|高|低|
|发布时间|2018年9月11日|2015年10月31日|


## 产品特性

- 内置10位 ADC
- 每个电极输入都有独立整合的自动校准功能
- 电极间完全独立，且有内置的自动配置功能
- 带有 IRQ 中断的 I2C 接口，可显示电极的状态改变
- I2C 地址硬件可配置
- 12个电极/电容感应输入中有8个可复用为 LED 驱动和 GPIO
- 每个电极输入的充电电流和充电时间可自动配置
- 每个电极可设定不同的触摸和释放电容阈值，提供一定的滞后性和电极独立性


## 规格参数

|项目|数值|
|---|---|
|工作电压|3.3V / 5V|
|工作温度|-40°C to +85°C|
|存储温度范围|-40°C to +125°C|
|电容范围|10 pF to over 2000 pF|
|感应精度|0.01 pF|
|每个引脚的 GPIO 拉电流|12 mA|
|每个引脚的 GPIO 灌电流|1.2 mA|
|接口|I^2^C|
|I^2^C 地址范围|0x5B,0x5C,0x5D|
|默认 I^2^C 地址|0x5B|


## 应用场景

- PC 外围设备
- MP3 播放器
- 遥控器
- 手机
- 照明控制


## 硬件概述

### 引脚定义

![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/pin_map_1_cn.png)


|引脚编号|引脚名称|功能|引脚复用|
|---|---|---|---|
|8|CH0| 通道0, 电极0, 输入电容的值|-|
|9|CH1| 通道1, 电极1, 输入电容的值|-|
|10|CH2| 通道2, 电极2, 输入电容的值|-|
|11|CH3| 通道3, 电极3, 输入电容的值|-|
|12|CH4| 通道4, 电极4, 输入电容的值|GPIO 或 LED 驱动|
|13|CH5| 通道5, 电极5, 输入电容的值|GPIO 或 LED 驱动|
|14|CH6| 通道6, 电极6, 输入电容的值|GPIO 或 LED 驱动|
|15|CH7| 通道7, 电极7, 输入电容的值|GPIO 或 LED 驱动|
|16|CH8| 通道8, 电极8, 输入电容的值|GPIO 或 LED 驱动|
|17|CH9| 通道9, 电极9, 输入电容的值|GPIO 或 LED 驱动|
|18|CH10| 通道10, 电极10, 输入电容的值|GPIO 或 LED 驱动|
|19|CH11| 通道11, 电极11, 输入电容的值|GPIO 或 LED 驱动|



!!!Tip
        对引脚 CH0 ~ CH11，一旦电极获得电容数据，经过和电容的基准值比较即可知电极的触摸/释放状态。您可以分别设置各个通道的基准值。引脚12 ~ 引脚19是可复用的，您可以将它们配置为 LED 驱动或者 GPIO。若您需要更多信息，可以查阅 freescale 的应用指导 [AN3894](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/res/AN3894.pdf).



![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/pin_map_2_cn.png)


!!!Danger
        中央的焊盘已经和地址线连接，您也可以通过切断引线和重新焊接来更改 I2C 地址。为了您和他人的安全，请小心使用刀具和焊枪。

### 原理图

**电源**

![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/schematic.jpg)


Freescale MPR121 的工作电压在 1.71V 到 3.6V 之间，但 Arduino 的工作电压在 3.3V 到 5V 之间。为了能够兼容 5V 系统，我们需要一个电压转换芯片来为 Freescale MPR121 提供 3.3V 的电压。

**双向电平转换器电路**

![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/schematic_1.jpg)


这是一个典型的双向电平转换器电路，用来连接 I^2^C 总线的两个不同的电压区。此感应器中的 I<sup>2</sup>C 总线使用 3.3V 电压, 若 Arduino 中的 I<sup>2</sup>C 总线使用 5V 电压, 您就会需要此电路。上面的原理图中， **Q1** 和 **Q2** 是一个N通道的 MOSFET [2N7002A](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/2N7002A_datasheet.pdf)，在这里承担双向开关的角色。为了更好地理解此部分，您可以查阅 [AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf)。



## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg)  |


!!!Caution
    以上列出的支持平台仅代表硬件和理论的兼容性。大部分情况下我们仅提供 Arduino 平台的软件库和代码示例。为所有的MCU平台提供软件库和示例代码是不可能的。因此，使用者可能需要写出自己使用的软件库。


## 入门指导


### 搭配 Arduino 一起使用


在这一部分，我们将会向您展示如何将 **Grove - 12 Key Capacitive I2C Touch Sensor V2 (MPR121)** 作为一个触摸传感器使用。至于如何将其配置为电容传感器或接近传感器，请查阅此 [数据手册](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/res/MPR121.pdf)。

#### 硬件连线

**硬件清单**

| Seeeduino V4.2 | Grove - Base Shield | I2C Touch Sensor V2|
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-12-Key-Capacitive-I2C-Touch-Sensor-V2-%28MPR121%29-p-3141.html" target="_blank">点击购买</a>|

!!!note
    **1** 请小心插入USB线缆，否则您可能会损坏端口。请使用4线的USB线缆，2线的USB线缆无法传输数据。若果您不确定您拥有的是哪种USB线缆，可以[点击此处](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)购买。
    
    **2** 在您购买时，每个 Grove 模块都附带一根 Grove 线缆。若您丢失了该线缆，可以[点击此处](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)购买。


- **步骤一** 将 Grove - 12 Key Capacitive I2C Touch Sensor V2 (MPR121) 连接到 Grove - Base Shield 上的 **I^2^C** 端口。

- **步骤二** 将 Grove - Base Shield 插到 Seeeduino 上。

- **步骤三** 通过一个 USB 线缆将 Seeeduino 连接到 PC 上。


![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/connect.jpg)

!!!Note
        若您没有 Grove 扩展板，您也可按照以下方式将此模块直接连接到 Seeeduino 上。


| Seeeduino     |  Grove-MPR121           |
|---------------|-------------------------|
| 5V            | 红色                     |
| GND           | 黑色                   |
| SDA           | 白色                   |
| SCL           | 黄色                  |


#### 软件运行

!!!Note
        如果这是您第一次使用 Arduino， 我们强烈推荐您在开始之前阅读 [Arduino 入门](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。


- **步骤一** 从 GitHub 上下载 [Grove touch sensor MPR121](https://github.com/linux-downey/Grove_touch_sensor_MPR121) 软件库。

- **步骤二** 参照 [如何安装软件库](http://wiki.seeedstudio.com/How_to_install_Arduino_Library) 来安装您下载的软件库

- **步骤三** 重启 Arduino IDE。您可通过以下三种方式打开例子：
    1. 在 Arduino IDE 中通过所示路径直接打开: **File --> Examples --> Grove touch sensor MPR121 --> MPR121_demo**.
    ![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/path.jpg)
    
    2. 在 **xxxx\Arduino\libraries\Grove_touch_sensor_MPR121-master** （ **XXXX** 是您安装 Arduino IDE 的目录）中找到 **MPR121_demo.ino** ，点击打开。
    ![](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/img/path_1.jpg)
    
    3. 又或者，您可以点击代码块右上角的图标![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg)复制下代码后将其粘贴到 Arduino IDE 的新文件中去。

```C++
#include "Seeed_MPR121_driver.h"

Mpr121 mpr121;

u16 touch_status_flag[CHANNEL_NUM]={0};
void setup()
{
  s32 ret=0;
  Serial.begin(115200);
  if(mpr121.begin()<0)
  {
    Serial.println("Can't detect device!!!!");
  }
  else
  {
    Serial.println("mpr121 init OK!");
  }
  delay(100);
}
void loop()
{
  u16 result=0;
  u16 filtered_data_buf[CHANNEL_NUM]={0};
  u8 baseline_buf[CHANNEL_NUM]={0};
  
  result=mpr121.check_status_register();

  mpr121.get_filtered_reg_data(&result,filtered_data_buf);

  for(int i=0;i<CHANNEL_NUM;i++)
  {
    if(result&(1<<i))                             /*key i is pressed!!*/
    {
      if(0==touch_status_flag[i])             
      { 
        touch_status_flag[i]=1;
        Serial.print("key ");
        Serial.print(i);
        Serial.println("pressed");
      }
    }
    else
    {
      if(1==touch_status_flag[i])
      {
        touch_status_flag[i]=0;
        Serial.print("key ");
        Serial.print(i);
        Serial.println("release");
      }
    }
  }
  delay(50); 
}
```

- **步骤四** 上传您的代码。若您不知道如何上传，请阅读文章 [如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤五** 点击 **Tool-> Serial Monitor** 打开 Arduino IDE 中的 **Serial Monitor**。或同时按下 ++ctrl+shift+m++ 键。 将波特率设置为 **115200**。


!!!success
     若一切顺利，您将得到结果。当您触摸 CH0 ~ CH11 块时，会触发 **key ?pressed** 和 **key ?release**


```C++
mpr121 inmpr121 init OK!
key 11pressed
key 11release
key 10pressed
key 10release
key 0pressed
key 0release
key 2pressed
key 2release

``` 


## 资源下载

- **[Zip]** [Grove - 12 Key Capacitive I2C Touch Sensor V2 原理图文件](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/res/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121.zip)

- **[Zip]** [Grove touch sensor MPR121 软件库](https://github.com/linux-downey/Grove_touch_sensor_MPR121/archive/master.zip)

- **[PDF]** [MPR121 数据手册](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/res/MPR121.pdf)

- **[PDF]** [AN3894 数据手册](https://github.com/SeeedDocument/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/raw/master/res/AN3894.pdf)



## 项目

这是本产品的介绍视频，有简单代码展示，您可以一试。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ds7kBVdeY4U?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



## 技术支持
欢迎您将您的问题提交至我们的 [论坛](https://forum.seeedstudio.com/)。
