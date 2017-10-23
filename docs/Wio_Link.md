---
title: Wio Link
category: Wio
bzurl: https://www.seeedstudio.com/Wio-Link-p-2604.html
oldwikiname: Wio_Link
prodimagename: WioLink.png
wikiurl: https://seeed.wiki/Wio_Link
sku: 102110037
---



![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/WioLink.png)


建立IoT应用程序最困难的部分是什么？ 有人说讨厌跳线，而另一个人说他最讨厌焊接。 甚至有些人不喜欢面包板。 也许你不是其中之一，但电子工程，微控制器编程，网络编程，IoT 协议处理的知识, 仍然是您成功搭建物联网项目的巨大负担。为了简化所有这些步骤，在2015年底，Seeed Studio 启动了 [Wio Link KickStarter](https://www.kickstarter.com/projects/seeed/wio-link-3-steps-5-minutes-build-your-iot-applicat?ref=nav_search), 定义了开发 IoT 应用的新方式。 Wio Link 是一款基于 ESP8266 SoC 的开源Wi-Fi开发板，其最重要的部分是允许用户通过使用移动应用程序，虚拟化即插即用模块，用 RESTful API 来创建 IoT 应用程序。 这意味着只要在手机上安装一个应用程序，就可以在5分钟内构建一个简单的 IoT 项目，就不会有硬件编程，没有面包板，没有跳线，也没有焊接。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.587534abSgehPe&id=555309142801)

## 产品特征

- 无硬件编程，无面包板，无跳线，无需焊接。
- 支持许多Grove模块（检查Mobile App中的列表）。
- 即插即用Grove模块
- 视觉配置而不是微控制器编程。
- 通过云端编译和OTA自动更新。
- 将现实世界带入虚拟平台。 所有传感器都成为虚拟RESTful API。
- Android和iOS Apps来管理Wio Link。
- 支持IFTTT

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio_Link_Banner.gif)

## 规格参数
----
|描述|值|电源|值|
|:---|---|:---|---:|
|**尺寸**|55mm * 48mm|**每个I/O的直流电流**|12mA|
|**晶振**|26MHz|**输入电压(Micro USB)**| 5V|
|**闪存**|4MBytes (W25Q32B)|**输入电压(电池接口)**|3.4~4.2V|
|**Wi-Fi 网络协议**|802.11b/g/n|**输出直流电流**|1000mA MAX
|**Wi-Fi 加密技术**|WEP/TKIP/AES|**工作电压**|3.3V|
|**Grove Connectors**|6 |**充电电流**|500mA MAX|
|**Flash**|	4MB (W25Q32B)|

## 创意应用
----
Wio Link精心设计，为以下项目提供简单的Wi-Fi解决方案：

- 智能家居
- 智能环境监测
- 搞笑玩具
- 物联网
- 物联网

其实我们已经设计了很多项目 [**recipe**](http://www.seeed.cc/projects.html?t=Wio), 来参观，找到一些有趣的项目，甚至分享你自己的项目，我相信会为你赢得很多粉丝〜

|浇灌系统 |LED灯光墙 | 自动喂食器|
|---|---|---|
|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/2.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/1.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/3.png)|
|[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1274)    |[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1594) |[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1066)|

|Kickstarter监控|未接来电监控|监控老板的突现|
|---|---|---|
|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/4.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/5.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/6.png)|
|[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1081)    |[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1059) |[MAKE IT NOW](http://www.seeed.cc/project_detail.html?id=1077)|

!!!Note
       * 一些应用是为Wio Node制作的，但它也适用于Wio Link。

## 硬件概述
---

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Hardware%20overview.jpg)

|描述|功能|
|---|---|
|MCU	|ESP8266|
|数字Port 0	|GPIO 14|
|数字Port 1|	GPIO 12|
|数字Port 2	|GPIO 13|
|Analog Port	|A3|
|UART Port|	Pin 1 & Pin 3|
|I2C Port|	Pin 4 & Pin 5|
|Status Light|蓝色LED是WiFi状态指示灯，红色LED表示工作状态|
|Configure Button| 配置和管理您的Wio Link|
|Battery Holder|JST2.0|
|Micro USB|为电路板供电或与PC通讯|
|Reset Button| 复位MCU|

###  LEDs指示灯
在FUNCTION按钮附近有2个状态LED，一个蓝色和一个红色。 蓝色LED指示网络状态。 它有以下闪烁模式：

- 呼吸配置模式下
- 快速闪烁两次，然后关闭1秒，请求路由器的IP地址
- 快速闪烁一次，然后关闭1s，连接到服务器
- 在1秒后关闭1s，已经连接到网络
- 快速闪烁（100ms亮100ms灭）OTA模式

