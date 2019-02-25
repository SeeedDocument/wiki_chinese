---
name: Wifi Shield V2.0
category: Shield
bzurl: https://seeedstudio.com/Wifi-Shield-V2.0-p-2505.html
oldwikiname: Wifi_Shield_V2.0
prodimagename: Wifi_Shield_v2.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Wifi_Shield_V2_0
sku: 113030008
---

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi_Shield_v2.jpg)

这个 WiFi shield 以 RN171 TCP/IP 模块为特色，能够使您的 Arduino/Seeeduino 连接到 802.11b/g 高速无线网络。

这个扩展板与 Arduino 的默认通信协议是 UART/Serial，您可以选择使用哪个数字引脚 (**D0** to **D7**) 用于 **RX** 和 **TX**，需要的两跳线排已包含在内。扩展板还具有两个用于 I2C 和 Serial 的板载 Grove 连接器，使得扩展板可以与任何我们的 Grove 设备一起使用。

板载天线可以使扩展板覆盖范围更广并传输信号的强度增加。RN171 模块支持 TCP，UDP，FTP 和 HTTP 通信协议，以满足大多数无线和物联网 (IoT) 网络项目的需求，例如 : 智能家居网，机器人控制，个人气象站。

后面的例子很好地论述了这个扩展板 : [使用手册](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf).

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.66.526a7c6bPuhwwp&id=45538497026&ns=1&abbucket=1#detail)

## 版本更替
---------------

| 项目          | Wifi Shield V1.0                                                        | Wifi Shield V1.1(v1.2)                                                 | Wifi Shield V2.0                                                                          |
|--------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 电压            | +3.5V~+5V                                                               | +3.5V~+5V                                                              | +3.5V~+5V                                                                                 |
| 校准扩展板    | 是                                                                     | 是                                                                    | 是                                                                                       |
| 通信模式 | Serial port                                                             | Serial port                                                            | Serial port                                                                               |
| 校准扩展板    | 否                                                                      | 是                                                                    | 是                                                                                       |
| 天线类型       | 桅杆式天线                                                            | PCB 板载天线                                                            |  板载天线                                                |
| 库文件       | [Wifi Shield Library V1.0](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WifiShield.zip) | [New Wifi Shield Library](https://github.com/Seeed-Studio/WiFi_Shield) | [New Wifi Shield Library](https://github.com/Seeed-Studio/WiFi_Shield) **和 v1.2 是一样的** |

## 规格参数
--------------

| 项目                        | 值                                                                |
|----------------------------------|----------------------------------------------------------------------|
| 工作电压                | 3.3~5.5 V                                                            |
| 兼容板        | Arduino Uno/Seeeduino                                                |
| 电流                          | 25~400mA                                                             |
| 发射功率                   | 0-10 dBm                                                             |
| 频率                        | 2402~2480 MHz                                                        |
| 通道                          | 0~13                                                                 |
| 网络速率                     | 1-11 Mbps for 802.11b/6-54Mbps for 802.11g                           |
| 尺寸                        | 60X56X19 mm                                                          |
| 净重                       | 24±1 g                                                               |
| WiFi 安全认证       | WEP-128, WPA-PSK (TKIP), WPA2-PSK (AES)                              |
| 内置网络应用 | DHCP client, DNS client, ARP, ICMP ping, FTP, TELNET, HTTP, UDP, TCP |
| 认证                    | RN171: FCC, CE                                                      |

## 兼容性

我们研发了许多扩展板，可以使您的平台板更加强大，但是并不是所有的扩展板都兼容所有的平台板，这里我们用一张表来说明这些板与平台板的兼容性。

!!!note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc.联系。

**点击查看全图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)

## 硬件概述
-----------------

WiFi shield 与任何 Arduino/Seeeduino 开发板兼容，因为它只需要在您选择的板中的 **D0-D7** 之间用于 UART/serial 通信的两个数字引脚。 安装时，只需将扩展板堆叠在 Arduino/Seeeduino 板上即可。


![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi_shield_v2_breakout.png)

1.  **Serial Peripheral Interface (SPI) Connections (MOSI, SCK, MISO):** 这些引脚没有连接到任何 Arduino 的引脚，它们是独立的，它们的逻辑电平输出/输入是 3.3V。它们可以用来通过 SPI 与 Arduino 进行通信，但是需要一个 3.3V 的逻辑转换器。 SPI模式下的数据传输速率可以达到 2Mbps。

    **RES_Wifi:** Wifi shield 有一个用于 RN-171 模块的板载 "Rest Button"，您也可以通过发送复位命令通过软件复位 RN-171。此外，如果您想将此引脚连接到 Arduino 的数字 6 引脚，只需在扩展板上焊上标有 "P5" 的焊盘即可。

2.  **RN171:** 内置 TCP/IP 协议栈的超低功耗无线模块。

3.  **Antenna:** I.PEX 连接器。

4.  **RN171 breakout section:** RN171 模块具有自己的模拟输入和 GPIO 引脚，扩展板可通过此 breakout section 进行访问。 GPIO 引脚 (IO3, IO7, IO8 和 IO9) 的能承受最大电压为 3.3V，模拟输入引脚 (S_0 和 S_1) 可以读取 0-400mV (不超过 1.2V)。 RN171 可以被配置为通过软件使用这些引脚，或者可以连接到其他引脚来使用其他 RN171 功能，例如 adhoc 模式。VCC 的电压取决于 WiFi shield 的电源。

5.  **UART/Serial Select area:** 两个跳线行，让您选择要使用哪个 RX 和 TX 引脚与 Arduino 进行通信。

6.  **Grove connectors:** Analog I2C Grove (如果使用 Arduino UNO 或 Seeeduino) 对应引脚 **A4** 和 **A5** 以及 Digital Serial Grove 对应引脚 **D8** 和 **D9**。VCC 的电压取决于 WiFi shield 的电源。

### 引脚使用 / 扩展板兼容性

WiFi shield 使用 **D0** 和 **D7** 之间的任意两个数字引脚与 RN171 WiFi 模块进行通信，但请记住，Arduino 使用 **D0** 和 **D1** 进行编程和串行通信，WiFi shield 使用这两个引脚可能会导致程序下载时报错。

在本页面的示例代码中，我们使用 **D2** 和 **D3** 作为扩展板的 RX 和 TX。在这种情况下，排线应如下图所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi_shield_v1.1_pinout.png)
**D2 对应 WIFI_TX, D3 对应 WIFI_RX**

### RN171 WiFi Module

RN-171 是一个独立的完整的 TCP/IP 无线网络模块。由于其小巧的外形和极低的功耗，RN-171 非常适合移动无线应用。它搭载了 2.4GHz 无线电，32 位 SPARC 处理器，TCP/IP 协议栈，实时时钟，加密加速器，电源管理和模拟传感器接口。

