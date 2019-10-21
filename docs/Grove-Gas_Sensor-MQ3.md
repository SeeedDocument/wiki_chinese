---
name: Grove - Gas Sensor(MQ3)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Gas-Sensor(MQ3)-p-1418.html
oldwikiname: Grove_-_Gas_Sensor(MQ3)
prodimagename: Grove_MQ3_Gas_Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Gas_Sensor-MQ3
sku: 101020006
tags: grove_analog, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/img/Grove_MQ3_Gas_Sensor.jpg)

Grove - Gas Sensor(MQ3) 模块可用于气体泄漏检测（在家庭和工业中）。 它适用于检测 <font color="Blue">酒精，汽油，甲烷，己烷，液化石油气，一氧化碳。</font> 由于响应时间快，测量可以尽快进行。且其灵敏度也可以通过电位器来进行调节。

<div class="admonition danger">
<p class="admonition-title">Note</p>
传感器值仅反映气体浓度在允许误差范围内的近似趋势，它不表示精确的气体浓度。 空气中某些部件的检测通常需要更精确和更昂贵的仪器，这些仪器不能用单个气体传感器来完成。 如果您的项目旨在以非常精确的水平获得气体浓度，那么我们不推荐使用这种气体传感器。
</div>

有 4 种气体传感器，每种都可以检测不同类型的气体，这里我们用一张表来说明。

|传感器类型|气体类型|点击购买|
|:---:|---|---|---|
|MQ2|可燃气体，烟雾|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.37f75a9db6SL89&id=520242943642)|
|MQ3|酒精蒸汽|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.15.5b31c1aeUvb14f&id=45575808671)|
|MQ5|石油气，天然气，城镇煤气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.5b31c1aeUvb14f&id=45508638349)|
|MQ9|一氧化碳，煤气，液化气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5b31c1aeUvb14f&id=45575800587)|

## 产品特性
--------

-   对酒精有高敏感度，对苯有低敏感度。
-   工作稳定且寿命长。
-   响应快，灵敏度高。

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
-------------

| 项目  | 参数              | 最小值  | 典型值    | 最大值 | 单位 |
|-------|-------------------------|------|------------|-----|------|
| VCC   | 工作电压         | 4.9  | 5          | 5.1 | V    |
| PH    | 热能耗     | 0.5  | -          | 750 | mW   |
| RL    | 负载电阻         |      | 可调 |     |      |
| RH    | 发热器电阻       | -    | 33         | -   | Ω    |
| Rs    | 敏电阻      | 1    | -          | 8   | MΩ   |
| Scope | 检测浓度 | 0.05 | -          | 10  | mg/L |

Platforms Supported
-------------------

## 创意应用
-----------------

-   酒精测试仪
-   呼气测醉器
-   玩具

## 硬件概述
-----------------

这是一个模拟输出传感器。这需要连接到 [Grove Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.7643e0c6l07gP5&id=520233320144) 中的任何一个模拟量插槽。 本教程中使用的示例使用 **A0** 模拟量引脚。将此模块连接到 Base Shield 的 **A0** 端口。

根据如下表所示的连接方式，将 Grove 模块直接连接到 Arduino:

| Arduino   | Gas Sensor |
|-----------|------------|
| 5V        | VCC        |
| GND       | GND        |
| NC        | NC         |
| Analog A0 | SIG        |

当气体浓度增加时，气体传感器的输出电压增加。灵敏度可以通过改变电位器来调节。<font color="Red">请注意，传感器的最佳预热时间是 24 小时以上</font>。 有关 MQ-3 传感器的详细信息，请参阅 **资源下载** 部分中提供的 data-sheet。

## 入门指导
---------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/img/Read_Gas_Sensor_data.jpg)

将 Grove - Gas Sensor (MQ3) 连接到 **A0** 端口，如上图所示。

### 气体检测的基本示例

在这个例子中，传感器连接到 **A0** 引脚。从传感器读取显示的电压。该值可用作检测气体浓度的任何增加/减少量的阈值。

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

### 测量 : 近似值

这个例子说明了一种了解气体近似浓度的方法。 根据 MQx 传感器的数据表，这些方程式在标准条件下进行了测试，并没有被校准。它可能会根据温度或湿度的变化而变化。

1. 将气体传感器保持在清洁的空气环境中。 上传如下的程序 :

```
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    float sensor_volt;
    float RS_air; //  Get the value of RS via in a clear air
    float R0;  // Get the value of R0 via in Alcohol
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
    R0 = RS_air/60.0; // The ratio of RS/R0 is 60 in a clear air from Graph (Found using WebPlotDigitizer)

    Serial.print("sensor_volt = ");
    Serial.print(sensor_volt);
    Serial.println("V");

    Serial.print("R0 = ");
    Serial.println(R0);
    delay(1000);

}
```

2. 然后打开 Arduino IDE 的串口监视器。 记下 R0 的值，它需要在下一个程序中使用。

<font color="Red"> 将 R0 替换为上面测出的 R0 值 </font>. 将传感器暴露在上述任何一种气体中。

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

现在，我们可以从下图获得气体浓度。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/img/GAS_Sensor_3.png)

根据该图可以看出，我们可以测试的最小浓度为 0.1mg/L，最大浓度为 10mg/L。然而，我们不能提供一个公式，因为比率和浓度之间的关系是非线性的。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/res/Gas_Sensor_Eagle_files.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---------

-   **[Eagle 文件]** [Grove Gas Sensor - EAGLE (Schematic and Board) files](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/res/Gas_Sensor_Eagle_files.zip)
-   **[原理图 PDF]** [Grove Gas Sensor - PDF Schematic](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/res/Gas_Sensor_Schematic.pdf)
-   **[数据手册]** [MQ-3 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ3/master/res/MQ-3.pdf)
-   **[其他资源]** [How to choose a Gas Sensor](/How_to_choose_A_Gas_Sensor)
-   **[其他资源]** [What's LEL](http://en.wikipedia.org/wiki/Flammability_limit)
<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor(MQ3) -->
