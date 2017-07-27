## 简介
Grove-Multichannel Gas Sensor是一个建立在MiCS-6814上的环境检测传感器，可以检测多种有害气体，由于其多通道特性，可以同时检测三种不同气体。因此，当环境内不止一种气体时，该传感器可以用于监测气体浓度。

这个传感器属于Grove system，你可以把它插到Base shield上，在不需要任何跳线的条件下，直接与Arduino组合使用。其接口为I2C，所以只需要将它连接到管座屏蔽的I2C接口，就可以开始使用。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/multi_gas/1.png)
 
## 使用前

### 相关阅读
我们极力推荐您在使用气味传感器之前，先阅读如下参考资料。这将帮助您了解更多关于Arduino和我们产品的相关知识。而且会使您在使用开源硬件时更得心应手。

* Getting Started with Arduino 
* What is Grove system 
* Why i need a Base shield

在阅读后，你将掌握如何在Base shield上将Grove产品与Arduino联合工作。那让我们开始吧！

### 充分准备

该教程将包含几个必须的产品：

* Arduino UNO R3 或 Seeeduino v4 
* Base Shield 
* Grove - 多通道气体传感器 

### 硬件综述

|管脚|描述|
|----|----|
|GND	|连接地|
|VCC	|供电电压：3.3V-5V|
|SDA	|I2C数据|
|SCL	|I2C时钟|

!!! tip "供电"
    该传感器的供电电压介于3.3V和5V之间，于是可与一个输出电压为3.3V的单片微控制器相兼容。


## 产品特性

* 三个完全独立的传感元件
* 用ATmega168PA建造
* I2C的可编程接口地址
* 可以通过关闭加热功耗降低功率
* 可检测的气体种类
* 一氧化碳 CO 1-1000ppm
* 二氧化氮 NO2 0.05-10ppm
* 乙醇 C2H6OH 10-500ppm
* 氢 H2 1-1000ppm
* 氨 NH3 1-500ppm
* 甲烷 CH4 >1000ppm
* 丙烷 C3H8 >1000ppm
* 异丁烷 C4H10 >1000ppm

## 方框图

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/multi_gas/4.jpg)
 
 
## 电气特性

|项目|状态|最小值|特征值|最大值|单位|
|----|----|------|------|------|----|
|电压|	- |3.1	 |3.3	 |5.25 |V   |
|波纹|最大供电	|-|	80	|100|	mV|
|发热功率	|-	|-	|-	|88	|mV|
|最大功率	|-	|-	|-	|150|	mV|
|ADC精度	|-	|-	|10	|-	|Bits|
|I2C速度|	-	|-|	100	|400|	kHz|
|VIL	|@I2C	|-0.5	|-	|0.99|	V|
|VIH	|@I2C	|2.31	|-	|5.25|	V|


RED传感器性能

|RED传感器特性|	符号|特征值|最小值|最大值|单位|
|-------------|-----|------|------|------|----|
|空气中阻值|	R0	|-	|100|	1500	|kΩ|
|典型的CO探测范围	|FS	|-	|1	|1000	|ppm|
|灵敏系数|	SR	|-	|1.2|	50|	-|

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/multi_gas/5.jpg)
 

NH3传感器性能

|NH3传感器特性|符号 |特征值|最小值|最大值|单位|
|-------------|-----|------|------|------|----|
|空气中阻值|R0|-|10	|1500|kΩ|
|典型的NH3探测范围|FS|-|1|300|ppm|
|灵敏系数|SR|-|1.5|15|-|

 
## 固件与库

### 固件

该Grove模块有以庞大固件库为支撑的ATMega168微处理器构成。这些固件可以完成以下功能：

1. 控制加热电路和指示LED灯电路的供电开关。
2. 根据命令做校正。校正时将把传感器的MEMS内核电阻作为参考样本值，所以请在一个空旷的环境运行校正。
3. 根据命令获得三个传感器内核的其中一个电阻值，以此计算环境中某个气体的浓度值。
4. 根据命令改变模块的I2C地址。在绝大多数情况下都不用更改模块（0x04）的I2C地址，除非有子模块与之冲突。

