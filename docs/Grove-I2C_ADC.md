---
name: Grove - I2C ADC
category: Communication
bzurl: https://seeedstudio.com/Grove-I2C-ADC-p-1580.html
oldwikiname: Grove_-_I2C_ADC
prodimagename: I2C_ADC_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-I2C_ADC
sku: 103020013
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/I2C_ADC_01.jpg)

Grove - I2C ADC 是基于 ADC121C021 的 12 位精密 ADC 模块。通过提供恒定的参考电压，它可以帮助您提高从模拟传感器收集的数值的准确性。由于其地址可变，最多可以同时使用最多 9 个 I2C ADC。 另一方面，该模块提供自动睡眠功能，可大大降低功耗。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.47590c2ef7Gcih&id=45477279346)

## 产品特性
-------

-   低功耗
-   高精度
-   自动掉电模式
-   地址可变

!!!Tip
     关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
-------------

| 项目            | 典型值 | 单位 |
|-----------------|---------|------|
| 工作电压 | 5.0     | VDC  |
| 分辨率      | 12      | Bit  |
| 采样率     | 188.9   | ksps |
| 尺寸       | 40X20   | mm   |

## Platforms Supported
-------------------

## 硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/IIC_ADC_Interface.png)
**J1:** 用于将 Arduino IIC 接口连接为 Grove - I2C ADC 输出接口。

**J2:** 用于将模拟传感器连接为 Grove - I2C ADC 输入接口。

**U1:** ADC121C021 IC，12 位模数转换器

**黑线区域用于设置 IIC 地址。 ADDR0 和 ADDR1 运出连接到 L，您可以将它们更改为 "H"，或者通过在板上进行一点修改把它更改为 Floating（悬空） ( Floating 既不连接 "H" 也不连接 "L")。 请在参考资料中查找详细信息。**

## 入门指导
---------------

### 与 [Arduino](/Arduino "Arduino") 一起使用

Grove - I2C ADC 有两个接口 : 输入插座 **(J2)** 和输出插座 **(J1)**。 将模拟传感器连接到Grove - I2C ADC 的输入插座，并通过 Grove 线缆将 I2C ADC 连接到 Arduino/Seeeduino。

以 Grove - Gas Sensor 为例，现在我们将学习如何使用 Grove - I2C ADC 读取传感器数据。
硬件安装应该是这样的 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/Read_gas_sensor_data_using_I2C_ADC.jpg)

现在您可以使用下面的代码读取气体传感器的值。

```
#include <Wire.h>
 
#define ADDR_ADC121             0x55
 
#define V_REF 3.00
 
#define REG_ADDR_RESULT         0x00
#define REG_ADDR_ALERT          0x01
#define REG_ADDR_CONFIG         0x02
#define REG_ADDR_LIMITL         0x03
#define REG_ADDR_LIMITH         0x04
#define REG_ADDR_HYST           0x05
#define REG_ADDR_CONVL          0x06
#define REG_ADDR_CONVH          0x07
 
unsigned int getData;
float analogVal=0;         // convert
void init_adc()
{
  Wire.beginTransmission(ADDR_ADC121);        // transmit to device
  Wire.write(REG_ADDR_CONFIG);                // Configuration Register
  Wire.write(0x20);
  Wire.endTransmission();  
}
 
void read_adc()     //unsigned int *data
{
 
 
    Wire.beginTransmission(ADDR_ADC121);        // transmit to device
    Wire.write(REG_ADDR_RESULT);                // get result
    Wire.endTransmission();
 
    Wire.requestFrom(ADDR_ADC121, 2);           // request 2byte from device
    delay(1);
    if(Wire.available()<=2)
    {
      getData = (Wire.read()&0x0f)<<8;
      getData |= Wire.read();
    }
    Serial.print("getData:");
    Serial.println(getData);
    delay(5);
    Serial.print("The analog value is:");
    Serial.print(getData*V_REF*2/4096);
    Serial.println("V");
}
void setup()
{
  Serial.begin(9600);
  Wire.begin();
  init_adc();
}
 
void loop()
{  read_adc();//adcRead);
   delay(50);
}
```

