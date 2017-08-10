---
title: Grove - Piezo Vibration Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Piezo-Vibration-Sensor-p-1411.html
oldwikiname: Grove_-_Piezo_Vibration_Sensor
prodimagename: Grove-Piezo_Vibration_Sensor-1.jpg
wikiurl: http://seeed.wiki/Grove-Piezo_Vibration_Sensor
sku: 101020031
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/img/Grove-Piezo_Vibration_Sensor-1.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/img/Piezo_Vibration_Sensor_02.jpg)

Grove - Piezo Vibration传感器适用于弹性，振动，冲击和触感的测量。该模块基于PZT薄膜传感器LDT0-028。当传感器来回移动时，其中的电压比较器将产生一定的电压。宽动态范围（0.001Hz〜1000MHz）保证了良好的测量性能。并且，您可以通过用螺丝调整板上电位器来调整其灵敏度。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.5e478797sIcKyY&id=45553185547)

## 产品特性
--------

-   标准Grove接口
-   宽动态测量范围：0.1Hz~180Hz
-   测量灵敏度可调
-   高度感知强烈冲击

!!!Tip
    更多关于Grove的信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 平台支持
-------------------
Arduino
Raspberry

## 创意应用
------------
- 洗衣机振动检测
- 低功耗唤醒开关
- 低成本振动感应
- 汽车警报系统
- 身体运动检测
- 安全系统

## 入门指导
-----

### 适用 [Arduino](/Arduino "Arduino")

#### 物理连接

在这里，我们将通过一个简单的例子向您展示Grove - Piezo Vibration传感器如何工作。首先，我们需要准备以下内容：



| Seeeduino V4 | Grove - Piezo Vibration | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/raw/master/img/Piezo%20vibration%20sensor_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.5-c.w5001-14920381017.3.24d7e03a9gi7Am&id=45721222112&qq-pf-to=pcqq.c2c&scene=taobao_shop)|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.14.65ebe8d8M8ajJY&id=45490731880)|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.5e478797sIcKyY&id=45553185547)|

当检测到振动时，Grove - Piezo Vibration传感器输出逻辑高电平。我们可以使用任何Arduino引脚来读取数据。以下是压电振动传感器控制LED的示例。当检测到振动时，该传感器输出逻辑高信号（灵敏度可通过调节电位器来更改），LED亮起。

<div class="admonition note">
<p class="admonition-title">注意</p>
当通过顺时针调节电位器来增加阈值电压时，即使原始输出应该为高电平，也可能最终输出低电平。
</div>



 - 通过4 pin的Grove接口将传感器模块和扩展板的**A0** 口相连。我们使用**数字脚 pin13 联通的板载LED** 来作为输出。
 - 将 the Grove - Basic Shield 插入 Arduino.
 - 通过USB数据线将Arduino 连接到PC。
![](https://github.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/raw/master/img/piezo%20vibration%20connection.jpg)

#### 软件

- 在Arduino 中新建一个文件，将下列代码复制粘贴到这个空白的文件中。

```
const int ledPin=13;
void setup() {
    Serial.begin(9600);
    pinMode(ledPin,OUTPUT);
}

void loop() {
    int sensorValue = analogRead(A0);
    Serial.println(sensorValue);
    delay(1000);
    if(sensorValue==1023)
    {
        digitalWrite(ledPin,HIGH);
    }
    else
    {
        digitalWrite(ledPin,LOW);
    }
}
```
- 触摸压电传感器使其振动，当然，任何方式使其振动都可以。当检测到振动时，LED将亮起。我们也可以打开串行监视器来查看传感器输出。

  ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/img/Grove-Piezo_Vibration_Sensor.jpg)

- 我们可以直接使用数字引脚，以扩展板上的D5为例，并将LED连接到引脚13。

```
const int ledPin=13;
void setup() {
    Serial.begin(9600);
    pinMode(ledPin,OUTPUT);
}

void loop() {
    int sensorState = digitalRead(5);
    Serial.println(sensorState);
    delay(1000);
    if(sensorState == HIGH)
    {
        digitalWrite(ledPin,HIGH);
    }
    else
    {
        digitalWrite(ledPin,LOW);
    }
}
```

### 使用于 Raspberry Pi （树莓派）

#### 物理连接
首先，我们需要准备以下内容：

| Raspberry pi | Grove - Piezo Vibration | GrovePi_Plus |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/raw/master/img/Piezo%20vibration%20sensor_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e478797F03vQV&id=528322046763)|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.14.65ebe8d8M8ajJY&id=45490731880)|[马上订购](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5e4787971UMLf1&id=45506190895)|

- 根据 [指南](http://seeed.wiki/GrovePi_Plus/) 来配置开发环境。
- 通过Grove线缆将传感器连接到grovepi+ 扩展板的 A0 端口。

![](https://github.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/raw/master/img/grove%20connection.jpg)

#### 软件

- 导航到示例目录下：

```
    转换路径到您的对应目录   cd yourpath/GrovePi/Software/Python/
```
-   代码如下：
```
    nano grove_piezo_vibration_sensor.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Piezo Vibration Sensor to analog port A0
    # OUT,NC,VCC,GND
    piezo = 0

    grovepi.pinMode(piezo,"INPUT")

    while True:
        try:
            # When vibration is detected, the sensor outputs a logic high signal
            print grovepi.analogRead(piezo)
            time.sleep(.5)

        except IOError:
            print "Error"
```

- 运行示例
```
    sudo python grove_piezo_vibration_sensor.py
```

## 资源下载
---------

- **[Eagle图]** [Grove - Piezo Vibration Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/res/Eagle.zip)
- **[原理图PDF]** [Grove - Piezo Vibration Sensor Schematic PDF File](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/res/Gvove-Piezo_Vibration_Sensor.pdf)
- **[PCB图PDF]** [Grove - Piezo Vibration Sensor PCB PDF File](https://github.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/raw/master/res/Gvove%20-%20Piezo%20Vibration%20Sensor%20v1.1%20PCB.pdf)
- **[数据手册]** [Piezo Vibration Sensor Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Piezo_Vibration_Sensor/master/res/Piezo_Vibration_Sensor.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Piezo_Vibration_Sensor -->
