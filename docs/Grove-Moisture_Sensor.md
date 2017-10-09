---
title: Grove - Moisture Sensor
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Moisture-Sensor-p-955.html
oldwikiname: Grove - Moisture Sensor
prodimagename: Moisture_sensor_.jpg
surveyurl: https://www.research.net/r/grove-moisture-sensor
sku: 101020008
---
---
![](https://github.com/SeeedDocument/Grove_Moisture_Sensor/raw/master/images/Moisture_sensor_.jpg)

这个Moisture Senor可以用于检测土壤的水分，或者判断传感器周围是否有水分，让您花园里的植物在渴望时能够伸出援手。 该传感器非常易于使用，您只需将它插入土壤并读取数据即可。 使用这个传感器，您可以制作一个小工程，让植物给您发送消息，如“我现在口渴，请给我一些水”。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11DbSHW8&id=520170918975)

## 产品特性
---
- 能够通过土壤电阻率，测量出的土壤水分含量
- 方便使用
- 2.0 cm X 6.0 cm 的grove 模块

!!!Tip
    关于Grove模块的更多细节请参考 [Grove_System](http://seeed.wiki/Grove_System/)

## 规格参数
---
|项目|使用环境|最小|标准|最大|单位|
|---|---|---|---|---|---|
|电压|-|3.3|-|5|V|
|电流|-|0|-|35|mA|
|输出数值|在干燥的土壤中<br>在潮湿的土壤中<br>在水中|0<br>300<br>700<br>|-|300<br>700<br>950|-|

## 创意应用
---
- 应用在植物园林中
- 湿度检测
- 浓度检测


## 使用方法
---
**使用Arduino**

这是可以用于检测土壤水分的moisture sensor的使用说明。 当检测到土壤水分消失时，传感器输出值会降低。 您可以观察传感器输出的结果知道植物是否需要水。 下面展示这个传感器在感应土壤水分方面的简单应用。

- 使用4针的Grove连接线将此模块连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的 **A0** 的模拟端口，，然后将传感器插入土壤或放置在任何你想要的地方。

- 将Grove-Base Shield插入Arduino Seeeduino，并通过USB数据线将Arduino连接到PC。

硬件安装如下图所示：

![](https://github.com/SeeedDocument/Grove_Moisture_Sensor/raw/master/images/518px-Moisture1.jpg)

!!!Note
    该传感器不会因为控制电路与水接触而失效，但是可能容易在探针之间发生电解腐蚀，因此不适合一直留在水里或在室外使用。

- 将下面的代码复制并粘贴到新的Arduino编辑页面上

```c
// Test code for Grove - Moisture Sensor
int sensorPin = A0; // select the input pin for the potentiometer
int sensorValue = 0; // variable to store the value coming from the sensor7

void setup() {
    // declare the ledPin as an OUTPUT:
    Serial.begin(9600);
}
void loop() {
    // read the value from the sensor:
    sensorValue = analogRead(sensorPin);
    Serial.print("sensor = " );
    Serial.println(sensorValue);
    delay(1000);
}
```

- 如果您不清楚怎么下载代码到您的板子里，请点击[这里](http://seeed.wiki/Upload_Code/)。

![](https://github.com/SeeedDocument/Grove_Moisture_Sensor/raw/master/images/in%20differen%20conditions.jpg)

**使用TI LaunchPad**


照顾你的植物（使用Moisture Sensor）

下面的示例展示了一个在土壤中检测水分的简单应用。通过观察传感器的输出结果，您可以知道植物是否需要水

![](https://github.com/SeeedDocument/Grove_Moisture_Sensor/raw/master/images/Moisture.jpg)

```c
/*
  Moisture-Sensor
  The following sketch demonstrates a simple application of sensing
  the moisture of the soil. You can know whether a plant needs water
  or not by observing the results that the sensor outputs.
  The circuit:
    * Moisture-Sensor attached to pin 24 (J6 plug on Grove Base BoosterPack)
    * one side pin (either one) to ground
    * the other side pin to +VCC
    * LED anode (long leg) attached to RED_LED
    * LED cathode (short leg) attached to ground
  - NOTE:
    This example code is in the public domain.
    http://seeedstudio.com/wiki/Grove_-_Moisture_Sensor
*/
#include "TM1637.h"
/* Macro Define */
#define CLK 39              /* 4-digital display clock pin */
#define DIO 38              /* 4-digiral display data pin */
#define BLINK_LED RED_LED   /* blink led */
#define MOISTURE_PIN 24     /* pin of moisture sensor */
#define THRESHOLD_VALUE 300 /* threshold for watering the flowers */
#define ON HIGH             /* led on */
#define OFF LOW             /* led off */
#define _handle_led(x) digitalWrite(BLINK_LED, x) /* handle led */

/* Global Varibles */
TM1637 tm1637(CLK, DIO);    /* 4-digital display object */
int analog_value = 0;       /* varible to store the value coming from rotary angle
sensor */
int8_t bits[4] = {0};       /* array to store the single bits of the value */
/* the setup() method runs once, when the sketch starts */
void setup() {
/* Initialize 4-digital display */
    tm1637.init();
    tm1637.set(BRIGHT_TYPICAL);
/* declare the red_led pin as an OUTPUT */
    pinMode(BLINK_LED, OUTPUT);
}
/* the loop() method runs over and over again */
void loop() {
    analog_value = analogRead(MOISTURE_PIN); /* read the value from the sensor */
/* if the value is smaller than threshold, turn on led */
    if(analog_value < THRESHOLD_VALUE) {
        _handle_led(ON);
    } else {
        _handle_led(OFF);
    }
    memset(bits, 0, 4); /* reset array when we use it */
    for(int i = 3; i >= 0; i--) {
/* get single bits of the analog value */
        bits[i] = analog_value % 10;
        analog_value = analog_value / 10;
        tm1637.display(i, bits[i]); /* display by 4-digital display */
    }
    delay(200);
}
```


**使用 Raspberry Pi**
1. 你应该准备一个Raspberry Pi和一个grove pi或grove pi +
2. 您需要完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。
3. 硬件连接
- 用grove连接线将传感器插入grove pi的 **A0** 端口。
4. 导航到演示目录

```
cd yourpath/GrovePi/Software/Python/
```

找到这行代码

```python
nano grove_moisture_sensor.py # "Ctrl+x" to exit #
import time
import grovepi
# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0
while True:
try:
print grovepi.analogRead(sensor)
time.sleep(.5)
except KeyboardInterrupt:
break
except IOError:
print "Error
```

5. 运行这个示例

```
sudo python grove_moisture_sensor.py
```

## 资源下载
---
- [202000089_PCBA-Grove Moisture sensor V1.3_schemic file](https://github.com/SeeedDocument/Grove_Moisture_Sensor/raw/master/resources/202000089_PCBA-Grove%20Moisture%20sensor%20V1.3_schemic%20file.zip)
