---
title: Grove - Temperature&Humidity Sensor (High-Accuracy &Mini) v1.0
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Temperature&Humidity-Sensor-(High-Accuracy-&-Mini)-p-1921.html
oldwikiname: Grove_-_Tempture&Humidity_Sensor_(High-Accuracy_&Mini)_v1.0
prodimagename: Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-TemptureAndHumidity_Sensor_High_Accuracy_AndMini-v1.0/
sku: 101020074
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/master/img/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-.jpg)

这是一个多功能传感器，可同时给你温度和相对湿度的信息。 它采用 TH02 sensor 进行测量，可满足一般需求的项目。 当环境湿度在 0-80％RH 和 0-70°C 之间的温度条件下，它可以提供可靠的读数，能够满足大多数家庭和日常应用的需求。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.50ef8c5fmllnAf&id=45506586247)

产品参数
--------------

- 工作电压范围
     - （3.3V〜5V）
- 低功耗
     - 在 RH 转换期间为350μA
- 0〜100％RH工作范围
- 测量范围：
     - 湿度：0％ - 80％RH
     - 温度：0〜70℃
- 准确性：
     - 湿度：±4.5％RH
     - 温度：±0.5°C
- 具有 I2C 主机接口
- 具有长期运行的稳定性

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

创意应用
------------


- 工业HVAC / R
- 恒温器/湿度计
- 微环境/数据中心

示范
-------------

该演示将向您展示如何从该 Grove - Temperature&Humidity Sensor (High-Accuracy &Mini) Sensor 读取温度和湿度信息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/master/img/Temperature_Sensor-xin.jpg)
将 Temperature and Humidity sensor 连接到 Grove - Base Shield 的模拟端口 **I2C**。

-   下载  [Grove_Temper_Humidity_TH02 库](https://github.com/Seeed-Studio/Grove_Temper_Humidity_TH02) 并且安装这个库到 Arduino 库文件。

```
/*
 * Demo name  ?: TH02_dev demo
 * Usage      ?: DIGITAL I2C HUMIDITY AND TEMPERATURE SENSOR
 * Author     ?: Oliver Wang from Seeed Studio
 * Version    ?: V0.1
 */

#include <TH02_dev.h>
#include "Arduino.h"
#include "Wire.h"

void setup()
{
    Serial.begin(9600);        // start serial for output

    Serial.println("****TH02_dev demo by seeed studio****\n");
    /* Power up,delay 150ms,until voltage is stable */
    delay(150);
    /* Reset HP20x_dev */
    TH02.begin();
    delay(100);

    /* Determine TH02_dev is available or not */
    Serial.println("TH02_dev is available.\n");
}


void loop()
{
    float temper = TH02.ReadTemperature();
    Serial.println("Temperature: ");
    Serial.print(temper);
    Serial.println("C\r\n");

    float humidity = TH02.ReadHumidity();
    Serial.println("Humidity: ");
    Serial.print(humidity);
    Serial.println("%\r\n");
    delay(1000);
}
```


将其上传到您的 Arduino 板上，打开串行监视器，观察环境的温度和相对湿度信息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/master/img/Result_Picture1.jpg)

资源下载
---------

-   [Grove - Temperature&Humidity Sensor (High-Accuracy & Mini) V1.0 sch pcb](https://raw.githubusercontent.com/SeeedDocument/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/master/res/Grove-TemperatureAndHumidity_Sensor-High-Accuracy_And_Mini-V1.0_sch_pcb.zip)
-   [TH02_SENSOR.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0/master/res/TH02_SENSOR.pdf)
-   [Grove_Temper_Humidity_TH02 library](https://github.com/Seeed-Studio/Grove_Temper_Humidity_TH02)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Tempture&Humidity_Sensor_(High-Accuracy_&Mini)_v1.0 -->
