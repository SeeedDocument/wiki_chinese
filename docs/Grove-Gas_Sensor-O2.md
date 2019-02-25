---
name: Grove - Gas Sensor(O₂)
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Gas-Sensor(O2)-p-1541.html
oldwikiname: Grove_-_Gas_Sensor(O₂)
prodimagename: cover.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Gas_Sensor-O2/
sku: 101020002
tags: plat_duino, grove_analog, io_3v3, io_5v
---
<!-- tags: io_3v3, io_5v, grove_i2c, grove_analog, grove_digital, grove_uart, plat_duino, plat_bbg, plat_pi, plat_wio, plat_linkit -->

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Gas_Sensor_O2/master/images/cover.jpg)

Grove-Gas sensor（O2）是一种用于测试空气中氧浓度的传感器，它是基于电化学电池原理工作的。 当输出与氧气浓度成比例的电压值时,通过参考氧浓度线性特征图，可以清楚地了解当前的氧气浓度。 它非常适合检测环境中的氧气浓度。 Grove - Gas Sensor(O2)是一种有机反应模块，它可以通过与空气中气体的化学反应产生一点电流，我们不需要为其提供外部电源，输出电压会随时间变化而变化。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.3ff19e117BYXwq&id=45508562458)

## 产品特性


* 高精准度
* 灵敏度高
* 线性范围广
* 抗干扰能力强
* 非凡的可靠性


!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

##规格参数

|项目| 参数 |
|-------|---------------|
|测量范围| 0-25% |
|使用寿命	| 两年 |
|灵敏度| 0.05~0.15 mA(in air) |
|温度范围 |	-20 oC~50 oC |
|预热时间	| 20 分钟|

## 支持平台

### 入门指导

!!!Note
    本章基于Win10和Arduino IDE 1.6.9

这是一个易于使用的模块，您需要做的是将信号引脚（Grove连接线的YELLOW引脚）连接到控制器的ADC输入。 如果控制器中没有内部ADC，建议使用[Grove - I2C ADC](http://www.seeedstudio.com/Grove-I2C-ADC-p-1580.html)。

在这里，我们将向您展示如何通过一个简单的示例让它进行工作， Grove - Gas Sensor(O2)。 首先，您需要准备以下内容：

| Seeeduino V4 | Grove - Gas Sensor(O2) | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Gas_Sensor_O2/master/images/gas_sensor_210.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.3ff19e117BYXwq&id=45508562458)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|

### 硬件连接

由于Grove系列模块的优点，您不需要制作焊接或面包板，您需要做的是将模块连接到 Base Shield 的正确端口。 对于这个演示，我们只需要一个Grove模块。

* Grove - Sound 传感器是一个模拟输出的模块，我们在此演示中将其连接到 **A0** 端口

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Gas_Sensor_O2/master/images/connection.jpeg)


### 将代码上传到Arduino

将以下代码复制到Arduino IDE。


```
// Grove - Gas Sensor(O2) test code
// Note:
// 1. It need about about 5-10 minutes to preheat the sensor
// 2. modify VRefer if needed

const float VRefer = 3.3;       // voltage of adc reference

const int pinAdc   = A5;

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(9600);
    Serial.println("Grove - Gas Sensor Test Code...");
}

void loop()
{
    // put your main code here, to run repeatedly:
    float Vout =0;
    Serial.print("Vout =");

    Vout = readO2Vout();
    Serial.print(Vout);
    Serial.print(" V, Concentration of O2 is ");
    Serial.println(readConcentration());
    delay(500);
}

float readO2Vout()
{
    long sum = 0;
    for(int i=0; i<32; i++)
    {
        sum += analogRead(pinAdc);
    }

    sum >>= 5;

    float MeasuredVout = sum * (VRefer / 1023.0);
    return MeasuredVout;
}

float readConcentration()
{
    // Vout samples are with reference to 3.3V
    float MeasuredVout = readO2Vout();

    //float Concentration = FmultiMap(MeasuredVout, VoutArray,O2ConArray, 6);
    //when its output voltage is 2.0V,
    float Concentration = MeasuredVout * 0.21 / 2.0;
    float Concentration_Percentage=Concentration*100;
    return Concentration_Percentage;
}

```

然后选择正确的板和COM端口，然后点击上传按钮，这个过程需要几秒钟。

### 获取数据

打开您的Arduino IDE的串行监视器，您将立即获取数据

!!!Warning
    传感器需要预热约20〜30分钟，否则会获得偏大的数值。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Gas_Sensor_O2/master/images/data.png)


##资源下载

* [ME2-O2 Datasheet](https://github.com/SeeedDocument/Grove_Gas_Sensor_O2/raw/master/resources/ME2-O2-D20%200-25%25%20Manual%20%28ver1.2%29.pdf)
* [Schematic in Eagle File](https://github.com/SeeedDocument/Grove_Gas_Sensor_O2/raw/master/resources/Schematics_O2.zip)
* [Github Repository of this Document](https://github.com/SeeedDocument/Grove_Gas_Sensor_O2)
