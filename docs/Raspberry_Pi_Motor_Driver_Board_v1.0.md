---
title: Raspberry Pi Motor Driver Board v1.0
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/Raspberry-Pi-Motor-Board-v1.0-p-2411.html
oldwikiname: Raspberry_Pi_Motor_Driver_Board_v1.0
prodimagename: Raspberry_Pi_Motor_Board_v1.0.jpg
wikiurl: http://seeed.wiki/Raspberry_Pi_Motor_Driver_Board_v1.0
sku: 103030031
---

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0.jpg)

Raspberry Pi Motor Driver Board v1.0 基于飞思卡尔（Freescale）MC33932 双 H 桥功率 IC，可以控制电感负载，每个电桥的峰值电流高达5.0A。它可以让您用 Raspberry Pi B/B+/A+和 Raspberry Pi 2 B 驱动两个直流电机，独立控制每个电机的速度和转向。

Raspberry Pi Motor Driver Board v1.0 支持从 6V〜28V 的宽范围输入电压。同时，板载 DC/DC 转换器支持很宽的输入电压范围，并且可以为 Raspberry Pi 提供 5V ，最大 1000mA 电流的电源。所以，你只需要一个电源来驱动电机，同时给 Raspberry Pi 供电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.6df8d5b0xxPhtg&id=531757335299)

产品特性
--------

-   输出短路保护（对 VPWR 或 GND 短路）
-   通过内部恒定关断时间 PWM 进行过流限制（调节）
-   温度过高电流降低保护
-   兼容 Raspberry Pi

规格参数
--------------

<table border="1" cellspacing="0" width="800">
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
输入电压
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
DC/DC 输出
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
输出电流（每一个通道）
</th>
<td>
/
</td>
<td>
2 (持续工作)
</td>
<td>
5 (瞬间)
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
输出占空比
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
91.20 * 56.15 * 32
</td>
<td>
mm
</td>
</tr>
</table>

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p3.jpg)

-   **J1**：直流输入接口。
-   **J2**：电机接口。
-   **EN,FT**：EN 使能和故障检测焊盘。如果短路 EN 焊盘，EN 信号连接到 D4 引脚，则可以通过D4引脚禁用 H 桥输出或复位故障标志。如果短路 FT 焊盘，FT 信号连接到 D3 引脚，您可以从 D3 引脚读取故障标志。
-   **IO**：逻辑电压电平选择跳线。您可以从这个跳线选择控制逻辑电平。默认连接 5V，如果需要选择 3.3V 电压，请先用小刀或其他锋利物品划开“IO”和“5V”之间的连接（请仔细观察），并用万用表等器材确认断开。然后焊接连接“IO”与“3.3V”。
-   **Power Supply**: 您必须从 J1（直流输入端口）给扩展板供电。输入电压范围可设置为直流 6V〜28V。板上 DC/DC 转换器可将直流输入电压转换为 5Vdc 输出电压，给逻辑电路供电。DC/DC 转换器也可以为微控制器板（Arduino / Seeeduino）供电，电压为 5V，最大电流为 **1000ma**。
-   **Motor Interface**：Out 1 和 Out 2(Out 3 和 Out 4) 连接直流电机 A(B)。  

!!!Caution
    不要在板子工作时触摸 H 桥或 PCB 板。它们高负荷下的温度最高可能超过 100°C。

使用方法
-----

 本示例展示了使用 Raspberry Pi B 和 Raspberry Pi Motor Driver Board v1.0 控制电机正反转。

### 硬件连接

- Raspberry Pi B 和 Raspberry Pi Motor Driver Board v1.0
- 按下图所示连接硬件。

连接好电源和网络。

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p6.jpg)

### 代码

1. 复制下面的代码。

```python
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

2. 在您自己的目录中将其保存为 **RPi_Motor_Shiled.py**。

3. 运行例程。Raspberry Pi Motor Driver Board v1.0 上的 LED1，LED2 会交替闪烁；同样的，LED3，LED4 也会交替闪烁。

    It means Out 1 and Out 2 (Out 3 and Out 4) connect Motor A(B) forward and back.这个表示 Out 1 和 Out 2 (Out 3 和 Out 4)连接的电机 A（B）正转和反转。

4. 您可以看到如下结果：

    串口监视器

      ![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p4.jpg)

        Raspberry Pi Motor Driver Board v1.0:
        绿色 LED 和蓝色 LED 交替闪烁。

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/img/Raspberry_Pi_Motor_Board_v1.0_p5.jpg)

资源下载
---------

-   **[Eagle 文件]**[Eagle file Raspberry Pi Motor Driver Board v1.0](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/Raspberry_Pi_Motor_Driver_Board_v1.0_sch_pcb_20150119.zip)
-   **[PDF 文件]**[PDF Raspberry Pi Motor Driver Board v1.0](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/Raspberry_Pi_Motor_Driver_Board_v1.0.pdf)
-   **[数据手册]**[MC33932VW Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/MC33932VW.pdf)
-   **[数据手册]**[TD1519A Datasheet](https://raw.githubusercontent.com/SeeedDocument/Raspberry_Pi_Motor_Driver_Board_v1.0/master/res/TD1519A.pdf)
