---
title: Grove - Serial RF Pro
category: Communication
bzurl: https://www.seeedstudio.com/Grove-Serial-RF-Pro-p-794.html
oldwikiname:  Grove - Serial RF Pro
prodimagename: Twigrf.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Serial_RF_Pro
sku:  113020000
---
![](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/img/Twigrf.jpg)

Grove-Serial RF Pro 是一款低成本，高性能的透明 FSK 信号收发器，工作频率为 433/470/868/915 MHz，最佳性能频率为 433M （默认）。 它有一个 UART 接口，只需提供 UART，数据便可实现无线数据传输。 用户可灵活设置 UART 波特率，频率，输出功率，数据速率，频率偏差，接收带宽等参数。 这是设计无线数据传输产品的理想选择，可广泛应用于无线数据传输领域。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7fb7f81f6MBAyc&id=534770397920)
##  版本更新

<table>
<tr>
<th> 版本调整
</th>
<th> 版本描述
</th>
<th> 发布日期
</th></tr>
<tr>
<td width="300px"> v0.9b
</td>
<td width="500px"> 首次公开发行
</td>
<td width="200px"> NA
</td></tr></table>

##  产品特性
---
* Grove 兼容
* 高输出功率
* 小尺寸
* 更长的传输距离

##  创新应用
---
* 远程控制，远程测量系统
* 无线电表
* 访问控制
* 识别系统
* 数据采集
* IT 家用电器
* 婴儿监护系统

##  规格参数
---
<table  cellspacing="0" width="80%">
<tr>
<th scope="col"> 项目
</th>
<th scope="col"> 最小值
</th>
<th scope="col"> 标准值
</th>
<th scope="col"> 最大值
</th>
<th scope="col"> 单位
</th></tr>
<tr>
<td scope="row">工作电压
</td>
<td> 4.75
</td>
<td> 5.0
</td>
<td> 5.25
</td>
<td> VDC
</td></tr>
<tr>
<td scope="row"> 睡眠模式下的电流
</td>
<td colspan="3"> 1
</td>
<td> uA
</td></tr>
<tr>
<td scope="row"> 输出强度
</td>
<td> 1
</td>
<td> -
</td>
<td> 20
</td>
<td> dB
</td></tr>
<tr>
<td scope="row"> 通讯速度
</td>
<td> 1.2
</td>
<td>  -
</td>
<td> 115.2
</td>
<td> Kbps
</td></tr>
<tr>
<td scope="row"> 传输距离（最大）
</td>
<td colspan="3"> 1
</td>
<td> Km
</td></tr>
<tr>
<td scope="row"> 灵敏度
</td>
<td colspan="3"> -117
</td>
<td> dBm
</td></tr>
<tr>
<td scope="row">通信协议
</td>
<td colspan="3">  UART
</td>
<td> /
</td></tr>
<tr>
<td scope="row"> 工作温度
</td>
<td> -40
</td>
<td>  -
</td>
<td> +85
</td>
<td> ℃
</td></tr></table>

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/img/Serial_RF_Pro1.jpg)

<table >
<tr>
<th> 部件类型（5V逻辑电平）
</th>
<th> 部件描述
</th></tr>
<tr>
<td width="100px"> G(GND)
</td>
<td width="450px"> 接地端口
</td></tr>
<tr>
<td> EN(ENABLE)
</td>
<td> 设置正常模式为数据收发器（默认值为低: 10k 至 GND ）。
设置高电平时进入睡眠模式。
</td></tr>
<tr>
<td> CON(CONFIG)
</td>
<td> 设置低电平时是配置模式（连接到GND）。
设置高电平时是通讯模式（默认为高）。
</td></tr>
<tr>
<td> RX
</td>
<td> UART 数据输入
</td></tr>
<tr>
<td> TX
</td>
<td> UART 数据输出
</td></tr>
<tr>
<td> V(VCC)
</td>
<td>  5V（+）电源供电
</td></tr>
<tr>
<td> AT
</td>
<td> 接线引脚
</td></tr></table>

##  入门
---
在这里我们展示两个RF Pro Grove 单元相互发送/接收数据。 您需要两个 RF Pro Grove 单元和两个 Seeeduino 来进行演示。

*   将一个 Grove - Serial RF Pro 连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的 UART ，然后将 Grove - Base Shield 连接到 Seeeduino。

