---
title: LinkIt Smart 7688 Duo
category: LinkIt
bzurl: https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html
oldwikiname:
prodimagename: cover.png
surveyurl: https://www.surveymonkey.com/r/LS_7688_Duo
sku: 102110017
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Linkit_7688_DUO_Product_view.jpg)

 LinkItTM Smart 7688 Duo（联发科物联网开发板）是基于 MT7688 ([联发科物联网开发板](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/MT7688_datasheet.pdf))和 ATmega32u4 的开放式开发板。 板与 Arduino Yun 编辑器兼容，并基于 OpenWrt Linux 发行版。 该板可以专门安装在智能家居或办公室的 Rich Application IoT 设备进行设计。 由于它与 Arduino 兼容，您可以他同时使用 Arduino Yun 和 LinkIt Smart 7688 Duo 的不同功能 。 这将帮助您制作各种基于 Arduino Yun 的有趣项目。 该板能够为您提供足够的内存和存储空间，来实现强大的视频处理功能。 可以通过 Python，Node.js 和 C 编程语言进行程序的编写来实现应用。


!!!Note
    本页仅引导您如何使用此开发板。 有关完整的指南，请参阅 [参考资料](http://labs.mediatek.com/en/platform/linkit-smart-7688#HDK) 。
    并且这里要注意，它一次只能有一个控制器作为主控制器。
    该板只是联发科 LinkItTM Smart 7688 平台的一部分，该平台包括其他开发板。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.13b873e5HE9its&id=524898724024)

## 产品特性


* 580 MHz MIPS CPU
* 单输入、单输出（1T1R）Wi-Fi 802.11 b / g / n（2.4G）
* 针对 GPIO，I2C，I2S，SPI，SPIS，UART，PWM 和以太网端口引脚
* 32MB 闪存和 128MB DDR2 RAM
* 能够通过 USB 数据线连接主机
* 具有 Micro SD 插槽
* 支持 Arduino API（ATmega32U4）

## 创意应用


* IoT /网关设备
* 机器人

## 规范



* MPU
    * 芯片组：MT7688AN
    * 核心：MIPS24KEc
    * 时钟速度：580MHz
    * 工作电压：3.3V
* MCU
    * 芯片组：ATmega32U4
    * 核心：Atmel AVR
    * 时钟速度：8MHz
    * 工作电压：3.3V
* 存储
    * Flash：32MB
    * RAM：128MB DDR2
* GPIO
    * 针数：3（MT7688AN），24（ATmega32U4）
    * 电压：3.3V
* PWM
    * 针数：8（Atmega32U4）
    * 电压：3.3V
    * 最大分辨率：16位（可定制）
* ADC
    * 针数12（ATmega32U4）
    * 分辨率：10位
* 外部中断：8
* SPI / SPIS
    * 针号：S0，S1，S2，S3
    * 最大速度：4MHz
* I2C
    * 针数：D2 / D3
    * 速度：400KHz
* UART Lite
    * 一个为 ATmega32U4，另一个为 MT7688AN
    * 针号：P8 / P9（MT7688AN），D​​0 / D1（ATmega32U4）
* USB主机
    * 针数：P6 / P7
    * 连接器类型：Micro-AB
* 通信
    * Wi-Fi：1T1R 802.11 b / g / n（2.4G）
    * 以太网：1端口10/100 FE PHY
    * 针数：P2 / P3 / P4 / P5
* 用户存储：SD卡Micro SD / SDXC
* 尺寸：60.8x26.0mm


## 硬件概况

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Front_component_view_with_text_1200_s.jpg)

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/7688_duo_backview_with_text_1200.jpg)

## 入门指导

### 连接到嵌入式操作系统

!!!Note
    手册中介绍了两种方法。 在这种情况下，我们只显示一个先进的方法（使用USB串行到适配器），看起来有点困难。 但是，从长远来看，你会受益匪浅。

#### 所需材料

