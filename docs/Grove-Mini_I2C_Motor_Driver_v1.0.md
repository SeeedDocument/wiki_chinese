---
title: Grove - Mini I2C Motor Driver v1.0
category: Actuator
bzurl: https://www.seeedstudio.com/Grove - I2C Mini Motor Driver-p-2508.html
oldwikiname: Grove_-_Mini_I2C_Motor_Driver_v1.0
prodimagename: Mini_I2C_motor_2.png
wikiurl: http://seeed.wiki/Grove-Mini_I2C_Motor_Driver_v1_0
sku: 105020010
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_I2C_motor_2.png)

Grove - MIni I2C motor driver 包含两个 DRV8830。DRV8830 为电池供电的玩具，打印机和其他低电压或电池供电的运动控制应用提供了集成电机驱动器的解决方案。该模块有两个 H 桥式驱动器，可以驱动两个直流电机或两个步进电机的绕组，以及其他负载如电磁铁。它需要一个板载 5V 电压调节器，可以为 I2C 总线供电。所有驱动器线路均采用二极管保护，避免反电动势。它具有两个故障指示灯和四个 LED 指示每个电机运行的方向。Grove 接口和 I2C 接口使您可以将它与许多其他设备进行菊花链连接。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.16.5e2f27f7HLV2ss&id=531757423678&ns=1&abbucket=1#detail)

## 产品特性
--------

-   无外部电源
-   两个故障指示灯
-   默认最大驱动电流 200mA
-   Grove 接口
-   I2C 接口
-   电机的速度和方向可控
-   通道数量 : 2
-   易于使用

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 创意应用
-----------------

该电机驱动器可用于驱动任何在 5v 时电流不超过 1A 的有刷电机。两个电机设置不同的速度和方向时可以同时驱动。速度可以完全按比例设置，由 I2C 命令控制。

-   电池供电 :
    -   打印机
    -   玩具
    -   机器人
    -   相机
    -   电话

-   小执行器，水泵等

以下项目供您参考。

| **Make a Mini Toy Car**                                              | **Make a Steampunk Style Award**                                       |
|----------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_toy_car.jpg)   | ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Seeed_award2015.jpg)  |
| [点击制作](http://www.seeed.cc/project_detail.html?id=392)       | [点击制作](http://www.seeed.cc/project_detail.html?id=1131)        |

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
工作电压
</th>
<td>
2.75
</td>
<td>
5
</td>
<td>
6.8
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
每个通道的最大输出电流
</th>
<td>
0.2(默认)
</td>
<td>
-
</td>
<td>
1
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
I2C 总线的输入/输出电压
</th>
<td colspan="3">
3.3/5
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
通信协议
</th>
<td colspan="3">
I2C
</td>
<td>
/
</td>
</tr>
<tr align="center">
<th scope="row">
默认 I2C 地址
</th>
<td colspan="3">
0xC0, 0xC4
</td>
<td>
/
</td>
</tr>
</table>

Platforms Supported
-------------------

## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_motor_driver.jpg)

-   **Grove Interface** 是一个具有相同的接口的系统，可以插入到 **[Base Shield](http://seeed.wiki/Base_Shield_V2/)**。将此模块连接到 Base Shield 的 **I2C** 端口，然后与 Arduino 配合使用。您也可以通过跳线将 Grove - Mini I2C Motor Driver 连接到没有使用 Base Shield 的 Arduino。

<table>
<tr>
<th width="150">
Arduino UNO
</th>
<th width="150">
Base Shield
</th>
<th width="150">
Grove - Mini I2C Motor Driver
</th>
</tr>
<tr align="center">
<td>
5V
</td>
<td rowspan="4">
I2C port
</td>
<td>
VCC
</td>
</tr>
<tr align="center">
<td>
GND
</td>
<td>
GND
</td>
</tr>
<tr align="center">
<td>
SDA
</td>
<td>
SDA
</td>
</tr>
<tr align="center">
<td>
SCL
</td>
<td>
SCL
</td>
</tr>
</table>


-   **CH1 故障指示灯** - 通道 1 故障指示灯
-   **CH2 故障指示灯** - 通道 2 故障指示灯
-   **方向指示灯** - 电机方向指示灯
-   **CH1 输出接口** - 电机 1 接口
-   **CH2 输出接口** - 电机 2 接口

## 硬件功能
-----------------

### 更改默认最大驱动电流

每个通道默认最大驱动电流为 200mA。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/QQ20150817-3.png)

每个通道 (CH1,CH2) 有一个电阻，每个电阻 (R5,R12) 的阻值都是 1Ω，所以按照下式最大驱动电流为 200mA

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_I2C_motor_7.png)

