---
title: BeagleBone Green
category: BeagleBone
bzurl: https://www.seeedstudio.com/SeeedStudio-BeagleBone-Green-p-2504.html
oldwikiname: BeagleBone_Green
prodimagename: cover.jpg
surveyurl: https://www.research.net/r/seeed_bbg
sku: 102010027
---

![enter image description here](https://github.com/SeeedDocument/BeagleBone_Green/blob/master/images/cover.jpg?raw=true)

SeeedStudio BeagleBone Green（BBG）是专为开发者和业余爱好者设计的，低成本，开源，社区支持的开发平台。 这是[BeagleBoard.org](http://beagleboard.org/)和Seeed Studio的共同努力。 它基于[BeagleBone Black](http://beagleboard.org/black) 的经典开源硬件设计，并开发成这种差异化版本。 BBG包括两个Grove连接器，使其更容易连接到大量Grove传感器系列。 移除板载HDMI为这些Grove连接器腾出空间。

在不到10秒内启动Linux，只需一根USB电缆即可在5分钟内开始开发。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3ff19e11ynmckW&id=521388762505)



## 产品特性
------

* **和BeagleBone Black完全兼容**
* **处理器: AM335x 1GHz ARMR Cortex-A8**
    * 512MB DDR3 RAM
    * 4GB 8-bit eMMC 板载 flash 存储
    * 3D 图形加速器
    * NEON 浮点加速器
    * 2x PRU 32-bit 微处理器
* **接口**
    * USB client可供电和通信
    * USB host
    * Ethernet
    * 2x 46 pin 接头
    * 2x Grove connectors (I2C and UART)
* **系统兼容**
    * Debian
    * Android
    * Ubuntu
    * Cloud9 IDE on Node.js w/ BoneScript library
    * 即将兼容更多

## 规格参数
------

|项目|内容|
|----|------|
|处理器|	AM335x 1GHz ARMR Cortex-A8|
|RAM|	512MB DDR3|
|板载Flash 存储	|4GB eMMC|
|CPU Supports	|NEON floating-point & 3D graphics accelerator|
|Micro USB	Supports |powering & communications|
|USB |Host	1|
|Grove Connectors	|2 (One I2C and One UART) |
|GPIO	|2 x 46 pin headers|
|Ethernet	|1|
|工作温度	|0 ~ 75°|

## 创意应用
---
* 物联网
* 智能家居
* 工业应用
* 自动化过程控制
* 机器人交互
* 传感器节点

这里有一些有趣的项目可以供您参考。

|Home Center|Retro Lamp|Drive a Motor|
|---------------|-----|--------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project2.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project3.jpg)|
|[MAKE IT NOW!](http://www.instructables.com/id/Home-Control-Center-Using-BeagleBone-Green-Wireles/)|[MAKE IT NOW!](http://www.instructables.com/id/DIY-a-Retro-Wooden-Lamp-with-BBG/)|[MAKE IT NOW!](http://www.instructables.com/id/A-BeagleBone-Tutorial-Getting-Started-With-Motor-B/)|

|BBG Acrylic Case|GPIO Control|Smart Light|
|---------------|-----|--------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project4.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project5.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/project6.png)|
|[MAKE IT NOW!](http://www.instructables.com/id/5-Design-of-Laser-Cut-Cases-for-5-Popular-Platform/)|[MAKE IT NOW!](http://www.seeed.cc/How-to-use-the-Grove-UART-port-as-a-GPIO-on-BBG-p-365.html)|[MAKE IT NOW!](http://www.seeed.cc/Smart-Light-Demo-with-BBG-%26amp%3B-BBG-Start-Kit(HA)-p-366.html)|


## 硬件概述
---
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/10201002703.jpg)


* **USB Host** - USB Host
* **DC Power and USB Client** - 为板子供电并且作为从机
* **LEDs**
    * **D2** 在 boot 中配置为心跳闪烁
    * **D3** 在 boot 中配置为读写SD卡数据时亮起
    * **D4** 在 boot 中配置为当 CPU 活动时亮起
    * **D5** 在 boot 中配置为当eMMC 读写时亮起
