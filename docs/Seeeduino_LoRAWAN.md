---
title: Seeeduino LoRaWAN
category: Arduino
bzurl: http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html
oldwikiname:
prodimagename: cover.png
wikiurl: http://seeed.wiki/Seeeduino_LoRAWAN
sku: 102010026
---

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/cover.png)

Seeeduino LoRaWAN W / GPS是嵌入了LoRaWan协议和GPS功能的Arduino开发板，通过这款开发板您可以快速上手并且体验到LoRa在物联网领域的优势。基于通信模块RHF76-052AM，Seeeduino LoRaWAN与LoRaWAN A / C类兼容，支持多种通信频率。


4个板载标准Grove连接器使Seeeduino LoRaWan能够方便地与Seeedstudio的数百个Grove传感器和执行器连接，从而使用户能够更加专注于应用程序本身，而不必担心不同模块之间的兼容性问题。此外，该板还嵌入了集成的锂电池管理芯片，可以通过USB接口对电路板进行充电。在低功耗模式下，充满电的锂电池可以为电池供电数月。

如果您想快速建立一个物联网应用程序，Seeeduino LoRaWAN将是您的最佳选择。


|产品版本|版本日期 | 购买方式|
|-------|-------------|----------|
|Seeeduino LoRaWAN |Dec 20, 2016|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.5e478797AMbAbP&id=556001961806)|
|Seeeduino LoRaWAN W/GPS |Dec 20, 2016|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.5e478797AMbAbP&id=543820324424)|

!!!Warning
    请在第一次使用时更新固件。

!!!Tip
    Seeeduino LoRaWAN W / GPS由GPS模块和LoRaWAN模块组成。

##产品特性

* 最小电流 (3.7V 锂电池) - 2mA
* 最小电流 (3.7V 锂电池 & 去掉 PWR LED) - 80 uA

###Arduino/Processor（处理器）

* ATSAMD21G18 @ 48MHz with 3.3V logic/power
* Arduino compatible (based on Arduino Zero bootloader)
* Embedded with lithium battery management chip and status indicator led
* 20 GPIOs
* 4 on-board Grove connectors
* 18 x PWM pins
* 6 x analog inputs
* 1 x analog output (A0)
* 3.3V regulator with 200mA output
* Reset button

###LoRaWAN/RHF76-052

* 1.45uA sleep current in WOR mode (Spec of the modules, not the board)
* High link budget of 160dB. -140dBm sensitivity and 19dBm Output power.
* Dual band, 434/470MHz and 868/915MHz
    * 19dBm@434MHz/470MHz
    * 14dBm@868MHz/915MHz
* Support LoRaWAN protocol, Class A/C
* Ultra long range communication
* Ultra low power consumption
* Firmware upgrade
* Small size: 23mm X 28mm with 33 pin SMT package

!!!Warning
    与大多数Arduino和Genuino板不同，Zore运行在3.3V。I / O引脚可承受的最大电压为3.3V。将高于3.3V的电压施加到任何I / O引脚可能会损坏电路板。

##规格参数

| 项目|数值|
|--------------|-------------------------------------|
|微处理器 |ATSAMD21G18, 32-Bit ARM Cortex M0+ |
|工作电压	|3.3V|
|Digital I/O Pins	|20|
|PWM Pins	|All but pins 2 and 7|
|UART	|2 (Native and Programming)|
|Analog Input Pins|	6, 12-bit ADC channels|
|Analog Output Pins	|1, 10-bit DAC|
|外部中断	|All pins except pin 4|
|直流电流 I/O Pin	|7 mA|
|Flash Memory	|256 KB|
|SRAM	|32 KB|
|EEPROM	|None|
|Clock Speed	|48 MHz|
|长	|68 mm|
|宽	|53 mm|
|净重	|19.6g(without GPS), 19.9(with GPS)|

##创意应用

* 物联网
* 安保
* 智能家居
* 智能电网
* 智能农场
* 智能公园

!!!Tip
    - 使用Grove模块扩展您的应用程序



