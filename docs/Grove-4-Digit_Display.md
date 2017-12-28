---
title: Grove - 4-Digit Display
category: Display
bzurl: https://seeedstudio.com/Grove-4-Digit-Display-p-1198.html
oldwikiname: Grove_-_4-Digit_Display
prodimagename: Grove-4_digit_display.jpg
wikiurl: http://seeed.wiki/Grove-4-Digit_Display
sku: 104030003
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_wio
---

[![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/Grove-4_digit_display.jpg)](http://www.seeedstudio.com/depot/grove-4digital-display-p-1198.html)

Grove - 4-Digit Display 模块是一个有着12个引脚的模块。 在这个模块中，我们使用TM1637将控制引脚的数量缩小到2个.也就是说，它只通过Arduino或Seeeduino的2个数字引脚来控制内容和亮度。 对于需要字母数字显示的项目，这是一个不错的选择。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4257a1e2FckHFV&id=45908368559)

产品特性
--------


- 能够显示4位红色字母和数字
- 能够兼容Grove接口（3.3V / 5V）
- 具有8个调节亮度的级别

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

创意应用
-----------------


- 显示时间
- 秒表
- 传感器数值的显示

产品规格
--------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小
</th>
<th scope="col">
标准
</th>
<th scope="col">
最大
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
3.3
</td>
<td>
5.0
</td>
<td>
5.5
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
工作电流
</th>
<td>
0.2
</td>
<td>
27
</td>
<td>
80
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
外形尺寸
</th>
<td colspan="3">
42x24x14
</td>
<td>
mm
</td>
</tr>
<tr align="center">
<th scope="row">
重量
</th>
<td colspan="3">
7±1
</td>
<td>
g
</td>
</tr>
</table>

Platforms Supported
-------------------

硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/4-digit_display_interface.jpg)

**Grove interface** - 可连接到Grove - Base Shield上的数字端口。

**4 - digit display** - 普通阳极数码管。

**管脚定义:** CLK DIO VCC GND

入门指导
---------------

### 使用 TI LaunchPad

显示数字（4位数字显示）

本示例演示了如何使用Grove-4-Digital Display显示一些数字。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/4_digital_display.jpg)

```
/*
 * TM1637.cpp
 * A library for the 4 digit display
 */
#include "TM1637.h"
#define CLK 39 //pins definitions for TM1637 and can be changed to other ports
#define DIO 38
TM1637 tm1637(CLK,DIO);
void setup()
{
    tm1637.init();
    tm1637.set(BRIGHT_TYPICAL);//BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7;
}
void loop()
{
    int8_t NumTab[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};//0~9,A,b,C,d,E,F
    int8_t ListDisp[4];
    unsigned char i = 0;
    unsigned char count = 0;
    delay(150);
    while(1)
    {
        i = count;
        count ++;
        if(count == sizeof(NumTab)) count = 0;
        for(unsigned char BitSelect = 0;BitSelect < 4;BitSelect ++)
        {
            ListDisp[BitSelect] = NumTab[i];
            i ++;
            if(i == sizeof(NumTab)) i = 0;
        }
        tm1637.display(0,ListDisp[0]);
        tm1637.display(1,ListDisp[1]);
        tm1637.display(2,ListDisp[2]);
        tm1637.display(3,ListDisp[3]);
        delay(300);
    }
}
```

### 使用 Arduino

使用 TM1637 来控制显示的内容以及改变亮度。 在这里我们展示如何显示时间。

1. 使用Grove连接线将LED Strip Driver 上标有“IN”的Grove插座和 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的数字 **D2** 端口连接起来。 您可以根据需要更改数字端口。 但是不要忘了在演示代码的定义中更改端口号。

2. 插入Arduino / Seeeduino或将 [Grove - Mega Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.40687f70xWU65e&id=45770800195) 插入Arduino Mega。

    Seeeduino 和 Grove - 4-digit display:

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/Seeeduino_and_4-digit_display.jpg)

    Arduino Mega 和 Grove - 4-digit display:
    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/Arduino_Mega_and_4-digit_display.jpg)

3. 通过USB数据线将Arduino / Seeeduino连接到PC。

4. 下载 [the 4-Digit Display 库](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/res/DigitalTube.zip) 和 [TimerOne 库](https://code.google.com/p/arduino-timerone/downloads/detail?name=TimerOne-v9.zip&can=2&q=). 解压并将它们放在Arduino IDE的库文件中，路径为：..\\arduino-1.0\\libraries。

5. 重新启动Arduino IDE，打开一个您喜欢的演示代码，例如时钟显示直接通过路径：**File(文件) - >Example(示例) - >DigitalTube - >ClockDisplay**。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/Open_ClockDisplay.ino.jpg)

6. 上传演示代码，几秒钟后时钟开始显示。

    你可以看到这个:
    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/img/Display_the_clock.jpg)

### 使用 Raspberry Pi

1.你应该有一个raspberry pi和grovepi或grovepi +。

2.您需要完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。

3.硬件连接

-   使用grove连接线将传感器插入Grovepi插座 **D5** 端口。

4.导航到演示目录：
```
cd yourpath/GrovePi/Software/Python/
```

