---
title: GrovePi+
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/GrovePi%2B-p-2241.html
oldwikiname:  GrovePi+
prodimagename:  GrovePi_Wiki_1.JPG
wikiurl: http://seeed.wiki/GrovePi_Plus
sku:     103010002
---
![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/110060049%2010_02.jpg)

[GrovePi](http://www.dexterindustries.com/GrovePi/) 是一个 [Raspberry Pi](http://www.seeedstudio.com/depot/s/Raspberry%2520Pi.html?search_in_description=0) 的扩展板，可以用来连接各种 [Grove Sensors](/GROVE_System "GROVE System")。 作为 [GrovePi](http://www.seeedstudio.com/depot/GrovePi-p-1672.html) 的新版本，它支持新型号的 RaspberryPi A+ 和 B+。它有三个安装孔可以完美匹配所有版本的 Raspberry Pi，同时配有相机电缆出口孔。它还改进了电压电平转换子电路。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.27eb8853k9ae6w&id=45506190895)

##   产品特性
---
*   7 个数字端口

*   3 个模拟端口

*   3 个 I2C 端口

*   1 个串口连接到 GrovePi

*   1 个串口连接到 Raspberry Pi

*   Grove 接口 Vcc 输出电压: 5V DC

##   开始使用
---
**<big>欢迎来到 GrovePi+ 的快速入门教程</big>**

如果你想了解更多，您可以访问 [Github Repository](https://github.com/DexterInd/GrovePi) 以获得更多的资源。

###   把 GrovePi 连接到 Raspberry Pi

First, 把你的 GrovePi 组装在 Raspberry Pi 上。按下图所示，对准 GrovePi 和 Raspberry Pi 的顶部，缓慢插入 GrovePi。

![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/GrovePiPlus_wiki_3.jpg)

![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/GrovePi_Wiki_1.JPG)


!!!note
  确保在安装 GrovePi 时针脚正确对齐。



###   在 Raspberry Pi 上安装软件

接下来我们将在 Raspberry Pi 上安装该软件。 有两个安装选项：

*   您可以使用我们的 BrickPi Image。

*   使用自己的固件。 如果您已经拥有自己的 Raspberry Pi 上运行的 linux 风格，可以使用我们的 bash 脚本来设置 GrovePi。

**使用 BrickPi Image**

*  下载 Brick Pi Image 并在你的 SD 卡中安装。[点击这里，按照 BrickPi 页面的步骤来配置SD卡](http://www.dexterindustries.com/BrickPi/getting-started/pi-prep/)。  您需要至少 4GB 的 SD 卡来进行安装。

*   在 Raspbian 的适当位置上克隆 Github 仓库。

```
git clone https://github.com/DexterInd/GrovePi.git
```

*   在脚本文件夹中运行bash脚本来配置Raspbian。[这里是使用脚本设置的教程。](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)

*   重启 Raspberry Pi。

**配置自己的 Image**

*   在适当的位置克隆 Github 仓库。

```
git clone https://github.com/DexterInd/GrovePi.git
```

*  在脚本文件夹中运行 bash 脚本来配置 Raspbian 。 [这里](http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/) 是使用脚本设置的教程。

*   重启 Raspberry Pi 然后就可以使用 Grove Pi 了。

###   测试 GrovePi

当您将 Raspberry Pi 配置为与 GrovePi 配合使用后，就可以看到它在运行。

我们已经开发了三个简单的项目来说明 GrovePi 的工作原理。

##   支持的产品
---
###   Grove 清单

*   [1. Grove - Button ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5e26f7a80QNXrv&id=532955584350)

*   [2. Light Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.3b61cb03tdB9ph&id=544373791068)

*   [3. Buzzer](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.460800e6ONwbkD&id=520245748676)

*   [4. Sound Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1f82ef71voHxXr&id=45507318433)

*   [5. Grove - Red LED ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.42.1c81bc13Pk5xch&id=45476819992)

*   [6. Grove - Blue LED ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.44.1c81bc13Pk5xch&id=531838541569)

*   [7. Grove - Green LED ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.34.1c81bc13Pk5xch&id=534288793023)

*   [8. LCD RGB Backlight ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.46274ca01Xm7BY&id=45475311124)

*   [9. Rotary Angle Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.faf9500sWtQ5L&id=45554377762)

*   [10. Temperature Humidity Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.17db0ba8YxIqXZ&id=520506479798)

*   [11. Ultrasonic Ranger Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.1e68d1c1JampD4&id=45550924107)

*   [12. Relay](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.16765e1cqPC0Xh&id=45670971061)


##   资源下载
---
-   **[Eagle 文件]** [GrovePi_Plus V3.0 eagle file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2BEagle%20FIle.zip)
-   **[PDF 文件]** [GrovePi_Plus V3.0 schematics pdf file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2B%20v3.0%20Sch.pdf)
-   **[PDF 文件]** [GrovePi_Plus V3.0 PCB pdf file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2B%20v3.0%20PCB.pdf)
-   **[PDF 文件]** [Setting_Up_Software_for_GrovePi](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/Setting_Up_Software_for_GrovePi.pdf)
