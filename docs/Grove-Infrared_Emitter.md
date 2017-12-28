---
title: Grove - Infrared Emitter
category: Actuator
bzurl: https://seeedstudio.com/Grove-Infrared-Emitter-p-993.html
oldwikiname: Grove_-_Infrared_Emitter
prodimagename: Grove-Infrared_Emitter.jpg
wikiurl: http://seeed.wiki/Grove-Infrared_Emitter
sku: 101020026
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Emitter/master/img/Grove-Infrared_Emitter.jpg)

Grove - Infrared Emitter 用于通过红外 LED 传输红外信号，而在另一侧有 **红外接收器** 用于获取信号。红外 LED 就像任何其他 LED 一样，它的波长 940nm。我们不仅可以使用发射器来传输数据或命令，而且还可以使用 Arduino 模拟遥控控制您的家用电器。红外发射器可以传输 10 米有效的信号。超过 10 米，接收器可能无法获得信号。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.46cb5251lwWLv9&id=45555269740)


## 规格参数
-------------

-   电压 : 3.3-5V
-   信号有效距离 : 10m

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported
-------------------

## 操作示例
-------------

The Grove - Infrared Emitter 发送数据 Grove - Infrared Receiver 接受数据。

-   将 Grove - Infrared Emitter 连接到 **D3**。
-   将 Grove - Infrared Receiver 连接到 **D2**。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Emitter/master/img/IR_SendRev.jpg)

与 Arduino/Seeeduino 一起使用
----------------------

### 参考资料

- [下载 Arduino 和安装 Arduino 驱动](/Download_Arduino_and_install_Arduino_driver)

- [Seeeduino/Arduino 入门指导](/Getting_Started_with_Seeeduino)

### IRSendRev 库

我们已经创建了一个库以帮助您快速开始使用 Seeeduino/Arduino，在这个部分中，我们将向您展示如何配置这个库。

#### 配置库

1.  从 IRSendRev github 页面下载 [library code as a zip file](https://github.com/Seeed-Studio/IRSendRev)
2.  解压文件至 **…/arduino/libraries**
3.  重命名解压文件夹为 "IRSendRev"
4.  打开 Arduino IDE

### Grove - Infrared Emitter  示例/应用

这些例子将告诉你如何使用 Grove - Infrared Emitter 的功能。 您可以将 Grove - Infrared Emitter 与 Grove - Infrared Receiver 组合使用。将 IR 发送引脚连接到 **D3** 进行演示。

#### 接收

<div class="admonition note">
<p class="admonition-title">Note</p>
您需要一个 <span style="font-weight:bold">Grove - Infrared Receiver</span>.。并通过它上传这个演示到主板。
</div>

-   打开 **File(文件)->Examples(示例)->IRSendRev->example->recv** 查看完整示例, 或者将以下代码复制并粘贴到新的 Arduino 草图。

**说明** :
这个例子将 IR 接收器引脚连接到 **D2**。您可以看到通过串口终端接收到的遥控器的红外数据，然后将接收到的红外数据写入 send.ino，并通过 Grove - Infrared Emitter 上传到电路板上，这样就可以用遥控器的按钮发送相同的数据。

**应用** :
您可以通过 Grove - Infrared Receiver 记录下遥控器的红外数据，然后在某些情况下通过 Grove - Infrared Emitter 发送相同的数据，例如室内温度大于 26 度时打开风扇开关。

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

-   将代码上传到开发板。
-   打开串口监视器窗口并等待输入。
-   使用红外遥控器发送数据<font color="Blue">(本例使用 MIDEA 公司的风扇红外遥控器，按开/关键)</font>。
-   可以看到如下的数据

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Emitter/master/img/Data：IR_remote_control_of_fans.jpg)

#### 发送

-   打开 **File(文件)->Examples(示例)->IRSendRev->example->send** 查看完整示例, 或者将以下代码复制并粘贴到新的 Arduino 编程页面。

**说明**:
  将 IR 发送引脚连接到 **D3** 进行演示。您可以看到通过 Grove - Infrared Receiver 接收到的遥控器的红外数据，例如上面的例子。然后将接收到的红外数据写入本例，并通过 Grove - Infrared Emitter 上传到电路板上，这样就可以用遥控器的按钮发送相同的数据。

**应用**:
您可以通过 Grove - Infrared Receiver 记录下遥控器的红外数据，然后在某些情况下通过 Grove - Infrared Emitter 发送相同的数据，例如室内温度大于 26 度时打开风扇开关。

<div class="admonition note">
<p class="admonition-title">Note</p>
本演示中，您必须将 IR 发送引脚连接到 **D3**。
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

## 资源下载
---------

-   **[Eagle文件]** [Grove-Infrared Emitter eagle files](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Emitter/master/res/Grove-Infrared_Emitter_eagle_files.zip)
-   **[库文件]** [IR Send and Receiver Library](https://github.com/Seeed-Studio/IRSendRev)
-   **[芯片数据手册]** [TSAL6200 Datasheet](http://www.vishay.com/docs/81010/tsal6200.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Infrared_Emitter -->
