---
title: Grove - Gas Sensor(MQ9)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Gas-Sensor(MQ9)-p-1419.html
oldwikiname: Grove_-_Gas_Sensor(MQ9)
prodimagename: Grove_MQ3_Gas_Sensor.jpg
wikiurl: http://seeed.wiki/Grove-Gas_Sensor-MQ9
sku: 101020045
tags: grove_analog, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/img/Grove_MQ3_Gas_Sensor.jpg)

 Grove - Gas Sensor(MQ9)模块可用于气体泄漏检测（可以在家里和工厂中使用）。 它适用于检测 <font color =“Blue”>LPG，CO，CH4</font> 。 由于其的灵敏度高，响应时间快，所以能够时时进行测量。 传感器的灵敏度可以通过使用电位器进行调整。

<div class="admonition danger">
<p class="admonition-title">Note</p>
这个传感器值仅能够反映气体浓度在允许误差范围内的近似趋势，它不表示精确的气体浓度。 空气中某些成分的检测通常需要更加精确和更加昂贵的仪器，这不能单单使用这个气体传感器来完成。 如果您的项目想要非常精确的得到气体浓度，那么我们不推荐使用这种气体传感器。
</div>

|传感器|检测气体类型|购买地址|
|:---:|---|---|---|
|MQ2|可燃气体，烟雾|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.16ffcea31SnYiT&id=520242943642)|
|MQ3|酒精蒸气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.15852b36Zh3I85&id=45575808671)|
|MQ5|石油气，天然气，城镇煤气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.1a5dbea7KWe93J&id=45508638349)|
|MQ9|一氧化碳，煤气，液化气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.51352e2wNrNua&id=45575800587)|


产品特性
--------


- 检测范围广
- 能够稳定和长时间使用
- 响应快，灵敏度高

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)


产品参数
-------------

| 项目             | 参数               |最小 | 标准    | 最大             |单位 |
|------------------|-------------------------|-----|------------|------------------|------|
| VCC              | 工作电压       | 4.9 | 5          | 5.1              | V    |
| PH               | 消耗能量    | 0.5 | -          | 340              | mW   |
| RL               | 负载电阻       |     | 可调整的 |                  |      |
| RH               | 加热器电阻       | -   | 33Ω±5%     | -                | Ω    |
| Rs               | 感应电阻    | 2   | -          | 20000            | Ω    |
| CO / CH4 / LPG范围 |检测浓度 | 200 | -          | 1000/10000/10000 | ppm  |

支持平台
-------------------

创意应用
-----------------

- 气体泄漏检测。
- 玩具。

硬件概述
-----------------

这是一个以模拟量输出的传感器。 这需要连接到[Grove Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.49bd3ea9eDqLsu&id=520233320144)中的一个模拟端口。 本教程中的示例使用的是 **A0** 模拟引脚。 将此模块连接到Base Shield的 **A0** 端口。

使用连接线将Grove模块按照下表连接到Arduino：

| Arduino   | Gas Sensor |
|-----------|------------|
| 5V        | VCC        |
| GND       | GND        |
| NC        | NC         |
|  A0 | SIG        |

当气体浓度增加时，气体传感器的输出电压会增加。 灵敏度可以通过改变电位器来调节。 <font color="Red">请注意，传感器的最佳预热时间需要超过24小时</font>。 有关MQ-9传感器的详细信息，请参阅 **资源下载** 部分中提供的数据表。

入门指导
---------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/img/Read_Gas_Sensor_data.jpg)

将 Grove - Gas Sensor(MQ9)连接到 **A0** 端口，如上图所示。

### 气体检测：基本例子

在这个例子中，传感器连接到 **A0** 引脚。 从传感器读取到的电压可以显示出来。 并且该值可以用作检测气体浓度是否增加/减少的基准。

```
void setup() {
    Serial.begin(9600);
}

void loop() {
    float sensor_volt;
    float sensorValue;

    sensorValue = analogRead(A0);
    sensor_volt = sensorValue/1024*5.0;

    Serial.print("sensor_volt = ");
    Serial.print(sensor_volt);
    Serial.println("V");
    delay(1000);
}
```

### 测量：近似值

这个例子介绍了一种知道气体近似浓度的方法。 根据MQ9传感器的数据表，在标准条件下对这些方程计算的结果进行测试，不需要进行校准。 不过它可能会根据温度或湿度的变化而变化。

1. 将气体传感器保持在清洁的空气环境中。 上传以下程序。

```
void setup() {
    Serial.begin(9600);
}

void loop() {
    float sensor_volt;
    float RS_air; //  Get the value of RS via in a clear air
    float R0;  // Get the value of R0 via in LPG
    float sensorValue;

    /*--- Get a average data by testing 100 times ---*/
    for(int x = 0 ; x < 100 ; x++)
    {
        sensorValue = sensorValue + analogRead(A0);
    }
    sensorValue = sensorValue/100.0;
    /*-----------------------------------------------*/

    sensor_volt = sensorValue/1024*5.0;
    RS_air = (5.0-sensor_volt)/sensor_volt; // omit *RL
    R0 = RS_air/9.9; // The ratio of RS/R0 is 9.9 in LPG gas from Graph (Found using WebPlotDigitizer)

    Serial.print("sensor_volt = ");
    Serial.print(sensor_volt);
    Serial.println("V");

    Serial.print("R0 = ");
    Serial.println(R0);
    delay(1000);

}
```

2. 然后打开Arduino IDE的串行监视器。 记下 **R0** 的值，这需要在下一个程序中使用。 读取稳定后，请将 **R0** 放在下方。

<font color="Red">将下面的 **R0** 替换为上面测试的 **R0** 值 </font>. 将下面的R0替换为上面测试的R0值。 将传感器放置在上述任何一种气体中。

```
void setup() {
    Serial.begin(9600);
}

void loop() {

    float sensor_volt;
    float RS_gas; // Get value of RS in a GAS
    float ratio; // Get ratio RS_GAS/RS_air
    int sensorValue = analogRead(A0);
    sensor_volt=(float)sensorValue/1024*5.0;
    RS_gas = (5.0-sensor_volt)/sensor_volt; // omit *RL

          /*-Replace the name "R0" with the value of R0 in the demo of First Test -*/
    ratio = RS_gas/R0;  // ratio = RS/R0
          /*-----------------------------------------------------------------------*/

    Serial.print("sensor_volt = ");
    Serial.println(sensor_volt);
    Serial.print("RS_ratio = ");
    Serial.println(RS_gas);
    Serial.print("Rs/R0 = ");
    Serial.println(ratio);

    Serial.print("\n\n");

    delay(1000);

}
```

现在，我们可以从下图获得气体的浓度。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/img/GAS_Sensor_7.png)

根据该图可以看出，我们可以测试的最小浓度为200ppm，最大值为10000ppm，换句话说，我们可以得到0.02％〜1％之间的气体浓度。 然而，我们不能得到一个公式，因为比例和浓度之间的关系是非线性的。

资源下载
---------

**Suggest Reading / References**

-   [How to choose a Gas Sensor](/How_to_choose_A_Gas_Sensor)
-   [What's LEL](http://en.wikipedia.org/wiki/Flammability_limit)

**Schematic**
---------

-   [Grove Gas Sensor - EAGLE (Schematic and Board) files](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/res/Gas_Sensor_Eagle_files.zip)
-   [Grove Gas Sensor - PDF Schematic](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/res/Gas_Sensor_Schematic.pdf)

**Datasheet**

-   [MQ-9 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ9/master/res/MQ-9.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor(MQ9) -->
