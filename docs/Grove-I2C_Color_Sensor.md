---
title: Grove - I2C Color Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-I2C-Color-Sensor-p-854.html
oldwikiname: Grove_-_I2C_Color_Sensor
prodimagename: Grove-I2C-Color-Sensor.jpg
wikiurl: http://seeed.wiki/Grove-I2C_Color_Sensor
sku: 101020041
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/img/Grove-I2C-Color-Sensor.jpg)

该模块基于有 **I2C** 数字输出端口的 color sensor TCS3414CS。 也基于 8×2 阵列的滤波光电二极管和 16位模数转换器，可以测量环境光的色度或物体的颜色。 在16个光电二极管中，4个具有红色滤光片，4个具有绿色滤光片，4个具有蓝色滤光片，4个没有滤光片（透明）。 他们使用同步输入引脚，外部脉冲光源可以提供精确的同步转换控制。

!!!Note
    请注意，最新版本V2.0已经用 TCS3472 替换了 IC ，而旧的库也已更新，如果您使用V2.0版本，请使用 [**新的库文件**](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor_TCS3472)。



版本信息
---
| 版本调整 | 描述                                             | 发布日期    |购买链接|
|----------|-----------------------------------------------------------|--------------|--------------|
| v1.2    | 初次公开发布（测试版）                             | 2013年1月17日 |无|
| v2.0    | 用 TCS34725FN 替换 TCS3472（EOL）并优化了 PCB 布局 |2010年4月27日 |[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.711afee6QwYr3g&id=45574348383)|

产品特性
--------


- 能够兼容 Grove 接口
- 带 I2C 端口的 16位数字输出
- SYNC 输入将积分周期同步到调制光源
- 工作温度范围为 -40°C 至 85°C
- 可以通过编程实现中断功能，可以设置上限和下限阈值
- 符合RoHS

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

产品规格
-------------

|参数 | 值/范围            |
|-----------|------------------------|
| PCB尺寸  | 2.0 cm x 4.0 cm       |
| 接口| 2.0mm节距的引脚|
| VCC       | 3.3 - 6.0 V            |
| I2C 频率 | 400 kHz                |

Platforms Supported
-------------------

入门指导
---------------

以下文档可以帮助用户使用 Grove 进行入门学习。

