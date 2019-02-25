---
name: Grove - Luminance Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Luminance-Sensor-p-1941.html
oldwikiname: Grove_-_Luminance_Sensor
prodimagename: Luminance.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Luminance_Sensor
sku: 101020076
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/img/Luminance.jpg)

Grove - Luminance Sensor 检测表面区域的环境光强度。 它使用 **APDS-9002** 模拟输出环境光照传感器。APDS-9002 测量频谱和人眼极其接近。Grove - Luminance Sensor 可用于要求照明自动调节的住宅或商业应用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.6.686bd0c8cCSeni&id=45574380098&ns=1&abbucket=1#detail)


## 规格参数
-------------

| 项目                   | 参数        |
|-----------------------------|--------------|
| Vcc                         | 2.4V ~ 5.5V  |
| 线性输出范围         | 0.0 ~ 2.3V   |
| 亮度测量范围 | 0 ~ 1000 Lux |

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

## 操作示例
-------------

**在 Seeduino Lotus 上使用 Grove Luminance sensor**

1.使用 Grove 线缆将 Grove-Luminance sensor 连接到 Seeeduino Lotus 的 **A0** 端口。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/img/Interface_Grove-Luminance.jpg)

2.将以下代码复制到 Arduino IDE 中。

```
float VoutArray[] =  { 0.0011498,  0.0033908,   0.011498, 0.041803,0.15199,     0.53367, 1.3689,   1.9068,  2.3};
float  LuxArray[] =  { 1.0108,     3.1201,  9.8051,   27.43,   69.545,   232.67,  645.11,   73.52,  1000};

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);

}

void loop() {
    // put your main code here, to run repeatedly:

    Serial.print("Vout =");
    Serial.print(readAPDS9002Vout(A0));
    Serial.print(" V,Luminance =");
    Serial.print(readLuminance(A0));
    Serial.println("Lux");
    delay(500);
}

float readAPDS9002Vout(uint8_t analogpin)
{
    // MeasuredVout = ADC Value * (Vcc / 1023) * (3 / Vcc)
    // Vout samples are with reference to 3V Vcc
    // The above expression is simplified by cancelling out Vcc
    float MeasuredVout = analogRead(A0) * (3.0 / 1023.0);
    //Above 2.3V , the sensor value is saturated

    return MeasuredVout;

}

float readLuminance(uint8_t analogpin)
{

    // MeasuredVout = ADC Value * (Vcc / 1023) * (3 / Vcc)
    // Vout samples are with reference to 3V Vcc
    // The above expression is simplified by cancelling out Vcc
    float MeasuredVout = analogRead(A0) * (3.0 / 1023.0);
    float Luminance = FmultiMap(MeasuredVout, VoutArray, LuxArray, 9);

    /**************************************************************************

    The Luminance in Lux is calculated based on APDS9002 datasheet -- > Graph 1
    ( Output voltage vs. luminance at different load resistor)
    The load resistor is 1k in this board. Vout is referenced to 3V Vcc.

    The data from the graph is extracted using WebPlotDigitizer
    http://arohatgi.info/WebPlotDigitizer/app/

    VoutArray[] and LuxArray[] are these extracted data. Using MultiMap, the data
    is interpolated to get the Luminance in Lux.

    This implementation uses floating point arithmetic and hence will consume
    more flash, RAM and time.

    The Luminance in Lux is an approximation and depends on the accuracy of
    Graph 1 used.

    ***************************************************************************/

    return Luminance;
}


//This code uses MultiMap implementation from http://playground.arduino.cc/Main/MultiMap

float FmultiMap(float val, float * _in, float * _out, uint8_t size)
{
    // take care the value is within range
    // val = constrain(val, _in[0], _in[size-1]);
    if (val <= _in[0]) return _out[0];
    if (val >= _in[size-1]) return _out[size-1];

    // search right interval
    uint8_t pos = 1;  // _in[0] allready tested
    while(val > _in[pos]) pos++;

    // this will handle all exact "points" in the _in array
    if (val == _in[pos]) return _out[pos];

    // interpolate in the right segment for the rest
    return (val - _in[pos-1]) * (_out[pos] - _out[pos-1]) / (_in[pos] - _in[pos-1]) + _out[pos-1];
}
```

3.上传代码至 seeeduino lotus。

4.将 Grove Luminance sensor 放在光源下面或需要检测亮度的地方。

5.打开串口监视器。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/img/LuminanceOutput.png)

6.数据将显示在串口监视器中。

## 资源下载
--------

-   **[Eagle 文件]** [Grove-Luminance Sensor eagle file](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/res/Grove-Luminance_Sensor.zip)
-   **[原理图 PDF]** [Grove-Luminance Sensor Schematic (PDF)](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/res/Grove-Luminance_Sensor_v1.0.pdf)
-   **[芯片数据手册]** [APDS-900 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/res/APDS-9002-.pdf)
-   **[其他资源]** [Grove-Luminance Sensor Demo code](https://raw.githubusercontent.com/SeeedDocument/Grove-Luminance_Sensor/master/res/Grove-Luminance.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Luminance_Sensor -->