在上面的代码中，我们将参考电压定义为由 I2C ADC 模块决定的 3.0V。该参考电压比由微控制器生成的参考电压更精确。您可以通过测量 **VA** 和 **GND** 之间的电压来使其更准确，并使用该值替换上述代码中的 3.00。

现在您可以上传这个代码。

然后，打开串行监视器并读取值 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/IIC_ADC_Read_Result.jpg)

<div class="admonition note">
<p class="admonition-title">Note</p>
Grove - I2C ADC 的地址是可更改的，这意味着您可以重新定义其地址。这需要在板上进行一些硬件修改。如果您正在考虑同时使用多个 I2C ADC，请按照以下参考部分中的说明进行操作。可以同时使用的I2C ADC 的最大值为 9，但在 <a href="/Base_Shield_V2">Grove - Base Shield V1.2</a> 上只有 4 个 I2C 插槽，因此如果要使用超过 4 个 I2C ADC，请使用 <a href="/Grove-I2C_Hub">Grove - I2C Hub</a> 创建更多 I2C 插槽。
</div>
### 与 Beaglebone Green 一起使用

要在 BBG 开始编辑程序，可以使用 Cloud9 IDE。
作为熟悉 Cloud9 IDE 的简单练习，创建一个简单的应用程序来闪烁 BeagleBone 上的一个 LED 是一个好的开始，这 4 个 LED 是用户可编程的。

如果这是您第一次使用 Cloud9 IDE，请按照 [**这个链接**](/BeagleBone_Green) 进行操作。

**Step1 :** 将 Grove - UART 插座设置为 Grove - GPIO 插座，只需按照 [**这个链接**](http://www.seeedstudio.com/recipe/362-how-to-use-the-grove-uart-port-as-a-gpio-on-bbg.html) 操作即可。

**Step2 :** 点击右上角的 **"+"** 创建一个新文件。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/C9-create-tab.png)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/C9_newfile.jpg)

**Step3 :** 将以下代码复制并粘贴到新选项卡中。

```
from Adafruit_I2C import Adafruit_I2C
import time
 
ADDR_ADC121 = 0x50
 
REG_ADDR_RESULT = 0x00
REG_ADDR_ALERT = 0x01
REG_ADDR_CONFIG = 0x02
REG_ADDR_LIMITL = 0x03
REG_ADDR_LIMITH = 0x04
REG_ADDR_HYST = 0x05
REG_ADDR_CONVL = 0x06
REG_ADDR_CONVH = 0x07
 
i2c = Adafruit_I2C(ADDR_ADC121)           
 
class I2cAdc:
    def __init__(self):
        i2c.write8(REG_ADDR_CONFIG, 0x20)
 
    def read_adc(self):
        "Read ADC data 0-4095."
        data_list = i2c.readList(REG_ADDR_RESULT, 2)
        #print 'data list', data_list
        data = ((data_list[0] & 0x0f) << 8 | data_list[1]) & 0xfff
        return data
 
if __name__ == '__main__':
    # Connect the Grove - I2C ADC to I2C Grove port of Beaglebone Green.
    adc = I2cAdc()
    while True:
        print 'sensor value ', adc.read_adc()
        time.sleep(.2)
```

**Step4 :** 通过单击磁盘图标保存文件，并为文件提供 .py 扩展名。

**Step5 :** 将 Grove I2C ADC 连接到 BBG 上的 Grove I2C 插座。

**Step6 :** 运行代码你会发现终端每 2 秒输出一次 AD 值。

## 参考资料
---------

### I2C 地址设置

ADC I2C 具有由 ADR0 和 ADR1 决定的 7 位硬件地址。默认情况下，ADR0 和 ADR1 连接到板内的 **"L"**。 但你可以改变它。例如，使用刀切断 **"L"** 和 ADR0 之间的连接(如下图所示)，然后将 ADR0 的状态置为 Floating(无连接)。而且如果你这次焊接 ADR0 和 **"H"**，那么你的 ADR0 的值为 **"H"**。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/Change_I2C_Address.jpg)

