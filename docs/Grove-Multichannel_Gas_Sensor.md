---
title: Grove - Multichannel Gas Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Multichannel-Gas-Sensor-p-2502.html
oldwikiname: Grove_-_Multichannel_Gas_Sensor
prodimagename: Multi_sensor1.png
bzprodimageurl: http://statics3.seeedstudio.com/images/product/101020088 1.jpg
surveyurl: https://www.research.net/r/Grove-Multichannel_Gas_Sensor
sku: 101020088
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_wio
---

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Multi_sensor1.png">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Multi_sensor2.png">
        </td>
    </tr>
</table>


## 产品简介
Grove-Multichannel Gas Sensor是一个建立在MiCS-6814上的环境检测传感器，可以检测多种有害气体，由于其多通道特性，可以同时检测三种不同气体。因此，当环境内不止一种气体时，该传感器可以用于监测气体浓度。

这个传感器属于Grove system，你可以把它插到Base shield上，在不需要任何跳线的条件下，直接与Arduino组合使用。其接口为I2C，所以只需要将它连接到扩展板自带的I2C接口，就可以开始使用

<div class="admonition caution">
<p class="admonition-title">注意提示</p>

传感器值仅反映了允许误差范围内气体浓度的近似趋势, 它并不代表准确真实的气体浓度。空气中特定成分浓度的检测无法通过单一的传感器实现，通常需要更加精确和昂贵的设备。如果您的项目旨在获取高精度气体浓度数据，我们不建议您使用这个传感器。
</div>

----------------------

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.16.5e47879706k20S&id=521355807303)


开始之前
------------

### 相关阅读

我们极力推荐您在使用气体传感器之前，先阅读如下参考资料。这将帮助您了解更多关于Arduino和我们产品的相关知识。而且会使您在使用开源硬件时更得心应手。

-   [Arduino入门指导](/Getting_Started_with_Seeeduino)
-   [Grove系统简介](/Grove_System)
-   [Base_Shield使用指南](/Base_Shield_V2)

阅读完上诉资料后您将掌握如何使用Base_Shield板卡将Grove系列产品与Arduino相连。好了，现在让我们开始吧！

### 准备工作

这个教程将需要使用到下列产品，您可以点击查阅或购买对应产品:

-   [Arduino UNO R3](http://www.seeedstudio.com/depot/Arduino-Uno-Rev3-p-694.html) 或者 [Seeeduino v4](http://www.seeedstudio.com/depot/Seeeduino-V4-p-669.html)
-   [Base Shield](http://www.seeedstudio.com/depot/Base-Shield-V2-p-1378.html)
-   Grove - Multichannel Gas Sensor

硬件概述
-----------------

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Multi_sensor1.png)
</center>


| pin名称 |   相关描述           |
|-----------|-------------------------|
| GND       | 接地       |
| VCC       | 3.3V - 5V |
| SDA       | I2C data                |
| SCL       | I2C clock               |

该传感器的供电电压介于3.3V和5V之间，可与输出电压为3.3V的单片机兼容。

产品特性
-------

* 三个完全独立的传感单元
* 基于ATmega168PA
* 带有可编程地址的I2C接口
* 可以通过关闭加热功耗降低功率
* 可检测的气体种类：
 -  一氧化碳 CO 1-1000ppm
 - 二氧化氮 NO2 0.05-10ppm
 - 乙醇 C2H6OH 10-500ppm
 - 氢 H2 1-1000ppm
 - 氨 NH3 1-500ppm
 - 甲烷 CH4 >1000ppm
 - 丙烷 C3H8 >1000ppm
 - 异丁烷 C4H10 >1000ppm

模块图
-------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Grove-Multichannel_Gas_Sensor_block_diagram.jpg)

支持平台
-------------------
Arduino, linkit, wio



电气特性
--------------------------

|项目|状态|最小值|特征值|最大值|单位|
|----|----|------|------|------|----|
|电压|	- |3.1	 |3.3	 |5.25 |V   |
|波纹|最大供电	|-|	80	|100|	mV|
|发热功率	|-	|-	|-	|88	|mV|
|最大功率	|-	|-	|-	|150|	mV|
|ADC精度	|-	|-	|10	|-	|Bits|
|I2C速度|	-	|-|	100	|400|	kHz|
|VIL	|@I2C	|-0.5	|-	|0.99|	V|
|VIH	|@I2C	|2.31	|-	|5.25|	V|



### RED传感器性能

| Characteristic RED sensor  | Symbol | Typ | Min | Max  | Unit |
|----------------------------|--------|-----|-----|------|------|
| Sensing resistance in air  | R0     | -   | 100 | 1500 | kΩ   |
| Typical CO detection range | FS     | -   | 1   | 1000 | ppm  |
| Sensitivity factor         | SR     | -   | 1.2 | 50   | -    |

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Red_sensor.jpg)

### OX传感器性能

| Characteristic OX sensor    | Symbol | Typ | Min  | Max | Unit |
|-----------------------------|--------|-----|------|-----|------|
| Sensing resistance in air   | R0     | -   | 0.8  | 20  | kΩ   |
| Typical NO2 detection range | FS     | -   | 0.05 | 10  | ppm  |
| Sensitivity factor          | SR     | -   | 2    | -   | -    |

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/OX_sensor.jpg)

### NH3传感器性能

| Characteristic NH3 sensor   | Symbol | Typ | Min | Max  | Unit |
|-----------------------------|--------|-----|-----|------|------|
| Sensing resistance in air   | R0     | -   | 10  | 1500 | kΩ   |
| Typical NH3 detection range | FS     | -   | 1   | 300  | ppm  |
| Sensitivity factor          | SR     | -   | 1.5 | 15   | -    |

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/NH3_sensor.jpg)