!!!Note
     * 蓝色LED是连到GPIO2，也是UART1的TX引脚。 当下载固件时，UART1会直接转储UART0发送的数据。 所以在下载固件时，BLUE LED会闪烁。 启动后，GPIO2将被配置为GPIO, 而不是UART1的不是TX。

红色LED是Grove模块的电源指示灯。 所有六个Grove接口的VCC汇聚在一起，可以通过GPIO 15进行控制。当节点处于深度睡眠模式时，所有Grove模块都会断电。 当Grove模块通电时，红色LED将亮起，当Grove模块未通电时，红色LED将熄灭。

### 其他功能
Wio Link具有内置的LiPo电池充电器，因此当USB连接时，您可以通过JST 2.0端口为3.7v LiPo电池充电。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/500px-Wio_Link_Battery.jpg)

!!!Note
     * 电池需要独立购买. 请访问 [Bazzar](https://www.seeedstudio.com/s/Battery.html) 采购。

## 入门指导
---

让我们用Wio Link构建一个非常基本的LED应用程序，在这个应用程序中，您将能够在5分钟内通过智能手机控制LED。 在我们开始之前，请确保你有以下的东西：

|Wio Link|Grove - LED|Micro USB Cable|
|:--------:|:-----------:|:---------------:|
|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio%20link%20small%20image.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Red%20LED.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/48cmUSBc.jpg)|
|[GET ONE NOW](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.587534abSgehPe&id=555309142801)|[GET ONE NOW](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.32.37296343Mc4sBK&id=45476819992)|[GET ONE NOW](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.155de3bePO3UzW&id=521385344999)|

!!!NOTE
    * 还需要智能手机（Android操作系统版本4.1或更高，iOS版本7或更高）
    * Grove - LED 包括 Grove cable

### **步骤1**： 安装Android / iOS应用程序
您需要安装Wio Link应用程序来管理和配置您的Wio Link设备。

下载Android或iOS App并进行安装。 或者你可以去Apple Store或Google Market的App Store搜索“Wio Link”，你会发现它。

|[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Android%20Robot%20new.jpg)](https://play.google.com/store/apps/details?id=cc.seeed.iot.ap)|[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Apple%20new.jpg)](https://itunes.apple.com/us/app/wio-link/id1054893491?mt=8)|
|:---:|:---:|
|[Get Android App](https://play.google.com/store/apps/details?id=cc.seeed.iot.ap)|[Get iOS App](https://itunes.apple.com/us/app/wio-link/id1054893491?mt=8)|

!!!Note
    * 确保您的Android操作系统版本是4.1或更高，iOS版本是7或更高。

### **步骤2**： 创建您的帐户
- 如果是您第一次使用Wio APP，可能需要您同意GPS授权，然后才能注册。
- 如果您已经有帐户，请在登录之前检查服务器的位置。

!!!Note
    * 请注意服务器位置，因为连接到Wio Link时服务器位置错误将导致故障。如果您在中国，请选择中国服务器。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)

### **步骤3**：连接Wio Link Wi-Fi AP
- 按住CONFIG按钮，直到蓝色LED变为呼吸模式（即闪烁，淡入淡出效果）。 这意味着Wio Link已经成功地转到配置模式，并且可以被Wio App检测到。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/WioLink_Configure-middle.png)

- 点击 "Add your first Device".
- 选择 Wio Link
- "Go to Wi-Fi list" 带您进入智能手机的Wi-Fi设置界面。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-1new.png)

- 如果您已成功将蓝色LED转为呼吸模式，您将在Wi-Fi列表中找到Wio Link，并连接到它（通常在Wi-Fi列表中通常不称为Wio Link，在该示例中， 我的是Wio_8B2F12，您可以在列表中找到一个名为wio_xxxxxx的文件。）
- 连接后，您将收到通知，然后您可以回到应用程序。
- 下一步是连接到家庭或公司的Wi-Fi

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-2.png)

- 如果您要连接的Wi-Fi有密码，需要输入密码
- 考虑到将来可能需要连接超过1个Wio设备，一个特殊的名称可以让您轻松区分它们。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-3.png)

### **步骤4**：使用Wio Link实现互连模块和更新固件
- 点击Wio Link，你将进入主界面。
- 有6个Grove连接器，选择左边的第一个。
- 因为LED是输出设备， 选择输出类别。
- 找到看起来像灯泡的图标，选择它。
- 然后您会发现底部矩形按钮变为红色，“View API”变为“Update Firmware”， 选择“Update Firmware”

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step4.png)

