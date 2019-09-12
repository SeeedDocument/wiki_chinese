
# Arduino 作为 ISP

Arduino的实现有很多方面，其中最重要的一个环节就是每一块Arduino开发板都可以通过Arduino IDE进行简单的编程。仅仅只需要点击一下Arduino IDE上面的`Upload`按键就能将Arduino IDE上面的代码通过电脑的USB口传输到微处理器的Flash内存中。
(本文取自[Arduino - ArduinoISP](https://www.arduino.cc/en/Tutorial/ArduinoISP))

## The Bootloader

之所以会出现上面的说描述的便利得益于那微控制器每次复位都会运行得那段`Bootloader`代码,同时`Bootloader`通过串口与电脑的USB连接使用特别的协议和速度将用户编辑好了的代码上传微控制器里面。如果`Bootloader`没有检测到微控制和电脑是连接的，那么`Bootloader`将会直接执行你自定义的代码。

`Bootloader`在微控制内存的最后那片地址区域，为了实现上述的功能，所以不能像用户自定义代码那样重复编程。

## ATmega328P的内存分布图

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/MemoryMap.jpg)


通过`bootloader`可以提供微处理器与Arduino IDE的兼容性。你需要使用板载串行编程器(ISP)去刷写`bootloader`，因为ISP是通过微处理器几个特殊引脚去烧写程序的驱动，可以将程序下载到微处理的任意一个片区(包括`bootloader`)

## 使用Arduino作为ISP编程器 

针对所有`ATmega`系列的`bootloader`代码和合适的`fuses`配置以使之变成`Arduino`的整个过程都可以在`Arduino IDE`上面进行管理。`Arduino IDE`提供特别的菜单同时也运行你使用多种编程器，其中就烧写`bootloader`到其他`Arduino`的最常见的编程器`Arduino as ISP`选项

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/ISP_Programmers.jpg)


编程过程使用VCC，GND和四个数据引脚。其中有三个引脚直接将编程板和目标板的MISO,MOSI和SCK相连接，还有一个引脚则是编程板的10号引脚连接到目标板的复位引脚。

## 怎么连接你两个板子

下表显示了不同`Arduino`板上MOSI，MISO和SCK的引脚：

| Arduino / Genuino Board |     MOSI     |     MISO     |      SCK     | Level |
|:-----------------------:|:------------:|:------------:|:------------:|:-----:|
|    Uno or Duemilanove   | 11 or ICSP-4 | 12 or ICSP-1 | 13 or ICSP-3 |   5V  |
|   Mega1280 or Mega2560  | 51 or ICSP-4 | 50 or ICSP-1 | 52 or ICSP-3 |   5V  |
|         Leonardo        |    ICSP-4    |    ICSP-1    |    ICSP-3    |   5V  |
|           Due           |    ICSP-4    |    ICSP-1    |    ICSP-3    |  3,3V |
|           Zero          |    ICSP-4    |    ICSP-1    |    ICSP-3    |  3,3V |
|           101           | 11 or ICSP-4 | 12 or ICSP-1 | 13 or ICSP-3 |  3,3V |
|        MKR Family       |       8      |      10      |       9      |  3,3V |

The SPI interface - and therefore these pins - is the interface used to program the AVR microcontrollers. Note that MISO, MOSI, and SCK are available in a consistent physical location on the ICSP header; this connector is used also by shields that rely on the SPI interface allowing the design of shields that work on every board.

`SPI`接口为`AVR`微控制器做为编程接口.注意MISO,MOSI,和SCK也可以在开发板`ICSP`的接口上面使用.`SPI`也可以在每块开发板的拓展接口上面使用。

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/ICSPHeader.jpg)

On the Arduino UNO in the following image, we have highlighted in red the connections on the female strips; in yellow the ICSP connector that connects to the ATmega328P. Please note that the Rev.3 board has an ATMega16U2 chip that manages the USB connection and also that chip can be reprogrammed via a dedicated connector labeled ICSP2, just above the ATMega16U2 itself.

在下面的`Arduino UNO`图中，我们红色圆圈标记需要连接的接口；使用黄色的圆圈标记`ICSP`接口
请注意`Rev.3`开发板里面有负责管理USB连接的`ATMega16U2`芯片，我们可以使用开发板上面的`ICSP1`直接通过`ICSP2`将程序下载到负责管理USB连接的`ATMega16U2`芯片上。

