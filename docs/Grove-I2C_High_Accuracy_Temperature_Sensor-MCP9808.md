---
title: Grove - I2C High Accuracy Temperature Sensor(MCP9808)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020556
tags: 
---

![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/main.JPG)
    
Grove - I2C 高精度温度传感器是一款基于MCP9808的高精度数字模块。不同于其他传感器，您可以选择该传感器测量分辨率。除了高精度温度测量，我们还提供可编程温度报警。我们使用一个独立的引脚来输出报警信号，您将会发现使用此信号作为控制其他板子的中断是多么地方便。
总之，我们相信这款传感器对于温度控制将会是一个新的开始！



<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-I2C-High-Accuracy-Temperature-Sensor%28MCP9808%29-p-3108.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特点


- 高精度
     - ±0.25℃ (典型值) -40℃ - +125℃
    - ±0.5℃ (最小值) -20℃ - 100℃
    - ±1℃ (最大值) -40℃ - +125℃

- 用户可选择测量分辨率
    - +0.5℃, +0.25℃, +0.125℃, +0.0625℃
- 用户可编程报警输出
- IIC 接口


## 产品规格

|**项目**|**参数**|
|:-:|:-:|
|工作电压|3.3V/5V|
|工作温度范围|-40°C to +125°C|
|数字接口|IIC 标准 400 kHz|
|IIC 地址|0x18(默认)/ 0x18~0x1F(可选)|



## 产品应用

- 工业应用
- 工业冷柜和冰箱
- 食品加工
- 个人电脑和服务器
- PC 外设
- 消费电子类产品
- 手持/便携式设备



## 硬件概述

### 引脚映射

![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/pin_map_front.jpg)
![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/pin_map_back.jpg)

**IIC 地址**

在PCB板的背面，我们提供了三组焊盘。默认情况下，AD0~AD2都被连接到低电平，您可以切断这些焊盘并将它们焊接到另一侧（高电平）。IIC地址是一个七位的地址 <mark>0011A<sub>0</sub>A<sub>1</sub>A<sub>2</sub></mark><mark>0011</mark>是出厂设置的地址码，我们无法改变。<mark>A<sub>0</sub>A<sub>1</sub>A<sub>2</sub></mark>是从可以改变的从机地址。默认设置是A<sub>0</sub>=0/A<sub>1</sub>=0/A<sub>2</sub>=0,所以IIC默认地址是<mark>0011000</mark>。通常情况下，地址应该是8位，所以我们需要向MSB（最高有效位）添加一位0，然后我们得到<mark>0001,1000</mark>.这是一个二进制地址，在代码中我们通常使用十六进制地址，因此让我们经二进制地址转换为十六进制地址，这里我们得到<mark>0x18</mark>。同样的道理，如果我们将所有的焊盘都焊接到高电平，我们将会得到<mark>0001,1111</mark>,即<mark>0x1F</mark>。所以IIC的地址范围是0x18到0x1F，您可以在其中选择您想要的地址，只需要将 **Grove_Temperature_sensor_MCP9808-master** 库中的 **Seeed_MCP9808.h** 里将IIC地址进行修改。


```c++
#define DEFAULT_IIC_ADDR  0X18
```
地址映射

A<sub>2</sub>=0|A<sub>0</sub>=0|A<sub>0</sub>=1
:-:|:-:|:-:
A<sub>1</sub>=0|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-000,0x18|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-001,0x19
A<sub>1</sub>=1|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-010,0x1A|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-011,0x1B

A<sub>2</sub>=1|A<sub>0</sub>=0|A<sub>0</sub>=1
:-:|:-:|:-:
A<sub>1</sub>=0|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-100,0x1C|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-101,0x1D
A<sub>1</sub>=1|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-110,0x1E|A<sub>2</sub>A<sub>1</sub>A<sub>0</sub>-111,0x1F


**<SPAN style="TEXT-DECORATION: overline">ALE</SPAN> 焊盘**

 <SPAN style="TEXT-DECORATION: overline">ALE</SPAN>焊盘在PCB板的背面。从该焊盘输出的报警信号可以被用来作为其他控制器的外部中断信号。默认输出是高电平，在该电路板应该是3.3V。当触发条件达到时，输出将变成0V。当您阅读完这篇wiki时，您就会设置这个触发条件了 😄




### 原理图

**IIC 地址**


![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/schamitc_a.jpg)

