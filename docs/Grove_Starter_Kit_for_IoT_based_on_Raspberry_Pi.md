---
name: Grove Starter Kit for IoT based on Raspberry Pi
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/Microsoft-IoT-Grove-Kit-(Azure-Certified)-p-2694.html
prodimagename: cover.jpg
other: 
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Starter_Kit_for_IoT_based_on_Raspberry_Pi
sku: 110060482
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/cover.jpg)

对于很多开发者来说，在 Raspberry Pi 上搭建 IOT 物联网项目并非易事，因为这需要涉及到大量硬件连接和软件编程。Seeed 和 Microsoft 通过合作推出 Microsoft IoT Grove Kit，使得这些艰难的挑战变得轻松。

套件包含 GrovePi+ 模块，该模块完全可以兼容 RaspberryPi 3 和 Raspberry Pi 2 (两者都是采用 Windows 10 IoT Core)，有了简便易用的 Grove 系统，开发者可以非常顺利的通过 GrovePi+ 开发板将 15 个 Grove 模块与 Raspberry Pi 连接在一起!

除了高性能传感器和执行器，该套件还包含一个 5 英寸 HDMI 显示屏 和一个带背光的 RGB LCD。Microsoft IoT Grove Kit 是一款功能强大的探索物联网世界的平台。

请注意此套件不含 Raspberry Pi 开发板，如需要可点击 [这里](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.5fe4f4a9zmh4JI&id=528322046763) 购买

!!!Note
    GrovePi+ 和一些代码是由 Dexter Industry 设计的。点击获取更多关于 [Dexter Industry](http://www.dexterindustries.com/) 的信息。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.26.f4adee36cO5BN&id=539380678772)

## 产品特性
* GrovePi+ 容易上手，并且兼容 Raspberry Pi B/B+/A+/2/3
* Grove 模块即插即用，可快速编程

## 产品清单

| SKU | 产品名称 | 数量 | 传送门 |
|------|--------------|------|-------|
|103010002 | GrovePi+ | 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3004ce6f5knzci&id=45506190895) |
|104990243| 5 Inch HDMI Display with USB TouchScreen | 1 | [点击购买](https://www.seeedstudio.com/5-Inch-HDMI-Display-with-USB-TouchScreen-p-2638.html) |
|103020005| Grove - Relay | 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.3c382cbd4GDvEa&id=45670971061) |
|101020011| Grove - Temp&Humi Sensor| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.c4792d6wVYWB3&id=520506479798) |
|101020010| Grove - Ultrasonic Ranger | 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.66278853uoa1pQ&id=45550924107) |
|104020006| Grove LED Bar v2.0 | 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.58bb6074ME86QD&id=520900900588) |
|101020048| Grove - Rotary Angle Sensor(P)| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.190e4690lMhRlT&id=45554377762) |
|107020000| Grove - Buzzer| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.32c4601auJZg7Y&id=520245748676) |
|101020023| Grove - Sound Sensor| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.33bdf4832D4Xi3&id=45507318433) |
|101020014 | Grove - Light Sensor v1.2 | 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.79973f16lJU95z&id=544373791068) |
|101020003| Grove - Button| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.2357f100AARkz&id=531838497696) |
|104030001| Grove - LCD RGB Backlight| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.40f24af455dQTR&id=45475311124) |
|109990056| HDMI Cable| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.5fb3e8d3FHweqm&id=529727851874) |
|321010007| Micro USB Cable - 48cm| 1 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.43f476a6gAfyDS&id=521385344999) |


## GrovePi+ 硬件连接

**1.1	将 GrovePi+ 连接至 Raspberry Pi**

首先将 GrovePi+ 与 Raspberry Pi 组装在一起。GrovePi+ 如下图所示堆叠在 Raspberry Pi 上。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/1_1_1.png)

确保两者的引脚和孔正确对齐

**Raspberry Pi 上电**

要为 GrovePi+ 和 Raspberry Pi 供电，您可以使用 Raspberry Pi 上的 micro USB 电源端口。请记住使用能够在 5V 供电 2A 的电源适配器。如果您想在独立配置下运行 GrovePi+，那么您需要一个 USB 移动电源(充电宝)。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/1_2_1.png)


## 为 Raspberry Pi 安装 GrovePi+ C# library

GrovePi+ 可以用 C# 进行编程，但首先应该安装 GrovePi+ 的 Windows 10 IoT C# 驱动库。有两种方法 : 安装 NuGet package 和使用 Dexter 提供的 GrovePi C# 库代码。

