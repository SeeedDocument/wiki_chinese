---
name: Grove - NFC Tag
category: Communication
bzurl: https://seeedstudio.com/Grove-NFC-Tag-p-1866.html
oldwikiname: Grove_-_NFC_Tag
prodimagename: Grove-NFC_Tag_uasge.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-NFC_Tag
sku: 101020070
tags: grove_i2c, io_3v3, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/Grove-NFC_Tag_uasge.jpg)

Grove-NFC Tag 是一款高度集成的近场通信 Tag 模块，该模块为 I2C 接口，基于 M24LR64E-R，M24LR64E-R 具有64位标识符和 64-Kbit EEPROM 。Grove–NFC Tag 附带一个独立的 PCB 天线，可以轻松地伸出您使用的任何外壳，留下更多空间来设计项目的外观。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.77079bceszXft5&id=520796740901)

## 规格参数
=============

-   工作电压 :5V 或 3V3
-   工作电流:&lt;1mA
-   2cm最大有效范围
-   13.56MHz的非接触式通信
-   兼容ISO 15693 和 ISO 18000-3 Model1
-   64 位唯一标识符（UID）
-   读块和写（32-bit blocks）
-   Grove I2C 接口

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

## 操作示例
=====

### 从手机读/写
--------------------

1.  下载并安装 [NfcV-reader for Android](https://github.com/Seeed-Studio/NFC_Tag_M24LR6E/blob/master/Resources/NfcVreader.apk)
2.  我们可以通过手机对它实现读和写

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/NFC_Tag_1.png)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/NFC_Tag_2.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/NFC_Tag_3.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/NFC_Tag_4.png)

控制 LED
-----------

### 硬件安装

![](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/img/Grove-NFC_Tag_Photo.jpg)

1.  下载并安装 [NfcV-reader for Android](https://github.com/Seeed-Studio/NFC_Tag_M24LR6E/blob/master/Resources/NfcVreader.apk)
2.  下载 [NFC Tag Lib](https://github.com/Seeed-Studio/NFC_Tag_M24LR6E), 将其重命名为  NFC_Tag_M24LR6E 并把它放入 Arduino 的库里 .
3.  打开 Arduino IDE 软件. 如果 Arduino IDE 已经打开, 关闭并重新打开它.
4.  在 Arduino IDE 软件中, 点击下拉菜单 :**File(文件) -> Example(示例) -> NFC_Tag_M24LR6E -> ledControl**
5.  现在您就可以通过手机控制 LED 灯了.

```
 
#include "NfcTag.h"
#include <Wire.h>
 
NfcTag nfcTag;
int led = 5;
bool flag = false;
bool preFlag = false;
void setup(){
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  nfcTag.init();
}
 
void loop(){
  flag = nfcTag.readByte(EEPROM_I2C_LENGTH-1) == 0xff?true:false;
  if(flag != preFlag){
    Serial.println("get remote NFC control signal!");
    if(flag == true){
      Serial.println("led will light up!");
      digitalWrite(led,HIGH);
    }else{
      Serial.println("led will turn dark!");
      digitalWrite(led,LOW);
    }
    preFlag = flag;
  }
  delay(5*1000);
}
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/res/Grove-NFC_Tag_v1.0.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
--------

-  **[原理图PDF]**  [Grove - NFC Tag.PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/res/Grove-NFC_Tag_v1.0.pdf)
-   **[Eagle文件]** [Grove - NFC Tag Eagle file](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/res/Grove-NFC_Tag_v1.0.zip)
-   **[库文件]** [NFC Tag M24LR6E Lib](https://github.com/Seeed-Studio/NFC_Tag_M24LR6E)
-   **[芯片数据手册]** [M24LR64E-R datasheet.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-NFC_Tag/master/res/M24LR64E-R.pdf)
-   **[其他资源]** [NfcV-reader for Android](https://github.com/Seeed-Studio/NFC_Tag_M24LR6E/blob/master/Resources/NfcVreader.apk)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_NFC_Tag -->
