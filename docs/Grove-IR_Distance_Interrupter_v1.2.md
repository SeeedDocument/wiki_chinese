---
name: Grove - IR Distance Interrupter v1.2
category: Sensor
bzurl: https://seeedstudio.com/Grove-IR-Distance-Interrupter-p-1278.html
oldwikiname: Grove_-_IR_Distance_Interrupter_v1.2
prodimagename: Grove_-_IR_Distance_Interrupter_v1.2.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-IR_Distance_Interrupter_v1.2
sku: 101020040
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/img/Grove_-_IR_Distance_Interrupter_v1.2.jpg)

**Grove - IR Distance Interrupter** 用于检测阻挡光线的任何物体。该模块由一个 IR LED 和一个光电传感器（光电晶体管）组成。IR LED 发出的光线被位于传感器前面的物体反射，这个反射被光电传感器（光电晶体管）检测到。任何白色（或浅色）表面的反射率大于黑色（或更深）的彩色表面。

当检测到反射光时，它会在 **SIG** 引脚上产生 **高电平**（或二进制 **1**）输出。 板载 LED 指示灯也会发光。 如果没有检测到反射，或者物体离传感器太远，**SIG** 引脚上的输出将保持 **低电平**（二进制 **0**）。 板载 LED 指示灯也将熄灭。 该传感器的可检测范围是 7.5-40 厘米。该模块集成了轨到轨运算放大器来放大光电晶体管的输出。有一个电位器可以用来调整放大器的增益，即检测灵敏度。

使用此传感器，您可以构建以下（但不限于）应用：**线路跟随机器人，光学编码器** 和 **对象计数应用程序**。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.11.35a15028ARqBMV&id=547068489828)

!!!Note
    该产品对非红外辐射也是轻度敏感的，因此光敏器件上的任何明亮的光都会干扰红外光的检测。

!!!Tip
    本产品的使用说明与 <span style="font-weight:bold">Grove - Infrared Reflective Sensor's</span> 相同。如果您曾经使用过 Grove - Infrared Reflective Sensor，则可以直接使用本产品。

## 版本变更
---------------

| 产品版本                                      | 发布日期 | 支持状态 |
|-------------------------------------------------------|--------------|----------------|
|  v1.2 以前的版本                             |  2012 年 6 月‎    | 不支持 |
| Grove - IR Distance Interrupter v1.2（当前版本） | 2016 年 4 月   | 支持   |


## 产品特性
--------

-   兼容 Grove，并且易于使用。
-   高灵敏度和可信度
-   更长的检测距离
-   可根据不同场合调节灵敏度
-   更加耐用。

!!!Tip
    有关 Grove 模块的更多信息，请参考 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)。

## 规格参数
--------------

| 参数                     | 值                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------|
| 工作电压(V)          | 3.3 或 5V                                                                       |
| 工作电流(mA)         | 最大：20 mA                                                                         |
| 有效检测距离 | 7.5–40 cm                                                                              |
| 感光元件        | [数据手册](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/Reflective_photosensor.pdf) |
| 输出运算放大器 | [数据手册](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/LM393.pdf)                  |
| 重量                        | 2.5 g（仅模块） 8.5 g（整个包装）                                   |

## Platforms Supported
-------------------

!!!Note
    如果没有提及特定平台的版本号，则表示该产品支持该平台的所有版本。但是，您将需要额外的格罗夫盾，如 [Grove Base Shield V2](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17789056553.22.5a9e7b45o9Zu1Z&id=520233320144)。


## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/img/Grove-IR_Distance_Interrupter_v1.2_hardware_overview_1200.jpg)

-   **RPR-359F Reflective photosensor**，高度灵敏的反射式光电传感器。
-   **LM393 operational amplifier**，轨到轨运算放大器。
-   **LED Indicator**，当接收到的红外光强度超过预设水平时，LED将亮起。
-   **Light sensitivity adjusting potentiometer**，调节反射光电传感器对光的灵敏度。

## 快速入门
---------------
让我们看看如何用这个模块来做出一些基本的应用：

### 与 Arduino 使用

#### 需求材料

