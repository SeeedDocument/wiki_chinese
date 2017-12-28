---
title: Grove - Touch Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Touch-Sensor-p-747.html
oldwikiname: Grove_-_Touch_Sensor
prodimagename: Grove-Touch_Sensor.jpg
wikiurl: http://seeed.wiki/Grove-Touch_Sensor
sku: 101020037
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Touch_Sensor/master/img/Grove-Touch_Sensor.jpg)

Grove - Touch Sensor 可以感受到你在抚摸过程中的压力。 当手指靠近时，它也可以检测电容的变化。 这意味着无论您的手指是直接触摸还是只是靠近，Grove - Touch Sensor 也会输出高电平。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.49560958exDLpw&id=45486442714)

产品特性
--------------


- 工作电压：2.0 - 5.5V
- 工作电流（Vcc = 3V）：1.5 - 3.0μA
- 工作电流（VDD = 3V）：3.5 - 7.0μA
- 输出响应时间：60 - 220mS
- 使用的芯片：TTP223-BA6

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

Platforms Supported
-------------------

**选项功能**

| AHLB                     | TOG         | LPMB       | MOTB         | SLRFTB          | RST       | Q           | OPDO            |
|--------------------------|-------------|------------|--------------|-----------------|-----------|-------------|-----------------|
| 输出有效高/低 |切换模式 | 电源模式 | Max. On Time | 取样时间长短 |复位引脚 | CMOS输出| Open Drain模式|
| V                        | V           | 0          | 1            | 1               | X         | V           | X               |
|有效高              | 不能    | LOW        | Infinite     | 1.6毫秒       | N/A       | Present     | N/A             |

示范
-------------

### 使用 Arduino

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Touch_Sensor/master/img/Touch_LED.jpg)
此演示将向您展示如何打开/关闭LED。

**演示代码:**

```
const int TouchPin=9;
const int ledPin=12;

void setup() {
    pinMode(TouchPin, INPUT);
    pinMode(ledPin,OUTPUT);
}

void loop() {
    int sensorValue = digitalRead(TouchPin);
    if(sensorValue==1)
    {
        digitalWrite(ledPin,HIGH);
    }
    else
    {
        digitalWrite(ledPin,LOW);
    }
}
```

### 使用 Raspberry Pi


1. 你应该有一个 raspberry pi 和一个 grovepi 或 grovepi +。
2. 您需要完成配置开发环境，否则遵循 [说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。
3. 硬件连接

     - 使用grove连接线将传感器插入 Grovepi 插座 **D4** 端口。

4. 导航到演示目录：

```
    cd yourpath/GrovePi/Software/Python/
```

   - 找到这行代码


```
    nano grove_touch_sensor.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Touch Sensor to digital port D4
    # SIG,NC,VCC,GND
    touch_sensor = 4

    grovepi.pinMode(touch_sensor,"INPUT")

    while True:
        try:
            print grovepi.digitalRead(touch_sensor)
            time.sleep(.5)

        except IOError:
            print "Error"

```

5.运行这个示例

        sudo python grove_touch_sensor.py


资源下载
---------

-   [Eagle Files](https://raw.githubusercontent.com/SeeedDocument/Grove-Touch_Sensor/master/res/Touch_sensor_Eagle_File.zip)
-   [TTP223pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-Touch_Sensor/master/res/TTP223.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Touch_Sensor -->
