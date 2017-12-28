---
title: Grove - Temperature Sensor V1.2
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Temperature-Sensor-p-774.html
oldwikiname: Grove - Temperature Sensor V1.2
prodimagename: Grove_Temperature_Sensor_View.jpg
wikiurl: http://seeed.wiki/Grove-Temperature_Sensor_V1.2/
sku: 101020015
tags: io_3v3, io_5v, plat_duino
---
![](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/img/Grove_Temperature_Sensor_View.jpg)

Grove - Temperature Sensor使用[热敏电阻](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/res/NCP18WF104F03RC.pdf) 来检测环境温度。 当环境温度降低时，热敏电阻的电阻将增加。 我们利用这个特性对环境温度进行预测。 该传感器的可检测范围为-40 - 125ºC，精度为±1.5ºC

!!!Note
    这个wiki资料的内容适用于Grove - Temperature sensorV1.1，同样也适用于V1.0，请参阅[Grove - Temperature Sensor](http://wiki.seeedstudio.com/wiki/Grove_-_Temperature_Sensor)

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11LH3OmL&id=520512844173)

## 产品特性
---
- 工作电压: 3.3 ~ 5V
- 零功率电阻: 100 KΩ
- 电阻容差: ±1%
- 工作温度范围: -40 ~ +125 ℃
- 标称B常数： 4250 ~ 4299K

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

## 入门指导
---
通过本节的学习之后，您只需要通过几步就可以使用Grove - Temperature Sensor V1.1 / 1.2完成项目。

**准备工作**  

现在我们做一个简单的演示，展示如何使用Grove - Temperature Sensor V1.1/1.2获得数据，下面是我们需要准备的模块。

- Seeeduino v4.2

Seeeduino V4.2与Arduino是完全兼容的。如果这是您第一次使用Arduino，请参阅 [这里](
http://seeed.wiki/Getting_Started_with_Seeeduino/)开始您的Arduino旅程。

**硬件连接**

只需将Grove - Temperature Sensor连接到Seeeduino v4.2的A5端口上
如下所示：

![](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/img/Grove_Temperature_Sensor_Hw_connect.jpg)


**下载程序**

启动Arduino IDE，然后单击File(文件)>New(新建)以打开新的编辑页面。

然后把下面的程序复制到Arduino IDE上:
```
// Demo code for Grove - Temperature Sensor V1.1/1.2
// Loovee @ 2015-8-26

#include <math.h>

const int B = 4275;               // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
const int pinTempSensor = A5;     // Grove - Temperature Sensor connect to A5

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int a = analogRead(pinTempSensor);

    float R = 1023.0/a-1.0;
    R = R0*R;

    float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // convert to temperature via datasheet

    Serial.print("temperature = ");
    Serial.println(temperature);

    delay(100);
}
```

点击Tools（工具）>Board（板） 选择Arduino UNO 并且选择相应的端口

现在点击上传（CTRL + U）录入测试代码。 请参考这里在上传过程中可能出现的错误提示，您也可以在论坛上进行评论，寻求帮助。

**看到的结果**

上传完成后，打开Arduino IDE的Tools（工具）>Serial Serial Monitor（串口监视器），可以获得温度数据：

![](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/img/Grove_Temperature_Sensor_result.jpg)


## 参考
---
如果你想知道温度算法如何来，请参考下图：

![](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/img/Grove_Temperature_Sensor_Basic_Characteristics.jpg)


## 资源下载
---
- [Schematic at Easyeda](https://easyeda.com/Seeed/Grove_Temperature_sensor_v1_2-ed433e462f14455e9aa38ae1a06e4680)
- [Grove - Temperature Sensor v1.1 Eagle File](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/res/Grove_-_Temperature_sensor_v1.1.zip)
- [Grove - Temperature Sensor v1.1.PDF](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/res/Grove_-_Temperature_sensor_v1.1.pdf)
- [Temperature Sensor datasheet](https://github.com/SeeedDocument/Grove-Temperature_Sensor_V1.2/raw/master/res/NCP18WF104F03RC.pdf)
