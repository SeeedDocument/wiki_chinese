---
title: Grove - Mini Track Ball
category: Sensor
bzurl: https://seeedstudio.com/Grove-Mini-Track-Ball-p-2586.html
oldwikiname: Grove_-_Mini_Track_Ball
prodimagename: Grove-Mini_Track_ball.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/101020091 3.jpg
surveyurl: https://www.research.net/r/Grove-Mini_Track_Ball
sku: 101020091
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/img/Grove-Mini_Track_ball.jpg)

Grove - Mini Track ball 将为您的应用提供一个实用的运动跟踪功能模块原型设计。 它具有高精度、快速响应的360度检测和单点检测功能， 集成在芯片 **STM32F103C8T6** 和 **AN48841B*中。 它也使用 Grove 接口进行标准化，这将为您在原型设计过程中节省大量工作。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ec57cb821QMNc&id=534730750709)

产品特性
--------

-   能够 360° 快速检测。
-   有半透明的点击按钮。
-   使用 Grove 接口进行标准化。
-   强大的 MCU 能够丰富您的应用程序。

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

创意应用
-----------------

-   游戏手柄的跟踪模块。
-   触觉控制器的跟踪模块。
-   玩具的跟踪模块

规格参数
-------------

| 参数                      |      数值                                |
|----------------------------------|------------------------------------------|
| 工作电压                         | 3.3V~5.5V (标准值为5V)                |
| 工作电流                         | 28 mA (最大工作电流：40 mA) |
| 工作温度范围                     | -25 ~ 75 ℃                               |
| MCU频率                          | 64 MHz                                   |
| 工作频率                         | 105±5kHz                                 |
|霍尔效应场强范围                  | (0.5) ~ (8) mT                           |

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/img/Grove-Mini_Track_ball_Hardware_Overview.jpg)

**Grove 界面**   
主控制电路板连接，如 **Seeeduino** 与 **Grove - Mini Track Ball**。


**MCU (STM32F103C8T6)**   
微控制器。

**跟踪球**   
接口控制动作。

### 产品清单

| 零件名称                 | 数量 |
|-------------------------|----------|
| Grove - Mini Track Ball | 1PC      |
| Grove 连接线             | 1PC      |

开始
-----------

### 所需材料

Seeeduino x 1

Grove 连接线 x 1

<div class="admonition tip">
<p class="admonition-title">Tip</p>
您可以使用<span style="font-weight:bold"> Grove - Base Shield v2</span> 使连接工作变得简单。
</div>

### **准备工作**

请参阅以下指南来构建适当的IDE:

<div class="admonition note">
<p class="admonition-title">注意</p>
在这种情况下，我们已经使用了 Seeeduino。
</div>

[Windows 入门](/Seeeduino_v4.2#Getting_Started_on_Windows)

[Mac OS X 入门](/Seeeduino_v4.2#Getting_Started_on_Mac_OS_X)

### 硬件连接

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/img/Grove-Mini_Track_ball_Hardware_Connection.jpg)

### 下载示例代码

1.请您下载 [示例代码](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/res/Grove-Mini_Track_ball_test.zip) 。


2.解压缩下载的ZIP文件。

3.打开文件 **Grove _-_ Mini_Track_ball_test.ino**

4.烧录（或上传）你的代码到 Seeeduino 板。如果上传过程完成，要打开串行监视器窗口，单击 **串行监视器** 在菜单 **工具** 下。

<div class="admonition note">
<p class="admonition-title">Note</p>
确保在 **工具** 菜单下.选择了正确的 <span style="font-weight:bold">开发板</span> 和 <span style="font-weight:bold">端口</span> 
</div>



5.跟踪球上的LED指示灯将以不同的模式亮起，持续约50秒

6.之后，您可以旋转或“点击”轨迹球以获取跟踪信息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/img/Grove-Mini_Track_ball_serial_output.jpg)

资源下载
---------

- [Schematic in Eagle](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/res/Grove-Mini_Track_ball_v1.0_schematic_files_in_Eagle.zip)
- [Schematic in PDF format](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/res/Grove-Mini_Track_ball_v1.0_schematic_files_in_PDF.zip)
- [STM32F103C8T6 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_Track_Ball/master/res/STM32F03C8T6.pdf)
- [AN48841B Datasheet](http://www.semicon.panasonic.co.jp/ds4/AN48841B_E.pdf)
- [Library file in Github](https://github.com/Seeed-Studio/Grove_Mini_Track_Ball)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Mini_Track_Ball -->
