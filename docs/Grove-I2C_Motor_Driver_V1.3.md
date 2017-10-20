---
title: Grove - I2C Motor Driver V1.3
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-I2C-Motor-Driver-p-907.html
oldwikiname: Grove_-_I2C_Motor_Driver_V1.3
prodimagename: I2CMotorDriver_New.jpg
bzprodimageurl: https://statics3.seeedstudio.com/images/product/12Cmotor.jpg
surveyurl: https://www.research.net/r/Grove-I2C_Motor_Driver_V1_3
sku: 105020001
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2CMotorDriver_New.jpg)

Grove - I2C Motor Driver V1.3（最新版本）可以直接控制步进电机或直流电机。 它的核心是一个双通道 H 桥驱动芯片 （L298N） ，可以处理高达每通道 2A 的电流，由 Atmel ATmega8L 控制，它处理与 Arduino 等平台的 I2C 通信。 两台电机可以同时驱动，同时设定为不同的速度和方向。 它可以为两个有刷直流电机或一个 4 线制的两相步进电机供电。 它需要 6V 至 15V 电源为电机供电，并具有板载 5V 稳压器，可为 I2C 总线和 Arduino 供电（可由跳线选择）。 所有驱动线路都受到反电动势的二极管保护。

与 [Grove - I2C motor driver V1.2](http://wiki.seeed.cc/Grove-I2C_Motor_Driver_V1.2/)对比， V1.3 使用户能够更轻松地控制步进电机。 您不需要一直控制步进器，只需发送命令到I2C motor driver V1.2驱动步进电机，它将作为您的命令，这将节省您的 Arduino 资源并简化您的代码。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5335d5b70kEV47&id=45476447918)

版本信息
---------------

| 版本| 版本描述                                | 发布时间      |
|----------|-------------------------------------------------|----------------|
| v1.0     |  首次公开发布                          | 2012年5月17日 |
| v1.2     | 修改由硬件设置的 I2C 地址          | 2012年7月2日|
| v1.3     | 修改固件以支持离线 Stepper | 2013年2月18日 |


产品特性
--------

-   Grove 兼容
-   I2C 接口
-   可调电机转速和转动方向
-   硬件可更改从站地址

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

  规格参数
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
标准值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr>
<th scope="row">
工作电压
</th>
<td>
6
</td>
<td align="center" >
-
</td>
<td>
15
</td>
<td>
VDC
</td>
</tr>
<tr>
<th scope="row">
单通道最大输出电流
</th>
<td colspan="3" align="center">
0.5
</td>
<td>
A
</td>
</tr>
<tr>
<th scope="row">
最大总电流
</th>
<td colspan="3" align="center" >
1.0
</td>
<td>
A
</td>
</tr>
<tr>
<th scope="row">
I2C 总线上的输入/输出电压
</th>
<td colspan="3" align="center" >
5
</td>
<td>
V
</td>
</tr>
<tr>
<th scope="row">
通讯协议
</th>
<td colspan="3" align="center" >
I2C
</td>
<td>
/
</td>
</tr>
</table>

支持平台
-------------------

硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2CMotorDriver-1.jpg)
**78M05 IC:**  5V 稳压器

**L298 IC:** 双全桥驱动

**ATmega8 IC:** 控制电机旋转.

<div class="admonition note">
<p class="admonition-title">注意</p>
螺丝端子上的输入电压调节到 5V ，并通过跳线 （J4） 连接到 I2C的  + 5V 。 如果使用螺丝端子的外部电源和 I2C 接头连接的电源，请拆下跳线。 如果将 5V 提供给 I2C 总线，则使用跳线。
</div>

创意应用
-----------------

-   机器人
-   家用 RC 车
-   风扇
-   大功率LED照明总线。
<div class="admonition danger">

<p class="admonition-title">警告</p>
该板在工作电流超过 1A 时板子将会非常热。 请勿触摸！
</div>


入门
-----

I2C Motor Driver 可以控制基于芯片 L298 的电机。 L298 不仅是双电机驱动器，它是双 H 桥。  h 桥基本上是一个特定的晶体管设置，允许您切换电流方向。 连接电机意味着您可以沿双向旋转; 通过 PWM 输入，您可以使用 Arduino 以任意速度旋转。 因为 L298 有2个 H 桥，所以你可以通过在不同的方向上旋转每个轮子来使机器人转动，当然也可以向前和向后旋转。

