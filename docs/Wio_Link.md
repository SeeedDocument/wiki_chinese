---
name: Wio Link
category: Wio
bzurl: https://www.seeedstudio.com/Wio-Link-p-2604.html
oldwikiname: Wio_Link
prodimagename: WioLink.png
wikiurl: http://wiki.seeedstudio.com/cn/Wio_Link
sku: 102110037
---

构建物联网应用程序最困难的部分是什么 ? 有人说跳线部分经常使他感到挫败，也有人说，他最讨厌焊接部分，甚至有些人不喜欢面包板。也许您不是其中之一，但是电子工程，微控制器编程，网络编程，物联网协议处理等方面的知识依然是您通往一个成功的物联网项目路上的千难万阻。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/WioLink.png)

为了扫清这些阻碍，在 2015 年年底，Seeed Studio 在 [KickStarter](https://www.kickstarter.com/projects/seeed/wio-link-3-steps-5-minutes-build-your-iot-applicat?ref=nav_search) 上发布了 Wio Link，为开发物联网应用程序另辟蹊径。Wio Link 是一款基于 ESP8266 SoC 的开源 Wi-Fi 开发板，令它大放异彩的是它的相关平台，这些相关平台可以使得用户通过使用手机应用程序将即插即用模块虚拟化到 RESTful API 来创建物联网应用程序。这意味着无需硬件编程 ! 无需面包板 ! 无需跳线 ! 也无需焊接 ! 只需在手机上安装应用程序，您就可以在 5 分钟内建立一个简单的物联网项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.27de35791Ua30s&id=555309142801)

## 产品特性

- 无需硬件编程，无需面包板，无需跳线，无需焊接
- 支持很多 Grove 模块 (查看手机应用程序列表)
- 可视化配置替代微控制器编程
- 通过云编译和 OTA 自动升级
- 把现实世界融入虚拟平台。所有的传感器都变成了虚拟 RESTful API
- Android & iOS 应用程序管理 Wio Link
- 支持 Seeed 的 IFTTT

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio_Link_Banner.gif)

## 规格参数
----
|常用参数|值|
|:---|---|
|**尺寸**|55mm * 48mm|
|**晶振**|26MHz|
|**闪存**|4MBytes (W25Q32B)|
|**Wi-Fi 网络协议**|802.11b/g/n|
|**Wi-Fi 加密技术**|WEP/TKIP/AES|
|**Grove 接口**|6 |
|**Flash**|	4MB (W25Q32B)|

|电压电流参数|值|
|:---|---:|
|**每个 I/O 引脚的直流电流**|12mA|
|**输入电压 (Micro USB)**| 5V|
|**输入电压 (电池)**|3.4~4.2V|
|**输出直流电流**|1000mA MAX
|**工作电压**|3.3V|
|**充电电流**|500mA MAX|

## 创意应用
----
Wio Link 可以为诸如此类的项目提供简单的 Wi-Fi 解决方案 :

- 智能家居
- 智能环境监测
- 玩具
- 物联网

事实上，我们已经在我们的 [**recipe**](http://www.seeed.cc/projects.html?t=Wio) 中设计了很多项目，快来看看吧，找到一些有趣的项目，甚至分享您自己的项目，我相信它会为您赢得很多粉丝 ~

|Irrigation control system |The internet of led wall | Dog feeding machine|
|---|---|---|
|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/2.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/1.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/3.png)|
|[点击制作](http://www.seeed.cc/project_detail.html?id=1274)    |[点击制作](http://www.seeed.cc/project_detail.html?id=1594) |[点击制作](http://www.seeed.cc/project_detail.html?id=1066)|

|Kickstarter Monitor|MIssing Call Monitor|Boss Key|
|---|---|---|
|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/4.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/5.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/6.png)|
|[点击制作](http://www.seeed.cc/project_detail.html?id=1081)    |[点击制作](http://www.seeed.cc/project_detail.html?id=1059) |[点击制作](http://www.seeed.cc/project_detail.html?id=1077)|

!!!Note
    一些案例是为 Wio Node 制作的，但是它也适用于 Wio Link。

## 硬件概述
---

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Hardware%20overview.jpg)

