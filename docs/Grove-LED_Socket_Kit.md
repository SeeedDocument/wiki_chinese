---
title: Grove - LED Socket Kit
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-White-LED-p-1140.html
oldwikiname:  Grove - LED Socket Kit
prodimagename: Grove-White-LED-p-2016.jpeg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-LED_Socket_Kit
sku:  104030009
---
![](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/img/Grove-White-LED-p-2016.jpeg)

Grove - LED 是为 Arduino/Seeeduino 的初学者设计的，显示数字端口输出。它可以很简单地安装到你的箱子或桌子的表面，并用作电源或信号的指示灯。其亮度可以通过电位器进行调节。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.2b637084NxFCI3&id=527003387872)

## 产品特性
---
*   兼容 Grove 接口

*   兼容 3.3V/5V

*   可调 LED 方向

*   可调 LED 亮度

## 规格参数
---
<table >
<tr>
<td width="400"> **项目**
</td>
<td width="400"> **描述**
</td></tr>
<tr style="font-size: 90%">
<td> LED 控制方法
</td>
<td> 使用 Arduino 的数字引脚控制
</td></tr>
<tr style="font-size: 90%">
<td> 工作电压
</td>
<td> 5V
</td></tr>
<tr style="font-size: 90%">
<td> 接口
</td>
<td> Grove 接口
</td></tr></table>

##  Arduino 入门指导
---
这里我们展示如何使用 Arduino 来控制 LED 的状态。

1. 使用 4pin Grove 电缆将 LED 连接到 Base Shield 的 **D2**。当然，如果需要，也可以更改为其他有效的数字端口，并且端口的定义也需要更改。

2. 把它插到 Arduino/Seeeduino 上。 使用 USB 电缆将电路板连接到电脑。
![](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/img/Grove-LED.jpg)

3. 将演示代码复制到 Arduino IDE 的新窗口，然后上传到 Arduino 或 Seeeduino 板。如果您不知道如何上传，请点击 [这里](http://wiki.seeedstudio.com/cn/Upload_Code/)。

    您可以看到 LED 灯每秒闪一次。

```c
/*************************************************************************
* File Name          : GroveLEDDemoCode.ino
* Author             : Seeedteam
* Version            : V1.1
* Date               : 18/2/2012
* Description        : Demo code for Grove - LED
*************************************************************************/

#define LED 2 //connect LED to digital pin2
void setup() {
    // initialize the digital pin2 as an output.
    pinMode(LED, OUTPUT);
}

void loop() {
    digitalWrite(LED, HIGH);   // set the LED on
    delay(500);               // for 500ms
    digitalWrite(LED, LOW);   // set the LED off
    delay(500);
}
```

##  Raspberry Pi 入门指导
---
使用 Grove 连接线将 LED 连接到 GrovePi+ 的端口 **D4**，然后打开 Raspberry Pi 的电源。例程代码如下：

```python
# GrovePi LED Blink example

import time
from grovepi import *

# Connect the Grove LED to digital port D4
led = 4

pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    try:
        #Blink the LED
        digitalWrite(led,1)		# Send HIGH to switch on LED
        time.sleep(1)

        digitalWrite(led,0)		# Send LOW to switch off LED
        time.sleep(1)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:				# Print "Error" if communication error encountered
        print "Error"
```

###  运行程序

*   转到示例代码文件所在的目录：

```python
cd GrovePi/Software/Python/
```

*   运行示例：

```python
sudo python grove_led_blink.py
```

##  资源下载
---
*   **[原理图]**[Grove - LED V1.3 Source files (Eagle and pdf)](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/res/Grove-LED_v1.3_Schematics.zip)
*   **[原理图]**[Grove - LED Source files (Eagle and pdf)](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/res/Grove-LED_v1.0_Source_File.zip)
*   **[代码]**[GroveLEDDemoCode](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/res/GroveLEDDemoCode.zip)
*   **[Eagle 文件]**[Grove-LED Socket Kit](https://github.com/SeeedDocument/Grove-LED_Socket_Kit/raw/master/res/Grove-LED_Socket_Eagle_File.zip)
