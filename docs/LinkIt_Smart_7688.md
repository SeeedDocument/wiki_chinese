---
title: LinkIt Smart 7688
category: LinkIt
bzurl: https://www.seeedstudio.com/LinkIt-Smart-7688-p-2573.html
oldwikiname:
prodimagename: cover.png
wikiurl: http://seeed.wiki/LinkIt_Smart_7688
sku: 102110018
---

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Linkit_Smart_product.jpg)

LinkIt Smart 7688（紧凑型控制器板）是一个基于OpenWrt Linux发行版和MT7688([数据手册](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/MT7688_datasheet.pdf))的开放式开发板。 该主板专为智能家居丰富多彩的物联网设备生态而设计。 该板提供足够的内存和存储，以实现强大的视频处理。 该平台还提供了在Python，Node.js和C编程语言中创建设备应用程序的选项。 该板只是联发科LinkIt Smart 7688平台的一部分，该平台还有许多功能性能不同的其他开发板。

!!!Note
  - 本页仅引导您开始使用此开发板。 有关完整的指南，请参阅此处 [详情指南](http://labs.mediatek.com/en/platform/linkit-smart-7688#HDK).

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11Ouw26V&id=524890877407)

## 产品特性
---
*   单输入单输出（1T1R）Wi-Fi 802.11 b / g / n。
*   GPIO引脚, I<sup>2</sup>C, I<sup>2</sup>S, SPI, UART, PWM 以及 Ethernet 接口.
*   580 MHz MIPS CPU.
*   32MB Flash and 128MB DDR2 RAM.
*   USB host.
*   Micro SD slot.

## 创意应用
---
*   丰富多彩的智能家居物联网应用
*   机器人

## 规格参数
---
<table>
<tr>
<th>分类
</th>
<th> 参数
</th>
<th>详情
</th></tr>
<tr>
<td rowspan="4"> MPU </td>
<td> 芯片集 </td>
<td> MT7688AN
</td></tr>
<tr>
<td> 内核 </td>
<td> MIPS24KEc
</td></tr>
<tr>
<td> 时钟频率</td>
<td> 580MHz
</td></tr>
<tr>
<td> 工作电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td> PCB 规格 </td>
<td> 尺寸 </td>
<td> 55.7 x 26 mm
</td></tr>
<tr>
<td rowspan="2"> 存储   </td>
<td> Flash </td>
<td> 32MB
</td></tr>
<tr>
<td>  RAM</td>
<td> 128MB DDR2
</td></tr>
<tr>
<td rowspan="2"> 电源  </td>
<td> USB Power </td>
<td> 5V (USB micro-B)
</td></tr>
<tr>
<td>  VCC </td>
<td> 3.3V (Pin Breakout)
</td></tr>
<tr>
<td rowspan="2"> GPIO  </td>
<td> 引脚数量 </td>
<td> 22 (MT7688AN)
</td></tr>
<tr>
<td>  电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td rowspan="5"> PWM  </td>
<td> 引脚数量</td>
<td> 4 (MT7688AN)
</td></tr>
<tr>
<td>  电压 </td>
<td> 3.3V
</td></tr>
<tr>
<td>  最大分辨率 </td>
<td> 7 bits (customizable)
</td></tr>
<tr>
<td rowspan="2">最高频率@分辨率 </td>
<td>

100kHz@1-bit,
50kHz@2-bit,
25kHz@3-bit,
12.5kHz@4-bit,
6.25kHz@5-bit,
3.125kHz@6-bit,
1.5625kHz@7-bit (标准模式)

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
(快速模式)

