---
title: Grove - RTC
category: Sensor
bzurl: https://seeedstudio.com/Grove-RTC-p-758.html
oldwikiname: Grove_-_RTC
prodimagename: Grove-RTC.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020013 1.jpg
surveyurl: https://www.research.net/r/Grove-RTC
sku: 101020013
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/img/Grove-RTC.jpg)

RTC 模块基于支持 I2C 协议的时钟芯片 DS1307。它采用锂电池 ( CR1225 )。 时钟/日历提供秒、分钟、小时、日期、月份和年份。 对于少于 31 天的月份月底的日期会自动调整，包括对闰年的更正。 时钟以 24 小时或 12 小时格式运行，具有 AM / PM 指示灯。 它可以在 2100 年之前有效。为了获得强劲的性能，您必须将 3 伏的 CR1225 锂电池放入电池座。 如果仅使用主电源，则模块可能无法正常工作，因为晶振可能不会振荡。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4de310cbc9GA9q&id=45552993984)

<div class="admonition note">
<p class="admonition-title">Note</p>
电池不包括在内
</div>

## 规格参数
---------
-   PCB 尺寸 : 2.0cm\*4.0cm
-   接口 : 2.0mm pitch pin header
-   IO 结构 : SCL,SDA,VCC,GND
-   ROHS : YES
-   VCC ：3.3~5.5V
-   逻辑高电平输入 ：2.2~VCC+0.3 V
-   逻辑低电平输入 ：-0.3~+0.8 V
-   电池电压 ：2.0~3.5 V

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported


## 入门指导

----
### With [Arduino](/Arduino "Arduino")
---

#### 连接

在这里，我们将通过一个简单的演示向您展示 Grove - RTC 的工作原理。 首先，您需要准备以下内容：

| Seeeduino V4 | Grove - RTC | Base Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/Grove-RTC_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.13eed3frK20RB&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.16d12d0b6ci0OF&id=45552993984)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.a12190dRaHSSr&id=520233320144)|

-   将模块连接到** Grove- Base Shield **的 **I2C** 接口。
-   将 Grove- Base Shield 插入 Arduino。
-   通过 USB 电缆将 Arduino 连接到 PC。

<div class="admonition note">
<p class="admonition-title">Note</p>
 为了获得强劲的性能，您必须将 3 伏的 CR1225 锂电池放入电池座。 如果仅使用主电源，则模块可能无法正常工作，因为晶振可能不会振荡。
</div>

![](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/arduino%20connection.jpg)

!!!Note
    如果我们没有底座，我们也可以直接连接 Grove-RTC 到 Arduino 板。 请按照下面的连接。

| Grove-RTC | Arduino  |
| :-------- | :------- |
| GND       | GND      |
| VCC       | VCC      |
| SDA       | A4       |
| SCL       | A5       |


