---
title: Grove BLE v1
category: Communication
bzurl: https://seeedstudio.com/Grove-BLE-p-1929.html
oldwikiname: Grove_BLE_v1
prodimagename: Grove-BLE_front.png
wikiurl: http://wiki.seeedstudio.com/cn/Grove-BLE_v1
sku: 113020007
tags: grove_uart, io_3v3, io_5v, plat_duino, plat_linkit
---

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/img/Grove-BLE_front.png)![](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/img/Grove-BLE_Back.png)
</center>

Grove - BLE v1 (Grove - Bluetooth Low Energy v1) 采用低功耗蓝牙模块 -- **HM-11**，基于支持 AT 指令的 TI CC2540 芯片。作为 Grove 产品，Grove - BLE 可以很方便地通过 Base Shield 与 Arduino 板一起使用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.9aa7f57idw0MQ&id=520168459821)

## 规格参数
----------

| 项目      | 参数                                                             |
|---------------------|------------------------------------------------------------------|
| 蓝牙版本          | Bluetooth Specification V4.0 BLE                                 |
| 工作频率   | 2.4GHz ISM band                                                  |
| 调制方法   | GFSK(Gaussian Frequency Shift Keying)                            |
| 射频功率            | -23dbm, -6dbm, 0dbm, 6dbm, can modify through AT Command AT+POWE |
| 传输速率               | Asynchronous: 6K Bytes, Synchronous: 6K Bytes                    |
| 灵敏度         | ≤-84dBm at 0.1% BER                                              |
| 安全性            | 认证与加密                                    |
| Service             | Central & Peripheral UUID FFE0,FFE1                              |
| 电源        | 3.3v - 5v                                                        |
| 工作温度 | –5 ~ +65 摄氏度                                              |
| 大小尺寸                | 40cm x 20cm                                                      |
| 工作电流     | &lt; 10 mA                                                       |
| Sourcing Current    | &lt; 20 mA                                                       |
| 睡眠电流    | &lt; 1 mA                                                        |

<div class="admonition caution">
<p class="admonition-title">Attention</p>
HM-11 的电源是 3.3v，而 Grove - BLE 是 3.3V 至 5V。
</div>

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](
http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

### 引出线

Grove 有四根线缆 : GND, VCC, RX, TX。

### 设计特点

我们使用 TD6810 芯片作为稳压器，所以供电范围是 3.3v 至 5v。 此外，还有一个电平转换电路，确保数据传输的准确性。

### AT 指令集


**1）Query module address (查询模块地址)**

Send： AT+ADDR?

Receive：OK+LADD:address

**2） Query baud rate (查询波特率)**

Send：AT+BAUD?

Receive：OK+Get:[para1]

Range： 0~8; 0--9600，1--19200，2--38400，3--57600，4--115200，5--4800，6--2400，7--1200，8--230400

Default: 0--9600.

**Set baud rate (设置波特率)**

Send：AT+BAUD[para1]

Receive：OK+Set:[para1]

Ex.：Send ：AT+BAUD1 ，Receive：OK+Set:1. The Baud rate has been set to 19200

<div class="admonition note">
<p class="admonition-title">Note</p>
如果设置为 7，下次上电后，模块将不支持任何 AT 指令，直到 PIO0 被按下，模块会将波特率改为 9600。
</div>

**3） Try connect an address (尝试连接一个地址)**

Send：AT+CON[para1]

Receive：OK+CONN[para2]

Range ：A,E,F

Ex.：Try to connect an device which MAC address is 00:17:EA:09:09:09

Send: AT+CON0017EA090909

May receive a reply: OK+CONNA --> Accept request, connecting ; OK+CONNE --> Connect error ; OK+CONN --> Connected , if AT+NOTI1 is setup ; OK+CONNF --> Connect Failed , After 10 seconds

<div class="admonition note">
<p class="admonition-title">Note</p>
只使用中心角色。如果远程设备已经连接到其他设备或关闭，大约 10 秒后会收到 “OK + CONNF”。
</div>


**4） Clear Last Connected device address (清除上次连接的设备地址)**

Send：AT+CLEAR

Receive：OK+CLEAR

**5） Query Module Work Mode (查询模块工作模式)**

Send：AT+MODE?

Receive：OK+Get:[para]

Range： 0~2;

0--Transmission Mode, 1--PIO collection Mode + Mode 0, 2--Remote Control Mode + Mode 0 .

Default: 0

**Set Module Work Mode (设置模块工作模式)**

Send：AT+MODE[]

Receive：OK+Set:[para]

**6） Query Module name (查询模块名称)**

Send：AT+NAME?

Receive：OK+NAME[para1]

**Set Module name (设置模块名称)**

Send：AT+NAME[para1]

Receive：OK+Set:[para1]

Ex.：Send: AT+NAMESeeed， Receive : OK+Set:Seeed

<div class="admonition note">
<p class="admonition-title">Note</p>
下次上电后名称会改变。
</div>

**7） Query Pin Code (查询引脚号)**

Send：AT+PASS?

Receive：OK+PASS:[para1]

Range : 000000~999999.

Default : 000000.

**Set Pin Code (设置引脚号)**

Send: AT+PASS[para1]

Receive：OK+Set:[para1]

**8） Restore all setup value to factory setup (将所有设置值恢复到出厂设置)**

Send：AT+RENEW

Receive：OK+RENEW

**9） Restart module (重新启动模块)**

Send：AT+RESET

Receive：OK+RESET

**10）Query Master and Slaver Role (查询主从角色)**

Send：AT+ROLE[para1]

Receive：OK+Set:[para1]

Range : 0~1;

0--Peripheral : 1--Central : Default: 0.

关于 AT 指令集的更多信息请参考 BLE 模块的芯片数据手册。

SoftwareSerial 通信
----------------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/img/Grove-BLE_connection1.png)