![](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/img/Rfdemo.jpg)

*   使用相同的方法将另一个Grove - Serial RF Pro 连接到 Seeeduino。

###  配置和查询方法

如果 ENABLE 引脚为低电平，则 CONFIG 引脚为低电平，模块将为配置状态。
如果红绿 LED 持续亮着，模块是将在 Config 中，然后你可以配置 &amp; 查询模块。

*   将 CON 引脚连接到 LOW / GND 进入配置模式。

*   发送命令修改并查询模块的配置。 配置 &amp; 查询说明参见[参考](http://wiki.seeed.cc/Grove-Serial_RF_Pro/#reference).

Config 指令格式为 AA + FA + [指令] + [参数]。 指令为 1 字节，参数为 0-4 字节的 HEX 数据（大字节排序，在低字节前的高字节）。

**注意:**

1) 请记住 UART 的传输速度（默认为 9600 ，最好不要更改），如果进行了一些更改，或者您将无法控制模块。 如果改变 UART 的传输速度，指令的传输速度将相应改变。 指令的传输速度范围为 1.2 Kbps - 115.2 Kbps。

2) LED功能说明：
- 当电源和模块正在工作时，红色和绿色 LED 将闪烁。
- 如果 EN（ENABLE） 引脚为低电平（默认为低电平），则 CON（Config） 引脚为低电平，模块将进入配置模式。 在配置模式下，红色和绿色 LED 都将亮起。 - 如果模块未处于配置模式，绿色和红色 LED 将不会亮起。
- 当模块发送数据时，红色 LED 闪烁，传输完成后红色 LED 将熄灭。
- 当模块正在等待接收数据时，绿色 LED 熄灭，当模块接收到数据时，绿色 LED 将闪烁一次。
</dd></dl>
</dd></dl>

###  通讯模式

