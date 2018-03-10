---
title: NFC Shield V2.0
category: Shield
bzurl: https://seeedstudio.com/NFC-Shield-V2.0-p-1370.html
oldwikiname: NFC_Shield_V2.0
prodimagename: NFC_front.png
wikiurl: http://wiki.seeedstudio.com/cn/NFC_Shield_V2_0
sku: 113030001
---

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/NFC_front.png">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/NFC_back.png">
        </td>
    </tr>
</table>

NFC (近场通信)是一种被广泛使用的技术。NFC 技术的应用包括无线访问控制系统(例如，无钥匙门锁)和移动设备支付(例如，通过电话应用程序接收支付信息的存储寄存器)。

NFC Shield 采用的收发器模块是 PN532，该模块可在 13.56MHz 处理无线通信，这意味着您可以使用此扩展板来读写 13.56MHz 的标签，或者在扩展板和智能手机之间实现点对点 (P2P) 数据交换。

对于这个新版本的扩展板，我们划分了一个独立的 PCB 天线区，使您能够轻松地在主电路外延长 NFC 接口。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=45703455300&qq-pf-to=pcqq.c2c)

## 兼容性

我们已经生产了大量扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里使用表格来说明扩展板和平台板之间的兼容性。

!!!note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc 联系。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 创意应用
-----------------

如果您想通过 NFC Shield V2.0 制作一些酷毙的项目，下面有一些供参考。

### NFC Shield 演示

***Paper Man***

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Seeed-recipe-paper_man.jpg)

[点击制作](http://www.seeedstudio.com/recipe/40-paper-man-an-interesting-object-to-interact-with-android.html)

[***通过 NFC Shield V2.0 制作更多酷毙的项目***](http://www.seeedstudio.com/recipe/index.php?query=NFC+Shield)

## 产品特性
--------

-   使用 SPI 协议的 ICSP 接头。因此这个扩展板可以与以下 Arduino 开发板一起工作 : Uno，Mega，Leonardo
-   无线近场通信频率 : 13.56MHz
-   SPI 协议 - 只需要 4 个引脚
-   输入电压 : Arduino 5V 引脚输入
-   电流(典型值) : 100mA
-   最大 5cm 有效距离
-   P2P 通信
-   支持 ISO14443 Type A 和 Type B 协议

## 硬件概述
-----------------

下面进行 NFC shield 的引脚和其他端子的介绍。

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Pn532-nfc-shield-pin-description.png)

**NFC shield 接口**

-   **D10** 和 **D9** 用于 SPI 片选 (CS/SS)。默认设置下 **D10** 处于连接，将 **D9** 焊接到 SS 焊盘，需要断开 SS 和 **D10** 之间的连接。
-   **D2** 可以用来接收扩展板的中断请求 (IRQ) 引脚信号。默认设置下中断没有连接，连接需要焊接 "D2/INT0" 和 "IRQ" 焊盘。
-   扩展板的 SPI 接口 (SPI MOSI，MISO 和 SCK 引脚)来自 Arduino 的 ICSP 接头，因此扩展板可以与以下 Arduino 主板搭配使用 : Uno，Mega 和 Leonardo。
-   ANT1 终端是 NFC 天线连接的地方。
-   扩展板电源来自 Arduino 板上的 5V 引脚。

NFC 扩展板天线是一个独立的 PCB 模块，通过线缆连接到扩展板。天线是用于接收和发送信息的区域。

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/NFC_Antanna_28x30.5.jpg)

**NFC 天线 PCB 图**

NFC shield 设置
----------------

### 硬件安装

1.  将 NFC 天线连接到扩展板。
2.  将 NFC Shield 堆叠在 Arduino 上，并使用 USB 线缆将 Arduino 连接到 PC。

### 安装库文件