</center>

同时，每个通道都提供了一个预留的可焊接焊盘 (CH1 对应 R6，CH2 对应 R13)，因此您可以在电路板上焊接一个电阻，以更改每个通道的电阻值。以下是更改后的电路板的新方程

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_I2C_motor_8.png)
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_I2C_motor_9.png)
</center>

<div class="admonition caution">
<p class="admonition-title">Caution</p>
每个通道的最大工作电流必须小于 1A。所以焊接到预留焊盘的电阻的最小值应该不小于 0.2Ω。
</div>

### 更改默认 I<sup>2</sup>C 地址

每个通道的 I2C 地址是可更改的。请看看电路板的背面，您会发现有4个跳线焊盘; A0_CH1 和 A1_CH1 是对应通道 1，A0_CH2 和 A1_CH2 是对应通道 2，如下所示 :

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Address_mini_i2c_motor_driver.png)
</center>

您可以焊接或脱焊各个连接以更改 I2C 地址 :

-   1 - 您需要焊枪将两侧焊接在一起
-   0 - 您需要焊枪将两侧脱焊

<center>
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_I2C_motor_12.png)
</center>

<div class="admonition note">
<p class="admonition-title">Note</p>
 Grove - Mini I2C Motor driver 库和默认地址有关
</div>

## 入门指导
---------------

现在开始使用 Grove - Mini I2C Motor Driver !

### 准备工作

现在为 Grove - Mini I2C Motor Driver v1.0 进行使用演示，它需要以下模块 :

-   2 * DC Motor 2V-6V
-   [Seeeduino Lite](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4534df99jXa0pT&id=45487750521)

**Seeeduino Lite 与 Arduino 兼容**

如果您使用的是 Arduino UNO 或任何带有 Grove 接口的 Arduino 兼容板，

您需要一个 [Grove Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.142df1b2snD5L8&id=520233320144) 以完成连接

如果这是您第一次使用 Arduino 或者 Seeeduino，请点击 [here](/Getting_Started_with_Seeeduino) 开始您的Arduino旅程。

### 硬件连接

Grove - Mini I2C Motor Driver 有一个 Grove 插座用于连接 Arduino 或者 Seeeduino。
它们是:

-   2 * DC Motor 2V-6V - 连接到 CH1 & CH2 输出接口。
-   Seeeduino Lite

按下图所示连接好 Seeeduino 的 I2C Grove 接口和 Mini Motor Driver 的 Grove 接口：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Mini_motor_driver_demo.jpg)

### 软件部分

