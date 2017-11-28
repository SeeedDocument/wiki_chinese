---
title: Grove - IMU 10DOF v2.0
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-IMU-10DOF-v2.0-p-2691.html
oldwikiname:
prodimagename: Grove-imu-10dof-v2.0.JPG
bzprodimageurl: https://statics3.seeedstudio.com/seeed/img/2016-08/mr7fhEvszUFQsHT2SjUSVb29.jpg
wikiurl: http://seeed.wiki/Grove-IMU_10DOF_v2
sku: 101020252
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg
---

![](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/img/Grove-imu-10dof-v2.0.jpg)

Grove-IMU 10DOF v2.0 是 Grove-IMU-10DOF 的升级版，用 BMP280 代替 BMP180。作为广泛采用的 BMP180 的继任者，BMP280 在需要精确压力测量的应用中具有强劲的性能。该模块基于 MPU-9250 和 BMP280，MPU-9250 是一个 9 轴 MotionTracking 设备，它结合了 3 轴陀螺仪，3 轴加速度计，3 轴磁力计和一个数字运动处理器（DMP），BMP280 是用于消费应用的高精度，超低功耗数字压力传感器。该模块非常适合智能手机，平板电脑和可穿戴设备的应用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.653c372dvP1Ko9&id=546828485726&ns=1&abbucket=1#detail)

## 版本对比
----
| 产品                | SKU       | 发布日期  | 说明                                | 产品链接 |
|------------------------|-----------|----------------|--------------------------------------------|---------------|
| Grove - IMU 10DOF      | 101020079 | 2015年3月     | 基于 [MPU-9250](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_10DOF/master/res/MPU-9250A_Product_Specification.pdf) 和 [BMP180](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_10DOF/master/res/BMP180.pdf)      | 已停产           |
| Grove - IMU 10DOF v2.0 | 101020252 | 2016年9月 | 采用博世公司继 BMP180 后推出的 [BMP280](https://raw.githubusercontent.com/SeeedDocument/Grove-Barometer_Sensor-BMP280/master/res/Grove-Barometer_Sensor-BMP280-BMP280-DS001-12_Datasheet.pdf)| [点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.15.653c372dvP1Ko9&id=546828485726&ns=1&abbucket=1#detail)   |


## 规格参数
-------------

-   I2C Grove 接口，包括 GND，VCC，SDA，SCL 引脚
-   MPU-9250 I2C 地址可选
-   低功耗
-   400kHz 快速模式 I2C 用于与所有寄存器通信
-   量程为 ±250，±500，±1000，和 ±2000°/sec 的数字输出 X-，Y- 和 Z- 轴角速度传感器(陀螺仪)
-   量程为 ±2g，±4g，±8g 和 ±16g 的数字输出 3 轴加速度计
-   数字输出磁强计，量程为 ±4800 uT
-   数字输出气压计，范围 300 ~ 1100hPa (海拔 9000m ~ -500m)
-   尺寸 : 25.43mm x 20.35mm

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## Platforms Supported
-------------------

## 硬件概述
------------------
![](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/img/hardware.jpg)


-  MPU-9250 I2C 地址选择焊盘，默认连接 **a** 和 **b** 地址为 0x68，如果连接 **b** 和 **c** 地址为0x69
-  MPU-9250 中断引脚，应配置中断，可用的中断源有 :  motion detection，fifo overflow， data ready，i2c master error。
- 轴向:
下图显示了轴的灵敏度方向和旋转极性。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_10DOF/master/img/Imu-10dof-dir-axes.png)
- BMP280 是专门为移动应用设计的绝对气压传感器。传感器模块采用非常紧凑的 8 引脚金属盖 LGA 封装，面积仅为 2.0×2.5 mm2，高度为 0.95 mm。其尺寸小， 2.7 μA @1Hz 的低功耗使得其在手机，GPS 模块或手表等电池驱动设备中大放异彩。

## 入门指导
-----

#### 连接

通过一个简单的演示向您展示 Grove - IMU 10DOF V2.0 如何工作的。开始前请进行以下准备 :

| Seeeduino V4 | Grove - IMU 10DOF v2.0 | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/img/Grove-imu-10dof-v2.0_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3b475e0Rof5cH&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.15.653c372dvP1Ko9&id=546828485726&ns=1&abbucket=1#detail)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.730262b4XlvZfE&id=520233320144)|


- 将 Grove - IMU 10DOF v2.0 连接到 Base Shield 的 **I2C** 端口。
- 将 Base Shield 插入 Arduino。
- 通过 USB 线缆将 Arduino 连接至 PC。

![](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/img/arduino%20connection.jpg)

#### 软件部分

- 下载 [Grove-IMU_10DOF_v2 library.](https://github.com/Seeed-Studio/Grove_IMU_10DOF_v2.0/archive/master.zip)
- 遵循 [how to install an arduino library](http://wiki.seeed.cc/How_to_install_Arduino_Library/) 安装库文件。
- 重启 Arduino IDE，通过路径 : **File(文件) -> Example(示例) ->GROVE_IMU_10DOF_V2-master-> IMU_10DOF_V2_Test** 打开 **IMM_10DOF_Test**
![](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/img/library%20example.jpg)
- 上传代码。请注意选择正确的板子类型和 COM 端口。
- 可以看见 :
![](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_10DOF/master/img/Imu-10dof-test.png)


## 资源下载
--------

-   **[Eagle 文件]** [Grove - IMU 10DOF v2 eagle file](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/res/Grove%20-%20IMU%2010DOF%20v2.0.zip)
-   **[原理图 PDF]** [Grove - IMU 10DOF v2 schematics pdf file](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/res/Grove%20-%20IMU%2010DOF%20v2.0%20Sch.pdf)
-   **[PCB 图 PDF]** [Grove - IMU 10DOF v2 PCB pdf file](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/res/Grove%20-%20IMU%2010DOF%20v2.0%20PCB.pdf)
-   **[库文件]** [Get library from github](https://github.com/Seeed-Studio/Grove_IMU_10DOF_v2.0/archive/master.zip)
-   **[数据手册]** [BMP280 datasheet](https://github.com/SeeedDocument/Grove-IMU_10DOF_v2.0/raw/master/res/BMP280-Datasheet.pdf)
-   **[数据手册]** [MPU-9250 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-IMU_10DOF/master/res/MPU-9250A_Product_Specification.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_IMU_10DOF -->