</td></tr>
<tr>
<td> 外部中断 </td>
<td> 引脚数量 </td>
<td> 22 (MT7688AN)
</td></tr>
<tr>
<td rowspan="3"> SPI </td>
<td> Set count </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P22, P23, P24 (和片上存储复用), P25
</td></tr>
<tr>
<td>  最高速度 </td>
<td> 25 MHz
</td></tr>
<tr>
<td rowspan="3"> SPI Slave </td>
<td> Set count </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P28, P29, P30, P31
</td></tr>
<tr>
<td>  最高速度 </td>
<td> 25 MHz
</td></tr>
<tr>
<td rowspan="2"> I<sup>2</sup>S </td>
<td> Set count </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P10, P11, P12, P13
</td></tr>
<tr>
<td rowspan="3"> I<sup>2</sup>C </td>
<td> Set count </td>
<td> 1
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P20, P21
</td></tr>
<tr>
<td>  速度 </td>
<td> 120K/400K
</td></tr>
<tr>
<td rowspan="3"> UART Lite </td>
<td> Set count </td>
<td> 3 (MT7688AN)
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P8, P9, P16, P17, P18, P19
</td></tr>
<tr>
<td>  最高速度 </td>
<td> 0.5Mbps
</td></tr>
<tr>
<td rowspan="3"> USB Host </td>
<td> Set count </td>
<td> 1 (MT7688AN)
</td></tr>
<tr>
<td>  引脚编号 </td>
<td> P6, P7
</td></tr>
<tr>
<td>  速度 </td>
<td> Micro-AB
</td></tr>
<tr>
<td rowspan="3"> 网络通信 </td>
<td> Wi-Fi </td>
<td> 1T1R 802.11 b/g/n (2.4G)
</td></tr>
<tr>
<td>  Ethernet </td>
<td> 1-port 10/100 FE PHY
</td></tr>
<tr>
<td> 引脚编号 </td>
<td> P2, P3, P4, P5
</td></tr>
<tr>
<td> 用户存储 </td>
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
<th>项目名称   </th>
<th> 数量
</th></tr>
<tr>
<td> LinkIt<sup>TM</sup> Smart 7688  </td>
<td> 1PC
</td></tr>
<tr>
<td> 指南 </td>
<td> 1PC
</td></tr></table>

## 入门指导
----
###  连接到嵌入式操作系统

!!!Note
  - 注意手册中描述了两种方法。 在这里，我们只展示似乎有点困难的高级方式（使用USB到串行适配器）。 但是，从长远来看，您会受益匪浅。

####  所需材料

*   LinkIt Smart 7688 × 1
*   USB 数据线 (type A to micro type-B) × 2
*   USB 转串口适配器× 1
*   跳线 × 3


### 对于Windows系统：

**1.**点击安装 [PuTTy](http://www.putty.org/) 。 PuTTY可以使用SSH（Secure Socket Shell）的系统控制台环境来访问开发板的操作系统。

**2.**点击安装 [Bonjour](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) 打印服务（对于Windows 7，Windows 8，Windows 10）。

**3.**安装驱动程序 如果您正在使用基于FTDI芯片的USB电缆，请点击 [这里](http://www.ftdichip.com/Drivers/VCP.htm) 下载并安装其驱动程序。 如果您遇到最新驱动程序问题，请尝试安装 [旧版本](http://www.ftdichip.com/Support/Documents/InstallGuides.htm)。

**4.** 接下来，您需要将USB转串口电缆连接到LinkIt Smart 7688的UART引脚，如下表所示：

| USB 适配器引脚 |	 LinkIt Smart 7688 对应引脚|
|-----------------------------------|--------------------------------------------------------|
| Pin RX	| Pin 8 |
| Pin TX	| Pin 9 |
| Pin GND |	Pin GND |

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/LinkIt_Smart_7688_demo_connection_1200_s.jpg)

**5.** 连接串口-USB电缆后，打开设备管理器并注意COM端口号，如下所示。 这个数字可能因不同的计算机而异。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/COM_port.jpg)

**6.** 启动PuTTY终端，输入设备管理器中找到的USB设备的COM端口号，单击“Serial”按钮，在“Speed”框中键入57600，单击“Open”，如下图所示。
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Putty_configuration.jpg)