在最简单的配置中，硬件仅需要连接四个引脚 (PWR, TX, RX 和 GND) 就可以创建无线 WiFi 数据连接。此外，RN171 的模拟传感器输入可用作模拟输入引脚，其额定值为 0-400 mV (不超过 1.2V DC)。

**Power:** RN-171 模块的工作电压一般为 3.3VDC，因此在 WiFi shield 上有一个电压调节器和逻辑电平转换器。扩展板上的 LD1117 调节器将电压转换为 3.3VDC，为 RN171 模块提供电源。但由于电源的自动判断原理，RN-171 可以通过 3V3 引脚和 5V 引脚供电。他们如果在同时供电，电源电压将是5V。如果使用 Arduino/Seeeduino，只需将 WiFi shield 堆叠在板上。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi_shield_v1.1_communicate.png)
**RN171 模块连接到 Arduino 示意图**

**GPIO_6 :** 默认情况下 RN171 WiFi 模块的 **GPIO6** 引脚连接到 WiFi shield 上标记为 **D5** 的 LED。该 LED 用于显示 Access Point (AP) 的连接的状态。但是如果您想将 **GPIO6** 连接到 Arduino 的数字引脚 **5**，只需在 WiFi shield 焊上标有 "P6" 的焊盘即可。

### LED 状态指示灯

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>名称</th>
<th>说明</th>
<th>状态</th>
<th>硬件连接</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D5</td>
<td>Green LED. 网络连接状态</td>
<td><strong>OFF:</strong> 模块未连接到网络<br />
<strong>Solid ON:</strong> 模块已连接到网络</td>
<td>连接到 RN171 模块的 **GPIO6** 引脚</td>
</tr>
<tr class="even">
<td>D1</td>
<td>Red LED. TCP/IP 连接状态</td>
<td><strong>Solid ON:</strong> 通过 TCP 连接<br />

<p><strong>Fast Toggle (2 times/second):</strong> 没有 IP 地址和模块处于命令模式<br />
</p>
<p><strong>Slow Toggle (once/second):</strong> IP 地址正常</p></td>
<td>连接到 RN171 模块的 **GPIO4** 引脚</td>
</tr>
<tr class="odd">
<td>RST</td>
<td>Red LED. WiFi 模块重置状态</td>
<td><strong>Solid ON:</strong> 按下重置按钮 (WIFI_RST)<br />
</td>
<td>连接到 RN171 模块的 **Reset** 引脚</td>
</tr>
<tr class="even">
<td>PWR</td>
<td>Green LED. WiFi 模块启动状态</td>
<td><strong>Solid ON:</strong>模块已启动</td>
<td>连接到 LD1117 电压调节器的 3.3V 输出</td>
</tr>
</tbody>
</table>

WiFi 库
------------

我们创建了一个库来帮助您与扩展板交互，在本节中，我们将向您展示如何设置库并介绍它的一些功能。

### Setup

