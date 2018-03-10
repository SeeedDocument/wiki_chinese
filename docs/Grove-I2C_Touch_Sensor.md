---
title: Grove - I2C Touch Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-I2C-Touch-Sensor-p-840.html
oldwikiname: Grove_-_I2C_Touch_Sensor
prodimagename: Grove-I2C-Touch-Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-I2C_Touch_Sensor
sku: 101020047
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/img/Grove-I2C-Touch-Sensor.jpg)

 基于 FreeScale - MPR121 的 I2C Touch Sensor 与 Proximity Capacitive Touch Sensor 比较类似。 它能够检测到人手指的触摸或接近。 传感器包括一个触摸传感器控制器和四个手指探测器。 您可以将触摸传感器插入到控制器的底座，并开始检测触摸信号。


 [![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4a9eb9a1D2v3iZ&id=521241924726)

规格参数
-------------

| 参数            | 值/范围                  |
|------------------------|-------------------------------------|
| 工作电压                 | 3~5.5V                              |
| 待机模式电流             | 2μA                                 |
| 触摸信号接收通道          | 12（包含4个触摸的信号通道）   |
| 沟通协议                 | I2C                                 |
| I2C地址                 | 0x5A - 0x5D                         |

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/img/DSC_0030.png)

有12个电极包括 CH0-CH11。 而 CH0-CH3 将连接到 4 个触摸感应器上。

 CH4-CH11 电极可以由用户扩展它的功能。 如果你需要更多的话，你可以自己扩充。

传感器上的触感线可以通过弯曲它来减少周围环境的影响。 如果需要更高的灵敏度，则可以切断黑色的（接地）线。

如果客户想要使用 MPR121 的中断引脚，则必须将 INT 引脚引出。

入门指导
---------------

### **Grove - 帮助**

以下文档帮助用户开始使用Grove。

-   [Preface - Getting Started](http://www.seeedstudio.com/document/pdf/Preface.pdf)
-   [to Grove](http://www.seeedstudio.com/document/pdf/Introduction%20to%20Grove.pdf)

<div class="admonition note">
<p class="admonition-title">Note</p>
由于每个电极需要在上电期间由 MPR121 自动配置，并且触摸传感器控制器上没有电源复位，每次插入或移除触发器时，都需要重新设置 Seeeduino 的电源。
</div>

这个传感器也可以感觉到人手指之间存在的东西，也就是说，你不需要用手指切实的去触摸。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/img/DSC_0026.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/img/DSC_0027.jpg)

使用约 3 毫米厚的纸板，传感器可以感受到手指的触感，使用这样的功能，能够完成各种有趣的应用。

资源下载
---------

-   [I2C Touch Sensor Library](https://github.com/Seeed-Studio/Grove_I2C_Touch_Sensor)
-   [I2C Touch Sensor eagle files(v1.1).zip](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/res/I2C_Touch_Sensor_eagle_files-v1.1-.zip)
-   [I2C Touch Sensor PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/res/Grove-I2C_Color_sensor_v1.2.pdf)
-   [How to detect finger touch?](/How_to_detect_finger_touch?)
-   [I2C Touch Sensor Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Touch_Sensor/master/res/Freescale_Semiconductor;MPR121QR2.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_I2C_Touch_Sensor -->