|功能区|功能|
|---|---|
|MCU	|ESP8266|
|数字端口 0	|GPIO **14**|
|数字端口 1|	GPIO **12**|
|数字端口 2	|GPIO **13**|
|模拟端口	|**A3**|
|UART 端口|	引脚 **1** & 引脚 **3**|
|I2C 端口|	引脚 **4** & 引脚 **5**|
|状态指示灯|蓝色 LED 是 WiFi 状态指示灯，红色 LED 是工作状态指示灯|
|配置按钮| 配置和管理您的 Wio Link|
|电池座|JST2.0|
|Micro USB|为主板供电或与 PC 通信|
|复位按钮|重置 MCU|

### 状态指示灯
靠近 FUNCTION 按钮的地方有 2 个状态指示灯，一个蓝色指示灯和一个红色指示灯。蓝色 LED 是 WiFi 状态指示灯。它有以下闪烁模式:

- 配置模式下呼吸灯
- 快速闪烁两次然后熄灭 1S ： 从路由器请求IP地址
- 快速闪烁一次然后熄灭 1S ： 连接到服务器
- 点亮 1S 然后熄灭 1S ： 该节点在线
- 长亮 ： 节点由于未获得 IP 或未连接到服务器离线。
- 快速闪烁 (点亮 100ms 然后熄灭 100ms)  ：OTA

!!!Note
    蓝色 LED 连接到 **GPIO2**，也是 UART1 的 **TX** 引脚。下载固件时，UART1 自动切换为在 UART0 上传输数据。所以在下载固件时，BLUE LED 会闪烁。启动后，**GPIO2** 将被配置为 GPIO 接口而不是 UART1 的 **TX**。

!!!Note
    红色 LED 是 Grove 模块的电源状态指示灯。所有的 6 个 Grove 接口的 VCC 接在一起，并且可以用 GPIO **15** 控制。当节点处于深度睡眠模式时，所有的 Grove 模块也都掉电。当 Grove 模块上电时，红色 LED 指示灯点亮，当 Grove 模块掉电时，红色 LED 指示灯熄灭。

### 电池管理
Wio Link 有一个内置的 LiPo 电池充电器，当 USB 连接时，您可以通过 JST 2.0 端口为 3.7v LiPo 电池充电。电池需要单独购买。点击购买 [3.8V 5100mAh 锂电池](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.25.3605a153ETyPH1&id=534229881706)

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/500px-Wio_Link_Battery.jpg)

## 入门指导
---

现在我们用 Wio Link 建立一个非常基本的 LED 应用程序，在这个应用程序中，您将能够在 5 分钟内通过智能手机控制 LED。在我们开始之前，请准备以下的器材 :

|Wio Link|Grove - LED|Micro USB Cable|
|:--------:|:-----------:|:---------------:|
|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio%20link%20small%20image.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Red%20LED.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/48cmUSBc.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.2e541469kJbDsv&id=555309142801)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.edea6cbbSX2PY&id=45476819992)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.10b8b8cc1r2l2j&id=521385344999)|

!!!Note
    * 还需要智能手机 (Android OS 4.1 或更高版本，iOS 7 或更高版本)
    * Grove - LED 内包含 Grove 线缆

### **步骤 1 :** 安装 Android/iOS App
您需要安装 Wio Link 应用程序来管理和配置您的 Wio Link 设备。

下载 Android/iOS 应用程序并安装，或者您可以去 App Store 或 Google Market 搜索 "Wio Link"。

|[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Android%20Robot%20new.jpg)](https://play.google.com/store/apps/details?id=cc.seeed.iot.ap)|[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Apple%20new.jpg)](https://itunes.apple.com/us/app/wio-link/id1054893491?mt=8)|
|:---:|:---:|
|[下载 Android App](https://play.google.com/store/apps/details?id=cc.seeed.iot.ap)|[下载 iOS App](https://itunes.apple.com/us/app/wio-link/id1054893491?mt=8)|

!!!Note
    确保您的 Android 系统版本是 Android OS 4.1 或更高版本，iOS 系统版本是 iOS 7 或更高版本。

### **步骤 2 :** 创建帐户
- 如果您是第一次使用 Wio APP，可能需要 GPS 授权，请允许，然后注册。
- 如果您已有帐户，请在登录之前检查服务器位置。

!!!Note
    请注意服务器位置，错误的服务器位置将导致无法连接到 Wio Link。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)

### **步骤 3 :** 连接 Wio Link Wi-Fi AP
- 按住 CONFIG 按钮，直到蓝色 LED 变为呼吸模式 (亮暗渐变)，此时 Wio Link 已成功转到配置模式，并可以被 Wio App 检测到。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/WioLink_Configure-middle.png)

