---
name: Grove - Barometer (High-Accuracy)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Barometer-(High-Accuracy)-p-1865.html
oldwikiname: Grove_-_Barometer_(High-Accuracy)
prodimagename: Grove-Barometer-High-Accuracy.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Barometer-High-Accuracy
sku: 101020068
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/img/Grove-Barometer-High-Accuracy.jpg)

该 Grove - Barometer (High-Accuracy) Sensor 采用 HP206C 高精度芯片，可检测气压，高度计和温度。 可以广泛测量 300mbar〜1200mbar 的压力，超高分辨率模式下的超高精度为 0.01mbar（0.1m），芯片仅接受 1.8V 至 3.6V 的输入电压。 然而，加上外部电路，该模块可以与 3.3V 和 5V 兼容。 因此，它可以在 Arduino / Seeeduino 或 Seeeduino Stalker 上使用，无需修改。它的设计是通过 I2C总线直接连接到微控制器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.27785814xJ3D2M&id=520516572843)

产品特性
--------


- 具有数字传输线线（I2C）接口
- 基于指令的读取方式，有补偿功能（可选）
- 可编写程序设置中断控制
- 全数据补偿
- 宽气压范围
- 灵活的电源电压范围
- 超低功耗
- 高度分辨率可达0.01米
- 能够进行温度测量

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

创意应用
-----------------


- 高精度移动的高度计/晴雨表
- 工业压力和温度传感器系统
- 汽车系统
- 个人电子测温仪
- 冒险和运动的手表
- 医用气体控制系统
- 气象站设备
- 室内导航和地图辅助
- 暖气，通风，空调

产品规格
--------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小
</th>
<th scope="col">
标准
</th>
<th scope="col">
最大
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
3.3
</td>
<td>
5
</td>
<td>
5.5
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
工作电流
</th>
<td>
635
</td>
<td>
/
</td>
<td>
1100
</td>
<td>
uA
</td>
</tr>
<tr align="center">
<th scope="row">
压力范围
</th>
<td>
300
</td>
<td>
/
</td>
<td>
1200
</td>
<td>
hPa
</td>
</tr>
<tr align="center">
<th scope="row">
I2C 数据传输频率
</th>
<td>
/
</td>
<td>
/
</td>
<td>
10
</td>
<td>
MHz
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
20.4x41.8x9.7
</td>
<td>
mm
</td>
</tr>
<tr align="center">
<th scope="row">
质量
</th>
<td colspan="3">
/
</td>
<td>
g
</td>
</tr>
</table>

Platforms Supported
-------------------

使用方式
-----

### 使用 Arduino

气压条件是用于预测天气变化和推断海拔高度的标准之一。 这是一个演示，向您展示如何从这个 Grove - Barometer Sensor 读取气压数据。

1.通过 Grove 连接线将其连接到 Seeeduino 或 Grove - Base Shield 的 **I2C** 端口。 并通过 USB 数据线将 Arduino 连接到 PC。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/img/Grove-Barometer_Sensor_hard.JPG)

2.下载库文件 [Grove_Barometer_HP20x](https://github.com/Seeed-Studio/Grove_Barometer_HP20x) 通过路径：.\\arduino-1.0.1\\libraries 将其解压缩到 Arduino IDE 的库文件中。

3.创建一个新的 Arduino 编辑页面，并将下面的代码粘贴到其中或直接通过路径打开代码：File（文件）-&gt; Example（示例） - > Barometer_Sensor-> Barometer_Sensor。

```
/*
* Demo name  ?: HP20x_dev demo
* Usage      ?: I2C PRECISION BAROMETER AND ALTIMETER [HP206C hopeRF]
* Author     ?: Oliver Wang from Seeed Studio
* Version    ?: V0.1
* Change log ?: Add kalman filter 2014/04/04
*/

#include <HP20x_dev.h>
#include <KalmanFilter.h>

#include "Arduino.h"
#include "Wire.h"

unsigned char ret = 0;

    /* Instance */
KalmanFilter t_filter;    //temperature filter
KalmanFilter p_filter;    //pressure filter
KalmanFilter a_filter;    //altitude filter


void setup()
{
    Serial.begin(9600);        // start serial for output

    Serial.println("****HP20x_dev demo by seeed studio****\n");
    Serial.println("Calculation formula: H = [8.5(101325-P)]/100 \n");
      /* Power up,delay 150ms,until voltage is stable */
    delay(150);
      /* Reset HP20x_dev */
    HP20x.begin();
    delay(100);

      /* Determine HP20x_dev is available or not */
    ret = HP20x.isAvailable();
    if(OK_HP20X_DEV == ret)
    {
        Serial.println("HP20x_dev is available.\n");
    }
    else
    {
        Serial.println("HP20x_dev isn't available.\n");
    }

}


void loop()
{
    char display[40];
    if(OK_HP20X_DEV == ret)
    {
        Serial.println("------------------\n");
        long Temper = HP20x.ReadTemperature();
        Serial.println("Temper:");
        float t = Temper/100.0;
        Serial.print(t);
        Serial.println("C.\n");
        Serial.println("Filter:");
        Serial.print(t_filter.Filter(t));
        Serial.println("C.\n");

        long Pressure = HP20x.ReadPressure();
        Serial.println("Pressure:");
        t = Pressure/100.0;
        Serial.print(t);
        Serial.println("hPa.\n");
        Serial.println("Filter:");
        Serial.print(p_filter.Filter(t));
        Serial.println("hPa\n");

        long Altitude = HP20x.ReadAltitude();
        Serial.println("Altitude:");
        t = Altitude/100.0;
        Serial.print(t);
        Serial.println("m.\n");
        Serial.println("Filter:");
        Serial.print(a_filter.Filter(t));
        Serial.println("m.\n");
        Serial.println("------------------\n");
        delay(1000);
    }
}
```

4.打开串行监视器来接收传感器的数据，包括温度，气压值，相对气压和高度。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/img/Barometer_Sensor.jpg)

以下是绘制海拔高度与大气压力之间关系的参考图。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/img/Pressure_and_Altitude.jpg)


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/res/Grove_Barometer_High-Accuracy_v1.0_sch_pcb.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


资源下载
---------

-   [Grove_Barometer_High-Accuracy_v1.0_sch_pcb Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/res/Grove_Barometer_High-Accuracy_v1.0_sch_pcb.zip)
-   [HP206C Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer-High-Accuracy/master/res/HP206C_Datasheet.pdf)
-   [Github repository for Grove\_Barometer\_HP20x](https://github.com/Seeed-Studio/Grove_Barometer_HP20x)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Barometer_(High-Accuracy) -->
