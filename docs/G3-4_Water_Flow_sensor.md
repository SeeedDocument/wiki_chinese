---
title: G3/4 Water Flow sensor
category: MakerPro
bzurl: https://www.seeedstudio.com/g34-water-flow-sensor-p-1083.html?cPath=144_151
oldwikiname:  G3/4 Water Flow sensor
prodimagename:  3wsp.JPG
wikiurl: http://wiki.seeedstudio.com/cn/G3-4_Water_Flow_sensor/
sku:   314150003
---
![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/P21408651.jpg)

 Water flow sensor 由塑料阀体，水转子和霍尔效应传感器组成。 当水流过转子时，转子滚动。 其速度随着流速的变化而变化。 霍尔效应传感器会输出相应的脉冲信号。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.5c20548bCMlEtQ&id=528296328471)

##   规格参数
---
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
<td>1～60L/min
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
<td>≤2.0MPa
</td></tr>
<tr>
<td>储存温度
</td>
<td>-25℃～+80℃
</td></tr>
<tr>
<td>储存湿度
</td>
<td>25%～95%RH
</td></tr></table>

##   机械尺寸
---
###   传感器组件

<table >
<tr>
<th>序号
</th>
<th>名字
</th>
<th>数量
</th>
<th>材料
</th>
<th>备注
</th></tr>
<tr style="font-size: 90%">
<td width="200"> 1
</td>
<td width="150"> 阀体
</td>
<td width="150">  1
</td>
<td width="150">  PA66 + 33％玻璃纤维
</td>
<td width="150">
</td></tr>
<tr style="font-size: 90%">
<td width="200"> 2
</td>
<td width="150">  不锈钢珠
</td>
<td width="150">  1
</td>
<td width="150">  不锈钢SUS304
</td>
<td width="150">
</td></tr>
<tr style="font-size: 90%">
<td> 3
</td>
<td>  轴
</td>
<td>  1
</td>
<td>  不锈钢SUS304
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 4
</td>
<td>  叶轮
</td>
<td>  1
</td>
<td>  POM
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 5
</td>
<td>  环形磁铁
</td>
<td>  1
</td>
<td>  铁素体
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 6
</td>
<td>  中环
</td>
<td>  1
</td>
<td>  PA66 + 33％玻璃纤维
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 7
</td>
<td>  O 型密封圈
</td>
<td>  1
</td>
<td>  橡胶
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 8
</td>
<td>  电子密封圈
</td>
<td>  1
</td>
<td>  橡胶
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 9
</td>
<td>  盖
</td>
<td>  1
</td>
<td>  PA66 + 33％玻璃纤维
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 10
</td>
<td>  螺栓
</td>
<td>  4
</td>
<td>  不锈钢SUS304
</td>
<td>
</td></tr>
<tr style="font-size: 90%">
<td> 11
</td>
<td>  线
</td>
<td>  1
</td>
<td>  1007 24AWG
</td>
<td>
</td></tr></table>

##  使用例子
---
<font>Note: 这个例子是由 Charles Gantt 完成的。 感谢他的贡献。看看它是如何工作的。</font>

###  用水流量传感器读取水流量

 这是一个我直在研究的一个项目的一部分，我会在这里分享一些，关于如何使用 Seeed Studio Depo 中的 Water Flow Sensor  读取每小时的水流量。 它使用一个简单的旋转轮并与霍尔传感器一起使用。 通过读取这些脉冲并记录数据，我们可以将液体流速精确到 3％ 以内。

**硬件安装**

您将需要 Seeeduino / Arduino，水流传感器，10K电阻，面包板和一些跳线。


连接 Water Flow Sensor 非常简单。 有三根电线：黑色，红色和黄色。
黑色连到 Seeeduino 的 **GND**
红色连到 Seeeduino 的 **5v** 端口
黄色线将需要连接到 10k 上拉电阻，然后连接到 Seeeduino 上的引脚 **2**。

这是一个硬件连接图，它将告诉你如何连线。

![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/Reading_liquid_flow_rate_with_an_Arduino.jpg)

一旦你有了它，你将需要上传以下代码到你的 Seeeduino。 一旦上传，并且有一些流体流过 Water Flow Sensor，您可以打开串行监视器，它将显示流量，每秒刷新一次。

