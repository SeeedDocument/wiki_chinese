---
name: Grove - 3-Axis Compass V1.0
category: Sensor
bzurl: https://seeedstudio.com/Grove-3-Axis-Digital-Compass-p-759.html
oldwikiname: Grove_-_3-Axis_Compass_V1.0
prodimagename: Grove-3-Axis_Compass_V1.0.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-3-Axis_Compass_V1.0
sku: 101020034
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/img/Grove-3-Axis_Compass_V1.0.jpg)

该模块基于磁场感应芯片 HMC5883L，可提供高达 1°~2° 的航向精度。HMC5883L 包含高分辨率的 HMC118X 系列磁场传感器，及 Honeywell 公司开发的专用放大器，具有自动消除功能，偏移消除和 12 位 ADC。 加上外围电源管理电路，这是一个可用于低成本的罗盘和磁力计的易于使用和可靠的罗盘模块。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.40df14c3i0K8b5&id=45460663307)

## 规格参数
--------------

-   输入电压 : 3.3V, 5V
-   睡眠模式下功耗 : 2.5uA
-   测量模式下功耗 : 640uA
-   高分辨率
-   I2C 接口
-   兼容 3.3V 或 5.0V 开发平台
-   最大 116Hz 输出频率
-   高航向精度

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

## 操作示例
-------------

### 与 [Arduino](/Arduino "Arduino") 一起使用

本演示将向您展示如何读取原始数据，如何使用本地磁偏角测量数据，以及如何获取方位角。

首先，在您要采取任何操作之前，您需要准备要在演示中使用的参数，也就是您当地的磁偏角。

你可以通过 [磁偏角网页](http://www.magnetic-declination.com/) 找到它。 例如，我的是 -2°37'，也就是 -2.617 度。

然后将其从度数转移到弧度，然后得到“偏角”。 例如，在我的情况下，declinationAngle = -2.617 \* π / 180 = -0.0456752665 rad。 三个有效数字就足够了，所以我会把它缩短到 -0.0456 rad。 这是您将要用演示代码替换 "declinationAngle" 值的参数。

让我们开始运行吧

1. 把 3-axis compass 插入到 Grove - Base Shield 的 I2C 口

2. 下载库文件 : [Digital Compass Library](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/res/Digital_Compass.zip)。通过路径 : **..\\arduino-1.0.1\\libraries** 将其解压缩到 Arduino IDE 的库文件中

3. 通过路径 : **File(文件) ->Example(示例) ->Digital Compass ->HMC5883L_Example** 打开示例

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/img/Digital_Compass1.jpg)

4. 将变量 "declinitionAngle" 的值替换为已经计算出的值。

5. 上传代码。

6. 打开串行监视器检查输出结果。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/img/Digital_Compass2.jpg)

### 与 Raspberry Pi 一起使用

1.你需要 Raspberry pi 和 一个 Grovepi 或 Grovepi+。

2.您应该已经完成配置开发环境，否则请按照 [这里](/GrovePiPlus) 来配置。

3.连接

-   将传感器用 Grove 线缆插入 Grovepi 的插座 i2c-x(1~3)。

4.跳转到演示目录 :

       cd yourpath/GrovePi/Software/Python/

-   演示代码如下 :

```
    nano grove_compass_lib.py       
    nano grove_compass_example.py    
```
```
    import grove_compass_lib
    c=grove_compass_lib.compass()
    while True:
            print "X:",c.x,"Y:",c.y,"X:",c.z,"Heading:",c.headingDegrees
            c.update()
            time.sleep(.1)
```

5.运行代码。
```
    sudo python grove_compass_example.py
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/res/Grove-3-Axis_Digital_Compass_Eagle_File.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---------

-   **[Eagle文件]** [Grove-3-Axis Digital Compass Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/res/Grove-3-Axis_Digital_Compass_Eagle_File.zip)
-   **[库文件]** [Digital Compass Library](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/res/Digital_Compass.zip)
-   **[芯片数据手册]** [HMC5883.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Compass_V1.0/master/res/HMC5883.pdf "File:HMC5883.pdf")


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Compass_V1.0 -->
