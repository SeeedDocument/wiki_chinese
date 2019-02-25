---
name: G1&2" Water Flow Sensor
category: MakerPro
bzurl: https://www.seeedstudio.com/g12-water-flow-sensor-p-635.html?cPath=84_87&zenid=020999c566d2f31841dc54602b7d02ef
oldwikiname: G1/2 Water Flow sensor
prodimagename: 113990010%201.jpg
wikiurl: http://wiki.seeedstudio.com/cn/G1_and_2_inch_Water_Flow_Sensor
sku: 314150005
---
![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/flowsensor_LRG.jpg)

G1&2" Water Flow Sensor 由塑料阀体，水转子和霍尔效应传感器组成。 当水流过转子时，转子滚动，其速度随着流速的变化而变化。 霍尔效应传感器输出相应的脉冲信号。

**版本更新**

|版本调整|	描述|	发布日期|
|---|---|---|---|
|v1.0|	首次公开发布	| 2010 年 5 月 31 日|
|v2.0|	公开发布 2.0 |	2010年 7 月 5 日|

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.3d9935f5JN2xoG&id=45553920414)

## 规格参数
---
|项目|范围|
|---|---|
|最小工作电压|直流 4.5V |
|最大工作电流| 15mA（直流 5V ）|
|工作电压| 5V 〜 24V |
|流量范围| 1〜30L / min |
|负载容量|≤10mA（直流5V）|
|工作温度|≤80℃|
|液体温度|≤120℃|
|工作湿度| 35％〜90％RH |
|水压|≤2.0MPa|
|储存温度| -25℃〜+ 80℃|
|储存湿度| 25％〜95％RH |


## 机械尺寸
---
单位: mm

![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/Dem1.png)

![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/Dem2.png)

## 传感器组件
---

|编号|名称|	数量|	材料	|注意|
|---|---|---|---|---|
| 1 | 阀体| 1 | PA66+33％ 玻璃纤维||
| 2 | 不锈钢珠|1| 不锈钢 SUS304 ||
| 3 | 轴| 1 |不锈钢 SUS304 ||
| 4 |叶轮|1|POM||
| 5 | 环形磁铁| 1 |铁氧体||
| 6 | 中间套环| 1 | PA66+33％ 玻璃纤维||
| 7 |  O 型密封圈| 1 |橡胶||
| 8 | 电子密封圈| 1 |橡胶||
| 9 |外壳| 1 | PA66+33％玻璃纤维||
| 10 |螺丝| 4 | 不锈钢 SUS304 | 3.0 * 11 |
| 11 |连接线| 1 | 1007 24AWG |||

## 使用示例

!!!Note
    这个示例是由 Charles Gantt 的论坛提供的。 请感谢他的贡献，现在让我们来看看它是如何工作的。

**用 Water Flow Sensor 读取水流量**

这是我们一直在努力的一个项目中的一部分，我会在这里分享一下，因为有一些关于如何使用 Seeed Studio Depo 中的 Water Flow Sensor 读取每小时的水流量的问题。它利用旋转霍尔效应传感器的简单旋转轮。 通过读取这些脉冲并进行一些数学运算，我们就可以将液体流速精确到 3％ 以内。线程是简单的 G3 / 4 ，所以你发现实现起来不会那么困难。

**硬件概述**

您将需要 Seeeduino / Arduino ， Water Flow Sensor ，10K 电阻，电路实验板和一些杜邦线。

连接 Water Flow Sensor 的方法非常简单。 有三根电线：黑色，红色和黄色。 黑色接到 Seeeduino 的接地引脚，红色接到 Seeeduino 的 **5v** 引脚，黄色线需要连接到 10k 电阻上，然后接到 Seeeduino 上的引脚 **2**。

通过这个图，我将告诉你如何连线。

![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/Reading_liquid_flow_rate_with_an_Arduino.jpg)

当你使用它时，你将需要上传以下代码到你的 Seeeduino 。 在上传以后，当有流体流过 Water Flow Sensor 时，您可以打开串行监视器，它将显示流量，每秒刷新一次。


**程序设计**

```c
// reading liquid flow rate using Seeeduino and Water Flow Sensor from Seeedstudio.com
// Code adapted by Charles Gantt from PC Fan RPM code written by Crenn @thebestcasescenario.com
// http:/themakersworkbench.com http://thebestcasescenario.com http://seeedstudio.com

volatile int NbTopsFan; //measuring the rising edges of the signal
int Calc;
int hallsensor = 2;    //The pin location of the sensor

void rpm ()     //This is the function that the interupt calls
{
  NbTopsFan++;  //This function measures the rising and falling edge of the

hall effect sensors signal
}
// The setup() method runs once, when the sketch starts
void setup() //
{
  pinMode(hallsensor, INPUT); //initializes digital pin 2 as an input
  Serial.begin(9600); //This is the setup function where the serial port is

initialised,
  attachInterrupt(0, rpm, RISING); //and the interrupt is attached
}
// the loop() method runs over and over again,
// as long as the Arduino has power
void loop ()
{
  NbTopsFan = 0;   //Set NbTops to 0 ready for calculations
  sei();      //Enables interrupts
  delay (1000);   //Wait 1 second
  cli();      //Disable interrupts
  Calc = (NbTopsFan * 60 / 7.5); //(Pulse frequency x 60) / 7.5Q, = flow rate

in L/hour
  Serial.print (Calc, DEC); //Prints the number calculated above
  Serial.print (" L/hour\r\n"); //Prints "L/hour" and returns a  new line
}
```

