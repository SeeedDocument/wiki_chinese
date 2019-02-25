---
name: Grove - Ultrasonic Ranger
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Ultrasonic-Ranger-p-960.html
oldwikiname: Grove - Ultrasonic Ranger
prodimagename: 350px-Ultrasonic_Ranger.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Ultrasonic_Ranger
sku: 101020010
tags: io_3v3, io_5v, plat_duino, plat_pi

---
![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/350px-Ultrasonic_Ranger.jpg)

Grove - Ultrasonic传感器是一种非接触式距离测量模块，工作在40KHz，适用于需要对中等距离进行测量的项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11bTW76G&id=45550924107)

## 产品更新
为了提高在使用一些低压主板时的电源稳定性，我们对此产品做了一些更新。这些更新包括：

- 增加电容C14
- 重新设计布局，使其更加整洁
- 兼容3.3V电压系统

这里我们通过两张图片来显示不同之处：

![](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/front.jpg)

![](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/back.jpg)

!!!注意
    请注意，新版本与旧版本共享相同的sku，所以您仍然可以使用旧的sku：101020010进行购买，我们将给您发送新版本。


## 规格参数
---
|参数    |	值/范围|
|:------|:------------------|
|工作电压|	3.2~5.2V|
|工作电流|	8mA|
|超声波频率|	40kHz|
|测量范围|	2-350cm|
|精度|	1cm|
|输出|PWM|
|尺寸|50mm X 25mm X 16mm|
|重量|13g|


!!!小提示
    关于Grove模块的更多细节请参考[Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

支持平台
-------------------

## 入门指导
---
### 使用Arduino
#### 物理连接

在这里，我们将通过一个简单的演示向您展示这个Grove - Ultrasonic Ranger 如何运作。 首先，您需要准备以下内容：

| Seeeduino V4 | Grove - Ultrasonic Ranger | Base Shield |Grove - LCD RGB Backlight |
|--------------|-------------|-----------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/Ultrasonic_Ranger_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/img/grove-lcd%20rgb_s.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11VmLc2i&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11RvgUQ3&id=45550924107)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11c2CnFR&id=520233320144)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11F8VXfy&id=45475311124)|

-   将Ultrasonic Ranger连接到Grove-Base Shield的 **D7** 端口。
-   将LCD RGB Backlight连接到Grove-Base Shield的 **I2C** 端口。
-   将Grove - Base Shield插入到Arduino中。
-   通过USB线将Arduino连接到PC。

![](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/arduino%20connection.jpg)

#### 软件代码

- 从Github下载[ UltrasonicRanger Library](https://github.com/Seeed-Studio/Grove_Ultrasonic_Ranger/archive/master.zip)和[  Grove - LCD RGB Backlight Library ](https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip) 。
-  如果您不知道如何安装库，请参阅 [如何安装库](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/)

```
#include <Wire.h>
#include "rgb_lcd.h"
#include "Ultrasonic.h"

rgb_lcd lcd;
Ultrasonic ultrasonic(7);

const int colorR = 0;
const int colorG = 255;
const int colorB = 0;


void setup()
{
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);
}

void loop()
{   
    long RangeInCentimeters;
    RangeInCentimeters = ultrasonic.MeasureInCentimeters();
    delay(150);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("The distance:");
    lcd.setCursor(0,1) ;
    lcd.print(RangeInCentimeters,DEC);
    lcd.setCursor(5,1) ;
    lcd.print("cm");
}
```
- 将代码复制到Arduino并上传。我们可以看到LCD上的距离显示。

### 使用 TI LaunchPad

#### 硬件连接

超声波传感器(Ultrasonic Ranger Sensor)

该示例显示如何使用超声波传感器测量与障碍物的距离，并在4位数字显示屏（厘米）上显示该值。

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/600px-Ultrasonic.jpg)

