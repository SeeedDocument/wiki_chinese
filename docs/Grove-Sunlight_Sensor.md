---
title: Grove - Sunlight Sensor
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Sunlight-Sensor-p-2530.html
oldwikiname: Grove - Sunlight Sensor
prodimagename: Grove_sunlight_sensor_view.jpg
wikiurl: http://wiki.seeedstudio.com/cn/grove_sunlight_sensor
sku: 101020089
---

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Grove_sunlight_sensor_view.jpg)

Grove - Sunlight Sensor 是一种多通道数字光线传感器，具有检测紫外光，可见光和红外光的能力。

该器件基于 SI1145，SiLabs 的最新传感器。Si1145 是一种低功耗，集成了反射率，红外接近，紫外线指数和环境光传感器检测功能的传感器，它具有 I2C 数字接口和可编程事件中断输出。该设备在宽动态范围和各种光源(包括直射阳光)的环境下表现出卓越的性能。

Grove - Sunlight Sensor 有一个板载 Grove 接头，它可以使您轻松连接到您的 Arduino。您可以使用此设备进行一些需要检测光线的项目，例如简单的紫外线检测器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.781a69a1cLUniH&id=531838337992)

## 产品特性
---
- 数字光线传感器
- 广谱检测范围提高准确性。
- 可编程配置
- 直接检测阳光
- Grove 接口
- I2C 接口(7 位)

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
---
|||
|---|---|
|工作电压	|3.0-5.5V|
|工作电流	|3.5mA|
|波长	|280-950nm|
|I2C 缺省地址|	0x60|
|工作温度|	-45-85℃|

## 硬件概述
---
![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Hardware_overview.jpg)

- Grove 接口 - 包括 VCC，GND，SDA 和 SCL 四个引脚的接口
- LED - LED 驱动引脚
- INT - 一个可编程中断输出
- SI1145 - IC

## 入门指导
---
在本节中，您可以通过几个步骤使 Grove - Sunlight Sensor 运行。

**准备工作**

现在我们做一个简单的演示来从 Grove - Sunlight Sensor 获取数据

需要以下模块 :

- [Seeeduino v4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.134c757H42Hz2&id=45721222112)

Seeeduino V4.2 与 Arduino 完全兼容。

如果这是您第一次接触 Arduino，请点击 [这里](http://wiki.seeedstudio.com/wiki/Getting_Started_with_Seeeduino) 开始您的 Arduino 之旅。

**硬件连接**

将 Grove - Sunlight Sensor 连接到 [Seeeduino v4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.134c757H42Hz2&id=45721222112) 的 I2C 接口


如图所示 :

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Grove_sunlight_hardware_connect.jpg)

!!!Note
    如果您需要在主控板上连接更多的模块，您可能需要一个 [Grove - base shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.23f567c4zWJVXH&id=520233320144)，这将使您的工作变得轻松。

**下载**

点击 [这里](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/res/Grove_Sunlight_Sensor-master.zip) 下载库文件并将其解压缩到 Arduino 的库文件夹。

库名称末尾有 "-master" ，只需将其删除即可。

打开 Arduino IDE 然后点击 **File(文件)>Examples(示例)>Grove_Sunlight_Sensor>SI1145DEMO** 打开示例代码。

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Grove_sunlight_sensor_arduino.jpg)

点击 **Tools（工具）> Board（开发板）** 选择 Arduino UNO 并选择对应的端口。

现在点击 Upload(CTRL+U) 上传代码。如果有任何错误提示请参考 [这里](http://wiki.seeedstudio.com/wiki/Arduino_Common_Error)，您也可以在 [社区](http://www.seeed.cc) 讨论。

**评估结果**

上传成功后，打开 Arduino IDE 的串口监视器，您将得到以下数据 :

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Grove_sunlight_sensor_arduino_result.jpg)

!!!Note
    Vis - 可见光，单位为 lm；
    IR  - 红外线，单位为 lm；
    UV  - 紫外线系数

现在把 Grove - Sunlight Sensor 放在阳光下，看看今天天气怎样。


## 参考资料

**光谱**

本章内容来源于 [**Wikipedia - Spectrum**](https://en.wikipedia.org/wiki/Spectrum)，点击查看原网页。

谱(多个谱或谱)是不限于特定的一组值的条件，但可以在连续谱内无限变化。这个词首先在光学领域被科学地用来描述当用棱镜分离时可见光中的彩虹。随着对光的科学理解的提高，它适用于整个电磁频谱。

频谱已经被类比地应用于光学之外的主题。因此，人们可以谈论政治观点的范围，或药物的活动范围或自闭症谱。 在这些用途中，谱图中的值可能与精确量化的数字或定义无关。这种使用意味着广泛的条件或行为聚集在一起，并在一个标题下研究，便于讨论。

在大多数现代频谱使用情况下，在任何一端都有一个统一的主题。一些老字号的用法没有一个统一的主题，但通过下面列出的一系列事件导致了现代的主题。数学的现代用法确实从一个统一的主题演变而来，但这可能很难认识到。

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/Grove_sunlight_spectrum.jpg)

**流明**

