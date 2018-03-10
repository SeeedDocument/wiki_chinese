---
title: Wio Node
category: Wio
bzurl: https://www.seeedstudio.com/Wio-Node-p-2637.html
oldwikiname: Wio_Node
prodimagename: Front%26Back.png
wikiurl: http://wiki.seeedstudio.com/cn/Wio_Node
sku: 102110057
---

创建物联网项目是令人兴奋的，因为您可以连接您周围的一切，并控制它们。然而有时候创建物联网应用并不容易，因为硬件，编程，跳线和焊接等工作都需要很多的努力。即使是训练有素的用户也要花费数小时来处理所有的工作，更不用说初学者了。为了简化物联网项目的发展，Seeed 在 **[kickstarter](https://www.kickstarter.com/projects/seeed/wio-link-3-steps-5-minutes-build-your-iot-applicat?ref=nav_search)** 上发布了 **[Wio Link](http://www.seeedstudio.com/wiki/Wio_Link)**，取得巨大的成功。Kickstarter 的口号很好地阐述了 Wio link 的主要特征 :

**3个步骤，5分钟，开发出你自己的 IOT 应用！**

如此简单，它能快速创建物联网项目，但它不是完美的。如果我们只需要 2 个 Grove 接口怎么办呢 ? 如果应用的空间有限，但是 Wio Link 的尺寸过大怎么办呢 ? 如果我们想要降低成本怎么办呢 ? 所以在我们发布 Wio Link 之后，一个小型和经济的产品也随之推出，几个月来，Seeeder 重新设计和优化了 Wi-Fi 板，这里是 Wio 家族的新成员 --- **Wio Node**。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Front%26Back.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Front%26Back.png)

物如其名，Wio Node 是一个真正意义上的 Wi-Fi 节点，它可以连接物联网项目中的其它事物。如果 Wio Link 是大哥，Wio Node 就是 Wio 家族的小兄弟，这个可爱的小家伙只有 Wio Link 的四分之一大小，但是它集 Wio Link 的所有基本功能于一体。

Wio Node 的生态系统还包括 Open Hardware **Wio Node board**，**Open Source Wio Link Mobile App** 和 **Open Source IoT Server implementation**。所以 Wio Link 的软件平台也适用于 Wio Node。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.15.3d494946SuZl5r&id=532984573761)

## 产品特性
----
- 没有编程，没有面包板，也没有跳线，更无需焊接。
- 支持很多 Grove 模块
- 即插即用 Grove 模块
- 可视化配置替代微控制器编程
- 通过云编译和 OTA 自动升级
- 把现实世界融入虚拟平台。所有的传感器都变成了虚拟 RESTful API
- Android & iOS 应用程序管理 Wio Node.
- IFTTT
- CE/FCC/TELEC 认证

## 规格参数
----
|普通参数|值|电气参数|值|
|:---|---|:---|---:|
|**尺寸**|28mm * 28mm|**每个 I/O 引脚的直流电流**|12mA|
|**晶振**|26MHz|**输入电压 (Micro USB)**|5V|
|**内存**|4MBytes (W25Q32B)|**输入电压 (电池座)**|3.4~4.2V|
|**Wi-Fi 网络协议**|802.11b/g/n|**输出直流电流**|1000mA MAX
|**Wi-Fi 加密技术**|WEP/TKIP/AES|**工作电压**|3.3V|
|**扩展 Grove 接口 1**|UART0/I2C0/D0 |**充电电流**|500mA MAX|
|**扩展 Grove 接口 2**|Analog/I2C1/D1|

## 创意应用
----
Wio Node 经过精心设计，为以下项目类型提供简单经济的 Wi-Fi 解决方案 :

- 智能家居
- 智能环境监测
- 有趣的玩具
- Web of Things
- Internet of Things