板上有4个Grove连接器。如果这是您第一次听说Grove，请点击 [Grove System](http://seeed.wiki/Grove_System/) 获取更多详细信息。简而言之，Groves系统是由数百种标准统一的传感器，执行器，显示器以及通讯模块组成的标准化系统。

##硬件概述

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/hw_LoRa.png)

* **1.** Micro USB - Programming and supply power to the board
* **2.** Grove connectors
* **3.** JST2.0 Lipo battery input (3.7V) and charge status led
* **4.** DFU Button - Firmware mode button
* **5.** Reset Button
* **6.** Arduino Pinout
* **7.** ICSP pins
* **8.** Firmware mode led
* **9.** Wire antenna
* **A.** uFL antenna
* **B.** RF module - RHF76-052AM
* **C.** ARM Cortex M0 processor - ATSAMD21G18
* **D.** LEDs
    * ***RX/TX*** - 当有UART数据传输时会闪烁(from/to USB)
    * ***L*** - an led connect to D13
    * ***PWR*** - power

!!!Tip
    - 如果要使用4板载Grove连接器，请使用命令digitalWrite（38，HIGH）打开VCC。否则您无法为Grove模块提供电源。

##管脚图

|Pin 名称|GPIO 编号|外部中断|PWM|Analog In|Analog Out|功能|
|--------|--------|-----------|---|---------|----------|--------|
|0       |#0      |YES        |YES|         |          | RX(Serial)|
|1       |#1      |YES        |YES|         |          | TX(Serial)|
|2       |#2      |YES        |   |         |          |        |
|3       |#3      |YES        |YES|         |          |        |
|4       |#4      |           |YES|         |          |        |
|5       |#5      |YES        |YES|         |          |        |
|6       |#6      |YES        |YES|         |          |        |
|7       |#7      |YES        |   |         |          |        |
|8       |#8      |YES        |YES|         |          |        |
|9       |#9      |YES        |YES|         |          |        |
|10      |#10     |YES        |YES|         |          |        |
|11      |#11     |YES        |YES|         |          | SPI_MOSI|
|12      |#12     |YES        |YES|         |          | SPI_MISO|
|13      |#13     |YES        |YES|         |          | SPI_SCK|
|SDA     |#20     |YES        |YES|         |          |        |
|SCL     |#21     |YES        |YES|         |          |        |
|A0      |#A0     |YES        |YES|YES      |YES       |        |
|A1      |#A1     |YES        |YES|YES      |          |        |
|A2      |#A2     |YES        |YES|YES      |          |        |
|A3      |#A3     |YES        |YES|YES      |          |        |
|A4      |#A4     |YES        |YES|YES      |          |Voltage of Battery|
|A5      |#A5     |YES        |YES|YES      |          |Charge Status|

!!!Note
    - 所有的引脚都可以作为数字信号的输入/输出。


##入门指南 - Arduino IDE

!!!Note
    - 这个指南是基于Win10 和 Arduino IDE v1.6.0

首先您需要安装最新的 Arduino IDE, 然后点击这里将 [Seeeduino LoRa](http://wiki.seeed.cc/Seeed_Arduino_Boards/) 添加到您的 Arduino IDE。

###安装驱动 (For Windows)

当第一次插入电路板时，您应该会得到名为Seeeduino LoRaWAN的USB COM设备。点击下面的链接来下载开发板的驱动。


[![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/driver.png)](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/driver.zip)

为了确保驱动程序安装成功，请打开设备管理器以查看 **Seeeduino LoRaWAN** 是否存在。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/device_manager.png)

###闪烁
现在我们可以上传我们的第一个示例 - “闪烁”到Seeeduino LoRaWAN。

打开您的Arduino IDE，然后单击 **File（文件） > Examples（示例） > 01.Basics > Blink** 来打开例程或者复制以下代码：

```c
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second
}
```

然后,

点击工具>板> Seeeduino LoRaWAN


单击工具>端口以选择正确的端口号。（不要选择COM1）

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/blink1.png)

然后点击Arduino IDE左上角的上传按钮，几秒钟后例程上传成功。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/blink2.png)

如果上传成功，您将看到下图所示的红色信息，这时观察您的板载LED，看，它在闪烁！

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/blink3.png)

##电池

