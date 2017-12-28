---
title: Grove - High Temperature Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-High-Temperature-Sensor-p-1810.html
oldwikiname: Grove_-_High_Temperature_Sensor
prodimagename: High_Temperature_Sensor_01.jpg
wikiurl: http://seeed.wiki/Grove-High_Temperature_Sensor
sku: 111020002
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/img/High_Temperature_Sensor_01.jpg)

热电偶是非常敏感的设备。它需要一个具有冷端补偿的良好放大器。Grove - High Temperatire Sensor 采用 K 型热电偶和热电偶放大器，通过热敏电阻测量环境温度进行冷端补偿。该传感器可检测范围为 -50-600°C，精度为 ±(2.0% + 2°C)

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.50e46bedwRG2Bv&id=45476571780&ns=1&abbucket=1#detail)

## 规格参数
--------------

-   电压 ：3.3 ~ 5V
-   25℃最大额定功率 ：300mW
-   工作温度范围 ：-40 ~ +125 ℃
-   温度测量范围是 (-50 ~ +600℃)
-   放大器输出电压范围 (0 ~ 3.3 V) mv
-   冷端补偿(环境温度测量)
-   热电偶测温精度 + / - 2.0% (+ 2 ℃)

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported
-------------------

## 入门指导
---------------

下面是一个示例，向您展示如何从传感器读取温度信息。

需要一个 Seeeduino V3.0 和一个 Grove - High Temperature Sensor.

### 硬件安装

**A4** 和 **A5** 连接 Seeeduino 的 I2C 线。将传感器插入 Seeeduino 的 I2C 端口以读取数据。

### 下载和上传代码

从 [这里](https://github.com/Seeed-Studio/Grove_HighTemp_Sensor/archive/master.zip) 下载库文件

然后将库提取到 Arduino 的库文件夹，打开示例文件夹中的演示。

然后上传到您的 Seeeduino.

### 打开串口监视器并获得数据

然后，打开你的串口监视器，你可以在这里找到摄氏温度。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/img/Htsdata.jpg)

### K type thermocouple indexing table

作为参考，下面是 K type thermocouple indexing table.

![](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/img/Ktype.jpg)

## 资源下载
--------

-   **[Eagle文件]** [Grove - High Temperature Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/res/Grove-High_Temperature_Sensor_v1.0_20140225.zip)
-   **[原理图PDF]** [Grove - High Temperature Sensor PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/res/Grove-High_Temperature_Sensor_v1.0.pdf)
-   **[库文件]** [High Temperature Sensor Library](https://github.com/Seeed-Studio/Grove_HighTemp_Sensor)
-   **[芯片数据手册]** [Datasheet OPA333 PDF](http://www.ti.com/lit/ds/symlink/opa333.pdf)
-   **[芯片数据手册]** [Datasheet LMV358 PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-High_Temperature_Sensor/master/res/Lmv358.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_High_Temperature_Sensor -->