* LinkIt Smart 7688 x 1
* USB数据线（type A to micro type-B）x 1
* USB 串行接口x 1
* 跳线x 3
### 在 Windows 上

**1** 安装 [PuTTy](http://www.putty.org/)。 PuTTY 提供使用 SSH（Secure Socket Shell）的系统控制台环境来访问开发板的操作系统。

**2** 安装 [Bonjour](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US)  打印服务（适用于Windows 7，Windows 8，Windows 10）。


**3** 安装驱动程序 如果您使用基于 FTDI 芯片的 USB 数据线，请从 [这里](http://www.ftdichip.com/Drivers/VCP.htm) 下载并安装其驱动程序。 如果您遇到最新驱动程序问题，请尝试安装
 [旧版本](http://www.ftdichip.com/Support/Documents/InstallGuides.htm)。

**4** 接下来，您需要将 Serial-to-USB 连接到 LinkIt Smart 7688 的UART引脚，如下表所示：


| 在USB适配器上的引脚 |	 在LinkIt Smart 7688上连接相应的引脚 |
|-----------------------------------|--------------------------------------------------------|
| 引脚 RX	| 引脚 8 |
|引脚 TX	|引脚 9 |
| 引脚 GND |	引脚 GND |

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/7688_duo_demo_view_1200_s.jpg)

**5** 连接串行到 USB 数据线后，打开设备管理器并注意 **COM** 端口号，如图22所示。该数字可能因不同的计算机而异。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/COM_port.jpg)

 **6** 启动 PuTTY 终端，输入设备管理器中 USB 设备的 COM 端口号，单击“串口”按钮，在“速度”框中输入57600，单击“打开”，如图23所示。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Putty_configuration.jpg)

 **7** 要退出系统控制台，请单击 PuTTY 窗口右上角的关闭图标。

### 在 Mac 上

 **1** 如果需要，安装驱动程序。 请查阅数据线制造商的网站了解 Mac 上的驱动程序要求和安装说明。

**2.** 将数据线插入PC /笔记本电脑，并将连接线连接到 LinkIt Smart 7688。

**3** 打开终端会话。


**4** 在终端中输入 **ls / dev / cu***。 您应该看到设备列表。 寻找类似于 cu.usbserial-XXXXXXXX 的东西，其中 XXXXXXXX 通常是一个随机标识符。 这是用于访问系统控制台的串行设备。

**例如:**

```
$ls /dev/cu*

/dev/cu.Bluetooth-Incoming-Port

/dev/cu.Bluetooth-Modem

/dev/cu.pablop-WirelessiAP

/dev/cu.usbserial-A6YMCQBR

```

**5.** 使用屏幕实用程序连接到串口，并将波特率设置为57600，这是因为默认情况下系统控制台的波特率为57600。 例如：
```
$screen /dev/cu.usbserial-XXXXXXXX 57600
```

**6.** 现在您应该连接到系统控制台。 在终端中按 ENTER 键显示提示。 您将注意到，提示与您的 OSX 终端应用程序不同，它是 LinkIt Smart 7688 提示符，它类似于以下内容：
```
  root@myLinkIt:/#
```

**7.** 您可以通过此控制台更改 LinkIt Smart 7688 系统。

### 在 Linux 上


**1.** 如果需要，安装驱动程序。 请查看USB转串口适配器制造商的相关网站了解 Linux 上的驱动程序要求和安装说明。


**2.** 插入数据线并将电缆连接到 LinkIt Smart 7688 Duo。

**3.** 打开终端会话。


**4.** 在终端中输入 **ls / dev / ttyUSB**。 您应该看到设备列表。 寻找类似于 cu.usbserial-XXXXXXXX 的东西，其中 XXXXXXXX 通常是一个随机标识符。 这是用于访问系统控制台的串行设备。 例如：
```
$ls /dev/ttyUSB*
/dev/ttyUSB0
```
**5.** 使用屏幕实用程序连接到串行端口，并将波特率设置为 57600。 这是因为默认情况下系统控制台的波特率为57600。 例如：
```
$sudo screen /dev/ttyUSB0 57600
```
 **6.** 现在您应该连接到系统控制台。 在终端中按 ENTER 键显示提示。 您将注意到，提示已成为不同的常规应用程序，它是 LinkIt Smart 7688 提示符，它类似于以下内容：
