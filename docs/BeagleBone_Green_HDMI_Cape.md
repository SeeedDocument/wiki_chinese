---
title: BeagleBone Green HDMI Cape
category: BeagleBone
bzurl: https://seeedstudio.com/SeeedStudio-BeagleBone-Green-HDMI-Cape-p-2570.html
oldwikiname: BeagleBone_Green_HDMI_Cape
prodimagename: BeagleBone_Green_HDMI_Cape.jpg
wikiurl: http://seeed.wiki/BeagleBone_Green_HDMI_Cape
tags: plat_bbg
sku: 103030034
---

![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/BeagleBone_Green_HDMI_Cape.jpg)

**BeagleBone Green HDMI Cape** 是一块 HDMI 显示扩展板，可以方便的接到 BBG 上，从而极大的拓宽 BBG 的应用场景，例如 DIY 小型电脑，投影仪，数字电视或者数字音频设备。此款扩展板可以连接到任何标准 HDMI 接口的显示设备。支持所有的高清信号，输出分辨率为 1280x720。同时，该扩展板也可以用来单独传输音频信号。该产品将使您基于 BeagleBone board 的应用在不同情况下具有更多功能。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.678ab188a3UM6k&id=527711785332)

## 产品特性
--------

-   即插即用。
-   适应不同的输入信号。
-   720P(1280×720) 输出分辨率。

## 规格参数
-------------

| 参数                | 值                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| 输入电压            | 5V/3.3V                                                                                                |
| 最大工作电流 | 80 mA                                                                                                  |
| HDMI 版本             | Version 1.2                                                                                            |
| 最大输出分辨率 | 1280x720 @60Hz                                                                                         |
| 音频传输       | Available                                                                                              |
| 芯片组                     | IT66121 HDMI Framer([Datasheet](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/res/IT66121FN_Datasheet_v1.02.pdf)) |

## Platforms Supported
-------------------

## 创意应用
-----------------

您可以将 BeagleBone 扩展到更多的多媒体外围设备，如电脑显示器，视频投影仪，数字电视或数字音频设备。

## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/BeagleBone_Green_HDMI_Cape_Componentss.jpg)


**IT66121 HDMI Framer**

   - HDMI 控制 IC

**Cape I2C address Switch**

   - I2C 地址配置开关

**Cape EEPROM**

   - 缓存器

**HDMI 连接器**

### 产品清单

|                            |          |
|----------------------------|----------|
| **零件名**             | 数量 |
| BeagleBone Green HDMI Cape | 1        |

## 入门指导
-----------

***本部分将通过几个步骤向您介绍如何开始使用该产品。***

### 准备工作

-   BeagleBone Green board (带 OS [安装](http://beagleboard.org/getting-started)) × 1.
-   USB 线 (type A to micro type B) × 1.
-   Standard HDMI 线缆 (type A to type A) × 1.

### 硬件连接

![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/BeagleBone_Green_HDMI_Cape_Connection_1200_s.jpg)

<div class="admonition note">
<p class="admonition-title">Note</p>
在本示例中，我们使用的是 Windows 7 操作系统。连接工作完成后，将电脑鼠标插入 BeagleBone Green board 上的 USB 接口。
</div>

将 USB 数据线 (C 型) 连接到电脑，您会发现计算机显示器上显示了 BeagleBone 桌面。

那么你可以像使用 PC 或 Mac 一样使用 BeagleBone。

![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/Bbb_vnc.jpg)

#### 故障排除

1. 电脑显示器上不显示 BeagleBone 桌面操作系统? 尝试以下步骤之一。

    - 关闭显示器并重新启动。
    - 按下 BeagleBone Green board 上的 RESET 按钮。
    - 按下 BeagleBone Green board 上的电源按钮，然后再次按下。


    ![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/Beaglebone-Green_s.jpg)

2. 电脑鼠标不工作 (不供电)？
    -   按下 BeagleBone Green board 上的 RESET 按钮，等待启动。

3. 如何快速拆卸  BeagleBone Green HDMI Cape?
    -   先用手拉出 HDMI 插座的一端，然后拉出另一端。如果有必要，重复前两个步骤。

## 演示
----

本 [视频](https://www.youtube.com/watch?v=-xvbXSd_9TY&feature=youtu.be) 演示如何使用   BeagleBone Green HDMI Cape 上网和播放音频。

## 资源下载
---------

- **[原理图]** [Schematic files](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/res/Schematic_Files.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/BeagleBone_Green_HDMI_Cape -->
