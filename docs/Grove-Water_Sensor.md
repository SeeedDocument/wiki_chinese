---
title: Grove - Water Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Water-Sensor-p-748.html
oldwikiname: Grove_-_Water_Sensor
prodimagename: Grove-Water_Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Water_Sensor
sku: 101020018
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Water_Sensor/master/img/Grove-Water_Sensor.jpg)

Water Sensor 模块是 Grove 系统的一部分。它通过测量电导率指示传感器是否干燥，潮湿或完全浸入水中。传感器走线使用 1MΩ 上拉电阻。电阻将拉高传感器的数值，直到水将传感器的信号线短接到地。此电路将使用 Arduino 的数字 I/O 引脚，您也可以使用模拟引脚来检测地和传感器信号线之间水的接触量。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.39.79618f20Awu3v4&id=45534561319)


## 产品特性
--------

-   Grove 兼容的接口
-   低功耗
-   2.0cm x 2.0cm Grove 模块
-   灵敏度高

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 创意应用
------------------

-   降雨检测
-   液体泄漏
-   箱体溢出探测器

<div class="admonition caution">
<p class="admonition-title">Caution</p>
此设备仅适用于教育和业余爱好应用程序。不能用于发生故障时可能导致财产损失或人身安全的应用。
</div>

## 规格参数
-------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
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
4.75
</td>
<td>
5.0
</td>
<td>
5.25
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
电流
</th>
<td colspan="3">
&lt;20
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
工作温度
</th>
<td>
10
</td>
<td>
-
</td>
<td>
30
</td>
<td>
℃
</td>
</tr>
<tr align="center">
<th scope="row">
工作湿度 (不结露)
</th>
<td>
10
</td>
<td>
-
</td>
<td>
90
</td>
<td>
 %
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 入门指导
-----

### 与 [Arduino](/Arduino "Arduino") 一起使用

使用任何数字引脚将模块连接到 Basic board。您可以获得信号引脚的值。裸导线上有水时，得到 LOW。 否则，将是 HIGH。

以下草图演示了使用 Water sensor 控制蜂鸣器的简单应用。如下图所示， Water sensor 连接到 **Grove - Base Shield** 的数字端口 **8**，蜂鸣器连接到数字端口 **12**。当裸导线上有水时，**SIG** 引脚输出一个 LOW 电平。然后蜂鸣器响起。硬件安装如下 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Water_Sensor/master/img/Water_Buzzer.jpg)

-   然后使用 USB 电缆将 Arduino 连接到 PC。
-   复制并粘贴下面的代码到一个新的 Arduino 草图程序。

```c
/*macro definition of water sensor and the buzzer*/
#define WATER_SENSOR 8
#define BUZZER 12

void setup()
{
    pins_init();
}
void loop()
{
    if(isExposedToWater())
    soundAlarm();
}

void pins_init()
{
    pinMode(WATER_SENSOR, INPUT);
    pinMode(BUZZER, OUTPUT);
}

/************************************************************************/
/*Function: When the sensor is exposed to the water, the buzzer sounds  */
/*          for 2 seconds.                                              */
/************************************************************************/
void soundAlarm()
{
    for(uint8_t i = 0;i < 20;i ++)
    {
        digitalWrite(BUZZER, HIGH);
        delay(50);
        digitalWrite(BUZZER, LOW);
        delay(50);
    }
}

/************************************************************************/
/*Function: Determine whether the sensor is exposed to the water        */
/*Parameter:-void                                                       */
/*Return:   -boolean,if it is exposed to the water,it will return true. */
/************************************************************************/
boolean isExposedToWater()
{
    if(digitalRead(WATER_SENSOR) == LOW)
    return true;
    else return false;
}
```

-   上传代码。

-   当传感器受潮或完全浸入水中时，蜂鸣器响起。 快试试吧 !

### 与 Raspberry 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi or Grovepi+.

2.配置开发环境，如果没有完成请按照 [这里](/GrovePiPlus) 进行配置。

3.连接

-   用 Grove 线缆将传感器插入Grovepi socket **D2**。

4.跳转到演示目录
```
cd yourpath/GrovePi/Software/Python/
```

-   代码如下 :
```
nano grove_water_sensor.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi

# Connect the Grove Water Sensor to digital port D2
# SIG,NC,VCC,GND
water_sensor = 2

grovepi.pinMode(water_sensor,"INPUT")

while True:
    try:
        print grovepi.digitalRead(water_sensor)
        time.sleep(.5)

    except IOError:
        print "Error"
```

5.运行代码。
```
sudo python grove_water_sensor.py
```

## 资源下载
---------

-   **[Eagle文件]** [Water Sensor Eagle Files](https://raw.githubusercontent.com/SeeedDocument/Grove-Water_Sensor/master/res/Water_sensor.zip)
-   **[其他资源]** [Demo code for Water Sensor](https://github.com/Seeed-Studio/Grove_Water_Sensor)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Water_Sensor -->
