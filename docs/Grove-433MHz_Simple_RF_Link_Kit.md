---
title: Grove - 433MHz Simple RF Link Kit
category: Communication
bzurl: https://seeedstudio.com/Grove-433MHz-Simple-RF-link-kit-p-1062.html
oldwikiname: Grove_-_433MHz_Simple_RF_Link_Kit
prodimagename: 433MHz_Simple_RF.jpg
wikiurl: http://seeed.wiki/Grove-433MHz_Simple_RF_Link_Kit
sku: 113060000
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/img/433MHz_Simple_RF.jpg)

该套件用于频率为433MHz的单向无线通信，包括发射器模块和接收器模块。 该套件的配置模式允许在室内约40米的传输距离，或在室外约100米。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=686.1000925.0.0.44913df4Rd7HtS&id=520923022498)

版本更迭
---------------

| 版本 | 描述           | 发售日期     |
|----------|------------------------|-------------|
| v0.9b    | 初始版本 | 03,11月,2011 |

产品特性
--------

-   Grove 兼容接口
-   使用 ASK (Amplitude Shift Keying幅移键控) 模式.
-   单向通信

!!!Tip
    更多关系Grove的细节请参考 [Grove 系统](http://seeed.wiki/Grove_System/)

规格参数
-------------

### 发射模块

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
3.0
</td>
<td>
5.0
</td>
<td>
12.0
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
工作电流
</th>
<td>
3
</td>
<td>
/
</td>
<td>
10
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
工作模式
</th>
<td colspan="3">
ASK
</td>
<td>
/
</td>
</tr>
<tr align="center">
<th scope="row">
发射功率(Max)
</th>
<td colspan="3">
15
</td>
<td>
mW
</td>
</tr>
<tr align="center">
<th scope="row">
工作距离
</th>
<td>
40
</td>
<td>
/
</td>
<td>
100
</td>
<td>
m
</td>
</tr>
</table>

### 接收模块

| 项目                | 典型值 | 单位 |
|----------------------|---------|------|
| 工作电压     | 5       | V  |
| 静态电流    | 5       | mA   |
| 接收灵敏度 | -105    | dBm  |
| 工作频率  | 433.92  | MHz  |

创意应用
-----------------

-   远程控制
-   远程自动化
-   警报系统

使用说明
-----

发射器和接收器模块都依靠单根导线进行通信。 尽管使用Arduino平台提供的UART可以工作，但是建议使用VirtualWire库，它使用幅移键控进行调制，从而提供更好的通信。

发射器和接收器模块都需要三根导线：Vcc，接地和信号。套件两部分的引脚2都未连接未使用。

-   将发射模块连接到与发射Aduino相连的 [Grove-Base Shield V2](https://www.seeedstudio.com/Base-Shield-V2-p-1378.html) 的数字 I/O 口 **D2**

-   将接收模块连接到与接收Aduino相连的 [Grove-Base Shield V2](https://www.seeedstudio.com/Base-Shield-V2-p-1378.html) 的数字 I/O 口 **D2**

-   下载 [VirtualWire 库](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/res/VirtualWire_Library.zip) 解压库文件到 Arduino IDE 的下列目录: **..\\arduino-1.0\\libraries**. 请参考 [这里](http://www.pjrc.com/teensy/td_libs_VirtualWire.html).
-   为发射模块上传下面的代码:

```
    #include <VirtualWire.h>

    //Grove - 315(433) RF link kit Demo v1.0
    //by :http://www.seeedstudio.com/
    //connect the sent module to D2 to use  
    #include <VirtualWire.h>

    int RF_TX_PIN = 2;

    void setup()
    {
      vw_set_tx_pin(RF_TX_PIN); // Setup transmit pin
      vw_setup(2000); // Transmission speed in bits per second.
    }

    void loop()
    {
      const char *msg = "hello";
      vw_send((uint8_t *)msg, strlen(msg));  // Send 'hello' every 400ms.
      delay(400);

    }
```

-   为接收模块上传下列代码:

```
    //Grove - 315(433) RF link kit Demo v1.0
    //by :http://www.seeedstudio.com/
    //connect the receive module to D2 to use ..
    #include <VirtualWire.h>

    int RF_RX_PIN = 2;

    void setup()
    {
      Serial.begin(9600);
      Serial.println("setup");
      vw_set_rx_pin(RF_RX_PIN);  // Setup receive pin.
      vw_setup(2000); // Transmission speed in bits per second.
      vw_rx_start(); // Start the PLL receiver.
    }

    void loop()
    {
      uint8_t buf[VW_MAX_MESSAGE_LEN];
      uint8_t buflen = VW_MAX_MESSAGE_LEN;
      if(vw_get_message(buf, &buflen)) // non-blocking I/O
      {
        int i;
        // Message with a good checksum received, dump HEX
        Serial.print("Got: ");
        for(i = 0; i < buflen; ++i)
        {
          Serial.print(buf[i], HEX);
          Serial.print(" ");
          //Serial.print(buf[i]);
        }
        Serial.println("");
      }
    }
```        

-   打开接收模块的串口监视器您将看到以下结果。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/img/Receive_Data.jpg)

这只是一个简单的发射和接收例程仅供参考。

资源下载
---------

-   **[库文件下载]**[VirtualWire Library.zip](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/res/VirtualWire_Library.zip)
-   **[例程]**[433MHz\_demo.zip](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/res/315MHz_Demo.zip)
-   **[其他资料]**[VirtualWire Documentation](http://www.open.com.au/mikem/arduino/VirtualWire.pdf)
-   **[数据手册]**[TI:LM358PSR](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/res/1110010P1.pdf)
-   **[数据手册]**[R433A Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-433MHz_Simple_RF_Link_Kit/master/res/ADI;ACTR433A.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_433MHz_Simple_RF_Link_Kit -->
