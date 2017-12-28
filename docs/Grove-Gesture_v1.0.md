---
title: Grove - Gesture V1.0
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Gesture-p-2463.html
oldwikiname: Grove - Gesture V1.0
prodimagename: Breakout_for_LinkIt_Smart_7688_v2.0_product_view_700.jpg
urlwiki: http://seeed.wiki/Grove-Gesture_v1.0/
sku: 101020083
---

---
![](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/img/400px-Gesture_sensor_3.png)

Grove - Gesture上的传感器是将手势识别功能与通用 I2C 接口集成到单个芯片中的 PAJ7620U2 。 它可以识别 9 种基本手势，并且可以通过 I2C 总线简单地访问这些手势信息。

应用：您可以使用手势作为输入设备来控制另一个 Grove 执行单元 ，或者计算机，手机，智能车，机器人等，只需轻轻一按即可。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3dd91d1pq00iU&id=520252964566)

## 产品特性
---
 - 内置检测
 - 主板支持：Arduino UNO / Seeeduino / Arduino Mega2560
 - 9 种基本手势
  - 向上
  - 向下
  - 向左
  - 向右
  - 向前
  - 向后
  - 顺时针
  - 逆时针
  - 挥手

!!!Tip
    关于 Grove 模块的更多细节请参考 [Grove System](http://wiki.seeed.cc/Grove_System/)


## 规格参数
---
|项目名称|参数|
|---|---|
|传感器|PAJ7620U2|
|电源 |5V
 |环境光强	 |< 100k Lux
 |正常模式下的手势速度|	 60°/s 到 600°/s
 |游戏模式下的手势速度|	 60°/s 到 1200°/s
 |接口类型 IIC 接口 |取决于400 kbit/s
 |工作温度	| -40°C到 +85°C
 |外形尺寸|	20 x20mm
 |检测范围|5-10cm

## 使用 Arduino/Seeeduino

推荐阅读入门
- [下载 Arduino 并安装 Arduino 驱动程序](http://wiki.seeedstudio.com/wiki/Download_Arduino_and_install_Arduino_driver)
- [Seeed入门指导](http://seeed.wiki/Getting_Started_with_Seeeduino/)

**硬件安装**

Grove 产品具有一种经济性的系统，并且都具有相同的连接器，可以连接[Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)。 将此模块连接到 Base Shield 的 **I2C** 端口，如果没有 Base Shield ，您也可以通过跳线将 Grove-Gesture 直接连接到 Arduino 。

|Arduino UNO|	Base Shield	|Grove - Gesture|
|---|---|---|
|5V	|I2C 端口|	VCC|
|GND|I2C 端口	|GND|
|SDA|I2C 端口	|SDA|
|SCL|I2C 端口	|SCL|
|Digit 2	|未连接|	INT (Reserved pad)|

INT：手势检测中断标志掩码。 您可以使用跳线将 INT PAD 连接到 Arduino 的 **Digit 2** 。

下图显示了如何将 Grove - Gesture 连接到 Base shield 的 **I2C** 端口上

![](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/img/700px-Gesture_install_1.png)

然后将 Base shield 连接到 Arduino UNO 上

![](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/img/700px-Gesture_install_2.png)


**Gesture 库**

我们创建了一个库，以帮助您快速开始使用 Seeeduino / Arduino ，在本节中，我们将向您展示如何设置库并介绍一些功能。

创建

- [从 Gesture_PAJ7620 github 页面将库代码作为zip文件下载](https://github.com/Seeed-Studio/Gesture_PAJ7620).
- 将下载的文件解压缩到 ... / arduino / libraries 中。
- 重命名解压缩的文件夹 "Gesture"(或:"Gesture_PAJ7620")
- 启动 Arduino IDE（如果打开，请重新启动）。

**简单演示**

以下简单的演示将向您展示一个非常简单的应用：当您向上移动时，红色的LED将被打开，反之红色的LED将被关闭。

```c
#include <Wire.h>
#include "paj7620.h"

void setup()
{
  paj7620Init();
}

void loop()
{
	uint8_t data = 0;  // Read Bank_0_Reg_0x43/0x44 for gesture result.

	paj7620ReadReg(0x43, 1, &data);  // When different gestures be detected, the variable 'data' will be set to different values by paj7620ReadReg(0x43, 1, &data).

	if (data == GES_UP_FLAG) 	    // When up gesture be detected,the variable 'data' will be set to GES_UP_FLAG.
		digitalWrite(4, HIGH);      // turn the LED on (HIGH is the voltage level)
	if (data == GES_DOWN_FLAG) 	    // When down gesture be detected,the variable 'data' will be set to GES_DOWN_FLAG.
        digitalWrite(4, LOW);       // turn the LED off by making the voltage LOW
```

![](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/img/IMG_0029.gif)

**功能描述**

这些是库中最重要/最有用的功能，您可以自己查看 .h 和 .cpp 文件，以查看所有可用的功能。

**1.初始化手势传感器芯片PAJ7620**

```c
void setup()
{
  paj7620Init();
}
```

这个初始化代码应该添加到每个演示。

**2.通过 I2C 从 PAJ7620 寄存器读取数据**
- paj7620ReadReg(uint8_t addr, uint8_t qty, uint8_t data[])
 - addr: 注册地址
 - qty: 读取的数据数量，注册地址不断增加。
 - data[]: 起始地址（一个变量或数组）来存储数据。

```c
 void loop()
 {
 	uint8_t data = 0;  // Read Bank_0_Reg_0x43/0x44 for gesture result.

 	paj7620ReadReg(0x43, 1, &data);  // When different gestures be detected, the variable 'data' will be set to different values by paj7620ReadReg(0x43, 1, &data).

 	if (data == GES_UP_FLAG) 							// When up gesture be detected,the variable 'data' will be set to GES_UP_FLAG.
 		digitalWrite(4, HIGH);   				        // turn the LED on (HIGH is the voltage level)
 	if (data == GES_DOWN_FLAG) 						// When down gesture be detected,the variable 'data' will be set to GES_DOWN_FLAG.
         digitalWrite(4, LOW);   					    // turn the LED off by making the voltage LOW
 }
```
- 我们定义手势的一些注册数据，请参考下表。

|手势| 注册数据| 注册地址| 是| 不是|
|----|---|---|---|---|
|向上	|data==GES_UP_FLAG|	0x43	|检测到手势	|未检测到手势	|
|向下|	data==GES_DOWN_FLAG|0x43	|检测到手势		|未检测到手势	|
|向左|	data==GES_LEFT_FLAG|0x43	|检测到手势		|未检测到手势	|
|向右|	data==GES_RIGHT_FLAG|0x43	|检测到手势		|未检测到手势	|
|向前	|data==GES_FORWARD_FLAG|0x43	|检测到手势		|未检测到手势	|
|向后|	data==GES_BACKWARD_FLAG|0x43	|检测到手势		|未检测到手势	|
|顺时针|	data==GES_CLOCKWISE_FLAG|0x43	|检测到手势		|未检测到手势	|
|逆时针	|data==GES_COUNT_CLOCKWISE_FLAG|0x43	|检测到手势		|未检测到手势	|
|挥手|	data==GES_WAVE_FLAG|	0x44|检测到手势		|未检测到手势	|


**手势示例/应用程序**

这些例子将告诉你如何识别这个 Grove 手势的手势。]

- 打开文件
- **File（文件）>example（示例） - > Gesture_PAJ7620-> example-> paj7620_9** 创建一个新的编辑程序。

**说明**：本示例可以识别 9 个手势并输出结果，包括向上移动，向下移动，向左移动，向右移动，向前移动，向后移动，顺时针，逆时针和挥手。 您也可以使用手势作为输入设备来控制另一个 grove ，电脑，手机，智能车，机器人等，只需轻轻一按即可。

!!!Note
    当您想要识别向前/向后的手势时，您的手势的反应时间必须小于GES_ENTRY_TIME（0.8s）。 您还可以根据实际情况调整反应时间。

```
/*
Notice: When you want to recognize the Forward/Backward gestures, your gestures' reaction time must less than GES_ENTRY_TIME(0.8s).
        You also can adjust the reaction time according to the actual circumstance.
*/

#define GES_REACTION_TIME		500	// You can adjust the reaction time according to the actual circumstance.
#define GES_ENTRY_TIME			800	// When you want to recognize the Forward/Backward gestures, your gestures' reaction time must less than GES_ENTRY_TIME(0.8s).
#define GES_QUIT_TIME			1000
```

以下是演示中使用的主要程序：

```c
void setup()
{
	uint8_t error = 0;

	Serial.begin(9600);
	Serial.println("\nPAJ7620U2 TEST DEMO: Recognize 9 gestures.");

	error = paj7620Init();			// initialize Paj7620 registers
	if (error)
	{
		Serial.print("INIT ERROR,CODE:");
		Serial.println(error);
	}
	else
	{
		Serial.println("INIT OK");
	}
	Serial.println("Please input your gestures:\n");
}

void loop()
{
	uint8_t data = 0, data1 = 0, error;

	error = paj7620ReadReg(0x43, 1, &data);				// Read Bank_0_Reg_0x43/0x44 for gesture result.
	if (!error)
	{
		switch (data) 									// When different gestures be detected, the variable 'data' will be set to different values by paj7620ReadReg(0x43, 1, &data).
		{
			case GES_RIGHT_FLAG:
				delay(GES_ENTRY_TIME);
				paj7620ReadReg(0x43, 1, &data);
				if(data == GES_FORWARD_FLAG)
				{
					Serial.println("Forward");
					delay(GES_QUIT_TIME);
				}
				else if(data == GES_BACKWARD_FLAG)
				{
					Serial.println("Backward");
					delay(GES_QUIT_TIME);
				}
				else
				{
					Serial.println("Right");
				}
				break;
			case GES_LEFT_FLAG:
				delay(GES_ENTRY_TIME);
				paj7620ReadReg(0x43, 1, &data);
				if(data == GES_FORWARD_FLAG)
				{
					Serial.println("Forward");
					delay(GES_QUIT_TIME);
				}
				else if(data == GES_BACKWARD_FLAG)
				{
					Serial.println("Backward");
					delay(GES_QUIT_TIME);
				}
				else
				{
					Serial.println("Left");
				}
				break;
			case GES_UP_FLAG:
				delay(GES_ENTRY_TIME);
				paj7620ReadReg(0x43, 1, &data);
				if(data == GES_FORWARD_FLAG)
				{
					Serial.println("Forward");
					delay(GES_QUIT_TIME);
				}
				else if(data == GES_BACKWARD_FLAG)
				{
					Serial.println("Backward");
					delay(GES_QUIT_TIME);
				}
				else
				{
					Serial.println("Up");
				}
				break;
			case GES_DOWN_FLAG:
				delay(GES_ENTRY_TIME);
				paj7620ReadReg(0x43, 1, &data);
				if(data == GES_FORWARD_FLAG)
				{
					Serial.println("Forward");
					delay(GES_QUIT_TIME);
				}
				else if(data == GES_BACKWARD_FLAG)
				{
					Serial.println("Backward");
					delay(GES_QUIT_TIME);
				}
				else
				{
					Serial.println("Down");
				}
				break;
			case GES_FORWARD_FLAG:
				Serial.println("Forward");
				delay(GES_QUIT_TIME);
				break;
			case GES_BACKWARD_FLAG:
				Serial.println("Backward");
				delay(GES_QUIT_TIME);
				break;
			case GES_CLOCKWISE_FLAG:
				Serial.println("Clockwise");
				break;
			case GES_COUNT_CLOCKWISE_FLAG:
				Serial.println("anti-clockwise");
				break;
			default:
				paj7620ReadReg(0x44, 1, &data1);
				if (data1 == GES_WAVE_FLAG)
				{
					Serial.println("wave");
				}
				break;
		}
	}
	delay(100);
}
```

在您自己的项目中，您可能需要多个手势而不是单个手势来实现一个功能，欢迎分享！
## 资源下载
---
- [Grove - Gesture_v1.0 sch pcb.zip](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/resources/Grove_-_Gesture_v1.0_sch_pcb.zip)
- [PAJ7620U2_Datasheet_V0.8_20140611.pdf](https://github.com/SeeedDocument/Grove_Gesture_V_1.0/raw/master/resources/PAJ7620U2_Datasheet_V0.8_20140611.pdf)
- [Library Grove - Guesture](https://github.com/Seeed-Studio/Gesture_PAJ7620)
