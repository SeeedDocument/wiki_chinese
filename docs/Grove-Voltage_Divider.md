---
title: Grove - Voltage Divider
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Voltage-Divider-p-1472.html
oldwikiname: Grove - Sunlight Sensor
prodimagename: Voltage_Divider_01.jpg
wikiurl: http://seeed.wiki/Grove-Voltage_Divider
sku: 104020000
---
![](https://github.com/SeeedDocument/Grove-Voltage_Divider/raw/master/img/Voltage_Divider_01.jpg)

Grove – Voltage Divider 提供了测量外部电压的接口，无需将电阻连接到输入接口。另外，电压增益可以通过拨码开关选择，使用方便简单。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.4f39e018wrr0YA&id=45764073725)

## 产品特性
---
- 外部电压接口和 Grove 接口
- 使用简便
- 可调整增益

!!!Tip
    了解更多 Grove 系统，请点击 [这里](http://seeed.wiki/Grove_System/)

## 规格参数
---

|项目|	最小值	|典型值	|最大值	|单位|
|---|---|---|---|---|
|工作电压|	4.7	|5.0|	5.3	|V DC|
|测量精度	|/|<=1|/|	 %|
|测量电压范围	(拨码选择 3)|	0.3	|/|	12.9|	V|
|测量电压范围 (拨码选择 10)|1.0	|/	|43|V|
|尺寸	|/|24X20|/|	mm|

## 使用方法
---
测量外部电压时，将外部电压连接到模块 J1 口，然后将板载 Grove 接口连接到 Arduino/Seeeduino 的模拟端口：
- 使用 Grove 线把模块连接到 [Grove - Base Shield](http://wiki.seeedstudio.com/wiki/Grove_-_Base_Shield) 的 A0 接口。
- 把 [Grove - Base Shield](http://wiki.seeedstudio.com/wiki/Grove_-_Base_Shield) 插到 Arduino/Seeeduino 上。

为了测试模块的精度，我测试了一些电压输入并得到了如下数据：

![](https://github.com/SeeedDocument/Grove-Voltage_Divider/raw/master/img/Voltage_Divider_Test_Score.jpg)

- 正如你所看到的，当输入在测量范围内时，分压器的精确度很高（<1%，我标记为“OK”）。但是，当输入超出范围时，准确度变低（我标记为“ON”）。

而当分压器输出电压高于 VCC（模拟量 Grove 接口电压和参考电压）时，指示灯将亮起以显示错误。

- 使用 Arduino 的串行监视器，您可以显示输入电压值。 演示代码如下所示：

```
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    long  sensorValue=analogRead(A0);
    long  sum=0;
    for(int i=0;i<1000;i++)
    {
        sum=sensorValue+sum;
        sensorValue=analogRead(A0);
        delay(2);
    }
    sum=sum/1000;

    Serial.print("if you set the Gain to 10,the input voltage:");
    Serial.println(10*sum*4980/1023.00);

    Serial.print("if you set the Gain to 3,the input voltage:");
    Serial.println(3*sum*4980/1023.00);

    delay(1000);
}
```

## 资源下载
---
- **[Eagle 文件]**[Grove - Voltage Divider Eagle File](https://github.com/SeeedDocument/Grove-Voltage_Divider/raw/master/res/Grove-Voltage_Divider_Eagle_File.zip)
- **[数据手册]**[LMV358ID Datasheet](https://github.com/SeeedDocument/Grove-Voltage_Divider/raw/master/res/LMV358ID_Datasheet.pdf)
