---
title: Grove - Infrared Temperature Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Infrared-Temperature-Sensor-p-1058.html
oldwikiname: Grove_-_Infrared_Temperature_Sensor
prodimagename: Grove-Infrared_Temperature_Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Infrared_Temperature_Sensor
sku: 101020062
tags: grove_analog, io_3v3, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Grove-Infrared_Temperature_Sensor.jpg)

红外温度传感器是非接触式温度测量模型。 它由 116 个热电偶元件串联在一个浮动的微型膜片上，传感器的黑色表面很好地吸收了入射的热红外辐射，可能在输出时触发电压响应。该传感器根据目标温度输出一个模拟电压 (0~1.1V) 。

旧版本: v0.92.

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.3b30d947rTX1Li&id=531816314395&ns=1&abbucket=13#detail)

## 规格参数
-------------

-   电压 : 3-5V
-   测量电流供应 : 160-200 uA
-   测量范围 : -10~100°C
-   占用时间 : 2S
-   工作温度 : -10~80 °C
-   储存温度 : -35-80 °C

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

## 操作示例
-------------

以下草图演示了测量传感器周围温度和传感器前方目标温度的简单应用。并将结果打印在串行监视器上。

-   使用 Grove-Base Shield 的端口 **A0** 和 **A1** 将此模块连接到 Seeeduino。
-   下载 [演示代码](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/MeasureTemperature.zip) 并打开。

测量温度之前，您需要简单的设置。按照下面的说明进行测试，将获得准确的结果。

**步骤 1: 调节传感器电压**

上传演示程序后，将传感器置于正常环境中 5 分钟以上，使传感器温度与周围温度一致。然后打开串口监视器检查传感器输出的电压。理想情况下，当环境温度等于温度传感器时，红外线传感器 (TP-538U) 输出为 0V，由硬件调节偏置在 0.5V 的参考电压。如下图所示，传感器电压为 0.014V，我们只需要将您从程序中的串行监视器获得的偏移\ _vol 值更改为 0.014 即可。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Infrared_Temperature_Sensor_code2.jpg)
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Serialmonitor.jpg)

**步骤 2: 调整传感器检测距离**

根据我们的实验，传感器的名义测量距离是 9CM，但是我们不能保证所有的传感器都具有相同的特性。所以如果想得到准确的结果，需要用冰水混合液调节 0℃，用开水调节 100℃。之后，您可以获得传感器的有效距离。

具体的测量方法是在一个黑色的容器里装满冰和水，这个容器有一个平坦的表面。等待容器下降到 0℃，将传感器保持在物体之间 9CM，向前或向后移动传感器并检查结果，如果输出为 0℃，记下距离值。同样的方法来检查开水。当你获得一对值时，做一个平均的计算处理。你可以开始测量你刚刚获得的额定距离。

现在我们可以测量传感器周围的温度。传感器适用于名义距离，您可以尝试其他距离，但距离 - 温度图既不是传感器的制造商获得的，也不是我们获得的，您可以按照以上两条说明进行绘制。我们在演示代码中保留变量 **"temperature_range"** 。我们假设目标距离是 3 厘米，你测量的可能会多于或少于 5 厘米。希望你使用愉快。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Infrared_Temperature_Sensor_Code_1.jpg)

**高级应用程序示例:**

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Infrared_temperature_example.JPG)

<div class="admonition note">
<p class="admonition-title">Note</p>
<ol><li> 演示代码不支持 Atmega168 内核</li>
<li>为了获得准确的测量结果，距离 (D) 和目标层数 (S) 率 D：S 必须小于 0.5。</li></ol>
</div>

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/img/Dsdiagram.jpg)

## 资源下载
---------

-   **[Eagle文件]** [Grove-Infrared Temperature Sensor V0.9 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/Infrared_Temperature_Sensor_v0.92_egale_file.zip)
-   **[Eagle文件]** [Grove-Infrared Temperature Sensor V1.0 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/Infrared_Temperature_Sensor_V1.0_egale_file.zip)
-   **[芯片数据手册]** [OTP-538U Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/OTP-538Udatasheet.zip)
-   **[其他资源]** [Demo Code](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/MeasureTemperature.zip)
-   **[其他资源]** [Infrared Temperature Demo Code with SerialLCD](https://raw.githubusercontent.com/SeeedDocument/Grove-Infrared_Temperature_Sensor/master/res/Infrared_temperature_demo_code_with_serialLCD.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Infrared_Temperature_Sensor -->
