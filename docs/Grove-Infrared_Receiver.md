---
title: Grove - Infrared Receiver
category: Sensor
bzurl: https://seeedstudio.com/Grove-Infrared-Receiver-p-994.html
oldwikiname: Grove_-_Infrared_Receiver
prodimagename: Grove-Infrared_Receiver.jpg
wikiurl: http://seeed.wiki/Grove-Infrared_Receiver
sku: 101020016
tags: grove_digital, io_3v3, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Receiver/master/img/Grove-Infrared_Receiver.jpg)

 Infrared Receiver 用于接收红外信号，也可用于远程控制检测。 Infrared Receiver 上有一个 IR 探测器，用于获得红外发射器发出的红外线。 IR 检测器内部有一个解调器，寻找 38 KHz的信号。 Infrared Receiver可以在10米以内接收信号。 如果超过10米，接收器可能无法得到信号。 我们经常使用两个 Groves-Infrared Receiver 和 [Grove - Infrared Emitter](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.7bdebac47XPzLS&id=45477043694) 来一起工作。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.7bdebac47XPzLS&id=45477043694)

产品特性
-------------

-   工作电压: 3.3-5V
-   接收距离: 10m

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

Platforms Supported
-------------------

示例
-------------

我们将在本示例中使用 Grove-Infrared Receiver 和 Grove - Infrared Emitter。 Infrared Receiver将收到  Grove - Infrared Emitter 发送的数据。


- 将 Grove - Infrared Emitter 连接到 **D3**。
- 将 Grove - Infrared Emitter 连接到 **D2**。

使用 Arduino/Seeeduino
----------------------

### 推荐阅读入门

