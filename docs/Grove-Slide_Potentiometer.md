---
title: Grove - Slide Potentiometer
category: Sensor
bzurl: https://seeedstudio.com/Grove-Slide-Potentiometer-p-1196.html
oldwikiname: Grove_-_Slide_Potentiometer
prodimagename: Slide Potentiometer.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/Slide Potentiometer.jpg
wikiurl: http://seeed.wiki/Grove-Slide_Potentiometer
sku: 101020036
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Sliding1.JPG)

The Grove - Slide Potentiometer 模块内有一个最大阻值为 10KΩ 的线性可变电阻，当您把控制杆从一端滑到另外一端，输出电压值在 0 到输入的 VCC 之间变化。它通过标准四线 Grove 线缆连接到其他 Grove 模块，其中 3 根分别连到了 **OUT** (引脚 **1**), **Vcc** (引脚 **3**) 和 **GND** (引脚 **4**)，剩下的那根线(引脚 **2**)连到了绿色的 LED 灯上，可以用它来表示电位计阻值的变化。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.7f561822qVySjY&id=45554612830)

## 产品特性
--------

-   滑动长度 30mm
-   阻值线性变化
-   通用 Grove 接口

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 创意应用
-----------------

这里有一些供您参考的项目

| **Arduino BoomBox**                                                  | **Arduino BeatBox**                                                    |
|----------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Recipe-Arduino_BoomBox.jpg)| ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Recipe-Arduino_BeatBox.jpg)  |
| [点击制作!](http://www.seeed.cc/project_detail.html?id=171)       | [点击制作!](http://www.seeed.cc/project_detail.html?id=187)         |


## 规格参数
--------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th>
最小值
</th>
<th>
典型值
</th>
<th>
最大值
</th>
</tr>
<tr align="center">
<th scope="row">
电压 (直流)
</th>
<td>
3.3V
</td>
<td>
5.0V
</td>
<td>
30V
</td>
</tr>
<tr align="center">
<th scope="row">
电流
</th>
<td>
-
</td>
<td>
-
</td>
<td>
30mA
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
24mm x60mm
</td>
</tr>
<tr align="center">
<th height="22" scope="row">
净重
</th>
<td colspan="3">
8.6g
</td>
</tr>
<tr align="center">
<th height="22" scope="row">
往复运动寿命
</th>
<td colspan="3">
&gt;15,000 cycles
</td>
</tr>
<tr align="center">
<th height="22" scope="row">
总电阻
</th>
<td colspan="3">
10KΩ
</td>
</tr>
<tr align="center">
<th height="22" scope="row">
行程长度
</th>
<td colspan="3">
30mm
</td>
</tr>
<tr align="center">
<th height="22" scope="row">
总电阻容差
</th>
<td colspan="3">
+/- 20%
</td>
</tr>
</table>


## Platforms Supported
-------------------

## 入门指导
---------------

#### 作为一个可调电阻

如下图所示，Grove - Slide Potentiometer 可用作任何 MCU 控制或独立项目中的滑动电位计。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Sliding_justr.JPG)

### 单独使用

按照以下步骤使构建用此模块但不使用任何微控制器板的 Grove 电路 :

1.  将 Grove - Slide Potentiometer 模块连接到电路的输入端 (电源模块左侧)。在电路的输出端，您可以使用一系列用户界面模块 (Grove - Red LED, Grove - LED String Light, Grove - Mini Fan, Grove - Buzzer, Grove - Recorder etc)。
2.  完成后重启电路。
3.  Grove - Slide Potentiometer 模块现在可以用来触发输出。例如 :

    -   当与 Grove - Red LED 输出模块配合使用时，请注意随着滑块从 GND 移动到 Vcc，LED的亮度会增加。在Vcc时，电阻值最小，LED最亮。 Grove - Slide Potentiometer 与 Grove - LED String Light 模块一起使用时，可以看到相同的现象 : 通过将滑块滑向 Vcc 施加的电压越多，LED 就越亮。
    -   同样，您可以使用 Grove - Slide Potentiometer 来改变 Grove - Mini Fan 的速度或 Grove - Buzzer 模块发声的频率