-   [入门指导](http://seeed.wiki/Getting_Started_with_Seeeduino/)
-   [关于 grove](http://seeed.wiki/Grove_System/)

### 硬件连接

Grove产品具有环保性，并且都具有可插入[Grove Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的相同连接口。 将此模块连接到 Base Shield 的 **I2C** 端口。 如果你没有 Base Shield，您也可以通过连接线将 Grove - I2C Color Sensor 连接到 Arduino。

| Arduino UNO | Grove - I2C Color Sensor |
|-------------|--------------------------|
| 5V          | VCC                      |
| GND         | GND                      |
| SDA         | SDA                      |
| SCL         | SCL                      |

软件安装
---------------------


[Seeed入门指导](http://seeed.wiki/Getting_Started_with_Seeeduino/)

演示
-----

该模块可用于检测光源的颜色或物体的颜色。 当用于检测光源的颜色时，应关闭 LED 开关，并且光源应直接照射到传感器上。 当用于检测物体的颜色时，LED 应该是打开的，你应该传感器放在物体的上面。通过反射理论来感知颜色。 如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/img/Reflcect.jpg)

### 彩色传感器库

我们创建了一个库，以帮助您快速开始使用 Seeeduino / Arduino，本节将介绍如何设置库。

#### 开始建立


1. 从 Grove_I2C_Color_Sensor github 页面下载 [库代码](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor)。 如果您使用的是最新版本V2.0（IC 为 TCS3472），请使用
 [新库](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor_TCS3472)
2. 将下载的文件解压缩到... / arduino / libraries 中。
3. 可以解压后重命名文件夹为 “Color_Sensor”
4. 启动 Arduino IDE（如果打开，请重新启动）。

#### 功能说明

这是库中最重要/最有用的功能，我们邀请您自己查看 .h 和 .cpp 文件，以查看所有可用的功能。

##### 通过库函数读取RGB数据


**readRGB(int \*red, int \*green, int \*blue)**

-   **red:** 使用可变地址保存 **R**.
-   **green:** 使用可变地址保存为 **G**.
-   **blue:** 使用可变地址保存为 **B**.

```
void loop()
{
    int red, green, blue;
    GroveColorSensor colorSensor;
    colorSensor.ledStatus = 1;            // When turn on the color sensor LED, ledStatus = 1; When turn off the color sensor LED, ledStatus = 0.
    while(1)
    {
        colorSensor.readRGB(&red, &green, &blue);    //Read RGB values to variables.
        delay(300);
        Serial.print("The RGB value are: RGB( ");
        Serial.print(red,DEC);
        Serial.print(", ");
        Serial.print(green,DEC);
        Serial.print(", ");
        Serial.print(blue,DEC);
        Serial.println(" )");
        colorSensor.clearInterrupt();
    }
}
```

### 颜色传感器示例/应用

此示例显示如何使用 Grove - I2C Color Sensor 的功能，并使用 [Chainable RGB LED Grove](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4a676fa41TunBo&id=45573760464) 显示检测到的颜色。

<div class="admonition note">
<p class="admonition-title">Note</p>
如果您之前尚未将 <a href="https://github.com/Seeed-Studio/Grove_Chainable_RGB_LED">Grove-Chainable RGB LED 库</a> 下载到你的 Arduino IDE , 请先下载并设置库。
</div>


打开 **File（文件） - >Examples（示例） - >Color_Sensor - >example - >ColorSensorWithRGB-LED** 使用 RGB-LED 完整的示例，或将代码复制并粘贴到新的 Arduino 编辑页面上。

**描述**: 该示例可以测量环境光的颜色色度或物体的颜色，并通过可连接的 RGB LED Grove，显示检测到的颜色。

您还可以使用其他显示模块通过 Grove - I2C Color Sensor 显示检测到的颜色。

```
#include <Wire.h>
#include <GroveColorSensor.h>
#include <ChainableLED.h>
 
#define CLK_PIN   7
#define DATA_PIN  8
#define NUM_LEDS  1            //The number of Chainable RGB LED
 
ChainableLED leds(CLK_PIN, DATA_PIN, NUM_LEDS);
 
void setup()
{
    Serial.begin(9600);
    Wire.begin();
}
 
void loop()
{
    int red, green, blue;
    GroveColorSensor colorSensor;
    colorSensor.ledStatus = 1;            // When turn on the color sensor LED, ledStatus = 1; When turn off the color sensor LED, ledStatus = 0.
    while(1)
    {
        colorSensor.readRGB(&red, &green, &blue);    //Read RGB values to variables.
        delay(300);
        Serial.print("The RGB value are: RGB( ");
        Serial.print(red,DEC);
        Serial.print(", ");
        Serial.print(green,DEC);
        Serial.print(", ");
        Serial.print(blue,DEC);
        Serial.println(" )");
        colorSensor.clearInterrupt();
        for(int i = 0; i<NUM_LEDS; i++)
        {
            leds.setColorRGB(i, red, green, blue);
        }
    }
}
```

-   将代码上传到开发板。
-   然后 Grove _ Chainable_RGB_LED 将显示检测到的颜色。


其他参考
---------------

该模块基于 color sensor TCS3414CS。 TCS3414CS digital color sensor 从四个通道返回数据：红色（R），绿色（G），蓝色（B）和清除（C）（未过滤）。 红色，绿色和蓝色通道（RGB）的响应可用于确定特定光源的色度坐标（x，y）。 这些标准由国际法委员会（CIE）制定。 CIE是涉及颜色和颜色测量的主要国际组织。为了使用 TCS3414CS 获取给定对象的颜色，我们必须首先将传感器响应（RGB）映射到CIE的标准值（XYZ）。 然后需要计算色度坐标（x，y）。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/img/Coordinates_transform.png)

色度计算过程概述

进行转换的方程式：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/img/Equations.png)

变换方程

-   当我们得到坐标（x，y）时，请参考下图，以获得推荐的颜色。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/img/Chromaticity_Diagram.jpg)


资源下载
---------

-   **[Library]**[Library for Grove - I2C Color Sensor V1.2](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor)
-   **[Library]**[Library for Grove - I2C Color Sensor V2.0](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor_TCS3472)
-   **[Eagle]**[Grove-I2C Color Sensor Eagle File V1.2](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove-I2C%20Color%20Sensor%20Eagle%20File%20V1.2.zip)
-   **[Eagle]**[Grove-I2C Color Sensor Eagle File V2.0](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove%20I2C%20Color%20Sensor%20v2.0.zip)
-   **[PDF]**[Grove-I2C Color Sensor SCH File V1.2](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove%20-%20I2C%20Color%20sensor%20v1.2%20SCH.pdf)
-   **[PDF]**[Grove-I2C Color Sensor SCH File V2.0](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove%20-%20I2C%20Color%20sensor%20v2.0%20SCH.pdf)
-   **[PDF]**[Grove-I2C Color Sensor PCB File V1.2](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove%20-%20I2C%20Color%20sensor%20v1.2%20PCB.pdf)
-   **[PDF]**[Grove-I2C Color Sensor PCB File V2.0](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/Grove%20-%20I2C%20Color%20sensor%20v2.0%20PCB.pdf)
-   **[Datasheet]**[TCS3414-A Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Color_Sensor/master/res/TCS3404_TCS3414-A.pdf)
-  **[Datasheet]**[TCS3472 Datasheet](https://github.com/SeeedDocument/Grove-I2C_Color_Sensor/raw/master/res/TCS3472%20Datasheet.pdf)

</li>

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_I2C_Color_Sensor -->