1.  如果打开 Arduino IDE，请关闭
2.  下载 [PN532 library](https://github.com/Seeed-Studio/PN532) 压缩文件夹并提取文件。
3.  将文件夹 PN532, PN532_HSU, PN532_SPI, and PN532_I2C 复制到 Arduino 的 "libraries" 文件夹中。
4.  下载 [Don's NDEF library](https://github.com/don/NDEF) 压缩文件夹并提取文件。
5.  打开提取的文件夹并将 "NDEF-master" 文件夹重命名为 "NDEF"。
6.  复制 "NDEF" 文件夹到 Arduino 的 "libraries" 文件夹中.
7.  重新启动 Arduino IDE。可以在 Arduino 的 "Examples" 子菜单中看到 "NDEF" 和 "PN532" 的选项(参见下图)。

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Ndef-and-pn532-libraries-installed-in-arduino-ide.png)

**Arduino 可用库菜单**

NFC Shield 示例
--------------------------------

### Example #1: NFC Tag Scan

本示例将向您展示如何使用 NFC shield 来扫描 NFC 标签并显示其信息数据。

复制代码并粘贴到 Arduino IDE ，然后上传至主板。

#### 代码
```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    PN532_SPI interface(SPI, 10); // create a PN532 SPI interface with the SPI CS terminal located at digital pin 10
    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    void setup(void) {
        Serial.begin(115200); // begin serial communication
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC communication
    }

    void loop(void) {

        Serial.println("\nScan an NFC tag\n");
        if (nfc.tagPresent()) // Do an NFC scan to see if an NFC tag is present
        {
            NfcTag tag = nfc.read(); // read the NFC tag into an object, nfc.read() returns an NfcTag object.
            tag.print(); // prints the NFC tags type, UID, and NDEF message (if available)
        }
        delay(500); // wait half a second (500ms) before scanning again (you may increment or decrement the wait time)
    }
```
检验代码 :

1.  打开 Arduino 串口监视器
2.  设置波特率为 115200
3.  在 NFC 天线区上放置 NFC 标签
4.  NFC shield 将扫描标签，能够在串行监视器窗口中看到 NFC 标签的 UID，标签类型和信息(如果可用)。见下图。

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Nfc-pn532-output-example-1.png)

**Example #1 中当扫描到 NFC 标签，串口监视器输出结果**

### Example #2: NFC(keyless) Door Lock

本示例将向您展示如何使用 NFC 标签作为门锁的钥匙。门/锁机制您只需想一想，我们只会涉及到代码的 NFC 部分。

1.  同 Example #1: NFC Tag Scan，获得 NFC 标签的 UID。
2.  可选步骤 - 将绿色 LED 连接到引脚 **3**，如下图所示。用此 LED 指示钥匙的成功匹配。
3.  可选步骤 - 将红色 LED 连接到引脚 **4**，如下图所示。用此 LED 指示钥匙未匹配。
    ![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-2-red-green-led-nfc-alarm.PNG)

    **NFC lock circuit**

    ![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-2-red-green-led-nfc-alarm-real.png)

    **NFC lock circuit**

4.  在 Arduino IDE 中创建一个新的工程，复制，粘贴并上传下面的代码到 Arduino，用 Example \#1 获得的标签的 UID 代替 myUID。

#### 代码
```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    String const myUID = "1B B3 C6 EF"; // replace this UID with your NFC tag's UID
    int const greenLedPin = 3; // green led used for correct key notification
    int const redLedPin = 4; // red led used for incorrect key notification

    PN532_SPI interface(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10
    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    void setup(void) {
        Serial.begin(115200); // start serial comm
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC comm

        // make LED pins outputs
        pinMode(greenLedPin,OUTPUT);
        pinMode(redLedPin,OUTPUT);

        // turn off the LEDs
        digitalWrite(greenLedPin,LOW);
        digitalWrite(redLedPin,LOW);
    }

    void loop(void) {

        Serial.println("Scanning...");
        if (nfc.tagPresent()) // check if an NFC tag is present on the antenna area
        {
            NfcTag tag = nfc.read(); // read the NFC tag
            String scannedUID = tag.getUidString(); // get the NFC tag's UID

            if( myUID.compareTo(scannedUID) == 0) // compare the NFC tag's UID with the correct tag's UID (a match exists when compareTo returns 0)
            {
              // The correct NFC tag was used
              Serial.println("Correct Key");
              // Blink the green LED and make sure the RED led is off
              digitalWrite(greenLedPin,HIGH);
              digitalWrite(redLedPin,LOW);

              delay(500);
              digitalWrite(greenLedPin,LOW);
              delay(500);
              digitalWrite(greenLedPin,HIGH);
              delay(500);
              digitalWrite(greenLedPin,LOW);
              // put your here to trigger the unlocking mechanism (e.g. motor, transducer)
            }else{
              // an incorrect NFC tag was used
              Serial.println("Incorrect key");
              // blink the red LED and make sure the green LED is off
              digitalWrite(greenLedPin,LOW);
              digitalWrite(redLedPin,HIGH);

              delay(500);
              digitalWrite(redLedPin,LOW);
              delay(500);
              digitalWrite(redLedPin,HIGH);
              delay(500);
              digitalWrite(redLedPin,LOW);
              // DO NOT UNLOCK! an incorrect NFC tag was used.
              // put your code here to trigger an alarm (e.g. buzzard, speaker) or do something else
            }
        }
        delay(2000);
    }
```

