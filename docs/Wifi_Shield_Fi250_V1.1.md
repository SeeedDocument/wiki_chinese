---
title: Wifi Shield (Fi250) V1.1
category: Shield
bzurl: https://www.seeedstudio.com/Wifi-Shield-(Fi250)-V1.1-p-2449.html
oldwikiname:  Wifi Shield (Fi250) V1.1
prodimagename:  Fi250_board1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Wifi_Shield_Fi250_V1.1
sku:    103030027
---

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/Fi250_board1.jpg)

Wifi Shield（Fi250）V1.1 是 Arduino 连接互联网的廉价解决方案。 Wi-Fi 模块支持 IEEE 802.11b / g / n 模式，最高速度可达 65Mbit / s。 Wifi Shield（Fi250）V1.1 集成了板载天线。该模块预留一个 UFL 连接器，您可以使用额外的天线来改善信号范围。主板上有一个按键，只要按一下就可以改变 WiFi Shield 为 AP 模式。该模块可以和计算机通讯软件通讯，您可以通过 USB-UART 转换器来控制模块。WiFi Shield 包含一个 Micro SD 卡插槽，当 WiFi Shield 作为 TCP，UDP 服务器工作时 SD 卡负责记录数据。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.90b3702jPsaQN&id=45586820224)


##   规格参数
---
<table  cellpadding="1" cellspacing="1" width="555">
<tr>
<td> 型号
</td>
<td>WIZnet FI250
</td></tr>
<tr>
<td> 工作电压
</td>
<td> 5V or 3.3V (自动选择)
</td></tr>
<tr>
<td> 电流
</td>
<td> 300mA (最大)
</td></tr>
<tr>
<td>频段
</td>
<td>2.4GHz IEEE 802.11b/g/n
</td></tr>
<tr>
<td>天线
</td>
<td>板载 PCB 天线 (预留 UFL 接口)
</td></tr>
<tr>
<td>存储
</td>
<td>1MB Flash Memory, 128KB SRAM, 1MB Serial Flash
</td></tr>
<tr>
<td>通信接口
</td>
<td>UART(默认)/SPI(固件升级)
</td></tr>
<tr>
<td>尺寸
</td>
<td>69.0x53.5x23.5 mm
</td></tr>
<tr>
</td></tr></table>

## 兼容性

我们有许多扩展板，可以使你的开发板更加强大，但是并不是所有的扩展板都兼容所有的开发板，这里我们用一张表来说明这些扩展板和开发板的兼容性。

!!!note
    请注意，"Not recommended"表示扩展板可能能与开发板搭配使用，但需要额外的工作，如跳线或重写代码。如果您有兴趣挖掘更多，欢迎联系 techsupport@seeed.cc。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)

##   使用方法
---
我们使用一个 Arduino Leonardo 演示。我们建议您使用硬件串口，软件串口速度不够快，无法与 Wifi 模块通信。

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/Fi250_board.jpg)

###  TCP 从机模式

点击 [这里](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wizfi250.zip) 下载 Wifi Shield (Fi250) 的库函数，然后将库函数添加进 Arduino IDE 库。复制下面的代码并粘贴到新的 Arduino IDE 窗口中，上传代码。

```c++
/*
//This demo use Arduino Leonardo or Seeeduino Lite. The jumper connect D0-WIFI_TX, D1_WIFI_RX; Let the boot pin not connect
*/
#include <Arduino.h>
#include "WizFi250.h"

#define SSID      "STEST" //Set your SSID
#define KEY       "87654321" //Set your phrase
#define AUTH       "WPA2" // Set the encrypt type


#define  HOST_IP       "192.168.168.185" //Set the TCP Server IP
#define  REMOTE_PORT    9090 //Set the port
#define LOCAL_PORT      1234  //Set the port

#define spi_CS  8

WizFi250 wizfi250(&Serial1);
boolean returnValue=false;
void setup() {

    Serial.begin(115200);
    Serial1.begin(115200);
    while (!Serial);
    pinMode(spi_CS,OUTPUT);
    Serial.println("--------- WIZFI250 TEST --------");
    // wait for initilization of Wizfi250
    delay(1000);
    Serial.println("Join " SSID );
    wizfi250.reset();
    delay(1000);
    wizfi250.sendCommand("AT+WLEAVE\r");
    delay(1000);
    if (!wizfi250.join(SSID, KEY, AUTH)) {
        Serial.println("Failed join " SSID);
        Serial.println("Please Restart");
    } else {

        Serial.println("Successfully join " SSID);
        wizfi250.sendCommand("AT+WSTAT\r");
        delay(5);
        char c;
        while(wizfi250.receive((uint8_t *)&c, 1, 100) > 0) {
            Serial.print((char)c);
        }
        delay(2000);
        returnValue=wizfi250.connect(HOST_IP,REMOTE_PORT,LOCAL_PORT);
        if(returnValue)
        Serial.println("Now you can send data to Server or receive data from Server!");
    }
}
void loop() {
    if(wizfi250.available()) {
        Serial.print((char)wizfi250.read());
    }
    if(Serial.available()) {
        wizfi250.print((char)Serial.read());
    }
}
```

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/FI_250_client.bmp)

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/FI_250_client_arduino.png)