如上所述，我们使用这三组焊盘来选择IIC地址，如果您想要改变默认地址，可以切断导线并重新焊接。


**MCP9808**

![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/schamitc_c.jpg)

如上图所示， **<SPAN style="TEXT-DECORATION: overline">ALE</SPAN> 焊盘**通过一个上拉电阻连接到了3.3V。


**双向电平转换电路**

![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/schamitc.jpg)

这一个连接在IIC总线差分电压部分的典型双向电平转换电路。传感器的IIC总线使用3.3V，而Arduino的IIC总线使用的是5V，因此这个电路是必须的。如上面的原理图所示，**Q6** 和 **Q5** 是作为双向开关的N沟道场效应管[2N7002A](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/2N7002A_datasheet.pdf)。为了更好地理解这一部分，您可以参考[AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf)


!!!**提示**

在这一部分我们仅仅展示了部分原理图，完整的原理图文件请您参考 [资源下载](/#resources)


## 兼容平台

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|:-:|:-:|:-:|:-:|:-:|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |


!!! **注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。




## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**



| Seeeduino V4.2 | Base Shield| Grove - I2C 高精度温度传感器 |
|:-:|:-:|:-:|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-I2C-High-Accuracy-Temperature-Sensor%28MCP9808%29-p-3108.html" target="_blank">点击购买</a>|



!!!**注**

**1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。
    
**2** 购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。



- **步骤 1.** 将 Grove - I2C 高精度温度传感器连接到 Grove-Base Shield 的 **IIC** 接口上。

- **步骤 2.** 将Grove - Base Shield 插到 Seeeduino 上。

- **步骤 3.** 通过USB线缆将 Seeeduino 连接到 PC 端。


![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/connect.jpg)



!!!**注**

如果没有Grove Base Shield，我们可以直接按照下面引脚定义将模块连接到Seeeduino上。


| Seeeduino     |  Grove-MCP9808          |
|:-:|:-:|
| 5V            | Red                     |
| GND           | Black                   |
| SDA           | White                   |
| SCL           | Yellow                  |



#### 软件代码

!!!**注意**

如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。


- **步骤 1.** 从Github上下载 [Grove MCP9808](https://github.com/Seeed-Studio/Grove_Temperature_sensor_MCP9808) 库。

- **步骤 2.** 请参考如何为Arduino安装库[如何安装库文件](http://wiki.seeedstudio.com/How_to_install_Arduino_Library)。

- **步骤 3.** 重启Arduino IDE。 通过路径： **File --> Examples --> Grove Temperature Sensor MCP9808 --> MCP9808_demo_with_limit** 打开示例程序。


![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/demo_path.jpg)


!!!**提示**

如上图所示，我们提供了 **MCP9808_basic_demo** 和 **MCP9808_demo_with_limit** 两个例程。 **MCP9808_basic_demo** 示例程序仅仅提供了温度测量，报警函数并未启用。
而 **MCP9808_demo_with_limit** 示例程序启用了报警函数。如果您只是想测量温度，基础例程就可以胜任。如果您需要启用报警函数，请使用 **MCP9808_demo_with_limit** 示例程序。


- **步骤 4.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤 5.** 通过点击 **Tool-> Serial Monitor** 打开Arduino IDE的 **Serial Monitor** 。或者同事按下 ++ctrl+shift+m++ 。如果一切运行正常，您将会看到以下运行结果。

运行结果如下所示：

```C++
sensor init!!
temperature value is: 29.31
temperature value is: 29.31
temperature value is: 29.31
temperature value is: 29.25
temperature value is: 29.25
temperature value is: 29.25
temperature value is: 29.25
temperature value is: 29.25
temperature value is: 29.19
temperature value is: 29.25
```

**接下来让我们看一下如何使用 <SPAN style="TEXT-DECORATION: overline">ALE</SPAN> 焊盘。**

示例程序在 **MCP9808_demo_with_limit** 中:

```c++
#include "Seeed_MCP9808.h"


MCP9808  sensor;

void setup()
{
    Serial.begin(115200);
    if(sensor.init())
    {
        Serial.println("sensor init failed!!");
    }
    //Set upper limit is 30°C
    sensor.set_upper_limit(SET_UPPER_LIMIT_ADDR,0x01e0);
    delay(10);
    //Set upper limit is 32°C
    sensor.set_critical_limit(SET_CRITICAL_LIMIT_ADDR,0x0200);
    delay(10);
    //Enable the alert bit.The alert bit outputs low when the temperature value beyond limit.Otherwise stays high.
    sensor.set_config(SET_CONFIG_ADDR,0x0008);

    Serial.println("sensor init!!");
}


void loop()
{
    float temp=0;
    //Get temperature ,a float-form value.
    sensor.get_temp(&temp);
    Serial.print("temperature value is: ");
    Serial.println(temp);
    delay(1000);
}

```


除了测量温度以外，该代码还实现了另外一个功能。当温度低于30℃时，**<SPAN style="TEXT-DECORATION: overline">ALE</SPAN>  焊盘** 输出默认高电平--3.3V。当温度高于30℃时，**<SPAN style="TEXT-DECORATION: overline">ALE</SPAN>  焊盘** 将会输出低电平--0V。

也许您会有疑问：如何改变温度阈值？ 请您看第14行：

```c++
sensor.set_upper_limit(SET_UPPER_LIMIT_ADDR,0x01e0);
```
我们使用这个函数来控制温度，第一个参数是 UPPER_LIMIT 寄存器地址，第二个参数<mark>0x01e0</mark>是我们上面提到设置的十六进制温度值--30℃。<mark> 0x01e0 </mark>是一个四位十六进制数，右边的最后一位代表小数部分。 我们将其设置为0，有效数字为<mark> 0x1e </mark>。 **e** 表示十进制的14，高位 **1** 在十进制中代表16 。所以<mark>0x1e</mark>=16+14=30。

在 **Seeed_MCP9808.cpp** 文件中，我们提供三个函数。

```sensor.set_upper_limit(SET_UPPER_LIMIT_ADDR,u16);```

```sensor.set_lower_limit(SET_LOWER_LIMIT_ADDR,u16);```

```sensor.set_critical_limit(SET_CRITICAL_LIMIT_ADDR,u16);```

正如以上所提到的，**<SPAN style="TEXT-DECORATION:overline">ALE</SPAN>焊盘**默认输出高电平，当温度满足条件时，输出低电平。您可以使用这三个函数设置温度条件。

**sensor.set_lower_limit(SET_LOWER_LIMIT_ADDR,u16)** 可以被用来设置低温度限制，**u16**是我们所要设置的4位十六进制温度值。当温度低于我们的设定值时，**<SPAN style="TEXT-DECORATION: overline">ALE</SPAN>焊盘** 输出低电平。

**sensor.set_upper_limit(SET_UPPER_LIMIT_ADDR,u16)** 可以被用来设置高温度限制，**u16**是我们所要设置的4位十六进制温度值。当温度高于我们的设定值时，**<SPAN style="TEXT-DECORATION: overline">ALE</SPAN>焊盘** 输出低电平。

**sensor.set_critical_limit(SET_CRITICAL_LIMIT_ADDR,u16)** 被用于中断模式，在这篇wiki里面我们仅仅向您演示如何用作比较器。如果您想要了解更多，请您参考 [芯片手册](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/MCP9808_datasheet.pdf) 。

接下来，我们将通过lower_limit和upper_limit设置一个温度条件,当温度符合该温度条件时，输出将会变为低电平。

![](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/img/Zone.jpg)

举个例子，如果您需要 **<span style="text-decoration: overline">ALE</span>焊盘**在28℃到30℃之间输出高电平，在该温度范围之外输出低电平。

相关代码如下所示：

```c++

sensor.set_lower_limit(SET_LOWER_LIMIT_ADDR,0x01c0);
delay(10);
sensor.set_upper_limit(SET_UPPER_LIMIT_ADDR,0x01e0);
delay(10);

```

!!!注意
        请确保 **upper_limit** 高于 **lower_limit**,否则将会输出不正常。请确保 **critical_limit** 高于 **upper_limit** 。此外还需要一定的延时以确保参数被正确地写入寄存器。


## 资源下载

- **[Zip]** [Grove - I2C High Accuracy Temperature Sensor(MCP9808) Eagle files](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808.zip)
- **[Zip]** [Seeed MCP9808 Library](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/Grove_Temperature_sensor_MCP9808-master.zip)
- **[PDF]** [Datasheet of MCP9808](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/MCP9808_datasheet.pdf)
- **[PDF]** [Datasheet of 2N7002A](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/2N7002A_datasheet.pdf)
- **[PDF]** [AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf)


## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！