---
title: Seeeduino Cloud
category: Arduino
bzurl: https://www.seeedstudio.com/Seeeduino-Cloud-Arduino-Yun-compatible-openWRT-controller-p-2123.html
oldwikiname: Seeeduino_Cloud
prodimagename: seeeduino_cloud_Cover.jpg
surveyurl: https://www.surveymonkey.com/r/Seeeduino_Cloud
sku: 102010021
---

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/seeeduino_cloud_cover.jpg)

Seeeduino Cloud是基于[Dragino WiFi IoT模块HE](http://www.dragino.com/products/linux-module/item/87-he.html)和ATmega32u4 的微控制器板。HE是一种高性能，低成本的150M，2.4G WiFi模块，这意味着中文的“核心”和内部的开源OpenWrt系统。Seeeduino Cloud也是Arduino兼容板，与Grove，Shield和IDE（Arduino IDE 1.5.3及更高版本）100%兼容。除了Arduino的正常接口，Seeeduino Cloud内置了以太网和WiFi支持，一个USB-A端口，非常适合那些需要网络连接和大容量存储的原型设计。使Seeeduino Cloud成为一个IoT网关也是一个好主意。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://www.seeedstudio.com/Seeeduino-Cloud-Arduino-Yun-compatible-openWRT-controller-p-2123.html)


## 创意应用

* 物联网  
* 智能家居
* 学习

这里有一些有趣的项目供您参考。

|简单的Wi-Fi Messager|将数据发送到Google文档|太阳能电池板监控系统|
|--------|----------|---------|
|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/example_1.jpg)|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/example_2.jpg)|![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/example_3.jpg)|
|[马上做一个](http://www.instructables.com/id/Arduino-Yun-Messager/)|[马上做一个](http://www.instructables.com/id/Google-Docs-and-the-Arduino-Y%C3%BAn/)|[马上做一个](http://www.instructables.com/id/Arduino-Yun-Solar-Panel-Monitoring-System/)|


## 产品特性

* 与Arduino Yun兼容
* 基于Dragino WiFi IoT模块HE
* 内置开源OpenWrt系统
* 支持 2.4Ghz WiFi, 802.11 b/g/n
* 支持以太网
* 支持 USB 2.0
* 板载Grove连接器

## 规格参数

因为Seeeduino Cloud有两个处理器，所以这一节显示了两个单独表格中每个处理器的特征。

**Dragino HE模块**

|参数|值|
|------------|------------|
|CPU|ATHEROS AR9331|
|Clock Speed|400MHz|
|RAM|64MB|
|Flash|16MB|
|OS|OpenWrt|
|Interfaces|2 x RJ45, 1 x USB Host, 1 x UART, 14 multiplex GPIOs|
|Power|3.3V Power Input|
|WiFi|Support 150M 2.4Ghz WiFi, 802.11 b/g/n|

**AVR Arduino微控制器**

|参数|值|
|------------|-------------|
|Microcontroller|ATmega32u4|
|Flash Memory|32KB|
|SRAM|2.5kB|
|EEPROM|1kB|
|Clock Speed|16MHz|
|Operating Voltage|5V|
|Digital I/O Pins|20|
|PWM Channels|7|
|Analog Input Channels|12|

## 硬件概述

下图显示了Seeeduino Cloud硬件功能的概述。引脚图中显示了Seeeduino Cloud各种引脚的功能。这可以作为快速参考。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/seeeduino_cloud_hardware.png)


