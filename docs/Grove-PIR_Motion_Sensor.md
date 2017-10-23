---
title: Grove - PIR Motion Sensor
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-PIR-Motion-Sensor-p-802.html
oldwikiname: Grove - PIR Motion Sensor
prodimagename: Breakout_for_LinkIt_Smart_7688_v2.0_product_view_700.jpg
surveyurl: https://www.surveymonkey.com/r/grove-pir-motion-sensor
sku: 101020020
tags: io_3v3, io_5v, plat_duino, plat_pi
---

---
![](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/images/Grove_-_PIR_Motion_Sensor.jpg)

该传感器允许您检测动物的运动，通常是用于检测在其检测范围内人体的运动。 只需将其连接到 Grove - Base shield 并对其进行编程，当任何人在其检测范围内移动时，传感器将在其 **SIG** 引脚上输出高电位。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2ac176a4pN2dqu&id=45568896887)


## 产品特性
---

- 具有 Grove 兼容接口
- 可调检测距离
- 可调节保持时间

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

## 规格参数
----
|参数|值/范围
|---|---|
|工作电压|	3V–5V
|工作电流(VCC = 3V)|	100uA
|工作电流(VCC = 5V)|	150uA
|测量范围|0.1 - 6m
|默认检测距离|	3m
|保持时间|1 - 25s
|工作波长|7 - 14um
|检测角度|	120度

## Platforms Supported
-----

## 入门指导
---
### 使用 Arduino

以下示例演示了感应运动的简单应用。 当有人在其检测范围内移动时，它将通过 SIG 引脚输出高电平，LED 将点亮。 否则，它将输出低电平。 这样你可以用它来检测是否有人。

#### 硬件连接

在这里，我们将通过一个简单的演示向您展示这个 Grove - PIR MOTION SENSOR 的工作原理。 首先，我们需要准备以下内容：

| Seeeduino V4 | Grove - PIR MOTION SENSOR | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/img/Grove%20-%20PIR%20Motion%20Sensor_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2ac176a4pN2dqu&id=45568896887)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|



- 将 Grove - PIR 运动传感器连接到 base shield 的 **D2** 端口。
- 将 Grove - LED 连接到基座屏蔽的 **D4** 端口。
- 将 base Shield 插入 Arduino。
- 使用 USB数据线将 Arduino 连接到 PC。

![](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/images/PIR_Motion_test.jpg)

#### 代码
- 将代码上传到Arduino。

```c
/*macro definitions of PIR motion sensor pin and LED pin*/
#define PIR_MOTION_SENSOR 2//Use pin 2 to receive the signal from the module
#define LED	4//the Grove - LED is connected to D4 of Arduino


void setup()
{
	pinMode(PIR_MOTION_SENSOR, INPUT);
	pinMode(LED,OUTPUT);
}

void loop()
{
	if(isPeopleDetected())//if it detects the moving people?
		digitalWrite(LED, HIGH);
	else
		digitalWrite(LED, LOW);
}


/***************************************************************/
/*Function: Detect whether anyone moves in it's detecting range*/
/*Return:-boolean, true is someone detected.*/
boolean isPeopleDetected()
{
	int sensorValue = digitalRead(PIR_MOTION_SENSOR);
	if(sensorValue == HIGH)//if the sensor value is HIGH?
	{
		return true;//yes,return true
	}
	else
	{
		return false;//no,return false
	}
}
```
- 当我们走动时，LED 灯将亮起。

!!!Note
    可以通过在板上增加两个额外的电位器来调整检测距离和保持时间。 详情请参考下面的 V1.2 Eagle。 也可以通过更换跳线帽将模块设置为可以重新触发或不可重新触发。


### 使用 Raspberry Pi

#### 硬件连接
首先，我们需要准备以下内容：

| Raspberry pi | Grove - PIR MOTION SENSOR | GrovePi_Plus |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/img/Grove%20-%20PIR%20Motion%20Sensor_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11zpryre&id=528322046763)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.cc5edb7DY3ttS&id=45568896887)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e113G7Bdt&id=45506190895)|


- 您需要完成配置开发环境，否则遵循 [说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。
- 使用Grove连接线将传感器插入Grovepi +插座 **D8**。

![](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/img/pi%20connection.jpg)

#### 软件

- 导航到演示目录：

```
  cd yourpath/GrovePi/Software/Python/
```

- 找到这行代码

```
   nano grove_pir_motion_sensor.py   # "Ctrl+x" to exit #
```

```python
import time
import grovepi

# Connect the Grove PIR Motion Sensor to digital port D8
# SIG,NC,VCC,GND
pir_sensor = 8

grovepi.pinMode(pir_sensor,"INPUT")

while True:
    try:
        # Sense motion, usually human, within the target range
        if grovepi.digitalRead(pir_sensor):
            print 'Motion Detected'
        else:
            print '-'

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.2)

    except IOError:
        print "Error"
```
- 运行这个示例

```
   sudo python grove_pir_motion_sensor.py
```

## 资源下载
---

- **[Eagle]** [Grove - PIR Motion Sensor Eagle File v1.2](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/res/Grove_-_PIR_Motion_Sensor_Eagle_File.zip)
- **[Easyeda]** [Schematics at Easyeda](https://easyeda.com/Seeed/Grove_PIR_Sensor_v1_2-101b3ca1281645c4a36fbc06b1c7b8d0)
- **[PDF]** [Grove - PIR Motion Sensor v1.2 Schematics](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/resources/Grove_PIR_Sensor_v1.2.pdf)
- **[PDF]** [Grove - PIR Motion Sensor Eagle V1.2 PCB](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/res/Grove%20-%20PIR%20motion%20sensor%20v1.1b%20PCB.pdf)
- **[Library]** [Github repository for PIR Motion Sensor](https://github.com/Seeed-Studio/PIR_Motion_Sensor)
- **[Datasheet]** [BISS0001 Datasheet](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/resources/Twig_-_BISS0001.pdf)
- **[Datasheet]** [Fresnel lens 8120 Datasheet](https://github.com/SeeedDocument/Grove_PIR_Motion_Sensor/raw/master/resources/Fresnel_lens_8120.pdf)
