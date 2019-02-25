---
name: Grove - 125KHz RFID Reader
category: Communication
bzurl: https://seeedstudio.com/Grove-125KHz-RFID-Reader-p-1008.html
oldwikiname: Grove_-_125KHz_RFID_Reader
prodimagename: Grove-125KHz_RFID_Reader.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-125KHz_RFID_Reader
sku: 113020002
tags: grove_digital, io_5v, plat_duino, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-125KHz_RFID_Reader/master/img/Grove-125KHz_RFID_Reader.jpg)

Grove-125KHz RFID Reader 是一个用于读取 uem4100 RFID 卡信息的模块，它具有两种输出格式：Uart 和 Wiegand。它具有最大 7cm 感应距离的灵敏度。

下面的模块和 RFID reader 配合使用 :

-   [RFID tag combo (125khz)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.20f4ea6G5RBQG&id=45673403608&ns=1&abbucket=1#detail)

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.16.51654862Yh5Xft&id=45783832978&ns=1&abbucket=1#detail)

## 规格参数
--------------

-   电压 : 4.75-5.25V
-   工作频率 : 125 KHz
-   最大感应距离 : 70mm
-   TTL输出 : 波特率为 9600，8 个数据位，1 个停止位，无校验位
-   Wiegand 输出 : 26位 Wiegand 格式，1 个偶校验位，24 个数据位和 1 个奇校验位

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

## 操作示例
-------------

在这里，我们展示了如何使用 Grove - 125KHz RFID Reader 读取 RFID 信息。将 Grove - 125KHz RFID Reader 连接到 Grove - Base Shield 的 UART。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-125KHz_RFID_Reader/master/img/RFID_reader.jpg)

### Uart 模式

您需要选择跳线至 "U" 进入该模式，设置为 : 9600 bps，N，8，1，TTL 输出

```c
/*
  link between the computer and the SoftSerial Shield
  at 9600 bps 8-N-1
  Computer is connected to Hardware UART
  SoftSerial Shield is connected to the Software UART:D2&D3
*/
 
#include <SoftwareSerial.h>
 
SoftwareSerial SoftSerial(2, 3);
unsigned char buffer[64];       // buffer array for data receive over serial port
int count = 0;                    // counter for buffer array
 
void setup()
{
    SoftSerial.begin(9600);     // the SoftSerial baud rate
    Serial.begin(9600);         // the Serial port of Arduino baud rate.
}
 
void loop()
{
    // if date is coming from software serial port ==> data is coming from SoftSerial shield
    if (SoftSerial.available())              
    {
        while(SoftSerial.available())               // reading data into char array
        {
            buffer[count++] = SoftSerial.read();      // writing data into array
            if(count == 64)break;
        }
        Serial.write(buffer, count);     // if no data transmission ends, write buffer to hardware serial port
        clearBufferArray();             // call clearBufferArray function to clear the stored data from the array
        count = 0;                      // set counter of while loop to zero
    }
    if (Serial.available())             // if data is available on hardware serial port ==> data is coming from PC or notebook
    SoftSerial.write(Serial.read());    // write it to the SoftSerial shield
}
void clearBufferArray()                 // function to clear buffer array
{
    // clear all index of array with command NULL
    for (int i=0; i<count; i++)
    {
        buffer[i]=NULL;
    }                  
}
```

打开串口监视器，读取的信息显示如下 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-125KHz_RFID_Reader/master/img/Read_Data_.jpg)

### Wiegand 模式

您需要选择跳线至 "W" 才能进入此模式。Seeeduino 的 [Wiegand demo code](https://raw.githubusercontent.com/SeeedDocument/Grove-125KHz_RFID_Reader/master/res/RFID_Wiegand_INT.zip) 在中断模式下读取 Wiegand 数据。

在 Wiegand 模式下，输出数据格式为 26 位，包括 24 位卡信息和 2 位奇偶校验。

<table border="1">
<tr style="font-weight:bold">
<td width="20">
bit
</td>
<td width="20">
0
</td>
<td width="20">
1
</td>
<td width="20">
2
</td>
<td width="20">
3
</td>
<td width="20">
4
</td>
<td width="20">
5
</td>
<td width="20">
6
</td>
<td width="20">
7
</td>
<td width="20">
8
</td>
<td width="20">
9
</td>
<td width="20">
10
</td>
<td width="20">
11
</td>
<td width="20">
12
</td>
<td width="20">
13
</td>
<td width="20">
14
</td>
<td width="20">
15
</td>
<td width="20">
16
</td>
<td width="20">
17
</td>
<td width="20">
18
</td>
<td width="20">
19
</td>
<td width="20">
20
</td>
<td width="20">
21
</td>
<td width="20">
22
</td>
<td width="20">
23
</td>
<td width="20">
24
</td>
<td width="20">
25
</td>
</tr>
<tr style="font-size: 90%" align="center">
<td>
-
</td>
<td>
PE
</td>
<td colspan="24" rowspan="1">
D
</td>
<td>
P0
</td>
</tr>
<tr style="font-size: 90%" align="center">
<td>
-
</td>
<td>
-
</td>
<td colspan="12" rowspan="1">
E
</td>
<td colspan="12" rowspan="1">
0
</td>
<td>
-
</td>
</tr>
<tr style="font-size: 90%" align="center">
<td>
-
</td>
<td>
-
</td>
<td colspan="8" rowspan="1">
D2[7..0]
</td>
<td colspan="8" rowspan="1">
D1[7..0]
</td>
<td colspan="8" rowspan="1">
D0[7..0]
</td>
<td>
-
</td>
</tr>
</table>
-   PE 是偶数位，PO 是奇数位;
-   E 是涉及偶数的数据位，O 是涉及奇数的数据位；
-   DX\[7..0\] 是对应 Mifare@ Standard & Light 卡只读 ID 的数据位;

### 如何将输出转换为卡号

以 ID: 0009776930 为例:

-   卡号 ID : 0009776930 ------- 十进制 [开始位 (00) + 卡号 (8 位数字)]
-   输出 : 0700952F229F ------------- 十六进制 [[开始位 (07h) + 卡号 (8 位数字) + 校验位]
-   十进制和十六进制的计算器都是可获得的。

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_125KHz_RFID_Reader -->
