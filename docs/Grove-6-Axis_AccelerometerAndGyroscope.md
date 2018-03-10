---
title: Grove - 6-Axis Accelerometer&Gyroscope
category: Sensor
bzurl: https://seeedstudio.com/Grove-6-Axis-Accelerometer&Gyroscope-p-2606.html
oldwikiname: Grove_-_6-Axis_Accelerometer&Gyroscope
prodimagename: Grove-6-Axis_AccelerometerAndGyroscope_product_view_1200_s.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-6-Axis_AccelerometerAndGyroscope
sku: 105020012
tags: plat_duino, plat_pi, plat_bbg, plat_linkit -->
---

<!-- tags: io_3v3, io_5v, grove_i2c, grove_analog, grove_digital, grove_uart, plat_duino, plat_bbg, plat_pi, plat_wio, plat_linkit -->

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/img/Grove-6-Axis_AccelerometerAndGyroscope_product_view_1200_s.jpg)

Grove - 6-Axis Accelerometer&Gyroscope 是一种把 Grove 接口和集成传感器组合的传感器，同时它也包含 3 轴数字加速度计和 3 轴数字陀螺仪。


它具有极低功耗数字芯片 LSM6DS3 ([datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/res/LSM6DS3TR.pdf)) 和内置电源调节器，以及很高灵敏度高，绿色科技和低噪音干扰。 它可以用于制作需要不同灵敏度加速度计和设定不同角速度测量范围的项目。如果提供详细的 SDK ，它可以使制作开发过程更快捷。

该产品可用于倾斜，运动和水龙头感应等不同应用，如机器人，IoT 设备和消费电子设备。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.403b31cctuXbqP&id=531757615410)

产品特性
--------

- Grove 接口和高经济性。
- 6 DOF 运动数据的数字输出。
- ±2 /±4 /±8 /±16 g 全尺寸精简加速度感应范围，适用于各种环境。
- ±125，±245，±500，±1000，±2000度/秒（dps），用于角速率测量范围使其具有通用性。
- 详细的 SDK ，便于编程。
- 可靠数据采集调节电源。
- 针对不同事件的编程中断。
- 8 kB 数据缓冲。

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

创新应用
-----------------

-   机器人
-   商用型飞机
-   电脑输入设备
-   可穿戴设备。
-   物联网

规格参数
--------------


有关详细信息，请参阅[数据表](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/res/LSM6DS3TR.pdf).。

| 参数                            | 范围                                                                               |
|---------------------------------------|--------------------------------------------------------------------------------------|
| 模拟电源电压：                | 5V/3.3V(DC)                                                                          |
| 能量消耗：                    | 组合正常模式下为 0.9 mA ， 1.6 kHz 的组合高性能模式为 1.25 mA |
| 线性加速度测量范围 |  ±2 /±4 /±8 /±16g 满量程（标准值）                                           |
| 角速率测量范围        | ±125, ±245, ±500, ±1000, ±2000 dps(标准值 )                                    |
| 线性加速灵敏度       | 0.061(FS = ±2), 0.122(FS = ±4), 0.244(FS = ±8), 0.488(FS = ±16) mg/LSB               |
| 角速率灵敏度              | 4.375(FS = ±125), 8.75(FS = ±245), 17.50(FS = ±500), 35(FS = ±1000), 70(FS = ±2000)  |

### Platforms Supported

<div class="admonition note">
<p class="admonition-title">注意</p>
如果没有特定平台代表版本号，则表示该产品支持该平台内的所有版本。 但是您将需要其他相应的 Grove 版块，例如 Grove - Base Shield v2 。
</div>

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/img/Grove-6-Axis_AccelerometerAndGyroscope_components_view_1200_s.jpg)

**Grove 部件**   
连接主控板如 Seeeduino 板与驱动板。

**LSM6DS3**   
Main MCU

### **部件列表**

| 部件名称                            | 数量 |
|----------------------------------------|----------|
| Grove - 6-Axis Accelerometer&Gyroscope | 1PC      |
| Grove 线                             | 1PC      |

入门
-----------

### **材料准备**

-   Seeeduino * 1

-   Grove - Base Shield v2

### **准备工作**

请参阅以下指南来构建适当的 IDE ：

<div class="admonition note">
<p class="admonition-title">注意</p>
在这种情况下，我们选择了 Seeeduino ，它与 Arduino 兼容。 您也可以使用 Arduino板。
</div>

[Windows入门](/Seeeduino_v4.2#Getting_Started_on_Windows)

[ Mac OS X 入门](/Seeeduino_v4.2#Getting_Started_on_Mac_OS_X)

### **硬件连接**

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/img/Grove-6-Axis_AccelerometerAndGyroscope_demo_connection_1200_s.jpg)

<div class="admonition note">
<p class="admonition-title">note</p>
将 Grove - 6-Axis Accelerometer&Gyroscope 连接到 Grove - Base shield 上的 **I<sup>2</sup>C** 接口。 并用 USB 数据线连接到电源。
</div>

### **简单演示**

下载 Grove - 6-Axis Accelerometer&Gyroscope 的 [程序库](https://github.com/Seeed-Studio/Accelerometer_And_Gyroscope_LSM6DS3)。 请参阅[从 Seeed 的 Github 下载的演示指南](/Guide_to_use_demos_downloaded_from_Seeed's_Github)，以便更快地将代码载入到主控制器板子上。 总共有三个演示示例在子目录 ***示例***。

资源下载
---------

- **[Eagle]** [Grove - 6-Axis Accelerometer&Gyroscopev 1.0](https://github.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/raw/master/res/Grove%20-%206-Axis%20AccelerometerGyroscopev1.0.zip)
- **[PDF]** [Grove - 6-Axis Accelerometer&Gyroscopev 1.0 SCH](https://github.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/raw/master/res/Grove%20-%206-Axis%20Accelerometer%26Gyroscope%20v1.0-SCH.zip)
- **[PDF]** [Grove - 6-Axis Accelerometer&Gyroscopev 1.0 PCB](https://github.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/raw/master/res/Grove%20-%206-Axis%20Accelerometer%26Gyroscope%20v1.0_PCB.pdf)
-  **[Library]** [Grove-6-Axis_AccelerometerAndGyroscope](https://github.com/Seeed-Studio/Accelerometer_And_Gyroscope_LSM6DS3)
-  **[Datasheet]** [Datasheet of LSM6DS3](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndGyroscope/master/res/LSM6DS3TR.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_6-Axis_Accelerometer&Gyroscope -->
