---
title: 7 Inch 1024x600 Capacitive Touch Screen DIY Kit
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/7-Inch-1024x600-Capacitive-Touch-Screen-DIY-Kit-p-2932.html
oldwikiname:
prodimagename:
wikiurl: http://seeed.wiki/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit
sku: 104060007
---

![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/1.jpg)

这是一个全新的 DIY 工具包，它是一个奇妙的 HDMI 监视器，配有电容触摸屏和免驱动程序。我们增加了一个 CTP 驱动板，并提供了电容触摸屏，使它成为一个全新的套件。之后，您不需要校准您的触摸屏，并可触摸。它已经在树莓派、BB black,PC 还有 Mac 上测试过，并且表现优异，且即插即用。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.11891debC41Z4M&id=557841549985)



##  产品特性
--------
-   它支持 1024x600 分辨率并且支持接近 30fps，最大 60fps。
-   电容触摸功能使用户可以完全控制任何设备。
-   内置 EDID 信息设备，因此可驱动自由。
-   易于识别。
-   电容式 USB 触摸屏可以支持鼠标右键的功能和拖放功能。
-   它可以支持多点触摸，最多 10 点。(仅在 Windows 10 中进行测试)

##  规格参数
--------

| 参数             | 值                                                                             |
|------------------|--------------------------------------------------------------------------------|
| 尺寸             | 265mm x 165mm x 50mm                                                           |
| 质量             | G.W 410g                                                                       |
| 电池             | 排除                                                                         |
| 工作电压         | 5V (current requirement 2A), 9V@1.5A(推荐), 12V@1A                      |
| 额定功率         | 6-7W                                                                           |
| 信号输入         | AV + VGA + HDMI (HDMI 1.2)                                                     |
| 分辨率           | 1024 * 600                                                                     |
| 即插即用         | 免驱动                                                                       |
| OSD 语言         | 简体中文，繁体中文，英文，日文，韩文，西班牙文，法文，德文，意大利文，葡萄牙文 |
| 控制             | 多功能 OSD 操作，电位计调整亮度和色彩，利用成熟的程序清晰显示                                          |
| 支持图像上下翻转 | 图像 ADC 转换 4: 3 / 16: 9 显示                                             |

##  配送清单

| 零件名称                     | 数量 |
|------------------------------|------|
| 7 英寸 1024x600 高分辨率屏幕 | 1    |
| 7 英寸电容式触控面板           | 1    |
| HDMI/VGA/S-Video 视频驱动板  | 1    |
| CTP 驱动板                   | 1    |
| 键盘                         | 1    |
| 键盘线                       | 1    |
| 驱动板电源线                 | 1    |
| USB 触摸屏线                 | 1    |

![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/2.jpg)

##  硬件概述
-----------------

CTP 驱动板有两个 USB 端口，其中右侧是 USB 数据线。(两者都可用于您的触摸屏，其中一个应该连接到输出设备)

![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/3.jpg)
![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/4.jpg)

##  使用方法
-----

### 与 Raspberry Pi 一起使用

如果您使用的是 Raspberry Pi，您可以通过以下步骤更改方案：

登录到您的 Raspberry Pi，然后编辑 /boot/config.txt file，确保它有以下参数 :

```
hdmi_force_hotplug = 1
hdmi_group = 2
hdmi_mode = 87
hdmi_cvt 1024 600 60 3 0 0 0
```

保存并重新启动系统。

## 常见问题解答

如果触摸屏工作异常，请确保显示器 USB 端口连接到您的设备 (PC, Raspberry Pi, Beagle bone black 等)

!!!Note
    由于尚未在 android 操作系统中测试，我们不确定它是否可以在 android 系统下工作。

如果您发现屏幕在连接到设备时模糊不清，请检查驱动板背面的 FPC 电缆，在运送过程中它可能会松动。

![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/5.jpg)

您只需拔出 FPC 线缆模块，然后将 FPC 线缆插入其中，确保紧固并再次尝试。请小心对待这根 FPC 线缆，因为它连接到电路板并将触摸屏数据发送到电路板上的芯片。

![](https://github.com/SeeedDocument/7_Inch_1024x600_Capacitive_Touch_Screen_DIY_Kit/raw/master/img/6.jpg)

##  资源下载
---------
- **[图纸]** [CTP Mechanical Drawing](http://wiki.52pi.com/images/3/38/CTP-5710.pdf)
- **[图纸]** [TP Mechanical Drawing](http://wiki.52pi.com/images/1/11/Tp-mechanical.pdf)
- **[图纸]** [Video Driver Board Mechanical Drawing](http://wiki.52pi.com/images/b/ba/Outlinedrawing_7_1_1_1.jpg)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Relay_Board_v1.0 -->
