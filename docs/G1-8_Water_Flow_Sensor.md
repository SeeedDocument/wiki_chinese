---
title: G1/8" Water Flow Sensor
category: MakerPro
bzurl: http://www.seeedstudio.com/depot/G18-Water-Flow-Sensor-p-1346.html?cPath=25_32
oldwikiname:  G1/8" Water Flow Sensor
prodimagename:  G18_Water_Flow_Sensor.jpg
wikiurl: http://seeed.wiki/G1-8_Water_Flow_Sensor
sku:    314150001
---
[![](https://github.com/SeeedDocument/G1-8_Water_Flow_Sensor/raw/master/img/G18_Water_Flow_Sensor.jpg)](http://www.seeedstudio.com/depot/G18-Water-Flow-Sensor-p-1346.html?cPath=25_32)

Water flow sensor 由塑料阀体，水转子和霍尔效应传感器组成。 当水流过转子时，转子滚动，其速度随着流速的变化而变化。 霍尔效应传感器输出相应的脉冲信号。这适用于检测饮水机或咖啡机中的流量。

我们拥有不同直径的全系列水流传感器。 检索并找到最符合你需求的那个。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.18651024ipeJqD&id=45550733026)

##  产品特性

*   紧凑，易于安装

*   高密封性能

*   高品质霍尔效应传感器

*   符合RoHS标准

##  规格参数

<table >
<tr>
<td>最小工作电压
</td>
<td>DC 4.5V
</td></tr>
<tr>
<td>最大工作电流
</td>
<td>15mA(DC 5V)
</td></tr>
<tr>
<td width="400px">工作电压
</td>
<td width="400px">5V～24V
</td></tr>
<tr>
<td>水流量范围
</td>
<td>0.3~6L/min
</td></tr>
<tr>
<td>承载量
</td>
<td>≤10mA(DC 5V)
</td></tr>
<tr>
<td>工作温度
</td>
<td>≤80℃
</td></tr>
<tr>
<td>液体温度
</td>
<td>≤120℃
</td></tr>
<tr>
<td>工作湿度
</td>
<td>35%～90%RH
</td></tr>
<tr>
<td>水压力
</td>
<td>≤0.8MPa
</td></tr>
<tr>
<td>储存温度
</td>
<td>-25℃～+80℃
</td></tr>
<tr>
<td>储存适度
</td>
<td>25%～95%RH
</td></tr></table>

##  入门指导

<font>注意：这个例子是由 Charles Gantt 完成的。感谢他的贡献。看看它是如何工作的。</font>

###   用Water Flow Sensor读取水流量

这是一个我直在研究的一个项目的一部分，我会在这里分享一些，关于如何使用 Seeed Studio Depo 中的 Water Flow Sensor 读取每小时的水流量。 它使用一个简单的旋转轮并与霍尔传感器一起使用。 通过读取这些脉冲并记录数据，我们可以将液体流速精确到 3% 以内。由于端口是简单的 G3/4，所以找到合适的接口并不难。

**硬件安装**

您将需要 Seeeduino / Arduino，水流传感器，10K电阻，面包板和一些跳线。

连接 Water Flow Sensor 非常简单。 有三根电线：黑色，红色和黄色。 黑色连到 Seeeduino 的 **GND**，红色连到 Seeeduino 的 **5v** 端口，黄色线将需要连接到 **10k** 上拉电阻，然后连接到 Seeeduino 上的**引脚 2**。

这是一个硬件连接图，它将告诉你如何连线。

![](https://github.com/SeeedDocument/G1-8_Water_Flow_Sensor/raw/master/img/Reading_liquid_flow_rate_with_an_Arduino.jpg)

一旦你有了它，你将需要上传以下代码到你的 Seeeduino。 上传后，使一些流体流过 Water Flow Sensor，您可以打开串行监视器，它将显示流量，每秒刷新一次。

** 程序设计 **
```
// reading liquid flow rate using Seeeduino and Water Flow Sensor from Seeedstudio.com
// Code adapted by Charles Gantt from PC Fan RPM code written by Crenn @thebestcasescenario.com
// http:/themakersworkbench.com http://thebestcasescenario.com http://seeedstudio.com

volatile int NbTopsFan; //测量信号的上升沿
int Calc;
int hallsensor = 2;    //设置传感器接线引脚

void rpm ()            //这是中断调用的功能
{
    NbTopsFan++;       //该功能测量霍尔效应传感器信号的上升沿和下降沿
}
// The setup() method runs once, when the sketch starts
void setup()
{
    pinMode(hallsensor, INPUT); //初始化数字引脚2作为输入
    Serial.begin(9600);         //串行端口初始化
    attachInterrupt(0, rpm, RISING);  //连接中断
}
// the loop() method runs over and over again,
// as long as the Arduino has power
void loop ()
{
    NbTopsFan = 0;   //将 NbTops 设置为 0 可以进行计算
    sei();          //启用中断
    delay (1000);   //等待1秒
    cli();          //禁止中断
    Calc = (NbTopsFan * 60 / 7.5); //(Pulse frequency x 60) / 7.5Q,流量为L/hour
    Serial.print (Calc, DEC);
    Serial.print (" L/hour\r\n");
}
```

您可以参考我们的论坛了解更多关于[用 Water Flow Sensor 读取水流量](http://www.seeedstudio.com/forum/viewtopic.php?f=4&amp;t=989&amp;p=3632#p3632).

##  接线图

![](https://github.com/SeeedDocument/G1-8_Water_Flow_Sensor/raw/master/img/Wfs-wiring.jpg)

##  输出表

水平位置测试中的脉冲频率（Hz）= 7.5Q，Q 为流量（L / min）。 （结果在± 3％范围内）
<table >
<tr>
<td width="400px">输出脉冲高电平
</td>
<td width="400px">信号电压 &gt;4.5 V( 输入 DC 5 V)
</td></tr>
<tr>
<td>输出脉冲低电平
</td>
<td>信号电压 &lt;0.5V( 输入 DC 5V)
</td></tr>
<tr>
<td>精度
</td>
<td>3% (流速从 1L/min 到 10L/min)
</td></tr>
<tr>
<td>输出信号占空比
</td>
<td>40%～60%
</td></tr></table>

##  资源下载

*   **[数据手册]**[Water flow sensor datasheet.pdf](https://github.com/SeeedDocument/G1-8_Water_Flow_Sensor/raw/master/res/Water_flow_sensor_datasheet.pdf)

*   **[创意应用]**[Reading Water Flow rate with Water Flow Sensor](http://www.seeedstudio.com/forum/viewtopic.php?f=4&amp;t=989&amp;p=3632#p3632)

*   **[<font color =“Red”>已失效]**[Water Flow rate display on LCD](http://www.practicalarduino.com/projects/water-flow-gauge)

*   **[<font color =“Red”>已失效]**[datasheet for the material](http://garden.seeedstudio.com/images/4/4e/YEE70G30HSLNC..pdf)
