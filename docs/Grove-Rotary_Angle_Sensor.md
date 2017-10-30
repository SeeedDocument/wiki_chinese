---
title: Grove - Rotary Angle Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Rotary-Angle-Sensor-p-770.html
oldwikiname: Grove_-_Rotary_Angle_Sensor
prodimagename: Grove-Rotary_Angle_Sensor.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020017 1.jpg
wikiurl: http://seeed.wiki/Grove-Rotary_Angle_Sensor
sku: 101020017
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/Grove-Rotary_Angle_Sensor.jpg)

电位计在其 D1 连接器上产生 0 和 Vcc 之间的模拟输出 ( 5V 直流，使用Seeeduino)。D2 连接器未使用。角度范围为 300 度，具有线性变化的特性。电阻值为 10 欧姆，非常适合 Arduino 使用。这也可以称为旋转角度传感器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.43fde5d8jba3QJ&id=45554377762&ns=1&abbucket=1#detail)

还有另一个产品 - [Grove - Rotary Angle Sensor(P)](http://www.seeedstudio.com/depot/grove-rotary-angle-sensorp-p-1242.html)。 "P" 是什么意思? "P" 是本产品中的“面板安装”。它是 Grove - Rotary Angle Sensor 的姐妹版本。 它们是相同的，除了 Grove 连接器被移动到后面，这样可以便您可以轻松地将其用作一个整洁的无线人机界面设备。

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/Grove-Rotary_Angle_Sensor-P-.jpg">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/GroveRotaryP_02.jpg">
        </td>
    </tr>
</table>

## 产品特性
--------

-   Grove 接口
-   易于使用
-   Grove Base 模块

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 规格参数
--------------

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
电压
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
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
旋转角度
</th>
<td>
0
</td>
<td>
~
</td>
<td>
300
</td>
<td>
Deg
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
19x19x30.1
</td>
<td>
mm
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 使用方法
-----

### 与 [Arduino](/Arduino "Arduino") 一起使用

以下草图演示了使用旋转角度传感器控制 LED 亮度的简单应用。旋转角度传感器的角度为 0~300 度，为了控制 LED 的亮度，我们应该在演示代码中转换为相应的电压值。

-   如下图所示，旋转角传感器传感器连接到 Grove - Base Shield 的模拟端口 **A0**，LED 连接到数字端口 **2**。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/Analog_Input_v1.0b.jpg)

-   将下面的代码复制并粘贴到新的 Arduino 文件上。

```
    /******************************************************************************/
    /*macro definitions of Rotary angle sensor and LED pin*/
    #define ROTARY_ANGLE_SENSOR A0
    #define LED 2//the Grove - LED is connected to D3 of Arduino
    #define ADC_REF 5//reference voltage of ADC is 5v.If the Vcc switch on the seeeduino
                     //board switches to 3V3, the ADC_REF should be 3.3
    #define GROVE_VCC 5//VCC of the grove interface is normally 5v
    #define FULL_ANGLE 300//full value of the rotary angle is 300 degrees
    void setup()
    {
        Serial.begin(9600);
        pinsInit();
    }

    void loop()
    {
        int degrees;
        degrees = getDegree();
        Serial.println("The angle between the mark and the starting position:");
        Serial.println(degrees);

        int brightness;
        /*The degrees is 0~300, should be converted to be 0~255 to control the*/
        /*brightness of LED                                                   */
        brightness = map(degrees, 0, FULL_ANGLE, 0, 255);
        controlBrightness(brightness);

        delay(500);
    }
    void pinsInit()
    {
        pinMode(ROTARY_ANGLE_SENSOR, INPUT);
        pinMode(LED,OUTPUT);
    }

    /*PWM control brightness                        */
    /*If brightness is 0,the LED is off.            */
    /*The Greater the brightness, the brighter the LED.*/
    /*The range of brightness is 0~255              */
    void controlBrightness(int brightness)
    {
        analogWrite(LED,brightness);
    }
    /************************************************************************/
    /*Function: Get the angle between the mark and the starting position    */
    /*Parameter:-void                                                       */
    /*Return:   -int,the range of degrees is 0~300                          */
    int getDegree()
    {
        int sensor_value = analogRead(ROTARY_ANGLE_SENSOR);
        float voltage;
        voltage = (float)sensor_value*ADC_REF/1023;
        float degrees = (voltage*FULL_ANGLE)/GROVE_VCC;
        return degrees;
    }
```

-   上传代码。
-   然后您就可以通过旋转传感器来控制 LED 了。试试吧!

### 与 TI LaunchPad 一起使用

**读取电位器 (旋转角度传感器)**