!!! warning "注意"
    标定是在模块离开工厂前就已经完成。如果希望重新标定，请保证环境空气的流通的。

### 驱动库

该库从模型中读取电阻值并计算气体的浓度。有一件必须注意的事是，从传感器读取的数据不能直接用来判断气体的类型，但当气体的类型确定以后可以用来计算气体的浓度。
该传感器对CO、HO2和NH3特别敏感，而对其他气体测量的精确度会降低很多。
注意：doCalibrate()函数需要耗费8s才能返回结果，正如上文提到的，在大多数情况下都不需要重新校正传感器。

## 示例

### 硬件安装
将Grove-多通道气体传感器连接到Seeeduino

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/multi_gas/6.jpg)
 
### 上传代码

1. 下载Arduino Library & Grove/Xadow firmware并将其安装到Arduino库中。
2. 直接打开代码路径：文件->示例->通道气体传感器->ReadSensorValue_Grove

ReadSensorValue_Grove的内容可以参考如下：

```arduino
/*
    This is a demo to test MutichannelGasSensor library
    This code is running on Xadow-mainboard, 
    and the I2C slave is Xadow-MutichannelGasSensor
    There is a ATmega168PA on Xadow-MutichannelGasSensor, 
    it get sensors output and feed back to master.
    the data is raw ADC value, algorithm should be realized on master.
    
    please feel free to write email to me if there is any question 
    
    Jacky Zhang, Embedded Software Engineer
    qi.zhang@seeed.cc
    17,mar,2015
*/

#include <Wire.h>
#include "MutichannelGasSensor.h"

void setup()
{
    Serial.begin(9600);  // start serial for output
    Serial.println("power on!");

    //the default I2C address of the slave is 0x04
    mutichannelGasSensor.begin(0x04);
    //mutichannelGasSensor.changeI2cAddr(0x10);
    //mutichannelGasSensor.doCalibrate();
    //delay(8000);
    while(mutichannelGasSensor.readR0() < 0)
    {
        Serial.println("sensors init error!!");
        delay(1000);
    }
    Serial.print("Res0[0]: ");
    Serial.println(mutichannelGasSensor.res0[0]);
    Serial.print("Res0[1]: ");
    Serial.println(mutichannelGasSensor.res0[1]);
    Serial.print("Res0[2]: ");
    Serial.println(mutichannelGasSensor.res0[2]);
    mutichannelGasSensor.powerOn();
}

void loop()
{
    mutichannelGasSensor.readR();
    Serial.print("Res[0]: ");
    Serial.println(mutichannelGasSensor.res[0]);
    Serial.print("Res[1]: ");
    Serial.println(mutichannelGasSensor.res[1]);
    Serial.print("Res[2]: ");
    Serial.println(mutichannelGasSensor.res[2]);
    
    mutichannelGasSensor.calcGas();
    Serial.print("NH3: ");
    Serial.print(mutichannelGasSensor.density_nh3);
    Serial.println("ppm");
    Serial.print("CO: ");
    Serial.print(mutichannelGasSensor.density_co);
    Serial.println("ppm");
    Serial.print("NO2: ");
    Serial.print(mutichannelGasSensor.density_no2);
    Serial.println("ppm");
    
    delay(1000);
    Serial.println("...");
}
```

###上传代码

记得在Arduino环境的Tools|Board 目录下选择Seeeduino Uno，并选择合适的Arduino串行端口。通过打开串口监测器，你可以看到从传感器读取到的原始数据。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/multi_gas/7.jpg)

## 资源

* [Grove - Multichannel Gas Sensor v1.0 sch](http://www.seeedstudio.com/wiki/images/4/41/Grove_-_Multichannel_Gas_Sensor_v1.0_sch.pdf)
* [Grove - Multichannel Gas Sensor eagle files](http://www.seeedstudio.com/wiki/images/2/21/Grove_-_Multichannel_Gas_Sensor_v1.0_eagle_files.zip)
* [Arduino Library & Grove/Xadow firmware](https://github.com/Seeed-Studio/Mutichannel_Gas_Sensor)
* [MiCS-6814 Datasheet](http://www.seeedstudio.com/wiki/images/1/10/MiCS-6814_Datasheet.pdf)


