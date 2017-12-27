---
title: UartSBee V4
category: Arduino
bzurl: https://www.seeedstudio.com/UartSBee-V4-p-688.html
oldwikiname: UartSBee V4
prodimagename: Xbs4.jpg
wikiurl: http://seeed.wiki/UartSBee_V4
sku:  103990023
---
 ![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//Xbs4.jpg)

**UartSBee v4.0** 是 FTDI 线缆兼容的 **USB to Serial** 适配器，并且配备了 BEE 插座 (20 针 2.0mm)。内部集成的 **FT232RL** 可用于编程或与 MCU 通信。另一方面，您可以通过 **Bee** 兼容模块将 PC 连接到各种无线应用。UartSBee 在 **FT232RL** 的 bit-bang 模式引脚上进行了突破。Bit-bang 模式引脚 (8 I/O 引脚) 可以用来替代涉及 PC 平行端口的应用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=520629042670)

##   更新日志

<table >
<tr>
<th> 版本
</th>
<th> 说明
</th>
<th> 发布日期
</th></tr>
<tr>
<td> UartSBee V3.1
</td>
<td> 删除底部的蓝牙模块，精简尺寸
</td>
<td> 2010 年 9 月 2 日
</td></tr>
<tr>
<td> UartSBee V2.3
</td>
<td> 3.3V 引脚支持高达 500mA 的直流电流，为 XBee Pro 提供更好的支持
</td>
<td> 2009 年 7 月 21 日
</td></tr>
<tr>
<td> UartSBee V2.1
</td>
<td> 原始版本
</td>
<td> 2009 年 2 月 1 日
</td></tr></table>

##   产品特性
---
*   FTDI 线缆兼容
*   USB 2.0 串口兼容
*   3.3V 和 5V 兼容 I/O 口
*   3.3V 和 5V 双电源输出
*   BEE 模块 RST 按钮
*   Bit-Bang 模式 (8个串行 I/Os 或 SPI)
*   用于 UART 和 BEE 操作的 LED

##   创意应用
---
*   USB 至串口适配器，用于与 TTL/CMOS 电平串行设备进行通信。
*   Arduino/Seeeduino 和及其兼容板的编程器。
*   使用 ISP 的微控制器 / CPLD 的编程器。
*   为面包板 MCU 应用作 3.3V/5V 电源
*   用于 BEE 模块的 USB 适配器。
*   在 FT232RL bit-bang 模式下作为基于 USB 并行设备的无限可能性 - 已知可用作 **AVR-ISP**，低速 **JTAG** ，作为 **I2C**。

!!!Cautions
    UartSBee v3.1 提供了一个电源选择 (3.3V 或者 5V) 切换开关。在将扩展板连接到任何其他设备之前，请确保将电源选择开关设置为 3.3V 或 5V。

##   原理图
---
![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSBee_V4.0_Sch.png)

##   规格参数
---
###   关键规格参数

<table cellpadding="1" cellspacing="1">
<tr>
<th scope="row"> 微处理器
</th>
<td> FT232RL
</td></tr>
<tr>
<th scope="row"> PCB 尺寸
</th>
<td> 3.1cm x 4.1cm
</td></tr>
<tr>
<th scope="row"> 指示灯
</th>
<td> 电源-绿色 LED。
</td></tr>
<tr>
<th scope="row"> 电源
</th>
<td> 3.3V 和 5V DC
</td></tr>
<tr>
<th scope="row"> 接口
</th>
<td> Mini-B USB, 2.54mm 间距引脚
</td></tr>
<tr>
<th scope="row"> 适配器插座
</th>
<td> XBee 兼容 2.0mm 间距引脚
</td></tr>
<tr>
<th scope="row"> 连接
</th>
<td> USB
</td></tr>
<tr>
<th scope="row"> 通行协议
</th>
<td> UART，Bit Bang I/O，SPI
</td></tr>
<tr>
<th scope="row"> ROHS
</th>
<td> 达标
</td></tr></table>

###   电气特性

<table >
<tr>
<th> 参数
</th>
<th> 最小值
</th>
<th> 典型值
</th>
<th> 最大值
</th>
<th> 单位
</th></tr>
<tr>
<td> 输入电压
</td>
<td> -
</td>
<td> 5
</td>
<td> 5
</td>
<td> Vdc
</td></tr>
<tr>
<td> 电流功耗
</td>
<td> -
</td>
<td> -
</td>
<td> 500
</td>
<td> mA
</td></tr>
<tr>
<td> 输出电压
</td>
<td> 3.3
</td>
<td> -
</td>
<td> 5
</td>
<td> Vdc
</td></tr></table>

##   系统框图
---
![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//Uartsbee-block-diagram.jpg)

*   小型 **reset** **开关** 用于重置 **Bee** 兼容设备。
*   除了 BEE 兼容模块的 **2 x 10** 针头外，还提供 **2 x 10** 针头接脚，**2 x 3** ISP 引脚。

##  应用
---
###   USB 至串口

**UartSBee** 通常用作 USB 至串口 (COM 端口) 的接口。这种配置可用于与 MCU 串口通信或对支持基于 ISP 的串口的 MCU 进行编程。

**Windows**

*   在 Windows 操作系统中，第一次插入设备时，可能会要求安装驱动程序。

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_Detected_Windows.JPG)

