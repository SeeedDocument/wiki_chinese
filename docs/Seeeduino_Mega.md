---
title: Seeeduino Mega
category: Arduino
bzurl: https://www.seeedstudio.com/Seeeduino-Mega-p-717.html
oldwikiname: Seeeduino_Mega
prodimagename: Seeeduino_Mega_Cover.jpg
wikiurl: http://seeed.wiki/Seeeduino_Mega
sku: 102010007
---

![](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/Seeeduino_Mega_cover.jpg?raw=true)

Seeduino Mega 是一款从 Arduino Mega 改良的功能强大的微控制器。它的主芯片 ATmega2560 令 Seeeduino Mega 具有高达 70 个数字 I/O 接口，16 个模拟输入接口，14 个 PWM 输出接口，和 4 个 UART 接口。与 Arduino Mega 相比，Seeduino Mega 的体积减少了至少 30%，同时它完全与 [Seeed Shield products](https://www.seeedstudio.com/s/shield.html) 产品兼容。同时，Seeeduino Mega 继承了 Seeeduino 在细节上的优良设计，如可选择的工作电压 (3.3V/5V) 等。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.6a3405bezVooSW&id=45487738016)


## 创意应用

* 物联网  
* DIY
* 机器人
* 智能家居
* 3D 打印机
* 工业控制

这里有一些有趣的项目供您参考。

|8*8*8 LED Cube|Hexapod Robot|DIY Arduino 3D Printer|
|-------|-------|--------
|![](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/example_1.jpg?raw=true)|![](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/example_2.jpg?raw=true)|![](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/example_3.jpg?raw=true)|
|[点击制作](http://www.instructables.com/id/Arduino-Mega-8x8x8-RGB-LED-Cube/)|[点击制作](http://www.instructables.com/id/Arduino-Mega-Hexapod/)|[点击制作](http://www.instructables.com/id/Arduino-Controlled-CNC-3D-Printer/)|

## 产品特性

* 与大多数 Arduino Duemilanove 和 Diecimila Shields 兼容
* ATmega 2560 @ 16MHz
* 可选 5V/3.3V
* 70 个数字 IO 接口
* 16 个模拟输入接口
* 14 个 PWM 输出接口
* 4 个 UART 接口
* 外形小巧，比 Arduino Mega 小 30％
* 编程简单，不需要额外的硬件来加载固件 – 只需插入 USB 端口，您就可以开始了。
* ICSP 接头
* 可以通过电池或交直电压转接器供电

## 规格参数

|项目|参数|
|------------|-----------|
|Microcontroller|ATmega2560|
|工作电压|5V/3.3V|
|输入电压|7-12V|
|数字 I/O 接口|70|
|PWM 接口|14|
|模拟输入接口|16|
|每个 I/O 接口的直流电流|20 mA|
|Flash|256 KB|
|RAM|8 KB|
|EEPROM|4 KB|
|时钟频率|16 MHz|


## 硬件概述

下图是 Seeeduino Mega 硬件功能的总览。引脚图中显示了 Seeeduino Mega 各引脚的引脚功能和备用功能。

![](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/Seeeduino_Mega_hardware1.png?raw=true)


- **Mini USB** :
Mini USB 端口用于连接电路板到您的电脑进行上电和编程。
- **Mode Switch** :
滑动开关用于开启或关闭自动重置和上传。
- **Power Switch** :
滑动开关用于将电路板的电压输出更改为 5V 或 3.3V。现在许多前沿的传感器正在开发在 3.3V 下工作，当使用其他 duino 板时，您需要在主板和这些传感器之间使用逻辑电平转换器，当使用 Seeeduino Mega 时只需滑动开关就可以了 !
- **DC Input** :
DC 输入使得您的 Seeeduino Mega 可以通过墙式转接器供电，因此需要的话可以为您的项目提供更多电力，例如使用直流电机或其他高功率设备时。直流电压输入是 7V-12V。上电峰值电流为 2A，因此 DC 电源是 USB 电源的最佳选择。
- **Reset** :
此按钮位于侧面，即使堆叠了扩展板，您也可以重置 Seeeduino。这和在其他 Arduino 板上，按钮在顶部使得难以重置情况不同。
- **ICSP** :
这是 ATmega328P 的 ICSP 连接，位于 Arduino Uno，Due，Mega 和 Leonardo 兼容硬件(例如扩展板)的标准 ICSP/SPI 接头处。这个端口的 SPI 引脚 : MISO，SCK 和 MOSI，也分别连接到数字引脚 12,13和 11，就像 Arduino Uno 的一样。
- **Digital Pins** :
Seeeduino Mega 有多达 70 个数字引脚。点击 [这里](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/res/Seeeduino%20Mega%20pin%20mapping.pdf) 查看 Arduino 引脚和 Atmega2560 引脚之间的引脚映射。Mega 上的 70 个数字引脚中的每一个都可以用作输入或输出，使用 pinMode()，digitalWrite() 和 digitalRead()函数。推荐工作条件下每个引脚可以提供或接收 20mA，并有一个 20-50kΩ 的内部上拉电阻(默认断开)。为了避免微控制器的永久损坏，最大值不得超过 40mA。另外，一些引脚具有专门的功能 :
	* Serial (串口) : 0 (RX) 和 1 (TX); Serial 1: 19 (RX) 和 18 (TX); Serial 2: 17 (RX) 和 16 (TX); Serial 3: 15 (RX) 和 14 (TX). 用于接收 (RX) 和发送 (TX) TTL 串行数据。引脚 0 和 1 也连接到 ATmega16U2 USB-to-TTL 串行芯片的对应引脚。
	* External Interrupts (外部中断) : 2 (interrupt 0)，3 (interrupt 1)，18 (interrupt 5)，19 (interrupt 4)，20 (interrupt 3)，和 21 (interrupt 2)。这些引脚可以配置为在低电平，上升沿或下降沿或电平变化时触发中断。详情请参阅 attachInterrupt() 函数。
	* PWM : 2 至 13 和 44 至 46，通过 analogWrite() 函数产生 8 位 PWM 输出。
	* SPI : 50 (MISO)，51 (MOSI)，52 (SCK)，53 (SS)。这些引脚支持 SPI 通信。 SPI 引脚也在 ICSP 接头上，与 Arduino /Genuino Uno 兼容。
	* LED : 13。有一个内置 LED 连接到数字引脚 13.当引脚为高电平时，LED 亮，当引脚为低电平时，LED 熄灭。
	* TWI : 20 (SDA) 和 21 (SCL)。通过 Wire library 支持 TWI 通讯。请注意，这些引脚与旧 Duemilanove 或 Diecimila Arduino 板上的 TWI 引脚不在同一位置。
	* Analog : Mega 2560 有 16 模拟输入，每一个提供 10 位的分辨率。默认情况下，输入电压为 0-5V，可以使用 AREF 引脚和 analogReference() 函数来改变其范围的上限。
	* AREF : 模拟输入的参考电压。与 analogReference() 函数一起使用。
	* Reset : 将此引脚置低电平以重置微控制器。
	* 未标记引脚 : 操作寄存器。

## 驱动安装

首先需要:

* **准备一根 Micro-USB 线缆** :
准备一根 [Micro-USB 线缆](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.bf2ee4eSLeuFO&id=521385344999)；Android 手机的数据线也可以。

* **连接主板** :
使用 USB 线缆将 Arduino 板连接到电脑。绿色电源 LED (标记为 **PWR**) 应亮。


**对于 Windows 系统**

!!!Note
    此驱动器用于 Windows XP，Windows Vista，Windows 7，Windows 8/8.1 和 Windows 10。

[![enter image description here](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/download_driver.png?raw=true)](https://github.com/Seeed-Studio/Signed_USB_Serial_Driver/archive/master.zip)

- 插入您的电路板并等待 Windows 开始驱动程序安装过程。过了一会儿，尽管付出了最大的努力，但还是失败了。
- 点击开始菜单，打开控制面板。
- 在控制面板中，跳转到系统和安全。接下来，点击系统。系统窗口启动后，打开 **Device Manager**。
- 查看端口 (COM & LPT) 下。您应该找到一个名为 "Seeeduino Mega" 的开放端口。如果没有 COM＆LPT部分，请查看其他设备下的未知设备。
- 右键单击 "Seeeduino Mega" 端口并选择 "Update Driver Software" 选项。
- 接下来，选择 "Browse my computer for Driver software" 选项。
- 最后，跳转到并选择名为 "Seeeduino Mega.inf" 的驱动程序文件
- Windows将驱动程序安装。

**对于 Mac OSX 系统**

无需安装任何驱动


## 入门指导

!!!Note
    在 Windows 10 中的 Arduino 1.6.9 进行。

首先安装一个 Arduino 软件。

[![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Stalker_V3_1/master/images/Download_IDE.png)](https://www.arduino.cc/en/Main/Software)


**启动 Arduino 程序**

双击之前下载的 Arduino 程序 (arduino.exe) 。

!!!Note
    您可以在首选项对话框中更改语言选项。有关详细信息，请参阅[Arduino Software (IDE) page](https://www.arduino.cc/en/Guide/Environment#languages)。


**打开 Blink 示例**

打开 LED blink 示例 : **File(文件) > Examples(示例) >01.Basics > Blink**.

![enter image description here](https://github.com/SeeedDocument/Seeeduino_GPRS/blob/master/img/select_blink.png?raw=true)

**添加 Seeeduino 到 Arduino IDE**

点击 **File > Preference**, 把以下 url 输入 Additional Boards Manager URLs :
    *https://raw.githubusercontent.com/Seeed-Studio/Seeeduino-Boards/master/package_seeeduino_index.json*

点击确定完成设置。然后通过 **Tools > Board > Boards Manager**，找到 **Seeeduino by Seeed Studio**，并安装它。

![enter image description here](https://github.com/SeeedDocument/SeeeduinoV4/blob/master/images/add_board.png?raw=true)

**选择主板类型**

在 **Tools > Board** 中选择与您的 Arduino 对应的主板。选择 **Seeeduino Mega 2560**

![enter image description here](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/mega_arduino_ide.png?raw=true)

**选择串口**

从 Tools | Serial Port  菜单中选择 Arduino 板的串口。可能是 COM3 或更高 (COM1 和 COM2 通常保留给硬件串口)。您可以断开 Arduino 板并重新打开菜单进行检验;消失的端口对应 Arduino 板。重新连接电路板并选择该串行端口。

![enter image description here](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/img/select_com_seeeduino_mega.png?raw=true)

!!!Note
    对于 Mac 系统，应该修改 **/dev/tty.USBmodem** 中的一些信息。

**上传**

现在，只需点击 "Upload" 按钮。等待几秒钟，如果上传成功，则消息 "Done uploading" 会出现在状态栏中。

![enter image description here](https://github.com/SeeedDocument/Seeeduino_GPRS/blob/master/img/upload_image.png?raw=true)

上传结束后，您会看到电路板上的引脚 **13** (L) LED 开始闪烁(橙色）。 如果是这样，恭喜! Arduino 正常运行了。如果您遇到问题，请参阅故障排除建议。

## Linux 入门指导

使用 Linux 的用户，请点击 [Installing Arduino on Linux](http://playground.arduino.cc/Learning/Linux)



## 资源下载

  **[Eagle 文件]** [Seeeduino Mega Eagle File](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/res/Seeeduino_Mega_v3.0.zip)

  **[引脚图 PDF]** [Seeeduino Mega Pin Mapping PDF](https://github.com/SeeedDocument/Seeeduino_Mega/blob/master/res/Seeeduino%20Mega%20pin%20mapping.pdf)

  **[其他资源]** [Getting Started with Arduino](https://www.arduino.cc/en/Guide/HomePage)

  **[其他资源]** [Arduino Language Reference](https://www.arduino.cc/en/Reference/HomePage)

  **[其他资源]** [Download the Arduino Software(IDE)](https://www.arduino.cc/en/Main/Software)

  **[其他资源]** [Arduino FAQ](https://www.arduino.cc/en/Main/FAQ)

  **[其他资源]** [Arduino Introduction](https://www.arduino.cc/en/guide/introduction)

  **其他资源[]** [Wikipedia page for Arduino](https://en.wikipedia.org/wiki/Arduino)

  **[其他资源]** [Arduino Mega](https://www.arduino.cc/en/Main/ArduinoBoardMega2560?setlang=en)

## FAQ

**What is the different between Arduino Mega with Seeeduino Mega?**

Seeeduino Mega is a powerful microcontroller derived from Arduino Mega. And there are the mainly difference list:

* Use a mini USB to power and program
* Add 3.3/5V system power switch
* Add automatic reset mode swtich
* Smaller size
