---
title: Grove - Flame Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Flame-Sensor-p-1450.html
oldwikiname: Grove_-_Flame_Sensor
prodimagename: Flame_Sensor_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Flame_Sensor
sku: 101020049
tags: grove_digital, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Flame_Sensor/master/img/Flame_Sensor_01.jpg)

 Grove - Flame Sensor 可用于检测波长760nm至1100nm范围内波长的火源或其他光源。 它是基于YG1006传感器，它是一种能够快速处理信号和具有高灵敏度的NPN硅光电晶体管。 由于采用黑色环氧树脂材质，传感器对红外辐射敏感。 在消防机器人组成中，传感器起着非常重要的作用，可以作为机器人找到火源的眼睛。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.67713b2eWbqO5p&id=45575868600)

产品特性
-------


- 兼容Grove接口
- 对于火光具有很高的灵敏度
- 响应时间很快
- 使用方便
- 灵敏度可调

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

规格参数
-------------

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
4.75
</td>
<td>
5.0
</td>
<td>
5.30
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
/
</td>
<td>
20
</td>
<td>
/
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
检测到光谱带宽的范围
</th>
<td>
760
</td>
<td>
940
</td>
<td>
1100
</td>
<td>
nm
</td>
</tr>
<tr align="center">
<th scope="row">
检测范围
</th>
<td>
0
</td>
<td>
~
</td>
<td>
1
</td>
<td>
m
</td>
</tr>
<tr align="center">
<th scope="row">
响应时间
</th>
<td colspan="3">
15
</td>
<td>
μS
</td>
</tr>
<tr align="center">
<th scope="row">
工作温度
</th>
<td>
-25
</td>
<td>
~
</td>
<td>
85
</td>
<td>
℃
</td>
</tr>
</table>

支持平台
-------------------

使用方法
-----

该模块主要用于检测红外线。 它通过比较器输出数字信号 **0** 和 **1**。 检测到红外灯时，输出值为 **0**。 它的灵敏度可由精密的电位计调节。

我们来用它来控制。 当输出值为 **0** 时，LED将亮起。


1.使用4针的 grove 连接线将模块连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的 **D3** 端口。

2.将 Grove - Base Shield 插入到 Arduino。

3.使用 USB 数据线将 Arduino 连接到 PC。

4.将下面的代码复制并粘贴到新的 Arduino 编辑页面上。

```
    /******************************************************************************/

    #define SENSOR 3 //connect SENSOR to digital pin3
    #define LED 2//connect Grove - LED to pin2

void setup()
{
    pinsInit();
}
void loop()
{
    if(isFlameDetected())
    turnOnLED();
    else turnOffLED();
}
    /********************************/
void pinsInit()
{
    pinMode(FLAME_SENSOR, INPUT);
    pinMode(LED,OUTPUT);
    digitalWrite(LED,LOW);
}
void turnOnLED()
{
    digitalWrite(LED,HIGH);
}
void turnOffLED()
{
    digitalWrite(LED,LOW);
}
boolean isFlameDetected()
{
    if(digitalRead(FLAME_SENSOR))
    return false;
    else return true;
}
```

5.当有检测到红外线的时候，LED会点亮。 你可以使用它来设计您的产品。

参考
---------

传感器可以检测波长在760nm-1100nm范围内的光源。 下图显示了光谱灵敏度。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Flame_Sensor/master/img/Spectral_Sensitive.jpg)

资源下载
--------

-   [Grove - Flame Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Flame_Sensor/master/res/Grove-Directional_Light_Sensor_Eagle_File.zip)
-   [Github repository for Grove_Flame_Sensor Library](https://github.com/Seeed-Studio/Grove_Flame_Sensor)
-   [LM293D datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Flame_Sensor/master/res/LM293D.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Flame_Sensor -->
