---
name: Grove - 6-Axis Accelerometer&Compass V2.0
category: Sensor
bzurl: https://seeedstudio.com/Grove-6-Axis-Accelerometer&Compass-v2.0-p-2476.html
oldwikiname: Grove_-_6-Axis_Accelerometer&Compass_V2.0
prodimagename: Accelerometer_And_Compass_v2.JPG
wikiurl: http://wiki.seeedstudio.com/cn/Grove-6-Axis_AccelerometerAndCompass_V2_0
sku: 101020081
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/Accelerometer_And_Compass_v2.JPG)

Grove –6-Axis Accelerometer&Compass V2.0 是一个 3 轴加速度计与 3 轴磁传感器的结合。它是 Grove - 6-Axis Accelerometer&Compass V1.0 的升级版本，它基于 LSM303D 传感器模块，LSM303D 的可选线性加速度量程为 : ±2g / ±4g / ±8g / ±16g，可选磁场量程为 : ±2 /±4 / ±8 / ±12 gauss。加速度计部件和磁性部件都可以单独关闭以降低功耗。通过这个模块的给定库，Arduino 可以通过 I2C 接口获取数据。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.8.4b0ee235vIl1j3&id=520936682474&ns=1&abbucket=1#detail)

## 规格参数
-------------

-   输入电压 : 5V
-   SPI，I2C 接口
-   可选量程
-   6 方向检测
-   2 个独立可编程中断发生器
-   掉电模式

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](
http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

## 硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/Grove-6-Axis_AccelerometerAndCompass_V2.0_inter.jpg)

-   ①I2C 接口
-   ②SPI 接口
-   ③I2C 或 SPI 的选择焊盘 (默认 I2C)，如果需要使用 SPI，隔断焊盘连接。
-   ④中断数字输出
-   ⑤地址选择的焊盘，默认连接 b 和 a 的地址是 0x1E，如果连接 b 和 c 的地址是 0x1D，如果需要使用 SPI，请将该焊盘隔断并连接到另一侧。

## 操作示例
-------------

LSM303D 是一款包含 3 轴加速计和 3 轴传感器的 6 轴传感器模块。它具有一个 I2C 数字接口，免去使用模数转换器。

MCU 可以通过 I2C 接口直接采集数据。让我们开始使用吧。

### 硬件连接

1.  硬件连接非常简单，因为在 Seeeduino 上有 I2C 的 Grove 接口，只需要通过 Grove 线缆将模块连接到 I2C 接口就可以了。
2.  通过 USB 线缆将 Seeeduino 连接到 PC 以给系统供电。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/6-Axis_AccelerometerAndCompass_V2.0_connect.jpg)

### 下载代码并上传

1.  下载 [demo\_code](https://github.com/Seeed-Studio/6Axis_Accelerometer_And_Compass_v2)，它演示了如何使用该模块来计算方向。
2.  上传代码。
3.  打开串口监视器，可以看见传感器的输出结果如下 :

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/6-Axis_AccelerometerAndCompass_V2.0_demo.jpg)

4. 您可以看到加速度值和磁北与 x 轴之间的顺时针角度。

先显示 X/Y/Z 3 轴的加速度;然后计算磁北和 x 轴之间的顺时针角度。

还计算了磁北与 x 轴投影之间的顺时针角度。

参阅 [这里](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/res/LSM303_application_note.pdf) 了解有关此参数的更多信息。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/Airplane.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/Airplane_calculated.jpg)

<div class="admonition note">
<p class="admonition-title">Notes</p>
<p>1.  所有 ST MEMS 加速度计都经过工厂校准，避免在大多数应用中需要进一步校准。但是为了达到低于 2° 的航向精度，需要一个简单的校准程序。</p>
<p>2.  测试磁北和 x 轴之间的顺时针角度时，可以将 Xa 轴对齐到任意方向，但不要使其朝下。 参考下面的图片 :</p>
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/img/Testing.jpg)

## 资源下载
---------
-   **[Eagle 文件]** [6-Axis\_Accelerometer%26Compass\_v2.0 eagle file](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/res/Grove-6-Axis_AccelerometerAndCompass_v2.0_sch_pcb.zip)
-   **[库文件]** [6-Axis Accelerometer&Compass v2.0 Library](https://github.com/Seeed-Studio/6Axis_Accelerometer_And_Compass_v2)
-   **[芯片数据手册]** [LSM303D\_datashet](https://raw.githubusercontent.com/SeeedDocument/Grove-6-Axis_AccelerometerAndCompass_V2.0/master/res/LSM303D_datasheet.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_6-Axis_Accelerometer&Compass_V2.0 -->