**程序设计**
```
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
    Calc = (NbTopsFan * 60 / 5.5); //(Pulse frequency x 60) / 5.5Q, = flow rate

    in L/hour
    Serial.print (Calc, DEC); //Prints the number calculated above
    Serial.print (" L/hour\r\n"); //Prints "L/hour" and returns a  new line
}
```
您可以参考我们的论坛了解关于[使用水流传感器读取水流量](http://www.seeedstudio.com/forum/viewtopic.php?f=4&amp;t=989&amp;p=3632#p3632)。

##   接线图
---
连接线使用的螺纹外径为1.4mm的。

![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/Wfs-wiring.jpg)

##   输出表
---
水平测试中的脉冲频率（Hz）= 5.5Q，Q为流量（L / min）。 （结果在+/- 3％范围内）

<table >
<tr>
<td width="400px">输出脉冲高电平
</td>
<td width="400px">信号电压> 4.5 V（输入DC 5 V）
</td></tr>
<tr>
<td>输出低电平脉冲
</td>
<td>信号电压<0.5V（输入DC 5V）
</td></tr>
<tr>
<td>精度
</td>
<td>3％（流速从1L / min到10L / min）
</td></tr>
<tr>
<td>输出信号占空比
</td>
<td>40%～60%
</td></tr></table>

![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/G34_Flow_rate_to_frequency.jpg)

##   常问问题
---
这里是[传感器常见问题](/w/index.php?title=Sensors_FAQ&amp;action=edit&amp;redlink=1 "Sensors_FAQ&amp;action=edit&amp;redlink=1")，人们可以去这里找到问题和答案 。

**Water flow sensor是由什么材料构成的？**

尼龙纤维，请避免强酸和强碱。

**水流量传感器对饮用水是否安全？**

是的，它已经用于饮水机。


##   资源下载
---
*   [Reading Water Flow rate with Water Flow Sensor](http://www.seeedstudio.com/forum/viewtopic.php?f=4&amp;t=989&amp;p=3632#p3632)

*   [Water Flow rate display on LCD](http://www.practicalarduino.com/projects/water-flow-gauge)

*   [datasheet for the material](http://garden.seeedstudio.com/images/4/4e/YEE70G30HSLNC..pdf)


##   相关项目
---
It's a pity that we don't have any demo about G3/4 Water Flow Sensor in the [Recipe](http://www.seeedstudio.com/recipe/) yet.

Post your awesome project about G3/4 Water Flow Sensor to <font color="#FF0000">win $100 Coupon!</font>. Please feel free to contact us: [recipe@seeed.cc](mailto:recipe@seeed.cc)

Here we introduce some projects about [Grove-Water Sensor](http://www.seeedstudio.com/depot/Grove-Water-Sensor-p-748.html).

###  What is Grove - Water Sensor

![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/Twig-Water_Sensor.jpg)

This water sensor module is part of the Twig system.You can use it with the analog pins to detect the amount of water induced contact between the grounded and sensor traces.

It works by having a series of exposed traces connected to ground and interlaced between the grounded traces are the sens traces.

The sensor traces have a weak pull-up resistor of 1 MΩ. The resistor will pull the sensor trace value high until a drop of water shorts the sensor trace to the grounded trace.

This circuit will work with the digital I/O pins of your Arduino.

###   Arduino Plant Warden

![](https://github.com/SeeedDocument/G3-4_Water_Flow_sensor/raw/master/img/552c2c4f2e5a8.jpg)

This project uses Grove - Water Sensor to create a simple but effective solution to watering plants.

How it works:

*   Display readouts of water sensor and temperature sensor on OLED screen

*   Send alert and activate a pump driver when water is under threshold.

*   Supply the variation in color by 10 RGB LEDs.

[**I want to make it.**](http://www.seeedstudio.com/recipe/102-arduino-plant-warden.html)

[**More Awesome Projects by Water Sensor**](http://www.seeedstudio.com/recipe/index.php?query=water+sensor)

###   Share Your Awesome Projects with Us

Born with the spirit of making and sharing, that is what we believe makes a maker.

And only because of this, the open source community can be as prosperous as it is today.

It does not matter what you are and what you have made, hacker, maker, artist or engineers.

As long as you start sharing your works with others, you are being part of the open source community and you are making your contributions.

Now share your awesome projects with us on [Recipe](http://www.seeedstudio.com/recipe/), and win a chance to become the Core User of Seeed.

*   Core Users, are those who show high interests in Seeed products and make significant contributions on Recipe.
*   We cooperate with our Core Users in the development of our new product, this, in another word, the Core Users will have the chance to experience any new products of Seeed before its official launch, and in return we expect valuable feedback from them to help us improve the product performance and user experience. And in most cases when our Core Users have some good ideas of making things, we'll offer hardware pieces, PCBA services as well as technical support. Besides, further commercial cooperation with the Core Users is highly possible.

<font color="#FF0000">Get more information about Core User, please email to:</font> [recipe@seeed.cc](mailto:recipe@seeed.cc)
