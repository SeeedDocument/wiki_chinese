---
name: W5500 Ethernet Shield v1.0
category: Shield
bzurl: https://www.seeedstudio.com/W5500-Ethernet-Shield-p-2433.html
oldwikiname: W5500_Ethernet_Shield_v1.0
prodimagename: W5500.jpg
wikiurl: http://wiki.seeedstudio.com/cn/W5500_Ethernet_Shield_v1_0
sku: 103030021
---

![](https://raw.githubusercontent.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/master/img/W5500.jpg)

The W5500 Ethernet Shield v1.0 可以为您的项目提供互联网连接。W5500 使用户能够通过使用单芯片(其中有 TCP/IP stack, 10 / 100 Ethernet MAC 和 PHY embedded)来实现应用中的互联网连接。The W5500 Ethernet Shield v1.0 还具有两个 Grove 连接器和一个 microSD 卡插槽，用于支持需求在 Grove 传感器中存储大量数据的项目。 RJ45 端口（以太网线缆连接到的位置）足够低使得您可以使用更多的 shield。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=534263404757&qq-pf-to=pcqq.c2c)

## 产品特性
--------

-   支持固线式 TCP/IP 协议 : TCP, UDP, ICMP, IPv4, ARP, IGMP, PPPoE
-   同时支持 8 个独立插座
-   支持掉电模式
-   支持通过 UDP 唤醒 LAN
-   支持高速串行外设接口 (SPI 模式 0, 3)
-   用于 TX/RX 缓冲器内部 32K 的字节内存
-   10BaseT/100BaseTX 以太网 PHY 嵌入式
-   支持自协商(全双工和半双工，10 和 100\* based)
-   不支持 IP 分段
-   3.3V 操作，具有 5V I/O 信号容差
-   LED 输出 (全/半双工,Link,速度,有效)
-   Micro-SD 卡插槽
-   用于 I2C 和 UART 的 Grove 连接器

## 兼容性

我们已经生产了大量扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里使用表格来说明扩展板和平台板之间的兼容性。

!!!note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。 如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc. 联系。

**点击查看全图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)

## 硬件概述
-----------------
![](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/img/W5500_Interface.jpg)


**硬件配置**

1. RJ45: 以太网端口;
2. IC W5500: 固线 TCP/IP 以太网控制器;
3. Reset Button: 重置 Ethernet shield ;
4. SD Card Socket: 支持 FAT16 或 FAT32 中的 Micro SD卡; 最大存储空间为 2GB。
5. I2C 接口
6. UART 接口

**Arduino上的引脚用途**

1. D4：  SD card 芯片选择
2. D10： W5200 芯片选择
3. D11： SPI MOSI
4. D12： SPI MISO
5. D13： SPI SCK

<div class="admonition note">
<p class="admonition-title">Note</p>
W5500 和 SD 卡都通过 SPI 总线与 Arduino 进行通信。 引脚 **10** 和引脚 **4** 是用于 W5500 和 SD 插槽的芯片选择引脚。它们不能用作通用 I/O 口。
</div>

## 使用方法
-----

我们将向您展示一个例子。该示例可以将数据上传到网页，并将传感器数据存储到 SD 卡。

### 软件部分

**零件表 :**

