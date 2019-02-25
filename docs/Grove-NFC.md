---
name: Grove - NFC
category: Communication
bzurl: https://seeedstudio.com/Grove-NFC-p-1804.html
oldwikiname: Grove_-_NFC
prodimagename: Grove-NFC_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-NFC
sku: 113020006
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/img/Grove-NFC_01.jpg">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/img/Grove-NFC_02.jpg">
        </td>
    </tr>
</table>

近场通信（NFC）是一套短距离无线技术。 它应用于日常生活中，如门禁系统和移动支付系统。Grove NFC 具有高度集成的收发器模块 PN532，能够处理 13.56MHz 的非接触式通信。 您可以使用此模块读取和写入 13.56MHz 标签，或使用两个 NFC 实现点对点数据交换。Grove NFC 设计为使用 I2C 或 UART 通信协议，UART 是默认模式。 此外，我们分配一个独立的 PCB 天线，可以轻松伸出您使用的任何外壳，为您设计外部设计项目预留更多空间。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.453ba1d4fAJNXX&id=527561799560)

## 规格参数
--------------

-   工作电压 : 3.3V
-   工作电流 :
    - 静态模式 : 73mA
    - 读写模式 : 83mA
-   支持主机接口 : I2C, UART( default )。
-   工作于 13.56MHz 的非接触式通信。
-   支持 ISO14443 A 类和 B 类协议。
-   用于检测 NFC 标签的最大操作距离为 28 毫米，其取决于当前的天线尺寸。
-   支持 P2P 通信。
-   外形尺寸: 25.43mm x 20.35mm。

!!!Tip
     关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

## 入门指导
-----------

1.  下载 [PN532 库文件](https://github.com/Seeed-Studio/PN532)，并将 4 个文件夹( PN532, PN532_SPI, PN532_I2C and PN532_HSU )放入 Arduino 的库中。
2.  下载 [NDEF 库](https://github.com/Seeed-Studio/Grove-NFC-libraries-Part), 将其放入 Arduino 的库中，并将其重命名为 NDEF。
3.  打开 Arduino IDE，如果 Arduino IDE 已经打开，请重启软件。
4.  在 Arduino IDE 中，点击菜单 : **File（文件） -> Example（示例） -> NDEF -> ReadTag**。
5.  我们在 NDEF 库中使用了 I2C 接口，因此请通过一把小刀切断 P1 和 UART 之间的连接，并将 P1 和 I2C 焊接在一起。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/img/NFC_cutAndsolder.jpg)

<div class="admonition caution">
<p class="admonition-title">Caution</p>
Grove - NFC v1.0 的调试 ：在使用 I2C 通信时有一个错误，请使用跳线来跟踪这些连接
</div>

| Arduino/Arduino Mega | Grove - NFC |
|----------------------|-------------|
| SCL                  | RX          |
| SDA                  | TX          |
| GND                  | GND         |
| 5V                   | VCC         |

您仍然可以在不断开任何连接的情况下使用 UART 接口，Seeeduino Mega( Arduino Mega ) 或 Seeeduino lite( Arduino Leonardo )是首选。 以下是修改后的程序。

```
#include "PN532_HSU.h"
#include "PN532.h"
#include "NfcAdapter.h"
 
PN532_HSU interface(Serial1);
NfcAdapter nfc = NfcAdapter(interface);
 
void setup(void) {
    Serial.begin(115200);
    Serial.println("NDEF Reader");
    nfc.begin();
}
 
void loop(void) {
    Serial.println("\nScan a NFC tag\n");
    if (nfc.tagPresent())
    {
        NfcTag tag = nfc.read();
        tag.print();
    }
    delay(5000);
}
```

<div class="admonition note">
<p class="admonition-title">Note</p>
如果和 Seeeduino 或 Arduino UNO 一起使用它，获取返回消息的唯一方法是将其设置为 I<sup>2</sup>C 接口总线。在和 Mega 或 Leonardo 一起使用它时，可以使用 UART 接口总线。 确保为 Arduino 库下载了 PN532 库和 Don's NDEF 库。 您可以在文件夹 <span style="font-weight:bold">example</span> 下测试示例 <span style="font-weight:bold">ReadTag.ino</span>。删除第1行到第10行（行  <span style="font-weight:bold">\#else ......</span> 和上面的行到顶部）。
</div>

切断以下连接 :

-   TP1 to UART
-   TP2 to RX
-   TP3 to TX

焊接以下连接 :

-   TP1 to I2C
-   TP2 to SCL
-   TP3 to SDA

## 资源下载
--------

- **[Eagle文件]** [Grove - NFC v1.0 EAGLE (schematic and board) files](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/res/Grove-NFC.zip)
- **[Eagle文件]** [Grove - NFC v1.1 EAGLE (schematic and board) files](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/res/Grove-NFC_v1.1.zip)
- **[芯片数据手册]** [PN532 Datasheet PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC/master/res/PN532.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_NFC -->
