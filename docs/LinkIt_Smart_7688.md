---
name: LinkIt Smart 7688
category: LinkIt
bzurl: https://www.seeedstudio.com/LinkIt-Smart-7688-p-2573.html
oldwikiname:
prodimagename: cover.png
wikiurl: http://wiki.seeedstudio.com/cn/LinkIt_Smart_7688
sku: 102110018
---

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Linkit_Smart_product.jpg)

LinkIt Smart 7688 (一个紧凑型控制器板) 是基于 MT7688 ([芯片](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/MT7688_datasheet.pdf))， 它运行 Linux 的 Open Wrt 系统。该主板专为用于智能家居的 Rich Application IoT devices 的原型而设计。该板提供足够的内存，能实现强大的视频处理功能。 该平台还提供了能在 Python, Node.js 和 C 编程语言中创建设备应用程序的选项。
该板只是 MediaTek LinkIt Smart 7688 平台的一部分，这个平台还包括其他开发板。

!!!Note
    本页仅引导您开始使用此开发板。 有关完整的指南，请参阅 [资源下载](http://labs.mediatek.com/en/platform/linkit-smart-7688#HDK).

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.420a725434YMOE&id=524890877407)  

## 产品特性
---
*   单输入/输出 Wi-Fi 802.11 b/g/n。
*   支持 GPIO, I<sup>2</sup>C, I<sup>2</sup>S, SPI, UART, PWM 和 Ethernet 引脚端口。
*   580 MHz MIPS CPU。
*   32MB 闪存和 128MB DDR2 内存。
*   丰富的外设连接选项。
*   支持额外 SD 卡储存。

## 创意应用
---
*   用于智能家居的 Rich application IoT Devices
*   机器人

## 规格参数
---
<table>
<tr>
<th>项目
</th>
<th> 特征
</th>
<th>规格
</th></tr>
<tr>
<td rowspan="4"> MPU </td>
<td> 芯片组 </td>
<td> MT7688AN
</td></tr>
<tr>
<td> 核心 </td>
<td> MIPS24KEc
</td></tr>
<tr>
<td> 主频</td>
<td> 580MHz
</td></tr>
<tr>
<td> 工作电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td> PCB Size </td>
<td> 尺寸 </td>
<td> 55.7 x 26 mm
</td></tr>
<tr>
<td rowspan="2"> Memory   </td>
<td> Flash </td>
<td> 32MB
</td></tr>
<tr>
<td>  RAM</td>
<td> 128MB DDR2
</td></tr>
<tr>
<td rowspan="2"> Power Source  </td>
<td> USB 供电 </td>
<td> 5V (USB micro-B)
</td></tr>
<tr>
<td>  VCC 供电</td>
<td> 3.3V (Pin Breakout)
</td></tr>
<tr>
<td rowspan="2"> GPIO  </td>
<td> 引脚数 </td>
<td> 22 (MT7688AN)
</td></tr>
<tr>
<td>  电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td rowspan="5"> PWM  </td>
<td> 引脚数</td>
<td> 4 (MT7688AN)
</td></tr>
<tr>
<td>  电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td>  最大分辨率 </td>
<td> 7 位 (可自定义)
</td></tr>
<tr>
<td rowspan="2">最大频率@分辨率 </td>
<td>

100kHz@1-bit,
50kHz@2-bit,
25kHz@3-bit,
12.5kHz@4-bit,
6.25kHz@5-bit,
3.125kHz@6-bit,
1.5625kHz@7-bit (Standard mode)

</td></tr>
<tr>
<td>

40MHz@1-bit,
20MHz@2-bit,
10MHz@3-bit,
5MHz@4-bit,
2.5MHz@5-bit,
1.25Mhz@6-bit,
625kHz@7-bit
(Fast mode)

