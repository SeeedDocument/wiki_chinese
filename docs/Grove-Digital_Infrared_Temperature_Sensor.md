---
name: Grove - Digital Infrared Temperature Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Digital-Infrared-Temperature-Sensor-p-2385.html
oldwikiname: Grove_-_Digital_Infrared_Temperature_Sensor
prodimagename: Grove－Digital_Infrared_Temperature_Sensor_4.jpg)
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Digital_Infrared_Temperature_Sensor
sku: 101020077
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

<table>
    <tr>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/Grove－Digital_Infrared_Temperature_Sensor_1.jpg"></td>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/Grove－Digital_Infrared_Temperature_Sensor_2.jpg"></td>
    </tr>
</table>

The Digital Infrared temperature sensor 是基于 MLX90615 的非接触式温度测量模块。红外敏感热电堆探测器芯片和信号调制芯片集成在同一个封装中。该模块与 Arduino 使用 SMBus 进行通信，多达 127 个传感器可以通过公共 2 线读取。由于模块的低噪声放大器，16 位 ADC 和强大的 DSP 单元，它可以在宽温度范围内实现 1℃ 的高精度和 0.02℃ 的高测量分辨率。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3cf0cb0eMTEAGk&id=531816314395)

## 规格参数
-------------

<table border="1" cellspacing="0" width="50%">
<tr>
<th>
项目
</th>
<th>
最小值
</th>
<th>
典型值
</th>
<th>
最大值
</th>
<th>
单位
</th>
</tr>
<tr align="center">
<th scope="row">
电压
</th>
<td>
2.6
</td>
<td>
3
</td>
<td>
3.4
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
电流
</th>
<td>
</td>
<td>
1.4
</td>
<td>
1.5
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
环境温度范围
</th>
<td colspan="3">
-40 - 85
</td>
<td>
℃
</td>
</tr>
<tr align="center">
<th scope="row">
物体温度范围
</th>
<td colspan="3">
-40 - 115
</td>
<td>
℃
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
 20x40x9.6
</td>
<td>
mm
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/Grove－Digital_Infrared_Temperature_Sensor_4.jpg)

| 引脚号 | 名称 | 类型   | 功能说明                             |
|------------|------|--------|--------------------------------------------------|
| 1          | GND  | -      | 信号地                                   |
| 2          | VCC  | in     | 正电源输入端 (3.3V 或 5V) |
| 3          | SDA  | in/out | I2C 数据输入/输出                            |
| 4          | SCL  | in     | I2C CLK                                          |

## 使用方法
-----

我们将在此提供一个示例，向您展示如何使用该传感器来测量传感器前面的目标温度，并将结果打印在串行监视器上。

-   使用 [Grove - Base Shield](/Base_Shield_V2 "Grove - Base Shield") 端口 **D2** 将此模块连接到 seeeduino。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/Digital_Infrared_Temperature_Sensor4.JPG)

### 软件

1. 下载库和演示代码 [Digital_Infrared_Temperature_Sensor_MLX90615](https://github.com/Seeed-Studio/Digital_Infrared_Temperature_Sensor_MLX90615)。
2. 通过路径 : **..\\arduino-1.0.5\\libraries** 将其解压缩到 Arduino IDE 的库文件中
3. 通过路径 : **File(文件) -&gt; Examples(示例) ->Digital_Infrared_Temperature_Sensor_MLX90615->MLX90615Soft** 直接打开演示代码

    您可以看见 :

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/MLX90615_demo_code.jpg)

    虽然传感器已通过启用数字 SMBus 兼容接口的工厂校准，但是库是基于 soft i2c library 的，因此您可以使用任何 AVR 芯片上的任何数字引脚来驱动 SDA 和 SCL 线路。我们使用 **D2** 作为 SCL 引脚和 **D3** 作为此演示代码中的 SDA 引脚。

4. 将代码上传到Arduino。
5. 启动串行监视器。

    您可以看见 :

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/img/Digital_Infrared_Temperature_Sensor_Serial_Monitor.jpg)

现在，您可以使用该传感器测量目标物体的温度。根据我们的实验，将传感器放置在室内正常温度下，确保传感器 1M 范围前面没有任何热量来源。物体温度将近似等于环境温度。当测量物体温度时，应确保物体尽可能靠近传感器，但不要接触传感器的表面，我们建议距离小于 3cm。祝你测试愉快。

!!!Tip
     关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/res/Grove_Digital_Infrared_Temperature_Sensor_v1.0_eagle_file.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


资源下载
--------

- **[Eagle文件]** [Grove Digital Infrared Temperature Sensor v1.0 eagle file.zip](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/res/Grove_Digital_Infrared_Temperature_Sensor_v1.0_eagle_file.zip "File:Grove Digital Infrared Temperature Sensor v1.0 eagle file.zip")
- **[数据手册]** [MLX90615.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Infrared_Temperature_Sensor/master/res/MLX90615.pdf "File:MLX90615.pdf")
- **[其他资源]** [Demo Code](https://github.com/Seeed-Studio/Digital_Infrared_Temperature_Sensor_MLX90615)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Digital_Infrared_Temperature_Sensor -->