- 由于您在APP中选择了数字0端口与LED连接，所以您需要物理上将Grove-LED连接到Wio Link的数字0端口。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio_Link_Grove_LED%20middle.JPG)

### **步骤5**：使用API测试应用程序
- 现在您已经将LED连接到Wio Link，点击“View API”来检查Wio Link的API
- 在“Test Request”区域中输入“1”或“0”，然后单击“Post”按钮，看看会发生什么。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step5.png)


## 开始使用IFTTT＆DoButton
---
不知道如何编码？ 不用担心，在[IFTTT](https://en.wikipedia.org/wiki/IFTTT) 帮助下, 即使您对编码一无所知，您仍然可以构建一些简单的项目。

IFTTT是“If That Then That”的缩写，它是一种免费的基于Web的服务，允许用户创建简单条件语句链，称为“recipes”，这些链接是基于其他Web服务（如Gmail， Facebook，Instagram。 IFTTT如何与Wio Link工作？ 如下图所示，Seeed在wio.seeed.io提供云服务，可以交换数据并向IFTTT和Wio Link发送指令。 所以通过创建一些简单的recipes，你可以在无需编码的情况下进行搭建项目。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/IFTTT.png)

如果你没有IFTTT账号, 请点击 [这里](https://ifttt.com/join) 来注册.

如果你已经有IFTTT账号,请点击 [这里](https://ifttt.com/recipes/search?q=seeed) 与Seeed连接，或在IFTTT网站上搜索Seeed。 在那里，您会发现Seeed的9种recipes教你如何使用IFTTT。
![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/IFTTT%20recipes.png)

什么是DoButton？ DoButton是IFTTT的应用程序之一，它使您可以轻松创建自己的个性化按钮，非常适合构建IoT项目并通过智能手机进行控制，下面是两个示例，介绍如何使用IFTTT和DoButton来制作有用的应用程序。

### 应用:

|**IFTTT**|**DoButton**|
|:---|:---|
|[**Recipe**][DIY自动花园灌溉](http://www.seeed.cc/project_detail.html?id=1080)|[**Recipe**][当你不在家时，如何喂养宠物](http://www.seeed.cc/project_detail.html?id=1066)|
|[**Video**][如何使用ITFFF](https://vimeo.com/148590984)|[**Video**][如何使用DoButton](https://vimeo.com/146988454)|


## 高级用户指南
----
感觉这些例子太简单了？ 想做更复杂的项目？ 以下是高级用户使用Wio Link的最佳指南。 通过这些指南，高级用户能够了解有关Wio Link的更多详细信息，部署私有服务器，甚至为Wio Link编写模块驱动程序。

[![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/GOTO_ADVANCED_GUIDE.png)](https://github.com/Seeed-Studio/Wio_Link/wiki)

指南涵盖：

- API参考
- 服务器部署指南
- 高级用户指南
- 如何为Wio Link编写模块驱动程序？

## 高级教程
如果您用智能手机成功控制了Grove，并希望尝试更困难而不是复杂的事情，为什么不学习本教程后，您将能够构建一个温湿度监测器，并点亮Grove RGB LED灯条。

在开始之前，请检查您是否有以下设备。

|RGB Led strip|Grove-Temperature and Humidity Sensor|
|:---:|:---:|
|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/RGB%20LED%20Strip.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/grove-T%26H%20sensor.jpg)|
|[Get One Now](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4ca0cf3fmMpgwS&id=531757655434)|[Get One Now](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.2b02e9a0iCClum&id=520506479798)|


- 步骤1：将LED条插入Wio Link，然后将相同的模块拖至应用程序中的Wio Link。更新固件。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/advance%20tutorial%20video.png)

- 步骤2：将Grove温度和湿度传感器插入Wio Link，然后将相同的模块拖到应用程序中的Wio Link中。更新固件。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/advance%20tutorial%20video%202.png)

- 步骤3：通过查看API，并查看您家中的温湿度。 下图显示了用手握住握温湿度传感器之前和之后的温度变化。 温度提高了1摄氏度。 尝试看看改变房子的温度和湿度。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Celsuis%202%20pics.png)

- 步骤4：通过改变RGB值控制LED条的光线。

因为Wio Link App读取十六进制RGB值，所以RGB值需要转换为十六进制值。 在这里我想推荐网站[RGB t0 Hex](http://www.rgbtohex.net/)。 只要输入3个RGB元素（红，绿，蓝）的RGB值，网站就会将RGB值转换为十六进制。 比如输入255，0，0

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/RGB%20255%200%200.png)

- 然后你会得到十六进制值为FF0000，颜色为红色。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/FF0000.png)