从 FTDI 网站下载并安装 **Virtual COM port** 驱动程序 :

[点击这里下载](http://www.ftdichip.com/Drivers/VCP.htm)

*   弹出安装驱动程序的向导。选择 **Install from a list or specific location**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_Driver_install_1.JPG)

*   选择驱动程序的下载路径

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_Driver_install_2.JPG)

*   如果出现下图情况，请点击 **Continue Anyway**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_Driver_install_2.1.JPG)

*   **UartSBee** 驱动程序已成功安装。Windows 将 **COM** 端口名称分配给 **FT232RL**，如 **COM10**, **COM11** 等...请在设备管理器中检查名称。本文的情况中，UartSBee 对应 **COM16**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_Driver_install_3.JPG)

**GNU/Linux**

**GNU/Linux OS** 自带 FT232RL 驱动程序。发送 **lsusb** 命令以检验是否检测到 UartSBee。应得到类似于下面的反馈。

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//Lsub.png)

**GNU/Linux** 分配 **/dev/ttyUSB0**, **/dev/ttyUSB1** 等... 作为设备名。

检验串口是否连接 UartSBee 的 **TxD** 和 **RxD** 引脚，并如下图使用像 **cutecom** 这样的终端应用程序来配置设备参数。

- **Baudrate**  : 9600
- **Data bits** : 8
- **Stop bits** : 无（None and no Handshake）

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//Uartsbee-txd-rxd-connected.JPG)

在终端输入的任何字符将返回显示，如图所示。

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartsBee-CuteCom.png)

在 **Windows** - **Hyperterminal** 中也可以实现相同功能

### 3.3V / 5v 电源

除 UartSBee 提供的 3.3V 和 5V 电源输出外，I/O 引脚的逻辑电平可以选择 **5.0V TTL** 或 **3.3V CMOS**。在下面的例子中，演示了基于面包的电路板微控制器应用。 LPC1343 ARM Cortex-M3 MCU 连接到 UartSBee。由于这是一个 3.3V 设备，电源切换开关设置为 3.3V。LPC1343 可以通过 UART 编程。此应用可以扩展到任何支持基于 UART 的闪存或基于 SPI 的闪存 (需要 FT232R Bit-bang 模式) 的 MCU / CPLD。

**原型设计** : **UartSBee v3.1** 充当 3.3V 电源和 LPC1343 的 3.3V UART 闪存编程端口。

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSBee_as_uCPowerSupplyAndProgPort_BreadBoard.JPG)

 **Switch**: 选择 3.3V

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UarSBee-Switch_3.3V_selected.jpg)

###   PC 无线应用中的 Bee 模块接口

**PC 无线附加设备**

UartSBee 的 Bee 兼容接口可以用来连接诸如 **XBee**，**Bluetooth Bee**，**RF Bee**，**Wifi Bee**，**GPS Bee** 等 Bee 模块至 PC USB。这使得基于 Bee 的 PC 无线应用使用更方便。由于这些 Bee 模块大部分都支持 UART 接口，所以 PC 编程也变得容易。

**MCU 无线附加设备**

这种配置也适用于微控制器 (Seeeduino) 的 UART 接口。

更多信息请参阅 Bee 模块文档

**XBee** 连接到 **UartSBee** 和 **BluetoothBee** 连接到 **UartSBee**
![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSBee-hardware.jpg) ![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//BluetoothBee_with_UartSBee.JPG)

###   Bit-bang 模式

与其他基于 FT232RL 的 USB 至串口设备相比，UartSBee V4 的一个亮点是将所有的 Bit-Bang I/O 引入到引脚。

Bit-Bang 模式是 FT232RL 的一个特殊功能，其中 8 条 I/O 线 (**D0 - D7**) 可用作通用双向 I/O 线。FT232RL 支持三种 Bit-Bang 模式。

*   **异步 Bit-Bang 模式**

写入器件的任何数据都被锁存到配置的输出引脚。数据传输速率是由波特率发生器配置的。在此模式下，可以将 8 个 I/O 线中的任何一个配置为输入或输出。

*   **同步 Bit-Bang 模式**

在这种模式下数据被同步发送。在输出字节发送到设备之前读取输入。因此要读取输入，必须执行写入操作。

*   **CBUS Bit-Bang 模式**

这是一个需要重新编程 FT232RL EEPROM 的特殊模式。使用信号 **C0 - C3**。

FT232RL 的 **Bit-Bang 模式** 在应用笔记 [[1]](http://www.ftdichip.com/Support/Documents/AppNotes/AN_232R-01_Bit_Bang_Mode_Available_For_FT232R_and_Ft245R.pdf) 中有详细记载

**表 : Bit-Bang I/O 映射**

<table >
<tr>
<th> UartSBee Signal
</th>
<th> BitBang I/O Signal
</th></tr>
<tr>
<td> TxD
</td>
<td> D0
</td></tr>
<tr>
<td> RxD
</td>
<td> D1
</td></tr>
<tr>
<td> RTS
</td>
<td> D2
</td></tr>
<tr>
<td> CTS
</td>
<td> D3
</td></tr>
<tr>
<td> DTR
</td>
<td> D4
</td></tr>
<tr>
<td> DSR
</td>
<td> D5
</td></tr>
<tr>
<td> DCD
</td>
<td> D6
</td></tr>
<tr>
<td> RI
</td>
<td> D7
</td></tr></table>

**BitBang 模式操作 : **

在下面的 DTR (D4) 引脚连接到 LED 的面包板布局中演示了一种简单的异步 Bit-Bang 模式操作。LED 闪烁速率由 PC 端程序控制。

**LED 闪烁电路**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSBee_bit-bang-DTR.jpg)

**BitBang I/O - 仰视图**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSBee_Bottom_Bit_Bang.png)