[![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Uno_Connect.jpg)](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Uno_Connect.jpg)

一些`Arduino`开发板，MOSI,MISO和SCK都是11,12和13号数字引脚。这就是为什么许多教程指示您将目标连接到这些引脚的原因。如果您发现下图的布线更实用，请定义`USE_OLD_STYLE_WIRING`。 即使不使用`Uno`，这也可以使用。

[![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/ArduinoUNOtoUNO_ISP2.jpg)](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/ArduinoUNOtoUNO_ISP2.jpg)

正如上图所示，我们使用`old style`将两个`UNO`开发板进行连接从而去烧写`bootloader`。在上面的是目标板，在下面的是编程板。我们需要注意的是那根黄色的接线，它连接是编程板的D10引脚和目标板的复位引脚。在MKR系列的开发板中，你不能使用D10去复位。我们建议使用D6，同时您需要记住的是去修改`ArduinoISPsketch`的73行代码，将`#define RESET 10`修改为`#define RESET 6`

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Arduino_ISP_wires.jpg)


这是`Arduino NANO`使用`UNO`通过`ICSP`接口对其进行编程的连接图。

[![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/MegaToUNO.jpg)](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/MegaToUNO.jpg)

The Arduino MEGA above is programming an Arduino UNO connecting D51-D11, D50-D12, D52-D13, GND-GND, 5V-5V and D10 to RESET. This type of board needs a 10µF electrolytic capacitor connected to RESET and GND with the positive (long leg) connected to RESET. The capacitor has to be placed after the programmer board has been loaded with the ISP sketch.  
The 10µF electrolytic capacitor connected to RESET and GND of the programming board is needed only for the boards that have an interface between the microcontroller and the computer's USB, like Mega, Uno, Mini, Nano. Boards like Leonardo, Esplora and Micro, with the USB directly managed by the microcontroller don't need the capacitor.  

上图的`Arduino MEGA`正在对`Arduino UNO`进行编程，其连接方式为D51-D11, D50-D12, D52-D13, GND-GND, 5V-5V and D10-RESET。这种类型的开发板需要将10µF电解电容连接到RESET和GND之间，正极接到RESET(长正短负)，在下载进ISP代码后，必须将电容放在对应的位置。只有开发板上面有USB芯片的开发板采将电容放置在RESET和GND之间，其他的没有USB芯片则不需要这个电容。

## 关于电压

The Arduino family of boards includes 5V and 3.3V devices. When using an Arduino that is not 5V tolerant (Due, Zero, ...) as the programmer, make sure to not expose any of the programmer's pins to 5V. A simple way to accomplish this is to power the complete system (programmer and target) at 3V3

`Arduino`系列的开发板中有工作电压为5v的也有工作电压为3.3v的设备。当使用一些`Arduino`不支持5V电压的开发板(Due, Zero, ...) 作为编程器的时候，不能将编程器的引脚接到被5V供电的开发板上面。一个最简单方式就是两个开发板都供3.3V的电压。

[![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/MKR1000_ISP_UNO_2.jpg)](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/MKR1000_ISP_UNO_2.jpg)


如上图中的`MKR1000`和`UNO`接线方式。正如上述的那样，每个板子需要在3.3V下面工作，将`MKR1000`的VCC和GND分别接到`UNO`的5V和GND上面。根据这一页的引脚输出说明将其他4个引脚进行连接。我们使用与其他图片相同的颜色来帮助您轻松地从“旧布线”切换到ICSP连接器。请注意，MKR系列开发板共用相同的引脚排列，因此您可以将任何`MKR`开发板用作ISP编程器。如果您使用`MKR`开发板做为ISP编程器，记住一定要修改ArduinoISP代码中的73行宏定义，将其修改为您连接到目标板Reset引脚的引脚。

!!!note

    在你接线期间不能连接目标板的USB和电源，我们同时也建议您在连接目标板之前对编程板进行编程。

## 下载程序

The Arduino that you will use as programmer needs a specific sketch. You find it under Examples > 11\. ArduinoISP> ArduinoISP.  