检验代码 :

1.  打开 Arduino 串口监视器。
2.  在天线区域拿一个正确的 NFC 标签。
3.  绿色 LED 亮，串口监视器打印 "Correct Key"。
4.  在天线区域拿一个不同的 NFC 标签。
5.  红色 LED 亮，串口监视器打印 "Incorrect Key"。

### Example #3: How to use the Interrupt Pin (Example #2: Revisited)

虽然 Example #2 中的代码达到期望，但是 NFC 标签的检测有一个更简洁的方法。在这个例子中，我们将向您展示如何使用 NFC shield 中的中断引脚，以代替轮询扩展板(询问“是否有标签存在？”)，等待扩展板告诉 Arduino 一个标签可读。为什么要这样做？原因很多，但是一个原因是由于没有连续触发扩展板，电路会省电。

#### 硬件修改

焊接扩展板上标有 "D2/INT0 IRQ" 的焊盘。

#### 代码

上传代码到 Arduino :
```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    // FLAG_NONE used to signal nothing needs to be done
    #define FLAG_NONE 0
    // FLAG_IRQ_TRIGGERED used to signal an interrupt trigger
    #define FLAG_IRQ_TRIGGERED 1
    // FLAG_RESET_IRQ used to signal that the interrupt needs to be reset
    #define FLAG_RESET_IRQ 2
    // flags variable used to store the present flag
    volatile int flags = FLAG_NONE;

    String const myUID = "1B B3 C6 EF"; // replace this UID with your NFC tag's UID
    // LED pins
    int const greenLedPin = 3; // green led used for correct key notification
    int const redLedPin = 4; // red led used for incorrect key notification

    // the interrupt we'll be using (interrupt 0) is located at digital pin 2
    int const irqPin = 2; // interrupt pin

    PN532_SPI interface(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10

    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    String scannedUID = ""; // this is where we'll store the scanned tag's UID

    void setup(void) {
        // make LED pins outputs
        pinMode(greenLedPin,OUTPUT);
        pinMode(redLedPin,OUTPUT);

        Serial.begin(115200); // start serial comm
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC comm

        // turn off the LEDs
        digitalWrite(greenLedPin,LOW);
        digitalWrite(redLedPin,LOW);
       // attach the function "irq" to interrupt 0 on the falling edges
       attachInterrupt(0,irq,FALLING);// digital pin 2 is interrupt 0, we'll call the irq function (below) on the falling edge of this pin
    }

    void loop(void) {
        int flag = getFlag(); // get the present flag

        switch(flag) // check which flag/signal we are on
        {
           case FLAG_NONE:
             // nothing needs to be done
           break;
           case FLAG_IRQ_TRIGGERED: // the interrupt pin has been triggered
               Serial.println("Interrupt Triggered");
               if (nfc.tagPresent())
               {
                 // an NFC tag is present
                  NfcTag tag = nfc.read(); // read the NFC tag
                  scannedUID = tag.getUidString(); // get the NFC tag's UID
                  if(myUID.compareTo(scannedUID) == 0) // compare the NFC tag's UID with the correct tag's UID (a match exists when compareTo returns 0)
                  {
                    // the scanned NFC tag matches the saved myUID value
                    Serial.println("Correct tag/key");
                    blinkLed(greenLedPin,200,4); // blink the green led
                    // put your here to trigger the unlocking mechanism (e.g. motor, transducer)
                  }else{
                    // the scanned NFC tag's UDI does not match the myUID value
                    Serial.println("Incorrect tag/key");
                    blinkLed(redLedPin,200,4); // blink the red led
                    // DO NOT UNLOCK! an incorrect NFC tag was used.
                    // put your code here to trigger an alarm (e.g. buzzard, speaker) or do something else
                  }
                  // return to the original state
                  setFlag(FLAG_NONE);
                  reset_PN532_IRQ_pin();
               }else{
                 // a tag was not present (the IRQ was triggered by some other action)
                 setFlag(FLAG_NONE);
               }
           break;
           default:
             // do any other stuff for flags not handled above
           break;
        }
    }

    /*
    * Name: setFlat
    * Description: used to set actions/flags to be executed in the loop(void) function
    * Parameters:
    *        int flag - the action/flag to store
    * Returns: void
    */
    void setFlag(int flag)
    {
      flags = flag;
    }

    /*
    * Name: getFlag
    * Description: used to get the present flag/action
    * Parameters: void
    * Returns: int - the flags variable. The action/flag set by setFlag
    */
    int getFlag()
    {
      return flags;
    }

    /*
    * Name: irq
    * Description: Interrupt service routine (ISR). This function will be executed whenever there is a falling edge on digital pin 2 (the interrupt 0 pin)
    * Parameters: void
    * Returns: void
    */
    void irq()
    {
      if(getFlag()==FLAG_NONE){
        setFlag(FLAG_IRQ_TRIGGERED);
      }
    }
    /*
    * Name: reset_PN532_IRQ_pin
    * Description: used to reset the PN532 interrupt request (IRQ) pin
    * Parameters: void
    * Returns: void
    */
    void reset_PN532_IRQ_pin()
    {
      nfc.tagPresent();
    }

    /*
    * Name: blinkLed
    * Description: used to toggle a pin to blink an LED attached to the pin
    * Parameters:
    *      ledPin - the pin where the led is connected to
    *      delayTime - the time in milliseconds between HIGH and LOW
    *      times - the number of times to toggle the pin
    * Returns: void
    */
    void blinkLed(int ledPin,int delayTime,int times)
    {
      for(int i=0;i<times;i++){
        digitalWrite(ledPin,HIGH);
        delay(delayTime);
        digitalWrite(ledPin,LOW);
        delay(delayTime);
      }
    }
```