-   Grove - IR Distance Interrupter v1.2 × 1
-   [Seeeduino V4.2](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17789056553.25.5a9e7b45o9Zu1Z&id=45721222112) （其他开发板也可以） × 1
-   [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) × 1
-   [Grove - Base Shield](/Base_Shield_V2) × 1

#### 连接

1. 使用 Grove 电缆将 Grove - IR Distance Interrupter v1.2 连接到 Seeeduino。
2. 将传感器放在白色（或浅色）表面。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/img/Reflective_photosensor3.jpg)

3. 用螺丝刀调整电位器，改变反射式光电传感器的灵敏度，直到 LED 指示灯亮起。当顺时针旋转时，反射式光电传感器将对光线更为敏感。
!!!Note
    使用合适的螺丝刀调整电位器。过大的操作力度或频繁调整可能会损坏电位器的触点。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/img/Reflective_photosensor2.jpg)
![](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/img/Reflective_photosensor1.jpg)

4. 新建一个 Arduino 的新窗口并将下面的代码上传到开发板。
```c++
void setup()  {
    Serial.begin(9600);
    pinMode(6,INPUT);
}
void loop()  {
    while(1)  {
        delay(500);
        if(digitalRead(6)==LOW)  {
            Serial.println("Somebody is here.");
        }
        else  {
            Serial.println("Nobody.");
        }
    }
}
```

5. 上传成功后，打开串口监视器。当光线被某个物体阻挡时，你会在串口监视器看到“Somebody is here.”，否则你会看到“Nobody.”。

### 使用 Raspberry Pi

#### 需求材料

-   [Raspberry Pi](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17789056553.23.1ec0d625SgNUaQ&id=528322046763) × 1
-   [Grovepi+](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17789056553.17.1ec0d625SgNUaQ&id=45506190895) × 1
-   [Grove 线](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.29.2d0d0afpfkVya&id=45575764936) × 1

#### 硬件连接和软件安装

1. 请准备好一个 GrovePi+。本例程基于 GrovePi+。

2. 请搭建好 GrovePi+ 的开发环境。如果没有，请参考 [这里](http://wiki.seeedstudio.com/cn/GrovePi_Plus/)。

3. 连接：使用 Grove 线把 Grove - IR Distance Interrupter 连接到 GrovePi 的 **D4** 接口上。

4. 浏览到演示目录，在终端中运行以下命令。
```
    cd yourpath/GrovePi/Software/Python/
```
    在终端中运行命令：
```
    nano grove\_infrared\_distance\_interrupt.py
```
在终端中运行命令：
```
nano grove\_infrared\_distance\_interrupt.py
```
    复制并粘贴下面的代码到界面中，然后退出并保存 :
```python
import time
import grovepi
 
# Connect the Grove Infrared Distance Interrupt Sensor to digital port D4
# SIG,NC,VCC,GND
sensor = 4
 
grovepi.pinMode(sensor,"INPUT")
 
while True:
    try:
        # Sensor returns LOW and onboard LED lights up when the
        # received infrared light intensity exceeds the calibrated level
        if grovepi.digitalRead(sensor) == 0:
            print "found something"
        else:
            print "nothing"
 
        time.sleep(.5)
 
    except IOError:
        print "Error"
```
5. 运行下面的指令来开始使用：
```
    sudo python grove\_infrared\_distance\_interrupt.py
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/Eagle_files.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


资源下载
---------

-   **[Eagle 文件]**[Grove - IR Distance Interrupter v1.2 Eagle file](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/Eagle_files.zip)
-   **[数据手册]**[Reflective Photosensor Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/Reflective_photosensor.pdf)
-   **[数据手册]**[LM393 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/LM393.pdf)
-   **[数据手册]**[LMV358 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/LMV358_datasheet.pdf)
-   **[代码文件]**[Infrared Reflective Sensor Source Files](https://raw.githubusercontent.com/SeeedDocument/Grove-IR_Distance_Interrupter_v1.2/master/res/Grove-Infrared_Reflective_Sensor_v1.0_SourceFile.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_IR_Distance_Interrupter_v1.2 -->
