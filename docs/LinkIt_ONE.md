---
title: LinkIt ONE
category: LinkIt
bzurl: https://www.seeedstudio.com/LinkIt-ONE-p-2017.html
oldwikiname: LinkIt_ONE
prodimagename: 500px-Linkit-one-page.jpg
surveyurl: https://www.surveymonkey.com/r/LinkIt_ONE
sku: 102030002
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/500px-Linkit-one-page.jpg)


LinkIt ONE 开发平台是一款用于可穿戴设备和 IoT 设备的开源高性能板。 它是基于全球领先的可穿戴服装 SoC，联发科技（ATS）（**MT2502**）与高性能 Wi-Fi（**MT5931**）和 GPS（**MT3332**）芯片组相结合，为您提供访问 联发科 LinkIt 的所有功能。 它还为 Arduino 板提供了类似的引脚功能，可以轻松连接各种传感器，外围设备和 Arduino shields。


LinkIt One 可以用于IoT /可穿戴设备 的一体化原型设计板。 将 GSM，GPRS，Wi-Fi，GPS，蓝牙功能集成到基本的 Arduino 外形. LinkIt ONE 是由 [Seeed Studio](https://www.seeedstudio.com/) 和 [MediaTek](http://www.mediatek.com/)一起设计生产的。 它将双方的技术结合在开源硬件，可穿戴设备和IoT设备中，以这些为参考来设计更加强大的开发板。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1dcebac653clNY&id=45453335551)


!!!Note

    LinkIt ONE 板具有很多功能，其 SDK（软件开发工具包）非常全面。 在使用该板之前，请仔细阅读本文档一次。 作为共同设计产品基础级别 [Seeedstudio LinkIt One Forum](http://www.seeed.cc/discover.html?t=linkit) 提供硬件技术支持。高级技术支持可在 [MediaTek LinkIt 论坛](https://labs.mediatek.com/forums/forums/list.page)。这些论坛中有很多关于此板的常见问题解答。请先搜索您的要求/问题的解决方案，然后再发布问题，这样可以节省您的时间。

## 产品特性
--------------

- 在这个开发板上具有 ARM7 EJ-S™，GSM，GPRS，Wi-Fi，蓝牙BR / EDR / BLE，GPS，音频编解码器和 SD卡连接器。
- 与 Arduino 类似的引脚，包括与 Arduino 兼容的数字 I / O 端口，模拟I / O 端口，PWM，I2C，SPI，UART和电源连接口。
- 提供各种接口，用于连接大多数传感器，外设，Groves和其他小部件。
- 使用 LinkIt ONE 和 MediaTek LinkIt SDK（对于Arduino）能够轻松的实现你的想法，使其成为现实。

## 规格参数
------------------
|参数   |值          |
|:------|:-----------------|
|芯片|	MT2502A (Aster, ARM7 EJ-S (TM) )|
|时钟速度|	260MHz|
|外形尺寸|	3.3x2.1英寸|
|闪存|	16MB|
|RAM|	4MB|
|每个I / O引脚的直流电流|	1mA|
|模拟引脚|	3|
|数字输出	|3.3V|
|模拟输入|	5V|
|UART|	软件串口基于 USB 调制解调器端口和硬件串口 **D0** 和 **D1** |
|SD 卡|	高达32GB（10级）|
|定位|	GPS(MT3332)|
|GSM|	850/900/1800/1900 MHz|
|GPRS|	12级|
|Wi-Fi|	802.11 b/g/n|
|蓝牙|BR / EDR / BLE（双模）|

## 创意应用
--------------------
* 物联网
* 智慧之家
* 可穿戴设计
* 工业
* 传感器中心
* 自动化与运输

以下是一些项目供您参考。 更棒的项目 [Recipe](https://www.seeed.cc/projects.html?t=LinkIt) 和 [Instructables](http://www.instructables.com/howto/linkit+one/).

|Facebook Like Monitor|Texting Door Alarm|Smart Bed Alarm|
|--------------------------|-------------|---------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project2.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project3.jpg)|
|[马上制作](http://www.instructables.com/id/Facebook-Like-Monitor/)|[马上制作](http://www.instructables.com/id/LinkIt-One-Texting-Door-Alarm/)|[马上制作](http://www.instructables.com/id/Smart-Bed-Alarm-with-LinkIT-ONE/)|


|AWS IoT Tutorial|Instructables Indicator|DIY an Acrylic Case|
|--------------------------|-------------|---------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project4.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project5.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/project6.jpg)|
|[马上制作](http://www.instructables.com/id/An-AWS-IoT-Tutorial-With-LinkIt-ONE/)|[马上制作](http://www.instructables.com/id/Make-a-Instructables-Indicator/)|[马上制作](http://www.instructables.com/id/5-Design-of-Laser-Cut-Cases-for-5-Popular-Platform/)|



## 硬件概况
-------------------
![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/1000px-LinkItONE_RESOURCE.png)

### 配置开关
LinkIt ONE上有3个滑动开关，用于配置功能/工作模式：

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/300px-LinkIt_ONE_Wiki_Button.jpg)

|开关号|	功能|	位置1 - 功能|	位置2 - 功能|
|:------|:-----------------|:-----------------|:-----------------|
|1|	程式模式|	**MS**： 在这个位置下，当连接到PC时，LinkIt One 板将显示为 10MB 的USB驱动器。 程序将不会在此模式下执行。 任何复制到此驱动器的文件都可以通过代码读取|	**UART**： UART：该位置用于将电路板设置为编程模式。 可以在此模式下上传固件。|
|2|	电源|	**BAT**：板由锂离子电池供电。 要为电池充电，请将开关设置到此位置，并将电路板连接到PC。|	**USB**：板由 USB 端口供电。 当没有电池连接来编程电路板时，将开关置于此位置。|
|3|	SD/SPI|	**SPI**：此位置允许访问外部SPI引脚（D10 - D13）	|**SD**：此位置允许代码访问 SD 卡。 此模式也禁止 SPI 引脚（D10-D13）的访问。|

!!!Note
    当您处理 USB micro type-B 插座时，请小心，否则可能会关闭插座。

## 入门指导

### 硬件概述
|序号|	步骤|阅读更多|
|:------|:-----------------|:-----------------|
|1|	安装 Arduino IDE 1.5.7 Beta（Windows或MAC OS X版本）|	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#installing-arduino-ide)
|2|		[ 在 MediaTek 实验室中注册](http://labs.mediatek.com/dpRegister/create).	| |
|3|	下载[ Linkit开发人员指南](http://labs.mediatek.com/fileMedia/download/5fed7907-b2ba-4000-bcb2-016a332a49fd) 并且阅读它	||
|4|	安装Arduino IDE（Windows或MAC OS X）的 [ LinkIt SDK](http://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/sdk_intro/index.gsp) |	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#installing-mediatek-linkit-one-sdk)|
|5|	安装 LinkIt ONE 驱动程序。|	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#installing-drivers)|
|6|更新机载固件版本。|	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#updating-firmware)|
|7|	打开Arduino IDE，选择LinkIt ONE板并开始编码。|	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#uploading-code-blinky)|
|8|	将GSM，GPS和 WiFi / BT 天线连接到 LinkIt One 板|	[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#connecting-antennae)|
|9	|插入 SIM 卡和 Micro SD 卡|[ 这里](http://wiki.seeed.cc/LinkIt_ONE/#inserting-sim-card-and-sd-card)|
|10	|探索更多示例和享受制作的快乐吧！|||

### 安装 Arduino IDE
下载最新的 [Arduino IDE](https://www.arduino.cc/en/Main/Software) .有关更高级的主题，请按照 MediaTekTM[  说明](http://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/sdk_intro/index.gsp).

### 安装Mediatek LinkIt ONE SDK
- 下载Arduino 的 [LinkIt SDK](http://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/sdk_intro/index.gsp) 在编写本指南时，使用了 v1.1.11 的 Windows SDK（Beta）。 阅读 Windows OS 和 MAC OS X 平台的视频指南 [ 点击这里](http://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/get-started/index.gsp)
- 将下载的文件解压缩到 Arduino IDE 文件夹。
- 双击.EXE文件并安装。
- 通过安装LinkIt ONE SDK，Arduino IDE可以使用LinkIt ONE IDE。

### 安装驱动

- 禁用 **驱动程序签名强制** 如果您使用的是Windows 8 / 8.1操作系统。
- 阅读 [如何安装](http://www.seeedstudio.com/wiki/Download_Arduino_and_install_Arduino_driver#Installing_drivers_for_the_Seeeduino_with_window8)
- 将 MS / UART 滑动开关置于 UART位置，并将 LinkIt ONE 连接到 PC。
- 打开设备管理器，将显示以下 COM 端口。

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/LinkIt_ONE_Wiki_Temp1.jpg)

- 从 **.. \ LinkIt_ONE_IDE \ drivers \ mtk** 文件夹安装驱动程序。
- 安装驱动程序后，Device Manger 应显示以下两个端口：

   **MTK USB调试端口** 用于上传代码。

   **MTK USB调制解调器端口** 用于打印消息，如Serial.println（）

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/LinkIt_ONE_Wiki_Temp2.jpg)  

!!!Note
    还没有官方的 Windows 10驱动程序。 Windows 10 用户可以从 **设备管理器** 手动从 **\ LinkIt_ONE_IDE \ drivers \ mtk** 中选择 Windows 7 驱动程序文件。 这是众所周知的几台电脑。


### 更新固件
LinkIt ONE 主板的固件需要一段时间更新一次。 最新的 LinkIt ONE SDK 附带固件版本。

- 在启动固件更新之前，请确保滑动开关处于正确的位置（ **MS / UART** 应处于 **MS** 位置。**USB / BAT** 在 **USB** 位置）：

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/LinkItONEUpdateFirmware2.jpg)  

- 从..  **\ LinkIt_ONE_IDE \ hardware \ tools \ mtk** 文件夹运行 FirmwareUpdater.exe 应用程序。

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/400px-LinkItONEUpdateFirmware.jpg)  

- 点击按钮，然后将 LinkIt ONE 连接到 PC。 等待1分钟，更新成功完成。

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/400px-LinkItONEUpdateFirmware_ok.jpg)  
### 上传代码（Blinky）

- 应将滑动开关配置为固件上传（即将 MS / UART 置于 UART 位置，电源开关位于 USB 位置）。

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/LinkIt_ONE_Wiki_Temp3.jpg)


- 打开 **File（文件） - > Examples（示例） - > Basics - > Blink**。
- 在 **Tools（工具）** - > **Port（端口）** 中选择对应于 **MTK USB 调试端口** 的 COM 端口号。
- 编译并上传代码。
- LED标记 **L** 应闪烁。

### 连接天线
LinkIt ONE 提供三个天线。 它们用于：

- GSM / GPRS
- Wi-Fi / BT
- 全球定位系统

连接天线如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/400px-Linkit_one_antenna.jpg)

!!!Note
    - 从天线拉出天线时，请小心操作。 请不要使用暴力。
    - 尝试使用垂直于电路板方向的力，否则可能会损坏天线垫。

### 插入SIM卡和SD卡

LinkIt ONE 接受标准尺寸的 SIM 卡和 Micro SD 卡。 按照以下图像插入它们：

![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/LinkItONE_SIM_SDCard_Insert.jpg)

### 探索 LinkIt ONE SDK 示例

LinkIt ONE SDK 附带许多示例/示例代码，以使用像 GSM，GPRS，WiFi，BT， Audio，GPS等外围设备。首先浏览并阅读有关API文档。 API文档可在[  用户指南 ](http://labs.mediatek.com/fileMedia/download/5fed7907-b2ba-4000-bcb2-016a332a49fd) 和 [  API参考网站 ](https://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/api_references/Core_Digital.gsp)中找到


## LinkIt ONE 兼容的 Groves 和 Shields


- 我们生产的产品有数百个 Groves 和 Shields，包括传感器，执行器，显示器和其他模块。
- 您可以轻松地与 Groves 和 Shields 实现您的想法。
- 但是，LinkIt ONE 并不完全支持所有的这些。
- 我们准备了一个兼容的 Groves 和 Shields 列表：

[![](https://raw.githubusercontent.com/SeeedDocument/Linkit-ONE/master/image/400px-Compatible_Groves_and_Shields_for_LinkIt_ONE.png)](https://github.com/SeeedDocument/Linkit_ONE/raw/master/resource/LinkIt_ONE_Comparability_Test.xlsx)

## Linkit ONE 的 Sidekick Basic Kit 教程

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Linkit_ONE/master/image/350px-LinkitONESidebox.jpg)


LinkIt ONE 的 Sidekick Basic Kit 旨在与您的 LinkIt ONE 板一起使用。 该套件将帮助您快速与 LinkIt 的平台保持一致。 它包括许多最受欢迎的 DIY 项目配件：如面包板，跳线，彩色LED，电阻器，蜂鸣器等。所有这些都是一个方便的盒子，易于运输和模拟杂乱。 该套件包含一个完整的指南，可以让您熟悉各种电子元件，同时创建小型，简单，易于组装的电路。 这里概述了 10 种不同的课程，将为初学者熟悉 LinkIt ONE 提供一个最佳方式。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.52923521j573Bg&id=45457487196)

- [The Basics](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_The_Basics)
- [Hello World](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Hello_World)
- [Push Button](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Push_Button)
- [Marquee](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Marquee)
- [Colorful World](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Colorful_World)
- [Analog Interface](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Analog_Interface)
- [Mini Servo](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Mini_Servo)
- [Light Sensor](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Light_Sensor)
- [SMS Control the LED](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_SMS_control_the_LED)
- [Get Temperature with Webpage](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Get_temperature_with_Webpage)

- [Github Repo for Sidekick Basic Kit for LinkIt ONE](http://www.seeedstudio.com/wiki/LinkIt_ONE_Tutorial_-_Get_temperature_with_Webpage)

## 资源下载
**Schematic / Design Files:**

- [LinkIt ONE V1.0 Eagle File](https://github.com/SeeedDocument/Linkit_ONE/raw/master/resource/202000437_PCBA%20Linkit%20ONE_PDF.zip)
- [LinkIt ONE V1.0 Schematic in PDF](https://github.com/SeeedDocument/Linkit_ONE/raw/master/resource/%5B202000437%5DLinkIt%20ONE-V1_Eagle.zip)

**Software:**

- [MediaTek_LinkIt_SDK_for_Ardunio](http://labs.mediatek.com/site/znch/developer_tools/mediatek_linkit/sdk_intro/index.gsp)

**Datasheets and User Guides:**

- [LinkIt_ONE_Hardware_Reference_Design_v1_0](http://labs.mediatek.com/site/znch/access_denied/access_denied.gsp)
- [LinkIt ONE_Pinout Diagram_v1.0【PDF】](https://github.com/SeeedDocument/Linkit-ONE/blob/master/resource/LinkIt_ONE_Pinout_Diagram_v1_0.pdf)
- [MediaTek_LinkIt_Developers_Guide_v1_0【PDF】](https://github.com/SeeedDocument/Linkit-ONE/blob/master/resource/MediaTek_LinkIt_ONE_Developers_Guide_v1_3.pdf)
- [MediaTek_MT2502A_SOC_Data_Sheet_v1_0【PDF】](https://github.com/SeeedDocument/Linkit-ONE/blob/master/resource/MediaTek_MT2502A_SOC_Data_Sheet_v1_0.pdf)
- [MediaTek_MT5931_Wi-Fi_Data_Sheet_v1_0【PDF】](https://github.com/SeeedDocument/Linkit-ONE/blob/master/resource/MediaTek_MT5931_Wi-Fi_Data_Sheet_v1_0.pdf)
- [MediaTek_MT3332_GPS_Data_Sheet_v1_0【PDF】](https://github.com/SeeedDocument/Linkit-ONE/blob/master/resource/MediaTek_MT3332_GPS_Data_Sheet_v1_0.pdf)

**Getting Help**

- [Seeedstudio LinkIt ONE Forum](http://www.seeed.cc/discover.html?t=linkit)
- [MediaTek LinkIt ONE Forums](https://labs.mediatek.com/forums/forums/list.page)

**More**

- [See Also: Sidekick Base Kit for LinkIt ONE](http://www.seeedstudio.com/wiki/Sidekick_Basic_Kit_for_LinkIt_ONE)
