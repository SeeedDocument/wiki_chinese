---
name: Motor Shield V2.0
category: Shield
bzurl: https://www.seeedstudio.com/Motor-Shield-V2.0-p-1377.html
oldwikiname: Motor_Shield_V2.0
prodimagename: 500px-Motorshield_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Motor_Shield_V2.0
sku: 105030001
tags: io_5v, plat_duino
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Motor_Shield_V2.0/master/image/500px-Motorshield_01.jpg)

!!!Note
    本文档适用于 Motor Shield V2.0/2.1/2.2.

Motor Shield 是电机的驱动模块，您可以使用 Arduino 来控制电机的工作速度和方向。基于 Dual Full-Bridge Drive Chip L298，它可以驱动两个直流电机或步进电机。The Motor Shield 既可以直接由 Arduino 供电，也可以由外部 6V~15V 电源通过端子输入供电。该模块可用于微型机器人和智能车辆等的开发。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=45491175129)


版本日志
---------------

| 版本号 | 说明                                    | 发布日期        |
|----------|-------------------------------------------------|----------------|
| v1.0| 首次公开发布| NA |
| v2.0| Arduino/Seeeduino 的 **+5V** 引脚能为电机供电 | 2013-2  |




## 产品特性
-------------------
- 标准的 Arduino UNO Shield 引脚分布
- 基于 L298 full bridge IC
- 驱动 2 个直流电机或步进电机
- 外部电源输入可用
- LED 指示灯
- 具有散热器可以及时散热，提高持续工作能力
- Arduino 库


## 规格参数
-------------------

|项目   |参数|
|:------|:-----------------|
|工作电压   |	5V |
|外部电源	|6-15V  |
|输出电流 	|2.0A Max @ 每个通道  |
|PWM 范围	 |0-100% |
|输出    |2 通道, 4 端口|


## Platforms Supported
-------------------


## 兼容性
-------------------

我们研发了许多扩展板，可以使您的平台板更加强大，但是并不是所有的扩展板都兼容所有的平台板，这里我们用一张表来说明这些板与平台板的兼容性。

!!!Note
    请注意，“不推荐”意味着它可能与平台板兼容，但需要额外的工作，如跳线或重写代码。如果您有兴趣发掘更多信息，欢迎与 techsupport@seeed.cc.联系。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 硬件概述
-------------------