</td></tr>
<tr>
<td> External Interrupts </td>
<td> 引脚数 </td>
<td> 22 (MT7688AN)
</td></tr>
<tr>
<td rowspan="3"> SPI </td>
<td> 数量 </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P22, P23, P24 (Shared with on-board flash), P25
</td></tr>
<tr>
<td>  最大频率 </td>
<td> 25 MHz
</td></tr>
<tr>
<td rowspan="3"> SPI Slave </td>
<td> 数量 </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P28, P29, P30, P31
</td></tr>
<tr>
<td>  最大频率 </td>
<td> 25 MHz
</td></tr>
<tr>
<td rowspan="2"> I<sup>2</sup>S </td>
<td> 数量 </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P10, P11, P12, P13
</td></tr>
<tr>
<td rowspan="3"> I<sup>2</sup>C </td>
<td> 数量 </td>
<td> 1
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P20, P21
</td></tr>
<tr>
<td>  速度 </td>
<td> 120K/400K
</td></tr>
<tr>
<td rowspan="3"> UART Lite </td>
<td> 数量 </td>
<td> 3 (MT7688AN)
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P8, P9, P16, P17, P18, P19
</td></tr>
<tr>
<td>  最大速度 </td>
<td> 0.5Mbps
</td></tr>
<tr>
<td rowspan="3"> USB Host </td>
<td> 数量 </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚数 </td>
<td> P6, P7
</td></tr>
<tr>
<td>  数量 </td>
<td> Micro-AB
</td></tr>
<tr>
<td rowspan="3"> ICommunication </td>
<td> Wi-Fi </td>
<td> 1T1R 802.11 b/g/n (2.4G)
</td></tr>
<tr>
<td>  Ethernet </td>
<td> 1-port 10/100 FE PHY
</td></tr>
<tr>
<td> 引脚数 </td>
<td> P2, P3, P4, P5
</td></tr>
<tr>
<td> User Storage </td>
<td> SD Card </td>
<td> Micro SD
SDXC

</td></tr></table>

## 硬件概述
----
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Component_intro_with_text_1200.jpg)

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Back_hardware_view_with_text_1200_s.jpg)

###  产品清单

<table>
<tr>
<th>零件名   </th>
<th> 数量
</th></tr>
<tr>
<td> LinkIt<sup>TM</sup> Smart 7688  </td>
<td> 1PC
</td></tr>
<tr>
<td> 使用手册 </td>
<td> 1PC
</td></tr></table>

## 入门指导
----
###  连接到嵌入式操作系统

!!!Note
    手册中介绍了两种方法。 在这里，我们只展示了难度更高的方式（使用 USB to Serial 适配器）。 但是，从长远来看你会受益匪浅。

####  需要的素材

*   LinkIt Smart 7688 × 1
*   USB cable (type A to micro type-B) × 2
*   USB to Serial adapter× 1
*   Jumper wires × 3


### 在 Windows 系统上

**1.** 安装 [PuTTy](http://www.putty.org/). PuTTY 提供使用 SSH ( Secure Socket Shell ) 的系统控制台环境来访问开发板的操作系统。

**2.** 安装 [Bonjour](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) 打印服务 (可用于 Windows 7, Windows 8, Windows 10).

**3.** 安装驱动程序 如果您使用基于 FTDI 芯片的 USB 线缆，请从 [这里](http://www.ftdichip.com/Drivers/VCP.htm) 下载并安装其驱动程序。如果您遇到有关最新驱动程序的问题，请尝试安装 [以往版本](http://www.ftdichip.com/Support/Documents/InstallGuides.htm)。

**4.** 接下来，您需要将 Serial-to-USB 线缆连接到 LinkIt Smart 7688 的 UART 引脚，如下表所示 :

| USB 适配器上的引脚 | LinkIt Smart 7688 上对应的引脚 |
|-----------------------------------|--------------------------------------------------------|
| Pin RX	| Pin 8 |
| Pin TX	| Pin 9 |
| Pin GND |	Pin GND |

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/LinkIt_Smart_7688_demo_connection_1200_s.jpg)

**5.** 串口连接好 USB 线缆后，打开设备管理器并注意 COM 端口号，如下所示。 这个数字会因不同的计算机而异。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/COM_port.jpg)

**6.** 启动 PuTTY 终端，输入在设备管理器中找到的 USB 设备的 COM 端口号，单击 **Serial** 单选按钮，在 **Speed** 框中键入 57600，单击 **Open**，如下图所示。
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Putty_configuration.jpg)