-   找到这行代码
```
nano grove_4_digit_display.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove 4 Digit Display to digital port D5
    # CLK,DIO,VCC,GND
    display = 5
    grovepi.pinMode(display,"OUTPUT")

    # If you have an analog sensor connect it to A0 so you can monitor it below
    sensor = 0
    grovepi.pinMode(sensor,"INPUT")

    time.sleep(.5)

    # 4 Digit Display methods
    # grovepi.fourDigit_init(pin)
    # grovepi.fourDigit_number(pin,value,leading_zero)
    # grovepi.fourDigit_brightness(pin,brightness)
    # grovepi.fourDigit_digit(pin,segment,value)
    # grovepi.fourDigit_segment(pin,segment,leds)
    # grovepi.fourDigit_score(pin,left,right)
    # grovepi.fourDigit_monitor(pin,analog,duration)
    # grovepi.fourDigit_on(pin)
    # grovepi.fourDigit_off(pin)

    while True:
        try:
            print "Test 1) Initialise"
            grovepi.fourDigit_init(display)
            time.sleep(.5)

            print "Test 2) Set brightness"
            for i in range(0,8):
                grovepi.fourDigit_brightness(display,i)
                time.sleep(.2)
            time.sleep(.3)

            # set to lowest brightness level
            grovepi.fourDigit_brightness(display,0)
            time.sleep(.5)

            print "Test 3) Set number without leading zeros"
            leading_zero = 0
            grovepi.fourDigit_number(display,1,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,12,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,123,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,1234,leading_zero)
            time.sleep(.5)

            print "Test 4) Set number with leading zeros"
            leading_zero = 1
            grovepi.fourDigit_number(display,5,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,56,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,567,leading_zero)
            time.sleep(.5)
            grovepi.fourDigit_number(display,5678,leading_zero)
            time.sleep(.5)

            print "Test 5) Set individual digit"
            grovepi.fourDigit_digit(display,0,2)
            grovepi.fourDigit_digit(display,1,6)
            grovepi.fourDigit_digit(display,2,9)
            grovepi.fourDigit_digit(display,3,15) # 15 = F
            time.sleep(.5)

            print "Test 6) Set individual segment"
            grovepi.fourDigit_segment(display,0,118) # 118 = H
            grovepi.fourDigit_segment(display,1,121) # 121 = E
            grovepi.fourDigit_segment(display,2,118) # 118 = H
            grovepi.fourDigit_segment(display,3,121) # 121 = E
            time.sleep(.5)

            grovepi.fourDigit_segment(display,0,57) # 57 = C
            grovepi.fourDigit_segment(display,1,63) # 63 = O
            grovepi.fourDigit_segment(display,2,63) # 63 = O
            grovepi.fourDigit_segment(display,3,56) # 56 = L
            time.sleep(.5)

            print "Test 7) Set score"
            grovepi.fourDigit_score(display,0,0)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,0)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,1)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,2)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,3)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,4)
            time.sleep(.2)
            grovepi.fourDigit_score(display,1,5)
            time.sleep(.5)

            print "Test 8) Set time"
            grovepi.fourDigit_score(display,12,59)
            time.sleep(.5)

            print "Test 9) Monitor analog pin"
            seconds = 10
            grovepi.fourDigit_monitor(display,sensor,seconds)
            time.sleep(.5)

            print "Test 10) Switch all on"
            grovepi.fourDigit_on(display)
            time.sleep(.5)

            print "Test 11) Switch all off"
            grovepi.fourDigit_off(display)
            time.sleep(.5)

        except KeyboardInterrupt:
            grovepi.fourDigit_off(display)
            break
        except IOError:
            print "Error"
```

5.运行这个示例
```
sudo python grove_4_digit_display.py
```
6.如果您的Grovepi没有最新的到最新的固件，此演示可能无法正常工作。
```
cd yourpath/GrovePi/Firmware
sudo ./firmware_update.sh
```
## 项目

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/gun.jpg)

Inspired by OVERWATCH, we have made a very cool Wooden Laser Gun toy for fun these day!

The Wooden Laser Gun and the Gun Target are all based on an Arduino board called Seeeduino Lotus. The laser emitter on the Laser Gun is controlled to fire laser pulse to "activate" the Gun Target. And there are 3 light sensors on the Gun Target to detect the laser pulse. It seems very simple right? If you are interested in our project, please make one for yourself or your child! It's worth to spend one day DIY it as a Xmas present.    

[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/make.png)](http://www.instructables.com/id/DIY-a-Wooden-Laser-Gun-As-a-Xmas-Present-for-Your-/)

资源下载
---------

-   [Grove - 4-Digit Display V1.0 eagle files](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/res/Grove-4-Digit_Display_V1.0_eagle_files.zip)
-   [Schematic in PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/res/Grove_4-Digit_Display_V1.0.pdf)
-   [4-Digit Display library](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/res/DigitalTube.zip)
-   [TimerOne library](https://code.google.com/p/arduino-timerone/downloads/detail?name=TimerOne-v9.zip&can=2&q=)
-   [Four-Digit Display Suli Library](https://github.com/Seeed-Studio/Four_Digit_Display_Suli)
-   [TM1637 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-4-Digit_Display/master/res/TM1637_datasheet.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_4-Digit_Display -->
