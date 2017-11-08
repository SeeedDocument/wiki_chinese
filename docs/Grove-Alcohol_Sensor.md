---
title: Grove - Alcohol Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Alcohol-Sensor-p-764.html
oldwikiname: Grove_-_Alcohol_Sensor
prodimagename: Alcohol_sensor_01.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020044 1.jpg
wikiurl: http://seeed.wiki/Grove-Alcohol_Sensor
sku: 101020044
tags: grove_analog, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/img/Alcohol_sensor_01.jpg)

Grove - Alcohol Sensor 是适用于 Arduino 或 Seeeduino 的一个完整酒精传感器模块。它由基于 [MQ303A](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/res/MQ303A.pdf) 半导体酒精传感器。它具有良好的灵敏度可对酒精快速反应。适合做呼吸酒精测验。该 Grove 具备了 MQ303A 的所有必要电路，如电源调节和加热器电源。该传感器输出电压与空气中的酒精浓度成反比。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3c08ae55agDFLx&id=520903013610)

<div class="admonition danger">
<p class="admonition-title">Note</p>
请注意传感器值仅反映气体浓度在允许误差范围内的近似趋势，它不表示精确的气体浓度。 空气中某些部件的检测通常需要更精确和更昂贵的仪器，这些仪器不能用单个气体传感器来完成。 如果您的项目旨在以非常精确的水平获得气体浓度，那么我们不推荐使用这种气体传感器。
</div>

## 产品特性
--------

-   输入电压 : 5V
-   工作电流 : 120mA
-   检测浓度范围 : 20-1000ppm
-   Grove 兼容连接器。
-   对酒精高灵敏度。
-   酒精暴露后快速反应和恢复。
-   寿命长。
-   紧凑的外形尺寸。

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported
-------------------

## 使用方法
-----

### 硬件连接

Grove 产品拥有一个生态系统，并且都有一个可以插入 [Grove Base Shield](/Base_Shield_V2) 的连接器。 将此模块连接到 Base Shield 的 **A0** 端口，但是也可以通过跳线将气体传感器连接到 Arduino，而不需要 Base Shield。

| Arduino UNO | Alcohol Sensor |
|-------------|----------------|
| 5V          | VCC            |
| GND         | GND            |
| Analog A1   | SCL            |
| Analog A0   | DAT            |

您可以通过传感器的 **DAT** 引脚获得当前的电压。<font color="Red">请注意，传感器的最佳预热时间是大于 48 小时</font>。有关酒精传感器的详细信息，请参考数据手册。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/img/Twig_Alcohol_Sensor_Connected_To_Seeeduino_via_BaseStem.jpg)

### 下载和上传代码

在得到气体的浓度之前有两个步骤需要完成。

首先，如上图所示使用 **A0** 将模块与 Grove Shield 连接。并将传感器放在空气中，并使用下面的程序。

```
#define heaterSelPin 15

void setup() {
    Serial.begin(9600);
    pinMode(heaterSelPin,OUTPUT);   // set the heaterSelPin as digital output.
    digitalWrite(heaterSelPin,LOW); // Start to heat the sensor
}

void loop() {
    float sensor_volt;
    float RS_air; //  Get the value of RS via in a clear air
    float sensorValue;

/*--- Get a average data by testing 100 times ---*/
    for(int x = 0 ; x < 100 ; x++)
    {
        sensorValue = sensorValue + analogRead(A0);
    }
    sensorValue = sensorValue/100.0;
/*-----------------------------------------------*/

    sensor_volt = sensorValue/1024*5.0;
    RS_air = sensor_volt/(5.0-sensor_volt); // omit *R16
    Serial.print("sensor_volt = ");
    Serial.print(sensor_volt);
    Serial.println("V");
    Serial.print("RS_air = ");
    Serial.println(RS_air);
    delay(1000);
}
```

然后打开 Arduino IDE 的监视器，可以看到一些数据被打印出来，记下 RS_air 的值，您需要在下面的程序中使用它。在此步骤中，您可以需要花一点时间来测得 RS_air 的值。

```
#define heaterSelPin 15

void setup() {
    Serial.begin(9600);
    pinMode(heaterSelPin,OUTPUT);   // set the heaterSelPin as digital output.
    digitalWrite(heaterSelPin,LOW); // Start to heat the sensor
}

void loop() {

    float sensor_volt;
    float RS_gas; // Get value of RS in a GAS
    float ratio; // Get ratio RS_GAS/RS_air
    int sensorValue = analogRead(A0);
    sensor_volt=(float)sensorValue/1024*5.0;
    RS_gas = sensor_volt/5.0-sensor_volt; // omit *R16

  /*-Replace the name "R0" with the value of R0 in the demo of First Test -*/
    ratio = RS_gas/RS_air;  // ratio = RS/R0
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

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/img/Gas_Sensor_5.png)

根据该图可以看出，我们可以测试的最小浓度为 20ppm，最大值为 10000ppm，换句话说，可以得到 0.002% ~ 1% 之间的气体浓度。然而我们不能提供一个公式，因为比率和浓度之间的关系是非线性的。

<div class="admonition note">
<p class="admonition-title">Notes</p>
<p> a. 该值在 500 至 905 之间变化。因此，高于 650 的值表示附近的酒精蒸气。</p>
<p> b. 一旦暴露于酒精蒸汽，传感器值需要一段时间才能完全降低。</p>
<p> c. 然而，任何新的曝光将变现为传感器值的瞬间增加。</p>
</div>


<div class="admonition danger">
<p class="admonition-title">Caution</p>
<p> a. 酒精传感器是非常灵敏的半导体器件。小心轻放。</p>
<p> b. 不要暴露于有机硅蒸汽，碱性或腐蚀性气体。</p>
<p> c. 不要使用冷冻水或将水溢出。</p>
<p> d. 保持适当的工作电压。</p>
</div>

## 资源下载
---------

- **[Eagle文件]** [Grove-Alcohol Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/res/Twig_-_Alcohol_Sensor_Eagle_Files.zip)
- **[Eagle文件]** [Grove-Alcohol Sensor v1.2 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/res/Grove-Alcohol_Sensor_sch_pcbv1.2.zip)
- **[原理图PDF]** [Schematics in PDF Format](https://github.com/SeeedDocument/Grove-Alcohol_Sensor/raw/master/res/Grove%20-%20Alcohol%20Sensor%20v1.2.pdf)
- **[其他文件]** [How to Choose A Gas Sensor](/How_to_choose_A_Gas_Sensor)
- **[其他文件]** [MQ303A](https://raw.githubusercontent.com/SeeedDocument/Grove-Alcohol_Sensor/master/res/MQ303A.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Alcohol_Sensor -->