1.  *从 Wifi Shield github 页面下载 [library code as a zip file](https://github.com/Seeed-Studio/WiFi_Shield)。*
2.  *将下载的文件解压缩到 **…/arduino/libraries/** 文件夹。*
3.  *重命名解压文件夹为 "WifiShield"。*
4.  *打开 Arduino IDE。*

### 函数

这些是库中最重要也最有用的函数，希望您自己查看 .h 文件以查看所有函数。

#### join()

-   **描述:**
    -   使用该函数进入一个 WiFi 热点
-   **语法:**
    -   join(const char *ssid, const char *phrase, int auth)
-   **参数:**
    -   **ssid:** 您想让扩展板接入的 Wifi 热点的名字
    -   **phrase:** 您想让扩展板接入的 Wifi 热点的密码
    -   **auth:** 您希望扩展板连接的Wifi热点的身份验证类型。 可能是以下列表中的某一种:
        -   WIFLY_AUTH_OPEN
        -   WIFLY_AUTH_WEP
        -   WIFLY_AUTH_WPA1
        -   WIFLY_AUTH_WPA1_2
        -   WIFLY_AUTH_WPA2_PSK
        -   WIFLY_AUTH_ADHOC
-   **返回值:**
    -   **boolean:** 如果到接入点的连接成功，则为true，否则为false。
-   **例程:**

```c
#include <SoftwareSerial.h>
#include "WiFly.h"

SoftwareSerial uart(2, 3); // create a serial connection to the WiFi shield TX and RX pins.
WiFly wifly(&uart); // create a WiFly library object using the serial connection to the WiFi shield we created above.

void setup()
{
    uart.begin(9600); // start the serial connection to the shield
    Serial.begin(9600); // start the Arduino serial monitor window connection
    wifly.reset(); // reset the shield
    while(wifly.join("mySSID","mySSIDpassword",WIFLY_AUTH_WPA2_PSK) == false)
    {
        Serial.println("Failed to connect to accesspoint. Will try again.");
    }
    Serial.println("Connected to access point!");
}

void loop()
{

}
```

!!!Tip
    本示例是基于 Arduino UNO 并我们用 **D2/D3** 作为 SoftwareSerial 引脚。如果您使用的是 Arduino Mega，**D2** 是不可用的。更多详情请点击 [Arduino Software Serial](https://www.arduino.cc/en/Tutorial/SoftwareSerialExample)
    这里是一个示例。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/connect_mega.jpg)

代码需要做出以下的修改 :

````c
SoftwareSerial uart(10, 3); // create a serial connection to the WiFi shield TX and RX pins.
````

#### receive()

-   **描述:**
    -   可以用于从扩展板读取数据, Arduino's read() 函数的替代函数。
-   **语法:**
    -   receive(uint8_t *buf, int len, int timeout)
-   **参数:**
    -   **buf:** 存储从扩展板读取的字节的缓冲数组
    -   **len:** 该缓冲数组的长度
    -   **timeout:** 设定超时值用于知道何时应该停止读取
-   **返回值:**
    -   **int:** 返回从扩展板中读到的字节数
-   **例程:**

```c
char c;
while (wifly.receive((uint8_t *)&c, 1, 300) > 0) {
    Serial.print((char)c);
}
```

查看 **File(文件)->Examples(示例)->WiFi_Shield->wifly_test sketch** 以获得完整示例。

#### sendCommand()

-   **描述:**
    -   我们提供的一些函数（例如，join（），reboot（），save（））都是封装好之后罗列在 RN171 模块的用户手册中。sendCommand() 函数允许您封装自己的函数，如果您觉得我们提供的函数不尽人意的话。
-   **语法:**
    -   sendCommand(const char *cmd, const char *ack, int timeout)
-   **参数:**
    -   **cmd:** 任何来自 RN-171's 用户指南的指令均可.
    -   **ack:** 选取的指令对应的返回字符串
    -   **timeout:** 在输出被认定为无效请求或无效响应之前允许的超时值
-   **返回值:**
    -   **boolean:** 如果WiFi Shild 扩展板使用ack字符串响应，则返回true，否则返回false。

-   **例程:**
```c
// our join() function is wrapper for the join command, as seen below.
//The string "Associated" is what the user manual says the RN171 will return on success.
if(sendCommand("join\r", "Associated",DEFAULT_WAIT_RESPONSE_TIME*10))
{
    // joined
}else{
    // not able to join
}
```

查看 **File(文件)->Examples(示例)->WiFi_Shield->wifly_test sketch** 以获得完整示例。

WiFi Shield 示例 / 应用
---------------------------------

### 示例 1: 通过 Arduino 串行监视器窗口发送命令到 WiFi Shield 并接收响应

WiFi Shield 的 RN-171 模块通过发送内建在 [datasheet](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf) 的命令经行配置。

我们创建了一个视频演示完成下面的步骤，如果您想看请点击 [Video - Getting Started With Seeeduino's WiFi Shield.](https://www.youtube.com/watch?v=8dCrAaN16lE) （注意：此视频源来自Youtube,您可能需要自备梯子）

**步骤 1: WiFi Shield 跳线配置**

在 WiFi shield 中配置跳线使 WIFI_TX 对应 **D2**，WIFI_RX 对应 **D3**，如下图所示。这些是我们用来发送和接收来自 RN-171 信息的引脚。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi_shield_v1.1_front.png)

**D2** 对应 **TX**，**D3** 对应 **RX**

**步骤 2: 软件/代码**

在下面的工程中我们创建了一个 UART object，允许我们从 RN-171/WiFi Shield 发送和接收数据。然后，我们将 UART object 与 WiFly 库一起使用来将数据发送到扩展板。Arduino's Serial object 用来打印我们从扩展板接收到的数据，并通过 WiFly/UART object 接收我们想要发送给扩展板的命令。

上传代码到您的 Arduino :

```c
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "WiFly.h"

// set up a new serial port.
SoftwareSerial uart(2, 3); // create a serial connection to the WiFi shield TX and RX pins.
WiFly wifly(&uart); // create a WiFly library object using the serial connection to the WiFi shield we created above.

void setup()
{
    uart.begin(9600); // start the serial connection to the shield
    Serial.begin(9600); // start the Arduino serial monitor window connection
    delay(3000); // wait 3 second to allow the serial/uart object to start
}

void loop()
{
    while (wifly.available())  // if there is data available from the shield
    {
        Serial.write(wifly.read()); // display the data in the Serial monitor window.
    }
    while (Serial.available()) // if we typed a command
    {
        wifly.write(Serial.read()); // send the command to the WiFi shield.
    }
}
```

**步骤 3: 进入 command 模式**

WiFi shield 中的 WiFly RN-171 模块可以以两种模式运行：data 和 command。 在 data 模式下，扩展板可以接收和发起连接。在 command 模式下，我们可以使用 datasheet 中列出的命令来配置模块。

通过以下步骤进入 command 模式 :

1.  打开 Arduino 串口监视器。
2.  在窗口右下角将串口监视器设置为 “No line ending（没有结束符）”，波特率设置为 9600。
3.  在串口监视器输入 "$$$" 并敲击回车键。
4.  模块返回字符 “CMD”，表示它已进入 command 模式。

通过以下步骤来测试一些命令 :

1.  在 Arduino 串口监视器窗口右下角选择 “Carriage return（回车）” 并设置波特率为 9600。
2.  在 Arduino 串口监视器窗口输入下表出的每种命令并敲击回车键。
3.  该模块将为每个命令输出一个响应，如表中所述。

| 命令 | 说明                                                                                                                                                                                                                 |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scan     | 该命令对所有 13 个通道上的接入点执行主动探测扫描。当您使用此命令时，模块会返回它检测到的接入点的 MAC 地址，信号强度，SSID 名称和安全模式。|
| get ip   | 此命令显示 IP 地址和端口号设置|


有关配置命令的完整列表，请参阅 RN-171 的 [Reference Guide](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf) 11 页开头。

### Example 2: 连接到 Access Point / Internet Router

在这个例子中，我们将向您展示在无需输入所需的命令的情况下如何将 WiFi shield 连接到接入点 (您的互联网路由器) :

#### 通过输入命令连接

本节将教您如何使用 RN-171 datasheet 中的命令将 WiFi shield 连接到接入点，通过阅读本节，您将了解使用 WiFi Arduino 库时实际发生了什么。

跟着说明做 :

1.  上传 Example One 中的代码到 Arduino。
2.  **进入 command 模式:**
    1.  将串口监视器设置为 “No line ending” 并把波特率设置为 9600。
    2.  在串口监视器输入 *$$$* 然后敲击回车键。

3.  将串口监视器设置为 “Carriage return”.
4.  **扫描可用的接入点 :**
    1.  输入 *scan*，然后按回车键。Arduino 串口监视器窗口将输出 WiFi shield 找到的每个接入点的 CSV 列表。从左到右，第三个值是安全模式，最后一个值是SSID。此示例显示安全模式为 4，SSID 名称为 MySSID: 01,01,-88,**04**,1104,1c,00,45:56:78:be:93:1f,**MySSID**

5.  从找到的接入点列表中，找到与您的 Internet 路由器相对应的接入点，并记下安全模式和 SSID，因为我们需要这两个值。
6.  **在扩展版中设置安全模式 :**
    1.  输入 *set wlan auth m*，把 *m* 替换成您希望连接到的接入点的安全模式数(本例中应该是4)。
    2.  WiFi shield 支持的安全模式如下图一所示。

7. **设置接入点 Phrase**
    1.  输入 *set wlan phrase myPhrase*，把 *myPhrase* 替换成接入点的安全码。
<div class="admonition note">
<p class="admonition-title">Note</p>
如果您的接入点的安全类型是 WEP，请在上面的命令中使用 *key* 而不是 *phrase* 。
</div>

    2.  接入点(互联网路由器) Phrase 是您用来从 PC 连接到它的密码。在 Windows 中，您可以找到它如下面的动态图所示 :
        ![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/How_to_find_network_security_key_password.gif)
        如何显示网络的安全码

8. **加入连接点**
    1.  现在我们已经设置了接入点的安全类型和 phrase，我们可以连接到它。
    2.  输入 *join MySSID*，把 MySSID 替换成接入点的 broadcast name。
    3.  成功后会在 Arduino 的串口监视器上显示 "Associated!"。

下表中提供了您在上述步骤中输入的命令的说明。更详细的说明可以在 RN171 的用户手册中找到。


| No. | 命令                  | 说明                                                                                                                                                                                                                                                                          |
|--------|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | scan                      | 该命令对所有 13 个通道上的接入点执行主动探测扫描。当您使用此命令时，模块会返回它检测到的接入点的 MAC 地址，信号强度，SSID 名称和安全模式。|
| 2      | set wlan auth 4           | 在接入点上查找与安全协议相对应的值。然后，告诉 WiFly 使用什么安全协议，这里 **图1** 中显示的数字对应于接入点的安全协议。这里我们选择 **4**。|
| 3      | set wlan phrase seeed-mkt | 告诉 WiFi shield 您的密码|
| 4      | join SEEED-MKT            | 告诉 WiFi shield 加入，“SEEED-MKT“ 是我们选择连接的接入点的名称。发送命令后，模块现在执行连接并打印出有关连接的信息。(如果连接失败，请尝试再次发送该命令直到成功)|


| 值 | 安全模式                   |
|-------|---------------------------------------|
| 0     | Open (Default)                        |
| 1     | WEP-128                               |
| 2     | WPA1                                  |
| 3     | Mixed WPA1 and WPA2-PSK               |
| 4     | WPA2-PSK                              |
| 5     | Not used                              |
| 6     | AD hoc mode (join any ad hoc network) |
| 8     | WPE-64                                |

*图一*

#### 使用 WiFi Libraries 连接

您已经知道如何通过输入命令来连接到接入点，现在可以使用我们提供的库和示例了。

要查看连接到接入点所需的代码，请转到 **File(文件) -> Examples(示例) -> Wifi_Shield -> wifi_test**。使用您自己的 SSID (访问点名称)和 KEY (您的访问点的密码)，然后将代码上传到您的 Arduino IDE。

    #define SSID      " SEEED-MKT "
    #define KEY       " seeed-mkt "

随着代码上传到您的 Arduino 板，打开串行监视器窗口。如果扩展板成功加入接入点，将显示 "OK" 消息以及 "get everything" 命令产生的连接信息。如果扩展板无法加入接入点，将显示 "Failed" 消息。

#### 配置扩展板上电连接

通过以下步骤扩展版可以实现上电连接 :

1.  发送 "set wlan ssid mySSID" 命令以用您的SSID 替换 mySSID
2.  发送 "set wlan join 1" 命令
3.  发送 "save" 命令

现在扩展板可以在上电后自动连接到接入点。

每个命令的功能说明可以在 RN-171 datasheet 和下表中找到。


| No. | 命令                   | 说明                                                                           |
|--------|----------------------------|---------------------------------------------------------------------------------------|
| 1      | set wlan ssid <ssid> | "<ssid>" 使您希望自动连接到的接入点名称 |
| 2      | set wlan join 1            | 告诉模块自动连接到储存在内存中的 SSID 接入点  |
| 3      | save                       | 将这些设置保存在 WIFI 的配置文件中                                   |


#### 设置静态 IP 地址

要使扩展板从接入点获得静态 IP 地址，一旦连接到接入点，请发送以下命令 :

| No. | 命令                       | 说明                   |
|--------|--------------------------------|-------------------------------|
| 1      | set ip dhcp 0                  | 关闭 DHCP |
| 2      | set ip address <address> | 设置 IP 地址 |


### Example 3: 您网络通信

这个例子将告诉您，您的设备，比如您的手机或者电脑如何和 WiFi shield 通信。

遵循以下步骤 :

1.  根据 Example 2 的 *Connecting By Typing Commands* 的部分步骤 1-7 配置模块。
2.  通过发送命令 "set ip local 80" 将 listening IP 端口设置为 "80"。
3.  根据 Example 2 的 *Connecting By Typing Commands* 的部分步骤 8 把扩展板连接到接入点。
4.  通过发送 "save" 命令保存这些设置。
5.  用 "get ip" 命令获取您的扩展板的 IP 地址。IP 地址和端口将显示在 "IP=" 的右侧 (e.g. IP=192.168.0.10:80)
6.  打开您的浏览器，在您的浏览器的网址栏中输入您的扩展板的 IP 地址，然后按回车键来访问它。
7.  您的 Arduino 串口监视器窗口将显示类似于下面的 HTTP 响应。这是您的浏览器发送给扩展板以请求数据的信息。

```
*OPEN*GET / HTTP/1.1
Host: 192.168.0.10
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
```

浏览器现在正在等待数据，Wifi 模块可以将传感器值，服务网页或任何其他数据直接发送回浏览器! 在这种情况下，浏览器正在等待网页。如果 Wifi 模块响应 HTML 格式的页面，浏览器将显示它。 接下来的例子会教您如何做所有这些有趣的事情。

### Example 4: 使用 WiFi Shield 作为 Webserver (来自扩展板的服务网页)

正如您在 Example 3 中看到的，浏览器可以连接到 WiFi shield。一旦建立了连接(当浏览器发送 HTTP 请求时)，WiFi shield 可以发回 HTML 代码以使浏览器显示网页。在这个例子中，您将了解扩展板响应浏览器需要什么。

**步骤 1: Arduino Code**

上传以下代码到您的 Arduino，分别用您的 Wifi 热点信息替换 "myssid" 和 "mypassword" :

```c
#include <SoftwareSerial.h>
#include "WiFly.h"

#define SSID      "myssid"
#define KEY       "mypassword"
// check your access point's security mode, mine was WPA20-PSK
// if yours is different you'll need to change the AUTH constant, see the file WiFly.h for avalable security codes
#define AUTH      WIFLY_AUTH_WPA2_PSK

int flag = 0;

// Pins' connection
// Arduino       WiFly
//  2    <---->    TX
//  3    <---->    RX

SoftwareSerial wiflyUart(2, 3); // create a WiFi shield serial object
WiFly wifly(&wiflyUart); // pass the wifi siheld serial object to the WiFly class

void setup()
{
    wiflyUart.begin(9600); // start wifi shield uart port
    Serial.begin(9600); // start the arduino serial port
    Serial.println("--------- WIFLY Webserver --------");

    // wait for initilization of wifly
    delay(1000);

    wifly.reset(); // reset the shield
    delay(1000);
    //set WiFly params

    wifly.sendCommand("set ip local 80\r"); // set the local comm port to 80
    delay(100);

    wifly.sendCommand("set comm remote 0\r"); // do not send a default string when a connection opens
    delay(100);

    wifly.sendCommand("set comm open *OPEN*\r"); // set the string that the wifi shield will output when a connection is opened
    delay(100);

    Serial.println("Join " SSID );
    if (wifly.join(SSID, KEY, AUTH)) {
        Serial.println("OK");
    } else {
        Serial.println("Failed");
    }

    wifly.sendCommand("get ip\r");
    char c;

    while (wifly.receive((uint8_t *)&c, 1, 300) > 0) { // print the response from the get ip command
        Serial.print((char)c);
    }

    Serial.println("Web server ready");

}

void loop()
{

    if(wifly.available())
    { // the wifi shield has data available
        if(wiflyUart.find("*OPEN*")) // see if the data available is from an open connection by looking for the *OPEN* string
        {
            Serial.println("New Browser Request!");
            delay(1000); // delay enough time for the browser to complete sending its HTTP request string
            // send HTTP header
            wiflyUart.println("HTTP/1.1 200 OK");
            wiflyUart.println("Content-Type: text/html; charset=UTF-8");
            wiflyUart.println("Content-Length: 244"); // length of HTML code
            wiflyUart.println("Connection: close");
            wiflyUart.println();

            // send webpage's HTML code
            wiflyUart.print("<html>");
            wiflyUart.print("<head>");
            wiflyUart.print("<title>My WiFI Shield Webpage</title>");
            wiflyUart.print("</head>");
            wiflyUart.print("<body>");
            wiflyUart.print("<h1>Hello World!</h1>");
            wiflyUart.print("<h3>This website is served from my WiFi module</h3>");
            wiflyUart.print("<a href=\"http://yahoo.com\">Yahoo!</a> <a href=\"http://google.com\">Google</a>");
            wiflyUart.print("<br/><button>My Button</button>");
            wiflyUart.print("</body>");
            wiflyUart.print("</html>");
        }
    }
}
```

**步骤 2: 获取 Wifi Shield 的 IP 地址**

打开串口监视器窗口，等待显示 "Web server ready" 消息。串口监视器也将显示 WiFi shield 的IP地址 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-serial-comm-window.png)

*Arduino 程序自带的串口打印窗口输出，扩展版地址高亮。*

**步骤 3: 访问网页**

现在在您的浏览器中访问该 IP 地址。应该显示下面的网页，它包含一个链接到 Yahoo! 和 Google 和一个暂时还没用到的按钮 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-simple-webserver-page.png)

*带有两个链接和一个按钮的网页*

当网页被访问时，串口监视器窗口也将显示 "New Browser Request!" 字符串如下所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-simple-webserver-arduino-serial-window-response.png)

*检测到新的浏览器访问请求*

<div class="admonition note">
<p class="admonition-title">Note</p>
在使用某些浏览器(如 Google Chrome) 的情况下，即使在栏中输入 URL 也会发送网页请求，这是因为这些浏览器在用户访问网页之前就会尝试获取网页的标题。
</div>


### Example 5: 从网页端控制 Arduino 数字引脚

在这个例子中，我们将创建一个带有三个按钮的网页来控制 Arduino 中的三个不同的数字引脚。

请按照以下步骤操作。我们还创建了一个视频以更详细地解释代码。

[Video - WiFi Shield Arduino Digital Pin Control From Webpage](https://www.youtube.com/watch?v=ek63patAl80)

**步骤 1: 硬件连接**

将三个 LED 和电阻连接到数字引脚 **11**,**12** 和 **13**，如下图所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-schematic.png)

*三个LED灯和3个1K欧的电阻连接到引脚11、12和13*

**步骤 2: 打开 Arduino 新建工程**

将代码上传到 Arduino，使用您的接入热点的 SSID 名称和密码替换 "mySSID" 和 "myPassword" :

```c
#include <SoftwareSerial.h>
#include "WiFly.h"

#define SSID      "mySSID"
#define KEY       "myPassword"
// check your access point's security mode, mine was WPA20-PSK
// if yours is different you'll need to change the AUTH constant, see the file WiFly.h for avalable security codes
#define AUTH      WIFLY_AUTH_WPA2_PSK

int flag = 0;

// Pins' connection
// Arduino       WiFly
//  2    <---->    TX
//  3    <---->    RX

SoftwareSerial wiflyUart(2, 3); // create a WiFi shield serial object
WiFly wifly(&wiflyUart); // pass the wifi siheld serial object to the WiFly class
char ip[16];

void setup()
{
    pinMode(11,OUTPUT);
    digitalWrite(11,LOW);

    pinMode(12,OUTPUT);
    digitalWrite(12,LOW);

    pinMode(13,OUTPUT);
    digitalWrite(13,LOW);

    wiflyUart.begin(9600); // start wifi shield uart port

    Serial.begin(9600); // start the arduino serial port
    Serial.println("--------- WIFLY Webserver --------");

    // wait for initilization of wifly
    delay(1000);

    wifly.reset(); // reset the shield
    delay(1000);
    //set WiFly params

    wifly.sendCommand("set ip local 80\r"); // set the local comm port to 80
    delay(100);

    wifly.sendCommand("set comm remote 0\r"); // do not send a default string when a connection opens
    delay(100);

    wifly.sendCommand("set comm open *OPEN*\r"); // set the string that the wifi shield will output when a connection is opened
    delay(100);

    Serial.println("Join " SSID );
    if (wifly.join(SSID, KEY, AUTH)) {
        Serial.println("OK");
    } else {
        Serial.println("Failed");
    }

    wifly.sendCommand("get ip\r");

    wiflyUart.setTimeout(500);
    if(!wiflyUart.find("IP="))
    {
        Serial.println("can not get ip");
        while(1);;
    }else
    {
        Serial.print("IP:");
    }

    char c;
    int index = 0;
    while (wifly.receive((uint8_t *)&c, 1, 300) > 0) { // print the response from the get ip command
        if(c == ':')
        {
            ip[index] = 0;
            break;
        }
        ip[index++] = c;
        Serial.print((char)c);
        ?
    }
    Serial.println();
    while (wifly.receive((uint8_t *)&c, 1, 300) > 0);;
    Serial.println("Web server ready");
}

void loop()
{
    if(wifly.available())       // the wifi shield has data available
    {

        if(wiflyUart.find("*OPEN*")) // see if the data available is from an open connection by looking for the *OPEN* string
        {
            Serial.println("New Browser Request!");
            delay(1000); // delay enough time for the browser to complete sending its HTTP request string

            if(wiflyUart.find("pin=")) // look for the string "pin=" in the http request, if it's there then we want to control the LED
            {
                Serial.println("LED Control");
                // the user wants to toggle the LEDs
                int pinNumber = (wiflyUart.read()-48); // get first number i.e. if the pin 13 then the 1st number is 1
                int secondNumber = (wiflyUart.read()-48);
                if(secondNumber>=0 && secondNumber<=9)
                {
                    pinNumber*=10;
                    pinNumber +=secondNumber; // get second number, i.e. if the pin number is 13 then the 2nd number is 3, then add to the first number
                }
                digitalWrite(pinNumber, !digitalRead(pinNumber)); // toggle pin
                // Build pinstate string. The Arduino replies to the browser with this string.
                String pinState = "Pin ";
                pinState+=pinNumber;
                pinState+=" is ";
                if(digitalRead(pinNumber)) // check if the pin is ON or OFF
                {
                    pinState+="ON"; // the pin is on
                }
                else
                {
                    pinState+="OFF";  // the pin is off
                }
                // build HTTP header Content-Length string.
                String contentLength="Content-Length: ";
                contentLength+=pinState.length(); // the value of the length is the lenght of the string the Arduino is replying to the browser with.
                // send HTTP header
                wiflyUart.println("HTTP/1.1 200 OK");
                wiflyUart.println("Content-Type: text/html; charset=UTF-8");
                wiflyUart.println(contentLength); // length of HTML code
                wiflyUart.println("Connection: close");
                wiflyUart.println();
                // send response
                wiflyUart.print(pinState);
            }
            else
            {
                // send HTTP header
                wiflyUart.println("HTTP/1.1 200 OK");
                wiflyUart.println("Content-Type: text/html; charset=UTF-8");
                wiflyUart.println("Content-Length: 540"); // length of HTML code
                wiflyUart.println("Connection: close");
                wiflyUart.println();

                // send webpage's HTML code
                wiflyUart.print("<html>");
                wiflyUart.print("<head>");
                wiflyUart.print("<title>WiFi Shield Webpage</title>");
                wiflyUart.print("</head>");
                wiflyUart.print("<body>");
                wiflyUart.print("<h1>LED Toggle Webpage</h1>");
                // In the <button> tags, the ID attribute is the value sent to the arduino via the "pin" GET parameter
                wiflyUart.print("<button id=\"11\" class=\"led\">Toggle Pin 11</button> "); // button for pin 11
                wiflyUart.print("<button id=\"12\" class=\"led\">Toggle Pin 12</button> "); // button for pin 12
                wiflyUart.print("<button id=\"13\" class=\"led\">Toggle Pin 13</button> "); // button for pin 13
                wiflyUart.print("<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js\"></script>");
                wiflyUart.print("<script type=\"text/javascript\">");
                wiflyUart.print("$(document).ready(function(){");
                wiflyUart.print("$(\".led\").click(function(){");
                wiflyUart.print("var p = $(this).attr('id');"); // get id value (i.e. pin13, pin12, or pin11)
                // send HTTP GET request to the IP address with the parameter "pin" and value "p", then execute the function
                // IMPORTANT: dont' forget to replace the IP address and port with YOUR shield's IP address and port
                wiflyUart.print("$.get(\"http://");
                wiflyUart.print(ip);
                wiflyUart.print(":80/a\", {pin:p},function(data){alert(data)});");// execute get request. Upon return execute the "function" (display an alert with the "data" send back to the browser.
                wiflyUart.print("});");
                wiflyUart.print("});");
                wiflyUart.print("</script>");
                wiflyUart.print("</body>");
                wiflyUart.print("</html>");
            }
            Serial.println("Data sent to browser");
        }
    }
}
```

**步骤 3: 串口监视器**

打开串口监视器，等待 "Web server ready" 消息显示。串口监视器还会显示 WiFi shield 的 IP 地址 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-serial-comm-window.png)

*Arduino 程序自带的串口打印窗口输出，扩展版地址高亮。*

**步骤 4: 浏览网页**

在网页浏览器中访问 IP 地址。会显示一个带有三个按钮的网页，如下图所示。点击按钮来控制LED。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-webpage.png)

*通过网页端控制 LED 灯*

Arduino 也会反馈给网页浏览器引脚的状态，它们会在警告窗中显示。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-arduino-response.png)

*警告对话框将显示 Arduino 发来的 引脚12的状态信息 “The string Pin12 is ON”。*

当浏览器发送请求访问网页或控制 LED 引脚时，串行监视器也将显示请求。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-led-control-serial-comm-response.png)

*当 HTTP 请求发送到 Wifi shield 时，Arduino 程序自带的串口打印窗口将输出该请求*

### Example 6: WiFi Shield 和 Android App

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Androidapp-ethernet-shield-led-toggle.png)

*使用这个 Android app 您可以通过 WiFi 或者 Ethernet Shield 来控制 Arduino 的引脚。*

**Android App**

我们创建了一个 Android APP，可以通过 WiFi shield 来切换 Arduino 中的数字引脚。在 [Video - WiFi Shield Android App for Arduino Pin Control](https://www.youtube.com/watch?v=0R709uGvkWM) 中观看视频，以查看应用程序是如何工作的，并了解代码:

**软件部分**

从这个 [链接](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFiShieldLEDControl.zip "WiFiShieldLEDControl.zip") 下载 Android Studio 项目和源代码。

### Example 7: 将数据发送到外部服务器并从中检索数据

WiFi shield 中的 RN-171 模块可以充当 HTML 客户端(基于文本的网页浏览器)，这意味着我们可以使用扩展板来发送和接收来自 Web 服务器的数据。在这个例子中，您将学习如何使用具有 Web 应用程序编程接口 (API) 的扩展板来显示任何城市的天气数据(即温度，湿度等)。

我们将使用的 API 的名称是 [OpenWeatherMap](http://openweathermap.org/api)，当您将城市和国家的名称发送到该网站时，它会返回一个包含天气信息的 JSON 字符串。例如，如果您想显示伦敦英国的天气，请参阅此链接 : http://openweathermap.org/appid 。从 2015 年 10 月 9 日开始，该网站要求用户在访问 API 前注册 API 密钥。获得API密钥后，您将可以访问以下URL http://api.openweathermap.org/data/2.5/weather?q=London,uk 它将返回如下所示的 JSON 字符串，其中包含了天气数据和其他信息。
```
{
    "coord":{"lon":-0.13,"lat":51.51},
    "sys":{"type":3,"id":60992,"message":0.0079,"country":"GB","sunrise":1421395087,"sunset":1421425352},
    "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],
    "base":"cmc stations",
    "main":{
        "temp":277.25,"humidity":79,"pressure":998.4,
        "temp_min":277.25,"temp_max":277.25
    },
    "wind":{
    "speed":2,"gust":5,"deg":180},
    "rain":{"3h":0},"clouds":{"all":32},
    "dt":1421372140,"id":2643743,"name":"London","cod":200
}
```

**步骤 1: The URL**

让我们继续为美国旧金山检索天气 JSON 字符串。我们的 WiFi shield 需要访问的URL如下 :

    http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco,US

**步骤 2: Arduino 代码**

[WiFly manual](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf) 的第 13 部分展示了连接到 Web 服务器的不同方法，但是无论如何，我们需要指定服务器的名称(如果服务器没有域名就指定IP地址)，然后是我们希望发送的数据。

我们需要发送到 WiFi shield 以接收来自 OpenWeatherMap 服务器的 JSON 字符串的命令如下 :

    set ip proto 18 //enable html client
    set dns name api.openweathermap.org //name of your webserver
    set ip address 0 // so WiFly will use DNS
    set ip remote 80 // standard webserver port
    set com remote 0 // turn off the REMOTE string so it does not interfere with the post
    open // to open the connection
    GET /data/2.5/weather?q=San%20Francisco,US \n\n // to send the data


这是将发送命令的 arduino 代码 :

```c
#include <SoftwareSerial.h>
#include "WiFly.h"

#define SSID      "mySSID"
#define KEY       "myPassword"
// check your access point's security mode, mine was WPA20-PSK
// if yours is different you'll need to change the AUTH constant, see the file WiFly.h for avalable security codes
#define AUTH      WIFLY_AUTH_WPA2_PSK

// Pins' connection
// Arduino       WiFly
//  2    <---->    TX
//  3    <---->    RX

SoftwareSerial wiflyUart(2, 3); // create a WiFi shield serial object
WiFly wifly(&wiflyUart); // pass the wifi siheld serial object to the WiFly class

void setup()
{
    wiflyUart.begin(9600); // start wifi shield uart port
    Serial.begin(9600); // start the arduino serial port
    Serial.println("--------- OpenWeatherMap API --------");

    // wait for initilization of wifly
    delay(3000);
    wifly.reset(); // reset the shield
    Serial.println("Join " SSID );
    if (wifly.join(SSID, KEY, AUTH)) {
        Serial.println("OK");
    } else {
        Serial.println("Failed");
    }

    wifly.sendCommand("set ip proto 18\r"); //enable html client
    delay(100);

    wifly.sendCommand("set dns name api.openweathermap.org\r"); // name of the webserver we want to connect to
    delay(100);

    wifly.sendCommand("set ip address 0\r"); // so WiFly will use DNS
    delay(100);

    wifly.sendCommand("set ip remote 80\r"); /// standard webserver port
    delay(100);

    wifly.sendCommand("set com remote 0\r"); // turn off the REMOTE string so it does not interfere with the post
    delay(100);

    wifly.sendCommand("open\r"); // open connection
    delay(100);

    wiflyUart.print("GET /data/2.5/weather?q=San%20Francisco,US \n\n");
    delay(1000);

}

void loop()
{
    //As soon as the data  received from the Internet ,output the data through the UART Port .
    while (wifly.available())
    {
        Serial.write(wifly.read());
    }
}
```

**步骤 3: 查看结果**

打开串口监视器，可以看到您在浏览器中看到的相同的 JSON 字符串。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Open-weather-api-json-string.png)

*JSON 天气字符将显示在 Arduino 串行监视器窗口*

### Example 8 : 与终端 TCP 通信

在这个例子中，我们将向您展示如何将 WiFi shield 的信息发送到 PC 终端程序。我们将制作一个简单的 Arduino 控制台，这个控制台包含一些菜单，让您可以选择查看 Arduino 数字引脚的状态并切换。

**步骤 1: 下载一个 TCP 终端**

[下载并安装 RealTerm](http://sourceforge.net/projects/realterm/files/Realterm/2.0.0.70/Realterm_2.0.0.70_setup.exe/download)，这个链接是一个公用事业终端，可以连接到 WiFi shield。

**步骤 2: Arduino Code**

将下面的代码上传到 Arduino，用您自己的接入点信息替换 "mySSID"，"myPassword" 和验证码 :

```c
#include <SoftwareSerial.h>
#include "WiFly.h"

#define SSID      "mySSID"
#define KEY       "myPassword"
// check your access point's security mode, mine was WPA20-PSK
// if yours is different you'll need to change the AUTH constant, see the file WiFly.h for avalable security codes
#define AUTH      WIFLY_AUTH_WPA2_PSK

#define FLAG_MAIN_MENU 1
#define FLAG_SUB_MENU_2 2

int flag = FLAG_MAIN_MENU;

// Pins' connection
// Arduino       WiFly
//  2    <---->    TX
//  3    <---->    RX

SoftwareSerial wiflyUart(2, 3); // create a WiFi shield serial object
WiFly wifly(&wiflyUart); // pass the wifi siheld serial object to the WiFly class

void setup()
{

    // define the pins we can control
    pinMode(11,OUTPUT);
    digitalWrite(11,LOW);

    pinMode(12,OUTPUT);
    digitalWrite(12,LOW);

    pinMode(13,OUTPUT);
    digitalWrite(13,LOW);

    pinMode(7,OUTPUT);
    digitalWrite(7,LOW);

    wiflyUart.begin(9600); // start wifi shield uart port

    Serial.begin(9600); // start the arduino serial port
    Serial.println("--------- TCP Communication --------");

    // wait for initilization of wifly
    delay(1000);

    wifly.reset(); // reset the shield
    delay(1000);

    wifly.sendCommand("set ip local 80\r"); // set the local comm port to 80
    delay(100);

    wifly.sendCommand("set comm remote 0\r"); // do not send a default string when a connection opens
    delay(100);

    wifly.sendCommand("set comm open *\r"); // set the string or character that the wifi shield will output when a connection is opened "*"
    delay(100);

    wifly.sendCommand("set ip protocol 2\r"); // set TCP protocol
    delay(100);

    Serial.println("Join " SSID );
    if (wifly.join(SSID, KEY, AUTH)) {
        Serial.println("OK");
    } else {
        Serial.println("Failed");
    }

    wifly.sendCommand("get ip\r");
    char c;

    while (wifly.receive((uint8_t *)&c, 1, 300) > 0) { // print the response from the get ip command
        Serial.print((char)c);
    }

    Serial.println("TCP Ready");
}

void loop()
{

    if(wifly.available())
    {
        delay(1000); // wait for all the characters to be sent to the WiFi shield
        char val = wiflyUart.read(); // read the first character

        if(flag == FLAG_MAIN_MENU)
        {
            switch(val)
            {
                case '*': // search for the new connection string
                printMainMenu();
                break;
                case '1': // the user typed 1, display the pin states
                printPinStates();
                printMainMenu();
                break;
                case '2': // the user typed 2, display the sub menu (option to select a particular pin)
                printSubMenu2();
                flag = FLAG_SUB_MENU_2; // flag to enter the sub menu
                break;
                default:
                wiflyUart.print("INVALID SUBMENU\r\n");
                break;
            }
        }
        else if(flag == FLAG_SUB_MENU_2)
        {
            int pinNumber = val-48; // get first number i.e. if the pin 13 then the 1st number is 1
            int secondNumber = (wiflyUart.read()-48);
            if(secondNumber>=0 && secondNumber<=9)
            {
                pinNumber*=10;
                pinNumber +=secondNumber; // get second number, i.e. if the pin number is 13 then the 2nd number is 3, then add to the first number
            }

            // Create the "You want to toggle pin x?? OK..." string.
            String response = "\r\nYou want to toggle pin ";
            response+=pinNumber;
            response+="? OK...\r\n";

            wiflyUart.print(response);

            digitalWrite(pinNumber, !digitalRead(pinNumber)); // toggle pin

            wiflyUart.print("Pin Toggled!\r\n"); // let user know the pin was toggled.
            printMainMenu();
            flag = FLAG_MAIN_MENU;
        }
    }

}

/*
* Prints the main menu options
*/
void printMainMenu()
{
    wiflyUart.print("\r\n\r\n");
    wiflyUart.print("Arduino Console Menu: \r\n");
    wiflyUart.print("1. Show digital pin states\r\n");
    wiflyUart.print("2. Toggle a digital pin's state\r\n");
    wiflyUart.print("\r\n\r\n");
}

// displays the pin states
void printPinStates()
{

    String pinState = "Pin 7 is ";
    pinState+=getPinState(7);
    pinState+="\r\n";

    pinState += "Pin 11 is ";
    pinState+=getPinState(11);
    pinState+="\r\n";

    pinState += "Pin 12 is ";
    pinState+=getPinState(12);
    pinState+="\r\n";

    pinState += "Pin 13 is ";
    pinState+=getPinState(13);
    pinState+="\r\n";

    wiflyUart.print(pinState);
}

// prints the option to enter a pin number
void printSubMenu2()
{
    wiflyUart.print("\r\nEnter the pin number you wish to toggle: ");
}
?
// get a pin state as a string.
String getPinState(int pinNumber)
{
    if(digitalRead(pinNumber)) // check if the pin is ON or OFF
    {
        return "ON"; // the pin is on
    }
    else
    {
        return "OFF";  // the pin is off
    }
}
```

**步骤 3: 获取扩展板的 IP 地址和端口**

打开 Arduino 串口监视器，获取 WiFi Shield 的 IP 地址和端口号，如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Tcp-arduino-serial-comm.png)

**Arduino 程序自带的串口打印窗口输出 TCP 例程, the ip 地址和端口号在图中高亮**

上图中的 IP 地址和端口 :

    192.168.0.10:80

**步骤 4: 配置 TCP 终端然后连接到 Shield**

打开 RealTerm 并在 "Display" 选项卡中为 "Rows" 输入 "30" 并选择 "Scrollback" 选项 :

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Realterm-display-tab.png)

*RealTerm window: rows = 30, 并且勾选 Scrollback 选项.*

在 RealTerm 程序的 "Port" 选项卡中，输入扩展板的 IP 地址和端口，例如 192.168.0.10:80，然后点击 "Open" 按钮，Arduino 的硬编码主菜单应该显示在终端上。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Realterm-port-tab.png)

*RealTerm window. 端口栏有 WiFi shield's 的 IP 地址和端口号*

在 "Send" 标签中选择菜单 "1" 或 "2" 中的一个选项，在文本框中输入，然后按 "Send ASCII" 发送值。

例如，要切换引脚 **13** 状态，输入 "2" 并按 "Send ASCII"，当提示 "Enter the pin number you wish you toggle" 时，输入 "13" 并点击 "Send ASCII"。Arduino 会回复 "Pin Toggled!" 并返回到主菜单。现在输入 "1"，然后按 "Send ASCII" 查看引脚的当前状态。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Realterm-send-tab.png)

*RealTerm window. 正如黄色文本所示，引脚13的状态已经从 **OFF** 变成了 **ON**。*

### Example 9: WiFi Shield 和 Relay Shield 配合使用

现在您明白如何发送和接收来自 WiFi shield 的信息，可以看见通过网络控制任何类型的设备都很容易。

如果您希望通过网页或电话应用程序控制台灯，电机或水泵等大功率设备，我们推荐使用 [Relay Shield V2.0](http://wiki.seeedstudio.com/cn/Relay_Shield_v3/#_7).

Relay Shield V3 使用引脚 **4**，引脚 **5**，引脚 **6** 和引脚 **7**，因此它完全兼容本页示例中的代码。

### Example 10: Adhoc 模式

要在 Adhoc 模式下使用扩展板作为接入点，只需将扩展板的引脚 **IO9** 连接到 Arduino 中的 3.3V 引脚(如下所示)，然后重置扩展板(如果打开)。

![](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/img/Wifi-shield-adhoc-mode-hardware-connection.png)

*Shield 连接需要 adhoc 模式. IO9 引脚连接到3.3V。*

为了获得扩展板的 SSID，将 Example 1 中的代码上传到 Arduino 并打开串口监视器，扩展板将会响应它的 SSID，如下例所示，在这种情况下 **WiFly-EZX-1b** 是 SSID。

    AP mode as WiFly-EZX-1b on chan 1

现在能够连接到 WiFi shield 作为一个接入点，例如 SSID 可以在电脑的 WiFi 网络列表中可见。

要了解有关 adhoc 模式的更多信息，请查看 [WiFly RN 用户手册](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf) 的 16 章的 "Adhoc Networking Mode"

## 资源下载
---------

-   **[Eagle 文件]** [WiFi Shield V2.0 Eagle Files](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/Wifi_Shield_v2.0.zip)
-   **[原理图 PDF]** [Schematic PDF](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/Wifi_shield_v2_schematic.pdf)
-   **[库文件]** [Wifi Shield Library](https://github.com/Seeed-Studio/WiFi_Shield)
-   **[芯片数据手册]** [RN-171 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-171.pdf)
-   **[用户手册]** [WiFi Module User Manual](https://raw.githubusercontent.com/SeeedDocument/Wifi_Shield_V2.0/master/res/WiFly-RN-UM.pdf) *-- This is where you'll find all the commands for the RN-171 module in the shield.*
-   **[其他资源]** [What is a Seeeduino](/Seeeduino_v4.2)
-   **[其他资源]** [w3schools](http://www.w3schools.com/) Great website to learn HTML, Javascript, and JQuery


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Wifi_Shield_V2.0 -->