在选择电源模块方面，您可以使用 Grove - USB Power 模块或 Grove - DC Jack Power 模块来构建独立的 Grove 电路。

### 与 [Arduino](/Arduino "Arduino") 一起使用

#### 作为分压器

按照以下步骤使 Grove - Slide Potentiometer 模块起到分压器的作用 :

1.1.将模块与 [Arduino](/Arduino "Arduino") 或 [Seeeduino](/Seeeduino_v4.2 "Seeeduino") 配合使用时，并使用指定的 Grove 接口(例如模拟端口 **A0**，如下所示)将 Grove - Slide Potentiometer 模块连接到 Grove - Base Shield。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Sliding2.JPG)

2.通过 USB 线缆将 MCU 控制板连接到 PC。

3.上传如下代码。

```
int adcPin = A0; // select the input pin for the potentiometer
int ledPin = A1; // select the pin for the LED
int adcIn = 0;   // variable to store the value coming from the sensor
void setup()
{
    Serial.begin(9600); // init serial to 9600b/s
    pinMode(ledPin, OUTPUT); // set ledPin to OUTPUT
    Serial.println("Sliding Potentiometer Test Code!!");
}
void loop()
{
    // read the value from the sensor:
    adcIn = analogRead(adcPin);
    if(adcIn &gt;= 500) digitalWrite(ledPin,HIGH);  // if adc in &gt; 500, led light
    else digitalWrite(ledPin, LOW);
    Serial.println(adcIn);
    delay(100);
}
```

4.打开串口监视器。可以看到来自 ADC 的一些数据。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Sliding_com.jpg)

5.使控制杆往复运动，串口数据将相应地改变。当输出电阻超过某个预设值时，板载 LED 指示灯会亮起。

#### 作为 HID 设备

滑动电位器是有效的人机交互设备 (HID)，并且可以用在例如无线电遥控玩具车的无线电控制器中。下面的图片显示了控制面板上的两个 Grove - Slide Potentiometer - 一个控制左轮的速度，另一个控制右轮的速度。现在，您可以更改两个电机的速度并观察现象。您会看到，如果您让右侧车轮比左侧车轮旋转得快，车子会向右转；而如果您让左侧车轮比右侧车轮旋转得快，车子会向左转。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/img/Car.JPG)

### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.完成配置开发环境，否则请遵循 [here](/GrovePiPlus)。

3.连接

-   将传感器用 Grove 线缆插入  Grovepi 插口 **A0**。

4.跳转到演示目录 :
```
    cd yourpath/GrovePi/Software/Python/
```

-   演示代码如下 :
```
nano grove_slide_potentiometer.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi

# Connect the Grove Slide Potentiometer to analog port A0
# OUT,LED,VCC,GND
slide = 0   # pin 1 (yellow wire)

# The device has an onboard LED accessible as pin 2 on port A0
# OUT,LED,VCC,GND
led = 1     # pin 2 (white wire)

grovepi.pinMode(slide,"INPUT")
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = grovepi.analogRead(slide)

        # Illuminate onboard LED
        if sensor_value > 500:
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)

        print "sensor_value =", sensor_value

    except IOError:
        print "Error"
```

5.运行代码。
```
sudo python grove_slide_potentiometer.py
```

## 资源下载
---------

-   **[Eagle文件]** [Sliding Potentiometer Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/res/Sliding_Potentiometer.rar)
-   **[原理图PDF]** [Sliding Potentiometer in PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/res/Sliding_protentiometer_sch.pdf)
-   **[数据手册]** [Sliding Potentiometer datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Slide_Potentiometer/master/res/Sliding_potentiometer_datasheet.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Slide_Potentiometer -->