您可以通过3.7V 锂电池为电路板供电。产品套件中有一个JST2.0电缆，如果您不能找到带有JST2.0连接器的电池，您可以使用这根线缆。


!!!Warning
    - 确保电池的正极和负极连接正确，否则可能会损坏电路板。.

电池的充电状态引脚和正极引脚分别连接到A4和A5，可以通过编程检测电池的充电状态和测量电池电压。

复制并上传以下代码以检测电池状态。

```c
// battey of Seeeduino LoRaWAN

const int pin_battery_status  = A5;
const int pin_battery_voltage = A4;

void setup() {
    SerialUSB.begin(115200);
    pinMode(pin_battery_status, INPUT);
}

void loop() {

    int a = analogRead(pin_battery_voltage);
    float v = a/1023.0*3.3*11.0;        // there's an 1M and 100k resistor divider
    SerialUSB.print(v, 2);
    SerialUSB.print('\t');
    SerialUSB.println(digitalRead(pin_battery_status));

    delay(1000);
}
```
!!!Note
    - 充电时，状态值返回0；充电完成或无电池插入，状态值返回1。

##发送和接收示例

LoRaWAN模块拥有一个很好用的库，对于简单的应用程序，你甚至不需要很多关于LoRa的协议（协议是很复杂和难以阅读的）。请注意，如果您想要高级应用程序，您仍然需要一些关于LoRa协议的知识。您不需要下载库，它已经包含在包中。您可以在 **File（文件） > Examples（示例） > LoRaWAN** 中找到示例程序。

您需要2块Seeeduino LoRaWAN来完成这个例子，一个用于发送，另一个用于接收。

###发送

打开您的Arduino IDE，然后单击 **File（文件） > Examples（示例） > LoRaWAN > p2p_tx** 来打开例程，或者您可以复制下面的的代码。
该例程将会每隔3000 ms广播一次 "Hello World!"

```
// Seduino LoRaWAN - TX example
#include <LoRaWan.h>

void setup(void)
{
    SerialUSB.begin(115200);
    lora.init();
    lora.initP2PMode(433, SF12, BW125, 8, 8, 20);
}

void loop(void)
{
    lora.transferPacketP2PMode("Hello World!");
    SerialUSB.println("Send string.");
    delay(3000);
}
```

###接收

打开您的 Arduino IDE 点击 **File（文件） > Examples（示例） > LoRaWAN > p2p_rx** 来打开例程，或者您可以复制下面的的代码：

```
// Seduino LoRaWAN - RX example
#include <LoRaWan.h>

unsigned char buffer[128] = {0, };

void setup(void)
{
    SerialUSB.begin(115200);
    lora.init();
    lora.initP2PMode(433, SF12, BW125, 8, 8, 20);
}

void loop(void)
{
    short length = 0;
    short rssi = 0;

    memset(buffer, 0, 128);
    length = lora.receivePacketP2PMode(buffer, 128,  &rssi, 1);

    if(length)
    {
        SerialUSB.print("Length is: ");
        SerialUSB.println(length);
        SerialUSB.print("RSSI is: ");
        SerialUSB.println(rssi);
        SerialUSB.print("Data is: ");
        for(unsigned char i = 0; i < length; i ++)
        {
            SerialUSB.print("0x");
            SerialUSB.print(buffer[i], HEX);
            SerialUSB.print(" ");
        }
        SerialUSB.println();
    }
}
```

在两个例程都上传完毕后，打开接收板的串行监视器，检查是否可以获取一些数据如下所示：

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/monitor_rx.png)

!!!Note
    我们将很快为LoRa提供网关套件，我们将在套件的维基上添加关于APB和OTAA模式的入门。

##举个例子

W我们提供了很多有用的例子。您可以打开 **File（文件） > Examples（示例） > LoRaWan** 来获取更多的信息，这些例程包括：

* ABP
* OTAA
* p2p-rx
* p2p-tx

##GPS数据

!!!Note
    本章仅适用于Seeeduino LoRaWAN W / GPS。