```
  root@myLinkIt:/#
```
**7.** 您可以通过此控制台更改 LinkIt Smart 7688系统。

### 运行 Blink 示例

#### 所需材料


* LinkIt Smart 7688 x 1
* USB数据线（type A to micro type-B）x 1
* USB连接到串行适配器x 1
* 跳线x 3

#### 运行 Blink


**1.** 使用 micro USB 数据线打开电路板（仅连接 USB 电源接口，而不是 USB 主机接口）。


 **2.** 启动 PuTTy 并使用 USB 数据线连接至串行适配器再连接到系统，如前几节所示。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Connect_to_computer.jpg)


**3.** 输入 **python /IoT/examples/blink-gpio44.py**，然后按 **Enter** 以运行 Blink 示例。


!!!note
    请注意，在第一个单词“python”之后有1个空格，否则将不会找到该示例。

**4.** 大约2秒钟后，您会注意到 Wifi LED 稳定闪烁。

**5.** 在系统控制台中，输入 **CTRL + C**，这将终止示例。

### 连接到互联网（切换到站模式）

有两种 Wi-Fi 模式：AP模式和站模式。 请参考这里的差异。

**1.** 使用 micro USB 数据线打开电路板。


**2.** 打开计算机上的 Wi-Fi 连接的程序，并连接到名为 LinkIt_Smart_7688_XXXXXX 的接入点。 XXXXXX 是一种不同硬件的标识符，各种板有各种板的不同的标识符。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Connect_wifi.jpg)


**3.** 打开带有 mylinkit.local / 或 192.168.100.1 网址的浏览器，设置 root 的密码并登录。单击右上角的“网络”。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Network_conf.jpg)

**4.** 选择站模式，然后单击右侧的刷新或向下箭头以查找要连接的 AP。 选择 AP 后，如果需要，请输入密码。 单击配置并重新启动完成，如下所示。 然后等待约 30 秒钟可以切换模式。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Station_mode.jpg)

**5.** 启动 PuTTy，并使用 USB 串行适配器连接到系统，如上一节所示。

**6.** 键入 ifconfig 并找到 inet addr 的IP地址，如下所示：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/IFCONFIG.jpg)

!!!Note
    重新启动系统后仍将进入“站”模式。 按 Wi-Fi 按钮至少 5 秒钟切换回 AP模式。 注意：需要使用 reboot 命令重启嵌入式操作系统。

 **7.** 在浏览器的新 Tab 中输入 IP，您可以登录到 Web 用户界面配置系统。

 **8.** 现在主机和 LinkIt Smart 7688 都连接到互联网。 在控制台中输入 ping [www.mediatek.com](www.mediatek.com)，您将得到：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Ping_result.jpg)

 **9.** 现在您可以使用互联网在开发板上配置系统。


### 安装 Arduino 编程环境


该开发板具有与 Arduino 兼容的功能。 因此，您可以将 Arduino 代码应用于 7688 平台，从而使开发流程更加快捷。 在本节中，我们将向您展示如何构建 Arduino 编程环境。

#### 下载并安装 Arduino IDE

您可以在计算机上安装 Arduino IDE 1.6.5。

为 LinkIt Smart 7688 平台配置 Arduino IDE

#### 安装开发板支持包


Arduino IDE 1.6.5支持使用 **Board Manager** 工具进行第三方板集成。 LinkIt Smart 7688 开发板是 Arduino IDE 的插件，您需要安装板卡，以便 Arduino 支持 LinkIt 板卡。 请按照以下步骤进行：

**1** 在 Arduino IDE 中，在文件菜单上单击首选项，然后插入

