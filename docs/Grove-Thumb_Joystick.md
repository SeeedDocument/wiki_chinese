---
title: Grove - Thumb Joystick
category: Sensor
bzurl: https://seeedstudio.com/Grove-Thumb-Joystick-p-935.html
oldwikiname: Grove_-_Thumb_Joystick
prodimagename: Bgjoy1.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/bgjoy1.jpg
wikiurl: http://seeed.wiki/Grove-Thumb_Joystick
sku: 101020028
tags: grove_analog, io_3v3, io_5v, plat_duino,plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Thumb_Joystick/master/img/Bgjoy1.jpg)

Grove - Thumb Joystick 是一个 Grove 兼容模块，与 PS2 (PlayStation 2) 手柄上的操纵杆非常相似。X 轴和 Y 轴是两个 ~10k 电位器，通过产生模拟信号来控制二维运动。操纵杆有一个可以用于特殊的应用的按钮。当模块处于工作模式时，将输出两个模拟值，代表两个方向。与普通操纵杆相比，其输出值被限制在一个较小的范围内(就是 200~800)，只有当按下时 X 值才会被设置为 1023，MCU才能检测到按下的动作。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.dc56acfYbp9xg&id=45706638616&ns=1&abbucket=1#detail)

## 产品特性
--------

-   Grove 接口
-   5V/3.3V
-   模拟量输出

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)


## 创意应用
-----------------

-   游戏控制器
-   机器人远程控制

### [Project - 2048 Game](http://www.instructables.com/id/DIY-a-Raspberry-Game-2048/)

这是一个由 Grove - Thumb Joystick 组成的 Pi 游戏项目。点击下面的图片获取更多关于这个项目的信息。


[![](https://github.com/SeeedDocument/Grove-Thumb_Joystick/raw/master/img/pi_game_new.jpg)](http://www.instructables.com/id/DIY-a-Raspberry-Game-2048/)


## 规格参数
--------------

| 项目                                | 最小值  | 典型值 | 最大值  | 单位 |
|-------------------------------------|------|---------|------|------|
| 工作电压                     | 4.75 | 5.0     | 5.25 | V    |
| 输出模拟值 （X 坐标） | 206  | 516     | 798  | \    |
| 输出模拟值 （Y 坐标） | 203  | 507     | 797  | \    |

## Platforms Supported
-------------------

## 使用方法
-----

### 与 [Arduino](/Arduino "Arduino") 一起使用

Grove - Thumb Joystick 是一个输出范围从 0 到 1023 的模拟信号的设备。这要求我们使用 Arduino 的模拟端口来读取数据。

1.使用 4 针 Grove 线缆将模块连接到 [Grove - Base Shield](http://www.seeedstudio.com/grove-base-shield-p-754.html) 的 **A0**/**A1**。

2.将 Grove - Basic Shield 插入 Arduino。

3.使用 USB 线缆将 Arduino 连到 PC。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Thumb_Joystick/master/img/Grove-Thumb_Joystick.jpg)

4.复制并粘贴下面的代码到一个新的 Arduino 编程页面。

```
/*
  Thumb Joystick demo v1.0
  by:http://www.seeedstudio.com
  connect the module to A0&A1 for using;
*/

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int sensorValue1 = analogRead(A0);
    int sensorValue2 = analogRead(A1);

    Serial.print("The X and Y coordinate is:");
    Serial.print(sensorValue1, DEC);
    Serial.print(",");
    Serial.println(sensorValue2, DEC);
    Serial.println(" ");
    delay(200);
}
```

5.您可以通过打开串行监视器来检查输出模拟信号的值。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Thumb_Joystick/master/img/Grove-Thumd_Joystick_Result.jpg)

通过使用公式 : R=(float)(1023-sensorValue)\*10/sensorValue，可以将 Arduino 模拟端口的输出值转换为相应的电阻值。

### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.完成配置开发环境，否则请遵循 [here](/GrovePiPlus)。

3.连接

-   将传感器用 Grove 线缆插入  Grovepi 插口 **A0**。
![](https://github.com/SeeedDocument/Grove-Thumb_Joystick/raw/master/img/Pi_Joystick%20connection.jpg)

4.跳转到演示目录 :
```
    cd yourpath/GrovePi/Software/Python/
```
-   演示代码如下 :
```
    nano grove_thumb_joystick.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Thumb Joystick to analog port A0

    # GrovePi Port A0 uses Arduino pins 0 and 1
    # GrovePi Port A1 uses Arduino pins 1 and 2
    # Don't plug anything into port A1 that uses pin 1
    # Most Grove sensors only use 3 of their 4 pins, which is why the GrovePi shares Arduino pins between adjacent ports
    # If the sensor has a pin definition SIG,NC,VCC,GND, the second (white) pin is not connected to anything

    # If you wish to connect two joysticks, use ports A0 and A2 (skip A1)

    # Uses two pins - one for the X axis and one for the Y axis
    # This configuration means you are using port A0
    xPin = 0
    yPin = 1
    grovepi.pinMode(xPin,"INPUT")
    grovepi.pinMode(yPin,"INPUT")

    # The Grove Thumb Joystick is an analog device that outputs analog signal ranging from 0 to 1023
    # The X and Y axes are two ~10k potentiometers and a momentary push button which shorts the x axis

    # My joystick produces slightly different results to the specifications found on the url above
    # I've listed both here:

    # Specifications
    #     Min  Typ  Max  Click
    #  X  206  516  798  1023
    #  Y  203  507  797

    # My Joystick
    #     Min  Typ  Max  Click
    #  X  253  513  766  1020-1023
    #  Y  250  505  769
    while True:
        try:
            # Get X/Y coordinates
            x = grovepi.analogRead(xPin)
            y = grovepi.analogRead(yPin)

            # Calculate X/Y resistance
            Rx = (float)(1023 - x) * 10 / x
            Ry = (float)(1023 - y) * 10 / y

            # Was a click detected on the X axis?
            click = 1 if x >= 1020 else 0

            print "x =", x, " y =", y, " Rx =", Rx, " Ry =", Ry, " click =", click
            time.sleep(.5)

        except IOError:
            print "Error"
```

5.运行代码。
```
    sudo python grove_thumb_joystick.py
```

## 资源下载
---------

- **[Eagle文件]** [Grove-Thumb Joystick Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Thumb_Joystick/master/res/Eagle_Design_Files.zip)

- **[原理图PDF]** [Joystick Schematic PDF File](https://github.com/SeeedDocument/Grove-Thumb_Joystick/raw/master/res/Joystick.pdf)

- **[数据手册]** [Analog Joystick Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Thumb_Joystick/master/res/Analog_Joystick_Datasheet.jpg)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Thumb_Joystick -->
