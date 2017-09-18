---
title: Grove - Barometer Sensor (BMP280)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Barometer-Sensor-(BMP280)-p-2652.html
oldwikiname: Grove_-_Barometer_Sensor_(BMP280)
prodimagename: Grove-Barometer_Sensor-BMP280-700_s.jpg
bzprodimageurl: http://statics3.seeedstudio.com/seeed/img/2016-06/oVNA7LQwPYYFnB674KEPM9w7.jpg
surveyurl: https://www.research.net/r/Grove-Barometer_Sensor-BMP280
sku: 101020192
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/img/Grove-Barometer_Sensor-BMP280-700_s.jpg)


**Grove - 气压计传感器（BMP280）** 是Bosch BMP280高精度和低功耗数字气压计的接线板。 该模块可用于精确测量 **温度** 和 **大气压力**。 随着大气压力随高度变化，它也可以测量一个地方的近似 **高度** 。 它可以连接到具有I2C（与Grove插槽集成）或通过SPI总线的微控制器。 我们还提供了高度抽象的库，使此产品更易于使用。

BMP280是BMP180的升级版。 BMP280比起BMP180有着了显着的改进。 BMP280体积更小，功耗更低，噪声测量更低，压力和温度更高的分辨率，更低的RMS噪声，新增的接口SPI，更多的测量模式，更高的测量速率和新增的滤波器，防止环境干扰。 由于大气压力读数受高度和温度的影响，我们在库中增加了补偿功能。 因此，Grove - 气压计传感器（BMP280）在提供精确的温度，大气压力值和近似高度数据方面将更加可靠。

这个传感器易于使用。 对于[Seeeduino](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)（兼容Arduino），只需使用[Grove cable](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11LDDtt2&id=546720638006) 到I2C Grove连接器。 然后，使用GitHub提供的库和示例代码。 如果您使用Arduino，请使用Base Shield v2.0或简单地将VCC引脚连接到5V电压引脚，GND接地，SCL至I2C时钟（模拟5）和SDA至I2C数据（模拟4）。


典型应用：增强GPS导航，户外/室内导航，天气预报或任何其他需要精确大气压力读数的项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11uVPPUa&id=534767716742)

产品特性
--------


- 获取更精确的温度，大气压力值和近似的高度数据。
- 能够兼容Grove并且易于使用
- 抽象的库，能够更快地建设项目


!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

参数规格
--------------

| 参数                        | 规格                                                                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 输入电压                      | 3.3V or 5V                                                                                                                  |
| I/O 口电压                        | 3.3V or 5V                                                                                                                  |
| 工作电流                   | 0.6mA                                                                                                                       |
| 工作温度              | -40 - 85 ℃                                                                                                                  |
| 有效压力测量范围 | 300〜1100 hPa（1 hPa = 100 Pa），精度为±1.0 hPa                            |
| 温度测量精度    | ±1.0°C                                                                                                                      |
| 测量模式                    | Piezo和 Temperature, forced 或 periodic   |
|芯片                             | BMP280 ([datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/res/Grove-Barometer_Sensor-BMP280-BMP280-DS001-12_Datasheet.pdf)) |
|采样频率              | 182 Hz（一般）       |
|接口总线                      |SPI，I2C（使用其中之一）                                                     |
|质量                        | 3克（接线板）                                                              |
| 外形尺寸                     | 40（长）×20（宽） mm                                                                                                  |

<div class="admonition note">
<p class="admonition-title">Notes</p>
<p> 1. 我们将尽快展示/描述如何选择接口总线。</p>
<p> 2. 高度由温度和大气压力的综合计算得到。 因为没有测量高度的专门组件。</p>
</div>



硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/img/Grove-Barometer_Sensor-BMP280-Components_1200_s.jpg)


- **SPI soldering pads**，电压监控电路。
- **Interface bus selection pads**，选择I2C总线，通过焊接连接两个焊盘（默认情况下连接）; 选择SPI总线，用锋利的刀或烙铁切割两个焊盘。
- **Slave board address selection pads**，选择Slave board 地址以避免地址冲突。


**Tips:** 您可以用锋利的刀切除不要的焊点。

如果选择了SPI总线，则slave board的默认地址为 **0x77**（右连接两个焊盘）。 如果要使用地址 **0x76**，请断开所有三个的焊盘。

<div class="admonition note">
<p class="admonition-title">Note</p>
工作时，请勿触摸或摇晃或让本产品发生振动。 这将造成干扰，并会影响收集的数据的准确性。
</div>

### **产品清单** (主要部分)

| 项目                                                                                                          | 数量 |
|-------------------------------------------------------------------------------------------------------------------------------|----------|
| Grove - Barometer Sensor (BMP280)                                                                                             | 1 片  |
| [Grove cable](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11tpUgf8&id=546720638006) | 1 根 |

入门指导
---------------

现在让我们运用这个模块的一些基本示例。

### 使用 Arduino

本节介绍如何使用Arduino平台构建一个简单的项目。 即使使用不同类型的主控板，这些指令和源代码也是有用的。

#### 所需材料

-   Grove - Barometer Sensor (BMP280) × 1
-   [Seeeduino 4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)（完全兼容Arduino）或Arduino UNO ×1（其他型号也很好）
-   [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) × 1 （如果您使用Seeeduino在Seeeduino v4.2上有两个I2C插座，则是可选的）
-   USB电缆（A型至B型，适用于Arduino）×1或USB电缆（Type-A至Micro Type-B，Seeeduino）×1
-   [Grove cable](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11xSC2Vg&id=546720638006) × 1

#### 硬件连接

如下连接所有部分：第一张图片显示与Seeeduino的连接，第二张图显示与Arduino UNO的连接：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/img/Grove-Barometer_Sensor-BMP280-Demo_Seeeduino_1200_s.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/img/Grove-Barometer_Sensor-BMP280-Demo_Arduino_UNO.jpg)

#### 编码

示例程序请点击 [这里](https://github.com/Seeed-Studio/Grove_BMP280/tree/master/example/bmp280_example) ，需要的库请点击  [这里](https://github.com/Seeed-Studio/Grove_BMP280)

1. 使用典型的示例代码。 您可以使用 [Codebender](https://codebender.cc)将代码上传到主控板。

    <iframe frameborder="0" height="500" src="https://codebender.cc/embed/sketch:305323" width="50%">
</iframe>

2.上传程序到你的Arduino ，如果您是第一次安装Arduino库文件，请点击 [这里](http://seeed.wiki/How_to_install_Arduino_Library/) 查看库文件的安装方法。如果您不清楚怎么下载代码到您的板子里，请点击 [这里](http://seeed.wiki/Upload_Code/)。

**Tips:** 如果您使用Seeeduino，请在上传工程时选择 **Tool(工具)** 下的 **Board(开发板)**。

资源下载
---------

-   [Schematic(Eagle) file](https://github.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/raw/master/res/Grove%20-%20Barometer%20Sensor_BMP280_Schematic.zip)
-   [BMP280 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/res/Grove-Barometer_Sensor-BMP280-BMP280-DS001-12_Datasheet.pdf)
-   [Library and example code](https://github.com/Seeed-Studio/Grove_BMP280) on GitHub
-   [I<sup>2</sup>C how-to for Arduino](https://www.arduino.cc/en/Reference/Wire)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Barometer_Sensor_(BMP280) -->
