---
title: Grove - UV Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-UV-Sensor-p-1540.html
oldwikiname: Grove_-_UV_Sensor
prodimagename: UV_Sensor_01.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020043 1.jpg
surveyurl: https://www.research.net/r/Grove-UV_Sensor
sku: 101020043
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit
---


![](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/img/UV_Sensor_01.jpg)

UV传感器用于检测射入紫外线（UV）辐射的强度。 这种形式的电磁辐射具有比可见光辐射更短的波长。 Grove-UV传感器基于传感器GUVA-S12D，其宽范围为200nm-400nm。 该模块输出随紫外线强度变化的电信号，这将给您的建议是否今天适合去沙滩。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11OovZ6x&id=45574580580)

产品特性
--------


- 高稳定性
- 良好的灵敏度
- 低功耗
- 具有Schottky光电二极管传感器
- 响应范围广
- 具有Grove接口

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

规格参数
--------------

|项目                | 最小 | 标准 | 最大 | 单位 |
|---------------------|-----|---------|-----|------|
| 工作电压     | 3.0 | 5.0     | 5.1 | VDC  |
| 工作电流             |     | 0.31    |     | mA   |
| 输出电压     |     |         |     | mV   |
| 响应波长| 240 | ~       | 370 | nm   |
| 工作温度| -30 | ~       | 85  | ℃    |

Platform Support
-------------------

创意应用
-----

* 紫外线传感器用于许多不同的应用，包括药品，汽车和机器人。
* UV传感器也用于印刷行业，用于溶剂处理和染色工艺。
* 此外，紫外线传感器也用于化学工业用于化学品的生产，储存和运输。

UV传感器的理论是：在阳光下，UV指数和光电流是线性相关的关系。

![](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/img/The%20theory%20of%20UV%20sensor.png)

关于我们的Grove-UV传感器，我们已将光电转换为Arduino / Seeeduino收集的相应电压值。 输出电压和UV指数是线性的：

**照明强度= 307 * Vsig**

Vsig是从Grove接口的SIG引脚测得的电压值。
对于波长测量范围为240nm〜370nm
照明强度单位：mW / m <sup> 2 </ sup>


<div class="admonition note">
<p class="admonition-title">Note</p>
要计算紫外线指数值，请参考<a href="http://www2.epa.gov/sunwise/uv-index">美国EPA </a>。 很难说这个传感器的测量值可以转换成EPA标准的紫外线指数，但可以大致估计。
</div>


UV指数=照明强度/ 200

入门指导
--------------

!!!Note
    本章基于Win10和Arduino IDE 1.6.9

我们将通过简单的演示向您展示这款Groove-UV传感器的工作原理。 首先，您需要准备以下内容：

| Seeeduino V4 | Grove - UV Sensor | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/img/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11Zo2lnI&id=45574580580)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|


  **硬件连接**


由于Grove系列模块的优点，您不需要制作焊接或面包板，您需要做的是将模块连接到Base Shield的正确端口。 对于此演示，我们只需要一个Grove模块。
- 将Grove UV传感器连接到Grove - Base Shield的A0端口。
- 将Grove - Base Shield插入Arduino / Seeeduino，并使用USB数据线将其连接到PC。
- 演示代码如下所示。

![enter image description here](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/img/connection.jpg)

  **将程序上传到Arduino并打开串口监控数据**

```
// modified by Victor
// to calculate UV index directly
void setup(){

    Serial.begin(9600);
}

void loop()
{
    int sensorValue;
    long  sum=0;
    for(int i=0;i<1024;i++)// accumulate readings for 1024 times
    {
        sensorValue=analogRead(A0);
        sum=sensorValue+sum;
        delay(2);
    }
    long meanVal = sum/1024;  // get mean value
    Serial.print("The current UV index is:");
    Serial.print((meanVal*1000/4.3-83)/21);// get a detailed calculating expression for UV index in schematic files.
    Serial.print("\n");
    delay(20);

}
```

资源下载
---------

- [Grove - UV Sensor v1.1 PCB and schematics(current version) in Eagle format](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/res/Grove%20-%20UV%20Sensor%20v1.1.zip)
- [Grove - UV Sensor v1.1 PCB(current version) in PDF format](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/res/Grove%20-%20UV%20Sensor%20v1.1%20brd.pdf)
- [Grove - UV Sensor v1.1 schematics(current version) in PDF format](https://github.com/SeeedDocument/Grove-UV_Sensor/raw/master/res/Grove%20-%20UV%20Sensor%20v1.1sch.pdf)
- [Grove - UV Sensor v1.1 Sensor Datasheets(current version)](https://raw.githubusercontent.com/SeeedDocument/Grove-UV_Sensor/master/res/Grove-UV_Sensor_v1.1_Datasheets.zip)
- [US EPA Suggestions About UV Radiation](https://www.epa.gov/sunsafety/uv-index-scale-1)
- [Grove - UV Sensor v1.0 schematics and datasheets(older version)](https://raw.githubusercontent.com/SeeedDocument/Grove-UV_Sensor/master/res/Grove-UV_Sensor_v1.0_Datasheets.zip)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_UV_Sensor -->
