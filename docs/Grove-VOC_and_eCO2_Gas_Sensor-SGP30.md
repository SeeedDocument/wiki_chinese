---
name: Grove-VOC and eCO2 气体传感器(SGP30)
category: 传感器
bzurl:
oldwikiname:
prodimagename:
surveyurl:
sku: 101020512
tags:
---


![](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/img/IMG_0012a.jpg)




Grove-VOC和eCO2气体传感器（SGP30）是一种空气质量检测传感器。 该模块基于SGP30，我们为该模块提供TVOC（总挥发性有机化合物）当量输出和CO2当量输出。


SGP30是一款数字多气体传感器，可轻松集成到空气净化器、指令控制通风和物联网应用中。 该传感器的的CMOSens®技术在单个芯片上提供完整的传感器系统，并带有I2C接口、温度控制的微型加热板和两个预处理的室内空气质量信号。 作为第一个在一个芯片上具有多个传感元件的金属氧化物气体传感器，SGP30提供了有关空气质量的更详细信息。


<p style="text-align:center"><a href="https://www.seeedstudio.com/-Grove-VOC-and-eCO2-Gas-Sensor-(SGP30)-p-3071.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>

## 产品特性


- 室内多气体检测传感器应用
- 出色的长期稳定性
- 通过I2C接口输出TOVC和CO2当量
- 低功耗
- 芯片模块卷带包装，可回流焊接


