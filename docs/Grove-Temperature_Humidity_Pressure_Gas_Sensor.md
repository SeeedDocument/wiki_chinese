---
name: Grove-Temperature&Humidity&Pressure&Gas Sensor(BME680)
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Temperature-Humidity-Pressure-and-Gas-Sensor-BME680.html
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020513
tags: 
---

Grove温湿度压力气体传感器（BME680）是一款多功能传感器，可以同时测量温度、压力、湿度和气体。它基于BME680模块，您可以在GPS、物联网设备或其他需要这四个参数的设备中使用此传感器。
  
![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/main.jpg)

Grove温湿度压力气体传感器（BME680）是一款多功能传感器，可以同时测量温度、压力、湿度和气体。它基于BME680模块，您可以在GPS、物联网设备或其他需要这四个参数的设备中使用此传感器。

!!!Note

    “气体”是指空气质量,主要受挥发性有机化合物（如e [VOCs](https://en.wikipedia.org/wiki/Volatile_organic_compound) ）气体影响。目前(8.8.2018)，此模块不支持某些Arduino开发板的气体测量。它仅适用于具有大RAM的Arduino平台（如ATMEGA2560）。如果您使用其他Arduino平台，如：Arduino Uno，请参见seedunio v4.2…你得到的气体值不准确。

[![click_to_buy](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://www.seeedstudio.com/Grove-Temperature%2C-Humidity%2C-Pressure-and-Gas-Sensor-(BME680)-p-3109.html)

!!!Tip

    我们已经发布了SEEED气体传感器选择指南，它将帮助您选择最适合您需要的气体传感器。

## 特征

- 4合1用于多次测量
- 低消耗
- 测量范围宽
- 可选输出：
- 单独的湿度、压力和气体传感器可以独立启用/禁用

## 具体参数

|项目|值
|----|----|
|工作电压|3.3V/5V
|工作范围|-40~+85℃；0-100%r.h.；300-11000hpa
|数字接口|I2c（最高3.4MHz）/SPI（3线和4线，最高10MHz）
|I2c地址|0x76（默认）/0x77（可选）

## 硬件概述

### 引脚映射

![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/pin_map.jpg)
![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/pin_map_back.jpg)

Seeeduino|Grove-BME680
----|----
5V| Red
GND |Black
SDA|White
SCL |Yellow

!!!Attention

    如果要更改默认设置，您可能需要自己切割焊盘和焊锡，请按照上图操作，使用刀或烙铁时请小心。

支持的平台

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |

!!!Attention
    上述支持的平台表示模块的软件或理论兼容性。在大多数情况下，我们只为Arduino平台提供软件库或代码示例。无法为所有可能的MCU平台提供软件库/演示代码。因此，用户必须编写自己的软件库。

## 入门

### Arduino演示

#### 硬件部分

所需材料

| Seeeduino V4.2 | Base Shield| Grove-BME680 |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/thumbnail.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3ff19e11ek83a4&id=45754325612)|[马上购买](https://www.seeedstudio.com/Grove-Temperature%2C-Humidity%2C-Pressure-and-Gas-Sensor-(BME680)-p-3109.html)|

!!!note

    **1** 请轻轻插入USB线，否则可能损坏端口。请使用内置4线的USB电缆，2线电缆无法传输数据。如果您不确定您拥有的电线，可以[单击此处购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.12.6b4f33dbNNLbE4&id=45774308858)

    **2** 购买时，每个Grove模块都配有Grove插头。如果不慎丢失，您可以[单击此处购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.33.775d33db4mcqCz&id=45575764936)

- **Step 1.** 将Grove温湿度压力气体传感器（BME680）连接到Grove Base Sheild的I2c端口

- **Step 2.** 将Grove-底座护板插入Seeduino

- **Step 3.** 通过USB电缆将seeeduino连接到PC

![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/7.jpg)

!!!note

    如果没有Grove Base Shield，我们也可以直接将此模块连接到Seeeduino，如下所示

| Seeeduino     |  Grove-BME680           |
|---------------|-------------------------|
| 5V            | 红                     |
| GND           | 黑                  |
| SDA           | 白                   |
| SCL           | 黄                 |

#### 软件部分

!!!Note

    如果这是你第一次使用Arduino，我们强烈建议你在开始前阅读[启动Arduino](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)

- **Step 1.** 从Github下载[Grove BME680库](https://github.com/Seeed-Studio/Seeed_BME680) 。

- **Step 2.**  请参阅[如何安装Arduino库](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/)安装库文件。

- **Step 3.** 重新启动Arduino IDE。通过以下路径打开“bme680”示例：**File --> Examples --> Seeed BME680 --> seeed_bme680_test**

![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/demo_path.jpg)

- **Step 4.** 上传演示。如果您不知道如何上传代码，请阅读[如何上传代码](http://wiki.seeedstudio.com/cn/Upload_Code/).

- **Step 5.** 单击工具->串行监视器，打开Arduino IDE的串行监视器。或者同时按ctrl+shift+m键。如果一切顺利，你就会得到结果。如下：

```c
Serial start!!!
temperature ===>> 27.14 C
pressure ===>> 94.51 KPa
humidity ===>> 65.76 %
gas ===>> 101.51 Kohms


temperature ===>> 27.15 C
pressure ===>> 94.51 KPa
humidity ===>> 65.76 %
gas ===>> 101.64 Kohms


temperature ===>> 27.14 C
pressure ===>> 94.51 KPa
humidity ===>> 65.77 %
gas ===>> 101.64 Kohms
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Grove-Temperature-Humidity-Pressure-and-Gas-Sensor_BME680.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源

- **[Zip]** [Grove-BME680 Eagle file](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Grove-Temperature-Humidity-Pressure-and-Gas-Sensor_BME680.zip)
- **[Zip]** [Seeed BME680 Library](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Seeed_BME680-master.zip)
- **[PDF]** [Datasheet of BME680](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/BME680.pdf)

## 技术支持

如果遇到问题，可以向我们的论坛求助 [forum](https://forum.seeedstudio.com/).