|名称|功能|数量|
|----|--------|---|
|[W5500 Ethernet Shield](https://www.seeedstudio.com/W5500-Ethernet-Shield-p-2433.html) |提供以太网连接| 1 |
|[Seeeduino V4.2](http://www.seeedstudio.com/item_detail.html?p_id=2517)|控制器|1|
|[Grove-Temp&Humi Sensor](https://www.seeedstudio.com/Grove-Temp%26Humi-Sensor-p-745.html)|传感器|1|
|[Base Shield V2](https://www.seeedstudio.com/Base-Shield-V2-p-1378.html)|Base Shield|1|
|Micro SD Card |存储数据|1|

**步骤 :**

1. 在Arduino上安装 W5500 Ethernet Shield v1.0，在 Ethernet Shield 上安装 Base Shield V2，并将 Grove-Temp&Humi 传感器连接到 Base Shield **D5** Grove 端口，并附上SD卡。
2. 使用标准以太网线缆 Ethernet shield 连接到网络;
3. 通过 USB 线缆将 Arduino 连接到 PC;
![](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/img/temp%26humi%20hardware.jpg)


### 软件部分

- 请按 [怎样安装Arduino库](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/) 中的步骤来安装库文件。
- 点击下面的按钮以下载 SD 和 W5500 Ethernet Shield 库。
[![](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/img/download%20SD%20library.png)](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/res/SdFat-master.zip)
[![](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/img/download%20W5500%20library.png)](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/res/WIZ_Ethernet_Library-IDE1.6.x-master.zip)

- 下载完成后将库安装到 Arduino IDE 中。
- 将以下代码复制到 Arduino IDE 中，然后上传 :

```
//This sketch uses W5500 Ethernet Shield,Seeeduino V4.2,Grove-Temp&Humi,
//Base Shield V2 Sensor and Micro SD Card to design a temperature and humidity collection station.
//attach the temperature and humidity sensor to base shield D5 grove port.
//It publishes the temperature and humidity data to webpage
//and refresh every 5 seconds, store the data into SD card datalog.txt file.

#include <SD.h>
#include <SPI.h>
#include <Ethernet.h>
#include <dht11.h>
dht11 DHT;
#define DHT11_PIN 5
const int chipSelect = 4;

// Please update IP address according to your local network
#if defined(WIZ550io_WITH_MACADDRESS) // Use assigned MAC address of WIZ550io
;
#else
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
#endif  
IPAddress ip(192,168,0,177);

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(80);

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // start the Ethernet connection and the server:
#if defined(WIZ550io_WITH_MACADDRESS)
  Ethernet.begin(ip);
#else
  Ethernet.begin(mac, ip);
#endif  
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());

  //initializing the SD card
  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  Serial.println("card initialized.");
}


void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
	  client.println("Refresh: 5");  // refresh the page automatically every 5 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");

          // output the value of input pin on web
          int chk;
          chk = DHT.read(DHT11_PIN);    // READ DATA
          client.print("Humidity: ");
          client.print(DHT.humidity);
          client.println("<br />");
          client.print("Temperature: ");
          client.print(DHT.temperature);   

          //write value of input pin into SD card
          // make a string for assembling the data to log:
          String dataString = "";
          // read the humidity and temperature and append to the string:
          dataString = String(DHT.humidity) + String(DHT.temperature);
          // open the file. note that only one file can be open at a time,
          // so you have to close this one before opening another.
          File dataFile = SD.open("datalog.txt", FILE_WRITE);
          // if the file is available, write to it:
          if (dataFile) {
          dataFile.println(dataString);
          dataFile.close();
          // print to the serial port too:
          Serial.println(dataString);
          }
          // if the file isn't open, pop up an error:
          else {
          Serial.println("error opening datalog.txt");
          }
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        }
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}

```

### 结果展示

现在我们来看看结果。

1. 把您的 SD 卡放入电脑，您会看到一些温、湿度的信息。
2. 此外，我们可以从网络上查看信息。

![](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/img/temp%26humi%20on%20web.png)

可见使用是很容易的，您也试试吧。

## 资源下载
- **[Eagle文件]**[W5500 Ethernet Shield in Eagle format](https://raw.githubusercontent.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/master/res/W5500_Ethernet_Shield_v1.0.zip)
- **[原理图PDF]**[W5500 Ethernet Shield Schematic in PDF format](https://raw.githubusercontent.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/master/res/W5500_Ethernet_Shield_v1.0.pdf)
- **[PCB图PDF]**[W5500 Ethernet Shield PCB in PDF format](https://github.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/raw/master/res/W5500%20Ethernet%20Shield%20v1.0%20PCB.pdf)
- **[库文件]**[W5500 Ethernet Shield Library](https://github.com/embeddist/WIZ_Ethernet_Library-IDE1.6.x)
- **[芯片数据手册]**[W5500 Ethernet Shield Datasheet.pdf](https://raw.githubusercontent.com/SeeedDocument/W5500_Ethernet_Shield_v1.0/master/res/W5500_datasheet_v1.0.2.pdf)
<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/W5500_Ethernet_Shield_v1.0 -->