**7.** 现在，您将会看到在 Linux 控制台中打印文本。

### 在 Mac 系统上

**1.** 如果需要，请安装驱动程序。 请查阅线缆制造商的网站了解 Mac 上的驱动程序要求和安装说明。

**2.** 将线缆插入 PC / 笔记本电脑，并将线缆连接到 LinkIt Smart 7688。

**3.** 打开终端会话。

**4.** 在终端中键入 **ls /dev/cu***。 您会看到设备列表。寻找类似于 cu.usbserial-XXXXXXXX 的东西，其中 XXXXXXXX 通常是一个随机标识符。这是用于访问系统控制台的串行设备。例如 :

```
$ls /dev/cu*

/dev/cu.Bluetooth-Incoming-Port

/dev/cu.Bluetooth-Modem

/dev/cu.pablop-WirelessiAP

/dev/cu.usbserial-A6YMCQBR

```

**5.** 使用屏幕实用程序连接到串口，并将波特率设置为 57600，这是因为默认情况下系统控制台的波特率为57600。 例如 :
```
$screen /dev/cu.usbserial-XXXXXXXX 57600
```

**6.** 现在您要连接到系统控制台。在终端中按 ENTER 键显示提示符。您将注意到，提示符与您的 OS X 终端应用程序的提示符不同，它是 LinkIt Smart 7688 提示符，像下面这样 :
```
  root@myLinkIt:/#
```

**7.** 您现在可以通过此控制台更改 LinkIt Smart 7688 系统。

### 在 Linux 系统上

**1.** 如果需要，请安装驱动程序。 请查看线缆制造商的网站了解 Linux 上的驱动程序要求和安装说明。

**2.** 插入线缆并连接到 LinkIt Smart 7688。

**3.** 打开终端会话。

**4.** 在终端中键入 **ls /dev/ttyUSB*** 。您应该看到设备列表。寻找类似于 cu.usbserial-XXXXXXXX 的东西，其中 XXXXXXXX 通常是一个随机标识符。这是用于访问系统控制台的串行设备。例如 :
```
$ls /dev/ttyUSB*
/dev/ttyUSB0
```
**5.** 使用屏幕实用程序连接到串口，并将波特率设置为 57600，这是因为默认情况下系统控制台的波特率为 57600。 例如 :
```
$sudo screen /dev/ttyUSB0 57600
```
**6.**现在您应该连接到系统控制台。在终端中按 ENTER 键显示提示符。 您将注意到，提示符已成为不同的常规应用程序，它是 LinkIt Smart 7688 提示符，它类似于以下内容 :
```
  root@myLinkIt:/#
```
**7.** 您现在可以通过此控制台更改 LinkIt Smart 7688 系统。

### 运行 Blink 示例

#### 需要的素材

* LinkIt Smart 7688 x 1
* USB cable (type A to micro type-B) x 1
* USB to Serial adapter x 1
* Jumper wires x 3

#### 运行 Blink

**1.** 使用 micro-USB 电缆打开电路板(仅连接 USB 电源接口，而不是 USB 主机接口)。
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Power_up.jpg)

**2.** 启动 PuTTy 并使用 USB 使串行适配器连接到系统，如前几节所示。

**3.** 输入 **python /IoT/examples/blink-gpio44.py** 然后按 **Enter** 来运行 Blink 示例。

!!!note
    请注意，在第一个单词 **python** 之后有 1 个空格，否则将找不到到该示例。

**4.** 大约 2 秒后，您会看到 Wi-Fi LED 稳定地闪烁。

**5.** 在系统控制台中键入 **CTRL + C** 将终止该示例。

### 连接到互联网(切换到站模式）

有两种 Wi-Fi 模式 : AP 模式和站模式。请参阅 [这里](https://answers.yahoo.com/question/index?qid=20061207225409AANCN17) 了解它们之间的区别。

**1.** 通过 micro-USB 线缆为主板上电。

**2.** 打开计算机上的 Wi-Fi 连接实用程序，并连接到名为 LinkIt_Smart_7688_XXXXXX 的接入点。XXXXXX 是一种硬件标识符，不同的开发板可能会有所差异。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Connect_wifi.jpg)

