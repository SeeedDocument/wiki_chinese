---
name: Grove - 2-Channel SPDT Relay
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 103020132
tags:
---

![](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/mian.jpg)


Grove - 2-Channel SPDT 继电器有两个单刀双掷（SPDT）开关。它只需要通过低电压和低电流信号来控制通断。具体地讲，您可以使用**5V DC**来控制最大**250V AC** 或者 **110V DC**。

您可以分别独立地控制两个通道。例如，通过SIG1控制，您可以根据需要将COM1连接到NC1或者NO1。它非常方便可靠，可以应用于开关高电压/大电流设备的大型产品或者工程中。


<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-2-Channel-SPDT-Relay-p-3118.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>

## 产品特点

- 耐高温塑料外壳
- 高电压负载
- 低功耗
- 持久工作

## 产品规格

|**项目**|**参数**|
|:----:|:----:|
|工作电压|5V|
|额定线圈电流|89.3mA|
|TUV认证负载|10A 250VAC/10 30VDC|
|UL认证负载|10A 125VAC/10A 28VDC|
|最大允许电压|250VAC/110VDC|
|功耗|约 0.45W|
|接触电阻|最大100mΩ|
|绝缘电阻|最小100MΩ（500VDC）|
|最大开关频率|30次操作/分钟|
|环境温度|-40℃ 到 +85℃|
|工作湿度|45% 到 85%（相对湿度）|
|触点材料|银氧化镉|
|输入接口|数字 SIG1/SIG2|
|输出接口|3引脚直插式绿色端子|

## 产品应用

- 家用电器
- 办公设备
- 遥控电视接收器
- 监视器显示
- 音响设备高冲电流应用

## 硬件概述

### 引脚映射

![](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/pin_map.jpg)

### 原理图

![](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/schematic.jpg)



**K1**是继电器模块，在K1的 **引脚1** 和 **引脚3** 之间有一个线圈。默认情况下，**COM1**与 **NC1**连通。如果K1的引脚3连接到地，那么线圈将会‘打开’，**COM1**将会连接到 **NO1**；

开启此线圈，需要约90mA的电流，然而，一般情况下Arduino的GPIO引脚只能提供20mA（最大40mA）。因此我们使用了一个可以提供500mA的NPN三极管[S9013](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/Transistors_NPN_25V-500mA.pdf)  。

当 **SIG1**通过10K电阻R2拉低时，如果没有信号，**Q1**的基极是0V，Q1关闭，那么K1将处于关闭状态。当 **SIG1** 为5V时，Q1将被打开。K1的 **引脚3** 会被连接到系统的GND，那么K1的 **引脚3** 和 **引脚1** 之间将会有5V的压差，线圈会被打开，然后 **COM1** 将会与 **NO1** 连接。

！！！**提示** 

**D3**是一个 [反激二极管（反冲二极管）](https://en.wikipedia.org/wiki/Flyback_diode)。反激二极管是连接在电感上的二极管，用于消除当电源电流突然降低或者中断时突然出现在感性负载上的电压尖峰。它被用于由开关控制的感性负载、开关电源和逆变器的电路中。


## 兼容平台


|Arduino|Raspberry Pi|BeagleBone|Wio|LinkIt ONE|
|:-:|:-:|:-:|:-:|:-:|
|![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) |![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo.jpg) |![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo.jpg) |![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo.jpg)  |

！！！**注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。


## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**

| Seeeduino V4.2 | Base Shield| Grove - 2-Channel SPDT Relay |Grove-LED x2|
|:-:|:-:|:-:|:-:|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/thumbnail.jpg)|![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/Red%20LED.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-2-Channel-SPDT-Relay-p-3118.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove---Red-LED-p-1142.html" target="_blank">点击购买</a>|



！！！**注**

   **1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。

   **2** 购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。

- **步骤 1.**  将Grove - LED的 **SIG** 引脚连接到Grove - 2-Channel SPDT 继电器的 **COM** 端口。将Grove - LED的 **GND** 引脚连接到Base Shield的 **GND** 。
- **步骤 2.**  将Grove - 2-Channel SPDT 继电器的 **NO** 端口连接到Base Shield的 **5V**。将Grove - 2-Channel SPDT 继电器的 **NC** 端口连接到Base Shield的 **GND**。

！！！ **注意**

步骤1 和步骤2 将Grove - LED的GND连接到系统的GND，将SIG连接到继电器的COM端口。如果COM端口连接到NO（5V），LED灯亮。如果COM端口连接到NC（0V），LED灯灭。在这篇wiki里我们使用两个LED，请确保LED<sub>1</sub> 连接到 Switch<sub>1</sub>,LED<sub>2</sub> 连接到 Switch<sub>2</sub>. 

- **步骤3** 将Grove - 2-Channel SPDT 继电器连接到Base Shield的 **D7** 端口
- **步骤4** 将Base Shield插到Seeeduino上
- **步骤5** 通过USB线缆将Seeeduino连接到PC端



![](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/connect.jpg)


#### 软件代码


！！！ **注意**

如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/).

- **步骤 1.** 打开Arduino IDE，创建一个新文件，然后将以下代码拷贝进去。

```c++
#include <Arduino.h>
uint8_t channel1 = 7;
uint8_t channel2 = 8;
void setup() {
  pinMode(channel1, OUTPUT);
  pinMode(channel2, OUTPUT);
}
void loop() {
  digitalWrite(channel1, HIGH);
  digitalWrite(channel2, LOW);
  delay(2000);
  digitalWrite(channel1, LOW);
  digitalWrite(channel2, HIGH);
  delay(2000);
}
```

- **步骤 2.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。
 
！！！**成功**

您将会看到板载的两个LED灯和两个Grove - LED一样交替亮灭。


![](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/img/test20180821_142634.gif)




## 资源下载

- **[Zip]** [Grove-2-Channel SPDT Relay eagle files](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/Grove-2-Channel_SPDT_Relay.zip)
- **[PDF]** [Datasheet of SRD 05VDC-SL-C Relay](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/SRD_05VDC-SL-C.pdf)
- **[PDF]** [Datasheet of S9013](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/Transistors_NPN_25V-500mA.pdf)



## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！