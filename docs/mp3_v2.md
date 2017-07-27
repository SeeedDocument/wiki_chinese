## 简介

Grove – MP3 V2.0是一款外形小巧，设计紧凑的音频模块。本模块支持多种格式的播放，MP3, WAV以及WMV灯。并支持多种播放模式，随机播放，循环播放以及单曲循环等。Grove – MP3 V2采用串口通信协议，可以使用于任何具有串口的主控板，例如Arduino, Raspberry, LaunchPad等主流的开源硬件开发板。另外，模块上集成有micro-SD卡槽以及3.5mm音频插孔，为你音频方面的应用带来极大的便利。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_MP3/1.jpg)

## 特性

* 内置基本的音频操作
* 半载micro-SD卡槽以及3.5mm音频插孔
* 多种采样率支持，8/11.025/12/16/22.05/24/32/44.1/48K
* 24位DAC高精度输出，最大90dB动态输出@85dB SNR
* 支持多种音频格式，MP3, WAV, WMV灯
* 10种均衡模式

## 规格参数

|参数|数值|
|----|----|
|电源输入|	5V|
|工作电流（无信号输出）|	<15mA|
|工作电压	|<40mA|
|芯片	|KT403A|
|支持音频格式	|MP3, WAV, WMA|
|最大支持SD卡容量	|32GB|
|采样率	|8/11.025/12/16/22.05/24/32/44.1/48K|

## 硬件概览

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_MP3/2.jpg)


## 产品清单

|物品名称|数量|
|---------|---|
|Grove – MP3 V2.0模块|	1|
|Grove连接线	|1|

## 快速入门

我们提供一个小例程，帮助你快速的把Grove – MP3 V2.0使用起来，有下面的几个步骤。

### 需要的材料

你需要准备一些材料，如下：

* Seeeduino x 1，主控板，你也可以使用其他的Arduino开发板，例如Arduino UNO, Ardduino Leonardo等等
* Grove – Base Shield V2 x 1
* Grove – MP3 V2模块
* Micro SD卡（需要把音频文件放置到该SD卡中）
* Micro USB线
* 耳机，或者音箱

### 准备工作

我们这里需要用到Arduino IDE作为下载工具。如果这是你第一次听说Arduino，那么你可以点击下面的链接获得关于Arduino的信息。另外，Seeeduino是一款与Arduino UNO完全兼容的开发板。

!!! tip "Arduino入门"
    如果这是你第一次使用Arduino, 可以通过以下两个链接获得Arduino的入门教程
    
    * [针对Windows的入门教程](http://www.seeedstudio.com/wiki/Seeeduino_v4.2#Getting_Started_on_Windows)
    * [针对OSX的入门教程](http://www.seeedstudio.com/wiki/Seeeduino_v4.2#Getting_Started_on_Mac_OS_X)

### 硬件连接
请按照下图把模块接好。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_MP3/3.jpg)


### 烧录代码

1. 到[这里](https://github.com/Seeed-Studio/Grove_Serial_MP3_Player_V2.0)下载驱动库。
2. 把下载的驱动库放到Arduino IDE的[libraries文件夹](http://www.seeedstudio.com/wiki/Guide_to_use_demos_downloaded_from_Seeed%27s_Github)
3. 打开MP3_Play_Test的example
4. 把代码烧录到Seeeduino
5. 然后，你就可以听到每秒的音乐了。

## 资源下载
* [原理图](http://www.seeedstudio.com/wiki/images/1/11/Grove_-_MP3_v2.0_Schematic_files.zip)
* [驱动库](https://github.com/Seeed-Studio/Grove_Serial_MP3_Player_V2.0)
* [如何下载一个Gihub的驱动库](http://www.seeedstudio.com/wiki/Guide_to_use_demos_downloaded_from_Seeed%27s_Github)
* [KT403A Datasheet (part)](http://www.seeedstudio.com/wiki/images/c/c0/Grove_-_MP3_v2.0_KT403A_datasheet_V1.3_EN%28Recompiled_by_Seeed%29.pdf)
