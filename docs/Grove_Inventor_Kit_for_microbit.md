---
title: Grove Inventor Kit for micro:bit
category: Tutorial
bzurl:  https://www.seeedstudio.com/Grove-Inventor-Kit-for-micro%3Abit-p-2891.html
oldwikiname: Grove_Inventor_Kit_for_micro:bit
prodimagename: https://statics3.seeedstudio.com/seeed/file/2017-06/bazaar492598_8.jpg
wikiurl: http://seeed.wiki/Grove_Inventor_Kit_for_microbit
sku:    110060762
---
![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/zoro_im_kitbox.jpg)

BBC micro:bit 是一台袖珍电脑，它很容易地激发您的创造力，并且无需太多的电气和编码知识。有很多创作的可能性，您可以从 micro:bit 中挖掘出来，例如机器人或者乐器。 然而，如果您想创造更多的东西，只有 BBC micro:bit 是不够的，这就是为什么我们要向您介绍 Grove Inventor 工具包。

此 Grove Inventor 套件为您的 micro：bit 带来无限的可能性。该套件中的核心板是 Micro：Bit 的 Grove 扩展基板，借由此板可以使用大量的 Grove 模块，包括传感器，显示器，执行器与 Micro：Bit 进行交互。如果您从来没有使用过，也不知道 Grove 是什么，这里是 [Grove 系统](http://seeed.wiki/Grove_System/) 的介绍。 您所需要知道的是，Grove不再需要焊接或跳线。你的原型设计将更容易，更方便。

我们已经准备了8个Grove模块，让您可以开始使用 micro：bit。 使用这些Grove模块，您可以测量距离并显示它，使用手势播放不同的音乐，或者为您的办公桌或房间做个聪明的警卫。 我们已经准备好了免费下载的所有必要的库（包）。 如果你是一个初学者，不要担心，因为我们还准备了12个不同的项目，可以一步一步的教您。如果您是一个高级用户，这个工具包将帮助您实现比别人更有创意的项目。

!!!note
    - micro：bit 的输出电压约为3.0V，使用 micro：bit 或 AA 电池给电路供电可能会导致需要高输入电压和驱动电流的 Grove 模块（如 Grove-Ultrasonic Ranger）发生故障。为了使这些 Grove 模块正常工作，请使用 Grove 扩展板上的微型 USB 端口来为整个系统供电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.55310a21a8XTop&id=554282801498)

## 产品特性

  - 酷炫的扩展板可以接入丰富而方便的外设；
  - 专为 micro:bit 臻选的10个精品 Grove 模块；
  - 12 个酷炫的项目让您可以快速入门；
  - 详尽的指南与手册。

## 硬件概述


![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/first_im.jpg)

###  **产品清单**
| 项目名称 | 数量 |
|--------------------------|-----|
|Grove Shield for micro:bit|  1  |
|Grove - Rotary Angle Sensor(P)| 1 |
|Grove - Speaker | 1 |
|Grove - Ultrasonic Ranger| 1 |
|Grove - Light Sensor v1.2| 1 |
|Grove - WS2812 Waterproof LED Strip - 30 LEDs 1 meter| 1 |
|Grove - Gesture | 1 |
|Grove - 4-Digit Display| 1 |
|Grove - Red LED| 1 |
|Micro USB 数据线 - 48cm| 1 |
|12 项目说明书| 1 |
|Alligator 连接线| 10 |
|Grove 连接线| 7 |


## 操作指南

### Micro:bit 基础知识

如果您是第一次使用 Micro：bit，则需要了解一些相关的基本知识。您可以点击 [ **这里** ](https://microbit.org/code/) 来了解关于 Micro:bit 的更多信息。

Micro:bit 提供了两种类型的编辑器 - JavaScript Block Editor 和 Python Editor. JavaScript Block Editor 支持图形化编程，它简单易学。所以，本教程基于 JavaScript Block Editor。

这里有两个简单的步骤您需要注意，完成这两步之后您可以开始享受您的 Micro:bit。

#### 步骤1.打开编辑器

请点击 **[JavaScript Block Editor](https://makecode.microbit.org/)** , 然后您将看到一个图形化编程的页面。

#### 步骤2.添加 Grove 包
  - 点击右上角的齿轮 > 选择 **Add Package(添加包)**

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-1.png)

  - 输入下列链接 URL: **github.com/seeed-studio/pxt-grove**

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-2.png)

  - 现在您将在工具栏中看到 **Grove**。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-3.png)

### 例程 1.手势识别

这个手势识别传感器可以识别9种不同的手势。在这个例程中，您将学到如何在 micro:bit 中显示这些手势的名称。

#### 部件清单

|部件|数量|
|---|---|
|Grove - Gesture|1|
|Grove Shield for micro:bit|1|
|micro:bit|1|
|Grove 通用4脚连接线|1|
|Micro-USB 数据线|1|