**3.** 通过 mylinkit.local/ 或 192.168.100.1 打开浏览器，设置 root 的密码并登录。单击右上角的 **Network**。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Network_conf.jpg)

**4.** 选择 **Station mode** ，然后单击右侧的 **Refresh** 或向下滑动以查找要连接的 AP。选择 AP 后，如果有需要请输入密码。单击 **Configure & Restart** 完成，如下所示。然后等待约 30 秒钟来切换模式。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Station_mode.jpg)

**5.** 启动 PuTTy 并通过 USB 把系统连接到串行适配器，如上一节所示。

**6.** 输入 ifconfig 然后找到 inet addr 的 IP 地址，如下所示 :

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/IFCONFIG.jpg)

!!!Note
    重新启动系统后仍将进入站模式。 按 Wi-Fi 按钮至少 5 秒钟可切换回 AP 模式。注意 : 需要使用 reboot 命令重启嵌入式操作系统。

**7.** 在浏览器的新 Tab 中键入 IP，您可以登录到 Web 用户界面配置系统。

**8.** 现在主机和 LinkIt Smart 7688 都连接到互联网。 在控制台中键入 **ping www.mediatek.com**，您将看到：
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Ping_result.jpg)

**9.** 现在，您可以通过互联网在开发板上配置系统。


## 演示: 一个 Hello world 的示例
---

!!!Note
    为了避免本地应用程序开发中的内存不足，您应该在更强大的主机环境中设置本机应用程序开发环境，从而使您能够交叉编译 LinkIt Smart 7688 目标的可执行格式。 下表显示了 LinkIt Smart 7688 编程语言和主机上相关开发环境的概述。


| Programming language | Tools and libraries                  | Applications                              | Host platforms supported |
|----------------------|--------------------------------------|-------------------------------------------|--------------------------|
| C/C++                | Cross compilation toolchain          | System programming                        | OS X Linux               |
| Python               | Python runtime on LinkIt Smart 7688  | Prototyping Network Arduino bridge library | OS X Linux Windows       |
| Node.js              | Node.js runtime on LinkIt Smart 7688 | Prototyping Network                       | OS X Linux  Windows      |

###  Hello world 示例在 Python 演示

**1.** 使用 FileZilla 并参考这个 [教程](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29)，服务器 IP ( 替换 **主机名** ) 地址是以前 [Switch to Station mode](https://seeeddoc.github.io/LinkIt_Smart_7688_Duo#Switch_to_Station_mode) 部分中的的 inet addr，用户名是 root，密码是您在该部分中设置的密码。

**2.** 打开一个文本编辑器，复制并粘贴以下示例代码并保存为 **helloworld.py**。
```
print "Hello World!"
```

**3.** Copy the file **helloworld.py** into system on target development environment (LinkIt Smart 7688) with FileZilla, place it under the folder **root**.

**4.** 启动 PuTTy 并使用 USB 连接系统到串行适配器。

**5.** 将工作目录设置为 **/root** 并输入 **python helloworld.py** 来执行。

**6.** 现在您将会看到 **Hello World!** 打印在控制台。


## 资源下载
----
* **[Eagle文件]** [LinkIt_Smart_7688](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/Hardware_Schematics.zip)
* **[PCB图PDF]** [LinkIt_Smart_7688 PCB](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt%20Smart%207688%20Layout.pdf)
* **[原理图PDF]** [LinkIt_Smart_7688 Schematic](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt%20Smart%207688.pdf)
* **[其他资源]** [Manual](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/Manual.zip)
* **[其他资源]** [OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
* **[其他资源]** [MediaTek LinkIt? Smart 7688 Resources:](http://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/hdk_intro/index.gsp)
* **[其他资源]** [Firmware_upgrade_Instruction](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt_Smart_7688_Firmware_upgrade.zip)
* **[其他资源]** [Certificates](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt_Smart_7688-Certificate.zip)