* **Boot 按钮**
    * 当有SD卡插入时，系统将首先从SD卡启动，如果要从eMMC启动，请按此按钮，然后接通电源.
    * 当启动后就作为一个普通按钮, 连接到 **GPIO_72**
* **I2C Grove Interface** - 连接到 **I2C2**
* **Uart Grove Interface** - 连接到 **UART2**
* **Serial Debug** - 连接到 **UART0**, PIN1~PIN6: GND, NC, NC, RX, TX, NC, 请注意pin1 是指靠近USB 的管脚.

**管脚图**

每个数字 I/O pin 拥有8种不同模式可供选择，包括 GPIO.

**65 种不同可能的数字 I/Os**

!!!Note
    在 GPIO 模式下，每个数字 I/O 管脚都可以处理中断。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_IO.png)

**PWMs and Timers**

!!!Note
    高达8个数字 I/O 引脚可以被配置成脉冲宽度调制模式 (PWM) ，从而在无需CPU参与的情况下用于产生信号来控制电机或者产生模拟电平。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_TIMER.png)

**模拟输入**

!!!Note
    请确保在任何模拟引脚加的输入电压不高于1.8V。板卡上只有一个8通道的 12-bit 数模转化器，其中7个通道引出到接口。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_ANALOG.png)


**UART**

!!!Note
    有一个专用的连接头用于连接UART0脚并且连接到debug线缆。5个附加的串行口也连接到了扩展接口。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_UART.png)


**I2C**

!!!Note
    第一个I2C总线用于读取Cape附加板上的EEPROMS，为了不会影响该功能该总线不能用于其他数字I / O操作，，但您仍然可以使用它在可用地址中添加其他I2C设备。 第二个I2C总线可供您自由配置和使用。


![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_I2C.png)

**SPI**

!!!Note
    若是需要快速传输数据，您可以考虑使用SPI接口。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/PINMAP_SPI.png)

## 入门指南
------

!!!Note
    此章节是基于Windows 10 系统，其他操作系统的指南与此类似。

**步骤1.通过 USB 接口连接 BBG**

使用我们提供的Micro-USB电缆将您的BBG接入电脑。 这将同时为电路板供电并提供开发接口。 BBG将从板载2GB或4GB eMMC启动Linux。

BBG将作为闪存驱动器运行，为您提供文档和驱动程序的本地副本。 请注意，此接口可能不用于使用新映像重新配置microSD卡，但可用于使用uEnv.txt文件更新引导参数。

您将看到PWR LED稳定点亮。 在10秒钟内，您应该看到另一个LED以其默认配置闪烁。

* **D2** 在 boot 中配置为心跳闪烁
* **D3** 在 boot 中配置为读写SD卡数据时亮起
* **D4** 在 boot 中配置为当 CPU 活动时亮起
* **D5** 在 boot 中配置为当eMMC 读写时亮起

**步骤2. 安装驱动**

为您的操作系统安装驱动程序，让您的Beaglebone可以通过USB访问网络。 其他驱动程序可让您访问的主板。