#### 硬件连接

  - 将 **micro:bit** 插入 **Grove Shield for micro:bit**.
  - 通过标准4线Grove连接线将 Grove-Gesture 和 micro:bit 的 **I2C** 端口相连。
  - 通过 Micro-USB 数据线将 micro:bit 和电脑相连。

!!!warning
    在您将 micro:bit 插入 扩展板时请确保 LED 阵列是朝上的，否则您可能会损坏 micro:bit 开发板。


![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/Gesture%20Recognition.png)


#### 软件
  - 步骤1:

  添加 **Grove** 模组中的 **Gesture**（手势）模块

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-1.png)

  - 步骤2:

  选择Right（右边）,这样当您的手从右边移动到左边时，传感器就可以检测到。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-2.png)

  - 步骤3:

  添加 **Baisc** 模组中的 **show string** 模块， 然后将它嵌入到 **Gesture**（手势）模块。然后双击 "Hello!", 把它改成 "Right".

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-3.png)

  - 步骤4:

  用相同的方法添加 "Left" 和 "Clockwise" , 并且将 **show icon** 嵌入到 "Clockwise" 里.

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-4.png)

  - 步骤5:

  当您完成上诉工作请将工程重命名为 "gesture"， 然后您可以将这个工程文件下载到您的开发板上。您只需点击左下角的 **Download** 按钮， 下载 **microbit-gesture.hex** 到 MICROBIT 的内存中.


  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-5.png)

  好了，您可以畅玩您的 Microbit 了.

!!!tip
    - 您可以根据颜色来寻找模块。举个例子，如果您不知道 **show icon** 模块在哪里， 您可以看到它是蓝色的，然后 **Basic** 模块也是蓝色的，所以您可以在这里面找到它。简单有效吧:D


### 例程 2. Ultrasonic Meter

在这个例程中，您将学会如何使用超声波传感器去测量距离并且将它显示在显示屏上。

#### 部件清单
|部件|数量|
|---|---|
|Grove - Ultrasonic Ranger（超声波传感器）|1|
|Grove - 4-Digit Display（数码显示屏）|1|
|Grove Shield for micro:bit|1|
|micro:bit|1|
|Grove 通用 4pin 连接线|2|
|Micro-USB 数据线|1|

#### 硬件连接

  - 将 **micro:bit** 插入到 **Grove Shield for micro:bit**.

!!!warning
      在您将 micro:bit 插入 扩展板时请确保 LED 阵列是朝上的，否则您可能会损坏 micro:bit 开发板。

  - 将 Grove-Ultrasonic Ranger 连接到 micro:bit的 **P0/P14** 端口。
  - 将 Grove-4-Digit Display 连接到 micro:bit 的 **P1/P15** 端口。
  - 将 micro:bit 和您的电脑通过 Micro-USB 数据线相连。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/Ultrasonic_Meter.png)

#### 软件

  - 步骤 1:

  添加 **Basic** 模组中的 **on start** 模块, 然后添加 **Variables** 模组中的 **set item to 0** 模块, 将 ‘items’ 重命名为 ‘Display’。如果您已经成功安装了 Grove 模组，请使用 **Grove** 模组中的 **4-Digit Display at P0 and P0** 模块替换掉 **set item to 0** 模块中的**0**。并且将 P0-P0 改为 P1-P15。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-1.png)

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-2.png)

  - 步骤 2:

  添加 **Basic** 模组中的 **forever** 模块, 然后添加 **Grove** 模组中的 **item show number 0** 模块, 将 ‘item’ 重命名为 ‘Display’, 将 **item show number 0** 模块中的 ‘0’ 替换为 **Grove** 模组中的 **Ultrasonic Sensor (in cm) at P0** 模块.

  - 步骤 3:

  将 **Basic** 模组中的 **pause (ms) (100)** 模块嵌入到 **Forever** 模块中。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-3.png)

  - 步骤 4:

  重命名工程文件为 "Ultrasonic Meter", 下载即玩。


## 资源下载

  **用户手册** [Grove Inventor Kit for micro:bit User Manual](https://github.com/SeeedDocument/Grove_kit_for_microbit/blob/master/res/Guide-Grove%20kit%20for%20microbit.pdf)

  **[视频教程]** [micro:bit Getting Started Videos](http://microbit.org/start/)

  **[Microbit 官网]** [About micro:bit](http://microbit.org/about/)

  **[Microbit 硬件图]** [micro:bit Hardware](http://microbit.org/guide/hardware/)

  **[Grove Shield for microbit 原理图]** [Grove Shield for microbit_eagle file.zip](https://github.com/SeeedDocument/Bazzar_Attachment/raw/master/103030195/202001587_Grove%20Shield%20for%20BBC%20microbit%20V1.2_eagle%20file.zip)

  **[其他资源]** [micro:bit Apps](http://microbit.org/code/)
