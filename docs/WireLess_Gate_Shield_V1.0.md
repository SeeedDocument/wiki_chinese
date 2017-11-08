---
title: WireLess Gate Shield V1.0
category: MakerPro
bzurl: https://www.seeedstudio.com/WireLess-Gate-Shield-p-2117.html
oldwikiname:  WireLess Gate Shield V1.0
prodimagename:  WLG_h.jpg
wikiurl: http://seeed.wiki/WireLess_Gate_Shield_V1.0
sku:      113990088
---
![](https://github.com/SeeedDocument/WireLess_Gate_Shield_V1.0/raw/master/img/WLG_h.jpg)

WireLess Gate Shield 是兼容 Arduino 的扩展板，旨在构建一个接收/发送和广播各种无线命令和数据的系统。为了最大限度地覆盖板上的无线通信接口，它有一个红外接收器接口，用于连接流行的收发器 nRF24L01 + 和 RFM69HW。此外，该主板还有一个实时时钟模块 DS1307。

![](https://github.com/SeeedDocument/WireLess_Gate_Shield_V1.0/raw/master/img/WLG_intro.jpg)

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.22.43e0812aZvyfUL&id=534769649601)

##   产品特性
---
*   接口可安装 315/433/868/915 MHz 的 [RFM69HW](http://devicter.ru/goods/RFM69HW-RF-transceiver)（取决于不同版本）
*   接口可安装 2.4 GHz 的 [nRF24L01 +](http://www.seeedstudio.com/depot/s/nRF24L01.html?search_in_description=0)
*   红外接收器
*   基于 DS1307 的电池供电的实时时钟模块
*   无线电模块 LED 活动指示灯
*   用户预留 LED
*   时钟采用按键控制
*   兼容 [GROVE](http://www.seeedstudio.com/depot/Grove-t-3.html?ref=top) 接口: I2C
*   与 [Ethernet Shield](http://www.seeedstudio.com/depot/W5200-Ethernet-Shield-p-1577.html) 完全兼容

##   电路图和布局
---
![](https://github.com/SeeedDocument/WireLess_Gate_Shield_V1.0/raw/master/img/Wl-top.png)

WireLess Gate Shield 的左侧是无线模块的接口：

*   nRF24l01 + ，包括增强 ("PA") 版本 (上部)
*   RFM69HW (下部)。

无线模块之间是用于 RFM69HW 外部天线的 U.FL 连接器。如果您打算使用常规天线（需要一定长度的导线） - 可以直接焊接到 Schild 上（靠近连接器 U.FL）。

在模块的右上方是 RFM69HW LED LED1 "RF433"

在电路板的中央部分有一个用于时钟模块 DS1307 供电电池的插槽

电池槽右下方的是 I2C 连接器

右边是（自上而下）：

*   LED LED2 "RF24"
*   红外接收器
*   LED LED3 - 用户预留
*   时钟按钮 S1

![](https://github.com/SeeedDocument/WireLess_Gate_Shield_V1.0/raw/master/img/Wl-Scheme.PNG)

##   基本功能
---
在基本版本中（不使用 Ethernet Shield ）可以在无线电和红外接收器之间设置一个无线网关。

命令（或数据）可以根据用户程序的逻辑通过所有三个无线接口进行广播。

实时时钟模块的用途在于可以把参考日期/时间与任何数据/命令一起发送出去。

设备管理可以使用扩展板上的按钮进行调整。

##  其他用途
---
此外，WireLess Gate Shield 可以使用Grove 接口连接任何 I2C 设备（传感器，显示器等）。

WireLess Gate Shield 被设计为与 [Ethernet Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.325db94279fWiP&id=534263404757) 完全兼容，这样你就可以一起使用两块板子创造一些更先进的无线通讯装置（在 SD 卡中存储，通过网络传输数据，通过网络管理无线设备）。

##  接口
---
*   RF 模块 nRF24L01 + 的接口：
    *   D11 - MOSI

        *   D12 - MISO
    *   D13 - SCK

        *   D7 - RF24_CE

        *   D8 - RF24_CSN

        *   D2 - RF24_IRQ

*   RF-module RFM69HW 的接口：
    *   D11 - MOSI

        *   D12 - MISO
    *   D13 - SCK

        *   D9 - RF433_NSS

        *   A0 - RF433_RESET

        *   D3 - RF433_IRQ

*   A4 (SDA), A5 (SCL) - "I2C" 接口(接口的另外两个引脚 - VCC 和 GND 用于传感器供电)
*   A4 (SDA), A5 (SCL) - RTC DS1307 并行接口
*   A1 - 按钮
*   D6 - 自定义 LED (LED3)

##  WireLess Gate Shield 产品特性
---
###   无线模式

两个模块 RFM69HW 和 nRF24l01 + 通过 SPI 总线连接。

选择无线模块时要选择合适的 CSN 和 NSS 引脚来控制使能端。

*   CSN (D8) 用于 nRF24l01 +
*   NSS (D9) 用于 RFM69HW

!!!Warning
如果已安装，但软件不涉及 RFM69HW，请务必将该模块的 NSS 引脚置于高电平状态。否则将干扰 nRF24l01 + 和 Ethernet Shield 的正常运行。

###   无线模块的自动显示

无线模块的 LED 指示灯操作如下：

*   LED1 "RF24" 的负极连接到模块 nRF24l01 的引脚 **CSN (D8)** ,LED 的正极（通过限流电阻）连接到 **SPI** 的 **SCK(D13)** 口
*   LED2 "RF433" 的负极连接到模块 RFM69HW 的引脚 **NSS (D9)** ，LED 的正极（通过限流电阻）连接到 **SPI** 的 **SCK(D13)** 口

当无线电休眠时，在适当的芯片引脚（CSN 和 NSS）输出高电平，引脚 SCK 的时钟就不会点亮 LED。

如果 MK 与其他无线电模块通信，会选择适当的引脚(CSN 和 NSS)设置为低电平，同时引脚 SCK 会发出脉冲点亮通信 LED 。

因此，用户不需要在 MC 上做任何编程工作来示意模块的工作状态。

###   产品特性

如有必要，SMD-LED 可取代普通输出端口（例如，连接一个显示屏）：

*   电路板靠近通讯 LED 的地方可以焊接直插 LED（或者使用跳线）
*   电路板上有限流电阻（不需要给 LED 串联限流电阻）
*   在设置 LED 的输出时必须从板上移除 SMD-LED

###   通过IR进行修改

自定义 LED 可以被 LED3 引脚 IR LED 取代，从而进一步扩展 WireLess Gate Shield 的使用范围（例如，可以通过任何无线接口或使用红外命令的 LAN 控制设备发送命令）。

##  函数库

###  必备函数库

要使用 WireLess Gate Shield，需要以下库：

*   使用 nRF24L01 + - [RF24](https://github.com/maniacbug/RF24/archive/master.zip)

*  使用 RFM69HW - [RFM69](https://github.com/LowPowerLab/RFM69/archive/master.zip)

*   实时时钟 (RTC) - [RTClib](https://github.com/adafruit/RTClib/archive/master.zip)

*   IR-接收管 - [IRremote](https://github.com/shirriff/Arduino-IRremote/archive/master.zip)

此外，在使用 RF24 和 LCD 显示器时还需要使用库：

*   SPI

.函数库是理解这些接口如何工作的极佳教程。

###   功能函数库

**NRF24l01 + **

初始化模块 nRF24l01 + 如下：

```
//RF24 radio(CE,CSN);
RF24 radio(7,8);
```


**RFM69HW**

如果使用模块 RFM69HW ，需要对 RFM69.h 做如下更改：

在文件开头找到下面几行：

```
#define SPI_CS               SS // SS is the SPI slave select pin, for instance D10 on atmega328
#define RF69_IRQ_PIN          2 // INT0 on AVRs should be connected to DIO0 (ex on Atmega328 it's D2)
```

然后把上面几行替换为：

```
//#define SPI_CS               SS // SS is the SPI slave select pin, for instance D10 on atmega328
//#define RF69_IRQ_PIN          2 // INT0 on AVRs should be connected to DIO0 (ex on Atmega328 it's D2)
#define SPI_CS               9 // SS is the SPI slave select pin, for WireLess Gate Shield - D9
#define RF69_IRQ_PIN          3 // INT1 on AVRs should be connected to DIO0 (ex on Atmega328 it's D3)
```

此外，在文件 RFM69.cpp 中找到下面一行：

```
void RFM69::isr0() { selfPointer-&gt;interruptHandler(); }
```

然后把它替换为：

```
//void RFM69::isr0() { selfPointer-&gt;interruptHandler(); }
void RFM69::isr1() { selfPointer-&gt;interruptHandler(); }
```

初始化模块 RFM69HW 如下：


```
  resetRFM69();
  radio.setCS(9); // NSS - D9
  radio.initialize(FREQUENCY,NODEID,NETWORKID);
```


!!!Note
  使用寄存器控制 RFM69HW 的工作模式。如果想了解更多请参考文件 RFM69.cpp 的函数 RFM69 :: initialize。为了更好地理解目标寄存器 ，请阅读 RFM69registers.h（也包含在库中） 和文档 [radio RFM69HW](http://st.devicter.ru/9/1115/243/RFM69HW.pdf)。


##   示例

###    WireLess Gate Shield 主要部件示例代码（使用 RTC, IR, RFM69HW, nRF24l01 +）

*   发送信息到另一个 RFM69HW 并接收响应( ping-pong 机制)。
*   nRF24l01 + 收到消息后输出到屏幕上。
*   通过红外接收器接收命令（识别的命令显示在显示器上）并点亮自定义 LED。

所有结果都显示在串口监视器中
```
#include <RFM69.h>
#include <SPI.h>
#include "RF24.h"
#include <IRremote.h>
#include <Wire.h>
#include "RTClib.h"

RF24 radio24(7,8);

RTC_DS1307 RTC;

int RECV_PIN = 5;

IRrecv irrecv(RECV_PIN);

decode_results results;

// create a framework for the transmission of values
typedef struct{
    int SensorID;        // ID sensor
    int CommandTo;       // command module number ...
    int Command;         // command
    // 0 - answer
    // 1 - get the value
    // 2 - set the value
    int ParamID;         // parameter identifier
    float ParamValue;    // value
    boolean Status;      // status
    // 0 - read-only (RO)
    // 1 -  can change the (RW)
    char Comment[16];    // comment
}
Message;

Message sensor;

const uint64_t pipes[2] = {
0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };

volatile boolean waitRF24 = false;

#define NODEID      99
#define NETWORKID   100
#define GATEWAYID   1
#define FREQUENCY   RF69_433MHZ //Match this with the version of your Moteino! (others: RF69_433MHZ, RF69_868MHZ)
#define KEY         "thisIsEncryptKey" //has to be same 16 characters/bytes on all nodes, not more not less!
#define LED         6
#define SERIAL_BAUD 115200
#define ACK_TIME    30  // # of ms to wait for an ack

#define RFM69_RESET 14  //A0
#define RFM69_NSS 9
#define RFM69_DIO0 3

#define BUTTON 15 // A1

#define MOSI 11
#define MISO 12
#define SCK 13

int TRANSMITPERIOD = 500; //transmit a packet to gateway so often (in ms)
byte sendSize=0;
boolean requestACK = false;
RFM69 radio;

int delta=2000;

unsigned long blinkStop;
unsigned long timeReady;

typedef struct {
    int           nodeId; //store this nodeId
    unsigned long uptime; //uptime in ms
    float         temp;   //temperature maybe?
}
Payload;
Payload theData;

void setup() {
    Serial.begin(SERIAL_BAUD);

    pinMode(LED, OUTPUT);

    pinMode(RFM69_NSS, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(MOSI, OUTPUT);
    pinMode(MISO, INPUT);
    pinMode(SCK, OUTPUT);

    pinMode(RFM69_RESET, OUTPUT);
    pinMode(RFM69_DIO0, INPUT);

    pinMode(BUTTON, INPUT);

    digitalWrite(RFM69_NSS, HIGH);
    digitalWrite(7, HIGH);

    resetRFM69();
    radio.setCS(RFM69_NSS);
    radio.initialize(FREQUENCY,NODEID,NETWORKID);

    //radio.setHighPower(); //uncomment only for RFM69HW!

    radio.encrypt(KEY);
    char buff[50];
    sprintf(buff, "\nTransmitting at %d Mhz...", FREQUENCY==RF69_433MHZ ? 433 : FREQUENCY==RF69_868MHZ ? 868 : 915);
    Serial.println(buff);

    radio24.begin();
    // optionally, increase the delay between retries & # of retries
    radio24.setRetries(15,15);
    radio24.setChannel(119);
    // по умолчанию СЛУШАЕМ
    radio24.openWritingPipe(pipes[1]);
    radio24.openReadingPipe(1,pipes[0]);
    radio24.startListening();

    delay(20);

    attachInterrupt(0, isr_RF24, FALLING);

    irrecv.enableIRIn();

    Wire.begin();
    RTC.begin();

    if (! RTC.isrunning()) {
        Serial.println("RTC is NOT running!");
        // following line sets the RTC to the date & time this sketch was compiled
        RTC.adjust(DateTime(__DATE__, __TIME__));
    }
}

long lastPeriod = -1;
void loop() {

    //check for any received packets
    if (radio.receiveDone())
    {
        Serial.print('[');
        Serial.print(radio.SENDERID, DEC);
        Serial.print("] ");
        for (byte i = 0; i < radio.DATALEN; i++)
        Serial.print((char)radio.DATA[i]);
        Serial.print("   [RX_RSSI:");
        Serial.print(radio.readRSSI());
        Serial.print("]");

        if (radio.ACK_REQUESTED)
        {
            radio.sendACK();
            Serial.print(" - ACK sent");
            delay(10);
        }
        Serial.println();
    }

    int currPeriod = millis()/TRANSMITPERIOD;
    if (currPeriod != lastPeriod)
    {
        //fill in the struct with new values
        theData.nodeId = NODEID;
        theData.uptime = millis();
        theData.temp = radio.readTemperature();//91.23; //it's hot!

        Serial.print("Sending struct (");
        Serial.print(sizeof(theData));
        Serial.print(" bytes) ... ");
        if (radio.sendWithRetry(GATEWAYID, (const void*)(&theData), sizeof(theData)))
        Serial.print(" ok!");
        else Serial.print(" nothing...");
        Serial.println();
        lastPeriod=currPeriod;
    }

    listenRF24();

    if (irrecv.decode(&results)) {
        Serial.println(results.value, HEX);
        irrecv.resume(); // Receive the next value
        blinkStop=millis()+100;
        digitalWrite(LED, HIGH);
    }

    if (digitalRead(BUTTON)==LOW) {
        blinkStop=millis()+1000;
        digitalWrite(LED, HIGH);
    }

    if (millis()>blinkStop) {
        digitalWrite(LED, LOW);
    }

    if(millis()>timeReady){
        timeReady=millis()+2000;
        DateTime now = RTC.now();

        Serial.print(now.year(), DEC);
        Serial.print('/');
        Serial.print(now.month(), DEC);
        Serial.print('/');
        Serial.print(now.day(), DEC);
        Serial.print(' ');
        Serial.print(now.hour(), DEC);
        Serial.print(':');
        Serial.print(now.minute(), DEC);
        Serial.print(':');
        Serial.print(now.second(), DEC);
        Serial.println();
    }
}

void Blink(byte PIN, int DELAY_MS)
{
    pinMode(PIN, OUTPUT);
    digitalWrite(PIN,HIGH);
    delay(DELAY_MS);
    digitalWrite(PIN,LOW);
}

void resetRFM69(){
    digitalWrite(RFM69_RESET, HIGH);
    delay(1);
    digitalWrite(RFM69_RESET, LOW);
    delay(10);
}

void isr_RF24(){
    waitRF24 = true;
}

void listenRF24() {
    if (waitRF24) {
        waitRF24 = false;
        if ( radio24.available() )
        {
            bool done = false;
            while (!done)
            {
                done = radio24.read( &sensor, sizeof(sensor) );
                if(sensor.Command == 0) {
                    Serial.print(sensor.SensorID);
                    Serial.print("  ");
                    Serial.print(sensor.ParamID);
                    Serial.print("  ");
                    Serial.print(sensor.ParamValue);
                    Serial.print(" ");
                    Serial.println(sensor.Comment);
                }
            }
        }
    }
}
```
###   代码 "receiver" （在面包板上使用 Arduino Nano 和 RFM69HW 模块进行测试）

*   采用 RFM69HW 结构
*   采用认证机制
*   输出有关模块 RFM69HW（寄存器等）的其他信息

```
#include <RFM69.h>
#include <SPI.h>

#define NODEID      1
#define NETWORKID   100
#define FREQUENCY   RF69_433MHZ //Match this with the version of your Moteino! (others: RF69_433MHZ, RF69_868MHZ)
#define KEY         "thisIsEncryptKey" //has to be same 16 characters/bytes on all nodes, not more not less!
#define LED         6
#define SERIAL_BAUD 115200
#define ACK_TIME    30  // # of ms to wait for an ack

#define RFM69_RESET 14

RFM69 radio;
bool promiscuousMode = false; //set to 'true' to sniff all packets on the same network

typedef struct {
    int           nodeId; //store this nodeId
    unsigned long uptime; //uptime in ms
    float         temp;   //temperature maybe?
} Payload;
Payload theData;

void setup() {
    Serial.begin(SERIAL_BAUD);
    pinMode(RFM69_RESET, OUTPUT);
    pinMode(3, INPUT);
    resetRFM69();
    radio.setCS(9);
    //delay(10);
    radio.initialize(FREQUENCY,NODEID,NETWORKID);

    //radio.setHighPower(); //uncomment only for RFM69HW!

    radio.encrypt(KEY);
    radio.promiscuous(promiscuousMode);
    char buff[50];
    sprintf(buff, "\nListening at %d Mhz...", FREQUENCY==RF69_433MHZ ? 433 : FREQUENCY==RF69_868MHZ ? 868 : 915);
    Serial.println(buff);
}

byte ackCount=0;
void loop() {
    //process any serial input
    if (Serial.available() > 0)
    {
        char input = Serial.read();
        if (input == 'r') //d=dump all register values
        radio.readAllRegs();
        if (input == 'E') //E=enable encryption
        radio.encrypt(KEY);
        if (input == 'e') //e=disable encryption
        radio.encrypt(null);
        if (input == 'p')
        {
            promiscuousMode = !promiscuousMode;
            radio.promiscuous(promiscuousMode);
            Serial.print("Promiscuous mode ");Serial.println(promiscuousMode ? "on" : "off");
        }

        if (input == 'd') //d=dump flash area
        {
            Serial.println("Flash content:");
            int counter = 0;

            while(counter<=256){
                //Serial.print(flash.readByte(counter++), HEX);
                Serial.print('.');
            }
            //while(flash.busy());
            Serial.println();
        }
        if (input == 'D')
        {
            Serial.print("Deleting Flash chip content... ");
            //flash.chipErase();
            //while(flash.busy());
            Serial.println("DONE");
        }
        if (input == 'i')
        {
            Serial.print("DeviceID: ");
            //word jedecid = flash.readDeviceId();
            //Serial.println(jedecid, HEX);
        }
    }

    if (radio.receiveDone())
    {
        Serial.print('[');Serial.print(radio.SENDERID, DEC);Serial.print("] ");
        Serial.print(" [RX_RSSI:");Serial.print(radio.readRSSI());Serial.print("]");
        if (promiscuousMode)
        {
            Serial.print("to [");Serial.print(radio.TARGETID, DEC);Serial.print("] ");
        }

        if (radio.DATALEN != sizeof(Payload))
        Serial.print("Invalid payload received, not matching Payload struct!");
        else
        {
            theData = *(Payload*)radio.DATA; //assume radio.DATA actually contains our struct and not something else
            Serial.print(" nodeId=");
            Serial.print(theData.nodeId);
            Serial.print(" uptime=");
            Serial.print(theData.uptime);
            Serial.print(" temp=");
            Serial.print(theData.temp);
        }

        if (radio.ACK_REQUESTED)
        {
            byte theNodeID = radio.SENDERID;
            radio.sendACK();
            Serial.print(" - ACK sent.");

            // When a node requests an ACK, respond to the ACK
            // and also send a packet requesting an ACK (every 3rd one only)
            // This way both TX/RX NODE functions are tested on 1 end at the GATEWAY
            if (ackCount++%3==0)
            {
                Serial.print(" Pinging node ");
                Serial.print(theNodeID);
                Serial.print(" - ACK...");
                delay(3); //need this when sending right after reception .. ?
                if (radio.sendWithRetry(theNodeID, "ACK TEST", 8, 0))  // 0 = only 1 attempt, no retries
                Serial.print("ok!");
                else Serial.print("nothing");
            }
        }
        Serial.println();
        Blink(LED,3);
    }
}

void Blink(byte PIN, int DELAY_MS)
{
    pinMode(PIN, OUTPUT);
    digitalWrite(PIN,HIGH);
    delay(DELAY_MS);
    digitalWrite(PIN,LOW);
}

void resetRFM69(){
    digitalWrite(RFM69_RESET, HIGH);
    delay(1);
    digitalWrite(RFM69_RESET, LOW);
    delay(10);
}
```

##  产品版本

<table  cellpadding="5" cellspacing="0">
<tr>
<td width="150"> **版次**
</td>
<td width="450"> **描述**
</td>
<td width="80"> **发行日期**
</td></tr>
<tr style="font-size: 90%">
<td> 0.9
</td>
<td> 原型
</td>
<td> 05.05.2014
</td></tr>
<tr style="font-size: 90%">
<td> 1.0
</td>
<td> 公开版本
</td>
<td> 05.07.2014
</td></tr></table>

##   应用

*   普通无线网关 RF2.4 GHz (nRF24l01 +), RF433 MHz (RFM69HW), IR 和 LAN (使用 Ethernet Shield)
*   记录系统命令和数据无线设备的时间 (使用 Ethernet Shield)
*   在某些时间发出无线命令来控制设备 (例如，“在 2014 年 8 月 23 日开灯”或者“每天 5 点自动浇水”)

##   FAQ

*   博客 [WireLess Gate Shield](//devicter.blogspot.ru) RU

*   有疑问请发邮件到 support@devicter.ru

##   购买链接

请分区域选择购买方式：

中国 (全球航运)

[Elecrow store](http://www.elecrow.com/wireless-gate-shield-p-1139.html)

[Seeed store](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.42287da9vYXNKa&id=534769649601)

俄罗斯

[Devicter store](http://devicter.ru/goods/WireLess-Gate-Shield)

##   了解更多

*   **[PDF 文件]**[Description RFM69HW](http://st.devicter.ru/9/1115/243/RFM69HW.pdf)

*   **[PDF 文件]**[Description nRF24l01+](ftp://imall.iteadstudio.com/Modules/IM120606002_nRF24L01_module/DS_nRF24L01.pdf)

*   **[PNG 文件]**[schematic of the device](http://wiki.devicter.ru/images/c/c7/Wl-Scheme.PNG)