#### 软件
---
-  下载 [RTC Library](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/res/RTC_Library.zip)。
- 请遵循 [how to install an arduino library](http://wiki.seeed.cc/How_to_install_Arduino_Library/) 步骤来安装库文件。
-   通过以下路径直接打开代码 : **File -> Example ->RTC->SetTimeAndDisplay**。

  ![](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/library%20example.jpg)


```     
#include <Wire.h>
#include "DS1307.h"

DS1307 clock;//define a object of DS1307 class
void setup()
{
    Serial.begin(9600);
    clock.begin();
    clock.fillByYMD(2013,1,19);//Jan 19,2013
    clock.fillByHMS(15,28,30);//15:28 30"
    clock.fillDayOfWeek(SAT);//Saturday
    clock.setTime();//write time to the RTC chip
}
void loop()
{
    printTime();
}
    /*Function: Display time on the serial monitor*/
void printTime()
{
    clock.getTime();
    Serial.print(clock.hour, DEC);
    Serial.print(":");
    Serial.print(clock.minute, DEC);
    Serial.print(":");
    Serial.print(clock.second, DEC);
    Serial.print("  ");
    Serial.print(clock.month, DEC);
    Serial.print("/");
    Serial.print(clock.dayOfMonth, DEC);
    Serial.print("/");
    Serial.print(clock.year+2000, DEC);
    Serial.print(" ");
    Serial.print(clock.dayOfMonth);
    Serial.print("*");
    switch (clock.dayOfWeek)// Friendly printout the weekday
    {
        case MON:
        Serial.print("MON");
        break;
        case TUE:
        Serial.print("TUE");
        break;
        case WED:
        Serial.print("WED");
        break;
        case THU:
        Serial.print("THU");
        break;
        case FRI:
        Serial.print("FRI");
        break;
        case SAT:
        Serial.print("SAT");
        break;
        case SUN:
        Serial.print("SUN");
        break;
    }
    Serial.println(" ");
}
```

-   设定时间，将函数参数更改为当前日期/时间。 请注意参数格式。

```
clock.fillByYMD(2013,1,19);//Jan 19,2013
clock.fillByHMS(15,28,30);//15:28 30"
clock.fillDayOfWeek(SAT);//Saturday
```

-   上传代码。
-   打开串口监视结果。

![](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/arduino%20result.png)


### With Raspberry Pi
---

#### 连接

- 首先，我们需要准备以下内容:

|  Raspberry pi | Grove - RTC | Grovepi+ |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/Grove-RTC_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4118806ccpMFM&id=528322046763)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7a3f53cdA1LtDQ&id=45552993984)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.8021e38ypeiLD&id=45506190895)|