检验代码:

1.  如果需要，请按照 Example \#2 所示连接 LED。
2.  打开 Arduino 串口监视器
3.  在天线区域拿一个正确的 NFC 标签。
4.  绿色 LED 亮，串口监视器打印 "Correct Key"。
5.  在天线区域拿一个不同的 NFC 标签。
6.  红色 LED 亮，串口监视器打印 "Incorrect Key"。

代码在串口监视器中输出结果如下，您的应该类似

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-3-nfc-pn532-shield-interrupt-example.png)

**Serial comm window output from example 3.**

### Example #4: Write an NDEF Message to a Tag

NFC 标签能够存储数据，数据量取决于每个标签。在这个例子中，我们将在一个标签上存储两个字符串/信息，然后您能够使用 *Example \#6: Read an NDEF Message From a Tag* 中的代码读取 NDEF 信息。

上传代码到 Arduino

<div class="admonition note">
<p class="admonition-title">Note</p>
如果您的 NFC 标签格式不正确(串口监视器中将显示 "Message write failed")，您需要查看标签格式是否与 <span style="font-style:italic">Example #5: Format a Tag as NDEF</span> 代码中一致。
</div>

#### 代码
```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    PN532_SPI interface(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10

    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    void setup(void)
    {
        Serial.begin(115200); // start serial comm
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC comm
    }

    void loop(void)
    {
      Serial.println("Place a formatted Mifare Classic NFC tag on the reader.");
      if(nfc.tagPresent())
      {
        NdefMessage message = NdefMessage();
        message.addUriRecord("Hello, world!");
        message.addUriRecord("How are you today?");

        bool success = nfc.write(message);
        if(success)
        {
          Serial.println("The message was successfully written to the tag.");Ho
        }else{
          Serial.println("Message write failed.");
        }
      }

      delay(5000);
    }
```

检验代码 :

1.  打开 Arduino 串口监视器
2.  将 NFC 标签放在 NFC shield 的天线区域，等待判定信息，如下图所示。
3.  一旦显示成功，就从天线区域移除 NFC 标签，以防重写。

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-4-write-ndef-message-to-tag.png)

**Serial comm window for NDEF message written to card example.**

### Example #5: Format a Tag as NDEF

全新 NFC 标签最初可能不是 NDEF 格式。要将标签转化为 NDEF 格式，请将以下代码上传到您的 Arduino 开发板 :

#### 代码
```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    PN532_SPI interface(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10

    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    void setup(void)
    {
        Serial.begin(115200); // start serial comm
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC comm
    }

    void loop(void)
    {
        Serial.println("Place an unformatted Mifare Classic tag on the reader.");
        if (nfc.tagPresent()) {

            bool success = nfc.format();
            if (success) {
              Serial.println("Success, tag formatted as NDEF.");
            } else {
              Serial.println("Format failed.");
            }

        }
        delay(5000);
    }
```

检验代码 :

1.  打开串口监视器
2.  在天线区域拿一个待转化格式的 NFC 标签。
3.  等待判定信息，如下图所示。
4.  一旦显示成功，就从天线区域移除 NFC 标签，以防二次转换。