**7.** 现在，您将看到Linux控制台中的打印文本

### 对于Mac系统：

**1.** 如果需要安装驱动程序，请查阅电缆制造商的网站了解Mac上的驱动程序要求和安装说明。

**2.** 将电缆插入PC /笔记本电脑，并将电缆连接到LinkIt Smart 7688。

**3.** 打开一个终端会话。

**4.** 在终端中键入 **ls /dev/cu*** 。您应该看到设备列表。 寻找类似于cu.usbserial-XXXXXXXX的东西，其中XXXXXXXX通常是一个随机标识符。 这是用于访问系统控制台的串行设备。 如下所示：
```
$ls /dev/cu*

/dev/cu.Bluetooth-Incoming-Port

/dev/cu.Bluetooth-Modem

/dev/cu.pablop-WirelessiAP

/dev/cu.usbserial-A6YMCQBR

```

**5.** 使用screen utility连接到串口，并将波特率设置为57600，这是因为默认情况下系统控制台的波特率为57600。 如下所示：
```
$screen /dev/cu.usbserial-XXXXXXXX 57600
```

**6.** 现在您应该连接到系统控制台。 在终端中按ENTER键显示提示。 您将注意到，提示与您的OS X终端应用程序不同，它是LinkIt Smart 7688提示符，如下所示：
```
  root@myLinkIt:/#
```

**7.** 您可以通过此控制台更改LinkIt Smart 7688系统。

### 对于 Linux 系统：

**1.** 如果需要安装驱动程序，请查阅电缆制造商的网站了解Mac上的驱动程序要求和安装说明。

**2.** 将电缆插入PC /笔记本电脑，并将电缆连接到LinkIt Smart 7688。

**3.** 打开一个终端会话。

**4.** 在终端中键入 **ls /dev//ttyUSB*** 。您应该看到设备列表。 寻找类似于cu.usbserial-XXXXXXXX的东西，其中XXXXXXXX通常是一个随机标识符。 这是用于访问系统控制台的串行设备。 如下所示：

```
$ls /dev/ttyUSB*
/dev/ttyUSB0
```
**5.** 使用**screen**实用程序连接到串行端口，并将波特率设置为** 57600 **。 这是因为默认情况下系统控制台的波特率为57600。 如下所示：

```
$sudo screen /dev/ttyUSB0 57600
```
**6.** 现在你应该连接到系统控制台。 在终端中按ENTER键显示提示。 您会注意到，命令行前的提示符已经不一样了，现在是LinkIt Smart 7688提示符，如下所示：

```
  root@myLinkIt:/#
```
**7.** 您可以通过此控制台更改LinkIt Smart 7688系统。

### 运行Blink 例程

#### 所需材料

*   LinkIt Smart 7688 × 1
*   USB 数据线 (type A to micro type-B) × 2
*   USB 转串口适配器× 1
*   跳线 × 3

#### 运行Blink

**1.** 使用micro-USB数据线给您的开发板供电。 (请注意需要连接下方的USB电源接口，而不是上方的USB数据接口）
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Power_up.jpg)

**2.** 启动PuTTy并使用USB转串口适配器连接到系统，如前几节所示。

**3.** 键入 **python /IoT/examples/blink-gpio44.py** 然后点击 **Enter** 来运行Blink 例程。

!!!note
  -  请注意，第一个单词“python”之后有1个空格，否则将不会找到该示例。

**4.** 大约2秒钟后，您将看到到Wi-Fi LED稳定闪烁。

**5.** 在系统控制台中，键入** CTRL + C **，这将终止该例程。

### 连接到互联网（切换到 station 模式）

有两种Wi-Fi模式：AP模式和station模式。 请参考它们之间的差异--[这是差异](https://answers.yahoo.com/question/index?qid=20061207225409AANCN17) 。

**1.** 使用micro-USB电缆为主板上电。

**2.** 打开计算机上的Wi-Fi连接应用程序，并连接到名为LinkIt_Smart_7688_XXXXXX的接入点。 XXXXXX是一种硬件标识符，因板而异。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Connect_wifi.jpg)