- [Arduino入门](http://seeed.wiki/Getting_Started_with_Seeeduino/)

- 如果您不清楚怎么下载代码到您的板子里，请点击[这里](http://seeed.wiki/Upload_Code/)。

### IRSendRev 库

我们创建了一个库，以帮助您快速开始使用 Seeeduino / Arduino，本节将介绍如何设置库。

#### 设置

1. 从 IRSendRev github 页面上下载 [库文件压缩包](https://github.com/Seeed-Studio/IRSendRev) 。
2.  将下载的文件解压缩到... / arduino / libraries 中。
3.  解压文件夹并命名为 “IRSendRev”
4.  启动 Arduino IDE（如果已经打开，请重新启动）。

### Infrared Receiver的示例/应用

这些例子将向您展示如何使用 Grove - Infrared Receiver 的功能。 您可以使用 Infrared Receiver 与 Grove - Infrared Emitter 组合使用。 将 **IR发射**  引脚连接到 **D2** 进行演示。

#### 接收器

-   打开File（文件） - >Examples（示例） - > IRSendRev-> example-> recv 查看完整的示例程序，或将代码复制并粘贴到新的 Arduino 编辑页面上。

**描述**:
此示例将 **IR接收器** 引脚连接到 **D2**。 您可以通过串口监视器看到遥控器的红外数据，然后将接收到的红外数据写入 send.ino，并使用 Infrared Emitter 上传到电路板，以便您可以使用遥控器发送相同的数据。

**创意应用**:
您可以通过 Infrared Receiver 知道遥控器发送的红外数据，然后在某些情况下通过 Infrared Emitter 发送相同的数据，例如室内温度大于26度时打开风扇开关。

```
#include <IRSendRev.h>
 
#define BIT_LEN         0
#define BIT_START_H     1
#define BIT_START_L     2
#define BIT_DATA_H      3
#define BIT_DATA_L      4
#define BIT_DATA_LEN    5
#define BIT_DATA        6
 
const int pinRecv = 2;              // ir receiver connect to D2
 
void setup()
{
    Serial.begin(115200);
    IR.Init(pinRecv);
    Serial.println("init over");
}
 
unsigned char dta[20];
 
void loop()
{
    if(IR.IsDta())                  // get IR data
    {
        IR.Recv(dta);               // receive data to dta
 
        Serial.println("+------------------------------------------------------+");
        Serial.print("LEN = ");
        Serial.println(dta[BIT_LEN]);
        Serial.print("START_H: ");
        Serial.print(dta[BIT_START_H]);
        Serial.print("\tSTART_L: ");
        Serial.println(dta[BIT_START_L]);
 
        Serial.print("DATA_H: ");
        Serial.print(dta[BIT_DATA_H]);
        Serial.print("\tDATA_L: ");
        Serial.println(dta[BIT_DATA_L]);
 
        Serial.print("\r\nDATA_LEN = ");
        Serial.println(dta[BIT_DATA_LEN]);
 
        Serial.print("DATA: ");
        for(int i=0; i<dta[BIT_DATA_LEN]; i++)
        {
            Serial.print("0x");
            Serial.print(dta[i+BIT_DATA], HEX);
            Serial.print("\t");
        }
        Serial.println();
 
        Serial.print("DATA: ");
        for(int i=0; i<dta[BIT_DATA_LEN]; i++)
        {
            Serial.print(dta[i+BIT_DATA], DEC);
            Serial.print("\t");
        }
        Serial.println();
        Serial.println("+------------------------------------------------------+\r\n\r\n");
    }
}
```


- 将代码上传到开发板。
- 打开串行监视器，等待数据输入。
- 使用红外遥控发送数据<font color="Blue">（此示例使用 MIDEA 公司的红外遥控器的风扇，然后按开/关键）</font>。
- 您可以看到以下信息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Receiver/master/img/Data：IR_remote_control_of_fans.jpg)

#### 发射器

-   打开 **File（文件） - >Examples（示例） - > IRSendRev-> example** 打开示例程序，或将代码复制并粘贴到新的 Arduino 编辑页面上。

**描述**:
在这个演示中我们将 **IR发射** 引脚连接到 **D3** 端口。 您可以看到通过 Infrared Receiver 接收到的遥控器的红外数据，如上述示例。 然后将接收到的红外数据写入此示例，并使用 Infrared Emitter 上传到电路板，这样你就可以使用遥控器发送出相同的数据。



<div class="admonition note">
<p class="admonition-title">Note</p>
此演示必须将 **IR发射** 引脚连接到 **D3** 端口。
</div>


```
#include <IRSendRev.h>
 
#define BIT_LEN         0
#define BIT_START_H     1
#define BIT_START_L     2
#define BIT_DATA_H      3
#define BIT_DATA_L      4
#define BIT_DATA_LEN    5
#define BIT_DATA        6
 
const int ir_freq = 38;                 // 38k
 
unsigned char dtaSend[20];
 
void dtaInit()
{
    dtaSend[BIT_LEN]        = 11;          // all data that needs to be sent
    dtaSend[BIT_START_H]    = 180;         // the logic high duration of "Start"
    dtaSend[BIT_START_L]    = 91;          // the logic low duration of "Start"
    dtaSend[BIT_DATA_H]     = 11;          // the logic "long" duration in the communication
    dtaSend[BIT_DATA_L]     = 33;          // the logic "short" duration in the communication
 
    dtaSend[BIT_DATA_LEN]   = 6;           // Number of data which will sent. If the number is other, you should increase or reduce dtaSend[BIT_DATA+x].
 
    dtaSend[BIT_DATA+0]     = 128;           // data that will sent
    dtaSend[BIT_DATA+1]     = 127;
    dtaSend[BIT_DATA+2]     = 192;
    dtaSend[BIT_DATA+3]     = 63;
    dtaSend[BIT_DATA+4]     = 192;
    dtaSend[BIT_DATA+5]     = 63;
}
 
void setup()
{
    dtaInit();
}
 
void loop()
{
    IR.Send(dtaSend, 38);
 
    delay(2000);
}
```

资源下载
---------

-   [Grove - Infrared Receiver eagle files](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Receiver/master/res/Grove-Infrared_Receiver_eagle_files.zip)
-   [IR Send and Receiver Library](https://github.com/Seeed-Studio/IRSendRev)
-   [IR Receive Library for LinkIt ONE](https://github.com/Seeed-Studio/IR_Recv_LinkIt_ONE)
-   [TSOP282 Datasheet](http://www.vishay.com/docs/82491/tsop382.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Infrared_Receiver -->