#### 软件代码
```
/*
 Ultrasonic-Ranger to 4-digit-display
 Measure the distance to obstacles in front and display the value on
 4-digital-display

 The circuit:
 * Ultrasonic Ranger attached to SPI plug on Grove Base BoosterPack
 * one side pin (either one) to ground
 * the other side pin to +VCC
 * LED anode (long leg) attached to RED_LED
 * LED cathode (short leg) attached to ground

 * Note:  


 This example code is in the public domain.

 http://www.seeedstudio.com/wiki/Grove_-_Ultrasonic_Ranger
 */

#include "TM1637.h"
#include "Ultrasonic.h"
/* Macro Define */
#define CLK               40                  /* 4-digital display clock pin */
#define DIO               39                 /* 4-digital display data pin */
#define BLINK_LED         RED_LED            /* blink led */
#define ULTRASONIC_PIN    38                  /* pin of the Ultrasonic Ranger */

/* Global Variables */
TM1637 tm1637(CLK, DIO);                  /* 4-digital display object */
Ultrasonic ultrasonic(ULTRASONIC_PIN);    /* Ultrasonic Ranger object */
int distance = 0;                         /* variable to store the distance to obstacles in front */
int blink_interval = 0;                   /* led delay time */
int8_t bits[4] = {0};                     /* array to store the single bits of the value */

/* the setup() method runs once, when the sketch starts */
void setup() {

    /* Initialize 4-digital display */
    tm1637.init();
    tm1637.set(BRIGHT_TYPICAL);

    /* declare the red_led pin as an OUTPUT */
    pinMode(RED_LED, OUTPUT);

}

/* the loop() method runs over and over again */
void loop() {   

    distance = ultrasonic.MeasureInCentimeters();   /* read the value from the sensor */   

    memset(bits, 0, 4);                             /* reset array when we use it */
    for(int i = 3; i >= 0; i--) {
        /* get single bits of the analog value */
        bits[i] = distance % 10;
        distance = distance / 10;  
        tm1637.display(i, bits[i]);                 /* display by 4-digital display */
    }
    delay(100);
}
```

### 使用 [Raspberry Pi](http://www.seeedstudio.com/wiki/GrovePi%2B)

#### 硬件连接
| Raspberry pi | Grove - Ultrasonic Ranger | GrovePi_Plus |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/Ultrasonic_Ranger_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11WcupfX&id=528322046763)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11RvgUQ3&id=45550924107)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11twVFej&id=45506190895)|

- 按照 [说明](http://wiki.seeed.cc/GrovePi_Plus/)  配置开发环境。
- .将超声波传感器连接到端口 ** D4 ** 并运行下面的程序。 它将在终端上的显示距离信息，如下图所示。

![](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/img/pi%20connection.jpg)



#### 软件代码

```python
# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4

while True:
    try:
        # Read distance value from Ultrasonic
        print ultrasonicRead(ultrasonic_ranger)

    except TypeError:
        print "Error"
    except IOError:
        print "Error"
```
### 运行程序
- 找到文件的路径（根据你自己的路径）
```Javascript
 cd GrovePi/Software/Python/
```
- 运行程序
```Javascript
 sudo python grove_ultrasonic.py
```

- 运行得到的结果
![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/600px-GrovePi%2B_Ultrasonic_Ranger_Sensor_terminal.jpg)


### 相关项目
如果您想通过Grove - Ultrasonic Ranger做一些有意思的项目，这里有一些项目供您参考。

#### 自动水位控制器

有许多方法使用浮力传感器来确定水位，或者使用探头来检测油箱中的水位高低。 如何在不使用探针或与水接触的情况下测量水位？ 是的，有一种方法只是使用超声波传感器，这很简单！ 您甚至可以通过设置最大和最小水平来确定水箱内水深。

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/600px-Automatic_Water_Level_Controller.jpg)

[![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/200px-Wiki_makeitnow_logo.png)](http://www.seeed.cc/project_detail.html?id=241)

#### 室内闪电云

做一个室内闪电云，把它挂在你的天花板上，并且跟朋友开一个玩笑，让任何通过它的人感到高兴！

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/Indoor_Lightning_Cloud.gif)

[![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/200px-Wiki_makeitnow_logo.png)](http://www.seeed.cc/project_detail.html?id=182)

#### 多彩螺旋

我们的艺术家王世辉最近向我展示了另一件惊人的艺术作品：多彩螺旋。 再加上几个简单的组件，她向我们介绍了艺术和电子的组合的美丽。

使用Grove - Ultrasonic Ranger，她可以通过提高或降低空气中的手掌来神奇地控制多彩螺旋内的发光LED数量。

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/600px-The_Colour_Helix.JPG)

[![](https://raw.githubusercontent.com/SeeedDocument/Grove_Ultrasonic_Ranger/master/image/200px-Wiki_makeitnow_logo.png)](http://www.seeed.cc/project_detail.html?id=138)

## 资源下载
---
- **[Library]** [Ultrasonic Ranger library](https://github.com/Seeed-Studio/Grove_Ultrasonic_Ranger/archive/master.zip)
- **[Library]** [Grove_LCD_RGB_Backlight-master](https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip)
- **[Example]** [Example_Measure_and_display_the_distance](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/res/Example_Measure_and_display_the_distance.zip)
- **[Example]** [Example_Measure_distance_and_led_display](https://github.com/SeeedDocument/Grove_Ultrasonic_Ranger/raw/master/res/Example_Measure_distance_and_led_display.zip)