事实上，我们的 [**recipe**](http://www.seeed.cc/projects.html?t=Wio) 中有很多项目，来看看吧，找一些有趣的项目，甚至分享您自己的项目，我相信它会为您圈粉。

|Irrigation control system |The internet of led wall | Dog feeding machine|
|---|---|---|
|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/2.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/1.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/3.png)|
|[点击制作](http://www.seeed.cc/project_detail.html?id=1274)    |[点击制作](http://www.seeed.cc/project_detail.html?id=1594) |[点击制作](http://www.seeed.cc/project_detail.html?id=1066)|

|Kickstarter Monitor|MIssing Call Monitor|Boss Key|
|---|---|---|
|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/4.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/5.png)|![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/6.png)|
|[点击制作](http://www.seeed.cc/project_detail.html?id=1081)    |[点击制作](http://www.seeed.cc/project_detail.html?id=1059) |[点击制作](http://www.seeed.cc/project_detail.html?id=1077)|


!!!Note
    有些项目是由 Wio Link 制作的，你可以用一个 Wio Node 替换它。

## 硬件概述
----

[![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/Wio_Node_illustrate.jpg)](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/Wio_Node_illustrate.jpg)

|No.|名称|功能描述|
|---|----|--------|
|1  |Function|设置 Wio Node 工作模式|
|2  |ESP8266|基于 ESP8266 的微控制器|
|3  |Reset|重置设备|
|4  |Micro USB|供电|
|5  | Battery Holder|一个 Jst2.0 连接器，连接一个 3.7V 锂电池|
|6  | Analog/I2C1/D1|Grove 端口，可以连接 Digital/I2C/Analog 类型的 Grove 模块|
|7  | UART/I2C0/D0|Grove 端口，可以连接一个 UART/I2C/Digital 类型的 Grove 模块|

### 状态 LED

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


### Bonus!
Wio Node 有一个内置的 LiPo 电池充电器，当 USB 连接时，您可以通过 JST 2.0 端口为 3.7v LiPo 电池充电。

!!!Note
    请轻轻握住 USB micro type-B 插座，否则可能会使插座与电路板分离。电池不包含在包装内。但是我们已经在 [淘宝旗舰店](https://seeedstudio.taobao.com/search.htm?q=%B5%E7%B3%D8&s_from=newHeader&ssid=s5-e&search_type=item&sourceId=tb.item) 中为您准备了很多选择。



## 入门指导
----
现在我们用 Wio Node 建立一个非常基本的 LED 应用程序，在这个应用程序中，您将能够在 5 分钟内通过智能手机控制 LED。在我们开始之前，请准备以下的器材 :

|Wio Node|Grove - LED|Micro USB Cable|
|--------|-----------|---------------|
|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20Node2.png)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Red%20LED.jpg)|![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/48cmUSBc.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.15.3d494946SuZl5r&id=532984573761)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.edea6cbbSX2PY&id=45476819992)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.10b8b8cc1r2l2j&id=521385344999)|


!!!Note
    * 还需要智能手机 (Android OS 4.1 或更高版本，iOS 7 或更高版本)
    * Grove - LED 内包含 Grove 线缆

### **步骤 1 :** 安装 Android/iOS App

您需要安装 Wio Link 应用程序来管理和配置您的 Wio Node 设备。
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
    请注意服务器位置，错误的服务器位置将导致无法连接到 Wio Node。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/sign%20in%2Blog%20in%2Bchoose%20server.png)

### **步骤 3 :** 连接 Wio Node Wi-Fi AP

- 按住 CONFIG 按钮，直到蓝色 LED 变为呼吸模式 (亮暗渐变)，此时 Wio Node 已成功转到配置模式，并可以被 Wio App 检测到。
[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Confiture%20button.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Confiture%20button.png)
- 点击 **Add your first Device**
- 选择 **Wio Node**
- **Go to Wi-Fi list** 将引导您进入智能手机的 Wi-Fi 设置界面。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node%201.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node%201.png)

- 如果您已成功将蓝色 LED 变为呼吸模式，您将在 Wi-Fi 列表中找到 Wio Node，连接到它 (通常在 Wi-Fi 列表中出现的不是 Wio Node，我的是 Wio_091016，您可能在您的列表中找到的是 Wio_xxxxxx)
- 一旦连接成功，您将收到通知，然后返回到应用程序
- 下一步是连接到您的家庭或公司 Wi-Fi

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node2.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node2.png)

