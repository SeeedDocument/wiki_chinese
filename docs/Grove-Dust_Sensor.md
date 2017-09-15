---
title: Grove - Dust Sensor
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Dust-Sensor-p-1050.html
oldwikiname: Grove - Dust Sensor
prodimagename: Dust_sensor.JPG
surveyurl: https://www.research.net/r/grove-dust-sensor
sku: 101020012
tags: plat_duino
---
---
![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/Dust_sensor.JPG)

该灰尘传感器通过测量灰尘浓度可以很好地显示周围环境中的空气质量。 通过计算给定时间单位中的低脉冲占用时间（LPO时间）来测量空气中的颗粒物质水平（PM水平）。 LPO时间与PM浓度成正比。 该传感器可为空气净化器系统提供可靠的数据; 它能够响应的pM范围可以达到直径1μm。

!!!note
    - 该传感器采用计数方式测量粉尘浓度，而不是通过称重方式，其单位为pcs / L或pcs / 0.01cf。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11dFbBNp&id=45490758155)

产品特性
--------
- 该传感器能够稳定和灵敏的检测不仅是烟草烟雾的浓度，还有室内会引起哮喘的尘埃。
- 使用内置的空气加热装置达到自我吸气的功能。
- 维护方便，能够保持高灵敏度的长期使用。
- 能够输出超过1微米和2.5微米（大约）的粒度。
- 更紧凑轻巧，安装方便。

!!!note
    在最新版本中，输出高电压从4.0V变为4.5V。

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

规格参数
-------------

|项目|	标准规格|	单位 |
|----|-----|-------|
|VCC |	4.75~5.75|	V    |
|待机电源|	90|	mA|
|可检测浓度范围|	0~28,000 / 0 ~ 8000	|	pcs/liter / pcs/0.01cf|
|工作温度范围|	0~45|	°C|
|输出方式|	Negative Logic, Digital output, High: over 4.0V(Rev.2), Low: under 0.7V|-|
|检测粒径|	>1 |μm|
|外形尺寸|	59(W) × 45(H) × 22(D) |mm|
|湿度范围|	95％rh以下|-|

支持平台
--------------------


创意应用
------------------
- 空气净化器
- 空气质量监测
- 冷气机
- 呼吸机

入门指导
---------------
### <span id="jump">注意事项</span>
- 请保持直立。
- 第一次使用时需要3分钟的预热时间。
- 任意操作可能会导致意外的损坏。
- 以下小部件（标有红色矩形的）仅用于出厂设置。 请 **不要** 更改默认配置。

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/Grove_-_Dust_Sensor_cautions.jpg)

### 硬件连接
这是一个演示，演示如何从这个Grove - Dust传感器获取PM浓度数据。

