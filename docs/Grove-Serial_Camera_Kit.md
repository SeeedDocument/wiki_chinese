---
title: Grove - Serial Camera Kit
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Serial-Camera-Kit-p-1608.html
oldwikiname:  Grove - Serial Camera Kit
prodimagename: GSCK_Introduction.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Serial_Camera_Kit
sku:  101020000
---

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_Introduction.jpg)

Grove - Serial Camera Kit 包括一个控制板和两个可互换镜头，一个是标准镜头，另一个是广角镜头。 这对 Arduino 中心图像识别项目来说，是一个很好的相机，因为 Arduino 能支持 30W 像素，所以实时图像识别是可能实现的。为了使其更有趣和可玩，两个规格的镜头都在这个工具包中。标准镜头用于普通照片，广角镜头专用于监控项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.33aec79ew4BQhB&id=45506346921)

##  规格参数
---
*   输入电压 : 5V

*   像素 : 30W

*   分辨率 : 640×480, 320×240, 160×120

*   串口波特率 : 9600~115200

*   通信接口 : RS485 和 RS232

*   图片 JPEG 压缩，高、中、低三档可选

*   自动增益控制

*   自动曝光事件控制

*   自动白平衡控制

*   焦距可调

##  操作示例
---
本演示将向您展示如何使用 Grove - Serial Camera Kit。 我们需要一个 [Seeeduino](https://item.taobao.com/item.htm?spm=2013.1.0.0.31fefbe7sY5lOc&id=45721222112)，一个 [SD Card Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.4804a358I5TBCb&id=520859772674) 和 [Grove - Button](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.15.3d739b0a0yS3Td&id=531838497696)。 按下按钮后，我们拍照并将其保存到 SD 卡。

按照以下步骤一步一步施行，您可以轻松地运行您的 Grove - Serial Camera Kit。开始做吧。

###  硬件安装

我们可以发现在 SD Card Shield V4.0 上有两个 Grove 接口，所以我们不需要 Base Shield，只需将按钮插入 I2C Grove 并将 Camera 插入 Uart Grove。

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_Hardware.jpg)

###  下载代码并上传

您可以在 github 下载演示代码，点击 [这里](https://github.com/Seeed-Studio/Grove_Serial_Camera_Kit)

上传代码，开始工作

###  拍照

完成上传演示代码后，我们可以立即拍照，只需按下按钮，然后等待几秒钟，照片将被保存到 SD 卡中。

以下图像是使用直角镜头拍的我办公室的天花板。

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_60.jpg)

###  更换镜头

还有一个广角镜头，我会告诉你如何更换它。

首先你应该有一把螺丝刀 ：

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_Step1.jpg)

然后，拧下镜头侧面的螺丝 :

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_Step2.jpg)

尝试旋转镜头，拧出镜头 :

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_Step3.jpg)

使用广角镜头拍我办公室的天花板

找到与之前的天花板图像有什么不同 ?

![](https://github.com/SeeedDocument/Grove-Serial_Camera_Kit/raw/master/img/GSCK_90.jpg)

###  如何聚焦

镜头螺丝不同的深度代表不同的焦距，试一试吧。

##  资源下载
---
**[其他资源]** [Demo Code](https://github.com/Seeed-Studio/Grove_Serial_Camera_Kit)