* **RJ45以太网端口**
LAN端口连接到ATHEROS AR9331，并具有自己的IP地址，可用于Internet连接和设备管理。
* **USB 输入**
USB端口用于将电路板连接到PC进行编程和上电。Micro USB是大多数Android手机和其他设备中普遍存在的USB版本。你家里可能有几十根这些数据线。
* **USB HOST**
Seeeduino Cloud提供USB HOST功能，使其能够连接到各种USB设备，如网络摄像头，USB驱动器，键盘，操纵杆等。
* **32U4 RST**
按32U4 Reset 按钮对ATmega32U4 MCU进行复位. 通常，它用于程序复位.
* **SYS RST**
按下系统复位按钮将重新启动Linux系统。
* **Wi-Fi RST**
Wi-Fi重置按钮仅支持长按。5秒钟后按下并释放，将重置WiFi设置。其他设置将被保留。如果在30秒后按下并释放按钮，则会将所有设置重置为出厂默认值。
* **Grove Connectors**
SeeedStudio具有支持I2C或UART连接的各种传感器/设备。另外，我们销售独立的Grove连接器，以帮助您制作自己的传感器连接。如果要使用这些引脚，I2C Grove连接器也分别连接到SDA和SCL的模拟引脚A4和A5。UART Grove连接器分别连接到数字引脚0和1，用于RX和TX。
* **ICSP**
这是ATmega32U4的ICSP接口，它位于Arduino Uno，Due，Mega和Leonardo兼容硬件（例如屏蔽）的标准ICSP / SPI位置。该端口中的SPI引脚：MISO，SCK和MOSI也分别连接到数字引脚12,13和11，就像Arduino Uno那样。
* **I-PEX Connector**
这是一个用于外部天线的I-PEX连接器。
* **Pins**
因为Atheros AR9331所有I / O线都连接到ATmega32U4，所以不能访问Atheros AR9331的I / O引脚。32U4上的20个数字引脚中的每一个可以用作输入或输出，使用pinMode（），digitalWrite（）和digitalRead（）函数。它们工作在5伏。每个引脚可提供或接收最大40 mA，并具有20-50 kOhms的内部上拉电阻（默认情况下断开）。此外，一些针脚具有专门的功能：

	* Serial: 0 (RX) and 1 (TX).用于ATmega32U4硬件串行接收（RX）和发送（TX）TTL数据。请注意，在Seeeduino Cloud中，Serial类是指USB（CDC）通信; 对于引脚0和1上的TTL串行，使用Serial1类。Seeeduino Cloud上的ATmega32U4和AR9331的硬件连接在一起，用于在两个处理器之间进行通信。如在Linux系统中常见的那样，在AR9331的串行端口上给控制台以访问系统，这意味着您可以在程序中访问Linux提供的程序和工具。
	* TWI: 2 (SDA) and 3 (SCL). 支持用Wire库文件进行TWI通讯。
	* External Interrupts: 3 (interrupt 0), 2 (interrupt 1), 0 (interrupt 2), 1 (interrupt 3) and 7 (interrupt 4). 这些引脚可以配置在低电平值触发，上升沿或下降沿触发，或值的变化的时候触发。有关详细信息，请参阅attachInterrupt（）函数。不建议使用引脚0和1作为中断，因为它们也是用于与Linux处理器通信的硬件串行端口。引脚7连接到AR9331处理器，将来可能被用作握手信号。如果打算将其用作中断，小心可能会有冲突。
	* PWM: 3, 5, 6, 9, 10, 11, 和 13. 用analogWrite（）函数提供8位PWM输出。
	* SPI: ICSP header. 这些引脚支持使用SPI库的SPI通信。请注意，SPI引脚没有连接到任何数字I / O引脚，因为它们位于Uno上，它们仅在ICSP连接器上可用。这意味着如果您有使用SPI的shield，但没有6针ICSP连接器连接到Seeeduino Cloud的6引脚ICSP接头，则shield将不起作用。SPI引脚也连接到AR9331 gpio引脚，它已经在SPI接口的软件中实现。这意味着ATMega32u4和AR9331也可以使用SPI协议进行通信。
	* Analog Inputs: Seeeduino Cloud有12个模拟输入，标记为A0至A11，所有这些都可以用作数字I / O。引脚A0-A5出现在与Uno相同的位置; 输入A6-A11分别位于数字I / O引脚4,6,8,9,10和12上。每个模拟输入提供10位分辨率（即1024个不同的值）。默认情况下，模拟输入从0到5伏，尽管可以使用AREF引脚和analogReference（）功能来更改其范围的上限。
	* AREF. 模拟输入的参考电压。与analogReference()一起使用.

