---
title: Grove - LED Bar
category: Display
bzurl: https://seeedstudio.com/Grove-LED-Bar-p-1178.html
oldwikiname: Grove_-_LED_Bar
prodimagename: Grove-LED_Bar-1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-LED_Bar
sku: 104030002
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_wio
---

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/img/Grove-LED_Bar-1.jpg">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/img/Grove-LED_Bar-2.jpg">
        </td>
    </tr>
</table>

Grove – LED Bar 包括一个 10 段 LED 灯和一个 MY9221 LED 控制芯片。它可以用作电池寿命，电压，水位，音乐音量或其他需要梯度显示的其他值。LED Bar 中有 10 个 LED 条：一个红色，一个黄色，一个浅绿色和七个绿色条。演示代码可用于初次上手和快速运行。 它将 LED 顺序地从红色点亮到绿色，最终整个 LED Bar 亮起。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.139f49d1BHsFUe&id=520900900588)

产品特性
--------

-   输入电压: 3.3V/5V
-   每个 LED 段都可以通过代码单独控制
-   显示直观
-   宽电压输入范围：3V-5.5V DC
-   可用演示代码
-   Suli 兼容库

!!!Tip
    关于 Grove 模块的更多细节请参考 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

<div class="admonition note">
<p class="admonition-title">Note</p>
想了解 Suli-compatible 的更多细节，请参考 <a href="/Suli">Suli</a>
</div>

操作示例
-------------

### 使用 [Arduino](/Arduino "Arduino")

这是一个简单的演示，可以帮助您快速开始使用 Grove - LED Bar。
我们需要一个 [Seeeduino V3.0](http://www.seeedstudio.com/depot/seeeduino-v30-atmega-328p-p-669.html?cPath=6_7) 和一个 **Grove - Base Shield** 之类的扩展板.

#### 硬件安装

把 Grove - LED Bar 接在 Grove - Base Shield 的 **D8** 接口上，然后把扩展板插在 Arduino 上。

#### 下载代码并上传

你可以在 github 上下载 函数库，点击 [这里](https://github.com/Seeed-Studio/Grove_LED_Bar) 下载，然后解压缩到 Arduino 的函数库文件夹下。

然后打开 Arduino IDE, **File（文件） -> examples（示例） -> LED_Bar -> Level**，打开示例代码。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/img/LED_BAR_IDE.png)

点击 **Upload（上传）** 上传代码，如果您在开始使用 Arduino 时遇到问题，请点击 [这里](/Getting_Started_with_Seeeduino) 获取帮助。

#### 工作演示

你的 Grove - LED Bar现在开始工作了，应该是如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/img/LED_Bar_shining.gif)

### 使用 Raspberry Pi

1.你应该已经有了 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.你应该已经配置好了开发环境，如果没有请访问 [这里](/GrovePiPlus)。

3.连接

-   把 LED Bar 用 Grove 线连接到 Grovepi 的 **D3** 接口上。

4.浏览到演示目录：
```
cd yourpath/GrovePi/Software/Python/
```