此示例显示如何读取来自 Grove 电位器模块的模拟输出。我们将在这个例子中组合几个 Grove 模块！通过旋转电位器旋钮，我们将在 Grove 4 数字显示屏上显示模拟读数值。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/Angle_sensor.jpg)

```
    /*
      Rotary Angle Sensor
     Demonstrates analog input by reading an analog sensor on J16 of the Grove Base BoosterPack. The speed of the red LED on the LaunchPad will change depending on the position of the potentiometer knob. This example will also display the analog reading value on the Grove 4-digital display.

     The circuit:
     * Potentiometer attached to pin 24 (J6 on Grove Base BoosterPack)
     * center pin of the potentiometer to the analog pin
     * one side pin (either one) to ground
     * the other side pin to VCC (3.3V)

     * Note: Because of unstable of the voltage, the value of the rotary angle sensor
             varies slightly from run to run even you don't touch it.  

     Created by Oliver Wang

     This example code is in the public domain.

     http://www.seeedstudio.com/wiki/GROVE_-_Starter_Kit_v1.1b#Grove_-_Rotary_Angle_Sensor
     */

    #include "TM1637.h"

    /* Macro Define */
    #define CLK               39                  /* 4-digital display clock pin */
    #define DIO               38                /* 4-digital display data pin */
    #define ROTARY_ANGLE_P    24               /* pin of rotary angle sensor */

    /* Global Variables */
    TM1637 tm1637(CLK, DIO);                  /* 4-digital display object */
    int analog_value = 0;                     /* variable to store the value coming from rotary angle sensor */

    int8_t bits[4] = {0};                     /* array to store the single bits of the value */

    /* the setup() method runs once, when the sketch starts */
    void setup() {

        /* Initialize 4-digital display */
        tm1637.init();
        tm1637.set(BRIGHT_TYPICAL);

    }

    /* the loop() method runs over and over again */
    void loop() {   

        analog_value = analogRead(ROTARY_ANGLE_P);      /* read the value from the sensor */
        memset(bits, 0, 4);                             /* reset array when we use it */
        for(int i = 3; i >= 0; i--) {
            /* get single bits of the analog value */
            bits[i] = analog_value % 10;
            analog_value = analog_value / 10;  
            tm1637.display(i, bits[i]);                 /* display by 4-digital display */
        }
        delay(100);
    }
```

### 与 [Raspberry Pi](/GrovePiPlus "GrovePi+") 一起使用

本示例使用 ADC 通道 **0** 来获得旋转角度的值。然后给出 PWM 输出以改变 LED 的亮度。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/img/GrovePiPlus_rotary_angle_sensor.jpg)

```
    # GrovePi + Grove Rotary Angle Sensor (Potentiometer) + Grove LED
    import time
    import grovepi

    # Connect the Grove Rotary Angle Sensor to analog port A0
    # SIG,NC,VCC,GND
    potentiometer = 0

    # Connect the LED to digital port D5
    # SIG,NC,VCC,GND
    led = 5

    grovepi.pinMode(potentiometer,"INPUT")
    grovepi.pinMode(led,"OUTPUT")
    time.sleep(1)

    # Reference voltage of ADC is 5v
    adc_ref = 5

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    while True:
        try:
            # Read sensor value from potentiometer
            sensor_value = grovepi.analogRead(potentiometer)

            # Calculate voltage
            voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

            # Calculate rotation in degrees (0 to 300)
            degrees = round((voltage * full_angle) / grove_vcc, 2)

            # Calculate LED brightess (0 to 255) from degrees (0 to 300)
            brightness = int(degrees / full_angle * 255)

            # Give PWM output to LED
            grovepi.analogWrite(led,brightness)

            print "sensor_value =", sensor_value, " voltage =", voltage, " degrees =", degrees, " brightness =", brightness

        except IOError:
            print "Error"
```

#### 运行程序

-   找到文件的路径 ( 根据你自己的路径 )。

```
    cd GrovePi/Software/Python/
```
-   运行程序。

```
    sudo python grove_rotary_angle_sensor.py
```

资源下载
---------

-   **[Eagle文件]** [Grove-Rotary Angle v1.2 Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/res/Grove-Rotary_Angle_Sensor_v1.2.zip)
-   **[Eagle文件]** [Grove-Rotary Angle Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Rotary_Angle_Sensor/master/res/Grove-Rotary_Angle_Sensor_Eagle_File.zip)
-   **[其他资源]** [Github repository for Rotary Angle Sensor](https://github.com/Seeed-Studio/Grove_Rotary_Angle_Sensor)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor -->
