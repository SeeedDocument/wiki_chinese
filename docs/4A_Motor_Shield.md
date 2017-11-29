---
title: 4A Motor Shield
category: Shield
bzurl: https://www.seeedstudio.com/4A-Motor-Shield-p-1954.html
oldwikiname:  4A_Motor_Shield
prodimagename: 4A_Motor_Shield_top.jpg
wikiurl: http://seeed.wiki/4A_Motor_Shield
sku: 105030004
tags: io_5v, plat_duino
---

![](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/img/4A_Motor_Shield_top.jpg)

4A Motor Shield 基于飞思卡尔 MC33932 双 H 桥功率 IC，可控制电机负载，每路电流峰值高达 5.0A。它可以让你用 Arduino/Seeeduino 板驱动两个直流电机，独立控制每个电机的速度和方向。您还可以测量每个电机的电机电流以及其他功能。板载 DC/DC 转换器支持很宽的输入电压范围，可以为单片机提供 5V 电源和 100mA 最大电流，所以只需要一个电源就可以驱动电机和为开发板上电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=45557268845)

## 规格参数
---

- 工作电压：6V~28V
- 5V 引脚输出：5V，100mA
- 输出电流（每个通道）：2A（连续工作）/ 5A（峰值）
- 输出占空比范围：0%~100%
- 输出短路保护（对 VPWR 或 GND 短路）
- 通过内部恒定关断时间 PWM 进行过流限制（调节）
- 温度过高电流降低保护

## Platforms Supported
-------------------

## 接口
---

![](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/img/4a_motor_shield_top_view.jpeg)

**①：J1:** 直流输入接口。

**②：J2:** 电机接口。

**③：EN,FT:** EN 使能和故障检测焊盘。如果短路 EN 焊盘，EN 信号连接到 D4 引脚，则可以通过D4引脚禁用 H 桥输出或复位故障标志。如果短路 FT 焊盘，FT 信号连接到 D3 引脚，您可以从 D3 引脚读取故障标志。

**④: IO:** 逻辑电压电平选择跳线。您可以从这个跳线选择控制逻辑电平。默认连接 5V，如果需要选择 3.3V 电压，请先用小刀或其他锋利物品划开“IO”和“5V”之间的连接（请仔细观察），并用万用表等器材确认断开。然后焊接连接“IO”与“3.3V”。

**⑤：IA,IB:** 电流传感器焊盘。如果需要检测电机电流，则必须将这些焊盘短路。电机电流将转换为电压信号，并可从 A0，A1 引脚读取。

**供电：** 您必须从 J1（直流输入端口）给扩展板供电。输入电压范围可设置为直流 6V〜28V。板上 DC/DC 转换器可将直流输入电压转换为 5Vdc 输出电压，给逻辑电路供电。DC/DC 转换器也可以为微控制器板（Arduino / Seeeduino）供电，电压为 5V，最大电流为 100ma。

**电机接口** Out 1 和 Out 2(Out 3 和 Out 4) 连接直流电机 A(B)。  

!!!Warning
    不要在板子工作时触摸 H 桥或 PCB 板。它们全负荷下的温度最高可能超过 100°C。

## 示例

### 驱动直流电机

把直流电机连接到 Motor Shield 的输出引脚 **OUT1** 和 **OUT2** (或者连接**OUT3** 和 **OUT4**)。然后把直流电源连接到驱动板上的电源输入接口。电机驱动板可以输出 5V 电压给 seeeduino 供电。然后把驱动板插在 [Seeedunio](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-14858770850.14.21fc5018bJodS7&id=45721222112&scene=taobao_shop) 上。把 Seeedunio 连接到电脑上。

![](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/img/Drive_DC_Motor.png)  

点击 [Motor Shield Library](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/res/MotorDriver20121210.zip) 下载库文件。然后把这个压缩包添加进 Arduino 库中。点击 **File(文件)->Example(示例)->MotorDrive->DCMotorDemo** 打开例程并上传。

这个演示使电机在一个方向旋转 2 秒钟，停止 1 秒钟，反向旋转 2 秒钟。


![](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/img/DC_Motor_Code.jpg)  


## 资源下载

- **[Eagle 文件]**[Schematic pdf](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/res/4A_MOTOR_Shield_v1.0.pdf)  
- **[Eagle 文件]**[Eagle File](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/res/4A_MOTOR_Shield_v1.0.zip)  
- **[库文件]**[Motor Shield Library](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/res/MotorDriver20121210.zip)
- **[数据手册]**[MC33932 Datasheet](https://github.com/SeeedDocument/4A_Motor_Shield/raw/master/res/MC33932.pdf)  