- 如果您想要连接 Wi-Fi 有密码，则需要输入密码。
- 考虑到将来您可能需要连接多个 Wio 设备，对其重命名能使您轻松地区分它们。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node3.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20to%20Wio%20node3.png)

### **步骤 4 :** 虚拟连接模块并更新固件

- 点击 Wio Node 进入主界面。
- 有 2 个 Grove 接口，请选择左边的 (D0)。
- LED 是输出设备，选择 **OUTPUT** 类别。
- 选择一个看起来像灯泡的图标。
- 然后底部的矩形按钮会变成红色，**View API** 变成 **Update Firmware**。选择 **Update Firmware**。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20modules%20with%20Wio%20node.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Connect%20modules%20with%20Wio%20node.png)

- 您需要将 Grove-LED 连接到 Wio Node 的 **D0** 端口。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Wio_Node_Grove_LED.JPG)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/Wio%20App/Wio_Node_Grove_LED.JPG)

### **步骤 5 :** 使用 API 测试应用程序
- 现在您已成功连接 LED 到 Wio Node，点击 "View API" 查看 Wio Node 的 API
- 在 "Test Request" 区域输入 "1" 或 "0"，然后点击 "Post" 按钮，看看会发生什么。

[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/change%20the%20valure%20to%20see%20what%20will%20happen.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/change%20the%20valure%20to%20see%20what%20will%20happen.png)


## IFTTT & DoButton 入门指导
-----
不知道如何编程 ? 不用担心，在 [IFTTT](https://en.wikipedia.org/wiki/IFTTT) 帮助下，即使您对编程一无所知，仍然可以构建一些简单的项目。

IFTTT 是 "If This Then That" 的缩写，它是一个免费的基于网络的服务，允许用户创建简单的条件语句链 (称为 "recipes")，这是根据对其他网络服务 (如 Gmail，Facebook，Instagram) 的更改而触发的。IFTTT 如何与 Wio Node 一起使用 ? 如下图所示，Seeed在 wio.seeed.io 上提供了云服务，可以交换数据并向 IFTTT 和 Wio Node 发送指令。

![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/WioLink-Workshop.png)

如果您没有IFTTT帐户，请点击 [这里](https://ifttt.com/join) 注册。

如果您已经拥有IFTTT帐户，请单击 [这里](https://ifttt.com/recipes/search?q=seeed) 与 Seeed 连接，或者在 IFTTT 网站搜索 Seeed。在那里，您会发现 9 个配方教您如何使用IFTTT。
[![](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/IFTTT%20recipes.png)](https://github.com/SeeedDocument/Wio_Node/raw/master/pictures/IFTTT%20recipes.png)

什么是 DoButton? DoButton 是 IFTTT 的一个应用程序，可以让您创建自己的个性化按钮，非常适合构建物联网项目并通过智能手机控制它，下面是两个示例，向您展示如何使用 IFTTT&DoButton 来创造有用的应用程序。

### 示例 :

| **IFTTT** | **DoButton** |
|:---|:---|
|[ **项目** ][DIY an Automatic Garden Irrigation without coding](http://www.seeed.cc/project_detail.html?id=1080)|[ **项目** ][How to feed your pets when you're not home](http://www.seeed.cc/project_detail.html?id=1066)|
|[ **视频** ][How to use ITFFF](https://vimeo.com/148590984)|[ **视频** ][How to use DoButton](https://vimeo.com/146988454)|


## 进阶指南
----
感觉这些例子太简单了? 想做更复杂的项目? 这里是高级用户指南。通过这些指南，高级用户可以了解更多关于 Wio Node 的详细信息，部署专用服务器，甚至为 Wio Node 编写模块驱动程序。

[![](https://raw.githubusercontent.com/SeeedDocument/Wio_Node/master/pictures/GOTO_ADVANCED_GUIDE.png)](https://github.com/Seeed-Studio/Wio_Link/wiki)

这个指南中包括 :

- 参考 API
- 服务器部署指南
- 高级用户指南
- 如何编写 Wio Link 的模块驱动程序



!!!Note
    该指南是为 Wio Link 编写的，但也适用于 Wio Node。

## 列表 : 支持的 Grove 模块

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
|101020019 |    Grove - Temperature&Humidity Sensor Pro |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.3ff19e11cJwMDK&id=45754325612) |
|101020026 |    Grove - Infrared Emitter                |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5c569fc8BjmPyt&id=45555269740) |
|101020029 |    Grove - Infrared Reflective Sensor      |其它    |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.31686ed5uZEUXW&id=558395535859) |
|101020030 |    Grove - Digital Light Sensor            |I2C       |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7d75ff313PQbmb&id=45507034521) |
|101020040 |    Grove - IR Distance Interrupter         |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.2c53d5c0TRodH6&id=547068489828) |
|103020018 |    Grove - Recorder                        |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.74025d8afMQc1W&id=45505914793) |
|104020006 |    Grove - LED Bar v2.0                    |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.11199f8ahwHx5F&id=520900900588) |
|104030003 |    Grove - 4-Digit Display                 |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.3517bf29wZTVb1&id=45908368559&qq-pf-to=pcqq.discussion) |
|316010005 |    Grove - Servo                           |数字   |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3a3c0158YgGB9u&id=45554357772) |
|101020067 |    Grove - CO2 Sensor                      |UART      |自驱                 | [点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.39759928QocDLK&id=45476707662) |