-   查看代码：
```
nano grove_ledbar.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi
import random

# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
ledbar = 5

grovepi.pinMode(ledbar,"OUTPUT")
time.sleep(1)
i = 0

# LED Bar methods
# grovepi.ledBar_init(pin,orientation)
# grovepi.ledBar_orientation(pin,orientation)
# grovepi.ledBar_setLevel(pin,level)
# grovepi.ledBar_setLed(pin,led,state)
# grovepi.ledBar_toggleLed(pin,led)
# grovepi.ledBar_setBits(pin,state)
# grovepi.ledBar_getBits(pin)

    while True:
        try:
        print "Test 1) Initialise - red to green"
        # ledbar_init(pin,orientation)
        # orientation: (0 = red to green, 1 = green to red)
        grovepi.ledBar_init(ledbar, 0)
        time.sleep(.5)


        print "Test 2) Set level"
        # ledbar_setLevel(pin,level)
        # level: (0-10)
        for i in range(0,11):
            grovepi.ledBar_setLevel(ledbar, i)
            time.sleep(.2)
        time.sleep(.3)

        grovepi.ledBar_setLevel(ledbar, 8)
        time.sleep(.5)

        grovepi.ledBar_setLevel(ledbar, 2)
        time.sleep(.5)

        grovepi.ledBar_setLevel(ledbar, 5)
        time.sleep(.5)


        print "Test 3) Switch on/off a single LED"
        # ledbar_setLed(pin,led,state)
        # led: which led (1-10)
        # state: off or on (0,1)
        grovepi.ledBar_setLed(ledbar, 10, 1)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 9, 1)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 8, 1)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 1, 0)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 2, 0)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 3, 0)
        time.sleep(.5)


        print "Test 4) Toggle a single LED"
        # flip a single led - if it is currently on, it will become off and vice versa
        # ledbar_toggleLed(ledbar, led)
        grovepi.ledBar_toggleLed(ledbar, 1)
        time.sleep(.5)

        grovepi.ledBar_toggleLed(ledbar, 2)
        time.sleep(.5)

        grovepi.ledBar_toggleLed(ledbar, 9)
        time.sleep(.5)

        grovepi.ledBar_toggleLed(ledbar, 10)
        time.sleep(.5)


        print "Test 5) Set state - control all leds with 10 bits"
        # ledbar_setBits(ledbar, state)
        # state: (0-1023) or (0x00-0x3FF) or (0b0000000000-0b1111111111) or (int('0000000000',2)-int('1111111111',2))
        for i in range(0,32):
            grovepi.ledBar_setBits(ledbar, i)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 6) Get current state"
        # state = ledbar_getBits(ledbar)
        # state: (0-1023) a bit for each of the 10 LEDs
        state = grovepi.ledBar_getBits(ledbar)
        print "with first 5 leds lit, the state should be 31 or 0x1F"
        print state

        # bitwise shift five bits to the left
        state = state << 5
        # the state should now be 992 or 0x3E0
        # when saved the last 5 LEDs will be lit instead of the first 5 LEDs
        time.sleep(.5)


        print "Test 7) Set state - save the state we just modified"
        # ledbar_setBits(ledbar, state)
        # state: (0-1023) a bit for each of the 10 LEDs
        grovepi.ledBar_setBits(ledbar, state)
        time.sleep(.5)


        print "Test 8) Swap orientation - green to red - current state is preserved"
        # ledbar_orientation(pin,orientation)
        # orientation: (0 = red to green, 1 = green to red)
        # when you reverse the led bar orientation, all methods know how to handle the new LED index
        # green to red
        grovepi.ledBar_orientation(ledbar, 1)
        time.sleep(.5)

        # red to green
        grovepi.ledBar_orientation(ledbar, 0)
        time.sleep(.5)

        # green to red
        grovepi.ledBar_orientation(ledbar, 1)
        time.sleep(.5)


        print "Test 9) Set level, again"
        # ledbar_setLevel(pin,level)
        # level: (0-10)
        # note the red LED is now at index 10 instead of 1
        for i in range(0,11):
            grovepi.ledBar_setLevel(ledbar, i)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 10) Set a single LED, again"
        # ledbar_setLed(pin,led,state)
        # led: which led (1-10)
        # state: off or on (0,1)
        grovepi.ledBar_setLed(ledbar, 1, 0)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 3, 0)
        time.sleep(.5)

        grovepi.ledBar_setLed(ledbar, 5, 0)
        time.sleep(.5)


        print "Test 11) Toggle a single LED, again"
        # ledbar_toggleLed(ledbar, led)
        grovepi.ledBar_toggleLed(ledbar, 2)
        time.sleep(.5)

        grovepi.ledBar_toggleLed(ledbar, 4)
        time.sleep(.5)


        print "Test 12) Get state"
        # state = ledbar_getBits(ledbar)
        # state: (0-1023) a bit for each of the 10 LEDs
        state = grovepi.ledBar_getBits(ledbar)

        # the last 5 LEDs are lit, so the state should be 992 or 0x3E0

        # bitwise shift five bits to the right
        state = state >> 5
        # the state should now be 31 or 0x1F


        print "Test 13) Set state, again"
        # ledbar_setBits(ledbar, state)
        # state: (0-1023) a bit for each of the 10 LEDs
        grovepi.ledBar_setBits(ledbar, state)
        time.sleep(.5)


        print "Test 14) Step"
        # step through all 10 LEDs
        for i in range(0,11):
            grovepi.ledBar_setLevel(ledbar, i)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 15) Bounce"
        # switch on the first two LEDs
        grovepi.ledBar_setLevel(ledbar, 2)

        # get the current state (which is 0x3)
        state = grovepi.ledBar_getBits(ledbar)

        # bounce to the right
        for i in range(0,9):
            # bit shift left and update
            state <<= 1;
            grovepi.ledBar_setBits(ledbar, state)
            time.sleep(.2)

        # bounce to the left
        for i in range(0,9):
            # bit shift right and update
            state >>= 1;
            grovepi.ledBar_setBits(ledbar, state)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 16) Random"
        for i in range(0,21):
            state = random.randint(0,1023)
            grovepi.ledBar_setBits(ledbar, state)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 17) Invert"
        # set every 2nd LED on - 341 or 0x155
        state = 341
        for i in range(0,5):
            grovepi.ledBar_setBits(ledbar, state)
            time.sleep(.2)

            # bitwise XOR all 10 LEDs on with the current state
            state = 0x3FF ^ state

            grovepi.ledBar_setBits(ledbar, state)
            time.sleep(.2)
        time.sleep(.3)


        print "Test 18) Walk through all possible combinations"
        for i in range(0,1024):
            grovepi.ledBar_setBits(ledbar, i)
            time.sleep(.1)
        time.sleep(.4)

    except KeyboardInterrupt:
        grovepi.ledBar_setBits(ledbar, 0)
        break
    except IOError:
        print "Error"
```

5.运行示例。
```
sudo python grove_ledbar.py
```

6.如果您的 Grovepi 没有安装最新的固件，请更新固件，否则此演示可能无法正常工作。
```
cd yourpath/GrovePi/Firmware
sudo ./firmware_update.sh
```

##Project

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/gun.jpg)

Inspired by OVERWATCH, we have made a very cool Wooden Laser Gun toy for fun these day!

The Wooden Laser Gun and the Gun Target are all based on an Arduino board called Seeeduino Lotus. The laser emitter on the Laser Gun is controlled to fire laser pulse to "activate" the Gun Target. And there are 3 light sensors on the Gun Target to detect the laser pulse. It seems very simple right? If you are interested in our project, please make one for yourself or your child! It's worth to spend one day DIY it as a Xmas present.    

[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/make.png)](http://www.instructables.com/id/DIY-a-Wooden-Laser-Gun-As-a-Xmas-Present-for-Your-/)

资源下载
---------

-   **[Eagle 文件]**[Grove - LED Bar Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/res/Grove-LED_Bar_v1.0.zip)
-   **[代码库]**[Grove - LED Bar Library](https://github.com/Seeed-Studio/Grove_LED_Bar)
-   **[代码库]**[Suli-compatible Library](https://github.com/Seeed-Studio/LED_Bar_Suli)
-   **[数据手册]**[MY9221 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-LED_Bar/master/res/MY9221_DS_1.0.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_LED_Bar -->
