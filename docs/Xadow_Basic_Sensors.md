---
title: Xadow Basic Sensors
category: RePhone
bzurl: https://www.seeedstudio.com/Xadow-Basic-Sensors-p-2555.html
oldwikiname: Xadow - Basic Sensors
prodimagename: Xadow_Basic_Sensors.JPG
wikiurl: http://seeed.wiki/Xadow_Basic_Sensors
sku: 101040006
---

---
![](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/images/Xadow_Basic_Sensors.JPG)

Xadow Basic Sensors 在一块单板上集成了三种不同的传感器：
- 3轴加速度计，用于运动检测，活动监测和速度跟踪
- 双二极管数字光传感器，可以单独测量红外，全光谱或人类可见光
- 用于温度监测的温度传感器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1b204534n0gGsT&id=534578911525)

## 产品特性
---
- 板载三种传感器
- 配合 RePhone Kit Create 使用时即插即用
- 开源和模块化设计
- 小而薄
- 内置 11 PIN Xadow 接口，可与其他 Xadow 模块灵活连接
- 可堆叠，可连接并可与其他Xadow模块焊接使用

## 规格参数
---
**概述**

|项目|值|
|---|---|
|微控制器	|STM32F030F4
|核心|	ARM® 32-bit Cortex® -M0 CPU
|供电|	3.3 ~ 6 V (通过外接引脚)
|Flash	|16 KB
|SRAM|	4 KB
|时钟频率|	48 MHz
|使用温度范围|-30°C to 70°C
|通信接口|	与 Xadow GSM+BLE 通过 I2C通信（7-bit 地址 0x03）
|尺寸	|25.37mm × 20.30mm / 1” × 0.8”

**3 轴加速度计 (ADXL345)**

|项目|值|
|---|---|
|g 值测量范围|	±2g (默认), ±4g, ±8g, or ±16g
|分辨率|	随着测量 g 值范围的增加，在测量 ±16g 范围时达到最高分辨率 13-bit。

**数字光线传感器 (TSL2561) -- 接近人眼的范围**

|项目|值|
|---|---|
|动态范围 (Lux)|	0.1 到 40,000 Lux
|双光电二极管	|红外和全光谱

**温度传感器 (LM75ADP)**

|项目|值|
|---|---|
|测量温度范围|	-55°C to 125 °C
|精确度	|-25°C 到 100°C 范围时 ± 2°C <br>-55°C 到 25°C 范围和 100 °C 到 125°C 范围时 ± 3°C|

## 硬件概述
---
![](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/images/Xadow_Basic_Sensors.png)

## 配合 RePhone Kit Create 使用
---
**获取传感器数据**

在没编程的情况下您可以把它连接到“RePhone Kit Create”的核心模块(Xadow GSM+BLE)上读取传感器的数据。

![](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/images/Xadow_Basic_Sensors_Sensor_Value.png)

**设置触发条件**

您还可以将传感器数据设置为触发音频，LED 矩阵和 LED 灯条等执行器的条件，或触发打电话和发送信息等操作。

![](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/images/Xadow_Basic_Sensors_Set_Sensor_Condition.png)

## RePhone Community
---
[![](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/images/300px-RePhone_Community-2.png)](http://www.seeed.cc/discover.html?t=RePhone)

We’ve been looking for a better place where our backers (RePhone Users) can sit together, warmly and comfortably, have conversations about RePhone, discuss technical problems, share ideas/projects, and give feedback on the modules’ development in the future. And then here we go, the [RePhone Community](http://www.seeed.cc/discover.html?t=RePhone).

Now join us in the [RePhone Community](http://www.seeed.cc/discover.html?t=RePhone)! Together we seek answers, make interesting stuff, care about each other, and share our experiences.


## 资源下载
---

- **[代码]**[Source Code for Xadow Basic Sensors](https://github.com/WayenWeng/Xadow_Basic_Sensors/)
- **[原理图]**[Xadow Duino Schematic Files](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/resources/202000745_PCBA%3BXadow%20Basic%20Sensors%20v1.0_schemic%20file.zip)
- **[数据手册]**[ADXL345 - 3_Axis Acceserometer](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/res/ADXL345-3_Axis_Acceserometer.pdf)
- **[数据手册]**[LM75A NXP - Temperature Sensor](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/res/LM75A_NXP-Temperature_Sensor_.pdf)
- **[数据手册]**[TSL2561 - Light Sensor](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/res/TSL2561-Light_Sensor_.pdf)
- **[数据手册]**[STM32F030F4](https://github.com/SeeedDocument/Xadow_Basic_Sensors/raw/master/res/STM32F030F4.pdf)