**3.** 打开浏览器，在地址栏输入以下链接 mylinkit.local/ 或者 192.168.100.1, 设置root用户的密码并登录。单击右上角的“Network”。

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Network_conf.jpg)

**4.** 选择station mode，然后单击右侧的REFRESH或单击向下箭头找到要连接的AP。 选择AP后，如果需要，请输入密码。 单击CONFIGURE & RESTART 完成，如下所示。 然后等待约30秒钟切换模式。
![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Station_mode.jpg)

**5.** 启动PuTTy并使用USB转串口适配器连接到系统，如上一节所示。

**6.** 键入ifconfig并找到inet addr的IP地址，如下所示：

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/IFCONFIG.jpg)

!!!Note
  - 重新启动系统后仍将进入“station”模式。 按住Wi-Fi按钮至少5秒钟切换回AP模式。 注意：需要使用reboot命令重启嵌入式操作系统。


**7.** 在浏览器的新网页中键入IP，您可以登录到Web用户界面来配置系统。

**8.** 现在主机和LinkIt Smart 7688都连接到互联网。 在控制台中键入ping ** www.mediatek.com **，您将得到如下所示：

![enter image description here](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/img/Ping_result.jpg)

**9.** 现在，您可以使用互联网在开发板上配置系统。


## 例程: Hello world
---

!!!Note
  为了避免本地应用程序开发过程中的内存不足，您应该在更强大的主机环境中设置本机应用程序开发环境，从而使您能够交叉编译LinkIt Smart 7688目标的可执行格式。 下表显示了LinkIt Smart 7688编程语言和主机上相关开发环境的概述。


| 编程语言| 工具和库                  | 应用程序                            | 主机支持平台 |
|----------------------|--------------------------------------|-------------------------------------------|--------------------------|
| C/C++                | Cross compilation toolchain          | System programming                        | OS X Linux               |
| Python               | Python runtime on LinkIt Smart 7688  | Prototyping Network Arduino bridge library | OS X Linux Windows       |
| Node.js              | Node.js runtime on LinkIt Smart 7688 | Prototyping Network                       | OS X Linux  Windows      |

###  A Hello world example in Python

**1.** 使用FileZilla [<参考本教程>](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29) 连接，服务器IP地址是先前切换到station模式时的inet addr，用户名是root，密码是刚刚您设置的密码。



**2.** 打开一个TXT文本编辑器，复制并粘贴以下示例代码并将其保存为** helloworld.py **。
```
print "Hello World!"
```

**3.** 使用FileZilla将文件** helloworld.py **复制到目标开发环境（LinkIt Smart 7688）的系统中，将其放在文件夹** root **下。


**4.** 启动PuTTy并使用USB转串口适配器连接到系统。

**5.** 使用CD命令将工作目录跳转到** / root **并输入** python helloworld.py **来执行。

**6.** 现在你可以看到** Hello World **！ 打印在控制台。


## 资源下载
----
* **[Eagle]** [LinkIt_Smart_7688](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/Hardware_Schematics.zip)
* **[PDF]** [LinkIt_Smart_7688 PCB](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt%20Smart%207688%20Layout.pdf)
* **[PDF]** [LinkIt_Smart_7688 Schematic](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt%20Smart%207688.pdf)
* **[文件]** [Manual](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/Manual.zip)
* **[文件]** [OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
* **[文件]** [MediaTek LinkIt? Smart 7688 Resources:](http://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/hdk_intro/index.gsp)
* **[文件]**  [Firmware_upgrade_Instruction](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt_Smart_7688_Firmware_upgrade.zip)
* **[文件]**   [Certificates](https://github.com/SeeedDocument/LinkIt_Smart_7688/raw/master/res/LinkIt_Smart_7688-Certificate.zip)
