---
name: Getting Started with Seeeduino
category: Tutorial
bzurl: 
oldwikiname:  Getting Started with Seeeduino
prodimagename:  Hello_world.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Getting_Started_with_Seeeduino
---
![](https://github.com/SeeedDocument/Getting_Started_with_Seeeduino/raw/master/img/Hello_world.jpg)

###  **0. Hello world**

一般来说，老师会教会我们在开始学习编程语言时编写一个简单的Hello World示例。这只是一个基本的介绍，但这是一个非常重要的过程。虽然你不熟悉Arduino，不用担心。你可以学习关于Arduino的问题：点亮LED。现在以Seeeduino为例，了解如何点亮由数字13针控制的LED。在此之前，请确保已下载Arduino Environment并成功安装Seeeduino驱动程序。如果没有，请点击 [这里](http://wiki.seeedstudio.com/cn/Seeeduino_v4.2/)了解具体步骤。

###   1. 将Seeeduino和电脑相连

使用USB电缆将Seeeduino板连接到电脑。绿色电源LED（标有PWR）应点亮。（当Seeeduino独立工作时，您可以选择USB或电源适配器为Seeeduino供电。）

###   2. 打开例程 Blink

按照以下路径找到并打开例程： **File（文件）&gt;Examples（示例）&gt;01.Basics&gt;Blink**.

![](https://github.com/SeeedDocument/Getting_Started_with_Seeeduino/raw/master/img/Getting_Started1.png)

###   3. 选择您的开发板

您需要按照以下路径进行选择 Tools（工具） &gt; Board menu（开发板），选择您当前的开发板. 在这里我们选择ATmega328.

![](https://github.com/SeeedDocument/Getting_Started_with_Seeeduino/raw/master/img/Getting_Started2.png)

###   4. 选择您的串口

选择您的开发板当前占用的串口，在 Tools（工具） | Serial Port（端口） 中进行选择。

![](https://github.com/SeeedDocument/Getting_Started_with_Seeeduino/raw/master/img/Getting_Started3.png)

###   5. 上传程序

现在，只需点击开发环境中的“上传”按钮即可。等待几秒钟，您应该看到板上的RX和TX LED闪烁。如果上传成功，则会在状态栏中显示“完成上传”消息。

![](https://github.com/SeeedDocument/Getting_Started_with_Seeeduino/raw/master/img/Getting_Started4.png)

###   6. 结果

上传完成后的几秒钟，您应该看到板上的13（L）针脚开始闪烁（橙色）。如果是，恭喜！你的Arduino程序已经开始运行了。
