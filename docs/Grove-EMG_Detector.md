---
title: Grove - EMG Detector
category: Sensor
bzurl: https://seeedstudio.com/Grove-EMG-Detector-p-1737.html
oldwikiname: Grove_-_EMG_Detector
prodimagename: Emg_product.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-EMG_Detector
sku: 101020058
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/img/Emg_product.jpg)

 EMG detector 是连接人体和电路的的桥梁，传感器能够收集肌肉收缩的电信号，然后进行二次放大和滤波，输出的信号可以被 Arduino 识别。 您可以把此个信号添加到您的控制系统中。

<div class="admonition danger">
<p class="admonition-title">Note</p>
传感器不能用于医疗用途。
</div>

在待机模式下，输出电压为1.5V。 当检测到肌肉活动时，输出上升的信号，最大电压为3.3V。 您可以在3.3V或5V系统中使用这个传感器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.106e3452xLJRXV&id=45476931120)

产品特性
--------


- 能够兼容Grove接口
- 需要3.5mm插头的连接线
- 包含有6个可以随意使用的表面电极
- 电源电压：3.3V-5V
- 有1000mm长的数据线
- 无需额外的电源

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/img/Grove_EMG_detector.jpg)


- J2：grove接口，连接到模拟I / O;
- J1：EMG的可随意使用的表面电极连接器。
- U1：INA331IDGKT，差分放大器。
- U2，U3：OPA333，零漂移放大器。

示范
-------------




这个演示将向您展示如何使用 Grove - LCD RGB Backlight，我们需要一个 [Seeeduino V3.0](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112) ，[Grove - LED Bar](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.398f735cz1ZKTs&id=520900900588) 和 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)。

### 硬件安装

将 Grove - Base Shield 插入到 Seeeduino，然后将 Grove - LED Bar 连接到 **D8** 端口，将 Grove - EMG 传感器连接到 **A0** 端口。

最后，把三个电极粘到你的肌肉上，并保持每个电极之间的距离。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/img/Emg_connect.jpg)

### 下载代码和上传

您可以在 github 中下载演示代码，点击
[这里](https://github.com/Seeed-Studio/Grove_EMG_detector_demo_code/)，然后将其解压到任何地方。

然后将代码上传到 Seeeduino，如果您对代码上传有任何问题，请参阅
  [Seeeduino入门](http://wiki.seeedstudio.com/cn/Getting_Started_with_Seeeduino/)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/img/Emg_ide.png)

### 更多

下载演示代码后，初始化大约需要5秒钟，请先不要运动。

您可以看到，当初始化时，Led Bar将会从10级转为0级。当Led Bar全部关闭时，您可以马上做一些动作。

当你移动时，你可以发现Led Bar的级别会发生变化。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/img/Grove_emg_demo_2.gif)

资源下载
--------

-   [Grove-EMG Sensor v1.0 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/res/Grove-EMG_Sensor_v1.0.zip)
-   [Grove-EMG Sensor v1.1 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/res/Grove-EMG_Sensor_v1.1_Eagle.zip)
-   [Grove-EMG Sensor v1.1 schematic PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-EMG_Detector/master/res/Grove-EMG_Sensor_v1.1_SCH.pdf)
-   [Demo Code](https://github.com/Seeed-Studio/Grove_EMG_detector_demo_code)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_EMG_Detector -->