将Dust传感器插入Grove-[BaseShield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 数字端口 **D8** 并且它只能是通过D8接口，因为这个传感器的操作涉及采样。 此功能只能通过Arduino / Seeeduino上ATmega328P的输入引脚D8来实现。


|Arduino UNO	| Dust Sensor Pin| Cable Color|
|--|--|--|
|5V| Pin 3|	红线|
|GND	| Pin 1|黑线|
|D8| Pin 4|	黄线|


Grove连接线包含在Grove Dust Sensor封装中。 我们也可以使用Dupont Line去连接Base Shield，如下图所示。
![](https://github.com/SeeedDocument/Grove_Dust_Sensor/raw/master/image/connection.jpg)

此外，您可以将Grove - Dust传感器连接到Arduino UNO，而不需要Base Shield。

### 软件程序

将下面的演示代码复制并粘贴到Arduino IDE上。

```c
/*
Grove - Dust Sensor Demo v1.0
 Interface to Shinyei Model PPD42NS Particle Sensor
 Program by Christopher Nafis
 Written April 2012

 http://www.seeedstudio.com/depot/grove-dust-sensor-p-1050.html
 http://www.sca-shinyei.com/pdf/PPD42NS.pdf

 JST Pin 1 (Black Wire)  =&gt; //Arduino GND
 JST Pin 3 (Red wire)    =&gt; //Arduino 5VDC
 JST Pin 4 (Yellow wire) =&gt; //Arduino Digital Pin 8
 */

int pin = 8;
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 2000;//sampe 30s&nbsp;;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  starttime = millis();//get the current time;
}

void loop() {
  duration = pulseIn(pin, LOW);
  lowpulseoccupancy = lowpulseoccupancy+duration;

  if ((millis()-starttime) >= sampletime_ms)//if the sampel time = = 30s
  {
    ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=&gt;100
    concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
    Serial.print("concentration = ");
    Serial.print(concentration);
    Serial.println(" pcs/0.01cf");
    Serial.println("\n");
    lowpulseoccupancy = 0;
    starttime = millis();
  }
}
```

在这个程序中，Seeeduino在30秒内对“逻辑低”的总持续时间进行了采样，这个时间表示了环境的灰尘浓度。 打开串行监视器，我们可以从PC的串行端口中获取传感器检测到的空气质量值。



![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/Dust_sensor_1.png)

**"lowpulseoccupancy"** 表示在30秒内检测到的低脉冲占用时间（LPO时间）。 单位是微秒。

**"ratio"** 反映了哪个级别的LPO时间占用了整个的采样时间。

**"concentration"** 是一个有物理意义的数字。 可以通过使用以下特征图来得出LPO时间。
![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/600px-Characteristics.jpg)

以下是办公室测量的粉尘浓度图：

![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/600px-Dust_sensor_4.jpg)

我们可以看到晚上的尘埃浓度很低，但是下午较高。 当浓度高于某个数值时，可以在这里设置阈值。 此外，如果要设置传感器更敏感，可以在传感器上添加风扇，并在Pin5和Ground之间添加一个10kΩ的电阻。 更多信息请访问 [blog of A.J](https://indiaairquality.com/2014/12/14/measuring-the-pickle-jr-a-modified-ppd42-with-an-attached-fan/).

相关项目
---
If you want to make some awesome projects by Grove - Dust Sensor, here is a project for reference.

### Air Quality Box
![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/600px-Overview0.png)

This section an IoT demo made by Seeeduino and [Grove](http://www.seeedstudio.com/wiki/Grove_System).

More attention is being paid to the environmental air quality nowadays because the tiny particles in the air around can badly endanger people’s health. We always get the information of environment from our government department. But it’s the average value of the whole city/section. It can not reflect the environment around you accurately.

[![](https://raw.githubusercontent.com/SeeedDocument/Grove_Dust_Sensor/master/image/200px-Wiki_makeitnow_logo.png)](http://www.instructables.com/id/Air-Quality-Test-Box/?ALLSTEPS)

资源下载
---
- **[Datasheet]** [Grove-Dust_sensor datasheet](https://github.com/SeeedDocument/Grove_Dust_Sensor/raw/master/resource/Grove_-_Dust_sensor.pdf)
- **[Datasheet]** [De-construction of the Shinyei PPD42NS dust sensor Made by Tracy Allen](https://github.com/SeeedDocument/Grove_Dust_Sensor/raw/master/resource/ShinyeiPPD42NS_Deconstruction_TracyAllen.pdf)
- **[Demo]**[Building a low-cost networked PM2.5 monitor](https://indiaairquality.com/2014/12/14/building-pickle-jr-the-low-cost-networked-pm2-5-monitor-part-2/) -- Made by A.J.
- **[Demo]** [Measuring the Pickle Jr. – a modified PPD42 with an attached fan.](https://indiaairquality.com/2014/12/14/measuring-the-pickle-jr-a-modified-ppd42-with-an-attached-fan/) -- Made by A.J.
- **[Demo]** [Testing the Shinyei PPD42NS](http://irq5.io/2013/07/24/testing-the-shinyei-ppd42ns/) -- Made by darell tan
- **[Demo]** [Air Quality Monitoring](http://www.howmuchsnow.com/arduino/airquality/grovedust/) -- Made by Chris Nafis