## 入门指导

Seeeduino Cloud 有2个处理器。 其中一个是类似Leonardo的ATmega32U4. 另外一个是Atheros 9331, 运行Linux和OpenWRT wireless stack, 使板可以连接到WiFi和以太网。 使用 [Yun Bridge Library](https://www.arduino.cc/en/Reference/YunBridgeLibrary), 可以通过Arduino在Linux系统上调用程序或自定义脚本来连接各种互联网服务。

**ATmega32U4 程序**

ATmega32U4使用[Arduino软件（IDE）](https://www.arduino.cc/en/Main/Software?setlang=en)编程，如果您尚未安装，请点击[此处](https://www.arduino.cc/en/Guide/HomePage)进行安装说明。

**安装驱动程序**

首先，你需要：

* **获取Micro-USB电缆**
    * 您首先需要Micro-USB电缆; Android手机的数据线也可以。如果找不到，可以在[这里](http://www.seeedstudio.com/depot/Micro-USB-Cable-48cm-p-1475.html?cPath=98_100)买一个。

!!!Warning
    小心连接 micro USB 接口, 否则可能会使插座脱落。

* **连接硬件**
    * 将USB连接到计算机或外部电源给Seeeduino Cloud供电。使用USB电缆将Arduino板连接到电脑。绿色电源LED（标有PWR）应该点亮。

**For Windows**

Windows版本的Arduino Software（IDE）已经包含驱动程序。安装它时，让操作系统自动安装它们。连接您的Seeeduino Yun的时候，驱动程序将自动安装。

**For MAC**

第一次将Seeeduino Cloud插入Mac，“Keyboard Setup Assistant”将会跳出。没有任何配置与Seeeduino Yun相关; 您可以通过单击窗口左上方的红色按钮来关闭此对话框。

**For Linux**

无需为Ubuntu 10.0.4及更高版本安装驱动程序，但请确保端口5353未被防火墙阻止。

**开始你的第一个程序**

打开 LED blink 程序: File > Examples >01.Basics > Blink.

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/UNO_Load_Blink.jpg)

**选择你的board type and port**

你需要通过 Tools > Board menu 来选择相应的 Arduino or Genuino board.

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/YUN_SelBoard.jpg)

通过 Tools -> Serial Port 菜单来选择端口. 类似 COM3 或者更高(COM1 和 COM2 通常作为硬件串口预留). 要了解具体哪个端口，您可以断开电路板并重新打开; 消失的就是Arduino或Genuino. 重新连接电路板并选择该串行端口。当您的电路板在WiFi上正确配置时，您将在“端口”列表中找到它，如屏幕截图所示。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/YUN_SelPort.jpg)

**上传程序**

现在，只需点击IDE中的“Upload”按钮即可。等待几秒钟 - 您应该看到板上的RX和TX LED闪烁。如果上传成功，则会在状态栏中显示“Done uploading”消息。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/UNO_Upload.png)

上传完成后的几秒钟，您应该看到电路板上的LED（D13）开始闪烁（绿色）。如果是，恭喜！你已经得到了Arduino的运行。如果您有问题，请参阅故障排除建议。

**在ATHEROS AR9331上编程**

**网络配置**

Seeeduino Cloud具有WiFi接口和LAN端口。他们都有IP地址，可以用于互联网连接和设备管理。

**1. Wi-Fi AP Mode**

当您第一次打开Seeeduino Cloud时，将会显示Wi-Fi连接中显示的不安全WiFi网络SeeeduinoCloud-AXXXX。您可以将计算机连接到此网络，如下所示。您的计算机将获得此网络的IP地址 **192.168.240.xxx**。Seeeduino Cloud的默认IP地址为 **192.168.240.1**。

**2. Wi-Fi STA Mode**

连接SeeeduinoCloud-AXXXX后，在浏览器搜索框中输入172.31.255.254或192.168.240.1，您将使用Web UI连接到Seeeduino Cloud。默认密码为“seeeduino”，然后单击LOG IN。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/seeeduino_cloud_login.png)