Bit-Bang 模式需要使用名为 [D2XX](http://www.ftdichip.com/Drivers/D2XX.htm) 的特殊 FTDI 直驱程序。移除 FT232RL 芯片的 **Virtual COM Port** 驱动程序后，需要安装此驱动程序。在 GNU/Linux 中，这个驱动程序以内核模式运行。也可以使用 D2XX 的替代品 - 免费开源驱动 [libFTDI](http://www.intra2net.com/en/developer/libftdi/)。它适用于 Windows，GNU/Linux 和 Mac OS。它在 GNU/Linux 中以用户模式运行。因此无需移除现有的 FT232RL 驱动程序。

**libUSB** libFTDI 所需的 libusb，可以从 [这里](https://sourceforge.net/projects/libusb/files/) 下载

下面的示例代码可以用与 libFTDI 示例文件类似的方式进行编译。一个简单的方法是将以下代码的内容复制到一个现有示例的 .c 文件中，然后构建整个驱动程序

**示例代码**

```c
/*
Blinky.C&nbsp;: UartSBee v3.1 (FT232RL) Bit-Bang mode - Blinky.

Circuit:
Connect DTR to Anode of LED, Connect one end of resistor to GND and other end
to Cathode of the LED
*/

#ifdef __WIN32__
#define sleep(x) Sleep(x)
#endif

// 8 bit pin mask for I/O pin
#define TXD 0x01
#define RXD 0x02
#define RTS 0x04
#define CTS 0x08
#define DTR 0x10
#define DSR 0x20
#define DCD 0x40
#define RI  0x80

#include &lt;stdio.h&gt;
#include &lt;ftdi.h&gt;

int main()
{
    unsigned char ouputState = 0;
    struct ftdi_context ftdic;

    /* 1. Initialize ftdi device context */
    ftdi_init(&amp;ftdic);

    /* 2. Open the device based of VID/PID pair */

    if(ftdi_usb_open(&amp;ftdic, 0x0403, 0x6001) &lt; 0)
    {
        printf("Unable to UartSBee v3.1");
        return 1;
    }

    /* 3. Enable Bit-Bang mode with for DTR line  */
    ftdi_set_bitmode(&amp;ftdic, DTR, BITMODE_BITBANG);

    /* 4. Blink LED every 1 second */
    while(1) {
        ouputState ^= DTR;
        ftdi_write_data(&amp;ftdic, &amp;ouputState, 1);
        sleep(1);
    }
}
```

FT232RL Bit-Bang 模式可用于构建 AVR ISP，JTAG，SPI 和 I2C 端口。参考外部链接。

**AVR-ISP 连接**

![](https://github.com/SeeedDocument/UartSBee_V4/raw/master/img//UartSbee_ISP_Connection_BitBang.jpg)


## 资源下载

*   **[Eagle 文件]** [Schematic and Board Files](https://github.com/SeeedDocument/UartSBee_V4/raw/master/res/UartSBee_v4.0_Source_file.zip)

##   外部链接

*   [FTDI FT232RL product Page](http://www.ftdichip.com/Products/ICs/FT232R.htm)

*   [FTDI Virtual COM Port (VCP) drivers](http://www.ftdichip.com/Drivers/VCP.htm)
*   [FTDI D2XX drivers](http://www.ftdichip.com/Drivers/D2XX.htm)

*   [FTDI Bit-Bang mode application note](http://www.ftdichip.com/Support/Documents/AppNotes/AN_232R-01_Bit_Bang_Mode_Available_For_FT232R_and_Ft245R.pdf)

**开源驱动**

*   [libFTDI](http://www.intra2net.com/en/developer/libftdi/)

*   [libUSB](http://libusb.info/)

**其他来源的 FT232RL 应用信息**

*   [Hackaday - Introduction to bit-bang mode](http://hackaday.com/2009/09/22/introduction-to-ftdi-bitbang-mode/)

*   [FT232R JTAG implementation with OpenOCD ](http://vak.ru/doku.php/proj/bitbang/bitbang-jtag)

*   [FT232R SPI Bitbang Mode example](http://openschemes.com/2009/11/05/bit-banging-spi-on-arduinos-ft232rl/)

*   [Flashing Arduino with FT232R bitbang mode](http://www.geocities.co.jp/arduino_diecimila/bootloader/index_en.html)