````
http://download.labs.mediatek.com/package_mtk_linkit_smart_7688_test_index.json
````

到附加板管理器 URL 字段：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Install_package.jpg)


**2.** 确保您的计算机已连接到互联网 [下载](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/LinkIt.zip) **LinkIt**，解压缩它，并将文件复制到文件夹 **packages**，它获得相同的位置 与文件 **Preferences.txt**。 点击以下红色矩形标记部分打开 **Preferences.txt** 的文件位置。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/7688_duo_demo_preferences.txt_location_s.jpg)

**3.** 在Arduino **工具** 菜单中指向 **板**。

 **4.** 现在应该有一个 LinkIt Smart 7688 项目出现在 Boards Manager 的主板列表中，并选择带有 **COMxx** （**LinkIt Smart 7688 Duo**）的端口。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Install_SDK.jpg)

**5.** 安装完成。

### 安装 LinkIt Smart 7688 Duo COM 端口驱动程序

安装板包之后，将 LinkIt Smart 7688 Duo 连接到计算机，您应该在设备管理器中看到一个带有以下端口 ID 的 USB 串行端口：

* 引导加载程序COM 端口：VID = 0x0E8D，PID = 0xAB00
* Arduino Sketch COM 端口：VID = 0x0E8D，PID = 0xAB01

接下来，您将需要根据操作系统安装驱动程序。 步骤是：

!!!Note
    对于 Windows 10，无需安装驱动程序。 但是，需要额外的步骤来确保 Windows 10 识别出该板。 将 LinkIt Smart 7688 Duo 连接到 Windows 10 机器，然后在 700 毫秒内快速按下 MCU 复位按钮两次。 该系统现在应该将 LinkIt Smart 7688 Duo 识别为 USB串行设备（COM5）。 不同机器上的数字5可能不同。 您只需要第一次将该电路板连接到 Windows 机器上即可。

!!!Note
     对于 Windows 8，系统可能会阻止驱动程序的安装。 请在 Windows 8 上禁用驱动程序签名强制。禁用签名强制后，请按照以下 Windows 7 中的步骤安装驱动程序。

!!!Note
    对于Windows 7，请在以下路径中找到串行COM端口INF驱动程序。 您也可以从这里安装。
{ARDUINO_IDE_PREFERENCE_LOCATION}Arduino15/packages/LinkIt/hardware/avr/0.1.5/driver/linkit_smart_7688.inf

 您将在 **File（文件） - >Preferences（首选项）** 中找到 Arduino 首选项位置，请参阅 **preferences.txt路径**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Preference_location.jpg)


右键单击 linkit_smart_7688.inf 并选择安装，出现安全窗口，**单击安装此驱动程序软件**。 这完成了驱动程序的安装。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Driver_inst_alert.jpg)


* 对于Ubuntu Linux，它应该没有安装驱动程序。 LinkIt Smart 7688 应该在/ dev文件夹中，并安装为 ttyUSB0。 每个 Ubuntu 机器上的 **数字0** 可能不同。
* 对于 OS X，也不需要安装驱动程序，LinkIt Smart 7688 Duo 作为串行设备安装在/ dev / tty.usbmodem1413 下。 每个OS X 机器上的号码 1413 可能不同。


### 演示: 一个输出 Hello world 的例子

!!!Note
    为了避免本地应用程序开发中的内存不足，您应该在更强大的主机环境中设置本机应用程序进行开发环境，从而使您能够交叉编译 LinkIt Smart 7688 目标的可执行格式。 下表显示了 LinkIt Smart 7688 编程语言和主机上相关开发环境的概述。