!!!Note
    * 您输入的RGB值应为0到255之间的任何数字（包括0和255）

然后输入您要的Leds数量和应用程序中的十六进制值，这里我的Led Strip有30个Leds，所以我选择了30个。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio%20link%20control%20led%20strip.png)

您还可以指定条纹的哪一部分被点亮，并给它一个特殊的颜色，或甚至像彩虹模式中的闪烁。 很多惊人的功能正在等待你的探索！


## 资源下载
---

**硬件**

- [EAGLE Schematic files](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/Wio_Link_SCH_v1.0.rar)
- [EAGLE PCB file](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/202000877%20Wio%20Link%20v1.0%20sch%20pcb.zip)
- [Schematic files(pdf)](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/Wio%20Link%20v1.0%20sch.pdf)

**软件**

- [Source Code on Github.](https://github.com/Seeed-Studio/Wio_Link)

**其他文档**

- [API Reference](http://seeed-studio.github.io/Wio_Link/)
- [Server Deployment Guide](https://github.com/Seeed-Studio/Wio_Link/wiki/Server%20Deployment%20Guide)
- [How to write module driver for Wio Link](https://github.com/Seeed-Studio/Wio_Link/wiki/How-to-write-module-driver-for-Wio-Link%3F)
- [iot.seeed.cc](http://iot.seeed.cc/index.html) 获取更多信息。


## FAQ
----

以下是我们从新用户那里得到的一些问题。 如果您在使用Wio Link或其他Wio产品时遇到任何其他问题，欢迎来到有许多专业用户的[Community of Wio](http://www.seeed.cc/topics.html?t=Wio) 。


**1. 电源和电池 - Wio Link是否配有Lipo电池？**

不，每个Wio Link都配有微型USB电缆进行充电，或者您可以从我们的淘宝购买3.7V的Lipo电池。 以下是您的参考资料：
- 最大输入电压：4.2V;
- 最大充电电流：500mA。

**2.电源和电池 - 我可以使用带有Wio Link的电源适配器吗？哪一种？**

有两种方式为Wio Link供电，Micro USB电缆或3.7V Lipo电池供电。如果Micro USB和电池都插入电路板，USB电源将为电池充电。您可以使用可以连接Micro USB电缆和5Vdc输出的各种电源适配器。电池座是JST-2.0连接器。


**3.功耗 - Wio Link的功耗是多少？**

平均功耗为70mA。使用700mAh的电池，可以保持活动长达10小时。有低功耗的API可以让Wio Link从工作模式更改为休眠模式。将平均功耗降至150uA以下。


**4.Grove电缆 - Groves是否在所有套件中配备了电缆？**

是的，我们每个Grove模块都装有一个标准的4针Grove电缆。


**5.RESTful API - 是否需要互联网连接，或者可以通过本地网络进行连接？**

我们将REST API服务器部署到iot.seeed.cc，以便您可以从iot.seeed.cc访问传感器和执行器。目前，Wio Link必须连接到互联网。此外，我们将开源服务器，以便用户以非常简单的Docker方式部署本地服务器。通过部署本地服务器，他们可以在本地使用编译和数据交换服务，而不用上线。

**6.支持的编程方法 - 是否支持其他编程方法，如Arduino IDE？**

Wio Link可以使用Arduino IDE进行编程，在这种情况下，它将失去RESTful API的功能。

如果您想与Arduino或RPI进行互动，您可以开发第三方模块驱动程序，参考[指南](https://github.com/Seeed-Studio/Wio_Link/wiki/How-to-write-module-driver-for-Wio-Link%3F)和[驱动](https://github.com/Seeed-Studio/Wio_Link/tree/master/grove_drivers/grove_example)。

**7. 支持的平台 - 支持Windows平台？**

现在，Wio Link提供Android和iOS两款移动应用。我们将所有服务都作为RESTful API，如果遵循API文档，第三方开发人员可以构建自己的应用程序，例如Mobile Apps或Desktop Apps。
Wio Link是一个社区友好的项目。它不会局限于某个平台。我们真的希望人们可以和他们一起玩Wio Link。


**8. 可以使用Wio Link与现有系统进行交互吗？**

是. 首先，将Wio Link的任何GPIO连接到其他系统，在移动应用中选择“Generic Digital Input”或“Generic Digital Output” Grove模块，然后通过RESTful API调用向现有系统发送/读取信号。其次，将Wio Link的模拟端口连接到其他系统，在移动应用程序中选择“Generic Analog Input” Grove模块，然后读取模拟测量，以获得现有系统的一些物理量。第三，为了与现有系统进行交互更灵活，您可以开发第三方模块驱动程序，通过I2C或UART接口将请求从互联网发送到现有系统。我们有关于如何开发第三方模块驱动程序的[指导](https://github.com/Seeed-Studio/Wio_Link#how-to-write-module-driver-for-wio-link)，我们也可以提供为您的开发提供技术支持。


**9. Wio Link支持多少个Groves？**

现在有150多种即插即用的Groves模块，其中Wio Link支持36个。

### Grove 模块支持列表

|描述                                        |接口 |
|--------------------------------------------|----------|
|    Grove - Moisture Sensor                 |模拟    |
|    Grove - Light Sensor                    |模拟    |
|    Grove - Temperature Sensor              |模拟    |
|    Grove - Rotary Angle Sensor             |模拟    |
|    Grove - Light Sensor(P)                 |模拟    |
|    Grove - Sound Sensor                    |模拟    |
|    Grove - Electricity Sensor              |模拟    |
|    Grove - Slide Potentiometer             |模拟    |
|    Grove - 80cm Infrared Proximity Sensor  |模拟    |
|    Grove - UV Sensor                       |模拟    |
|    Grove - Rotary Angle Sensor(P)          |模拟    |
|    Grove - Loudness Sensor                 |模拟    |
|    Grove - Luminance Sensor                |模拟    |
|    Grove - Air quality sensor v1.3         |模拟    |
|    Grove - Button                          |数字   |
|    Grove - Switch(P)                       |数字  |
|    Grove - Collision Sensor                |数字  |
|    Grove - Line Finder                     |数字  |
|    Grove - Water Sensor                    |数字  |
|    Grove - PIR Motion Sensor               |数字  |
|    Grove - Tilt Switch                     |数字  |
|    Grove - Touch Sensor                    |数字  |
|    Grove - Magnetic Switch                 |数字  |
|    Grove - Hall Sensor                     |数字  |
|    Grove - Flame Sensor                    |数字  |
|    Grove - Button(P)                       |数字  |
|    Grove - Electromagnet                   |数字  |
|    Grove - Water Atomization v1.0          |数字  |
|    Grove - Solid State Relay               |数字  |
|    Grove - Relay                           |数字  |
|    Grove - MOSFET                          |数字  |
|    Grove - 2-Coil Latching Relay           |数字  |
|    Grove - Dry-Reed Relay                  |数字  |
|    Grove - Variable Color LED              |数字  |
|    Grove - Purple LED (3mm)                |数字  |
|    Grove - LED String Light                |数字  |
|    Grove - Red LED                         |数字  |
|    Grove - Green LED                       |数字  |
|    Grove - White LED                       |数字  |
|    Grove - Blue LED                        |数字  |
|    Grove - Multi Color Flash LED (5mm)     |数字  |
|    Grove - Vibration Motor                 |数字  |
|    Grove - EL Driver                       |数字  |
|    Grove - Buzzer                          |数字  |
|    Grove - Speaker                         |数字  |
|    Grove - 3-Axis Digital Compass          |I2C       |
|Grove - 3-Axis Digital Accelerometer(±1.5g) |I2C       |
|    Grove - 3-Axis Digital Gyro             |I2C       |
|    Grove - Barometer Sensor (BMP180)       |I2C       |
|    Grove - Gesture                         |I2C       |
|    Grove - Multichannel Gas Sensor         |I2C       |
|    Grove - I2C ADC                         |I2C       |
|    Grove - OLED Display 1.12''             |I2C       |
|    Grove - OLED Display 0.96''             |I2C       |
|    Grove - I2C Motor Driver                |I2C       |
|    Grove - I2C FM Receiver                 |I2C       |
|    Grove - Barometer(BMP280)               |I2C       |
|Grove - Temp&Humi&Barometer Sensor(BME280)  |I2C       |
|    Grove - Ultrasonic Ranger               |数字   |
|    Grove - Infrared Receiver               |数字  |
|    Grove - Temperature&Humidity Sensor Pro |数字  |
|    Grove - Infrared Emitter                |数字  |
|    Grove - Infrared Reflective Sensor      |Others    |
|    Grove - Digital Light Sensor            |I2C       |
|    Grove - IR Distance Interrupter         |数字  |
|    Grove - Recorder                        |数字  |
|    Grove - LED Bar v2.0                    |UART      |
|    Grove - 4-Digit Display                 |UART      |
|    Grove - Servo                           |数字  |
|    Grove - CO2 Sensor                      |UART      |
