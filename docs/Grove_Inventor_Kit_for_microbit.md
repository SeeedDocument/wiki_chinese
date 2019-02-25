---
name: Grove Inventor Kit for micro:bit
category: Tutorial
bzurl:  https://www.seeedstudio.com/Grove-Inventor-Kit-for-micro%3Abit-p-2891.html
oldwikiname: Grove_Inventor_Kit_for_micro:bit
prodimagename: https://statics3.seeedstudio.com/seeed/file/2017-06/bazaar492598_8.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Inventor_Kit_for_microbit
sku:    110060762
---
![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/zoro_im_kitbox.jpg)

The BBC micro:bit 是一个袖珍电脑，可以很容易地激发您的创造力，并且无需太多的电气和编码知识。有很多创作的可能性，您可以从 micro:bit 中挖掘出来，例如机器人或者乐器。 然而，如果您想创造更多的东西，只有 BBC micro:bit 是不够的，这就是为什么我们要向您介绍 Grove Inventor 工具包。

此 Grove Inventor 套件：为您的 micro：bit 带来无限的可能性。该套件中的核心板是 Micro：Bit 的 Grove 扩展基板，借由此板可以使用大量的 Grove 模块，包括传感器，显示器，执行器与 Micro：Bit 进行交互。如果您从来没有使用过，也不知道 Grove 是什么，这里是 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/) 的介绍。 您所需要知道的是，Grove不再需要焊接或跳线。您的原型设计将更容易，更方便。

我们已经准备了8个Grove模块，让您可以开始使用 micro：bit。 使用这些Grove模块，您可以测量距离并显示它，使用手势播放不同的音乐，或者为您的办公桌或房间做个聪明的警卫。 我们已经准备好了免费下载的所有必要的库（包）。 如果您是一个初学者，不要担心，因为我们还准备了12个不同的项目，可以一步一步的教您。如果您是一个高级用户，这个工具包将帮助您实现比别人更有创意的项目。

!!!note
    micro：bit 的输出电压约为3.0V，使用 micro：bit 或 AA 电池给电路供电可能会导致需要高输入电压和驱动电流的 Grove 模块（如 Grove-Ultrasonic Ranger）发生故障。为了使这些 Grove 模块正常工作，请使用 Grove 扩展板上的微型 USB 端口来为整个系统供电。

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
  - 点击右上角的齿轮 > 选择 **Add Package (添加包)**

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-1.png)

  - 输入下列链接 URL: **github.com/seeed-studio/pxt-grove**

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-2.png)

  - 现在您将在工具栏中看到 **Grove**。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/0-3.png)

### 演示 1. 手势识别

Gesture sensor 可识别 9 种不同的手势，在本演示中，您将学习如何在 micro:bit 上显示识别的手势名称。


#### 器材清单

|零件名称|数量|
|---|---|
|Grove - Gesture|1|
|Grove Shield for micro:bit|1|
|micro:bit|1|
|Grove 线缆|1|
|Micro-USB 线缆|1|

#### 连接

  - 将 **micro:bit** 插入 **Grove Shield for micro:bit**。
  - 通过 Grove 线缆将 Grove-Gesture 连接到 micro:bit 的 **I2C** 端口。
  - 通过 Micro-USB 线缆将 micro:bit 连接到 PC。

!!!Warning
    请确保插入 micro:bit 时 LED 阵列朝外，否则可能会损坏 micro:bit。


![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/Gesture%20Recognition.png)


#### 软件部分
  - 步骤 1:

  添加 Gesture sensor

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-1.png)

  - 步骤 2:

  选择 Right，以便传感器可以识别何时您的手从右向左移动。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-2.png)

  - 步骤 3:

  添加 Basic 块里的 **show string** 并将其嵌入到 Gesture 块中。然后双击 "Hello!"，将其更改为 "Right"。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-3.png)

  - 步骤 4:

  以同样的方式添加 "Left" 和 "Clockwise"，并将 **show icon** 嵌入到 "Clockwise" 中。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-4.png)

  - 步骤 5:

  完成上述所有操作后，重命名项目为 "gesture"。然后，您可以下载项目到您的主板。单击左下角的 **Download**，将文件 **microbit-gesture.hex** 下载到 MICROBIT 的 flash 中。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/1-5.png)

!!!tip
    你可以通过颜色找到块。例如，如果你不知道 **show icon** 的位置，但是它是蓝色的，**Basic** 模块也是蓝色的，你可以通过颜色找到它。简单而有效，不是吗 ?


### 演示 2. 超声波流量计

在这个演示中，您将学习如何使用超声波传感器来测量距离，并显示在显示器上。

#### 器材清单
|零件名称|数量|
|---|---|
|Grove - Ultrasonic Ranger|1|
|Grove - 4-Digit Display|1|
|Grove Shield for micro:bit|1|
|micro:bit|1|
|Grove 线缆|2|
|Micro-USB 线缆|1|

#### 连接

  - 将 **micro:bit** 插入 **Grove Shield for micro:bit**.

!!!warning
    请确保插入 micro:bit 时 LED 阵列朝外，否则可能会损坏 micro:bit。

  - 通过 Grove 线缆将 Grove - Ultrasonic Ranger 连接到 micro:bit 的 **P0/P14** 端口。
  - 通过 Grove 线缆将 Grove - 4-Digit Display 连接到 micro:bit 的  **P1/P15** 端口。
  - 通过 Micro-USB 线缆将 micro:bit 连接到 PC。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/Ultrasonic_Meter.png)

#### 软件部分

  - 步骤 1:

  添加 basic 块 **on start**，然后添加 variable 块 **set item to 0**，将 ‘items’ 重命名为 ‘Display’。如果您已成功添加 Grove 软件包，请将 **Grove block 4-Digit Display at P1 and P15** 替换为 ‘0’。

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-1.png)

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-2.png)

  - 步骤 2:

  添加 basic 块 **forever**，然后添加 Grove 块 **item show number 0**，将 ‘items’ 重命名为 ‘Display’，将 **Grove block Ultrasonic Sensor (in cm) at P0** 替换为 ‘0’。

  - 步骤 3:

  添加 basic 块 **pause (ms) (100)**.

  ![](https://github.com/SeeedDocument/Grove_kit_for_microbit/raw/master/img/2-3.png)

  - 步骤 4:

  重命名项目为 "Ultrasonic Meter"。


## 资源下载

  **[Eagle 文件]** [**Grove Shield for microbit eagle file.zip**](https://github.com/SeeedDocument/Bazzar_Attachment/raw/master/103030195/202001587_Grove%20Shield%20for%20BBC%20microbit%20V1.2_eagle%20file.zip)

  **[用户手册]** [**Grove Inventor Kit for micro:bit User Manual**](https://github.com/SeeedDocument/Grove_kit_for_microbit/blob/master/res/Guide-Grove%20kit%20for%20microbit.pdf)

  **[其他资源]** [**micro:bit Getting Started Videos**](http://microbit.org/start/)

  **[其他资源]** [**About micro:bit**](http://microbit.org/about/)

  **[其他资源]** [**micro:bit Hardware**](http://microbit.org/guide/hardware/)

  **[其他资源]** [**micro:bit Apps**](http://microbit.org/code/)
