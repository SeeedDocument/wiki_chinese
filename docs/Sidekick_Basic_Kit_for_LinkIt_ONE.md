---
name: Sidekick Basic Kit for LinkIt ONE
category: LinkIt
bzurl:  https://www.seeedstudio.com/Sidekick-Basic-Kit-for-LinkIt-ONE-p-2027.html
oldwikiname: Sidekick Basic Kit for LinkIt ONE
prodimagename:  SKP-0.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Sidekick_Basic_Kit_for_LinkIt_ONE
sku:    110060038
---


![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_LinkIt_ONE/raw/master/img/SKP-0.jpg)


##   快速开始

我们将讨论如何使用 LinkIt ONE

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.1.64fe3af7JQon8G&id=45457487196&ns=1&abbucket=1#detail)

##   基础

让我们用一个晶体管，LED 和一个拨动开关构建一个简单的电路。发光二极管 (LED) 将电能转换为可见光。晶体管是电子器件中的一个基本组成部分，可用作开关或电流放大器。在这里，我们使用晶体管间接作为开关来打开和关闭 LED。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-The_Basics/) 查看完整的教程。

##   教程 2 : Hello World

在前面的章节中，我们已经对如何用电子元件控制 LED 有所了解，现在让我们用一些软件来自动控制 LED。您只需上传本节中提供的代码即可。代码将会先打开 LED，延迟 3 秒后将其关闭。让我们开始使用 LinkIt 板。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Hello_World/) 查看完整的教程。

##   教程 3 : Push Button (按钮)

我们从前面的章节中了解到软件和硬件是如何工作的。在本章中，我们将学习如何整合软件和硬件用以控制LED。按照图 3.2 所示进行面包板连接并上传代码。现在这个电路作为一个双向开关，当您按下左侧的按钮时，LED 发光；当按下右侧的按钮时，LED关闭。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Push_Button/) 查看完整的教程。

##   教程 4 : Marquee (跑马灯)

前面几节中的实验只使用了一个 LED，为了显示令人眼花缭乱的光效，可以使用三个 LED。按照图 4.2 所示进行连接，并上传下面给出的代码，然后观察发生的变化。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Marquee/) 查看完整的教程。

##   教程 5 : Colorful World (多彩的世界)

我们现在知道如何控制 LED。R-Red G-Green B-Blue 是基本色，当他们以不同比例混合时，产生不同颜色。RGB LED 由四个引脚组成，长引线是正极，另外三个引脚用于控制 RGB 颜色。如图 5.2 所示的连接硬件，并上传代码。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Colorful_World/) 查看完整的教程。

##   教程 6 : Analog Interface (模拟接口)

在前面的章节中，我们学习了如何使用数字接口来控制电路的输入和输出。在本节中，我们将学习如何使用称为电位计 (也称为可变电阻器) 的模拟设备来改变输出。电位器用于在 0 ~ 5V 范围内改变电压。MPU 读取 0-1023 范围内的电压值模拟值，可以用来控制 LED ( PWM模拟输出接口) 的亮度。如果电位器顺时针旋转，LED 会逐渐变亮。如果逆时针旋转，LED 会逐渐变暗。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Analog_Interface/) 查看完整的教程。

##   教程 7 : Mini Servo (舵机)

舵机通常用于小型机器人和其他机器的控制角位置。它由一个小齿轮箱包裹，并由定时控制脉冲定位。在本节中，我们通过电位计控制舵机的角度位置。

点击 [这里](http://wiki.seeed.cc/LinkIt-ONE-Tutorial---Mini-Servo/) 查看完整的教程。

##   教程 8 : Light Sensor (光传感器)

是时候知道一些新的传感器了，它们可以使我们的项目更有趣。光敏电阻 (光敏电阻或光电池) 是根据环境光的强度改变其电阻值的光敏元件。蜂鸣器是一种电声装置，用于在连接到电源时产生标准音调。我们将在实验中使用这两个组件。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Light-Sensor/) 查看完整的教程。

##   教程 9 : SMS control the LED (短信控制LED)

在这一节中，我们将实现一些很酷的功能。LinkIt One 的突出特点集成了通信模块。我们正在通过 GSM 通信模块来传输消息，开关状态改变以开关 LED。首先连接天线，然后将 SIMCARD 插入 LinkIt One 的插槽，然后按照原理图连接电路。使用 GSM 手机，编辑信息内容 ON 或 OFF，发送指定的号码 (SIM 号码)，现在可以控制 LED 开关状态，并进行全局同步。

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-SMS_control_the_LED/) 查看完整的教程。

##   教程 10 : Get temperature with Webpage (通过网页获取温度)

LinkIt One 具有 Wi-Fi 通信功能。我们通过 LinkIt One 收集了一些数据。作为 Internet AP 通过提供 Web Server 来支持数据访问。通过浏览器访问相应的 IP 地址可以获取数据。下一步您需要连接电路，从温度传感器获取数据。然后配置 Wi-Fi 天线，并连接到网络，请选择网络并输入三个参数，网络名称 (WiFi_AP)，访问密码 (WIFI_PASSWORD) 和路由器的传输模式 (选项 LWIFI_OPEN, LWIFI_WPA, LWIFI_WEP)。最后，代码被上传到 LinkIt One。使用网络终端设备，打开浏览器并输入 IP 地址即可获取温度数据。(通过 DHCP 路由器访问访问 IP 地址分配)

点击 [这里](http://wiki.seeed.cc/LinkIt_ONE_Tutorial-Get_temperature_with_Webpage/) 查看完整的教程。

##   资源下载

*   **[其他资源]** [Github Repo for Sickkick Basic Kit for LinkIt ONE](https://github.com/Seeed-Studio/Sidekick_Basic_Kit_for_LinkIt)
