---
title: Grove - 3-Axis Analog Accelerometer
category: Sensor
bzurl: https://seeedstudio.com/Grove-3-Axis-Analog-Accelerometer-p-1086.html
oldwikiname: Grove_-_3-Axis_Analog_Accelerometer
prodimagename: Grove-3-axis_Analog_Accelerometer_photo.JPG
wikiurl: http://wiki.seeedstudio.com/cn/Grove-3-Axis_Analog_Accelerometer
sku: 101020051
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/img/Grove-3-axis_Analog_Accelerometer_photo.JPG)

ADXL335 是具有信号调节电压输出的轻薄，低功耗，完整功能的 3 轴加速度计。 该产品以 ±3 g 为最小量程测量加速度。
该模块被设计为分组板，因为 ADXL335 的信号是模拟(更多端口请求)。但板外型是 Grove 模块化的，您可以像对待其他 Grove 模块一样方便地使用。传感器组合 3.3 和 5V 电源，可用于标准 Arduino 设备和 Seeeduino Stalker。以下程序代码包括一级过滤器，当传感器用于机器人或玩具车时可以平滑地进行输出。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.79718794iEYzUc&id=520400638054)

产品特性
--------

-   3V 至 5V 宽范围直流电
-   Grove 外型
-   3 轴感应
-   小巧的包装 : 4×4×1.45mm LFCSP (引脚架构芯片级封装)
-   低功率下 3V 时 350µA (典型值)
-   高灵敏度
-   能承受 10,000 g 震动打击
-   每个轴使用单个电容器进行 BW 调整
-   符合 RoHS/WEEE 无铅标准

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 创意应用
-----------------

-   运动传感器
-   震动检测器
-   振动传感器
-   玩具车
-   机器人

## Platforms Supported
-------------------


## 使用须知
------------

我们建议您在使用气体传感器之前阅读这些知识，它将帮助您更多地了解 Arduino 和我们的产品，同时也让您更轻松地使用开放式硬件。

-   [Arduino 入门指导](/Getting_Started_with_Seeeduino)
-   [什么是 Grove system](/Grove_System)
-   [我为什么需要 Base shield?](/Base_Shield_V2)

阅读后，您将了解如何使用 Base shield 和 Grove 产品与 Arduino 配合使用。让我们开始吧 !


## 入门指导
-----

这个传感器没有 Grove 接口，需要通过杜邦线连接。

-   **VCC** 接至电源插口 (DC5V 或 DC3.3V), **GND** 接地, X 至 Arduino 模拟口 **A0**, Y 至 **A1**, Z 至 **A2**.
    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/img/Grove-3-axis_analog_accelerometer_V1.0_hardware.jpg)
-   下载 [3-Axis Analog Accelerometer Library](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/res/AnalogAccelerometer.zip) 通过路径 : **..\\arduino-1.0.1\\libraries** 将其解压缩到 Arduino IDE 的库文件中。
-   调节传感器

这个传感器是模拟设备，在使用前需要进行校对

**步骤 1:** 打开演示 : Calibration 然后下载到 Arduino 上。

**步骤 2:** 打开串行显示器，确保传感器已连接。按照印刷在传感器板上的轴机构。 首先确定Z轴方向是竖直的，如果你准备好了，请输入任何字符。 调整传感器位置，重复上述操作以获得 X 轴和 Y 轴方向的确认。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/img/3-Axis_Analog_Accelerometer.jpg)


**步骤 3:** 你可以得到如上所示的值。 请根据以下数据调整 ADXL335.h 的宏定义

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/img/Analog_Accelerometer_Code.jpg)

现在校准已经完成了

-   下载演示代码 : Measuring Acceleration，然后打开串行监视器，将传感器转动任意角度，可以看到从加速度计发送到串行监视器的数字角度值。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/img/3-Axis_Analog_Accelerometer1.jpg)

## 资源下载
---------

-   **[Eagle文件]** [Grove - 3-Axis Analog Accelerometer Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/res/Grove-3-Axis_Analog_Accelerometer_Eagle_File.zip)

-   **[库文件]** [3-Axis Analog Accelerometer Library](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/res/AnalogAccelerometer.zip)

-   **[芯片数据手册]** [ADXL335 datasheet.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Analog_Accelerometer/master/res/ADXL335_datasheet.pdf)

-   **[其他资源]** [github repository for 3-Axis Analog Accelerometer](https://github.com/Seeed-Studio/Grove_3Axis_Analog_Accelerometer)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Analog_Accelerometer -->
