---
name: Seeeduino Lite
category: Arduino
bzurl: https://www.seeedstudio.com/Seeeduino-Lite-p-1487.html
oldwikiname:   Seeeduino Lite
prodimagename:  Seeeduino_ethernet-2.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Seeeduino_Lite
sku:   102010008
---
![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/400px-Lite_01.jpg)

Seeeduino Lite 是基于 ATmega32U4 微控制器的开发板。就像 Arduino Leonardo 一样，它无需 USB 转串口通信所需的辅助处理器。这使得 Seeeduino Lite 可以作为计算机上的 USB 设备，如键盘和鼠标。Seeeduino Lite 源自 Leonardo，我们还将 Seeeduino 系列的自定义细节合并到 Seeeduino Lite 中，如可选工作电压，板载 Grove 接口等等。它有 20 个数字 I/O（其中 7 个可输出PWM），一个 Micro USB 连接，一个电源插孔，一个 ICSP 插头和一个复位按钮。它使用非常简单，只需使用 USB 电缆将其连接到计算机，或使用外接电源工作。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.40.ec746f3rav3r6&id=45487750521)


## 规格参数
---
- 微控制器：ATmega32u4
- 工作电压：5V
- 输入电压 (推荐值)：7-12V
- 输入电压 (最大范围)：6-20V
- 数字 I/O 引脚：20
- PWM 通道：7
- 模拟输入通道：12
- 每个 I/O 引脚的直流电流：40 mA
- 3.3V 引脚的直流电流：50 mA
- Flash 存储：32 KB (ATmega32u4) 其中有 4 KB用于引导装在程序
- SRAM：2.5 KB (ATmega32u4)
- EEPROM：1 KB (ATmega32u4)
- 时钟频率：16 MHz

## 接口
---
![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/Seeeduino_Lite_Intrface_Function.jpg)

**U1:** 78M05 IC，三端稳压器。

**U3:** LD1117 IC，低压降稳压器，能够提供高达 800mA 的输出电流。

**U5:** Atmega32U4 IC，具有 32KB 的 ISP 闪存和 USB 控制器的8位AVR微控制器。


## 安装驱动程序
---
从这里下载驱动程序： [https://github.com/Seeed-Studio/Signed_USB_Serial_Driver](https://github.com/Seeed-Studio/Signed_USB_Serial_Driver).

使用 Micro-USB 线把 Seeeduino Lite 连接到电脑。

等待发现新硬件。如果安装程序没有自动启动，请打开 Windows 设备管理器并找到 Seeeduino Lite 这一项。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/Unknow_Device.jpg)

右键单击并选择更新驱动程序。 当要求自动搜索或手动查找时，请选择“浏览我的计算机以查找驱动程序软件”。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/Update_Driver.jpg)

选择“在以下位置搜索驱动程序：”，然后点击下方文本框的“浏览”找到您下载好的驱动程序，选择该文件并点击确定。


![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/Browse_Driver_Location.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lite/master/image/Successfully_Update_Driver.jpg)

替换 Arduino 路径中的两个文件。打开 **Arduino-1.0.1/hardware/arduino/cores/arduino** 目录，用 **新的** USBCore.cpp 覆盖原来的 **USBCore.cpp**，然后在目录 **Arduino-1.0.1/hardware/arduino** 下用 **新的 boards.txt** 替换原来的文件。文件可在篇尾的 **“资源下载”** 中找到。现在，您可以用使用其他 Arduino 板的方法来和使用 seeeduino lite。

## 资源下载
---
- **[Eagle 文件]**[Seeeduino Lite Eagle File](https://github.com/SeeedDocument/Seeeduino_Lite/blob/master/resource/Seeeduino_Lite_Eagle_File.zip).
- **[替换文件]**[new boards.txt](https://github.com/SeeedDocument/Seeeduino_Lite/blob/master/resource/Boards.zip).
- **[替换文件]**[new USBCore.cpp](https://github.com/SeeedDocument/Seeeduino_Lite/blob/master/resource/Boards.zip).
- **[驱动程序]**[Lite Driver File](https://github.com/SeeedDocument/Seeeduino_Lite/blob/master/resource/Signed_USB_Serial_Driver-master.zip).  
