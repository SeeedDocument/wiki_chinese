---
title: GrovePi+ Starter Kit for Raspberry Pi A+,B,B+&2,3 (CE certified)
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/GrovePi%2B-Starter-Kit-for-Raspberry-Pi-A%2B%2CB%2CB%2B%262%2C3-(CE-certified)-p-2572.html
oldwikiname: Raspberry_Pi_Motor_Driver_Board_v1_0
prodimagename: Raspberry_Pi_Motor_Driver_Board_v1_0.jpg
wikiurl: http://seeed.wiki/Raspberry_Pi_Motor_Driver_Board_v1_0
sku: 110060161
---

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/1.jpg)

这款套件包含了 12 个精心挑选的 Grove 模块，10 根连线，以及一块专门为树莓派设计的 Grove 扩展板 -- GrovePi+。仅需将 GrovePi+ 堆叠在树莓派上，再把传感器连接到 GrovePi+ 上，就可以在树莓派这个强大的平台上开始玩起硬件并搭建原型啦 !

GrovePi+ 是一款即插即用的树莓派扩展板，它可以直接堆叠在树莓派上，用 I2C 接口建立通讯。所有的 Grove 模块都可以通过 Grove 线缆直接连接到 GrovePi+ 上的 Grove 接口，然后给树莓派编程，实现对 Grove 模块的控制和使用。


GrovePi+ 与 Raspberry Pi A+,B,B+/2,3 兼容

!!!Note
    Raspberry Pi 板不包括在内。新的 GrovePi+ 通过 CE 认证，与 Linux 和 Win 10 IoT 兼容。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.11891debBnV3Dd&id=45475491903)

## 产品特性
--------

*   7 个数字引脚

*   3 个模拟引脚

*   3 个 I2C 接口

*   1 个连接到 GrovePi 的串口

*   1 个连接到 Raspberry Pi 的串口

*   Grove 接口输出电压 : 5V 直流电压

##   入门指导
---------

**<big>GrovePi+ 快速入门</big>**

如果您想了解更多关于它是如何工作的，您可以在 [Github Repository](https://github.com/DexterInd/GrovePi) 找到所有的设计文件。

###   将 GrovePi+ 连接到 Raspberry Pi

首先将 GrovePi+ 安装在 Raspberry Pi 上。GrovePi+ 堆叠在 Raspberry Pi 的顶部，如下图所示。

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/2.jpg)

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/3.JPG)


堆叠 GrovePi+ 时，确保引脚对齐。


### 软件设置

接下来安装这个软件。有两个安装选项 :

*   You can use our BrickPi Image (使用 BrickPi 固件).

*   Use your own image.  If you already have your own flavor of linux running on the Raspberry Pi, you can use our bash script to setup for the GrovePi (使用个人固件。如果您已经在 Raspberry Pi 上运行 linux，您可以使用 bash 脚本来设置 GrovePi+).

**使用 BrickPi 固件**

