---
title: Solar Charger Shield V2.2
category: Shield
bzurl: https://www.seeedstudio.com/Solar-Charger-Shield-v2.2-p-2391.html
oldwikiname:  Solar Charger Shield V2.2
prodimagename:  Solar_Charger_Shield_v2.2.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Solar_Charger_Shield_V2.2
sku: 106990020
---
![](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/img/Solar_Charger_Shield_v2.2.jpg)

Solar Charger Shield V2.2 是一个 Arduino 平台的可堆叠扩展板，配有电源管理功能，充当能量采集器，用于现场充电。您可以使用电压为 3.0V-4.2V 的各种电池升压 5V 输出，或者将锂离子电池和太阳能电池板组合在一起形成一个自主传感器系统。电路板提供的最大电流可达 600mA。太阳能板、USB口都可以给锂电池充电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.32ccc9e8QuwOWZ&id=45456743177&ns=1&abbucket=1#detail)

##   产品特性
---
*   输出断开

*   短路保护

*   连接电池时 3V 输出

*   连续充电电流高达 900mA

*   电池状态指示 ( 红 : 充电中 , 绿 : 充电完成 )

*   Micro-USB 连接器

##   规格参数
---
*   电池输入电压 : 3.0~4.5V

*   USB 输入电压 : 4.75~5.25V

*   太阳能输入电压 : 4.8~6V

*   最大输出电压(带电池): 3W(600mA@5V)

*   纹波电压 ：&lt;100mV @ 500mA

*   尺寸 : 68*53mm

##   创意应用
---
*   无线传感器
*   太阳能充电

##  使用太阳能板充电
---
1) 太阳光和白炽灯都可以给太阳能板充电，前者的效率要高于后者。太阳能板需要紫外线或红外线的辐射来产生电流。

2) 测试太阳能板在白炽灯下的工作效率时，把太阳能板放置到距离灯小于 20cm 处。然而在白炽灯下的充电效率并不高。

3) 太阳能板的放置呈一定角度能最大程度接收到光照。

4) 避免太阳能板和水或水蒸气过度接触，可能会氧化太阳能板，降低转化效率。

5) 通常太阳能板出厂会配有塑料保护膜，使用前请撕掉它。

6) 爱护太阳能板，避免刮痕和碰撞。

##   注意事项
---
1) Solar Charger Shield V2.2 设计时已考虑到短路保护的问题，但使用时仍然要避免短路。

2) Solar Charger Shield V2.2 工作电压不能超过 5V。

##   使用方法
---
1) 把电池和太阳能板安装在相应的接口上，如下图所示 :

![](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/img/Solar_Charger_Shield_v2.2_inputs.jpg)



2) 太阳能板放置在阳光或白炽灯下，参照“使用太阳能板充电”部分。

3) 确保红色充电指示灯亮，见下图 :

![](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/img/Solar_Charger_Shield_v2.2_charging.jpg)

4) 充电完成后绿色指示灯亮。

5) 充电完成后，把 Solar Charger Shield V2.2 安装到 Arduino 上，把开关拨到ON上，它会给给 Arduino 供电，如下所示 :

![](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/img/Solar-Charger-Shield-v2.2_power-arduino.jpg)

##   产品测试
---
本部分将教您如何测量锂电池的电压。

将 **VBAT** 引脚连接到模拟引脚 **A0**，以便我们可以读取来自 **A0** 引脚的数据，我们需要使用一个跨接电阻器来短接 R7，如图所示 :

![](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/img/Solar_Charger_Shield_v2.2_shortR7.jpg)

###   编程示例

您可以通过以下示例测量电池的电压 :
```
/*
 Solar charger shield voltage measurement example. Connect VBAT pin to analog pin A0.

 The pin measures 2.0 V when not under direct exposre to sunlight and 5V when exposed to sunlight.

 This example code is in the public domain.

 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the VBAT pin is attached to


int BatteryValue = 0;        // value read from the VBAT pin
float outputValue = 0;        // variable for voltage calculation

void setup() {
    // initialize serial communications at 9600 bps:
    Serial.begin(9600);
}

void loop() {
    // read the analog in value:
    BatteryValue = analogRead(analogInPin);
    // Calculate the battery voltage value
    outputValue = (float(BatteryValue)*5)/1023*2;
    // print the results to the serial monitor:
    Serial.print("Analog value = " );
    Serial.print(BatteryValue);
    Serial.print("\t voltage = ");
    Serial.println(outputValue);
    Serial.println("V \n");

    // wait 10 milliseconds before the next loop
    // for the analog-to-digital converter to settle
    // after the last reading:
    delay(10);
}
```
##  资源下载
---
- **[Eagle文件]** [Solar Charger Shield v2.2 sch&amp;pcb](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/res/Solar_Charger_Shield_v2.2_sch_pcb.zip)

- **[原理图PDF]** [Solar Charger Shield v2.2.pdf](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/res/Solar%20Charger%20Shield%20v2.2.pdf)
- **[芯片数据手册]** [DSE-CN3065.pdf](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/res/DSE-CN3065.pdf)

- **[芯片数据手册]** [ETA1036.pdf](https://github.com/SeeedDocument/Solar_Charger_Shield_V2.2/raw/master/res/ETA1036.pdf)