###  Http 连接

下载并安装好库文件后，打开示例中的 **Wizfi250_http** 例程。

```c++
/*
//This demo use Arduino Leonardo or Seeeduino Lite. The jumper connect D0-WIFI_TX, D1_WIFI_RX; Let the boot pin not connect
*/
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "WizFi250.h"

#define SSID      "STEST"   //Set your SSID
#define KEY       "87654321" //Set your phrase
#define AUTH       "WPA2" //Set the encrypt type

#define TSN_HOST_IP        "74.125.128.103" //google.com server
//#define TSN_HOST_IP        "115.239.210.26" //baidu.com server
//#define TSN_HOST_IP      "192.168.1.254"      // broadcast
#define TSN_REMOTE_PORT    80
#define LOCAL_PORT     9000

#define spi_CS  8

//SoftwareSerial sprintSerial(4,5);   // The software serial port is not stable.
WizFi250 wizfi250(&Serial1);
void setup() {

    Serial.begin(115200);
    Serial1.begin(115200);
    while (!Serial);
    pinMode(spi_CS,OUTPUT);
    digitalWrite(spi_CS,HIGH);
    Serial.println("--------- WIZFI250 TEST --------");
    // wait for initilization of Wizfi250
    delay(1000);
    Serial.println("Join " SSID );
    delay(10);
    if (!wizfi250.join(SSID, KEY, AUTH)) {
        Serial.println("Failed join " SSID);
    } else {
        Serial.println("Successfully join  "  SSID);

        wizfi250.clear();

        wizfi250.connect(TSN_HOST_IP,TSN_REMOTE_PORT,LOCAL_PORT);
        delay(10);
        wizfi250.send("GET / HTTP/1.1\r\n\r\n");
    }
    char c;
    for(int i=0;i<320;i++){
        if (wizfi250.receive((uint8_t *)&c, 1, 100) > 0) {
            Serial.print((char)c);
        }
    }
}
void loop() {
    while (wizfi250.available()) {
        Serial.write(wizfi250.read());
    }
    while (Serial.available()) {
        wizfi250.write(Serial.read());
    }
}
```

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/FI_250_HTTP.jpg)

###  重置模块

*   如果需要将模块重置为出厂默认设置，请快速按下 **Function** 键三次。然后 MODE 和 WIF LED 将闪烁，直到模块复位。

*   模块恢复出厂设置后，波特率恢复为 115200。

**<span style="color:#ff0000">下图文字错误，是按 3 次。</span>**

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/Fi250_reset.png)

###  一键设置为 AP 模式。

*   设置为 AP 模式很容易，按一次 **Function** 按键，等到 WIFI LED 变为红色，您就可以找到 Wifi 信号了。名字为 **WizFi250_AP_******。

*   按下 Wifi Shield Fi250 的 **reset** 按钮退出 AP 模式。

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/FI2350_AP.png)

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/FI250APshow.png)

###   更新固件

The step for upgrade F/W show as below: <big>Connect your wifi shield(Fi250) via UART directly,you can use a UartSBee or other UART tools</big>
升级 F/W 的步骤如下：通过 UART 连接 Wifi Shield(Fi250) ，可以使用 UartSBee 或其他 UART 工具。在升级 F/W 之前，您可以将模块设置为编程模式（短接 BOOT 跳线引脚）。[点击这里下载固件](http://wizwiki.net/wiki/doku.php?id=products:wizfi250:wizfi250firmware:start)。

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/Fi250_update_firmware副本.png)

第一步：

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/WizFi250_firmware1.png)

第二步：

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/WizFi250_firmware2.png)

第三步：

![](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/img/WizFi250_firmware3.png)

*   下载成功后，拔掉跳线帽并重启模块。

##   资源下载
---
*   **[Eagle 文件]**[Wifi_Shield_(Fi250)_V1.1_sch_pcb.zip ](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Eagle_File_Wifi_Shield-Fi250-V1.1_sch_pcb.zip)
*   **[编程指南]**[Wizfi250_programmer_s_guide.pdf](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wizfi250_programmer_s_guide.pdf)
*   **[快速上手指南]**[Wizfi250_quick_start_guide.pdf](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wizfi250_quick_start_guide.pdf)
*   **[数据手册]**[Wizfi250_datasheet.pdf](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wizfi250_datasheet.pdf)
*   **[库函数]**[Wizfi250 library](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wizfi250.zip)
*   **[PDF 原理图]**[PDF_Wifi_Shield_(Fi250)_V1.1](https://github.com/SeeedDocument/Wifi_Shield_Fi250_V1.1/raw/master/res/Wifi_Shield-Fi250-V1.1.pdf)
