---
name: RS232 Shield
category: Shield
bzurl: https://seeedstudio.com/RS232-Shield-p-1910.html
oldwikiname: RS232_Shield
prodimagename: RS232_Shield_Photo.jpg
wikiurl: http://wiki.seeedstudio.com/cn/RS232_Shield
sku: 113030016
---

![](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/img/RS232_Shield_Photo.jpg)

RS232 Shield 是工业设备的标准通信端口。该模块基于 MAX232，它是一个双路驱动器/接收器，它包含一个电容式电压发生器，用于从单个 5V 电源提供 TIA/EIA-232-F 电压。该扩展板集成了 DB9 连接器(内孔的)，提供连接到各种设备的 RS232 接口。此外，RS232 接头将有助于您的连接和调试。它提供了焊接区域，充分利用扩展板上的额外空间，这对于原型制作来说非常方便。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.1.6bd29b76wvYGJS&id=45509558795&ns=1&abbucket=1#detail)

## 规格参数
-------------

-   符合 TIA/EIA-232-F 和 ITU
-   速度高达 120 kbit/s
-   电源电流低
-   LED 指示灯
-   DB9 连接器(内孔的)
-   提供焊接区域

## 兼容性
-------
我们已经生产了大量扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里使用表格来说明扩展板和平台板之间的兼容性。

!!!note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。 如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc 联系。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 接口功能
------------------

**使用方法**

首先可以通过电脑来测试。

### 硬件安装

1. 需要 : Seeeduino，Mini usb Cable，RS232 Shield，和 RS232 to USB Cable.
2. 建立如下连接 : 跳线帽可用于从数字引脚选择软件串行端口。您可以将它们设置为 D7(232\_TX) 和 D6(232\_RX)，并将代码修改为 "*SoftwareSerial mySerial(7, 6); // 232\_TX, 232\_RX*"

![](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/img/RS232_Shield_usage.jpg)

### 软件部分

-   1) 打开 Arduino IDE，粘贴下面的代码 :

```
 
#include <SoftwareSerial.h>
 
SoftwareSerial mySerial(7, 6); //232_TX,232_RX
 
void setup()
{
    // Open serial communications and wait for port to open:
    Serial.begin(9600);
    while (!Serial) {
        ; // wait for serial port to connect. Needed for Leonardo only
    }
 
 
    Serial.println("Goodnight moon!");
 
    // set the data rate for the SoftwareSerial port
    mySerial.begin(9600);
    mySerial.println("Hello, world?");
}
 
void loop() // run over and over
{
    if (mySerial.available())
    Serial.write(mySerial.read());
    if (Serial.available())
    mySerial.write(Serial.read());
}
```

-   2) 上传代码。请注意您应该选择正确的主板类型和 COM 端口。
-   3) 打开串口监视器。

结果如下 :
![](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/img/RS232_Shield_usage1.jpg)

## 资源下载
--------

-   **[Eagle文件]** [RS232 Shield eagle file](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/res/RS232_Shield_v1.0_Eagle.zip)
-   **[原理图 PDF]** [RS232\_Shield\_v1.0.pdf](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/res/RS232_Shield_v1.pdf)
-   **[芯片数据手册]** [Datasheet MAX232D.pdf](https://raw.githubusercontent.com/SeeedDocument/RS232_Shield/master/res/MAX232D.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/RS232_Shield -->