**安装 NuGet package**

当前版本的 GrovePi+ NuGet package 可用。要安装适用于 Windows IoT 的 GrovePi+，请遵循以下步骤。

**步骤 1**

从 Tools 中选择 **Library Package Manager**，然后单击 **Package Manager Console**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_1_1.png)

**Package Manager Console window** 窗口显示

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_1_2.png)

**步骤 2**

在 Package Manager Console 中运行以下命令

    PM> Install-Package GrovePi+

更多详细信息请点击 [这里](https://www.nuget.org/packages/GrovePi/).


**使用 GrovePi C# 库代码**

如果您无法成功安装 GrovePi+ NuGet package，请单击 [这里](https://github.com/DexterInd/GrovePi/tree/master/Software/CSharp) 下载库代码。

**步骤 1**

将两个 C# 库项目 “GrovePi+” 和 “Driver” 移动到您的项目所在的文件夹中。并将其添加到 **Solution Explorer** 中。例如，右键单击 **Solution Explorer** 中的 “GrovePiExamples ”，**Add | Existing Project**，如下所示。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_2_1.png)

把 “GrovePi+” 和 “Driver” 添加到 **Solution Explorer**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_2_2.png)


**步骤 2**

将 C# library 设置为参考项目。右键单击 **References**，然后单击 **Add References**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_2_3.png)

点击 **Projects | Solution**， 勾选下面红框中的复选框，然后点击 **OK**.
**
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/2_2_4.png)

现在您已经成功安装了 GrovePi+ C# library。

传感器都可以通过 DeviceFactory 获得。

**示例**

下面是一些使用库的示例 :   

 * **测量距离**

将 Ultrasonic sensor 连接到 **D2**

    var distance = DeviceFactory.Build.UltraSonicSensor(Pin.DigitalPin2).MeasureInCentimeters();

* **在屏幕上显示 Hello World**

       DeviceFactory.Build.RgbLcdDisplay().SetText("Hello World").SetBacklightRgb(0, 255, 255);


* **鸣笛**

将 buzzer 连接到 **D2**

    DeviceFactory.Build.Buzzer(Pin.DigitalPin2).ChangeState(SensorStatus.On);


## 在 Rpi3 上运行 Win10 IoT 示例

这里我们有一个示例项目列表，展示了用 Raspberry Pi 开始一个项目是多么容易。这些 Raspberry Pi 项目将使用方便的 Grove 系列传感器与强大的 Raspberry Pi 结合在一起。

您可以点击 [这里](https://github.com/Seeed-Studio/GrovePiExamples_win10) 下载适用于 win10 的 GrovePi+ Example 代码。您需要点击右侧的绿色按钮 **Clone or download**，然后选择 **Download ZIP**，然后需要选择位置释放压缩文件。使用 Visual Studio 2015 打开 GrovePiExamples(win10).sln，可以看到在 Solution Explorer 中有 12 个项目，如下图所示。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/3_0_1.png)

首先建立起 **GrovePi+** 项目，这是因为其他项目都是建立在它的基础上的。

示例 : **Hello World from RGB LCD**

这个例子是您使用 GrovePi+ 的第一个项目。GrovePi+ Starter Kit 中提供了该项目中会使用到的所有部件。掌握了这个项目，就可以进行更复杂的项目，例如将显示器或其他传感器连接到 Raspberry Pi。

- **步骤 1 :** 将 HelloWorld(LCD) 设置为 StartUp Project。
- **步骤 2 :** 硬件连接。

通过 Grove 线缆将 RGB LCD 连接到 **I2C-1** 端口并给 Raspberry Pi 上电。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/3_1_1.png)

- **步骤 3 :**  配置您的 app。

1)	在 Visual Studio 中打开 app，在 toolbar 下拉菜单中设置 **architecture**，选择 **ARM**。

2)	在 Visual Studio 的 toolbar 中，单击 **Local Machine** 下拉列表并选择 **Remote Machine**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/3_1_2.png)

3)	此时 Visual Studio 将显示 Remote Connections 对话框。如果您以前使用 [PowerShell](http://ms-iot.github.io/content/en-US/win10/samples/PowerShell.htm) 为您的设备设置了唯一名称，则可以在此输入(在本例中使用的是我自己的设备)。否则，请使用 Windows IoT Core 设备的 IP 地址。 输入设备 name/IP 后，在 Windows Authentication 选项中选择 **None**，然后单击 **Select**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Microsoft_IoT_Grove_Kit/master/images/3_1_3.png)

4)	您可以通过跳转到 project properties (在 Solution Explorer 中选择 Properties) 并选择左侧的 **Debug** 选项卡来验证或修改这些值。