*   下载 BrickPi Image 并安装到SD卡上。[这里是在 BrickPi 页面配置 SD 卡步骤的链接](http://www.dexterindustries.com/BrickPi/getting-started/pi-prep/)。此安装需要内存最少为 4GB 的 SD 卡。

*   在 Raspbian 的适当位置粘贴 Github repository。

```
git clone https://github.com/DexterInd/GrovePi.git
```

*   运行脚本文件夹中的 bash 脚本来配置 Raspbian。这里是[教程](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)。
*   重启 Raspberry Pi。

**配置个人固件**

*   在适当的位置粘贴 Github repository

```
git clone https://github.com/DexterInd/GrovePi.git
```

*   运行脚本文件夹中的 bash 脚本来配置 Raspbian。 这里是 [教程](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)。

*   重启 Raspberry Pi 并开始使用 GrovePi+。

###   测试 GrovePi+

将 Raspberry Pi 配置为与 GrovePi+ 配合使用后，就可以看到它的实际应用了。

## 产品清单
---------

| 产品名称                    | 数量 |
|-----------------------------|------|
| [Grove Pi+](http://seeed.wiki/GrovePi_plus)                   | 1    |
| [Grove - Rotary Angle Sensor](http://seeed.wiki/Grove-Rotary_Angle_Sensor/) | 1    |
| [Grove - Sound Sensor](http://seeed.wiki/Grove-Sound_Sensor/)        | 1    |
| [Grove - LCD RGB Backlight](http://seeed.wiki/Grove-LCD_RGB_Backlight/)   | 1    |
| [Grove - Temp&Humi Sensor](http://seeed.wiki/Grove-Temperature_and_Humidity_Sensor/)    | 1    |
| [Grove - Red LED](http://seeed.wiki/Grove-Red_LED/)             | 1    |
| [Grove - Blue LED](http://seeed.wiki/Grove-Red_LED/)            | 1    |
| [Grove - Green LED](http://seeed.wiki/Grove-Red_LED/)           | 1    |
| [Grove - Light Sensor](http://seeed.wiki/Grove-Light_Sensor/)        | 1    |
| [Grove - Buzzer](http://seeed.wiki/Grove-Buzzer/)              | 1    |
| [Grove - Relay](http://seeed.wiki/Grove-Relay/)               | 1    |
| [Grove - Button](http://seeed.wiki/Grove-Button/)              | 1    |
| [Grove - UItrasonic Ranger](http://seeed.wiki/Grove-Ultrasonic_Ranger/)   | 1    |
| Cables                      | 10   |
| GrovePi+ Guidebook          | 1    |

## 使用示例
---------
以下是使用 GrovePi+ 构建的一些有趣的项目。

###  Home Weather Display (家庭气象站)

在这个项目中，我们使用 Grove - Temp&Humi Sensor 作为 Raspberry Pi 温度传感器。该项目使用连接到 Raspberry Pi 的 Grove - LCD RGB Backlight 来显示温度和湿度。您可以按照设计使用这个项目 : 家庭气象站。

您也可以将此示例项目作为您自己项目的基础。该项目展示了如何在 Raspberry Pi 上使用温度计传感器，以及如何在没有监视器的情况下显示数据。您可以使用 Raspberry Pi 为您自己的数据记录项目调整或添加更多传感器。

这是一个简单的示例，用于演示如何在您的项目中使用 GrovePi+ 的多个 Grove 传感器。

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/4.jpg)
家庭气象站

####  器材准备

1.  Raspberry Pi
2.  GrovePi+
3.  Grove - Temp&Humi Sensor
4.  Grove - RGB LCD display
5.  Grove Connection wires
6.  SD card and WiFi module

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/5.jpg)

####  硬件连接

将 Grove - Temp&Humi Sensor 连接到 **D7**，将 Grove - RGB LCD display 连接到任意 I2C 端口。然后给 Raspberry Pi 上电。

#### 运行程序

在 Raspberry Pi 终端中，将目录更改为 GrovePi/Projects/Home_Weather_Display :

```
cd /home/pi/Desktop/GrovePi/Projects/Home_Weather_Display
```

在目录中，以 root (sudo) 运行示例 python 程序中的 Home_Weather_Display.py :

```
sudo python Home_Weather_Display.py
```

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/6.jpg)
来自 Raspberry Pi 的温湿度信息。

![](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/img/7.jpg)
Grove - RGB LCD display 将开始显示来自 Grove - Temp&Humi Sensor 的实时温度数据和湿度数据。

#### 源码

示例源码点击 [这里](https://github.com/DexterInd/GrovePi/blob/master/Projects/Home_Weather_Display/Home_Weather_Display.py) 获取

点击 [这里](https://www.dexterindustries.com/grovepi-tutorials-documentation/) 获取更多的使用示例

## 资源下载
---------
-   **[Eagle 文件]** [GrovePi_Plus V3.0 eagle file](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/res/GrovePi%2BEagle%20FIle.zip)
-   **[原理图 PDF]** [GrovePi_Plus V3.0 schematics pdf file](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/res/GrovePi%2B%20v3.0%20Sch.pdf)
-   **[PCB图 PDF]** [GrovePi_Plus V3.0 PCB pdf file](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/res/GrovePi%2B%20v3.0%20PCB.pdf)
-   **[其他资源]** [Setting_Up_Software_for_GrovePi](https://github.com/SeeedDocument/GrovePi-Starter-Kit-for-Raspberry-Pi-A-B-B-2-3-CE-certified-/raw/master/res/Setting_Up_Software_for_GrovePi.pdf)
-   **[其他资源]** [GrovePi+ Github](https://github.com/DexterInd/GrovePi.git)
-   **[其他资源]** [Raspberry Pi 兼容 Grove 传感器](https://www.dexterindustries.com/GrovePi/supported-sensors/?PageSpeed=noscript)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Motor_Driver_Board_v1.0 -->
