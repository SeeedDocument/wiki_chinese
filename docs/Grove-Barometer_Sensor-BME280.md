---
title: Grove - Barometer Sensor(BME280)
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Temp&Humi&Barometer-Sensor-(BME280)-p-2653.html
oldwikiname: Grove_-_Barometer_Sensor(BME280)
prodimagename: Grove-Barometer_Sensor-BMP280-700_s.jpg
wikiurl: http://seeed.wiki/Grove-Barometer_Sensor-BME280
sku: 101020193
tags: plat_duino, plat_bbg, plat_linkit -->
---

<!-- tags: io_3v3, io_5v, grove_i2c, grove_analog, grove_digital, grove_uart, plat_duino, plat_bbg, plat_pi, plat_wio, plat_linkit -->

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/img/Grove-Barometer_Sensor-BMP280-700_s.jpg)

Grove - Barometer Sensor (BME280) 是一款基于 **Bosch BMP280** 的高精度，低功耗传感器。该模块可准确，快速地测量温度，大气压力和湿度。随着大气压力随高度变化而变化，它也可以测量一个地方的近似 **高度**。它可以连接到有 **I<sup>2</sup>C** （与 Grove 插槽集成）或有 **SPI** 总线的微控制器。 我们还提供了很多开发资料，使这种产品更容易使用。

BME280 是 BMP180 的升级版，BME280 相对 BMP180 获得了显着的改进。BME280的体积更小，功耗更低，测量噪声更低，压力和温度的分辨率更高，RMS噪声更低，同时新增了 SPI 总线和更多的测量模式，提高了测量速率，增加了滤波器防止环境干扰。由于大气压力读数受高度和温度的影响，因此我们增加了补偿功能。 所以，Grove - Barometer Sensor (BME280) 提供的温度，大气压力值，湿度和近似高度等数据更加可靠。

传感器使用很简单. 对于[Seeeduino](http://www.seeedstudio.com/depot/Seeeduino-V42-p-2517.html?cPath=6_7) (与 Arduino 兼容), 只需要使用 [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) 把电路板连接到 I2C Grove 接口上.然后，使用 GitHub 上的例程和代码即可。.如果您使用 Arduino，请使用 Base Shield v2.0 或简单地将 **VCC** 引脚连接到 **5V** 电压引脚，**GND 接地**，**SCL** 至 I2C 时钟（**A5**）和 **SDA** 至 **I2C** 数据（**A4**）。

典型应用：增强 GPS 导航，户外/室内导航，天气预报或任何其他需要精确的大气压力读数的项目。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.72ae476b6pdgwH&id=534636479507)

产品特性
--------

-   获取的温度，大气压力值，湿度和近似高度数据更精确。
-   兼容 Grove 并易于使用。
-   有丰富的资料来帮助你建立项目。

!!!Tip
    更多关于 Grove 的细节请参考 [Grove 系统](http://wiki.seeed.cc/Grove_System/)

规格参数
--------------

| 参数                                     | 值                                                                                             |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| 输入电压                                 | 3.3V or 5V                                                                                        |
| I/O 口电压                                   | 3.3V or 5V                                                                                        |
| 工作电流                             | 0.4mA                                                                                             |
| 工作温度                         | -40 - 85 ℃                                                                                        |
| 大气压力传感器测量范围 | 300 - 1100 hPa (1 hPa= 100 Pa)，精度 ±1.0 hPa                                   |
| 温度传感器测量范围          | -40 - 85 ℃，精度  ±1.0°C                                                                  |
| 湿度传感器测量范围            | 0% - 100% 相对湿度，精度 ±3%                                                  |
| 测量模式                            | 压电&温度，自定义&周期性                                                          |
| 芯片                                          | BME280 ([数据手册](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/res/Grove-Barometer_Sensor-BME280-.pdf)) |
| 接口总线                                 | SPI, I<sup>2</sup>C (使用其中一个)                                                      |
| 重量                                        | 3.2 g (印刷电路板), 9.3 g 整个包装每件                                    |
| 尺寸                                    | 40 (长) × 20 (宽) mm                                                                       |

<div class="admonition note">
<p class="admonition-title">Note</p>
<ol><li>我们将尽快展示/描述如何选择接口总线。</li>
<li>高度由温度和大气压力的组合计算得到的。没有高度的专门组件。</li></ol>
</div>

### 支持平台

<div class="admonition note">
<p class="admonition-title">Note</p>
<ol><li>以上列表仅适用于使用电池的情况。</li>
<li>如果没有针对特定平台提及版本号，则表示此产品支持该平台内的所有版本。</li></ol>
</div>

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/img/Grove-Barometer_Sensor-BME280-Components_1200_s.jpg)

