---
title: Bluetooth Shield V2.0
category: Shield
bzurl: https://www.seeedstudio.com/Bluetooth-Shield-V2-p-2416.html
oldwikiname: Bluetooth Shield V2.0
prodimagename: Bluetooth_Shiled_v2.JPG
wikiurl: http://wiki.seeedstudio.com/cn/Bluetooth_Shield_V2
sku:  113030019
---

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shiled_v2.JPG)

Bluetooth Shield 集成了一个串行蓝牙模块。 它可以很方便地与 Arduino / Seeedstudio 一起用于连续的无线串行通信。您可以从 Arduino D0 到 D7 中选择两个引脚作为软件串行端口与 Bluetooth Shield （D0和D1是硬件串行端口）进行通信。Shield 还有两个 Grove 接口（一个是 Digital，另一个是 Analog），用于连接 Grove 模块。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.28.27fd28d4NbaMeo&id=45557972221)

##   产品特性
---
*   输入电压：3.3V
*   波特率: 9600, 19200, 38400, 57600, 115200, 230400, 460800
*   兼容 Seeeduino/Arduino
*   无障碍环境通讯距离可达 10m
*   具有可编程波特率的 UART 接口（TTL）
*   默认波特率：9600，数据位：8，停止位：1，奇偶校验：无奇偶校验
*   默认 PINCODE：“1234”
*   一套完整的配置命令
*   板载 PCB 天线

##   接口功能
---
![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shield_V2.0_K.jpg)

<table >
<tr>
<th> 接口名称
</th>
<th> 描述
</th></tr>
<tr>
<td> BT_IO
</td>
<td> 蓝牙模块的 IO 端口可以控制：读取，写入。
</td></tr>
<tr>
<td> BT_RX
</td>
<td> 蓝牙模块的 UART 数据输入
</td></tr>
<tr>
<td> BT_TX
</td>
<td> 蓝牙模块的 UART 数据输出
</td></tr>
<tr>
<td> 两个 Grove 端口
</td>
<td> 一个是数字端口(D8 和 D9), 另一个是 I2C/模拟端口 (A4 和 A5).
</td></tr></table>



##   示例

### 1：两个 Bluetooth Shield 连接

这个示例会展示如何连接两个 Bluetooth shield。

你需要两个 [Seeeduino V4.2](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.16a86daf0qHouM&id=45721222112)，一个 Bluetooth shield 作为主机，另一个为从机。

**硬件连接**

如下所示：

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_shield_demo_image0.png)

确定跳线帽的位置正确。

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_shield_demo_image4.jpg)

**下载代码并上传**

1.  你可以在 github 上下载代码，点击 [这里](https://github.com/Seeed-Studio/Bluetooth_Shield_V2_Demo_Code/archive/master.zip)，然后下载 Arduino 的代码。

2.  打开 Arduino IDE，点击 **项目 -&gt; 加载库 -&gt; 添加一个 .ZIP 库**，导入代码。然后点击 **文件 -&gt; 示例 -&gt; Bluetooth_Shield_V2_Demo_Code -&gt; Master_Button**，打开主机示例代码。点击 **上传** 按钮把代码上传到主机开发板。

3.  点击 **文件 -&gt; 示例 -&gt; Bluetooth_Shield_V2_Demo_Code -&gt; Slave_led**，打开从机示例代码。点击 **上传** 按钮把代码上传到从机开发板。

4.  如果您对使用 Arduino 有任何困难，请点击 [这里](http://wiki.seeedstudio.com/cn/Getting_Started_with_Seeeduino/) 获取帮助。

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_ide_1.jpg)

**查看结果**

1.  代码上传到主机和从机后，同时复位两个设备

2.  您可以看到指示灯闪烁，表示设备正在初始化并连接。

3.  经过大约几秒钟的时间，LED 灯保持点亮，表示主机和从机连接完成。

!!!Note
    如果没有出现上述结果，请拔掉电源并重新连接。


### 2：连接智能手机

本演示将向您展示如何将蓝牙连接到智能手机。

我们需要一个带蓝牙功能的智能手机和 [Seeeduino V4.2](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.16a86daf0qHouM&id=45721222112)。

安装蓝牙 SPP 应用程序

**硬件安装**

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_shield_demo_image1.png)

**下载代码并上传**

1.  你可以在 github 上下载代码，点击 [这里](https://github.com/Seeed-Studio/Bluetooth_Shield_V2_Demo_Code/archive/master.zip)，然后下载 Arduino 的代码。

2.  打开 Arduino IDE，点击 **项目 -&gt; 加载库 -&gt; 添加一个 .ZIP 库**，导入代码。然后点击 **文件 -&gt; 示例 -&gt; Bluetooth_Shield_V2_Demo_Code -&gt; Slave_Temperature**，打开主机示例代码。点击 **上传** 按钮把代码上传到主机开发板。

3.  点击 **上传** 按钮把代码上传到主机开发板。如果您对使用 Arduino 有任何困难，请点击 [这里](/Getting_Started_with_Seeeduino) 获取帮助。

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shield_Demo2.jpg)


**下载一个 SSP App**

这里我们使用一个 Ardriod 手机。打开应用商店，搜索 **蓝牙串口 SPP**，找到合适的软件并下载。

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shield_Find_spp.png)

**获取温度**

安装 SPP 应用程序后，尝试连接到 SeeedBTSlave，密码是：“0000”

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shield_App_1.png)

当连接好后，发送 't' 到 SeeedBTSlave，就会返回温度数据。

![](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/img/Bluetooth_Shield_get_temp.png)

##   资源下载

*   **[Eagle 文件]**[Schematic and Layout in Eagle format](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/res/Bluetooth_en.pdfBuletooth_Shield_v2.0_sch_pcb.zip)

*   **[数据手册]**[module Datasheet](https://github.com/SeeedDocument/Bluetooth_Shield_V2/raw/master/res/Bluetooth_en.pdfBluetooth_en.pdf)