将以下代码上传到 Seeeduino ，如果您不知道如何上传，请点击[这里](http://wiki.seeedstudio.com/wiki/Upload_Code)。

```
//send data routine

// link between the computer and the SoftSerial Shield
//at 9600 bps 8-N-1
//Computer is connected to Hardware UART
//SoftSerial Shield is connected to the Software UART:D2&D3

#include <SoftwareSerial.h>

SoftwareSerial SoftSerial(11, 10); // TX, RX
int buffer[64];
int count=0;
void setup()
{
    SoftSerial.begin(9600);               // the SoftSerial baud rate
    Serial.begin(9600);             // the Serial port of Arduino baud rate.

}

void loop()
{
    delay(1000);
    SoftSerial.write(0xAA);
    SoftSerial.write(0xFA);
    SoftSerial.write(0xE1);

    if (SoftSerial.available())              // if date is coming from software serial port ==> data is coming from SoftSerial shield
    {
        while(SoftSerial.available())          // reading data into char array
        {
            buffer[count++]=SoftSerial.read();     // writing data into array
            if(count == 64)break;
        }
        for (int i=0; i<count; i++) {
            Serial.print(buffer[i],HEX);            // if no data transmission ends, write buffer to hardware serial port
        }
        clearBufferArray();              // call clearBufferArray function to clear the stored data from the array
        count = 0;                       // set counter of while loop to zero
    }
    if (Serial.available())            // if data is available on hardware serial port ==> data is coming from PC or notebook
    SoftSerial.write(Serial.read());       // write it to the SoftSerial shield
    Serial.println("...");
}
void clearBufferArray()              // function to clear buffer array
{
    for (int i=0; i<count;i++)
    { buffer[i]=NULL;}                  // clear all index of array with command NULL
}
```

*   打开串行监视器后可以看到以下的界面。

![](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/img/Communication_result.jpg)

##  可供参考
---
下表列出了与串行 RF Pro v0.9b 进行交互的命令和响应情况。

<table>
<tr>
<th>指令（HEX）
</th>
<th>描述
</th>
<th>配置指令（HEX）
</th>
<th>响应
</th></tr>
<tr>
<td>F0
</td>
<td>重置为默认参数（ UART 传输速度除外），如下所示
</td>
<td width="400px">AA FA F0
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>E1
</td>
<td>读取当前的配置参数，如下所示
</td>
<td>AA FA E1
</td>
<td>16个字节：（ **按照下面的顺序** ）
<pre>working frequency-4 bytes,
wireless data rate-4 bytes,
receiving bandwidth-2 bytes,
frequency deviation-1 byte,
transmission power-1 byte,
UART transfer speed-4 bytes
</pre>
</td></tr>
<tr>
<td>D2
</td>
<td>设置工作频率，[参数] 4字节，[参数]单位：Hz。

设置范围：

*   HM-TRP-433: 414000000-454000000Hz;

*   HM-TRP-470: 450000000-490000000Hz;

*   HM-TRP-868: 849000000-889000000Hz;

*   HM-TRP-915: 895000000-935000000Hz
</td>
<td>示例:

*   配置指令：AA FA D2 **36 89 CA C0**，设置频率为 915000000Hz（**0x36 89 CA C0 = 915000000**）

*  配置指令：AA FA D2 **19 DE 50 80**，设置频率为 434000000Hz（**0x19 DE 50 80 = 434000000**）
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>C3
</td>
<td>设置无线数据速率，[参数] 4字节，[参数]单位：bps。

设置范围：1200-115200 bps

</td>
<td>示例:

*   配置指令：AA FA C3 **00 00 25 80**，设置传输速度为 9600bps（**0x00 00 25 80 = 9600**）

*   配置指令：AA FA C3 **00 00 96 00**，设置传输速度为 38400bps（**0x00 00 96 00 = 38400**）
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>B4
</td>
<td>设置接收带宽，[参数] 2字节，[参数]单位：KHz

设定范围：30-620KHz

</td>
<td>示例:

*   配置指令：AA FA B4 **00 69**，设置接收频带为 105KHz（**0x00 69 = 105**）

*   配置指令：AA FA B4 **01 2C**，设置接收频带为 300KHz（**0x01 2C = 300**）
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>A5
</td>
<td>设置频偏，[参数] 1字节，[参数]单位：KHz

设置范围：10-160KHz

</td>
<td>示例:

*   配置指令：AA FA A5 **23**，设置调制频率为 35KHz（**0x23 = 35**）

*   配置指令：AA FA A5 **32**，设置调制频率为 50KHz（**0x32 = 50**）
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>96
</td>
<td>设置发送功率，[参数] 1字节，0〜7级

设置范围：0-7级（1-20dBm）

</td>
<td>示例:

*   配置指令：AA FA 96 **07**，设置发射功率为7级（+20 dBm）

*   配置指令：AA FA 96 **03**，设置发射功率为3级（+8 dBm）
<pre>Transmission power level     Transmission power
7                                 +20dBm
6                                 +17dBm
5                                 +14dBm
4                                 +11dBm
3                                 +8dBm
2                                 +5dBm
1                                 +2dBm
0                                 +1dBm
</pre>
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>1E
</td>
<td>设置UART传输速度，[参数] 4字节，[参数]单位：bps

设置范围：1200-115200 bps

</td>
<td>示例:

*   配置指令：AA FA 1E **00 00 25 80**，设置速度为 9600bps（**0x00 00 25 80 = 9600**）

*   配置指令：AA FA 1E **00 00 96 00**，设置速度为 38400bps（**0x00 00 96 00 = 38400**）
</td>
<td>4F 4B 0D 0A （OK /r/n)
</td></tr>
<tr>
<td>87
</td>
<td>接收有用数据时的无线信号强度，无[参数]
</td>
<td>配置说明：AA FA 87

![](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/img/WirelesssignalstrengthRSSI.jpg)

</td>
<td>RSSI value is 8 bit, range: 0-255
</td></tr>
<tr>
<td>78
</td>
<td>无线信号强度，无[参数]

注意：

*   调制指数 : h = Fd/Rb, 范围： 0.5 ~ 32.

*   如果 h&gt;1, 则BW =Rb+2Fd; 如果 h&lt;1, 则BW =2Rb+ Fd.
</td>
<td>配置说明：AA FA 78
</td>
<td> RSSI 值为 8 位，范围：0-255
</td></tr></table>



##  资源下载

*   **[Code]** [Serial RF Pro Demo Code](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/res/Grove-Serial_RF_Pro_Demo_Code.zip)

*   **[Datasheet]** [HopeRF HM-TRP Series 100mW Transceiver modules V1.0 Datasheet](https://github.com/SeeedDocument/Grove-Serial_RF_Pro/raw/master/res/HM-TRP-RS232_enV1.0_20120604.pdf)