本章内容来源于 [**Wikipedia - Lumen (unit)**](https://en.wikipedia.org/wiki/Lumen_(unit))，点击查看原网页。

流明(符号：lm)是 SI 衍生的光通量单位，是光源发出的可见光总量的量度。光通量不同于功率(辐射通量)，因为光通量测量反映了人眼对不同波长的光的不同灵敏度，而辐射通量测量指示所发射的所有电磁波的总功率，而与眼睛的感知能力无关。流明与勒克斯有关，一勒克斯是每平方米一流明。

**比如 : **

- 黑夜: 0.001—0.02
- 月夜: 0.02—0.3
- 阴天室内: 5—50
- 阴天室外: 50—500
- 晴天室内: 100—1000
- 适合阅读: 500—600
- 家用摄像机: 1400


**紫外线指数**

本章内容来源于 [**Wikipedia - Ultraviolet index**](https://en.wikipedia.org/wiki/Ultraviolet_index)，点击查看原网页。

紫外线指数或紫外线指数是在特定地点和时间对产生紫外线的紫外线 (UV) 辐射强度的国际标准测量值。该标准是 1992 年由加拿大科学家提出的，1994 年由联合国世界卫生组织和世界气象组织通过和标准化。它主要用于针对大众的日常预报，并且也以小时预报。

紫外线指数被设计成一种开放式的线性比例尺，与引起人体皮肤晒伤的紫外线辐射强度成正比。例如，如果一个皮肤浅的人(没有防晒霜或晒黑)在紫外线指数为 6 的情况下在 30 分钟内开始晒伤，那么在紫外线指数为 12 的情况下，这个人应该在 15 分钟内晒伤 - 也就是紫外线指数翻倍，辐射强度翻倍。

紫外线指数的目的是帮助人们有效地保护自己免受紫外线辐射的伤害，紫外线辐射对健康有益，但过度导致晒伤，皮肤老化，DNA 损伤，皮肤癌，免疫抑制和眼部损伤，如白内障(见 *Human health-related effects of ultraviolet radiation* 一节）。公共卫生机构建议，如果在紫外线指数为 3 或更高的时候在户外度过相当长的时间，人们应该自我保护(例如，通过在皮肤上涂抹防晒霜并戴上帽子和墨镜)，请参阅下表以获取更详细的建议。

当一天预测的紫外线指数在不同数值范围内时，保护建议如下 :

![](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/img/uv%20index.png)

**警告**

在解释紫外线指数和建议时，请注意 :

- 地球表面的紫外线辐射强度取决于太阳在天空中的角度。太阳每天在正午达到最高角(强度最高，阴影最短)，大约相当于时钟的12:00。因为在特定的时区太阳时间和当地时间存在差异。一般来说，当太阳直射到人的阴影比他们的身高短时，紫外线晒伤的风险就很高。
- 同样，对于与水平线成不同角度的表面，紫外线强度可以更高或更低。例如，如果人们在户外行走或站立，那么当太阳较低时，例如夏天的傍晚或冬天的下午的一条滑雪道上，紫外线照射到眼睛和皮肤的垂直表面，例如脸部，实际上可能更严重。这部分是由于指数所基于的测量设备是平坦的水平表面这一事实的结果。紫外线强度几乎可以通过雪或其他光亮表面(如水，沙或混凝土)的反射来加倍。
- 给出的建议是针对一般皮肤浅褐色的成年人的。那些皮肤较深的人更有可能经受更大的阳光照射，而对于儿童，老年人，特别是皮肤白皙的成年人以及那些由于医学原因或在过去几天的紫外线照射下具有较高的日光敏感度的人，需要额外的预防措施。(皮肤从紫外线辐射中恢复的过程通常需要两天或更长的时间才能完成)
- 计算紫外线指数的方式，在技术上表现出主要由 UVB 辐射引起的晒伤。但是，UVA 辐射也会造成损伤(光老化，黑素瘤)。在某些情况下，包括大多数照晒棕褐色皮肤的浴床
，UVA 水平可能不成比 UV 指数所描述的更高。广谱 (UVA/UVB) 防晒霜的使用可以帮助解决这个问题。


## 资源下载
---
- **[Eagle 文件]** [Schematic in Eagle File](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/res/Grove_-_Sunlight_Sensor_v1.0_SCH%26PCB%26PDF.zip)
- **[原理图 PDF]** [Schematic in PDF](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/res/Grove_-_Sunlight_Sensor_v1.0.pdf)
- **[库文件]** [Github Repositoriy for Grove - Sunlight Sensor](https://github.com/Seeed-Studio/Grove_Sunlight_Sensor)
- **[芯片数据手册]** [Si1145 datasheet](https://github.com/SeeedDocument/Grove-Sunlight_Sensor/raw/master/res/Si1145-46-47.pdf)
- **[其他资源]** [Spectrum](https://en.wikipedia.org/wiki/Spectrum)
- **[其他资源]** [Lumen (unit)](https://en.wikipedia.org/wiki/Lumen_(unit))
- **[其他资源]** [Ultraviolet index](https://en.wikipedia.org/wiki/Ultraviolet_index)
