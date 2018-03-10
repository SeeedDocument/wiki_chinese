---
title: USB To Uart 5V/3V3
category: Essentials
bzurl: https://www.seeedstudio.com/USB-To-Uart-5V%263V3-p-1832.html
oldwikiname:  USB To Uart 5V/3V3
prodimagename:  Photo_USB_To_Uart_5V_3V3.JPG
wikiurl: http://wiki.seeedstudio.com/cn/USB_To_Uart_5V_3V3
sku:  103990049
---
![](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/img/Photo_USB_To_Uart_5V_3V3.JPG)

USB To Uart 5V/3V3  是基于 CH34 的 USB 至串口适配器，CH340 是一个 USB 总线转换芯片，可实现 USB 至串口，USB 至 IrDA 红外或 USB 至打印机接口的转化。该模块 I/O 口兼容 5V 或 3v3，可用于上传代码或与 MCU 通信。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=521795408834)

##  产品特性
---
*   高速 USB2.0 接口

*   3.3V 或 5V 兼容 I/O 口

*   支持 2400bps 至 115200bps 的波特率

*   硬件全双工串行接口，设置收发缓冲区

*   LED 指示灯

##  规格参数
---
*   工作电压 ：DC 5V

*   工作电流 &lt; 10mA

*   操作系统 ： Windows、Linux、Mac

##  硬件概述
---
![](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/img/USB_To_Uart_5V_3V3.jpg)

*   ①：电源指示灯

*   ②：Micro USB

*   ③：TX 指示灯

*   ④：RX 指示灯

*   ⑤：Uart 引脚

*   ⑥：VCC 切换开关 : 选择 5V 或 3V3

##  使用方法
---
**驱动安装**

USB To Uart 5V/3V3 用作 USB 至串口接口时，需要安装驱动程序。

**Windows/Linux**

完全兼容计算机终端 Windows 操作系统中的串口应用程序

*   1)通过 USB 端口将其插入计算机。

*   2)片刻之后您可以在设备管理器中找到它。

![](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/img/CH340_Driver.jpg)

  *   3)如果找不到端口，请从 [这里](http://www.wch.cn/download/CH341SER_ZIP.html) 下载驱动程序

**Mac OS**

驱动下载 :  [点击这里](http://www.wch.cn/download/CH341SER_MAC_ZIP.html)

在 Mac OS Yosemite 上 :

*   1) 安装 CH340 驱动

*   2) 打开终端程序 (位于 /Applications/Utilities/)

*   3) 输入命令 : sudo nvram boot-args="debug=0x146 kext-dev-mode=1"

*   4）输入密码 ;

*   5）重启电脑 ;

如果您想恢复您的 Mac 的设置，您可以通过重新定义启动参数到您以前的设置以退出开发者模式，或通过命令清除您的启动参数，命令为 : sudo nvram -d boot-args

<big>硬件</big>

![](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/img/USB_To_Uart_Download.jpg)

请像这样连接电路。

<big>示例</big>

我们可以通过 USB To Uart 5V/3V3 下载代码到 Seeeduino Ethernet。

![](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/img/USB_To_Uart_5V_3v3_Usage.jpg)

请注意应选择正确的电路板类型和 COM 端口。

##  资源下载
---
- **[Eagle 文件]** [USB To Uart 5V/3V3 v1.0 Eagle File](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/res/USB_To_Uart_5V_3V3_Eagle.zip)

- **[原理图 PDF]** [Schematic in pdf](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/res/USB_To_Uart_5V_3V3_v1.pdf)

- **[芯片数据手册]** [Datasheet of CH340](https://github.com/SeeedDocument/USB_To_Uart_5V_3V3/raw/master/res/CH340DS1_EN.PDF)
