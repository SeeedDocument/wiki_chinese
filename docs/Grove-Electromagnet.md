---
title: Grove - Electromagnet
category: Sensor
bzurl: https://seeedstudio.com/Grove-Electromagnet-p-1820.html
oldwikiname: Grove_-_Electromagnet
prodimagename: Grove_Electromagnet_02.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Electromagnet
sku: 101020073
tags: grove_digital, io_5v, plat_duino, plat_wio
---

<table>
    <tr>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/img/Grove_Electromagnet_02.jpg"></td>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/img/Grove_Electromagnet-1.png"></td>
    </tr>
</table>

Electromagnet是一种通过电流产生磁场的磁体。 根据安培定律，流入电线的电流在电线周围产生磁场（如图所示）。 为了使磁场更加集中，在Electromagnet中，缠绕着很多整齐排布的线圈。 所有线圈的磁场通过线圈的中心，在那里产生强磁场。 这样Grove - Electromagnet可以吸起1KG重的铁。 它使用很方便，可以通过它学习到电磁铁的原理。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.44c32a0a6LYmdY&id=45478243491)

产品特性
--------

-   兼容Grove接口
-   最大能够吸气1KG
-   待机电流比较低

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

规格参数
-------------


- 工作电压：DC 5V
- 工作电流：400mA
- 待机电流：200uA
- 吸起重量：1KG

平台支持
-------------------

使用方法
-----

### 使用 Arduino

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/img/Grove_Electromagnet-2.png)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/img/Grove_Electromagnet-3.png)

程序:

```
/*
  Turns on an Electromagnet on for one second, then off for one second, repeatedly.
  This example code is in the public domain.
*/

int Electromagnet = 0;
int LED = 13;

// the setup routine runs once when you press reset:
void setup() {
    // initialize the digital pin as an output.
    pinMode(Electromagnet, OUTPUT);
    pinMode(LED, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
    digitalWrite(Electromagnet, HIGH);  // turn the Electromagnet on (HIGH is the voltage level)
    digitalWrite(LED, HIGH);            // turn the LED on (HIGH is the voltage level)
    delay(1000);                        // wait for a second
    digitalWrite(Electromagnet, LOW);   // turn the Electromagnet off by making the voltage LOW
    digitalWrite(LED, LOW);             // turn the LED off by making the voltage LOW
    delay(1000);                        // wait for a second
}
```

### 使用 Raspberry Pi

1.你应该有一个 raspberry pi和grovepi或grovepi +。

2.您需要完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。

3.硬件连接

-   使用 grove连接线将传感器插入Grovepi 插座 **D4** 端口。

4.导航到演示目录：
```
    cd yourpath/GrovePi/Software/Python/
```

-   找到这行代码

```
    nano grove_electromagnet.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # The electromagnet can hold a 1KG weight

    # Connect the Grove Electromagnet to digital port D4
    # SIG,NC,VCC,GND
    electromagnet = 4

    grovepi.pinMode(electromagnet,"OUTPUT")
    time.sleep(1)

    while True:
        try:
            # Switch on electromagnet
            grovepi.digitalWrite(electromagnet,1)
            print "on"
            time.sleep(2)

            # Switch off electromagnet
            grovepi.digitalWrite(electromagnet,0)
            print "off"
            time.sleep(2)

        except KeyboardInterrupt:
            grovepi.digitalWrite(electromagnet,0)
            break
        except IOError:
            print "Error"
```

5.运行这个示例。
```
    sudo python grove_electromagnet.py
```

资源下载
--------

- [Grove Electromagnet v1.0 SCH PCB.zip](https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/res/Grove_Electromagnet_v1.0_SCH_PCB.zip "File:Grove Electromagnet v1.0 SCH PCB.zip")
- [Datasheet ZYE1-P20-15 PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-Electromagnet/master/res/ZYE1-P20-15.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Electromagnet -->
