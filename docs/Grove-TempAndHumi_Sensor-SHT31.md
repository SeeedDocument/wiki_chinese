---
name: Grove - Temp&Humi Sensor(SHT31)
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Temperature&Humidity-Sensor-(SHT31)-p-2655.html
oldwikiname: Grove_-_Temp&Humi_Sensor(SHT31)
prodimagename: Grove-TempAndHumi_Sensor-SHT31-Product_View_700_S.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-TempAndHumi_Sensor-SHT31
sku: 101020212
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/img/Grove-TempAndHumi_Sensor-SHT31-Product_View_700_S.jpg)

Grove - Temp&Humi Sensor(SHT31) 是一款高度可靠，准确，能够快速响应和非常集成的温湿度传感器。 该模块中使用的传感器（芯片）采用 Sensirion 的 CMOSens < sup >®</ sup>  技术设计。 该芯片经过良好校准，线性化和补偿数字输出。

该模块的标准精度可以是 **±2％RH** （相对湿度）和 **±0.3°C** （对于温度）。 该模块兼容 3.3 V 和 5 V，因此不需要电压电平转换器。 该模块能与  I < sup > 2 </ sup> C  串行总线进行通信，并且可以工作高达 1 MHz 的速度。 我们还提供了一个高度精炼的库，使这个产品更容易使用。

使用这种传感器很容易。 对于 [Seeeduino](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112) （符合Arduino），只需将此分支板与主控板通过 [Grove cable](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.660b1b44FmOXo6&id=546720638006)。 然后使用 GitHub 提供的库和示例/演示代码来获取您的数据。 如果您使用的是没有 Base Shield 的 Arduino ，只需将 VIN 引脚连接到 5V 电压引脚， GND 接地， SCL 至 I2C 时钟（模拟5）和 SDA 至 I2C 数据（模拟4）。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.7421ab95L67vUC&id=534770660296)

产品特性
--------

- 高度可靠，准确快速的响应时间
- Grove 兼容且易于使用
- 良好校准，线性化，补偿数字输出
- 高度精炼的开发库

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

规格参数
--------------

| 参数               | 范围                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------|
| 输入电压（VCC）     | 3.3 V 或 5 V                                                                                      |
|  I / O 逻辑电平      | 基于VCC的 3.3 V 或 5 V                                                                            |
| 工作电流       | 100 μA                                                                                                       |
| 工作温度    | -40–125 ℃                                                                                                                                                                                                                                                                         |
| 温度传感器范围 | -40–125 ℃, 有 ±0.3°C 的精度                                                                              |
| 湿度传感器范围   | 0% - 100%(相对湿度), 有 ±2% 的精度                                                              |
|传感器芯片             | SHT31([Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/res/Grove-TempAndHumi_Sensor-SHT31-Datasheets.zip)) |
| 接口总线          | I<sup>2</sup>C                                                                                               |
| 重量                  | 4 g (for breakout board), 9 g for whole package each piece                                                   |
| 外形尺寸               | 40 (长)× 20 (宽) mm                                                                                      |

支持平台
-------------------

<table>
<tr>
<td>
平台
</td>
<td>
Seeeduino/Arduino
</td>
<td>
Raspberry Pi
</td>
<td>
Beaglebone
</td>
<td>
LinkIt ONE
</td>
</tr>
<tr>
<td>
支持状态
</td>
<td>
支持
</td>
<td>
不支持
</td>
<td>
支持
</td>
<td>
支持
</td>
</tr>
<tr>
<td>
注意
</td>
<td colspan="5">
如果相应平台没有提到版本号，则表示该产品支持该平台内的所有版本。
</td>
</tr>
</table>

硬件概述
-----------------

应用 Grove 接口该模块将非常容易被使用。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/img/Grove-TempAndHumi_Sensor-SHT31-components_1200_s.jpg)
<div class="admonition caution">
<p class="admonition-title">警告</p>
使用时请勿触摸，摇晃或让本产品振动。 否则会影响测量数据的准确性。
</div>


### **套装包括**(主要部分)

| 名称                                                                                                                   | 数量 |
|-------------------------------------------------------------------------------------------------------------------------------|----------|
| Grove - Temp&Humi Sensor(SHT31)                                                                                               | 1 片  |
| [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) | 1 片  |

入门
---------------

现在让我们运用这个模块使用所提供的库/示例的一些基本的例子。

### 使用 Arduino

本节介绍如何使用Arduino平台构建一个简单的项目。 即使使用不同类型的主控板，这些说明和源代码可能仍然有帮助。

#### 需要的素材

-   Grove - Temp&Humi Sensor(SHT31) × 1
-   [Seeeduino 4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112) （与 Arduino 完全兼容）或 Arduino UNO （其他型号也很好）×1
- Grove - Base Shield ×1（这是可选的，如果您使用 Seeeduino ，因为 Seeeduino  v4.2上有两个 I2C 插座）
- USB 数据线（A型至B型，适用于 Arduino ）×1 或 USB 数据线（ Type-A 至 Micro Type-B，Seeeduino） ×1
-   [Grove cable](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.660b1b44FmOXo6&id=546720638006) × 1

#### 连接

如果您使用 Seeeduino ，请将 Grove 模块连接到 **I2C** 端口，如：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/img/Grove-TempAndHumi_Sensor-SHT31-wiki_demo_on_seeeduino1200_s.jpg)

如果您使用 Arduino UNO 或其他兼容机型，请先加入 Grove - Base Shield V2 。 然后，将 Grove 模块连接到 I2C 端口，如：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/img/Grove-TempAndHumi_Sensor-SHT31-wiki_demo_on_arduino1200_s.jpg)


#### 编码工作

你可以找到演示代码 [这里](https://github.com/Seeed-Studio/Grove_SHT31_Temp_Humi_Sensor/blob/master/example) 和开发库 [这里](https://github.com/Seeed-Studio/Grove_SHT31_Temp_Humi_Sensor).

1. 典型的演示代码。 您可以使用 [Codebender](https://codebender.cc) 将代码上传到主控板。
    <iframe frameborder="0" height="500" src="https://codebender.cc/embed/sketch:318318" width="50%">
</iframe>

2. 下载并上传代码。 如果您不知道如何上传 Arduino 数据，请访问 Windows 用户的<https://www.arduino.cc/en/Guide/Windows>或为 Mac 用户提供的<https://www.arduino.cc/en/Guide/MacOSX>。 您可以看到以下结果。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/img/Grove-TempAndHumi_Sensor-SHT31-Wiki_Demo_Result_600_S.jpg)

<div class="admonition tip">
<p class="admonition-title">小提示</p>
如果您使用 Seeeduino ，当你上传数据时，请选择 <span style="font-weight:bold">Boards</span> under <span style="font-weight:bold">Tools</span>
</div>

资源下载
---------

-   [EAGLE schematics, PCB files and PDF schematic](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/res/Grove-TempAndHumi_Sensor-SHT31-v1.0_Schematics.zip)
-   [SHT31 Sensor Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-TempAndHumi_Sensor-SHT31/master/res/Grove-TempAndHumi_Sensor-SHT31-Datasheets.zip)
-   [Library and example code](https://github.com/Seeed-Studio/Grove_SHT31_Temp_Humi_Sensor) on GitHub
-   [I<sup>2</sup>C How-to for Arduino](https://www.arduino.cc/en/Reference/Wire)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Temp&Humi_Sensor(SHT31) -->
