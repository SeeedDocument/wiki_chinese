---
title: Raspberry Pi Motor Driver Board v1.0
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/Raspberry-Pi-Motor-Board-v1.0-p-2411.html
oldwikiname: Raspberry_Pi_Motor_Driver_Board_v1.0
prodimagename: Raspberry_Pi_Motor_Board_v1.0.jpg
wikiurl: http://seeed.wiki/Raspberry_Pi_Motor_Driver_Board_v1_0
sku: 103030031
---

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0.jpg)

Raspberry Pi Motor Driver Board v1.0 基于 Freescale MC33932 dual H-Bridge Power IC，可控制电感负载，每个桥接电流峰值高达 5.0A。它可以让您用 Raspberry Pi B/B+/A+ 或 Pi 2 Model B 驱动两台直流电机，并且独立控制每台电机的速度和方向。

Raspberry Pi Motor Driver Board v1.0 支持 6V~28V 的各种输入电压，可以为 Raspberry Pi 提供 1000mA,5V 的电源。所以，您只需要一个电源即可驱动电机并为 Raspberry Pi 供电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.11891debNA69TQ&id=531757335299)

## 产品特性
--------

-   输出短路保护 (对 VPWR 或 GND 短路)
-   通过内部恒定关断时间 PWM 进行过流限制 (调节)
-   取决于温度的电流限制阈值降低
-   Raspberry Pi 兼容

## 规格参数
--------------

<table border="1" cellspacing="0" width="800">
<tr>
<th scope="col">
参数
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
6
</td>
<td>
/
</td>
<td>
28
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
DC/DC 输出:
</th>
<td>
/
</td>
<td>
5V/1000mA
</td>
<td>
/
</td>
<td>
</td>
</tr>
<tr align="center">
<th scope="row">
输出电流 (每个通道)
</th>
<td>
/
</td>
<td>
2 (连续操作)
</td>
<td>
5 (峰值)
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
PWM 频率
</th>
<td>
/
</td>
<td>
/
</td>
<td>
11
</td>
<td>
kHz
</td>
</tr>
<tr align="center">
<th scope="row">
输出占空比范围
</th>
<td>
0
</td>
<td>
/
</td>
<td>
100
</td>
<td>
 %
</td>
</tr>
<tr align="center">
<th scope="row">
逻辑输入电压
</th>
<td>
-0.3
</td>
<td>
/
</td>
<td>
7
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
工作温度
</th>
<td>
-40
</td>
<td>
/
</td>
<td>
120
</td>
<td>
℃
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
91.20 × 56.15 × 32
</td>
<td>
mm
</td>
</tr>
</table>

## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p3.jpg)

-   **J1** : DC 输入端。
-   **J2** : 电机驱动输出端。
-   **EN,FT** : 用于 EN 控制和故障标志检测的焊盘。如果 EN 焊盘短路，EN 信号被映射到 **D4** 引脚，则可以通过 **D4** 引脚控制 H 桥禁用输出或复位故障标志。如果 FT 焊盘短路，则故障标志信号被映射到 **D3** 引脚，您可以从 **D3** 引脚以太网读取故障标志。
-   **IO** : 逻辑电压电平选择跳线。您可以从该跳线选择控制逻辑电压电平。
-   **Power Supply** : 必须从J1 (DC input connector) 给扩展板上电。输入电压范围为 6Vdc ~ 28Vdc。板上 DC/DC 转换器可将直流输入电压转换为 5VDC 输出电压为逻辑电路供电。DC/DC 转换器还可以为微控制器板 (Arduino/Seeeduino) 提供最大 100mA 电流。
-   **Motor Interface** : 输出 1 和输出 2 (输出 3 和输出 4) 连接直流电机的电机 A (B)。

!!!Caution
    工作期间请勿接触 H 桥 IC 或 PCB 板。满载运行时，其温度可达 100 摄氏度。

##  使用方法
-----

此示例使用 Raspberry Pi B 演示 Raspberry Pi Motor Driver Board v1.0 可用于控制直流电机的正转和反转。

### 硬件连接

- Raspberry Pi B & Raspberry Pi Motor Driver Board v1.0
- 硬件连接如图所示

连接到网络并上电。

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p6.jpg)

### 软件部分

1.复制以下代码;

