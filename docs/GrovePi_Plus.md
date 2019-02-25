---
name: GrovePi+
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/GrovePi%2B-p-2241.html
oldwikiname:  GrovePi+
prodimagename:  GrovePi_Wiki_1.JPG
wikiurl: http://wiki.seeedstudio.com/cn/GrovePi_Plus
sku:     103010002
---
![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/110060049%2010_02.jpg)

[GrovePi](http://www.dexterindustries.com/GrovePi/) 是将 [Grove Sensors](/GROVE_System "GROVE System") 引入 [Raspberry Pi](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.2a6a4c472NbhKT&id=528322046763) 的扩展板。作为 [GrovePi](https://item.taobao.com/item.htm?spm=a230r.1.14.16.6044a066Efadnl&id=45475491903&ns=1&abbucket=1#detail) 的新版本。它支持新的 RaspberryPi Model B+ 和 Model A+。有三个安装孔可以完美匹配所有版本的 Raspberry Pi，它们都是相机线缆出口孔。它还改善了电压电平转换子电路。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.27eb8853k9ae6w&id=45506190895)

##   产品特性
---
*   7 个数字引脚

*   3 个模拟引脚

*   3 个 I2C 接口

*   1 个连接到 GrovePi 的串口

*   1 个连接到 Raspberry Pi 的串口

*   Grove 接口输出电压 : 5V 直流电压

##   入门指导
---
**<big>GrovePi+ 快速入门</big>**

如果您想了解更多关于它是如何工作的，您可以在 [Github Repository](https://github.com/DexterInd/GrovePi) 找到所有的设计文件。

###   将 GrovePi+ 连接到 Raspberry Pi

首先将 GrovePi+ 安装在 Raspberry Pi 上。GrovePi+ 堆叠在 Raspberry Pi 的顶部，如下图所示。

![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/GrovePiPlus_wiki_3.jpg)

![](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/img/GrovePi_Wiki_1.JPG)


堆叠 GrovePi+ 时，确保引脚对齐。


### 软件设置

接下来安装这个软件。有两个安装选项 :

*   You can use our BrickPi Image(使用 BrickPi 固件).

*   Use your own image.  If you already have your own flavor of linux running on the Raspberry Pi, you can use our bash script to setup for the GrovePi(使用个人固件。如果您已经在 Raspberry Pi 上运行 linux，您可以使用 bash 脚本来设置 GrovePi+).

**使用 BrickPi 固件**

*   下载 BrickPi 固件 并安装到SD卡上。[这里是在 BrickPi 页面配置 SD 卡步骤的链接](http://www.dexterindustries.com/BrickPi/getting-started/pi-prep/)。此安装需要内存最少为 4GB 的 SD 卡。

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

我们开发了三个简单的项目来说明 GrovePi+ 是如何工作的。

##   零件清单
---
###   Grove 系列零件

*   [1. Grove - Button ](http://wiki.seeedstudio.com/cn/Grove-Button/)

*   [2. Light Sensor](http://wiki.seeedstudio.com/cn/Grove-Light_Sensor/)

*   [3. Buzzer](http://wiki.seeedstudio.com/cn/Grove-Buzzer/)

*   [4. Sound Sensor ](http://wiki.seeedstudio.com/cn/Grove-Sound_Sensor/)

*   [5. Grove - Red LED ](http://wiki.seeedstudio.com/cn/Grove-Red_LED/)

*   [6. Grove - Blue LED ](http://wiki.seeedstudio.com/cn/Grove-Red_LED/)

*   [7. Grove - Green LED ](http://wiki.seeedstudio.com/cn/Grove-Red_LED/)

*   [8. LCD RGB Backlight ](http://wiki.seeedstudio.com/cn/Grove-LCD_RGB_Backlight/)

*   [9. Rotary Angle Sensor ](http://wiki.seeedstudio.com/cn/Grove-Rotary_Angle_Sensor/)

*   [10. Temperature Humidity Sensor ](http://wiki.seeedstudio.com/cn/Grove-Temperature_and_Humidity_Sensor/)

*   [11. Ultrasonic Ranger Sensor](http://wiki.seeedstudio.com/cn/Grove-Ultrasonic_Ranger/)

*   [12. Relay](http://wiki.seeedstudio.com/cn/Grove-Relay/)


## 资源下载
---
-   **[Eagle 文件]** [GrovePi_Plus V3.0 eagle file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2BEagle%20FIle.zip)
-   **[原理图 PDF]** [GrovePi_Plus V3.0 schematics pdf file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2B%20v3.0%20Sch.pdf)
-   **[PCB图 PDF]** [GrovePi_Plus V3.0 PCB pdf file](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/GrovePi%2B%20v3.0%20PCB.pdf)
-   **[其他资源]** [Setting_Up_Software_for_GrovePi](https://github.com/SeeedDocument/GrovePi_Plus/raw/master/res/Setting_Up_Software_for_GrovePi.pdf)