![](https://raw.githubusercontent.com/SeeedDocument/Motor_Shield_V2.0/master/image/700px-MotorShieldHardware.png)

**1**.通道 1 指示，包括 3 lED

- EB - 通道 1 使能，高电平有效
- IN3 - OUT3 状态
- IN4 - OUT4 状态

**2**.通道 1 感应 - 请连接左边的 2 个引脚以正常使用。

!!!Note
    这是感应电流的高级应用，请参考数据表和原理图了解更多信息。

**3**.输出 - 有两个通道，每个通道有两个输出

- 通道 0 - OUT1, OUT2
- 通道 1 - OUT3, OUT4

**4**.通道 0 感应

**5**.通道 0 指示，包括 3 lED

- EB - 通道 0 使能，高电平有效
- IN1 - OUT1 状态
- IN2 - OUT2 状态

**6**.外部电源输入，范围为 6-15V

**7**.重置指示灯 - 按下重置按钮时变为红色

**8**.重置按钮 - 按下重置扩展板和 Arduino

**9**.电源指示灯 - 上电后变绿，无论内外部供电

**A.** 电源开光

- 连接 - Arduino 供电
- 断开 - 外部电源供电

**B.** 标准的 Arduino UNO Shield 引脚分布

### 数字引脚功能
|Arduino 引脚   |功能        |
|:------|:-----------------|
|D0   |	未使用       |
|D1	|未使用           |
|D2 	|未使用    |
|D3	    |未使用  |
|D4    |未使用 |
|D5    |未使用 |
|D6    |未使用 |
|D7    |未使用 |
|D8    |**OUT1** |
|D9    |**通道 0 使能** |
|D10    |**通道 1 使能** |
|D11    |**OUT2** |
|D12    |**OUT3**|
|D13    |	**OUT4** |

!!!Note
    Motor Shield 使用 D8~D13。请不要使用这些引脚。

### 模拟引脚功能
|Arduino 引脚   |功能        |
|:------|:-----------------|
|D0   |	未使用       |
|D1	|未使用           |
|D2 	|未使用    |
|D3	    |未使用  |
|D4    |未使用 |
|D5    |未使用 |


!!!Note
    未使用表示您可以随意使用这些引脚。

## 入门指导
-------------------
### 驱动一个直流电机

#### 连接

现在我们将通过一个简单的演示向您展示 Motor Shield 的工作原理。首先，您需要准备下列器材:

| Seeeduino V4 | DC Motor | Motor Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/image/130%20DC%20Motor_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/image/motor%20shield_s.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.44466619EsP2NP&id=45721222112)|[点击购买](https://www.seeedstudio.com/130-DC-Motor-p-2023.html)|[点击购买](https://item.taobao.com/item.htm?id=45491175129)|

- 设置 **SEN_A** 和 **SEN_B**，用跳线帽将左侧的 2 个引脚连接在一起。
- 用跳线帽连接 **MB_EN** ，因为我们不使用外部电源。
- 将直流电机连接到通道 0 (OUT1 和 OUT2)。
- 将 Motor Shield 堆叠在 Arduino 上。
- 通过 USB 线缆将 Arduino 连接到 PC。

![](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/image/DC%20connection.jpg)

#### 软件部分

- 点击下面的按钮下载 Motor Shield 库文件。
- 遵循 [这里](http://wiki.seeed.cc/How_to_install_Arduino_Library/) 的步骤来安装库。

[![](https://raw.githubusercontent.com/SeeedDocument/Motor_Shield_V2.0/master/image/400px-Motor_shield_v2_library.png)](https://github.com/Seeed-Studio/SeeedMotorShieldV2/archive/master.zip)

- 上传代码到 Seeeduino。

```c
//  Demo function:The application method to drive the DC motor.
//  Author:Loovee (luweicong@seeed.cc)
//  2016-3-11

#include "MotorDriver.h"

MotorDriver motor;

void setup()
{
    // initialize
    motor.begin();
}

void loop()
{
    motor.speed(0, 100);            // set motor0 to speed 100
    delay(1000);
    motor.brake(0);                 // brake
    delay(1000);
    motor.speed(0, -100);           // set motor0 to speed -100
    delay(1000);
    motor.stop(0);                  // stop
    delay(1000);
}
// END FILE
```
- 然后您会发现电机正转 (1s)，停止 (1s)，反转 (1s)，停止 (1s) 的循环。

如果电机没有任何动作，请确保 :

- 已成功上传代码
- 电机正确连接
- LED 指示灯正常闪烁

### 驱动一个步进电机

#### 连接

现在我们将通过一个简单的演示向您展示 Motor Shield 的工作原理。首先，您需要准备下列器材:

| Seeeduino V4 | Stepper Motor | Motor Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/image/Motor%2024BYJ48_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/image/motor%20shield_s.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.44466619EsP2NP&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.56.3283b8c7vHNGRJ&id=534734937446)|[点击购买](https://item.taobao.com/item.htm?id=45491175129)|



- 设置 SEN_A 和 SEN_B，用跳线帽将左侧的 2 个引脚连接在一起。
- 用跳线帽连接 MB_EN ，因为我们不使用外部电源。
- 将 Stepper 的引脚连接到 Motor Shield 的 OUTPUT。如下图所示 :

|Stepper   |Motor Shield  |
|:------|:-----------------|
|A+   |	OUT1  |
|A-	|OUT2  |
|B+ 	|OUT3  |
|B-    |OUT4 |

- 将 Motor Shield 堆叠在 Arduino 上。
- 通过 USB 线缆将 Arduino 连接到 PC。

#### 软件部分

将下面的代码复制到 Arduino IDE 并上传到 Seeeduino，然后您会发现步进电机转动。

```c
/*
 * Stepper test for Seeed Motor Shield V2
 * loovee @ 15 Mar, 2016
 */

#include <Stepper.h>

// change this to the number of steps on your motor
#define STEPS 200

// create an instance of the stepper class, specifying
// the number of steps of the motor and the pins it's
// attached to
Stepper stepper(STEPS, 8, 11, 12, 13);

// the previous reading from the analog input
int previous = 0;

void step(int steps)
{
    digitalWrite(9, HIGH);
    digitalWrite(10, HIGH);
    stepper.step(steps);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
}

void setup()
{
    // set the speed of the motor to 30 RPMs
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    stepper.setSpeed(30);
}

void loop()
{
    step(1000);
    step(-1000);
}

// END FILE
```
如果电机没有任何动作，请仔细检查连线是否正确。

## 函数库 APIs
---------

### DC Motor APIs:

#### begin (开始)

**描述**

```c
void begin();
```
#### speed (速度)
**描述**

```c
void move(int motor_id, int speed);
```
- motor_id
  - 0 - Chanel 0
  - 1 - Chanel 1
- 转速 : -100~100，越大越块，0 停转

#### stop (停车)
**描述**

```c
void stop(unsigned char motor_id);
```
#### brake (刹车)
**描述**

```c
void brake(unsigned char motor_id);
```
#### 步进电机
!!!Note
    使用 Arduino IDE 提供的库来驱动步进电机。有些东西需要修改，请参考示例。

## 资源下载
-------------------
- **[Eagle 文件]** [ Motor Shield V2.0 Eagle File ](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/Motor_Shield_Eagle_File.zip)
- **[Eagle 文件]** [Motor shield V2.1 Eagle File ](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/Motor_shield_2.1.rar)
- **[原理图 PDF]** [Motor Shield 2.0 schematics](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/Motor_shield_2.0.pdf)
- **[原理图 PDF]** [Motor Shield 2.1 schematics](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/Motor_shield_2.1.pdf)
- **[原理图 PDF]** [Motor Shield 2.2 schematics](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/Motor%20Shield%20v2.2.pdf)
- **[库文件]** [Motor Shield Library](https://github.com/Seeed-Studio/SeeedMotorShieldV2/archive/master.zip)
- **[芯片数据手册]** [L298 Datasheet](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/L298.pdf)
- **[芯片数据手册]** [78M05 Datasheet](https://github.com/SeeedDocument/Motor_Shield_V2.0/raw/master/resource/78M05_datasheet.pdf)