您可以参考我们的论坛了解更多有关 Water Flow Sensor 读取水流量方法的详细信息。

## 接线简图
---

连接线使用的螺纹外径为 1.4mm。
![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/Wfs-wiring.jpg)

## 输出表
---

水平测试中的脉冲频率（Hz）= 7.5Q，Q 为流速（L / min）。 （结果在 +/- 3％ 范围内）

|项目|范围|
|---|---|
|输出脉冲高电平| 信号电压> 4.5 V（输入 DC 5 V）|
|输出脉冲低电平|信号电压<0.5V（输入直流 5V）|
|精度| 3％（流量从 1L / min 到 10L / min）|
|输出信号占比| 40％〜60％|

## 相关项目

很遗憾，我们还没有关于 [Recipe](http://www.seeed.cc/projects.html#recipe) 中的 G1/2 Water Flow Sensor 的演示。

在这里，我们介绍一些关于 [Grove-Water Sensor](http://www.seeedstudio.com/depot/Grove-Water-Sensor-p-748.html) 的项目。

**关于 Grove - Water Sensor**

![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/Twig_-_Water_Sensor.jpg)

Grove - Water Sensor 模块是 Twig 系统的一部分。您可以使用模拟引脚来检测接地和传感器之间的水流量。


传感器连接线具有 1MΩ 的弱上拉电阻。当水从传感器流出时，电阻器会将传感器检测的数值拉高。

该电路将与您的 Arduino 的数字 I / O 引脚一起工作。


**Arduino 工厂监督设备**

![](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/img/552c2c4f2e5a8.jpg)

该项目使用 Grove - Water Sensor 来创建一个简单但有效的浇灌设备的解决方案。
怎么运行的：
- 在 OLED 屏幕上显示水传感器和温度传感器
- 当水位低于阈值时发送警报并激活泵驱动器。
- 通过 10个 RGB LED 提供颜色变化。

[制作流程.](http://www.seeed.cc/project_detail.html?id=103)

[更多基于 Grove - Water Sensor 的项目](http://www.seeedstudio.com/recipe/index.php?query=water+sensor)

**请分享你制作的精彩的项目给我们**

以制作和分享的精神出发，这就是我们所相信的制造商。
正因为如此，开源社区才能像今天一样有良好的发展。
无论你是谁，你所制造的，黑客，制造商，艺术家或工程师都无关紧要。
只要你开始与他人分享你的作品，你就是开源社区的一部分，你正在为此作出贡献。

现在在 [Recipe](http://www.seeed.cc/) 上与我们分享您的精彩项目，并赢得成为 Seeed 核心用户的机会。

- 核心用户，对 Seeed 产品非常感兴趣的，对开源社区作出重大贡献。

- 我们与核心用户合作开发我们的新产品，换句话说，核心用户将有机会在正式推出之前体验到 Seeed 的任何新产品，作为回报，我们期望他们有宝贵的意见，帮助我们提高产品性能和用户体验。 在大多数情况下，当我们的核心用户有一些好的想法，我们将提供硬件， PCBA 服务以及技术支持。 此外，与核心用户进一步商业合作也是非常有可能的。

获取有关核心用户的更多信息，请发送电子邮件至：recipe@seeed.cc

## 许可证书
---

本文档根据知识共享[Attribution-ShareAlike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/) 获得许可。源代码和数据库可通过[GPL/LGPL](http://www.gnu.org/licenses/gpl.html)获得，有关详细信息，请参阅源代码文件。

## 常见问题

关于传感器常见问题，人们可以去这里找到这种产品的问题和答案。

1. **water flow sensor 使用什么材料制成的?**

  - 尼龙纤维，避免强酸和强碱。

2. **water flow sensor 是否可用于饮用水系统?**

  - 是的，它已经用于饮水机.

## 资源下载
---
- [Water flow sensor datasheet.pdf](https://github.com/SeeedDocument/G1_and_2_inch_Water_Flow_Sensor/raw/master/res/Water_flow_sensor_datasheet.pdf)
- [Reading Water Flow rate with Water Flow Sensor](http://www.seeed.cc/topic_detail.html?id=575#p3632)
- [Water Flow rate display on LCD](https://github.com/practicalarduino/WaterFlowGauge)
- [datasheet for the material](http://garden.seeedstudio.com/images/4/4e/YEE70G30HSLNC..pdf)
