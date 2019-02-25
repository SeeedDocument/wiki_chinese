---
name: Grove - IMU 9DOF v2.0
category: Sensor
bzurl: https://seeedstudio.com/Grove-IMU-9DOF-v2.0-p-2400.html
oldwikiname: Grove_-_IMU_9DOF_v2.0
prodimagename: Grove-IMU_9DOF_v2.0.JPG
wikiurl: http://wiki.seeedstudio.com/cn/Grove-IMU_9DOF_v2.0/
sku: 101020080
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/Grove-IMU_9DOF_v2.0.JPG)

 Grove - IMU 9DOF v2.0是 **Grove - IMU 9DOF v1.0** 的升级版，它是基于 MPU-9250 的高性能 9 轴运动检测模块。 MPU-9250 是集成的 9 轴运动检测设备，专为低功耗，低成本和高性能要求的消费电子设备（包括智能手机，平板电脑和可穿戴式传感器）而设计。 MPU-9250 具有三个 16 位 ADC，用于数字化陀螺仪输出和三个 16 位 ADC，用于数字化加速度计输出和三个16位ADC，用于数字化磁力计输出。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.12eb6c70u21V9X&id=45574308377)

产品特性
-------------


- I2C / SPI 接口
- Auxiliary I2C
- 低功耗
- 400kHz 快速模式 I2C，用于与所有寄存器进行通信
- 数字输出 3 轴角速率传感器（陀螺仪），用户可编程的数值范围为 ±250，±500，±1000和±2000°/秒
- 数字输出 3 轴加速度计，可编程数值范围为 ±2g，±4g，±8g和±16g
- 满量程测量范围的数字输出三轴加速度计为 ±4800μT


!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/Grove-IMU_9DOF_v2_inter.png)


① - Grove 接口，连接到 **I2C** 端口

② - I2C 或 SPI 两种端口可以供选择（默认为I2C），如果要使用SPI，请断开这一个。

③ - 地址选择键，默认连接 b 和 c 地址为 0x68，如果连接 b 和 a 地址为0x69，如果要使用 SPI，请将此连接断开。

④ - SPI 接口

⑤ - Auxiliary I2C 端口进行主机串行数据传输的端口

⑥ - Auxiliary I2C 端口作为主串行时钟

⑦ - 中断数字输出

使用方法
-----

基于库，我们可以在串行监视器上显示 Accel 和 Gyro 和 Magnet 的值。 现在我们来演示如何使用该模块。

### 硬件安装

 硬件安装非常简单，因为 Seeeduino 有一个 **I2C Grove**，所以我们需要做的是通过 Grove连接线连接到 **I2C Grove** 端口。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/Grove-IMU_9DOF_v2.0_connect.jpg)

### 程序部分

1. 下载 [库](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/Grove_IMU_9DOF_9250.zip).
2. 通过路径将库解压缩到 Arduino IDE 的库文件中： ..\arduino-1.0.5\libraries.
3. 将IMU_9D0F_Demo 文件解压缩到 Arduino IDE 的库文件中: ..\arduino-1.0.5\libraries.
4. 通过路径直接打开代码： **File(文件) -> Example(示例) -> Grove_IMU_9DOF_9250**
5. 上传代码 请注意，您应该选择正确的电路板类型和 COM 端口。
6. 你可以看到

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/Grove-IMU_9DOF_v2.0_demo.jpg)

在静态状态下，z 轴输出值约为 0.98g，所以可以参考这一点来测试传感器是否正常工作。

**轴定向**

下图显示了灵敏度轴和旋转的方向。注意图中的标识符（•）。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/MPU9250_axes.jpg)

加速度计和陀螺仪的旋转灵敏度和极性方位

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/img/MPU9250_axes2.jpg)

指南针灵敏度轴方向

资源下载
--------
-   **[Eagle 文件]** [Grove - IMU 9DOF v2.0 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/Grove-IMU_9DOF_v2.0_sch_pcb.zip)
-   **[库文件]** [Grove - IMU 9DOF v2.0 library](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/Grove_IMU_9DOF_9250.zip)
-   **[芯片数据手册]** [MPU-9250 datashet](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/MPU-9250A_Product_Specification.pdf)
-   **[其他资源]** [MPU-9250 Register Map](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_9DOF_v2.0/master/res/MPU-9250A_Reg_Map.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_IMU_9DOF_v2.0 -->