## 规格参数

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#999;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#999;color:#444;background-color:#F7FDFA;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#999;color:#fff;background-color:#26ADE4;}
.tg .tg-eh2d{background-color:#ffffff;border-color:inherit;vertical-align:top}
.tg .tg-xf7g{background-color:#444444;border-color:inherit;text-align:center}
.tg .tg-f5ry{background-color:#ffffff;border-color:inherit}
.tg .tg-28l8{background-color:#ffffff;border-color:inherit;text-align:center}
.tg .tg-3xi5{background-color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-3we0{background-color:#ffffff;vertical-align:top}
.tg .tg-i81m{background-color:#ffffff;text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 529px">
<colgroup>
<col style="width: 143px">
<col style="width: 98px">
<col style="width: 288px">
</colgroup>
  <tr>
    <th class="tg-xf7g">Parameter</th>
    <th class="tg-xf7g">Signal</th>
    <th class="tg-xf7g">Values</th>
  </tr>
  <tr>
    <td class="tg-f5ry">工作电压</td>
    <td class="tg-f5ry" colspan="2">                           3.3V/5V</td>
  </tr>
  <tr>
    <td class="tg-f5ry" rowspan="2">输出范围</td>
    <td class="tg-f5ry">TVOC</td>
    <td class="tg-28l8">    0 ppb to 60000ppb</td>
  </tr>
  <tr>
    <td class="tg-eh2d">CO₂当量</td>
    <td class="tg-3xi5">    400 ppm to 60000 ppm</td>
  </tr>
  <tr>
    <td class="tg-eh2d" rowspan="2"><br><br>采样频率</td>
    <td class="tg-eh2d">TVOC</td>
    <td class="tg-3xi5">1HZ</td>
  </tr>
  <tr>
    <td class="tg-eh2d">CO₂当量</td>
    <td class="tg-3xi5">1HZ</td>
  </tr>
  <tr>
    <td class="tg-3we0" rowspan="7"><br><br><br><br><br><br><br>Resolution<br></td>
    <td class="tg-3we0" rowspan="3"><br><br>TVOC</td>
    <td class="tg-i81m">0 - 2008 ppb / 1 ppb</td>
  </tr>
  <tr>
    <td class="tg-i81m">2008 - 11110 ppb / 6 ppb</td>
  </tr>
  <tr>
    <td class="tg-i81m">11110 - 60000 ppb / 32 ppb</td>
  </tr>
  <tr>
    <td class="tg-3we0" rowspan="4"><br><br><br>CO₂eq</td>
    <td class="tg-i81m">400 - 1479 ppm / 1 ppm</td>
  </tr>
  <tr>
    <td class="tg-i81m">1479 -5144 ppm / 3 ppm</td>
  </tr>
  <tr>
    <td class="tg-i81m">5144 - 17597 ppm / 9 ppm</td>
  </tr>
  <tr>
    <td class="tg-i81m">17597 - 60000 ppm / 31 ppm</td>
  </tr>
  <tr>
    <td class="tg-3we0">Default I2C address</td>
    <td class="tg-i81m" colspan="2">0X58</td>
  </tr>
</table>



## 创意应用

- 空气净化器
- 需求控制通风系统
- 物联网应用
- 新型室内空气监测系统




## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |

!!!Caution
  上面提到的支持的平台是模块的硬件或理论兼容性的指示。 在大多数情况下，我们仅为Arduino平台提供软件库或代码示例。 无法为所有可能的MCU平台提供软件库/演示代码。 因此，用户必须编写自己的软件库。






## 入门指导

!!!Note
    如果您是第一次使用arduino，我们强烈建议您在开始之前看[Arduino](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)



### 连接Arduino示例

#### 硬件

**需要物品**

| Seeeduino V4.2 | Base Shield| Grove-VOC and eCO2 Gas Sensor(SGP30) |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/-Grove-VOC-and-eCO2-Gas-Sensor-(SGP30)-p-3071.html" target="_blank">Get One Now</a>|



!!!note
      **1** 请小心插拔microUSB连接线，否则将可能会对接口造成破坏。另外，请使用4线microUSB，2线的只能用来充电，不能作为数据线。如果没有请点击下面链接购买。
     [here](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)


    **2** 每个Grove 模块在购买时会带有连接线，若丢失连接线，您可以点击下面链接购买。
     [here](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)



- **Step 1.** 将传感器与扩展板D2口通过Grove连接线链接

- **Step 2.** 将主控板seeeduino与扩展板连接。

- **Step 3.** 将seeeduino和PC通过microUSB连接.


![](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/img/3.jpg)



!!!Note
	 如果没有扩展板，也是可以直接将传感器连接在seeeduino上的，seeeduino上有2个Grove接口，分别是Grove-I2C、Grove-uart

| Seeeduino     | Grove-VOC 和 eCO2 传感器(SGP30) |
|---------------|-------------------------|
| 5V            | 红                     |
| GND           | 黑                   |
| SDA           | 白                   |
| SCL           | 黄                  |




#### 软件

- **Step 1.** 从github上下载需要的库 [Seeed SGP30 library](https://github.com/Seeed-Studio/SGP30_Gas_Sensor) 。

- **Step 2.** 参考 [How to install library](http://wiki.seeedstudio.com/How_to_install_Arduino_Library) 来安装相应的库

- **Step 3.** 解压你刚刚下载的 `SGP30_Gas_Sensor-master.zip` ，在example文件夹你将会看到三个文件


![](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/img/ex.png)



`absolute_humidity_example` 需要外部湿度传感器进行校准


`base_example` 是一个简单的、不需校准的收集数据示例

`baseline_operation_example`可以将收集的数据保存到flash，程序将会自动收集并保存


我们建议使用`baseline_operation_example`，然后单击`xxx.ino`文件打开示例。

- **Step 4.** 下载demo，如果不知道如何下载请点击[How to upload code](http://wiki.seeedstudio.com/Upload_Code/).

- **Step 5.** 打开arduino IDE的 **Serial Monitor** 然后点击 **Tool-> Serial Monitor**. 然后同时点击 ctrl+shift+m 。如果一切正常的话，你将会看到:



```

318
tVOC  Concentration:74ppb
CO2eq Concentration:506ppm
319
tVOC  Concentration:80ppb
CO2eq Concentration:509ppm
320
tVOC  Concentration:66ppb
CO2eq Concentration:500ppm
321
tVOC  Concentration:69ppb
CO2eq Concentration:511ppm
322
tVOC  Concentration:70ppb
CO2eq Concentration:511ppm
323
tVOC  Concentration:60ppb
CO2eq Concentration:493ppm
324
tVOC  Concentration:72ppb
CO2eq Concentration:502ppm

```


!!!Tips
        1- ppm: parts per million. 1 ppm = 1000 ppb (parts per billion)

        2- 上面的结果是基于 `baseline_operation_example.ino`文件作为示例的

        3- 我们的测试是在办公室进行的，由于和您的环境不同，测试结果可能有差异。



## 资源下载

- **[Zip]** [Grove-VOC and eCO2 Gas Sensor(SGP30) eagle file](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/res/Grove-VOC_and_eCO2_Gas_Sensor%20-SGP30.zip)
- **[PDF]** [SGP30 Datasheet](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/res/Sensirion_Gas_Sensors_SGP30_Datasheet_EN.pdf)
- **[PDF]** [SGP30 Driver Integration Guide HW I2C](https://github.com/SeeedDocument/Grove-VOC_and_eCO2_Gas_Sensor-SGP30/raw/master/res/Sensirion_Gas_Sensors_SGP30_Driver-Integration-Guide_HW_I2C.pdf)



## 技术支持

如果你有文档或者技术上的任何疑问，请联系 [techsupport@seeed.cc](techsupport@seeed.cc) [forum](https://forum.seeedstudio.com/).
