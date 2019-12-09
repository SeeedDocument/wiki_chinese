---
name: 7 inch 720x1280 HDMI IPS LCD Display
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/7-inch-720-1280-HDMI-IPS-LCD-Display-p-2861.html
wikiurl:
sku: 104990443
---

![](https://media-cdn.seeedstudio.site/media/catalog/product/cache/ab187aaa5f626ad16c8031644cd2de5b/d/e/demo7.jpg)

在这里，我们为您提供这种高分辨率，超宽视角IPS HDMI显示器。具体地说，此显示器的分辨率为720 * 1280，视角高达178度的两倍。它小巧轻便，便于携带。无需驱动程序。我们使用树莓派3b/3b+/4b+和Windows10对其进行了测试。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a2oq0.12575281.0.0.39af1debtp7vqs&ft=t&id=601830334921&qq-pf-to=pcqq.c2c)

##  产品特性
--------

-   它支持720 * 1280分辨率
-   易于识别。
-   超薄
-   高视角
- 可以在Raspberry Pi背面组装

##  规格参数
--------

| 参数             | 值                                                                             |
|------------------|--------------------------------------------------------------------------------|
| 尺寸             | 7 寸                                                        |
| 分辨率           | 720x1280                      |
| 刷新频率         | 60HZ                                                                        |                                          |
| 电源             | 标准Micro usb接口                                                                 |
| 工作电流         | 5v  360mA                                            |
| 接口             |          HDMI2.0 (兼容 HDMI1.4)    |

##  配送清单

| 零件名称                     | 数量 |
|------------------------------|------|
| IPS LCD 屏幕 | 1    |
| HDMI2.0 线|1|
| Micro USB 线|1|
| 后支架 |1|
|树莓派安装螺丝袋|1|

![](https://media-cdn.seeedstudio.site/media/catalog/product/cache/ab187aaa5f626ad16c8031644cd2de5b/4/_/4.jpg)
##  硬件概述
-----------------

![](https://github.com/SeeedDocument/Pi_screen/raw/master/7inch.jpg)

##  使用方法
-----

### 与 Raspberry Pi4 一起使用

- 第一步.修改`config.txt`文件
如果您使用的是 Raspberry Pi 4，您可以通过以下步骤更改方案：

假如你使用的是7寸的显示器，登录到您的 Raspberry Pi，然后编辑 /boot/config.txt file，确保它有以下参数 :

```

hdmi_pixel_freq_limit=400000000 
hdmi_group=2
hdmi_mode=87 
hdmi_force_hotplug=1
config_hdmi_boost=4
disable_overscan=1
hdmi_ignore_edid=0xa5000080
hdmi_timings=720 0 100 24 52 1280 0 10 4 4 0 0 0 60 0 70000000 0 
max_framebuffer_width=1280 
max_framebuffer_height=1280  
framebuffer_width=1280 
framebuffer_height=720

```

假如你使用的是10寸的显示器，，登录到您的 Raspberry Pi，然后编辑 /boot/config.txt file，确保它有以下参数 :

```

hdmi_pixel_freq_limit=400000000 
hdmi_group=2
hdmi_mode=87 
hdmi_force_hotplug=1
config_hdmi_boost=4
disable_overscan=1
hdmi_ignore_edid=0xa5000080
hdmi_timings=1200 0 100 24 52 1920 0 65 4 25 0 0 0 60 0 169000000 0
max_framebuffer_width=1920
max_framebuffer_height=1920
framebuffer_width=1920
framebuffer_height=1200

```


- 第二步.重启并旋转屏幕

完成上面操作后，你只需要重启系统应该就可以看到树莓派的桌面在屏幕上面显示了

![](https://projects-static.raspberrypi.org/projects/raspberry-pi-setting-up/e22d152dd4f5bee4e6c932d716bc74c6a2098b69/en/images/pi-desktop.png)

假如屏幕是竖屏显示的，我们只需要按照下图的说明，旋转成横屏即可

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry-4-get-start/master/img/Screen-Config.jpg)

### 与 Raspberry Pi3/3b+ 一起使用

直接按照下面的文档说明操作即可
[树莓派3操作指南](https://docs.google.com/viewer?url=https://github.com/SeeedDocument/Pi_screen/raw/master/Instructions_for_use.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Relay_Board_v1.0 -->