## FAQ(疑问解答)
----
以下是我们通常从新用户处收到的一些问题。如果您在使用 Wio Node 或其他 Wio 产品时遇到任何其他问题，欢迎访问 [Wio 社区](http://www.seeed.cc/topics.html?t=Wio)，这里有许多专业用户为您提供建议，还有许多高级用户提供了有关如何使用 Wio 产品的创意 !

**Q1. Wio Node 和 Wio Link 有什么区别 ?**

>Wio Node 就像迷你 Wio Link 一样，只有 Wio Link 的四分之一大小，而且便宜很多。除去尺寸和价格，Wio Node 还具有 Wio Link 的全部功能。对于那些喜欢较小的尺寸的用户，Wio Node 是最好的选择。

**Q2. 如果无法连接服务器，我该怎么办 ?**

>检查是否选择了错误的服务器。如果您不在中国大陆，请选择全球服务器。

**Q3. 无法配置 Wio Node，或无法在 wifi 列表中找到 Wio Node ?**

>注意蓝色 LED，确保其处于呼吸模式，只有 LED 处于呼吸模式时才能在 WiFi 列表中找到 Wio Node。

**Q4. 如果我想连接多个 I2C 设备，该怎么做 ?**

>[Grove - I2C hub](https://www.seeedstudio.com/s/I2C%20hub.html) 可以将 1 个 I2C 端口分成 4 个。点击 [这里](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.9.217e7e5dMhGRTD&id=45807345671) 购买。

**Q5. 可以将 Wio Node 更改为睡眠模式吗 ?**

>是的，请检查最后一个 API，在那里你可以命令 Wio Node 进入睡眠模式。

## 资源下载
----
- **文档**
    - [API Reference](http://seeed-studio.github.io/Wio_Link/)
    - [Server Deployment Guide](https://github.com/Seeed-Studio/Wio_Link/wiki/Server%20Deployment%20Guide)
    - [How to write module driver for Wio Link](https://github.com/Seeed-Studio/Wio_Link/wiki/How-to-write-module-driver-for-Wio-Link%3F)
- **软件**
    - [Sourcecode on **Github**](https://github.com/Seeed-Studio/Wio_Link)
- **硬件**
    - **[原理图 PDF]** [Schematic File in **PDF**](https://github.com/SeeedDocument/Wio_Node/raw/master/Recources/Wio%20Node%20v1.0.pdf)
    - **[Eagle 文件]** [Schematic File in **Eagle**](https://github.com/SeeedDocument/Wio_Node/raw/master/Recources/Wio_Node_Schematics.zip)
- **认证**
    - **[认证文件]**https://github.com/SeeedDocument/Wio_Node/raw/master/Recources/CE-FCC-TELEC_Certified(only)_for_core_module_ESP-WROOM-02.zip