```
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    import time
    import signal   

    from PiSoftPwm import *

    #print 'Go_1...'
    #frequency = 1.0 / self.sc_1.GetValue()
    #speed = self.sc_2.GetValue()

    class Motor():
        def __init__(self):
        # MC33932 pins
        self.PWMA = 25  
        self.PWMB = 22
        self._IN1 = 23  
        self._IN2 = 24
        self._IN3 = 17
        self._IN4 = 27

        # Initialize PWMA PWMB
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        GPIO.output(self.PWMA, True)
        GPIO.output(self.PWMB, True)

        # Initialize PWM outputs
        self.OUT_1  = PiSoftPwm(0.1, 100, self._IN1, GPIO.BCM)
        self.OUT_2  = PiSoftPwm(0.1, 100, self._IN2, GPIO.BCM)
        self.OUT_3  = PiSoftPwm(0.1, 100, self._IN3, GPIO.BCM)
        self.OUT_4  = PiSoftPwm(0.1, 100, self._IN4, GPIO.BCM)

            # Close pwm output
        self.OUT_1.start(0)
        self.OUT_2.start(0)
        self.OUT_3.start(0)
        self.OUT_4.start(0)

            self.frequency = 0.01
            self.duty = 60

        def Setting(self, frequency, duty):
            self.frequency = frequency
            self.duty = duty

        def Go_1(self):
        self.OUT_1.changeBaseTime(self.frequency)
        self.OUT_2.changeBaseTime(self.frequency)
        self.OUT_1.changeNbSlicesOn(self.duty)
        self.OUT_2.changeNbSlicesOn(0)

        def Back_1(self):
        self.OUT_1.changeBaseTime(self.frequency)
        self.OUT_2.changeBaseTime(self.frequency)
        self.OUT_1.changeNbSlicesOn(0)
        self.OUT_2.changeNbSlicesOn(self.duty)

        def Go_2(self):
        self.OUT_3.changeBaseTime(self.frequency)
        self.OUT_4.changeBaseTime(self.frequency)
        self.OUT_3.changeNbSlicesOn(0)
        self.OUT_4.changeNbSlicesOn(self.duty)

        def Back_2(self):
        self.OUT_3.changeBaseTime(self.frequency)
        self.OUT_4.changeBaseTime(self.frequency)
        self.OUT_3.changeNbSlicesOn(self.duty)
        self.OUT_4.changeNbSlicesOn(0)

        def Stop():
        self.OUT_1.changeNbSlicesOn(0)
        self.OUT_2.changeNbSlicesOn(0)
        self.OUT_3.changeNbSlicesOn(0)
        self.OUT_4.changeNbSlicesOn(0)

    if __name__=="__main__":
        motor=Motor()
        # Called on process interruption. Set all pins to "Input" default mode.
        def endProcess(signalnum = None, handler = None):
            motor.OUT_1.stop()
            motor.OUT_2.stop()
            motor.OUT_3.stop()
            motor.OUT_4.stop()
            motor.GPIO.cleanup()
            exit(0)

        # Prepare handlers for process exit
        signal.signal(signal.SIGTERM, endProcess)
        signal.signal(signal.SIGINT, endProcess)
        signal.signal(signal.SIGHUP, endProcess)
        signal.signal (signal.SIGQUIT, endProcess)

        motor.Setting(0.01, 60)
        print 'motor start...'
        while True:
            print 'turning direction...'
            motor.Go_1()
            time.sleep(1)
            motor.Back_1()
            time.sleep(1)
            motor.Go_2()
            time.sleep(1)
            motor.Back_2()
            time.sleep(1)
```

2.根据你自己的路径保存在 Raspberry Pi 中。

3.运行这个程序。Raspberry Pi Motor Driver Board v1.0 上的 LED1，LED2 将交替点亮; LED3，LED4 也会交替点亮。

这意味着 Out 1 和 Out 2 (Out 3 和 Out 4) 使得电机 A (B) 正转和反转。

4.您会看到如下现象 :

串行监视器 :

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p4.jpg)

Raspberry Pi Motor Driver Board v1.0 :
绿色 LED 和蓝色 LED 交替点亮。

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p5.jpg)

## 资源下载
---------

-   **[Eagle 文件]** [Eagle file Raspberry Pi Motor Driver Board v1.0](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/Raspberry_Pi_Motor_Driver_Board_v1.0_sch_pcb_20150119.zip)
-   **[原理图 PDF]** [PDF Raspberry Pi Motor Driver Board v1.0](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/Raspberry_Pi_Motor_Driver_Board_v1.0.pdf)
-   **[芯片数据手册]** [MC33932VW Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/MC33932VW.pdf)
-   **[芯片数据手册]** [TD1519A Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/TD1519A.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Motor_Driver_Board_v1.0 -->