- 点击 **Add your first Device**
- 选择 **Wio Link**
- **Go to Wi-Fi list** 将引导您进入智能手机的 Wi-Fi 设置界面。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-1new.png)

- 如果您已成功将蓝色 LED 变为呼吸模式，您将在 Wi-Fi 列表中找到 Wio Link，连接到它 (通常在 Wi-Fi 列表中出现的不是 Wio Link，我的是 Wio_8B2F12，您可能在您的列表中找到的是 Wio_xxxxxx)
- 一旦连接成功，您将收到通知，然后返回到应用程序
- 下一步是连接到您的家庭或公司 Wi-Fi

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-2.png)

- 如果您想要连接 Wi-Fi 有密码，则需要输入密码。
- 考虑到将来您可能需要连接多个 Wio 设备，对其重命名能使您轻松地区分它们。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step3-3.png)

### **步骤 4 :** 连接模块并更新固件
- 点击 Wio Link 进入主界面。
- 有 6 个 Grove 接口，请选择左边的第一个。
- LED 是输出设备，选择 **OUTPUT** 类别
- 选择一个看起来像灯泡的图标
- 然后底部的矩形按钮会变成红色，"View API" 变成 "Update Firmware"。选择 "Update Firmware"

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step4.png)

- 您需要将 Grove-LED 连接到 Wio Link 的 **D0** 端口。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio_Link_Grove_LED%20middle.JPG)

### **步骤 5 :** 使用 API 测试应用程序
- 现在您已成功连接 LED 到 Wio Link，点击 "View API" 查看 Wio Link 的 API
- 在 "Test Request" 区域输入 "1" 或 "0"，然后点击 "Post" 按钮，看看会发生什么。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Step5.png)



## IFTTT & DoButton 入门指导
---
不知道如何编程 ? 不用担心，在 [IFTTT](https://en.wikipedia.org/wiki/IFTTT) 帮助下，即使您对编程一无所知，仍然可以构建一些简单的项目。

IFTTT 是 "If This Then That" 的缩写，它是一个免费的基于网络的服务，允许用户创建简单的条件语句链 (称为 "recipes")，这是根据对其他网络服务 (如 Gmail，Facebook，Instagram) 的更改而触发的。IFTTT 如何与 Wio Link 一起使用 ? 如下图所示，Seeed在 wio.seeed.io 上提供了云服务，可以交换数据并向 IFTTT 和 Wio Link 发送指令。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/IFTTT.png)

如果您没有IFTTT帐户，请点击 [这里](https://ifttt.com/join) 注册。

如果您已经拥有IFTTT帐户，请单击 [这里](https://ifttt.com/recipes/search?q=seeed) 与 Seeed 连接，或者在 IFTTT 网站搜索 Seeed。在那里，您会发现 9 个配方教您如何使用IFTTT。
![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/IFTTT%20recipes.png)

什么是 DoButton? DoButton 是 IFTTT 的一个应用程序，可以让您创建自己的个性化按钮，非常适合构建物联网项目并通过智能手机控制它，下面是两个示例，向您展示如何使用 IFTTT&DoButton 来创造有用的应用程序。

### 示例:

| **IFTTT** | **DoButton** |
|:---|:---|
|[ **项目** ][DIY an Automatic Garden Irrigation without coding](http://www.seeed.cc/project_detail.html?id=1080)|[ **项目** ][How to feed your pets when you're not home](http://www.seeed.cc/project_detail.html?id=1066)|
|[ **视频** ][How to use ITFFF](https://vimeo.com/148590984)|[ **视频** ][How to use DoButton](https://vimeo.com/146988454)|

## 高级用户指南
----
感觉这些例子太简单了? 想做更复杂的项目? 这里是高级用户指南。通过这些指南，高级用户可以了解更多关于 Wio Link 的详细信息，部署专用服务器，甚至为 Wio Link 编写模块驱动程序。

[![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/GOTO_ADVANCED_GUIDE.png)](https://github.com/Seeed-Studio/Wio_Link/wiki)

这个指南中包括:

- 参考 API
- 服务器部署指南
- 如何编写 Wio Link 的模块驱动程序

## 高级教程
如果您已经用智能手机成功地控制 Grove-LED，并且想要尝试一些更加困难而又不复杂的项目，来试试这个教程吧，在学习之后，您将能够建立一个温湿度监视器，并且通过 Wio Link 点亮 RGB Led strip 。

在开始之前，请检查是否以下器材 :

|RGB Led strip|Grove-Temperature and Humidity Sensor|
|:---:|:---:|
|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/RGB%20LED%20Strip.jpg)|![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/grove-T%26H%20sensor.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.1aa43c97koOhYN&id=45783932318)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.15.3c437e6b12HsEQ&id=520506479798)|

- 步骤 1: 从 Grove 接口中取出 Grove-LED，将 LED Strip 插入 Wio Link，并将相同的模块添加到 App 中的 Wio Link
- 更新固件

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/advance%20tutorial%20video.png)

- 步骤 2：将 Grove-Temperature&Humidity Sensor 插入 Wio Link，并将相同的模块添加到 App 中的 Wio Link
- 更新固件

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/advance%20tutorial%20video%202.png)

- 步骤 3: 查看 API 并读取室内温度和湿度。下面的图片显示手持前后的温度变化。温度升高了 1 摄氏度。尝试看看如何改变室内的温度和湿度。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Celsuis%202%20pics.png)

