---
name: Grove - 3-Axis Digital Gyro
category: Sensor
bzurl: https://seeedstudio.com/Grove-3-Axis-Digital-Gyro-p-750.html
oldwikiname: Grove_-_3-Axis_Digital_Gyro
prodimagename: Grove-3-Axis_Digital_Gyro.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-3-Axis_Digital_Gyro
sku: 101020050
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/img/Grove-3-Axis_Digital_Gyro.jpg)

Grove - 3-Axis Digital Gyro 是一个基于 ITG3200 的电子陀螺仪模块。ITG3200 是目前业界最快的单芯片，数字输出的三轴 MEMS 运动处理陀螺仪。适用于游戏、3D 鼠标或其他运动检测相关的应用。ITG-3200 具有三个用于数字化陀螺仪输出的 16 位模数转换器，一个用户可选的内部低通滤波器和一个快速模式的 I2C (400kHz) 接口。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.16.77e6a58cFyJ8YW&id=45483246815&ns=1&abbucket=1#detail)

## 产品特性
--------

-   输入电压 : 3.3V, 5V
-   输入电压 : 6.5mA
-   闲置模式电流 : 5μA
-   分辨率 : 14 LSBs per °/sec
-   满量程范围 : ±2000°/sec
-   加速度 : 10,000g for 0.3ms
-   I2C 接口
-   三个 16 位模数转换器
-   片上温度传感器
-   集成放大器和低通滤波器
-   保温耐湿
-   符合 RoHS 和及绿色环保标准

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

Platforms Supported
-------------------

## 操作示例
-------------

本演示将向您展示如何从这个数字陀螺仪获取数据，数据以 rad/s 为单位。

准备一个 Grove - 3-Axis Digital Gyro 和一个 [Seeeduino](https://item.taobao.com/item.htm?spm=a230r.1.14.41.5b62a1c0aCA5Q9&id=45721222112&ns=1&abbucket=1#detail)

### 硬件连接

硬件连接非常简单，因为 Seeeduino 有一个 I2C Grove 接口

所以，我们需要做的是通过 Grove 线缆将其连接到 I2C Grove 接口。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/img/Grove-3-Axis_Digital_Gyro_Hardware.JPG)

### 下载代码并盛传

点击 [这里](https://github.com/Seeed-Studio/Grove_3_Axis_Digital_Gyro/) 下载库，然后将其放到 Arduino 的库文件夹。

打开 **File(文件) -> examples(示例) -> Grove_3_Digital_Gyro -> ITG3200_gyro**，打开演示代码

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/img/ITG3200_gyro_ArduinoIde.jpg)

点击 Upload 上传代码，如果您对如何启动 Arduino 有任何疑问，请点击 [这里](/Getting_Started_with_Seeeduino)。

### 检查结果

现在，您可以打开串口监视器来检查结果。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/img/Grove-3-Axis_Digital_Gyro_SerialDta.jpg)

## 参考资料
---------

下图显示了 3 个轴的方向。您可以借助它来理解结果的物理意义。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/img/Gyro_Reference_1.jpg)


 ## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/res/Grove-3-Axis_Digital_Gyro_Eagle_File.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---------

-   **[Eagle文件]** [Grove - 3-Axis Digital Gyro Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/res/Grove-3-Axis_Digital_Gyro_Eagle_File.zip)
-   **[库文件]** [Digital Gyro Library](https://github.com/Seeed-Studio/Grove_3_Axis_Digital_Gyro)
-   **[芯片数据手册]** [Datasheet of ITG-3200.](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Gyro/master/res/ITG-3200.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Gyro -->