-   **SPI 焊盘**, 一个电压监控电路。
-   **Interface bus selection pads** ，选择 I<sup>2</sup>C 总线, 通过焊接连接两个焊盘（默认连接）; 选择 SPI 总线, 用锋利的刀或烙铁切割开两个焊盘。
-   **从板地址选择焊盘**, 选择从板地址以避免地址冲突。

    - 如果选择了 I2C 总线，则从机板的默认地址为 **0x76**（连接右侧两个焊盘）。 如果要使用地址 **0x77**，仅通过焊接连接左侧两个（断开右侧两个）。
<div class="admonition tip">
<p class="admonition-title">Tip</p>
你可以用一把锋利的刀切断焊盘间的连接。
</div>
    - 如果选择了 SPI 总线，则从机板的默认地址为 **0x76**（连接右侧两个焊盘）。如果要使用地址 **0x77**，请断开所有三个焊盘。

<div class="admonition note">
<p class="admonition-title">Note</p>
工作时，请勿触摸或摇晃让本产品发生振动。这将造成干扰，并会影响收集的数据的准确性。
</div>

### **包装清单** (主要部件)

| 部件名称                                                                                                                    | 数量 |
|-------------------------------------------------------------------------------------------------------------------------------|----------|
| Grove - Barometer Sensor (BME280)                                                                                             | 1 片  |
| [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) | 1 根  |

开始使用
---------------

现在让我们使用这个模块运行一些简单例子吧。

### 使用 Arduino

本节介绍如何使用 Arduino 平台构建一个简单的项目。即使使用不同类型的主控板，这些指令和源代码也是很有用的。

#### 准备材料

-   Grove - Barometer Sensor (BME280) × 1
-   [Seeeduino 4.2](http://www.seeedstudio.com/depot/Seeeduino-V42-p-2517.html) (与 Arduino 充分兼容) 或 Arduino UNO (其他型号的也是可以的) × 1
-   Grove - Base Shield × 1 (如果您使用 Seeeduino 就不必使用它了，因为 Seeeduino v4.2 自带两个 I2C 接口)
-   USB 电缆 (Type-A to Type-B, 用于 Arduino) × 1 或者 USB 电缆 (Type-A to Micro Type-B, 用于 Seeeduino) × 1
-   [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) × 1

#### 连接方法

把所有部件按如下所述连接：下面的第一张图展示了使用 Seeeduino 时的连接方法，第二张图展示了使用 Arduino UNO 时的连接方法：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/img/Grove-Barometer_Sensor-BME_280-Demo_1200_s.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/img/Grove-Barometer_Sensor-BME_280-Demo_Arduino_UNO_1200_s.jpg)

#### Coding Work

您可以在 [这里](https://github.com/Seeed-Studio/Grove_BME280/tree/master/example)找到更多例程和 [开发库](https://github.com/Seeed-Studio/Grove_BME280)。

1. 一个典型的示例程序. 您可以使用 [Codebender](https://codebender.cc)来上传您的代码。

    <iframe frameborder="0" height="500" src="https://codebender.cc/embed/sketch:310854" width="50%">
</iframe>

2. 下载并上传代码。如果您不知道如何上传代码，请访问： <https://www.arduino.cc/en/Guide/Windows> 适用于 Windows 或 <https://www.arduino.cc/en/Guide/MacOSX> 适用于 Mac。

<div class="admonition tip">
<p class="admonition-title">Tip</p>
如果您使用的是 Seeeduino ，请在  <span style="font-weight:bold">Tools（工具）</span> 菜单下点击 <span style="font-weight:bold">Boards（开发板）</span> 来更改为您使用的板子的型号。
</div>

资源下载
---------

-   **[Eagle 文件]**[Schematic(Eagle) file](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/res/Grove-Barometer_Sensor-BME280-v1.0_Schematics.zip)
-   **[数据手册]**[BME280 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BME280/master/res/Grove-Barometer_Sensor-BME280-.pdf)
-   **[示例代码]**[Library and example code](https://github.com/Seeed-Studio/Grove_BME280) on GitHub
-   **[[I<sup>2</sup>C 教程]**[I<sup>2</sup>C how-to for Arduino](https://www.arduino.cc/en/Reference/Wire)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Barometer_Sensor(BME280) -->
