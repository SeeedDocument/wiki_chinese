---
title: Grove - Fingerprint Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Fingerprint-Sensor-p-1424.html
oldwikiname: Grove_-_Fingerprint_Sensor
prodimagename: Print_Sensor.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/Print Sensor.jpg
wikiurl: http://seeed.wiki/Grove-Fingerprint_Sensor
sku: 101020057
tags: grove_uart, io_5v, plat_duino, plat_linkit, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/Print_Sensor.jpg)

指纹传感器是一种光学指纹传感器，可以超级简单地增加指纹检测和验证的功能。该传感器带有一个高功率 DSP 芯片 AS601 可进行图像渲染，计算，特征查找和搜索。您也可以直接注册录入新的手指指纹，最多 162个 手指指纹可以存储到板载闪存中。且在镜头中有一个红色的 LED 在照片中亮起，通过它你可得知它的工作情况。它是易于使用和迄今为止最好的指纹传感器，您值得拥有。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7392149at0grL4&id=45506770989)

## 规格参数
-------------

-   电源电压 : 3.6~6.0 V
-   最大工作电流 : 120 mA
-   指纹成像时间 : 1.0 S
-   匹配模式 : Compare Mode 1:1
-   搜索模式 : 1:N
-   存储容量 : 162 模版
-   错误验收率 : 0.001% (安全级别 3)
-   错误拒收率 : 1.0% (安全级别 3)
-   波特率 : 9600, 19200, 28800, 38400, 57600bps (默认 57600)
-   接口 : TTL 串行
-   工作温度 : -20 ~ +50 ℃
-   接口

| 引脚数 | 名称 | 类型 | 功能描述                                     |
|------------|------|------|----------------------------------------------------------|
| 1          | Vin  | in   | 正电源输入端子（线路颜色 : 红色）     |
| 2          | TD   | out  | 串行数据输出，TTL逻辑电平（线路颜色 : 黄色） |
| 3          | RD   | in   | 串行数据输入，TTL逻辑电平（线路颜色 : 白色）   |
| 4          | GND  | -    | 信号地（线路颜色 : 黑色）                         |

Platforms Supported
-------------------

## 入门指导
-------------

指纹传感器模块通常用于安全部门，它有一个高功率 DSP 芯片进行图像渲染，计算，特征查找和搜索。它可以连接到具有 TTL 串行的任何微控制器或系统，并发送数据包以拍照，检测打印，散列和搜索。您还可以直接录入新的手指指纹，最多可以存储 162 个指纹在板载闪存中。透镜中有一个红色的 LED，在拍摄照片时会点亮，以便您了解其工作状态。

-   将传感器连接到 [Grove - Base Shield](/Base_Shield_V2 "Grove - Base Shield") 的数字端口 2。
-   将 Grove - Base Shield 插入 Arduino，并使用 USB 线将 Arduino 连接到 PC。

当插入电源时，您会看到红色 LED 闪烁，这表示传感器正在工作。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/FingerPrint_Sensor1.jpg)

-   下载 [Finger Print Sensor Library](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/res/Fingerprint_library.rar) 并通过路径 : **..\\arduino-1.0.1\\libraries** 将其解压缩到 Arduino IDE 的库文件中。

这个库文件可以登记和搜索，因此它适用于任何项目。 它可以帮助您在 10 分钟内得到运行。 使用光学指纹传感器主要有两个要求。 首先，您需要登记指纹 - 这意味着为每个指纹分配 ID \#'s，以便以后查询。 一旦您登记了您所有的指纹，您就可以轻松地“搜索”传感器，要求它哪一个 ID (如果有)目前已被录入。

-   通过路径直接打开注册码 : **File->Example->FingerPrint->Enroll**。
-   上传代码到 Arduino。
-   启动串行工具并选择 Arduino 使用的 ComNum 和 BaudRate。
-   选择 "SendNew" 选项，发送您想使用的 ID \#，您最多可以使用 162 个 ID 号，并且会要求您将手指按在传感器上。此时您应该会看到红色的LED闪烁。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/FingerPrint_Sensor3.jpg)
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/Finger1.jpg)

-   如果您的按压足够，您会看到以下消息。然后，您必须重复该过程，用同一个手指以获得第二个干净的指纹。成功后，您将看到消息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/Finger2.jpg)

-   如果有指纹录入不成功的问题，你必须再次做。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/Finger_Print_Score_2.jpg)

一旦你录入了指纹，最好做一个快速测试，以确保它可以在数据库中找到。

-   打开演示代码 : **fingerprint** 并上传。
-   出现提示时，用其他/相同的手指按压传感器。如果是同一个手指，则应该与 ID \# 匹配，如下所示。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/img/Finger_Print_Score_3.jpg)

-   如果数据库中没有指纹，该串行端口将不会输出任何内容。

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](
http://seeed.wiki/Grove_System/)

## 资源下载
--------

- **[库文件]** [Finger Print Sensor Library File](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/res/Fingerprint_library.rar)
- **[芯片数据手册]** [ZhianTec ZFM-206 Series Datasheet (for this version, but in Simplified Chinese)](https://raw.githubusercontent.com/SeeedDocument/Grove-Fingerprint_Sensor/master/res/ZFM206用户手册V2.1.pdf)
- **[芯片数据手册]** [ZhianTec ZFM-20 Series Datasheet (for older series, but in English)](https://github.com/SeeedDocument/Grove-Fingerprint_Sensor/raw/master/res/ZFM-user-manualV15.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Fingerprint_Sensor -->