<div class="admonition note">
<p class="admonition-title">Note</p>
如果标签无法格式转化，请重试。如果失败，您的标签不能转格式为NDEF。
</div>

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-5-format-nfc-tag-as-ndef.png)

**Serial comm window output when formatting an NFC tag to NDEF.**

### Example #6: Read an NDEF Message From a Tag

正如您在上面的例子中看到的，NFC shield 能够将信息写入 NFC 标签，在这个例子中，您会看见 NFC shield 也能够从标签读取 NDEF 信息。

#### 代码

上传代码到 Arduino

```
    #include <SPI.h>
    #include "PN532_SPI.h"
    #include "PN532.h"
    #include "NfcAdapter.h"

    PN532_SPI interface(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10

    NfcAdapter nfc = NfcAdapter(interface); // create an NFC adapter object

    void setup(void)
    {
        Serial.begin(115200); // start serial comm
        Serial.println("NDEF Reader");
        nfc.begin(); // begin NFC comm
    }

    void loop(void)
    {
      Serial.println("\nScan an NFC tag\n");
      if (nfc.tagPresent()) // Do an NFC scan to see if an NFC tag is present
      {
          NfcTag tag = nfc.read(); // read the NFC tag
          if(tag.hasNdefMessage())
          {
            NdefMessage message = tag.getNdefMessage();
            for(int i=0;i<message.getRecordCount();i++)
            {
              NdefRecord record = message.getRecord(i);
              int payloadLength = record.getPayloadLength();
              byte payload[payloadLength];
              record.getPayload(payload);
              Serial.write(payload,payloadLength);
            }
          }
      }
      delay(500); // wait half a second (500ms) before scanning again (you may increment or decrement the wait time)
    }
```

检验代码:

1.  打开 Arduino 串口监视器
2.  在天线区域拿一个带有 NDEF 信息的 NFC 标签。
3.  标签中的 NDEF 信息成功读取，如下图所示

![](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/img/Example-6-read-ndef-message.png)

**Serial comm window output for NDEF message read**

### Example #7: How to Change the Chip Select Pin From D10 to D9

#### 硬件修改

1.  割断扩展板上标有 **SS** 和 **D10** 的焊接。
2.  在焊盘上焊接 **SS** 和 **D9**。

然后，您可以在上面的示例中使用相同的代码，但对于 PN532 接口使用引脚 **9** 而不是引脚 **10** ：

#### 代码

    PN532_SPI interface(SPI, 9); // create a SPI interface for the shield with the SPI CS terminal at digital pin 9

### Example #8: Use Two NFC Shields With One Arduino Board

#### 硬件修改

1.  在两个扩展板中的一个上执行 Example #7 中描述的硬件修改。
2.  在 Arduino 上堆叠两个扩展板。

现在您可以创建两个单独的 NFC 项目，每个扩展板对应一个项目，如下所示 :

#### 代码
```
    PN532_SPI interface_shield_1(SPI, 10); // create a SPI interface for the shield with the SPI CS terminal at digital pin 10
    PN532_SPI interface_shield_2(SPI, 9); // create a SPI interface for the shield with the SPI CS terminal at digital pin 9

    NfcAdapter nfc_shield_1 = NfcAdapter(interface_shield_1); // create an NFC adapter object for shield one
    NfcAdapter nfc_shield_2 = NfcAdapter(interface_shield_2); // create an NFC adapter object for shield two
```

资源下载
---------

- **[Eagle 文件]** [NFC Shield v2.0 Eagle File](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/res/NFC_Shield_V2.0b_Eagle_files.zip)
- **[Eagle 文件]** [NFC Shield v2.1 Eagle File](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/res/NFC_Shield_v2.1_Eagle_File.zip)
- **[原理图 PDF]** [NFC Shield v2.0 Schematic](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/res/NFC_Shield_Schematic.pdf)
- **[原理图 PDF]** [NFC Shield v2.1 Schematic](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/res/NFC_Shield_v2.1.pdf)
- **[库文件]** [PN532_SPI Library For NFC Shield v2.0](https://github.com/Seeed-Studio/PN532)
- **[芯片数据手册]** [PN532 Datasheet](https://raw.githubusercontent.com/SeeedDocument/NFC_Shield_V2.0/master/res/PN532.pdf)
- **[其他资源]** [FAQ of NFC Shield](http://support.seeedstudio.com/knowledgebase/articles/462025-nfc-shield-sku-sld01097p)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/NFC_Shield_V2.0 -->
