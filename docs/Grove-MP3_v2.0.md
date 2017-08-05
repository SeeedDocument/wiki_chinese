---
title: Grove - MP3 v2.0
category: Actuator
bzurl: https://seeedstudio.com/Grove-MP3-v2.0-p-2597.html
oldwikiname: Grove_-_MP3_v2.0
prodimagename: Grove-MP3_v2.0_Product_View_700_S.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/107020008 2.jpg
surveyurl: https://www.research.net/r/Grove-MP3_v2_0
sku: 107020008
tags: plat_duino, plat_pi, plat_bbg, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/img/Grove-MP3_v2.0_Product_View_700_S.jpg)

## 简介

Grove – MP3 V2.0是一款外形小巧，设计紧凑的音频模块。本模块支持多种格式的播放，MP3, WAV以及WMV灯。并支持多种播放模式，随机播放，循环播放以及单曲循环等。Grove – MP3 V2采用串口通信协议，可以使用于任何具有串口的主控板，例如Arduino, Raspberry, LaunchPad等主流的开源硬件开发板。另外，模块上集成有micro-SD卡槽以及3.5mm音频插孔，为你音频方面的应用带来极大的便利。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797rUlXRn&id=528296284801)

版本更新
---------------
| 产品版本  | 发布时间   | 当前支持状态 |
|-------------------|----------------|----------------|
| Version 1.0       | 2013 04 28  | 支持      |
| Version 2.0       | 2015 11 15    | 支持      |

产品特性
--------

* 内置基本的音频操作
* 半载micro-SD卡槽以及3.5mm音频插孔
* 多种采样率支持，8/11.025/12/16/22.05/24/32/44.1/48K
* 24位DAC高精度输出，最大90dB动态输出@85dB SNR
* 支持多种音频格式，MP3, WAV, WMV灯
* 10种均衡模式

!!!note
    - 更多关于Grove接口的信息请点击下面链接 [Grove System](http://wiki.seeed.cc/Grove_System/)

创意应用
-----------------

-   适合各种音频应用的中间解决方案.

规格参数
-------------

| 参数                                  | 数值                                                                                                             |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 输入                                      | 5 V (DC)                                                                                                          |
| 工作电流 (无信号输出时) | < 15 mA                                                                                                   |
| 工作电流                          | < 40 mA                                                                                                   |
| 主控芯片                                      | KT403A [(datasheet)](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/res/Grove-MP3_v2.0_KT403A_datasheet_V1.3_EN-Recompiled_by_Seeed-.pdf) |
| 芯片输出电压                    | 3.3 V                                                                                                             |
| 芯片输出电流                        | 100mA(at Max.)                                                                                                    |
| 支持音频格式                     | MP3, WAV, WMA                                                                                                     |
| 支持SD卡最大容量      | 32 GB                                                                                                             |
| 采样频率                              | 8 / 11.025 / 12 / 16 / 22.05 / 24 / 32 / 44.1 / 48(KHz)                                                           |


支持平台
-------------------
Arduino, Raspberrypi, bbg, linkitone

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/img/Grove-MP3_v2.0_Component_view-front-1200_S.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/img/Grove-MP3_v2.0_Component_View-Back-1200_S.jpg)

### **产品清单**

| 组件名称              | 数量 |
|-------------------------|----------|
| Grove - MP3 v2.0        | 1PC      |
| Grove - Universal Cable | 1PC      |

入门指导
-----------

#### 需要的素材

-   Seeeduino × 1
-   Grove - Base Shield v2 × 1
-   Grove - MP3 v2.0 × 1
-   装有音频文件的SD卡 × 1
-   USB 适配线 (type A to micro type-B) × 1
-   带有3.5mm接口的耳机或音箱 × 1

### 准备工作

在开始之前，您需要点击下面的指南来搭建好您的IDE编译工具:.

[Windows系统IDE指南](/Seeeduino_v4.2#Getting_Started_on_Windows)

[Mac OS X IDE指南](/Seeeduino_v4.2#Getting_Started_on_Mac_OS_X)


<div class="admonition note">
<p class="admonition-title">提示</p>
我们选取的Seeeduino作为此实例的开发板，但是您也可以选用Arduino的开发板来实现所有功能，他们是完全兼容的。
</div>


### 硬件连接图

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/img/Grove-MP3_v2.0_Demo_connection_1200_S.jpg)

### 软件
如果您是第一次安装Arduino库文件，请点击 [这里](http://seeed.wiki/How_to_install_Arduino_Library/) 查看库文件的安装方法。


!!!tip
    - 如果您不清楚怎么下载代码到您的板子里，请点击[这里](http://seeed.wiki/Upload_Code/)。


#### 烧录例程


1. 到 [这里](https://github.com/Seeed-Studio/Grove_Serial_MP3_Player_V2.0) 下载驱动库。
2. 把下载的驱动库放到Arduino IDE的 [libraries](http://www.seeedstudio.com/wiki/Guide_to_use_demos_downloaded_from_Seeed%27s_Github) 文件夹
3. 打开MP3_Play_Test的example，把代码烧录到Seeeduino
4. 打开串口监视器（Ctrl + Shift + M），发送命令播放音乐


资源下载
---------

- **[硬件原理图]** Hardware [Schematic files](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/res/Grove-MP3_v2.0_Schematic_files.zip)
-   **[库]**[Libraries](https://github.com/Seeed-Studio/Grove_Serial_MP3_Player_V2.0) on Github.
-  **[数据手册]** KT403A [Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-MP3_v2.0/master/res/Grove-MP3_v2.0_KT403A_datasheet_V1.3_EN-Recompiled_by_Seeed-.pdf) (part)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_MP3_v2.0 -->