复制下面的代码你Seeeduino LoRaWAN W / GPS。
```
void setup()
{
    Serial.begin(9600);
    SerialUSB.begin(115200);
}

void loop()
{
    while(Serial.available())
    {
        SerialUSB.write(Serial.read());
    }
    while(SerialUSB.available())
    {
        Serial.write(SerialUSB.read());
    }
}
```

打开串行监视器，然后您将从GPS获取数据。
![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/gps.png)

##低功耗、小电流

我们测试的最小电流为80uA（对于Seeeduino LoRaWAN）。请按照以下步骤操作。

    1、取下PWR LED（如果不取下此LED，电流将> 2mA）
    2、取下CHG LED
    3、将以下代码上传到您的主板。



```
#include <LoRaWan.h>
#include <EnergySaving.h>

EnergySaving nrgSave;

void blink()
{
    for(unsigned char i = 0; i < 5; i ++)
    {
        digitalWrite(13,HIGH);
        delay(500);
        digitalWrite(13,LOW);
        delay(500);
    }
}

void setup()
{
    for(unsigned char i = 0; i < 26; i ++)      // important, set all pins to HIGH to save power
    {
        pinMode(i, OUTPUT);
        digitalWrite(i, HIGH);
    }

    lora.init();
    blink();    
    lora.setDeviceLowPower();
    blink();    
    nrgSave.begin(WAKE_EXT_INTERRUPT, 7, dummy);    // buton on D7 to wake up the board
    nrgSave.standby();
}

void loop()
{
    blink();
    nrgSave.standby();
}

void dummy(void)
{
    // do something
}

// END File
```

##更新固件

固件版本为2.0.10，如果您想检查您的版本，请将以下代码上传到您的主板。
```
void setup()
{
    Serial1.begin(9600);
    SerialUSB.begin(115200);
}

void loop()
{
    while(Serial1.available())
    {
        SerialUSB.write(Serial1.read());
    }
    while(SerialUSB.available())
    {
        Serial1.write(SerialUSB.read());
    }
}
```
打开您的串口监视器，然后输入：
```
AT+VER
```
然后您将看到您的开发板当前的版本。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/VER.png)

如果要更新固件，则需要遵循几个步骤。

**步骤1**

将下列代码复制并上传到您的主板。

```c
// Update firmware to RHF76-052AM
#include <Arduino.h>

void setup()
{
    SerialDBG.begin(115200);
    SerialUSB.begin(115200);
}

void loop()
{
    while(SerialDBG.available())
    {
        SerialUSB.write(SerialDBG.read());
    }
    while(SerialUSB.available())
    {
        SerialDBG.write(SerialUSB.read());
    }
}

```

**步骤2**

将板卡的USB接头取下，然后插上，重新连接电脑，然后点击DFU按钮，等到固件模式LED开始闪烁您就可以进行下一步操作。

**步骤3**

点击下载最新的固件 .bin file.

[![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/firmware_bin.png)](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/rhf76-052am-v2.0.10-20160923.ebin%202.bin)

**步骤4**

打开PuTTy并连接到电路板

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/firmware_1.png)

!!!Tip
    - 您可以在这里找到最新的PuTTy：.php [http://www.extraputty.com/download.php](http://www.extraputty.com/download.php)

**步骤5**

将您的开发板和Putty相连，您将看到字母“C”不断地打印在屏幕上。点击**Files Transfer（文件传输） > Ymodem > Send**, 然后选择步骤4中下载的.bin file。

然后升级就开始了。
![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_LoRa/master/img/firmware_4.png)

##资源下载

* **[eagle原理图]** [Schematics in Eagle](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/202001246 Seeeduino LoRaWAN Eagle.zip)
* **[sketchup文件]** [Sketchup file(3D)](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/Seeeduino LoRaWAN.skp)
* **[RHF76-052 电气图]**  [CE certification of RHF 76-052](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/ce-rhf76-052.pdf)
* **[RHF76-052固件]** [RHF76-052 Firmware V2.0.10](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/rhf76-052am-v2.0.10-20160923.ebin 2.bin)
* **[数据手册RHF76-052AM]** [Datasheet of RHF76-052AM](https://github.com/SeeedDocument/Seeeduino_LoRa/raw/master/res/rhf-ds01500_rhf76-052_datasheet_v03.pdf)
