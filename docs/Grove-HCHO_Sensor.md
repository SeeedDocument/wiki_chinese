---
name: Grove - HCHO Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-HCHO-Sensor-p-1593.html
oldwikiname: Grove_-_HCHO_Sensor
prodimagename: HCHO_Sensor_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-HCHO_Sensor
sku: 101020001
tags: grove_analog, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/img/HCHO_Sensor_01.jpg)

Grove - HCHO Sensor是一种半导体VOC气体传感器。 其设计基于WSP2110，它的电导率可以随着空气中VOC气体浓度而变化。 通过电路，电导率可以转换为对应于气体浓度的输出信号。 该传感器可以检测浓度高达1ppm的气体。 适用于检测甲醛，苯，甲苯等挥发性成分。 本产品可用于在家庭环境中检测有害气体。 因此，这是提升室内环境质素的好帮手。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11Z15PDh&id=45506470348)

<div class="admonition warning">
<p class="admonition-title">Warning</p>
这个传感器输出的数值仅仅能够反映在允许误差范围内气体浓度的近似趋势，它不能精确的表示气体浓度。 空气中特定成分的检测通常需要更精确、更加昂贵的仪器，这不能只使用一个气体传感器来完成。 如果您的项目旨在获得非常精确的气体浓度，那么我们不推荐使用这种气体传感器。
</div>

产品参数
-------------

-   工作电压: 5.0V ± 0.3V
-   目标气体：HCHO，苯，甲苯，酒精
-   浓度范围：1〜50 ppm
-   传感器电阻值（Rs）：10KΩ-100KΩ（10ppm HCHO）
-   灵敏度：Rs（空气中）/ Rs（10ppm HCHO）≥5

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

支持平台
-------------------

入门指导
---------------

Grove - HCHO Sensor可用于检测VOC，如HCHO，甲苯，苯，酒精。 在这里，我们以HCHO为例来演示如何使用该传感器。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/img/HCHO_Hardware_Connection.jpg)

```
// demo of Grove - HCHO Sensor

#define Vc 4.95

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int sensorValue=analogRead(A0);
    float R0=(1023.0/sensorValue)-1;
    Serial.print("R0 = ");
    Serial.println(R0);
    delay(500);
}
```

在上传代码后，打开串口监视器，使R0输出的数值显示在正常状态下（在室外是最好的）。

使用小起子调整R1（蓝色电位器）的电阻，使R0的数值在10-100范围内，并记录该数字（我的R0显示的在正常状况下为34.28）。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/img/R0.png)

在 `#define R0 ***`中输入之前R0的显示的数值，然后上传代码。 记住不要再拧紧R1，除非你决定再次检测R0的值。

```
// demo of Grove - HCHO Sensor
#include <math.h>
#define Vc 4.95
//the number of R0 you detected just now
#define R0 34.28

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int sensorValue=analogRead(A0);
    double Rs=(1023.0/sensorValue)-1;
    Serial.print("Rs = ");
    Serial.println(Rs);
    double ppm=pow(10.0,((log10(Rs/R0)-0.0827)/(-0.4807)));
    Serial.print("HCHO ppm = ");
    Serial.println(ppm);
    delay(1000);
}
```

然后将传感器移入办公室，并读取HCHO ppm值：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/img/Rs.png)

从典型灵敏度曲线图我们可以知道这个检测范围是1-50ppm。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/img/Sensitivity_Characteristic.jpg)

要检测其他VOC气体，可以计算Rs / R0，然后参考灵敏度特性曲线图，找到相应的气体浓度。 或者使用以下python程序来匹配对应的曲线并计算a和b的值：

`ppm = 10 ^ ((log10(Rs/R0) + a) / b)`

```
# coding=utf-8
# calculate a and b of HCHO
import numpy as np
import matplotlib.pyplot as plt

#get the measure data from the Typical Sensitivity Curve
x = np.array([1, 5, 10, 20, 40])
y = np.array([1.21, 0.56, 0.4, 0.3, 0.21])

plt.subplot(221)
plt.loglog(x,y,lw=2)
#plt.ylim(0,1.5)  
plt.xlabel('log(x)')  
plt.ylabel('log(y)')  
plt.show()  
```

资源下载
---------

-   [Grove - HCHO Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/res/Grove-HCHO_Sensor_Eagle_File.zip)
-   [Grove - HCHO Sensor Schematic in PDF](https://github.com/SeeedDocument/Grove-HCHO_Sensor/raw/master/res/Grove%20-%20HCHO%20Sensor.pdf)
-   [WSP2110 Datasheet (Chinese)](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/res/WSP2110.pdf)
-   [WSP2110 Datasheet (English)](https://raw.githubusercontent.com/SeeedDocument/Grove-HCHO_Sensor/master/res/Wsp2110-1-.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_HCHO_Sensor -->