- 步骤 4: 通过改变 RGB 值来控制 LED strip 的亮度。

由于 Wio Link App 读取十六进制 RGB 值，所以需要将 RGB 值转换为十六进制值。在这里我安利网站 [RGB to Hex](http://www.rgbtohex.net/)。只需输入 3 个 RGB 元素 (红色，绿色，蓝色) 的 RGB 值，网站将 RGB 值转换为十六进制。这里是一些例子。
- 输入 255, 0, 0

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/RGB%20255%200%200.png)

- 转换后您得到的十六进制值为 FF0000，颜色是红色。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/FF0000.png)

!!!Note
    输入的 RGB 值应该是 0 到 255 之间的任何自然数 (包括 0 和 255)

然后在 App 中输入要点亮的 LED 数量和十六进制值，这里我的 LED strip 有 30 个 LED，所以我点亮了所有的 LED。

![](https://github.com/SeeedDocument/Wio_Link/raw/master/image/Wio%20link%20control%20led%20strip.png)

您也可以指定灯条的哪一部分被点亮，并赋予特殊颜色，甚至可以以彩虹模式闪烁。更多惊人的功能正在等待您的探索 !


## 资源下载
---

- **[Eagle 文件]** [EAGLE PCB file](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/202000877%20Wio%20Link%20v1.0%20sch%20pcb.zip)

- **[原理图]** [EAGLE Schematic files](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/Wio_Link_SCH_v1.0.rar)

- **[原理图 PDF]** [Schematic files(pdf)](https://github.com/SeeedDocument/Wio_Link/raw/master/resource/Wio%20Link%20v1.0%20sch.pdf)

- **[其他资源]** [Source Code on Github.](https://github.com/Seeed-Studio/Wio_Link)

- **[其他资源]** [API Reference](http://seeed-studio.github.io/Wio_Link/)

- **[其他资源]** [Server Deployment Guide](https://github.com/Seeed-Studio/Wio_Link/wiki/Server%20Deployment%20Guide)

- **[其他资源]** [How to write module driver for Wio Link](https://github.com/Seeed-Studio/Wio_Link/wiki/How-to-write-module-driver-for-Wio-Link%3F)

- **[其他资源]** [iot.seeed.cc](http://iot.seeed.cc/index.html) to get more info.


## FAQ
----
以下是来自用户的一些高频问题。如果您在使用 Wio Link 或其他 Wio 产品时遇到任何其他问题，欢迎来到 [Wio 产品社区](http://www.seeed.cc/topics.html?t=Wio) 获取更多信息，那里有许多专业用户给您提供产品使用建议，还有许多高级用户提供了大量有关如何使用 Wio 产品的建议 !

**1. 电源和电池 - Wio Link 是否带有锂电池 ?**

没有。每个 Wio Link 都配有一根 micro USB 线缆进行充电，您也可以从我们的淘宝店铺购买一个锂电池。以下是参考参数 :
- 最大输出电压 : 4.2V;
- 最大充电电流 : 500mA.


**2. 电源和电池 - Wio Link 可以使用电源适配器吗 ? 哪种类型 ? 还有电池座类型 ?**

有两种方法为 Wio Link 供电，Micro USB 线缆或锂电池供电。如果 Micro USB 和电池均插入主板，电池将由 USB 电源充电。您可以使用各种可以连接 Micro USB 电缆和 5VDC 输出的电源适配器。电池座是一个 JST-2.0 连接器。


**3. 功耗 - Wio Link 的功耗是多少 ?**

平均功耗为 70mA。使用 700mAh 的电池，可以连续工作 10 个小时。低功耗 API 可以将 Wio Link 从工作模式更改为睡眠模式。睡眠模式下平均功耗降低到 150uA 或更少。


**4. Grove 线缆 - 所有 Grove 套件中是否都装有 Grove 线缆 ?**

是的，每个 Grove 模块都包含一根标准的 4针 Grove 线缆。


**5. RESTful APIs - 终端在哪里 ? 访问是不是需要通过一些云服务器呢 ? 是需要连接到互联网还是可以通过本地网络完成 ?**

我们将 REST API 服务器部署到 iot.seeed.cc，以便您可以从 iot.seeed.cc 访问传感器和执行器。目前，Wio Link 必须连接到互联网。另外，我们将开源服务器，以便用户以非常简单的 Docker 方式部署本地服务器。在部署了本地服务器的情况下，他们可以在本地使用编译和数据交换服务，而不连接到互联网。


**6. 支持的编程方法 - 是否支持其他编程方法，如 Arduino IDE ?**

Wio Link 可以使用 Arduino IDE 进行编程，在这种情况下，它将失去 RESTful API 的功能，除非在同一时间执行另一个。Wio Link 最大期望地将物联网转换为物理硬件，所以交互将在网络 / 互联网上运行。但不用担心，软件架构灵活，可以将源代码下拉到本地，将 Wio Link 连接到本地服务器，然后修改将要编译的源代码。

如果您想与 Arduino 或 RPI 交互，可以开发一个第三方模块驱动程序，这里是 [指南](https://github.com/Seeed-Studio/Wio_Link/wiki/How-to-write-module-driver-for-Wio-Link%3F) 和 [示例驱动程序](https://github.com/Seeed-Studio/Wio_Link/tree/master/grove_drivers/grove_example)


**7. 支持平台 - Wio Link 支持 Windows 吗 ?**

现在 Wio Link 提供了 Android 系统和 iOS 系统的 APP。所有服务都视为 RESTful API，例如用户帐户和 OTA，遵循 API 文档，第三方开发人员可以构建自己的应用程序，如移动应用程序或桌面应用程序。Wio Link 是一个社区友好的项目。它不会局限于某个平台。我们真的希望人们以他们自己的方式享受 Wio Link。


**8. 可以使用 Wio Link 与现有系统进行交互吗 ?**

可以的。 Who Link 可以通过多种方式与现有系统进行交互。首先，将 Wio Link 的任意 GPIO 连接到其他系统，在移动应用程序中选择 “Generic Digital Input” 或 “Generic Digital Output” 的虚拟 Grove 模块，然后使用 RESTful API 调用向 / 从现有系统发送 / 读取信号。其次，将 Wio Link 的模拟端口连接到其他系统，在移动应用程序中选择 “Generic Analog Input” 的虚拟 Grove 模块，然后读取现有系统的某个物理量的模拟量测量。第三，为了更灵活地与现有系统进行交互，可以开发第三方模块驱动程序，通过 I2C 或 UART 接口将请求从互联网发送到现有系统。我们有关于如何开发第三方模块驱动程序的指导[1]，同时我们也可以为您提供技术支持。

[如何开发第三方模块驱动程序的指导](https://github.com/Seeed-Studio/Wio_Link#how-to-write-module-driver-for-wio-link)


**9. Wio Link 支持哪些 Grove 模块?**

现在有 150 多种即插即用 Grove 模块可供选择，其中有 36 个目前在 Wio Link 上可使用，我们正在不断努力完善。

以下是目前支持的 Grove 模块列表 :

### 列表 : 支持的 Grove 模块

|SKU       |名称                                        |接口 |驱动                 |购买链接       |
|----------|--------------------------------------------|----------|-------------------    |-----------|
|101020008 |    Grove - Moisture Sensor                 |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11DbSHW8&id=520170918975) |
|101020014 |    Grove - Light Sensor                    |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3d843e4bASb9K3&id=544373791068) |
|101020015 |    Grove - Temperature Sensor              |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11RJtPqc&id=520512844173) |
|101020017 |    Grove - Rotary Angle Sensor             |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.5205ed58aC6jOO&id=45531021242) |
|101020022 |    Grove - Light Sensor(P)                 |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.21.3d843e4bASb9K3&id=558132536414) |
|101020023 |    Grove - Sound Sensor                    |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.34488b0fhMBGev&id=45507318433) |
|101020027 |    Grove - Electricity Sensor              |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.74f1ae10Uw4ULo&id=45558584472) |
|101020036 |    Grove - Slide Potentiometer             |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3469939BDfGyn&id=45554612830) |
|101020042 |    Grove - 80cm Infrared Proximity Sensor  |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.73b21493UP1CiX&id=45459991191) |
|101020043 |    Grove - UV Sensor                       |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.17e77669ZnMGKl&id=45574580580) |
|101020048 |    Grove - Rotary Angle Sensor(P)          |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.1dbf48558LIOMS&id=45554377762) |
|101020063 |    Grove - Loudness Sensor                 |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4075f3d30KVeTf&id=45476699231) |
|101020076 |    Grove - Luminance Sensor                |模拟    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.6.686bd0c8cCSeni&id=45574380098&ns=1&abbucket=1#detail) |
|101020078 |    Grove - Air quality sensor v1.3         |模拟    |通用模拟输入   | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11UP6yWS&id=520569030749) |
|101020003 |    Grove - Button                          |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.43b722dcozKioJ&id=531838497696) |
|101020004 |    Grove - Switch(P)                       |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.390686a76gl5mN&id=538862309682) |
|101020005 |    Grove - Collision Sensor                |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.15.5bbf7f72OycBQY&id=45507110387&ns=1&abbucket=1#detail) |
|101020009 |    Grove - Line Finder                     |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.53b85aa6LYBBRO&id=540386082647) |
|101020018 |    Grove - Water Sensor                    |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.39.79618f20Awu3v4&id=45534561319) |
|101020020 |    Grove - PIR Motion Sensor               |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2ac176a4pN2dqu&id=45568896887) |
|101020025 |    Grove - Tilt Switch                     |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.15.156ac3aD5feFp&id=45477183101&ns=1&abbucket=1#detail) |
|101020037 |    Grove - Touch Sensor                    |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.49560958exDLpw&id=45486442714) |
|101020038 |    Grove - Magnetic Switch                 |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3235e8fuVLe7e&id=521463829492) |
|101020046 |    Grove - Hall Sensor                     |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.15f3e5efluXnfn&id=45555333014) |
|101020049 |    Grove - Flame Sensor                    |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.67713b2eWbqO5p&id=45575868600) |
|111020000 |    Grove - Button(P)                       |数字   |通用数字输入  | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.71f0ac4aGsq76G&id=532955584350) |
|101020073 |    Grove - Electromagnet                   |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.544740f4IE4s7g&id=45478243491) |
|101020090 |    Grove - Water Atomization v1.0          |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.41675b41iTWiz5&id=531586572094) |
|103020004 |    Grove - Solid State Relay               |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.25.159652ccC7eAat&id=45507430313) |
|103020005 |    Grove - Relay                           |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.159652ccC7eAat&id=45670971061) |
|103020008 |    Grove - MOSFET                          |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10678284.0.0.4f8e27d5qZhowx&id=45573744942&qq-pf-to=pcqq.discussion) |
|103020010 |    Grove - 2-Coil Latching Relay           |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.31.54fdba01g7whYL&id=45571928583) |
|103020014 |    Grove - Dry-Reed Relay                  |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.54fdba01g7whYL&id=45508590653) |
|104020001 |    Grove - Variable Color LED              |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.66.1a792andVk9L&id=45507366183) |
|104020002 |    Grove - Purple LED (3mm)                |数字   |通用数字输出 | 停售 |
|104020005 |    Grove - LED String Light                |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.30.7f07baa7K6ptMq&id=45574372169) |
|104030005 |    Grove - Red LED                         |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.27.7f07baa7K6ptMq&id=45476819992) |
|104030007 |    Grove - Green LED                       |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.54.7f07baa7K6ptMq&id=534288793023) |
|104030009 |    Grove - White LED                       |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.39.7f07baa7K6ptMq&id=527003387872) |
|104030010 |    Grove - Blue LED                        |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.57.7f07baa7K6ptMq&id=531838541569) |
|104030014 |    Grove - Multi Color Flash LED (5mm)     |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.63.7f07baa7K6ptMq&id=520712642812) |
|105020003 |    Grove - Vibration Motor                 |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.7b0f5c5eZLDIt3&id=45574264986) |
|105020004 |    Grove - Mini Fan                        |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.7a1236d08j5Lxv&id=546834577734) |
|105020005 |    Grove - EL Driver                       |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.16.1631005e0go193&id=531816002922) |
|107020000 |    Grove - Buzzer                          |数字   |通用数字输出 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.1ee44319IeGQK0&id=520245748676) |
|107020001 |    Grove - Speaker                         |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.20.12a3e2204K97PC&id=45477159219&ns=1&abbucket=1#detail) |
|101020034 |    Grove - 3-Axis Digital Compass          |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.21.422c5206CViGkC&id=45460663307&ns=1&abbucket=11#detail) |
|101020039 |Grove - 3-Axis Digital Accelerometer(±1.5g) |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=686.1000925.0.0.4d555aagVGiYe&id=45770637854) |
|101020050 |    Grove - 3-Axis Digital Gyro             |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.16.77e6a58cFyJ8YW&id=45483246815&ns=1&abbucket=1#detail) |
|101020072 |    Grove - Barometer Sensor (BMP280)       |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1aa2d2c5LlFSih&id=534767716742) |
|101020083 |    Grove - Gesture                         |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.7bd41b6cq03WZR&id=520252964566) |
|101020088 |    Grove - Multichannel Gas Sensor         |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.16.5e47879706k20S&id=521355807303) |
|103020013 |    Grove - I2C ADC                         |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.ed36d45w5WElN&id=45477279346) |
|104030008 |    Grove - OLED Display 1.12''             |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3d29aa41N1HWQN&id=531865752955) |
|104030011 |    Grove - OLED Display 0.96''             |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3d29aa41N1HWQN&id=520855873601) |
|105020001 |    Grove - I2C Motor Driver                |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.25.2fdd15dcCiiUMm&id=45476447918) |
|107020006 |    Grove - I2C FM Receiver                 |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.19.2fdd15dcCiiUMm&id=45506822801) |
|101020193 |Grove - Temp&Humi&Barometer Sensor(BME280)  |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2b966a3ayT6w2X&id=534636479507) |
|101020010 |    Grove - Ultrasonic Ranger               |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11bTW76G&id=45550924107) |
|101020016 |    Grove - Infrared Receiver               |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.66e00062bQ3UW9&id=45477043694) |
|101020019 |    Grove - Temperature&Humidity Sensor Pro |数字   |自驱                 | [点击购买](http://wiki.seeedstudio.com/cn/Grove-Temperature_and_Humidity_Sensor_Pro/) |
|101020026 |    Grove - Infrared Emitter                |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5c569fc8BjmPyt&id=45555269740) |
|101020029 |    Grove - Infrared Reflective Sensor      |其它    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.31686ed5uZEUXW&id=558395535859) |
|101020030 |    Grove - Digital Light Sensor            |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7d75ff313PQbmb&id=45507034521) |
|101020040 |    Grove - IR Distance Interrupter         |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.2c53d5c0TRodH6&id=547068489828) |
|103020018 |    Grove - Recorder                        |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.74025d8afMQc1W&id=45505914793) |
|104020006 |    Grove - LED Bar v2.0                    |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.11199f8ahwHx5F&id=520900900588) |
|104030003 |    Grove - 4-Digit Display                 |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.3517bf29wZTVb1&id=45908368559&qq-pf-to=pcqq.discussion) |
|316010005 |    Grove - Servo                           |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3a3c0158YgGB9u&id=45554357772) |
|101020067 |    Grove - CO2 Sensor                      |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.39759928QocDLK&id=45476707662) |
