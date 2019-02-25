---
name: Grove - Haptic Motor
category: Actuator
bzurl: https://seeedstudio.com/Grove - Haptic Motor-p-2546.html
oldwikiname: Grove_-_Haptic_Motor
prodimagename: Grove_Haptic_Motor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Haptic_Motor
sku: 105020011
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/img/Grove_Haptic_Motor.jpg)

 Grove - Haptic motor 是与 [DRV2605L](http://www.ti.com/product/DRV2605L) 集成的 Grove 模块，它将为您带来更好的项目体验。 该电机专为各种效果而设计，例如上下摆动、震动的，可穿戴式及其他 IoT 设备。 现在我们开发了一个易于使用的库，可以模拟 123 种振动模式，这将使您项目制作更快捷。 此外，您可以使用驱动器 DRV2605L 开发更高级的功能，它在启动时间和中断时间方面会有更高的执行性能，并可通过共享 I2C 兼容总线或 PWM 输入信号进行访问。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.591c5a5870Qcv6&id=540407861708)

产品特性
--------


- 能够识别很多振动效果。
- 能够加快项目制作开发过程。
- 有123 种振动模式和易于使用的库。
- 有强大的驱动程序来配置更高级的功能。

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


参数规格
-------------

| 项目                    |参数        |
|--------------------------------|----------------|
| 工作电压| 3.3〜5.0 V |
| 电压（最大功率）| 50〜100 mV |
| 最大功率| 750 mW |
| I2C 频率| 100 kHz |
| 振动效应| 123 种|
|驱动器 | DRV2605L |
| 接口| I<sup>2</sup>C |
| 默认 I<sup>2</sup>C 地址 | 0x5A |

支持平台
-------------------

创新应用
-----------------

- 手机，平板电脑
- 可穿戴设备。
- 遥控器，启用触控功能的设备。
- 工业人机界面。

硬件概述
-----------------

**正视图:**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/img/Grove_Haptic_Motor.jpg)

**后视图:**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/img/Grove_Haptic_Motor_back.jpg)

入门指导
---------------

<div class="admonition note">
<p class="admonition-title">注意</p>
本节仅显示如何构建基本开发环境。 您可以使用以下指南为项目构建开发环境：
</div>

### 创建 IDE

请参阅以下指南来构建适当的IDE：

[Windows 入门](/Seeeduino_v4.2#Getting_Started_on_Windows)

[Mac OS X 入门](/Seeeduino_v4.2#Getting_Started_on_Mac_OS_X)

<div class="admonition note">
<p class="admonition-title">注意</p>
由于 <a href="/Seeeduino_v4.2">Seeeduino</a> 与 Arduino 兼容，因此如果您没有 Seeeduino 板， Arduino 板也可以代替。
</div>

### 硬件连接

<div class="admonition note">
<p class="admonition-title">注意</p>
<p>a. 确保您已经通过之前的步骤成功构建了开发环境.</p>
<p>b.确保您选择了电路板的 Arduino Uno 和 COM 端口。 并连接到 Seeeduino 板上的 I<sup>2</sup>C 接口和 Haptic motor.</p>
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/img/Grove_haptic_motor_connection.jpg)

### 下载示例代码

1. 您可以下载 [示例代码](https://github.com/Seeed-Studio/Grove_Haptic_Motor) 和库或头文件。
2. 点击[Github](https://github.com/Seeed-Studio/Grove_Haptic_Motor) 上名为 “Download Zip” 的按钮。
3. 解压缩下载的 ZIP 文件。
4. 在解压文件名中删除 “-master” 两次。
5. 将文件夹 Grove_Haptic_Motor 复制到库文件夹中（默认情况下，它与 Sketchbook 位置相同，可以通过单击 **文件&gt;首选项** 找到）。在Windows中，它可能会被称为“我的文档\ Arduino \库”。 对于Mac用户来说，它可能被称为“文档/ Arduino /库”。 在Linux上，它将是您的 sketchbook 中的“库”文件夹。
6. 将文件 **drv2605.cpp** 和文件 **drv2605.h** 复制到其上一级目录中。

### 下载示例代码

<div class="admonition note">
<p class="admonition-title">注意</p>

在这种情况下，我们使用<a href="/Seeeduino_v4.2"> Seeeduino 4.2 </a>作为与 Arduino 兼容的实验板。
</div>

<div class="admonition tip">
<p class="admonition-title">小提示</p>
您可以使用<a href="/Base_Shield_V2"> Base Shield v2 </a>作为扩展板，这将使您的模块连接变得简单。
</div>


<div class="admonition warning">
<p class="admonition-title">警告</p>
在 DRV2605L 驱动器使用中请不要触摸，否则这有可能会损坏它。
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/img/Grove_Haptic_Motor_cautions.png)

1. 确保 haptic motor 和主控板良好连接。
2. 将示例代码 drv2605.ino 加载到解压缩文件的示例文件中。
3. 通过单击 **Project（项目）-> Upload（CTRL + U）** 将代码载入到主控板上。
4. 上传后，您就可以让 haptic motor 稳定的运行了。

资源下载
---------

-   Schematic files in [Eagle format](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/res/Grove_Haptic_Motor_v0.9_Eagle.zip) and [PDF format](https://raw.githubusercontent.com/SeeedDocument/Grove-Haptic_Motor/master/res/Grove_Haptic_Motor_v0.9_SCH.pdf).
-   [More about drive circuit DRV2605L](http://www.ti.com/product/DRV2605L).
-   [Git repository](https://github.com/Seeed-Studio/Grove_Haptic_Motor)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Haptic_Motor -->
