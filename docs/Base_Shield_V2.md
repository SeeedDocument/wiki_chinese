---
title: Base Shield V2
category: Shield
bzurl: https://www.seeedstudio.com/base-shield-v13-p-1378.html
oldwikiname:
prodimagename: Base_Shield_v2-1.png
surveyurl: https://www.surveymonkey.com/r/base_shield_v2
sku: 103030000
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Base_Shield_V2/master/img/Base_Shield_v2-1.png)

作为扩展板，Base Shield v2有许多Grove连接接口，方便您将多个Grove产品一起使用。它与一系列Arduino产品兼容。

!!!Note
    -  点击获取更多信息 [Grove System](/Grove_System/).

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797vOWxHW&id=520233320144)


## 产品特性

* 电源兼容：每个Grove连接器都有四根电线，其中一根是Vcc。但是，并不是每个微控制器主板都需要5V的电源电压，有些需要3.3V。这就是为什么我们在Base Shield v2上添加一个电源开关。这样，您可以通过该开关调节Vcc的电压，确保Vcc的电压与主板的电源相同。

    所以在使用Arduino UNO与Base Shield v2时，请将开关转到5v位置; 在使用带有Base Shield v2的Seeeduino Arch时，请将开关转到3.3v。


* 开发板兼容：引脚数与Arduino UNO R3相同。


!!!Note
    - 如果使用带有Seeeduino V3的Base Shield v2，请焊接P1，P2。

Grove 连接器: Base Shield v2 有16个Grove 连接头.

| 参数 | 名称 | 数量|
|----------------|---------|-----|
|Analog port|	A0/A1/A2/A3	|4|
|Digital port|	D2/D3/D4/D5/D6/D7/D8	|7|
|UART port|	UART|	1|
| 2C port  |	I2C  |	1 |

* 尺寸: 2.1 * 2.7 英寸
* LED 指示: 供电时绿色LED指示灯亮起。

### 兼容性

我们已经生产了大量的扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有的平台板兼容，这里我们使用表格来说明这些板与平台板的兼容性。


!!!note
    请注意，下表中标识的"Not recommended"并不代表一定就不能兼容，可能您需要一些额外的操作，比如跳线、焊接。如此，部分标识不兼容的也是可能正常使用的。更多兼容性信息请联系我们的技术支持techsupport@seeed.cc。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)



## 应用

我们已经使用了Grove - LED和Grove - Button与Base Shield v2。所有Grove产品都有Grove连接器，可以直接插入Base Shield。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Base_Shield_V2/master/img/Base_Shield_v2-3.png)

```
/*
 The circuit:
* LED attached from pin 3 to ground
* Button attached to pin 2 from +5V
* 10K resistor attached to pin 2 from ground
* Button Control An LED
*/

const int button = 2;       // the Grove port No. you attached a button to
const int LED    = 3;       // the Grove port No. you attached an LED to
void setup()
{
    pinMode(button, INPUT); //set button as an INPUT device
    pinMode(LED, OUTPUT);   //set LED as an OUTPUT device
}
void loop()
{
    int btn = digitalRead(button); //read the status of the button
    digitalWrite(LED, btn);
    delay(10);
}
```

##资源下载

* **[Easyeda原理图]** [Schematic at Easyeda](https://easyeda.com/Seeed/Base_Shield_v2-73af558cabc84d489aa150d218c9a39d)
*  **[Base Shield原理图]** [Schematic of Base Shield v2](https://raw.githubusercontent.com/SeeedDocument/Base_Shield_V2/master/res/Base_Shield_v2.zip)
*  **[Base Shield原理图 pdf版]** [Schematics PDF of Base Shield V2](https://raw.githubusercontent.com/SeeedDocument/Base_Shield_V2/master/res/Base_Shield_v2.pdf)
