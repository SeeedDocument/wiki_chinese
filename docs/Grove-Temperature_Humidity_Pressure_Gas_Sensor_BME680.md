---
name: Grove-Temperature&Humidity&Pressure&Gas Sensor(BME680)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020513
tags: 
---


![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/main.jpg)



Grove-温度&湿度&气压&气体 传感器(BME680)是一款可以同时测量温度、湿度、气压以及气体的多功能传感器。该模块基于BME60所设计，您可以将它用在需要测量这四个参数的GPS、IoT或者其他设备之中。


!!!**注**

“气体”指的是主要受[挥发性有机化合物](https://en.wikipedia.org/wiki/Volatile_organic_compound)影响的空气质量。在这之前（2018-08-08），这个模块不支持使用某些Arduino板对气体进行测量。它仅适用于诸如ATMEGA2560等大容量内存的Arduino。如果您使用的是的其他Arduino平台，例如：Arduino UNO、Seeeduino V4.2…… 那么测量到的气体值不精确。



<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-Temperature%2C-Humidity%2C-Pressure-and-Gas-Sensor-(BME680)-p-3109.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>




## 产品特点

- 4和1，多参数测量
- 低功耗
- 测量范围宽
- 可选输出: 
   
   可以独立启用/禁用各个湿度，压力和气体测量





## 产品规格

|**项目**|**参数**|
|:----:|:----:|
|工作电压|3.3V/5V|
|工作范围|-40~+85℃; 0-100% r.H.; 300-1100hPa|
|数字接口|IIC(高达3.4MHZ)/ SPI(3线或者4线, 高达 10MHz)|
|IIC 地址|0x76(默认)/ 0x77(可选)|







## 硬件概述


### 引脚映射

![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/pin_map.jpg)
![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/pin_map_back.jpg)



!!!**注意**

如果您想更改默认设置，您可能需要自己切割焊盘和焊接，请按照上图进行操作，使用刀具或烙铁时请小心。 



## 兼容平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|:-:|:-:|:-:|:-:|:-:|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |


!!!**注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。




## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**
| Seeeduino V4.2 | Base Shield| Grove-BME680 |
|:-:|:-:|:-:|:-:|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-Temperature%2C-Humidity%2C-Pressure-and-Gas-Sensor-(BME680)-p-3109.html" target="_blank">点击购买</a>|


!!!**注**

   **1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。

   **2** 购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。




- **步骤 1.** 将Grove-温度&湿度&气压&气体 传感器(BME680)连接到Grove - Base Shield的 **IIC** 接口。

- **步骤 2.** 将Base Shield插到Seeeduino上。

- **步骤 3.** 通过USB线缆将Seeeduino连接到PC端。


![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/7.jpg)


!!!**注意**

如果没有Grove Base Shield，我们可以直接按照下面引脚定义将模块连接到Seeeduino上。


| Seeeduino     |  Grove-BME680           |
|:-:|:-:|
| 5V            | 红                     |
| GND           | 黑                   |
| SDA           | 白                   |
| SCL           | 黄                  |




#### 软件代码

!!!**注意**


如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/).




- **步骤 1.** 从Github上下载[Grove BME680](https://github.com/Seeed-Studio/Seeed_BME680)库。

- **步骤 2.** 请参考如何为Arduino安装库[如何安装库文件](http://wiki.seeedstudio.com/How_to_install_Arduino_Library)。

- **Step 3.** 重启Arduino IDE。通过路径： **File --> Examples --> Seeed BME680 --> seeed_bme680_test**打开BME680示例程序。


![](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/img/demo_path.jpg)

- **步骤 4.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤 5.** 通过点击 **Tool-> Serial Monitor** 打开Arduino IDE的 **Serial Monitor** 。或者同事按下 ++ctrl+shift+m++ 。如果一切运行正常，您将会看到以下运行结果。


运行结果如下所示:


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


temperature ===>> 27.15 C
pressure ===>> 94.51 KPa
humidity ===>> 65.80 %
gas ===>> 101.76 Kohms

```


!!!**bug**

1 - 为了获得稳定和准确的值，您需要让Arduino的代码运行约2小时。其结果才更加可靠。

2 - 对于气体部分，它是一个反映了挥发性有机化合物气体值的可变电阻，，所以单位Kohms。

3 - 如果您想获得可靠的气体部件结果，请使用Arduino Mega并在[此处](https://github.com/Seeed-Studio/Seeed_BME680_V1)查看.


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Grove-Temperature-Humidity-Pressure-and-Gas-Sensor_BME680.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载

- **[Zip]** [Grove-BME680 Eagle file](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Grove-Temperature-Humidity-Pressure-and-Gas-Sensor_BME680.zip)
- **[Zip]** [Seeed BME680 Library](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/Seeed_BME680-master.zip)
- **[PDF]** [Datasheet of BME680](https://github.com/SeeedDocument/Grove-Temperature-Humidity-Pressure-Gas-Sensor_BME680/raw/master/res/BME680.pdf)


## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！