你将`Arduino`使用你需要一个专门的代码，你可以在`Examples > 11 . ArduinoISP > ArduinoISP.`中找到

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/LoadSketch.jpg)


通过查看代码你会发现有很多参数，这些参数随着目标板的变化而变化。但是，这些参数由Arduino软件(IDE)支持的每个引导加载程序/板可用的特定文件设置。其他的参数也被注释将其清楚解释，一般不需要做修改。这个代码也支持通过3个LED将程序处理的情况进行视觉的反馈。


[![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Arduino_ISP_LEDSOK.jpg)](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Arduino_ISP_LEDSOK.jpg)



## 烧写bootloader



如果接好了所有的线，则需要通过选择开发板类型来选择不同的`bootloader`的二进制文件和`fuses`的配置。在烧写程序期间，会检查微控制的签名，虽然很多的开发板使用同一款微控制器但是有他们自己的`bootloader`。在`Tools`下面选择`Burn bootloader`,等待`Arduino IDE`下面的窗口的配置信息。

![](https://github.com/SeeedDocument/Arduino-as--ISP/raw/master/img/Burn.jpg)

## 串口编程模式

编程过程根据标准SPI编程协议管理三条SPI线(MISO，MOSI和SCK)，用于读写SD存储卡。 与存储卡的唯一区别是缺少CS(芯片选择)引脚。 在我们的AVR微控制器上，我们使用RESET引脚来停止执行任何草图或引导加载程序，并将微控制器置于特定状态，以便监听从SPI接口到达的命令。 协议所需的第一个命令是在_Serial Programming Mode_中进入微控制器的命令。

一旦该特定模式有效，我们就可以写入和读取所有微控制器可编程区域：闪存，EEPROM和熔丝。 在闪存的末尾，我们有`bootloader`程序代码区域，如本文开头的图像中突出显示的那样。 `Burn Bootloader`程序还根据电路板的设计正确设置了微控制器的`fuses`。 这是您必须刻录引导加载程序选择列表中的确切板模型的原因之一。

## 编程的技术方面


用于编程微控制器的开源软件工具是[avrdude](http://www.nongnu.org/avrdude/)。 该过程分为四个步骤：解锁芯片的引导加载程序部分，设置芯片上的`fuses`，将引导加载程序代码上传到芯片，锁定芯片的引导加载程序部分。

根据存储在与电路板相关的每个参数文件中的偏好来管理`fuses`，从而避免潜在的错误。


`fuses`的管理，通常是一组三个字节 - 低，高和扩展 - 是引导程序编程中最精细的方面：错误的保险丝设置可能会破坏微控制器和电路板。 保险丝定义了微控制器功能的许多方面，例如：选择不同的时钟源并改变芯片运行的速度，设置芯片工作前所需的最小电压(掉电)，设置是否使用引导加载程序，设置分配的内存量 引导加载程序(从256到2048字 -  512到4096字节)，禁用复位或串行编程，并在上载新草图时停止擦除EEPROM数据。

有关`fuses`的详细说明，请参见每个微控制器的数据表。每个设置都有自己的用法，允许开发人员锁定芯片并保护其免受ISP编程是合乎逻辑的，但可能会错误地以错误的方式设置`fuses`，通过ISP接口将您锁定在编程过程之外。 要恢复微控制器，您必须依靠使用12V来复位保险丝的高压串行编程器。

## 回顾：以8个步骤刻录Bootloader

* 打开ArduinoISPfirmware(在示例中)到您的Arduino板。
* Arduino 1.0的注意事项：你需要对ArduinoISPcode做一个小改动。 在heartbeat()函数中找到“delay(40);”的行。 并将其改为“延迟(20);”。
* 选择工具>电路板和串行端口菜单中与您作为编程器使用的电路板对应的项目(而不是正在编程的电路板)。
* 上传ArduinoISPsketch。
* 连接你的Arduino板..
* 选择工具>板菜单中与要刻录引导加载程序的板对应的项目(而不是您用作编程器的板)。 有关详细信息，请参阅环境页面上的板描述。
* 在工具>程序员菜单中选择Arduino作为ISP。
* 使用Burn Bootloader命令。