您可以在下表中找到硬件 I2C 地址与 ADR0 和 ADR1 的值的关系。

<table border="1" cellspacing="0" width="50%">
<tr>
<th rowspan="2" scope="col">
设备地址[A6 - A0]
</th>
<th colspan="2" scope="col">
ADR0 和 ADR1 输入状态
</th>
</tr>
<tr>
<td scope="col">
ADR1
</td>
<td scope="col">
ADR0
</td>
</tr>
<tr>
<td scope="row">
1010000(0x50)
</td>
<td>
Floating
</td>
<td>
Floating
</td>
</tr>
<tr>
<td scope="row">
1010001(0x51)
</td>
<td>
Floating
</td>
<td>
L
</td>
</tr>
<tr>
<td scope="row">
1010010(0x52)
</td>
<td>
Floating
</td>
<td>
H
</td>
</tr>
<tr>
<td scope="row">
1010100(0x54)
</td>
<td>
L
</td>
<td>
Floating
</td>
</tr>
<tr>
<td scope="row">
1010101(default 0x55)
</td>
<td>
L
</td>
<td>
L
</td>
</tr>
<tr>
<td scope="row">
1010110(0x56)
</td>
<td>
L
</td>
<td>
H
</td>
</tr>
<tr>
<td scope="row">
1011000(0x58)
</td>
<td>
H
</td>
<td>
Floating
</td>
</tr>
<tr>
<td scope="row">
1011001(0x59)
</td>
<td>
H
</td>
<td>
L
</td>
</tr>
<tr>
<td scope="row">
1011010(0x5A)
</td>
<td>
H
</td>
<td>
H
</td>
</tr>
</table>

### I2C ADC 增加了多少精度？

这是一个实验，让您了解 I2C ADC 如何提高模拟传感器的精度。 首先，我们从 Grove - Gas Sensor(MQ5) 检查 Arduino/Seeeduino 上模拟端口直接收集的数值。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/Read_Gas_Sensor_data.jpg)

我们上传下面的代码以获取数据。

```
    /*
     * Grove - Gas Sensor(MQ5)  
     *
     * The Gas Sensor detect the related Gas density,
     * Arduino get the result by analogread. the gas Density is
     * 0~1, larger the output is, the denser the gas.
     * Connect the Sensor to A0 in this demo;
     *
     *  By: http://www.seeedstudio.com
    */
    #define Vref 4.95
    void setup() {
      Serial.begin(9600);
    }

    void loop() {
      float vol;
      int sensorValue = analogRead(A0);
      vol=(float)sensorValue/1023*Vref;
      Serial.print("The sensorValue is ");
      Serial.println(sensorValue);
      Serial.print("The analog value is ");
      Serial.print(vol);
      Serial.println("V");
      delay(100);
    }
```

结果如下:

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/Read_ADC_2.jpg)

默认情况下，参考电压由 Arduino 生成，理论上为 5V。但实际上这是一个会导致最终数据的偏差的浮动值。使用 Grove - I2C ADC 时可避免这种不准确，因为它提供了一个绝对的 3.0V 为参考电压。
相反，在相同的条件下，由 Grove - I2C ADC 电路采集的传感器值范围如下所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/IIC_ADC_Read_Result.jpg)

为了找出哪个结果更贴近实际情况，我们用万用表测量传感器引脚 **SIG** 和引脚 **GND** 之间的电压。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/img/Measure_the_real_sensor_value_using_DMM.JPG)

资源下载
--------

-   **[Eagle文件]** [I2C ADC Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/res/I2C_ADC_Eagle_File.zip)
-   **[芯片数据手册]** [ADC121C021 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_ADC/master/res/ADC121C021_Datasheet.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_I2C_ADC -->
