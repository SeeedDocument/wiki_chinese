---
title: Grove - MOSFET
category: Others
bzurl: https://seeedstudio.com/Grove-MOSFET-p-1594.html
oldwikiname: Grove_-_MOSFET
prodimagename: Mosfet_01.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/mosfet.jpg
surveyurl: https://www.research.net/r/Grove-MOSFET
sku: 103020008
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MOSFET/master/img/Mosfet_01.jpg)

Grove - MOSFET使您能够在微控制器上以低电压（例如5V）来控制需要更高电压的项目，例如15VDC。 MOSFET也是一种开关，但其开关频率可以达到5MHz，比正常的机械式继电器快得多。 板上有两个螺丝端口。 一个用于外部电源，另一个用于要控制的设备。 当它关闭时，MOSFET的电力将从一端传递到另一端。 但是如果外部电源不存在，您的设备仍然可以通过Grove接口从微控制器获取电力。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11BQ34EK&id=45573744942)

产品特性
-------------

- 工作电压：5V
- 输入电压：5〜15V
- MOSFET型号：CJQ4435

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

支持平台
-------------------

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MOSFET/master/img/MOSFET_Interface_Function.jpg)

Vin：接受电流小于2A的5V〜15V电源。

Vout：在这里连接执行器。

示范
-------------

### 使用 Arduino

这里我们演示如何使用Grove-MOSFET来控制电机。 我们为外部电源提供电源，如果受控设备的电流小于300mA，Seeeduino也可以完全支持它，无需额外的电源。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-MOSFET/master/img/Static_image.gif)

```
    // demo of Grove - MOSFET
    // use pin 6 to control a motor

    int motorPin = 6;

    void setup()
    {
        Serial.begin(38400);
        pinMode(motorPin, OUTPUT);
        Serial.println("Grove - MOSFET Test Demo!");
    }

    void loop()
    {
        motorOnThenOffWithSpeed();
        motorAcceleration();
    }

    void motorOnThenOffWithSpeed()
    {
        int onSpeed  = 200;                         // a number between 0 (stopped) and 255 (full speed)
        int onTime   = 2500;
        int offSpeed = 50;                          // a number between 0 (stopped) and 255 (full speed)
        int offTime  = 1000;
        analogWrite(motorPin, onSpeed);
        delay(onTime);
        analogWrite(motorPin, offSpeed);
        delay(offTime);
    }

    void motorAcceleration()
    {
        int delayTime = 50;
        for(int i=0; i<256; i++)
        {
            analogWrite(motorPin, i);
            delay(delayTime);
        }

        for(int i=255; i>=0; i--)
        {
            analogWrite(motorPin, i);
            delay(delayTime);
        }
    }
```

### 使用Raspberry Pi

1.你应该准备一个raspberry pi 和  grovepi 或者 grovepi+.

2.您应该已经完成配置开发环境，否则请遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 进行配置。

3.硬件连接

-   用Grove数据线将传感器插入Grovepi端口 **D6**。

4.导航到示例目录：
```
    cd yourpath/GrovePi/Software/Python/
```
-   找到这行代码
```
    nano grove_mosfet.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove MOSFET to analog port D6
    # SIG,NC,VCC,GND
    mosfet = 6

    grovepi.pinMode(mosfet,"OUTPUT")
    time.sleep(1)

    while True:
        try:
            # Full speed
            grovepi.analogWrite(mosfet,255)
            print "full speed"
            time.sleep(2)

            # Half speed
            grovepi.analogWrite(mosfet,128)
            print "half speed"
            time.sleep(2)

            # Off
            grovepi.analogWrite(mosfet,0)
            print "off"
            time.sleep(2)

        except KeyboardInterrupt:
            grovepi.analogWrite(mosfet,0)
            break
        except IOError:
            print "Error"
```

5.运行这个示例
```
    sudo python grove_mosfet.py
```

资源下载
---------

- [Grove - MOSFET Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-MOSFET/master/res/Grove-MOSFET_Eagle_File.zip)
- [Grove - MOSFET Schematic PDF](https://github.com/SeeedDocument/Grove-MOSFET/raw/master/res/Grove%20-%20MOSFET%20.pdf)
- [CJQ4435 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-MOSFET/master/res/CJQ4435.pdf)
- [MOSFET Wikipedia](http://en.wikipedia.org/wiki/MOSFET)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_MOSFET -->