### Python

 **1.** 使用 FileZilla 参考这个[tutorial](https://wiki.filezilla-project.org/FileZilla_Client_Tutorial_%28en%29)，服务器IP（替换 **主机名**）的地址是 inet addr 在以前的[切换到station模式](https://seeeddoc.github.io/LinkIt_Smart_7688_Duo#Switch_to_Station_mode)部分中找到，用户名是 root，密码是该部分中设置的密码。

**2.** 打开文本编辑器，复制并粘贴以下示例代码，并将其保存为 **helloworld.py**。
```
print "Hello World!"
```
**3.** 使用 FileZilla 将文件 **helloworld.py** 复制到目标开发环境（LinkIt Smart 7688）的系统中，将其放在文件夹 **root** 下。

**4.** 启动 PuTTy 并使用 USB连接到串行适配器连接到系统。

**5.** 将工作目录设置为 **/ root**，并输入 **python helloworld.py** 来执行。

**6.** 现在你可以看到 **Hello World !**  打印在控制台。

### Arduino

#### 在主机（Arduino side）

MCU side 被作为 Arduino 编辑页面进行程序编辑。 在本示例中，编辑器上简单地接收到从 MPU (Linux) 端发出的命令，并相应地点亮板子上的 LED。

 **1.** 首先，将 LinkIt Smart 7688 Duo 连接到 PC，然后打开 Arduino IDE，并将以下代码粘贴到IDE中：

```
void setup() {
    Serial.begin(115200); // open serial connection to USB Serial port (connected to your computer)
    Serial1.begin(57600); // open internal serial connection to MT7688
    // in MT7688, this maps to device
    pinMode(13, OUTPUT);
}
void loop() {
    int c = Serial1.read(); // read from MT7688
    if (c != -1) {
        switch(c) {
        case '0': // turn off D13 when receiving "0"
            digitalWrite(13, 0);
            break;
        case '1': // turn off D13 when receiving "1"
            digitalWrite(13, 1);
            break;
        }
    }
}
```

**2.** 然后从 IDE 中选择正确的 COM 端口（检查设备管理器），方法是单击 **Tools(工具) - >port(端口)**。

**3.** 将代码上传到电路板。 请注意，电路板上的灯尚未闪烁 - 您需要在 Linux 端编写一个程序使其闪烁，这是下一步。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/img/Blink_in_arduino.jpg)


#### 在开发板（Linux端）

**1.** 使用您选择的文本编辑器，并创建一个新文件（一个Python文件），然后复制以下代码并保存。


```
import serial
import time
s = None
def setup():
    global s
# open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
# the baudrate is set to 57600 and should be the same as the one
# specified in the Arduino sketch uploaded to ATmega32U4.
s = serial.Serial("/dev/ttyS0", 57600)
def loop():
# send "1" to the Arduino sketch on ATmega32U4.
# the sketch will turn on the LED attached to D13 on the board
s.write("1")
time.sleep(1)
# send "0" to the sketch to turn off the LED
s.write("0")
time.sleep(1)
if __name__ == '__main__':
setup()
while True:
loop()
```

 **2.** 在系统控制台中执行此 Python 程序 - 该程序基本上将 1 和 0 的字符串写入并映射到 Arduino 的 Serial1 接口的/ dev / ttyS0 端口上。 在上一节中上传的 Arduino 串口界面上将收到字符串，然后相应地让板上的 LED 闪烁。

您现在可以扩展 Arduino 编辑页面来驱动其他设备，如 PWM，I2C 设备，并通过扩展 Arduino 和 Linux 端之间的命令消息来同步状态。 如果需要更多的外设类型，可以使用一些外部库来实现通信协议。 这样的协议 - Firmata 在下面的部分描述。


## 资源下载

* [Hardware Schematic files](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/Hardware_Schematics.zip)
* [Manual](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/Manual.zip)
* [OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
* [MediaTek LinkIt? Smart 7688 Resources:](http://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/hdk_intro/index.gsp)
* [How to flash the firmware via a USB drive](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/Linkit_Smart_7688_DUO_Firmware.pdf)
* [Certificates](https://raw.githubusercontent.com/SeeedDocument/LinkIt_Smart_7688_Duo/master/res/LinkIt_Smart_7688_Duo-Certificate.zip)