入门指导
-------------

!!!注意
    为了得到稳定的数据，这个传感器需要预加热十分钟以上。

**硬件连接图:**

1.将 Grove - Multichannel Gas Sensor 和 Seeeduino按照下图方式相连.

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Grove-MultiChannelGasSensor.jpg)

**上传代码:**


如果您是第一次安装Arduino库文件，请点击 [这里](http://seeed.wiki/How_to_install_Arduino_Library/) 查看库文件的安装方法。


如果您不清楚怎么下载代码到您的板子里，请点击 [这里](http://seeed.wiki/Upload_Code/)。

2.下载 [Arduino Library & Grove/Xadow firmware](https://github.com/Seeed-Studio/Mutichannel_Gas_Sensor/archive/master.zip) 然后添加到Arduino库文件中。


3.按照以下路径打开示例程序:File -> Example -> Mutichannel_Gas_Sensor-> ReadSensorValue_Grove.

ReadSensorValue_Grove 的示例代码如下所示：

```c
// Read Data from Grove - Multichannel Gas Sensor
#include <Wire.h>
#include "MutichannelGasSensor.h"

void setup()
{
    Serial.begin(115200);  // start serial for output
    Serial.println("power on!");
    gas.begin(0x04);//the default I2C address of the slave is 0x04
    gas.powerOn();
    Serial.print("Firmware Version = ");
    Serial.println(gas.getVersion());
}

void loop()
{
    float c;

    c = gas.measure_NH3();
    Serial.print("The concentration of NH3 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_CO();
    Serial.print("The concentration of CO is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_NO2();
    Serial.print("The concentration of NO2 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_C3H8();
    Serial.print("The concentration of C3H8 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_C4H10();
    Serial.print("The concentration of C4H10 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_CH4();
    Serial.print("The concentration of CH4 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_H2();
    Serial.print("The concentration of H2 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    c = gas.measure_C2H5OH();
    Serial.print("The concentration of C2H5OH is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");

    delay(1000);
}
```

4.上传代码。请记得在Arduino软件的 工具 | 开发板中勾选对应的板卡，本例程使用的是Seeeduino Uno，同时请选择正确的串口。

打开串口监视器（ctrl+shift+M），您就可以看到来自传感器的数据了.

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/Mutichannel_Gas_Sensor_Grove_Print.jpg)

!!!tip
    - 更多的关于Grove模块的信息请点击参考 [Grove System](http://seeed.wiki/Grove_System/)

更新固件
-----------------

该Grove模块有一个ATmega168 MCU 出厂固件。固件已经于2016年11月11更新到了V2.0版本。通过下面的代码来检测您当前的固件版本。

```c
// Get firmware version of Grove Multichannel Gas Sensor
#include <Wire.h>
#include "MutichannelGasSensor.h"

#define SENSOR_ADDR     0X04        // default to 0x04

void setup()
{
    Serial.begin(115200);
    gas.begin(SENSOR_ADDR);

    unsigned char version = gas.getVersion();
    Serial.print("Version = ");
    Serial.println(version);    
}

void loop()
{
    // nothing to do
}
```

如果检测结果您的固件版本是V1，我们建议您更新固件到V2以获取更稳定的数据。

为了更新固件，您需要准备以下素材,

* An Arduino UNO/Seeeduino V3/
* 6 根杜邦线
* 烙铁

在板卡的背面留有ICSP焊盘，您需要将这些焊盘与Arduino板子相连。管脚定义如下表，连接方式如下图所示。

| Sensor | Arduino |
|--------|---------|
| MISO   | D12     |
| SCK    | D13     |
| NRST   | D10     |
| GND    | GND     |
| MOSI   | D11     |
| VCC    | 5V      |

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/firmware_connect.jpeg)

连接好之后，请打开您Arduino示例中的 **UpdateFrimware** , 运行，打开您的串口监视器。您将看到一些打印的信息。

输入一个 “ g ”来开始烧录。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/img/firmware_done.png)


校准
--------------

如果您总是得到一些不可靠的数据，请尝试校准传感器。打开示例中的 **calibration** ,上传至您的Arduino，打开您的串口监视器来查看校准的相关信息。

!!!注意
   在传感器出厂前已经校准过了，如果您想要重新校准，请确保校准时空气环境是新鲜清新的。校准大致需要几分钟到半小时不等的时间。

资源下载
---------

-  **[原理图]**  [Grove - Multichannel Gas Sensor v1.0 sch](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/res/Grove-Multichannel_Gas_Sensor_v1.0_sch.pdf)
-   **[PCB图]** [Grove - Multichannel Gas Sensor eagle files](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/res/Grove-Multichannel_Gas_Sensor_v1.0_eagle_files.zip)
-   **[库文件]** [Arduino Library & Grove/Xadow firmware](https://github.com/Seeed-Studio/Mutichannel_Gas_Sensor)
-   **[芯片数据手册]** [MiCS-6814 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Multichannel_Gas_Sensor/master/res/MiCS-6814_Datasheet.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Multichannel_Gas_Sensor -->

FAQ
---------
* **Q1. 如何改变模块的I2C地址**

    * *A1. 打开示例中名为I2C_Address的例程，运行它。*

* **Q2. 我改了I2C地址但是不小心忘了**

    * *A2. 别担心，运行示例中名为 factory_setting的例程，回到出厂状态。 *


!!!小提示
    如果您需要进一步的支持，请联系下面的邮箱，我们期待并欢迎您的咨询： [techsupport@seeed.cc]([techsupport@seeed.cc])
