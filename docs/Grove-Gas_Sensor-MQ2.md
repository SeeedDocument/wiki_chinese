---
name: Grove - Gas Sensor(MQ2)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Gas-Sensor(MQ2)-p-937.html
oldwikiname: Grove_-_Gas_Sensor(MQ2)
prodimagename: Twig-Gas_Sensor.bmp
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Gas_Sensor-MQ2
sku: 101020055
tags: grove_analog, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/img/Twig-Gas_Sensor.bmp)

Grove气体传感器 (MQ2) 模块可用于气体泄漏检测（在家庭和工业中）。可检测<font color="Blue">H2, LPG, CH4, CO, 酒精, 烟雾或丙烷</font>等。 由于其快速响应的时间特性， 测量可以迅速完成。且其灵敏度也可以通过电位器来进行调节。

!!!Note
    传感器值仅反映气体浓度在允许误差范围内的近似趋势，它不表示精确的气体浓度。 空气中某些部件的检测通常需要更精确和更昂贵的仪器，这些仪器不能用单个气体传感器来完成。 如果您的项目旨在以非常精确的水平获得气体浓度，那么我们不推荐使用这种气体传感器。

有 4 种气体传感器，每种都可以检测不同类型的气体，这里我们用一张表来说明。

|传感器类型|气体类型|点击购买|
|:---:|---|---|---|
|MQ2|可燃气体，烟雾|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.37f75a9db6SL89&id=520242943642)|
|MQ3|酒精蒸汽|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.15.5b31c1aeUvb14f&id=45575808671)|
|MQ5|石油气，天然气，城镇煤气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.5b31c1aeUvb14f&id=45508638349)|
|MQ9|一氧化碳，煤气，液化气|[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5b31c1aeUvb14f&id=45575800587)|

##   产品特性
--------

-   检测范围广
-   工作稳定且寿命长
-   响应快，灵敏度高

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
-------------

| 项目  | 参数               | 最小值 | 典型值    | 最大值   | 单位 |
|------|---------------------|-----|------------|-----|------|
| VCC  | 工作电压     | 4.9 | 5          | 5.1 | V    |
| PH   | 热能耗 | 0.5 | -          | 800 | mW   |
| RL   | 负载电阻     |     | adjustable |     |      |
| RH   | 发热器电阻   | -   | 33         | -   | Ω    |
| Rs   | 敏电阻  | 3   | -          | 30  | kΩ   |

## Platforms Supported
-------------------

## 创意应用
-----------------

-   气体泄漏检测。
-   玩具。

## 硬件概述
-----------------

这是一个模拟输出传感器。 这需要连接到 [Grove Base Shield](/Base_Shield_V2) 中的任何一个模拟量插槽。 本教程中使用的示例使用 **A0** 模拟量引脚。将此模块连接到 Base Shield 的 **A0** 端口。

根据如下表所示的连接方式，使用跳线将 Grove 模块直接连接到 Arduino:

| Arduino   | Gas Sensor |
|-----------|------------|
| 5V        | VCC        |
| GND       | GND        |
| NC        | NC         |
| Analog A0 | SIG        |

当气体浓度增加时，气体传感器的输出电压增加。 灵敏度可以通过改变电位器来调节。 <font color="Red">请注意，传感器的最佳预热时间是 24 小时以上</font>。 有关 MQ-2 传感器的详细信息，请参阅**资源下载**部分中提供的 data-sheet。

## 入门指导
---------------

### 硬件准备

|名称|功能|数量|Link|
|----|--------|---|----|
|Base Shield V2 |提供 Grove 连接器 | 1 | [link](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.27adb9509R92gq&id=520233320144) |
|Seeeduino V4.2|控制器|1|[link](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.33.712cdf2fuhLMKx&id=45721222112)|
|Grove-Gas Sensor MQ2 |传感器|1|<a href="https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.6906def0XYQFRb&id=520242943642">link</a>|

### 连接

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/img/Read_Gas_Sensor_data_MQ2_MQ5.jpg)

将 Grove - Gas Sensor (MQ2) 连接到 **A0** 端口，如上图所示。

### 气体检测的基本示范例

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

这个例子说明了一种了解气体近似浓度的方法。 根据 MQx 传感器的数据表，这些方程式在标准条件下进行测试，并且没有被校准。 它可能会根据温度或湿度的变化而变化。

-  将气体传感器保持在清洁的空气环境中。 上传如下的程序 :

```
void setup() {
    Serial.begin(9600);
}

void loop() {
    float sensor_volt;
    float RS_air; //  Get the value of RS via in a clear air
    float R0;  // Get the value of R0 via in H2
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
    R0 = RS_air/9.8; // The ratio of RS/R0 is 9.8 in a clear air from Graph (Found using WebPlotDigitizer)

    Serial.print("sensor_volt = ");
    Serial.print(sensor_volt);
    Serial.println("V");

    Serial.print("R0 = ");
    Serial.println(R0);
    delay(1000);

}
```

-  然后打开 Arduino IDE 的串口监视器。 记下 R0 的值，这需要在下一个程序中使用。 读取稳定后，请将 R0 放在下方。

    <font color="Red"> 将 R0 值替换为上面测出的 R0 值 </font>. 将传感器暴露在上述任何一种气体中。

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

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/img/Gas_sensor_1.png)

根据该图可以看出，我们可以测试的最小浓度为 100ppm，最大值为 10000ppm，换句话说，我们可以得到 0.01% ~ 1% 之间的气体浓度。 然而，我们不能提供一个公式，因为比率和浓度之间的关系是非线性的。


## 资源下载
---------

-   **[Eagle文件]** [Grove Gas Sensor - EAGLE (Schematic and Board) files](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/res/Gas_Sensor_Eagle_files.zip)

-   **[原理图PDF]** [Grove Gas Sensor - PDF Schematic](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/res/Gas_Sensor_Schematic.pdf)

-   **[芯片数据手册]** [MQ-2 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Gas_Sensor-MQ2/master/res/MQ-2.pdf)

-   **[其他资源]** [How to choose a Gas Sensor](/How_to_choose_A_Gas_Sensor)

-   **[其他资源]** [What's LEL](http://en.wikipedia.org/wiki/Flammability_limit)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor(MQ2) -->