###  1. 安装库
- 如果您是第一次安装Arduino库文件，请点击 [这里](http://seeed.wiki/How_to_install_Arduino_Library/) 查看库文件的安装方法。

直接运行命令或或者下载[zip 文件](https://github.com/Seeed-Studio/Grove_I2C_Motor_Driver_v1_3/archive/master.zip)

```
  git clone https://github.com/Seeed-Studio/Grove_I2C_Motor_Driver_v1_3.git

```



- 只需将 Grove_I2C_Motor_Driver_v1_3 文件夹复制到 Arduino 库集合中即可。 例如， arduino-1.6.12 / 库。 下次运行 Arduino IDE 时，您将在 **file(文件) - >Sketch - > Include Library - > Grove_I2C_Motor_Driver_v1_3**  中添加一个新选项。 在 Grove_I2C_Motor_Driver_v1_3 中查看包含的示例。 我们提供直流和步进电机控制示例。
![](https://github.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/raw/master/img/library%20example.jpg)

### 2. 设置 I2C 电机驱动程序的地址

- 通过拨号开关设置地址是添加到新的 I2C 电机驱动程序的新功能。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2CMotorDriver-9.jpg)

- 然后将程序中的地址设置与 I2C 电机驱动程序上的地址设置保持一致。 程序中的默认地址设置为 0x0f 。

```
// default I2C address is 0x0f
#define I2C_ADDRESS 0x0f

void setup()
{
    Motor.begin(I2C_ADDRESS);
}
```

### 3. 驱动 2 台直流电机


![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2CMotorDriver-4.jpg)

<div class="admonition note">
<p class="admonition-title">注意</p>
首先要注意的是，您需要一个外部电源作为您的直流电机。  Arduino 上的 5V 引脚无法提供足够的电力来驱动 2 个电机，否则可能会损坏 Arduino 。
</div>

- 控制直流电机有两项功能：

```

// Set the speed of a motor, speed is equal to duty cycle here
void speed(unsigned char motor_id, int _speed);

// Stop one motor
void stop(unsigned char motor_id);

```

使用 speed（）功能，您可以按所需的速度驱动一台电机。

- **motor_id**  表示要使用的电机。 您可以填写 MOTOR1 或 MOTOR2 。


- **_speed**  表示您设置到电机的速度。 你可以在这里填 -100〜100。 当_speed> 0时，直流电机顺时针运行，而_speed <0时，直流电机逆时针运转。 而_speed的绝对值越大，直流电机的速度越快。

使用 stop（）功能，您可以停止正在运行的直流电动机。

- **motor_id** 表示要使用的电机。 您可以填写 MOTOR1 或 MOTOR2 。


### 4. 驱动步进电机

以 [24BYJ48 步进电机](http://www.seeedstudio.com/depot/high-quality-stepper-motor-12v-p-335.html?cPath=170_171)为例，硬件安装如下图所示：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2C_Motor_Driver_control_a_Stepper_Motor.jpg)

[24BYJ48](http://www.seeedstudio.com/depot/high-quality-stepper-motor-12v-p-335.html?cPath=170_171) 步进电机和 I2C 电机驱动器之间的连接如下所示：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/img/I2C_Motor_Driver_Connector.jpg)


- 我们提供一个驱动步进电机的功能。

```
// Drive a stepper motor
void StepperRun(int _step);
```

**_step**  表示您设置为步进电机运行的步骤。 可以填-1024〜1024。 当_step> 0时，步进电机顺时针运行，而_step <0时，步进电机逆时针运行。 当_step为512 / -512时，步进电机将运行一整圈，如果_step为1024 / -1024，则步进电机将运行2圈。 步进电机在完成步骤后会自动停止。

资源下载
---------

-   [Grove - I2C Motor Driver V1.3 in Eagle Format](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/res/Grove-I2C_Motor_Driver_v1.3_Eagle_File.zip)
-   [Grove - I2C Motor Driver V1.3 PCB in PDF Format](https://github.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/raw/master/res/Grove%20-%20I2C%20Motor%20Driver%20%20v1.3b%20PCB.pdf)
-   [Grove - I2C Motor Driver V1.3 Schematic in PDF Format](https://github.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/raw/master/res/Grove%20-%20I2C%20Motor%20Driver%20%20v1.3b.pdf)
-   [Grove - I2C Motor Driver V1.3 Library](https://github.com/Seeed-Studio/Grove_I2C_Motor_Driver_v1_3)
-   [L298 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/res/L298datasheet.pdf)
-   [78M05 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/res/ST_78M05DataSheet.pdf)
-   [On-Chip Firmware for I2C motor driver](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_Motor_Driver_V1.3/master/res/On-Chipfirmware_for_Motor_driver.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_I2C_Motor_Driver_V1.3 -->
