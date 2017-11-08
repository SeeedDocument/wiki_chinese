---
title: Grove - Collision Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Collision-Sensor-p-1132.html
oldwikiname: Grove_-_Collision_Sensor
prodimagename: Grove_–_Collision_Sensor_photo.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020005 1.jpg
wikiurl: http://seeed.wiki/Grove-Collision_Sensor
sku: 101020005
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Collision_Sensor/master/img/Grove_–_Collision_Sensor_photo.jpg)

Grove - Collision Sensor可以检测碰撞和振动，当检测到时会输出一个低位脉冲信号。为了使输出信号更稳定准确，我们增加了电路以过滤噪音，因此正常的振动不会促发信号输出。传感器有较高的灵敏度，可用于电源的唤起和休眠管理。

它的工作电压是 5V，可以和标准的 Arduino/Seeeduino 5V 系统兼容。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.5bbf7f72OycBQY&id=45507110387&ns=1&abbucket=1#detail)

## 规格参数
-------------

-   电压 : 3.3/5V

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported
-------------------

## 操作示例
-------------

### 与 [Arduino](/Arduino "Arduino") 一起使用

根据发生碰撞时输出信号会发生变化，我们设计了这个演示 : 每当传感器检测到碰撞，LED 就会亮起来。这里的 LED 是作为一个受管设备，你可以参考演示来控制你的设备，如自行车灯。

步骤如下 :

1.使用 Grove 线缆将 collision sensor 连接到 Grove - Basic Shield 的数字端口 **2**，并将 LED 连接到引脚 **13**。

2.将 Grove - Basic Shield 插入 Arduino。

3.使用 USB 电缆将 Arduino/Seeeduino 连接到 PC。

4.复制并粘贴下面的代码到一个新的 Arduino 工程文件。并将其上传到您的 Arduino。

```c
// Test Grove - Collision Sensor
#define LED 13 //the onboard LED of Arduino or Seeeduino
#define COLLISION_SENSOR 2//collision sensor is connected with D2 of Arduino

void setup()
{
    pins_init();
}

void loop()
{
    if(isTriggered())
    {
        turnOnLED();
        delay(2000);
    }
    else turnOffLED();
}

void pins_init()
{
    pinMode(LED,OUTPUT);
    turnOffLED();
    pinMode(COLLISION_SENSOR,INPUT);
}

boolean isTriggered()
{
    if(!digitalRead(COLLISION_SENSOR))
    {
        delay(50);
        if(!digitalRead(COLLISION_SENSOR))
        return true;//the collision sensor triggers
    }
    return false;
}

void turnOnLED()
{
    digitalWrite(LED,HIGH);//the LED is on
}

void turnOffLED()
{
    digitalWrite(LED,LOW);//the LED is off
}
```

5.现在你可以检查 LED 的状态。 每当你在桌子上敲打手指时，LED 应该点亮。

您可以通过更改代码中的功能 delay(50) 来调整传感器灵敏度。

```c
if(!digitalRead(COLLISION_SENSOR))
{
    return true;//the collision sensor triggers
}
return false;
```
### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.完成配置开发环境，否则请遵循 [here](/GrovePiPlus)。

3.连接

-   将传感器用 Grove 线缆插入  Grovepi socket **D2**。

4.跳转到演示目录 :
```
cd yourpath/GrovePi/Software/Python/
```
-   演示代码如下 :

```
nano grove_collision_sensor.py   # "Ctrl+x" to exit #
```
```
import time
import grovepi

# Connect the Grove Collision Sensor to digital port D2
# SIG,NC,VCC,GND
collision_sensor = 2

grovepi.pinMode(collision_sensor,"INPUT")

while True:
    try:
        print grovepi.digitalRead(collision_sensor)
        time.sleep(.5)

    except IOError:
        print "Error"
```

5.运行代码。
```
sudo python grove_collision_sensor.py
```

## 资源下载
---------

-   **[Eagle文件]** [Grove - Collision Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Collision_Sensor/master/res/Grove-Collision_Sensor_eagle_file.zip)
-   **[芯片数据手册]** [MVS0608.02 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Collision_Sensor/master/res/DataSheet-MVS0608_02-v2_1.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Collision_Sensor -->
