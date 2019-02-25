---
name: Grove - 3-Axis Digital Accelerometer(±1.5g)
category: Sensor
bzurl: https://seeedstudio.com/Grove-3-Axis-Digital-Accelerometer(±1.5g)-p-765.html
oldwikiname: Grove_-_3-Axis_Digital_Accelerometer(±1.5g)
prodimagename: 3_aix_acc.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-3-Axis_Digital_Accelerometer-1.5g
sku: 101020039
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_wio
---

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><div class="center">
<div class="floatnone">
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/3_aix_acc.jpg" />
</div>
</div></td>
<td><div class="center">
<div class="floatnone">
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/Grove-3-Axis_v1.3.jpg" />
</div>
</div></td>
</tr>
<tr class="even">
<td><div style="text-align: center">
Grove - 3-Axis Digital Accelerometer v1.2
</div></td>
<td><div style="text-align: center">
Grove - 3-Axis Digital Accelerometer v1.2b
</div></td>
</tr>
</tbody>
</table>

3-Axis Digital Accelerometer 是方向检测，手势检测和运动检测等项目中的关键部分。这款 3-Axis Digital Accelerometer(±1.5g) 基于 Freescale 的低功耗模块 MMA7660FC。它具有高达 10,000g 的高冲击耐受性和可配置的每秒采样率。对于大量不需要太大测量范围的应用，这款加速度计是一个很好的选择，因为它具有耐用，节能和合算的特点。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=686.1000925.0.0.4d555aagVGiYe&id=45770637854)


## 规格参数
--------------

-   工作电压 : 3.0 - 5.5V
-   关闭模式电流 : 0.4μA
-   待机模式电流 : 2μA
-   活动模式电流 : 47 μA 在 1 ODR
-   测量范围 : ±1.5g
-   灵敏度 : 21LSB/g
-   Suli 兼容库

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

<div class="admonition note">
<p class="admonition-title">Note</p>
关于 Suli 兼容库的更多信息请点击 <a class="external text" href="/Suli" rel="nofollow" target="_blank">Suli</a>.
</div>

## 操作示例
-------------

### 与 [Arduino](/Arduino "Arduino") 一起使用

在这里，我们将向您展示如何从这个传感器获取原始数据和由 "g" 测量的数据。

通过 Grove 线缆将此模块连接到 Grove - Base Shield 的 I2C 端口。

<div class="admonition note">
<p class="admonition-title">Note</p>
如果你想激活这个模块的中断功能，你需要将我们在板上划分出的 INT 焊盘连接到一个能够执行中断服务程序的 Arduino 引脚。
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/Digital_Accelerometer_Sensor_Connector1.5g.jpg)

安装我们在 [Resources](/Grove-3-Axis_Digital_Accelerometer-1.5g#resources) 部分提供的库。

直接按路径 : **File(文件) -> Example(示例) ->DigitalAccelerometer_MMA7660FC ->MMA7660FC_Demo** 打开代码。

在这个程序中，加速度信息通过 I2C 总线从传感器发送到 Seeeduino，然后 Seeeduino 将它们打印到串行监视器上。打开串口监视器检查结果。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/Grove-3-Axis_Digital_Accelerometer-1.5g-.jpg)

该传感器的输出由两部分组成 : 原始数据和转换为以重力 "g" 为单位的 3 轴加速度信息。


### 与 Raspberry 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或者 Grovepi+.

2.完成配置开发环境，否则请遵循 [here](/GrovePiPlus)。

3.连接

-   将传感器用 Grove 线缆插入 Grovepi socket i2c-x(1~3)。

4.跳转到演示目录 :

       cd yourpath/GrovePi/Software/Python/

-   演示代码如下 :

```
    nano grove_i2c_accelerometer.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Accelerometer (+/- 1.5g) to any I2C port eg. I2C-1
    # Can be found at I2C address 0x4c
    # SCL,SDA,VCC,GND

    while True:
        try:
            print grovepi.acc_xyz()
            time.sleep(.5)

        except IOError:
            print "Error"
```

5.运行代码。
```
    sudo python grove_i2c_accelerometer.py
```

## 参考资料
---------

下面是两个图帮助你理解结果的物理意义。

第一个图是关于每个轴的方向 :
![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/MMA7660_Direction.jpg)

第二个图给出了一些例子 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/img/Sensing_Direction_1.jpg)

## 资源下载
---------

-   **[Eagle文件]** [Grove - 3-Axis Digital Accelerometer Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/res/Grove-3-Axis_Digital_Accelerometer-1.5g-Eagle_File.zip)
-   **[芯片数据手册]** [Datasheet of MMA7660FC](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-1.5g/master/res/MMA7660FC.pdf)
-   **[其他资源]** [github repository for 3-Axis Digital Accelerometer(±1.5g)](https://github.com/Seeed-Studio/Accelerometer_MMA7660)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(±1.5g) -->