当一切都设置好后，你可以在 Visual Studio 中按 **F5**。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

HelloWorld app 将在 Windows IoT 设备上配置并启动，您将在 Grove RGB LCD 中看到 HelloWorld。


**Grove - Rotary Angle Sensor**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1 :** 将 Grove - Rotary Angle Sensor 设置为 StartUp Project。
* **步骤 2 :** 硬件连接。
将 Grove Angle Sensor 连接到 **A0** 端口并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。
* **步骤 3 :** 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Rotary Angle Sensor app 将在 Windows IoT 设备上配置并启动，您将在 LCD 屏幕中看到 Grove - Rotary Angle Sensor 的值。


**Grove - LED Bar**


本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1 :** 将 Grove - LED Bar 设置为 StartUp Project。
* **步骤 2 :** 硬件连接。
将 Grove Led Bar 连接到 **D5** 端口。
* **步骤 3 :** 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - LED Bar app 将在 Windows IoT 设备上配置并启动，您将看到 Grove - LED Bar 被循环点亮。

**Grove - Light Sensor**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Grove - Light Sensor 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Light Sensor 连接到 **A2** 端口并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。
* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Light Sensor app 将在 Windows IoT 设备上配置并启动，您将在 LCD 屏幕中看到 Grove - Light Sensor 的值。

**Grove - Relay**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Grove - Relay 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Relay 连接到 **D2** 端口。
* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Relay app 将在 Windows IoT 设备上配置并启动，您看到 Grove - Relay 在每隔 1s 不停地启动和关闭。

**Grove - Sound Sensor**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Grove - Sound Sensor 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Sound Sensor 连接到 **A1** 端口并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。
* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Sound Sensor app 将在 Windows IoT 设备上配置并启动，您将在 LCD 屏幕中看到 Grove - Sound Sensor 的值。


**Grove - Temperature and Humidity Sensor**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Grove - Temperature and Humidity Sensor 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Temperature and Humidity Sensor 连接到 **D3**并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。
* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Temperature and Humidity Sensor app 将在 Windows IoT 设备上配置并启动，您将在 LCD 屏幕中看到温湿度的值。

**Grove - Ultrasonic Ranger**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Grove - Ultrasonic Ranger 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Ultrasonic Ranger 连接到 **D4** 端口并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。
* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Grove - Ultrasonic Ranger app 将在 Windows IoT 设备上配置并启动，您将在 LCD 屏幕中看到距离值。

**Home Weather Display**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 Home Weather Display 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
将 Grove - Temperature and Humidity Sensor 连接到 **D3** 端口，使用 Grove 线缆将 RGB LCD 连接到 **I2C** 端口.
* **步骤 3**: 配置您的 app，参阅示例 Blink 中的步骤 5。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

Home Weather Display app 将在 Windows IoT 设备上配置并启动，您将在 Grove - RGB LCD 中看到 温度值。


**All Modules in One Project**

本示例采用像 HelloWorld(LCD) 示例同样的设置。

* **步骤 1**: 将 All_in_One 设置为 StartUp Project。
* **步骤 2**: 硬件连接。
    * Grove - Relay > D2
    * Grove - Temp&Humi Sensor > D3
    * Grove - Ultrasonic Ranger > D4
    * Grove - LED Bar V2.0 > D5
    * Grove - Buzer > D6
    * Grove - Button > D7
    * Grove - Rotary Angle Sensor > A0
    * Grove - Sound Sensor > A1
    * Grove - Light Sensor > A2

如表所示地将 Grove 模块连接到 GrovePi+， 并通过 HDMI 线缆将 Raspberry Pi 连接到 LCD 屏幕。

* **步骤 3**: 配置您的 app，参阅示例 HelloWorld(LCD) 中的步骤 3。

当一切都设置好后，你可以在 Visual Studio 中按 F5。如果在安装过程中有漏装的软件包，Visual Studio 会提示您立即获取这些软件包。

All_in_One app 将在 Windows IoT 设备上配置并启动，各个模块各司其职。


## 资源下载

* **[库文件]** [GrovePi C# Library Code](https://github.com/DexterInd/GrovePi/tree/master/Software/CSharp)
* **[其他资源]** [Example Code](https://github.com/Seeed-Studio/GrovePiExamples_win10)
* **[其他资源]** [Windows Dev Center](https://dev.windows.com/en-us/iot)