|操作系统|	USB 驱动 |	备注 |
|---------------------|---------|------------|
|Windows (64-bit) |	[64-bit installer](http://beagleboard.org/static/Drivers/Windows/BONE_D64.exe)	 | |
|Windows (32-bit) |	[32-bit installer](http://beagleboard.org/static/Drivers/Windows/BONE_DRV.exe)||
|Mac OS X|[Network](http://beagleboard.org/static/Drivers/MacOSX/RNDIS/HoRNDIS.pkg) and [Serial](http://beagleboard.org/static/Drivers/MacOSX/FTDI/EnergiaFTDIDrivers2.2.18.pkg) |注意Network和Serial是两个不同的驱动，您都需要安装 |
|Linux|[mkudevrule.sh](http://beagleboard.org/static/Drivers/Linux/FTDI/mkudevrule.sh)|驱动程序安装不是必需的，但是您可能会发现几个udev规则很有帮助。.|

!!!Note
    对于Windows系统，请注意以下几点:

    * Windows 驱动认证警告可能会弹出两到三次，点击 "忽略", "安装" 或者 "运行"
    * 点击下面链接查看您需要安装64位或者32位 [点击这里](https://support.microsoft.com/kb/827218)
    *  在非最新版本的Windows系统下,您在安装过程中可能会遇到错误 (0xc000007b)。在这种情况下，请点击 [安装](https://www.microsoft.com/en-us/download/confirmation.aspx?id=13523) 再重试一次。
    * 您可能需要重启电脑。
    * 该驱动在Windows 10 下测试通过。

!!!Note
    Additional FTDI USB to serial/JTAG information and drivers are available from [https://www.ftdichip.com/Drivers/VCP.htm](https://www.ftdichip.com/Drivers/VCP.htm).

!!!Note
    Additional USB to virtual Ethernet information and drivers are available from [https://www.linux-usb.org/gadget/](https://www.linux-usb.org/gadget/) and [https://joshuawise.com/horndis](https://joshuawise.com/horndis).


**步骤3. 使用浏览器浏览您的 Beagle**

使用Chrome或Firefox（Internet Explorer将不起作用），浏览到您的电路板上运行的Web服务器。 它将加载一个演示文稿，向您显示电路板的功能。 使用键盘上的箭头键浏览演示文稿。
使用Chrome或Firefox（Internet Explorer将不起作用），浏览到您的电路板上运行的Web服务器。 它将加载一个演示文稿，向您展示电路板的功能。 使用键盘上的箭头键导航演示文稿。

点击 [http://192.168.7.2](http://192.168.7.2) 来加载您的 BBG.
较旧的软件映像要求您使用BEAGLE_BONE驱动器启动网络。 使用最新的软件映像，不再需要该步骤。

[![Click to view larger image](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/launch.png)](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/launch.png)

**步骤4. Cloud9 IDE**

要开始编辑您的主板上的程序，可以单击下面链接来开启 Cloud9 IDE

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/cloud9.png)](http://192.168.7.2:3000/ide.html)



## 更新到最新的软件
-----
您需要将主板更新到最新的软件以保持更好的性能，这里我们将向您展示如何逐步实现。

**步骤1. 下载最新的固件**


首先，您必须在这里下载合适的固件。


[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/down_latest_image.png)](http://beagleboard.org/latest-images)

!!!Note
    由于软件大小，此下载可能需要约30分钟或更长时间。

您下载的文件将有一个**img.xz **扩展名。 这是用于SD卡烧录的固件。


**步骤2. 安装SD卡烧录程序**

下载并且安装  [Image Writer for Windows](https://sourceforge.net/projects/win32diskimager/files/latest/download). 请确保您下载的是对应自己系统的版本。

**步骤3. 将您的固件写入SD卡**

首先需要通过一个SD适配器将microSD卡连接到电脑。 然后使用软件Image Write for Windows将解压缩的固件写入SD卡。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/win32_disk_image.png)

点击 **Write** 按钮,然后写入程序将开启。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/win32_disk_image_process.png)

!!!Note
    * 您可能会看到有关损坏SD卡的警告，请您放心选择接受。
    * 此时您不应将 BeagleBone 链接到电脑。
    * 整个过程大概会持续10分钟。


**步骤4. 从SD卡启动您的系统**

关闭电源，插入SD卡，然后打开电源，系统就将从SD卡启动。

!!!Note
  - 如果您不需要将固件写入您的板载eMMC，则无需阅读本章最后一章。 否则请继续。


如果您希望将固件写入您的板载eMMC，则需要加载进板卡并修改文件。


在 **/boot/uEnv.txt** 中找到:

    ##enable BBB: eMMC Flasher:
    #cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh
修改为:

    ##enable BBB: eMMC Flasher:
    cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh

然后您将看到4个LED灯会如下图闪烁。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/flashing.gif)

!!!Note
  - 如果没有看到上图所示的的灯迹，请按RESET按钮重置电路板。


  当闪烁完成时，所有4个用户指示灯 LED将关闭。 最新的Debian系统在完成固件加载后自动关闭电路板。这个过程最多可能会持续** 10分钟**。 关闭电源，取出SD卡，再次接通电源即可完成。

## Grove for BBG
------

Grove 是一个模块，是一个具有标准协议的连接器系统。 Grove采用积木式组装电子技术。 与基于跳线或焊接的系统相比，具有连接方便、结构简单、易于上手、可快速入门学习等诸多优点。

下表罗列了适用于 BBG 的Grove 模块.

|SKU        |名称|接口|购买链接|
|-----------|-----|-----|----------|
|101020054  |Grove - 3-Axis Digital Accelerometer(+16g)     |	I2C| [购买链接](http://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer%28%C2%B116g%29-p-1156.html)|
|101020071  |Grove - 3-Axis Digital Accelerometer(+400g)    |	I2C| [购买链接](http://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer%28%C2%B1400g%29-p-1897.html)|
|101020034  |Grove - 3-Axis Digital Compass                 |	I2C| [购买链接](http://www.seeedstudio.com/Grove-3-Axis-Digital-Compass-p-759.html)|
|101020050  |Grove - 3-Axis Digital Gyro                    |	Analog| [购买链接](http://www.seeedstudio.com/Grove-3-Axis-Digital-Gyro-p-750.html)|
|101020081	|Grove - 6-Axis Accelerometer&Compass v2.0      |	I2C| [购买链接](http://www.seeedstudio.com/Grove-6-Axis-Accelerometer&Compass-v2.0-p-2476.html)|
|101020072	|Grove - Barometer Sensor(BMP180)              |	I2C| [购买链接](http://www.seeedstudio.com/Grove-Barometer-Sensor-%28BMP180%29-p-1840.html)|
|104030010	|Grove - Blue LED                               |	I/O| [购买链接](http://www.seeedstudio.com/Grove-Blue-LED-p-1139.html)|
|101020003	|Grove - Button	                                |I/O| [购买链接](http://www.seeedstudio.com/Grove-Button-p-766.html)|
|111020000	|Grove - Button(P)	                            |I/O| [购买链接](http://www.seeedstudio.com/Grove-Button%28P%29-p-1243.html)|
|107020000	|Grove - Buzzer	                                |I/O| [购买链接](http://www.seeedstudio.com/Grove-Buzzer-p-768.html)|
|104030006	|Grove - Chainable RGB LED	                    |I2C| [购买链接](http://www.seeedstudio.com/Grove-Chainable-RGB-LED-p-850.html)|
|101020030	|Grove - Digital Light Sensor	                |I2C| [购买链接](http://www.seeedstudio.com/Grove-Digital-Light-Sensor-p-1281.html)|
|103020024	|Grove - Finger-clip Heart Rate Sensor	        |I2C| [购买链接](http://www.seeedstudio.com/Grove-Finger-clip-Heart-Rate-Sensor-p-2425.html)|
|101020082	|Grove - Finger-clip Heart Rate Sensor with shell	|I2C|[购买链接](http://www.seeedstudio.com/Grove-Finger-clip-Heart-Rate-Sensor-with-shell-p-2420.html)|
|113020003	|Grove - GPS	                        |UART| [购买链接](http://www.seeedstudio.com/Grove-GPS-p-959.html)|
|104030007	|Grove - Green LED	|I/O| [购买链接](http://www.seeedstudio.com/Grove-Green-LED-p-1144.html)|
|103020013	|Grove - I2C ADC	|I2C| [购买链接](http://www.seeedstudio.com/Grove-Green-LED-p-1144.html)|
|103020006	|Grove - I2C Hub	|I2C| [购买链接](http://www.seeedstudio.com/Grove-I2C-Hub-p-851.html)|
|101020079	|Grove - IMU 10DOF	|I2C| [购买链接](http://www.seeedstudio.com/Grove-IMU-10DOF-p-2386.html)|
|101020080	|Grove - IMU 9DOF v2.0	|I2C| [购买链接](http://www.seeedstudio.com/Grove-IMU-9DOF-v2.0-p-2400.html)|
|101020040	|Grove - IR Distance Interrupter	|I/O| [购买链接](http://www.seeedstudio.com/Grove-IR-Distance-Interrupter-p-1278.html)|
|104030011	|Grove - OLED Display 0.96''	|I2C| [购买链接](http://www.seeedstudio.com/Grove-OLED-Display-1.12%22-p-824.html)|
|104030008	|Grove - OLED Display 1.12''	|I2C| [购买链接](http://www.seeedstudio.com/Grove-OLED-Display-0.96%22-p-781.html)|
|104030005	|Grove - Red LED	|I/O| [购买链接](http://www.seeedstudio.com/Grove-Red-LED-p-1142.html)|
|103020005	|Grove - Relay	|I/O| [购买链接](http://www.seeedstudio.com/Grove-Relay-p-769.html)|
|316010005	|Grove - Servo	|I/O| [购买链接](http://www.seeedstudio.com/Grove-Servo-p-1241.html)|
|101020023	|Grove - Sound Sensor	|Analog| [购买链接](http://www.seeedstudio.com/Grove-Sound-Sensor-p-752.html)|
|101020004	|Grove - Switch(P)	|I/O| [购买链接](http://www.seeedstudio.com/Grove-Switch%28P%29-p-1252.html)|
|101020015	|Grove - Temperature Sensor	|Analog| [购买链接](http://www.seeedstudio.com/Grove-Temperature-Sensor-p-774.html)|
|101020019	|Grove - Temperature&Humidity Sensor Pro	|Analog| [购买链接](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11pBcK4M&id=534770660296)|

## Cape for BBG
-------

在您开始自己的项目时，可能需要一些扩展板。 BBG 已经有许多扩展板，包括液晶显示器，电机驱动器以及HDMI扩展等。以下是其中的一些推荐。

|Grove Cape| Motor Bridge Cape|HDMI Cape|
|------------|----------------|----------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product2.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product3.jpg)|
|[GET ONE NOW!](http://www.seeedstudio.com/Grove-Cape-for-BeagleBone-Series-p-1718.html)|[GET ONE NOW!](http://www.seeedstudio.com/Motor-Bridge-Cape-p-2569.html)|[GET ONE NOW!](http://www.seeedstudio.com/SeeedStudio-BeagleBone-Green-HDMI-Cape-p-2570.html)|

|Grove Cape| 5 Inch LCD|7 Inch LCD|
|------------|----------------|----------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product4.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product5.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green/master/images/product6.jpg)|
|[GET ONE NOW!](http://www.seeedstudio.com/Grove-Base-Cape-for-Beaglebone-v2.0-p-2644.html)|[GET ONE NOW!](http://www.seeedstudio.com/5-Inch-BeagleBone-Green-LCD-Cape-with-Resistive-Touch-p-2642.html)|[GET ONE NOW!](http://www.seeedstudio.com/7-Inch-BeagleBone-Green-LCD-Cape-with-Resistive-Touch-p-2643.html)|

## FAQ
---
1. BBG 1 和 BBG 2 有何不同?
   ![](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/bbg12.png)
我们在2016年更新了Beaglebone Green的eMMC。因此，以前的BBG1固件在BBG2上无法使用，但新的固件在BBG1和BBG2可以正常使用。
    
## 参考
---
有很多参考资料可以帮助您获得有关 BBG 的更多信息。

* [BeagleBoard Main Page](http://beagleboard.org/)
* [BeagleBone Green info at BeagleBoard page](http://beagleboard.org/green)
* [BeagleBoard Getting Started](http://beagleboard.org/getting-started)
* [Troubleshooting](http://beagleboard.org/getting-started#troubleshooting)
* [Hardware documentation](http://beagleboard.org/getting-started#hardware)
* [Projects of BeagleBoard](http://beagleboard.org/project)
* [CE certification of BBG](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/resources/CE.zip)
* [FCC certification of BBG](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/resources/FCC.zip)

## 资料下载
---

* [BEAGLEBONE_GREEN SRM(v1a)(pdf)](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/resources/BBG_SRM_V1a_20151009.pdf)
* [BEAGLEBONE_GREEN Schematic(pdf)](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/resources/BEAGLEBONE_GREEN_V1.pdf)
* [BEAGLEBONE_GREEN Schematic(OrCAD)](https://github.com/SeeedDocument/BeagleBone_Green/raw/master/resources/BEAGLEBONE_GREEN_V1_166%28sch%29.rar)
* [BEAGLEBONE_GREEN PCB(OrCAD)](https://github.com/SeeedDocument/BeagleBone_Green/blob/master/resources/BeagleBone_Green_v1.166%28board%29.rar)