-   按照 [instruction](http://wiki.seeed.cc/GrovePi_Plus/) 配置开发环境。
-   使用 grove cable 将传感器插入 grovepi+ socket i2c-x(1~3)。

![](https://github.com/SeeedDocument/Grove-RTC/raw/master/img/pi%20connenction.jpg)

#### 软件
-----

**演示 1: Grove_i2c_rtc**

- 导航到演示目录 Navigate to the demos' directory:
```
    cd yourpath/GrovePi/Software/Python/
```
-   找到代码。
```
    nano grove_i2c_rtc.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Real Time Clock to any I2C port eg. I2C-1
    # Can be found at I2C address 0x68
    # SCL,SDA,VCC,GND

    while True:
        try:
            print grovepi.rtc_getTime()
            time.sleep(.5)

        except IOError:
            print "Error"
```

- 运行演示。
```
    sudo python grove_i2c_rtc.py
```

- 结果如下 :

  ![](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/img/Grovepi_i2c_rtc_00.png)

**演示 2: Grove_rtc**

  - 使用此演示显示共有的时间

```
    /*
     * Grove-RTC.py
     * Demo for Raspberry Pi
     *
     * Copyright (c) 2014 seeed technology inc.
     * Website    : www.seeed.cc
     * Author     : Lambor
     * Create Time: Nov 2014
     * Change Log :
     *
     * The MIT License (MIT)
     *
     * Permission is hereby granted, free of charge, to any person obtaining a copy
     * of this software and associated documentation files (the "Software"), to deal
     * in the Software without restriction, including without limitation the rights
     * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     * copies of the Software, and to permit persons to whom the Software is
     * furnished to do so, subject to the following conditions:
     *
     * The above copyright notice and this permission notice shall be included in
     * all copies or substantial portions of the Software.
     *
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

    #!/usr/bin/python
    import time
    import smbus


    bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)   

    class DS1307():     
        def __init__(self):
            self.MON = 1
            self.TUE = 2
            self.WED = 3
            self.THU = 4
            self.FRI = 5
            self.SAT = 6
            self.SUN = 7
            self.DS1307_I2C_ADDRESS = 0x68

            print 'begin'

        def decToBcd(self, val):
            return ( (val/10*16) + (val%10) )

        def bcdToDec(self,  val):
            return ( (val/16*10) + (val%16) )

        def begin(self, news):
            print news

        def startClock(self):   
            bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
            self.second = bus.read_byte(self.DS1307_I2C_ADDRESS) & 0x7f
            bus.write_byte_data(self.DS1307_I2C_ADDRESS, 0x00, self.second)

            print 'startClock..'

        def stopClock(self):                        
            bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
            self.second = bus.read_byte(self.DS1307_I2C_ADDRESS) | 0x80
            bus.write_byte_data(self.DS1307_I2C_ADDRESS, 0x00, self.second)         

            print 'stopClock..'

        def setTime(self):
            data = [self.decToBcd(self.second), self.decToBcd(self.minute), \
                    self.decToBcd(self.hour), self.decToBcd(self.dayOfWeek), \
                    self.decToBcd(self.dayOfMonth), self.decToBcd(self.month), \
                    self.decToBcd(self.year)]

            bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
            bus.write_i2c_block_data(self.DS1307_I2C_ADDRESS,0x00,data)

            print 'setTime..'

        def getTime(self):
            bus.write_byte(self.DS1307_I2C_ADDRESS, 0x00)
            data = bus.read_i2c_block_data(self.DS1307_I2C_ADDRESS,0x00)
            #A few of these need masks because certain bits are control bits
            self.second = self.bcdToDec(data[0] & 0x7f)
            self.minute = self.bcdToDec(data[1])
            self.hour = self.bcdToDec(data[2] & 0x3f)  #Need to change this if 12 hour am/pm
            self.dayOfWeek = self.bcdToDec(data[3])
            self.dayOfMonth = self.bcdToDec(data[4])
            self.month = self.bcdToDec(data[5])
            self.year = self.bcdToDec(data[6])

            print 'getTime..'

        def fillByHMS(self, _hour,  _minute,  _second):
            self.hour = _hour
            self.minute = _minute
            self.second = _second

            print 'fillByHMS..'

        def fillByYMD(self, _year,  _month,  _day):     
            self.year = _year - 2000
            self.month = _month;
            self.dayOfMonth = _day

            print 'fillByYMD..'

        def fillDayOfWeek(self,  _dow):     
            self.dayOfWeek = _dow

            print 'fillDayOfWeek..'

    if __name__ == "__main__":
        clock = DS1307()
        clock.fillByYMD(2015,3,5)
        clock.fillByHMS(12,42,30)
        clock.fillDayOfWeek(clock.THU)  
        clock.setTime()
        while True:     
            clock.getTime()
            print clock.hour, ":", clock.minute, ":", \
                    clock.second, " ", clock.dayOfMonth, "/", \
                    clock.month, "/", clock.year,"  ", "weekday", \
                    ":", clock.dayOfWeek            
            time.sleep(1)
```

- 在上面创建 **grove_rtc.py** 和复制代码.

- 运行代码
```
    sudo python grove_rtc.py
```

- 结果如下 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/img/Grovepi_i2c_rtc_01.png)
### Without Grove Shield
--------------
#### 连接
没有Grove Shield，您可以通过将引脚分配增加到 Grove 接口来实现连接到 Arduino。

| grove | Arduino |
|-------|---------|
| GND   | GND     |
| VCC   | VCC     |
| SDA   | SDA     |
| SCL   | SCL     |

## 资源下载
---------

- **[Eagle文件]** [Grove-RTC in Eagle format](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/res/Real_Time_Clock.zip)
- **[PDF文件]** [Grove-RTC Schematic in PDF format](https://github.com/SeeedDocument/Grove-RTC/raw/master/res/Grove%20-%20RTC%20v1.1%20Sch.pdf)
- **[PDF文件]** [Grove-RTC PCB in PDF format](https://github.com/SeeedDocument/Grove-RTC/raw/master/res/Grove%20-%20RTC%20v1.1%20PCB.pdf)
- **[库文件]**[Github repository for RTC](https://github.com/Seeed-Studio/RTC_DS1307/archive/master.zip)
- **[芯片数据手册]** [DS1307 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/res/DS1307.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_RTC -->