Grove - BLE 可以作为主设备或从设备使用，可以通过不同的演示程序使用。**如果您要使用以下 SoftwareSerial 程序，请参考上图中的连接方式。 TX-->D2, RX-->D3。**

打开 Arduino IDE，复制下面的程序并上传到 Arduino/Seeeduino 板上。然后两个 BLE 模块可以相互通信。

**Demo : BLE Slave**

```
    #include <SoftwareSerial.h>   //Software Serial Port
    #define RxD 2
    #define TxD 3

    #define DEBUG_ENABLED  1

    SoftwareSerial BLE(RxD,TxD);

    void setup()
    {
      Serial.begin(9600);
      pinMode(RxD, INPUT);
      pinMode(TxD, OUTPUT);
      setupBleConnection();

    }

    void loop()
    {
      char recvChar;
      while(1){
        if(BLE.available()){//check if there's any data sent from the remote BLE
          recvChar = BLE.read();
          Serial.print(recvChar);
        }
        if(Serial.available()){//check if there's any data sent from the local serial terminal, you can add the other applications here
          recvChar  = Serial.read();
          BLE.print(recvChar);
        }
      }
    }

    void setupBleConnection()
    {
      BLE.begin(9600); //Set BLE BaudRate to default baud rate 9600
      BLE.print("AT+CLEAR"); //clear all previous setting
      BLE.print("AT+ROLE0"); //set the bluetooth name as a slaver
      BLE.print("AT+SAVE1");  //don't save the connect information
    }
```

**Demo : BLE Master**

```
    #include <SoftwareSerial.h>   //Software Serial Port
    #define RxD 2
    #define TxD 3

    #define DEBUG_ENABLED  1

    SoftwareSerial BLE(RxD,TxD);

    void setup()
    {
      Serial.begin(9600);
      pinMode(RxD, INPUT);
      pinMode(TxD, OUTPUT);
      setupBleConnection();

    }

    void loop()
    {
      char recvChar;
      while(1){
        if(BLE.available()){//check if there's any data sent from the remote BLE
          recvChar = BLE.read();
          Serial.print(recvChar);
        }
        if(Serial.available()){//check if there's any data sent from the local serial terminal, you can add the other applications here
          recvChar  = Serial.read();
          BLE.print(recvChar);
        }
      }
    }

    void setupBleConnection()
    {
      BLE.begin(9600); //Set BLE BaudRate to default baud rate 9600
      BLE.print("AT+CLEAR"); //clear all previous setting
      BLE.print("AT+ROLE1"); //set the bluetooth name as a master
      BLE.print("AT+SAVE1");  //don't save the connect information
    }
```

## 资源下载
---------

- **[Eagle文件]** [Schematic](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/res/Grove-BLE_v1.0.zip)

- **[数据手册]** [Datasheet of BLE module](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/res/Bluetooth4_en.pdf)

- **[其他资源]** [BLE_apk_for_Android](https://raw.githubusercontent.com/SeeedDocument/Grove-BLE_v1/master/res/HMBLEComAssistant.rar)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_BLE_v1 -->