[![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/img/Arduino_mini_i2c_motor_driver.jpg)](http://https://www.arduino.cc/)

The Grove - Mini I2C Motor Driver 基于芯片 DRV8830 可以控制电机。DRV8830 不仅仅是一个双电机驱动器，它还是一个双 H 桥式电机控制电路。 一个 H 桥式电机控制电路是一个特定的晶体管设置，允许您切换电流的方向。您可以使用您的 Arduino 使它们以任何速度旋转。

由于模块具有 2 个 H 桥式电机控制电路，不仅可以使机器人前后移动，还可以使每个车轮以不同的方向旋转以转弯。

通过 USB 线缆将 Seeeduino 连接到 PC。

现在，让我们使用 Grove - Mini I2C Motor Driver 来控制两个直流电机正向或反向旋转。

下面给出的是一个与 Arduino 一起使用的示例程序。这个代码是非常基础的，您也可以改变它，并以您自己的方式做。

```c
/****************************************************************
Example code demonstrating the use of the Arduino Library for
the SparkFun MiniMoto board, which uses the TI DRV8830 IC for I2C
low-voltage DC motor control.
 
This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.
 
17 Sep 2013- Mike Hord, SparkFun Electronics
 
Code developed in Arduino 1.0.5, on a Fio classic board.
 
**Updated for Arduino 1.6.4 5/2015**
****************************************************************/
 
#include <SparkFunMiniMoto.h>  // Include the MiniMoto library
 
// Create two MiniMoto instances, with different address settings.
MiniMoto motor0(0xC4); // A1 = 1, A0 = clear
MiniMoto motor1(0xC0); // A1 = 1, A0 = 1 (default)
 
#define FAULTn  16     // Pin used for fault detection.
 
// Nothing terribly special in the setup() function- prep the
//  serial port, print a little greeting, and set up our fault
//  pin as an input.
void setup()
{
    Serial.begin(9600);
    Serial.println("Hello, world!");
    pinMode(FAULTn, INPUT);
}
 
// The loop() function just spins the motors one way, then the
//  other, while constantly monitoring for any fault conditions
//  to occur. If a fault does occur, it will be reported over
//  the serial port, and then operation continues.
void loop()
{
    Serial.println("Forward!");
    motor0.drive(100);
    motor1.drive(100);
    delayUntil(1000);
    Serial.println("Stop!");
    motor0.stop();
    motor1.stop();
    delay(1000);
    Serial.println("Reverse!");
    motor0.drive(-100);
    motor1.drive(-100);
    delayUntil(1000);
    Serial.println("Brake!");
    motor0.brake();
    motor1.brake();
    delay(1000);
}
 
// delayUntil() is a little function to run the motor either for
//  a designated time OR until a fault occurs. Note that this is
//  a very simple demonstration; ideally, an interrupt would be
//  used to service faults rather than blocking the application
//  during motion and polling for faults.
void delayUntil(unsigned long elapsedTime)
{
    // See the "BlinkWithoutDelay" example for more details on how
    //  and why this loop works the way it does.
    unsigned long startTime = millis();
    while (startTime + elapsedTime > millis())
    {
        // If FAULTn goes low, a fault condition *may* exist. To be
        //  sure, we'll need to check the FAULT bit.
        if (digitalRead(FAULTn) == LOW)
        {
            // We're going to check both motors; the logic is the same
            //  for each...
            byte result = motor0.getFault();
            // If result masked by FAULT is non-zero, we've got a fault
            //  condition, and we should report it.
            if (result & FAULT)
            {
                Serial.print("Motor 0 fault: ");
                if (result & OCP) Serial.println("Chip overcurrent!");
                if (result & ILIMIT) Serial.println("Load current limit!");
                if (result & UVLO) Serial.println("Undervoltage!");
                if (result & OTS) Serial.println("Over temp!");
                break; // We want to break out of the motion immediately,
                //  so we can stop motion in response to our fault.
            }
            result = motor1.getFault();
            if (result & FAULT)
            {
                Serial.print("Motor 1 fault: ");
                if (result & OCP) Serial.println("Chip overcurrent!");
                if (result & ILIMIT) Serial.println("Load current limit!");
                if (result & UVLO) Serial.println("Undervoltage!");
                if (result & OTS) Serial.println("Over temp!");
                break;
            }
        }
    }
}
```

现在点击 Upload(CTRL+U) 上传代码。如果有任何错误提示请参考 [这里](/Arduino_Common_Error "Arduino Common Error")，您也可以在 [社区](http://www.seeed.cc) 讨论。

### 查看结果

上传完成后，电机将循环正转或反转。

## 资源下载
---------

-   **[Eagle 文件]** [Grove - Mini I2C Motor Driver\_Eagle\_File](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/res/Grove-Mini_I2C_Motor_Driver_v1.0_SCH_PCB.rar)
-   **[原理图 PDF]** [Grove - Mini I2C Motor Driver Schematic Document](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/res/Grove-Mini_I2C_Motor_Driver_v1.0_SCH.pdf)
-   **[库文件]** [Grove - Mini I2C Motor Driver Source Library](https://github.com/Seeed-Studio/Drv8830_Motor_Driver)
-   **[芯片数据手册]** [DRV8830 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Mini_I2C_Motor_Driver_v1.0/master/res/DRV8830.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Mini_I2C_Motor_Driver_v1.0 -->