点击 "SYSTEM", 选择您的Wi-Fi网络，输入密码，然后点击 "CONFIGURE & RESTART".

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/seeeduino_cloud_sta.png)

**3. Onboard Ethernet**

当您使用以太网电缆将Seeeduino Cloud连接到有线网络时，将尝试通过DHCP自动连接。该板将显示在网络列表上，就像通过WiFi一样。

**Terminal**

您可以通过SSH访问Seeeduino Cloud的终端，以编程或配置ATHEROS AR9331。

* 下载 SSH client 例如 [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
* 使用Seeeduino Cloud的IP地址并运行SSH client。

```
username: root
password: seeeduino
```

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/seeeduino_cloud_terminal.png)


**Yun Bridge Library**

The Bridge Library 简化了Arduino Board和Dragino HE之间的通讯。 来自AVR的Bridge commands由HE上的Python来解析.

他的作用如下：

* 在Arduino要求的时候在GNU / Linux端执行程序
* 提供共享存储空间，用于共享数据，如Arduino和Internet之间的传感器读数;
* 接收来自Internet的命令，并将其直接传递到Arduino。

[Arduino Official Website](https://www.arduino.cc/en/Reference/YunBridgeLibrary)有详细的解释和很多例子来展示如何使用Bridge. 以下是使用Bridge Library的一些示例.

**Example 1: Say hello to Linux**

This example is a hello test between the Arduino and Seeeduino Cloud. The example can be found on the Arduino IDE--> File --> Examples --> Bridge --> ConsoleRead. A tutorial of this example can be found [here](https://www.arduino.cc/en/Tutorial/ConsoleRead). You can see the code below with some additional details to understand it with the Seeeduino Cloud:
这个例子是Arduino和Seeeduino Cloud之间的一个hello测试。该示例可以在Arduino IDE-> File - > Examples - > Bridge - > ConsoleRead中找到。这个例子的教程可以在[这里](https://www.arduino.cc/en/Tutorial/ConsoleRead)找到。您可以在下面的代码中查看一些其他详细信息:

```
#include <Console.h>

String name;

void setup() {
    // Initialize Console and wait for port to open:
    Bridge.begin();
    Console.begin();

    // Wait for Console port to connect
    while (!Console);

    Console.println("Hi, what's your name?");
}

void loop() {
    if (Console.available() > 0) {
        char c = Console.read(); // read the next char received
        // look for the newline character, this is the last character in the string
        if (c == '\n') {
            //print text with the name received
            Console.print("Hi ");
            Console.print(name);
            Console.println("! Nice to meet you!");
            Console.println();
            // Ask again for name and clear the old name
            Console.println("Hi, what's your name?");
            name = "";  // clear the name string
        }
        else {       // if the buffer is empty Cosole.read() returns -1
            name += c; // append the read char from Console to the name string
        }
    }
}

```

**Example 2: Upload data to IoT Server**

此示例显示如何将数据记录到公共IoT服务器“Xively”。示例是从Arduino IDE-> File - > Examples - > Bridge - > XivelyClient. 这个例子的教程可以在[这里](https://www.arduino.cc/en/Tutorial/YunXivelyClient)这里参考。上传程序之前，请确保：

* Seeeduino Cloud 接入互联网。
* 根据教程输入您的FEED ID和API KEY。注意，FEED ID应在双引号“”内。

```
/*
  Xively sensor client with Strings

 This sketch connects an analog sensor to Xively,
 using an Arduino Yún.

 created 15 March 2010
 updated 27 May 2013
 by Tom Igoe

 http://arduino.cc/en/Tutorial/YunXivelyClient

 */
#include <Process.h>
#include "passwords.h"      // contains my passwords, see below

/*
  NOTE: passwords.h is not included with this repo because it contains my passwords.
 You need to create it for your own version of this application.  To do so, make
 a new tab in Arduino, call it passwords.h, and include the following variables and constants:

 #define APIKEY        "foo"                  // replace your pachube api key here
 #define FEEDID        0000                   // replace your feed ID
 #define USERAGENT     "my-project"           // user agent is the project name
 */

// set up net client info:
const unsigned long postingInterval = 60000;  //delay between updates to xively.com
unsigned long lastRequest = 0;      // when you last made a request
String dataString = "";

void setup() {
    // start serial port:
    Bridge.begin();
    Serial.begin(9600);

    while (!Serial);   // wait for Network Serial to open
    Serial.println("Xively client");

    // Do a first update immediately
    updateData();
    sendData();
    lastRequest = millis();
}

void loop() {
    // get a timestamp so you can calculate reading and sending intervals:
    long now = millis();

    // if the sending interval has passed since your
    // last connection, then connect again and send data:
    if (now - lastRequest >= postingInterval) {
        updateData();
        sendData();
        lastRequest = now;
    }
}

void updateData() {
    // convert the readings to a String to send it:
    dataString = "Temperature,";
    dataString += random(10) + 20;
    // add pressure:
    dataString += "\nPressure,";
    dataString += random(5) + 100;
}

// this method makes a HTTP connection to the server:
void sendData() {
    // form the string for the API header parameter:
    String apiString = "X-ApiKey: ";
    apiString += APIKEY;

    // form the string for the URL parameter:
    String url = "https://api.xively.com/v2/feeds/";
    url += FEEDID;
    url += ".csv";

    // Send the HTTP PUT request

    // Is better to declare the Process here, so when the
    // sendData function finishes the resources are immediately
    // released. Declaring it global works too, BTW.
    Process xively;
    Serial.print("\n\nSending data... ");
    xively.begin("curl");
    xively.addParameter("-k");
    xively.addParameter("--request");
    xively.addParameter("PUT");
    xively.addParameter("--data");
    xively.addParameter(dataString);
    xively.addParameter("--header");
    xively.addParameter(apiString);
    xively.addParameter(url);
    xively.run();
    Serial.println("done!");

    // If there's incoming data from the net connection,
    // send it out the Serial:
    while (xively.available() > 0) {
        char c = xively.read();
        Serial.write(c);
    }
}

```

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/500px-SeeeduinoCloud_Sketch_xively.png)


**Example 3: Log Data to USB flash**

This example shows how to log data to a USB flash. The sketch used in this example is same as [here](http://wiki.dragino.com/index.php?title=Arduino_Yun_examples#Log_sensor_data_to_USB_flash). And the source code can be found there.
The Seeeduino Cloud will auto mount the USB flash to directory /mnt/sda1. And the sketch will append the sensor data to the file /mnt/sda1/data/datalog.csv. So make sure there is such a file in the USB flash before running the sketch.

此示例显示如何将数据记录到USB闪存。本示例中使用的程序与[此处](http://wiki.dragino.com/index.php?title=Arduino_Yun_examples#Log_sensor_data_to_USB_flash)相同。并且可以在那里找到源代码。Seeeduino Cloud将自动将USB闪存映射到目录/ mnt /sda1。而程序会将传感器数据附加到文件/mnt/sda1/data/datalog.csv。因此，在运行程序之前，请确保在USB闪存中有这样的文件。

```
#include <FileIO.h>     //FileIO class allow user to operate Linux file system
#include <Console.h>    //Console class provide the interactive between IDE and Yun Shield
void setup() {
    // Initialize the Console
    Bridge.begin();
    Console.begin();
    FileSystem.begin();
    while(!Console);   // wait for Serial port to connect.
    Console.println("Filesystem datalogger\n");
}
void loop () {
    // make a string that start with a timestamp for assembling the data to log:
    String dataString;
    dataString += getTimeStamp();
    dataString += " , ";
    // read three sensors and append to the string:
    for (int analogPin = 0; analogPin < 3; analogPin++) {
        int sensor = analogRead(analogPin);
        dataString += String(sensor);
        if (analogPin < 2) {
            dataString += ",";    // separate the values with a comma
        }
    }
    // open the file. note that only one file can be open at a time,
    // so you have to close this one before opening another.
    // The USB flash card is mounted at "/mnt/sda1" by default
    File dataFile = FileSystem.open("/mnt/sda1/data/datalog.csv", FILE_APPEND);
    // if the file is available, write to it:
    if (dataFile) {
        dataFile.println(dataString);
        dataFile.close();
        // print to the serial port too:
        Console.println(dataString);
    }
    // if the file isn't open, pop up an error:
    else {
        Console.println("error opening datalog.csv");
    }
    delay(15000);  //Write every 15 seconds
}
// getTimeStamp function return a string with the time stamp
// Yun Shield will call the Linux "date" command and get the time stamp
String getTimeStamp() {
    String result;
    Process time;
    // date is a command line utility to get the date and the time
    // in different formats depending on the additional parameter
    time.begin("date");
    time.addParameter("+%D-%T");   // parameters: D for the complete date mm/dd/yy
    //              T for the time hh:mm:ss
    time.run();   // run the command
    // read the output of the command
    while(time.available()>0) {
        char c = time.read();
        if(c != '\n')
        result += c;
    }
    return result;
}

```

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/500px-SeeeduinoCloud_Sketch_USB.png)


**IoT Server Configuration**

IoT Server页面允许您将数据上传到诸如Xively之类的IoT网站，而您只需要将传感器数据写入串口。

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Cloud/master/img/500px-SeeeduinoCloud_IoTServer.png)

程序如下：

```
/*
  Simulate UART TX Data

 This sketch simulate Temperature and Humidity data to UART.

 To test the pass through feature for different IoT service

 created 25 Apr 2014
 by Dragino Technology Co., Limited

 Reference:
 http://wiki.dragino.com/index.php?title=Xively#Upload_data_to_Xively_use_Pass_Through_Mode

 */
String dataString = "";

void setup() {
    Serial1.begin(115200);
}

void loop() {
    dataString = "temp:";
    dataString += random(10) + 20;
    Serial1.println(dataString);  // upload Temperature data
    delay(20000);
    dataString = "humidity:";
    dataString += random(5) + 70;  // upload humidity data
    Serial1.println(dataString);
    delay(20000);
}
```

## 资源下载

* **Schematic**
    * [Seeeduino Cloud Eagle file](https://github.com/SeeedDocument/Seeeduino_Cloud/raw/master/res/Seeeduino_Cloud_v1.0.zip)
    * [Seeeduino Cloud PDF file](https://github.com/SeeedDocument/Seeeduino_Cloud/raw/master/res/Seeeduino_Cloud_PDF.pdf)

* **Firmware**
    * [Seeeduino Cloud Firmware](https://github.com/SeeedDocument/Seeeduino_Cloud/raw/master/res/Seeeduino_Cloud_Firmware--v1.3.4--20140815-1100.zip)

* **References**
    * [Getting Started with Arduino](https://www.arduino.cc/en/Guide/HomePage)
    * [Arduino Language Reference](https://www.arduino.cc/en/Reference/HomePage)
    * [Download the Arduino Software(IDE)](https://www.arduino.cc/en/Main/Software)
    * [Arduino FAQ](https://www.arduino.cc/en/Main/FAQ)
    * [Arduino Introduction](https://www.arduino.cc/en/guide/introduction)
    * [Wikipedia page for Arduino](https://en.wikipedia.org/wiki/Arduino)
    * [Arduino Yun Wiki](https://www.arduino.cc/en/Main/ArduinoBoardYun)
    * [Getting started with Arduino Yun](https://www.arduino.cc/en/Guide/ArduinoYun#toc2)
    * [Yun Bridge Library](https://www.arduino.cc/en/Reference/YunBridgeLibrary)


## FAQ

* 什么是 Yun Bridge Library?

Yun Bridge Library 用于MPU和MCU之间通信的机制。 Seeeduino Cloud 使用 Yun Bridge Library， 让Arduino用户轻松构建其物联网项目。
