---
name:  Green LCD Cape with Resistive Touch
category: BeagleBone
bzurl: https://www.seeedstudio.com/5-Inch-BeagleBone-Green-LCD-Cape-with-Resistive-Touch-p-2642.html
oldwikiname: BeagleBone_Green_HDMI_Cape
prodimagename: BeagleBone_Green_HDMI_Cape.jpg
wikiurl: http://wiki.seeedstudio.com/cn/BeagleBone_Green_HDMI_Cape
tags: plat_bbg
sku: 104990262
---

![](https://www.seeedstudio.site/media/catalog/product/cache/ef3164306500b1080e8560b2e8b5cc0f/h/t/httpsstatics3.seeedstudio.comseeedimg2016-08ddkssqrw2lfthpq0phlecp1r.jpg)

**Green LCD Cape with Resistive Touch** 采用紧凑型5英寸液晶显示屏，适用于SeeedStudio Beagle bone® Green 或 Beagle bone Black。尺寸略小于7英寸版本，但它仍然具有800x480分辨率的图形显示和一层4线电阻式触摸屏，用于用户交互。设置起来非常简单，因为您只需要通过2x46针头将其直接连接到SeeedStudioBeaglebone®Green/Beaglebone®Black，这将提供斗篷需要的所有电源和显示信号。另外，您可以通过背面的内置微型USB为Cape供电。屏幕下方是一组按钮 - 左，右，上，下和ENTER，它们提供了另一种与屏幕交互的方式。此外，两个LED用于指示电源和用户状态。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.15.4e2533dbJTz1bd&id=592870112931)

## 产品特性

--------

- 分辨率高达800 x 480
- 电阻式触摸
- 5个按钮包括LEFT，RIGHT，UP，DOWN和ENTER
- 支持Debian
- ULP（超低功耗）消耗背光
- 4 x 3mm安装孔
- 内置USB供电

## 规格参数

-------------

| 参数                | 值                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| 大小            | 200mm x130mm x50mm                                                                                              |
| 重量 | G.W 120g                                  |
|工作电压|5V |
|工作电流|110mA |
|功率|0.55W |


## 创意应用

-----------------

您可以将 BeagleBone 在任何地方进行显示

## 硬件概述
-----------------

![](https://www.seeedstudio.site/media/catalog/product/cache/ef3164306500b1080e8560b2e8b5cc0f/h/t/httpsstatics3.seeedstudio.comseeedimg2016-08za8h5rzwtbm1lq3n3oydkcxp.jpg)


**SN74HC245**

   - IO驱动阔流

**Cape I2C 地址开关**

   - I2C 地址配置开关

**CAT4139TD**

   - 背光恒流稳压


### 产品清单

|                            |          |
|----------------------------|----------|
| **零件名**             | 数量 |
|  Green LCD Cape with Resistive Touch | 1        |

## 入门指导
-----------

***本部分将通过几个步骤向您介绍如何开始使用该产品。***

### 准备工作

- BeagleBone Green board 或者 BeagleBone black board(带 OS [安装](http://beagleboard.org/getting-started)) × 1.
- USB 线 (type A to micro type B) × 2.

### 硬件连接

![](https://www.seeedstudio.site/media/catalog/product/cache/ef3164306500b1080e8560b2e8b5cc0f/h/t/httpsstatics3.seeedstudio.comseeedimg2016-086yqt2uwelst8w5mwuaklys12.jpg)

<div class="admonition note">
<p class="admonition-title">Note</p>

为了有足够的驱动 BeagleBone Green board 和  Green LCD Cape with Resistive Touch需要分别接上USB.

</div>

### 软件配置

1.打开设备管理器看查看BeagleBone Green board的com口

![](https://github.com/SeeedDocument/BBG-LCD-Cape-with-Resistive-Touch/raw/master/img/com-show.png)

2.使用标记的com口通过putty进入BeagleBone Green board系统

![](https://github.com/SeeedDocument/BBG-LCD-Cape-with-Resistive-Touch/raw/master/img/putty-config.png)

账号：debian,密码 temppwd

![](https://github.com/SeeedDocument/BBG-LCD-Cape-with-Resistive-Touch/raw/master/img/BBG-start.png)

3.修改`/boot/uEnv.txt `里面的配置文件

假如是7寸的就修改为

![](https://github.com/SeeedDocument/BBG-LCD-Cape-with-Resistive-Touch/raw/master/img/7-inch-config.png)

假如是5寸就修改为

![](https://github.com/SeeedDocument/BBG-LCD-Cape-with-Resistive-Touch/raw/master/img/5-inch-config.png)

4.重新启动系统则可以LED闪烁，则可以看如下界面

![](https://raw.githubusercontent.com/SeeedDocument/BeagleBone_Green_HDMI_Cape/master/img/Bbb_vnc.jpg)

## 资源下载
---------

- **[原理图]** [Schematic files](http://statics3.seeedstudio.com/assets/file/bazaar/product/5INCH_BBG_00A2_SCH.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/BeagleBone_Green_HDMI_Cape -->
