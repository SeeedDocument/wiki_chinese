---
name: Grove - Loudness Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Loudness-Sensor-p-1382.html
oldwikiname: Grove_-_Loudness_Sensor
prodimagename: LoudnessSensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Loudness_Sensor
sku: 101020063
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/img/LoudnessSensor.jpg)

 Grove - Loudness Sensor 旨在检测环境的声音。 它基于LM2904放大器和内置的麦克风，它可以从麦克风中接收到高频信号并且进行放大和滤波，并输出正包络。 这可以用Arduino进行信号采集。 而且它输出值取决于声音输入的电平高低。输入信号会经过模块的两次滤波来避免不必要的信号干扰。 而且这里有一个螺旋电位计可以通过手动调整输出增益。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4075f3d30KVeTf&id=45476699231)

产品特性
--------------

-   工作电压 ：3.5~10 VDC
-   工作频率 ：50~2000 Hz
-   灵敏度 : -48~66 dB
-   信噪比：> 58 dB
-   输出信号范围：模拟信号（0-1023）

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


支持平台
-------------------

入门指导
-------------

### 使用 Arduino
#### 硬件连接
该模块使用芯片LM2904将迷你麦克风产生的电子信号进行放大。 最后，您将获得模数转换值。 我们尝试读取输出值。

在这里，我们将通过一个简单的演示向您展示这个 Grove - Loudness Sensor的工作原理。 首先，您需要准备以下内容：

| Seeeduino V4 | Grove - Loudness Sensor | Base Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Loudness_Sensor/raw/master/img/LoudnessSensor_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4075f3d30KVeTf&id=45476699231)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|


- 如下图所示，将 Loudness sensor 连接到 Grove-Base Shield 的模拟端口 **A0**。

![](https://github.com/SeeedDocument/Grove-Loudness_Sensor/raw/master/img/arduino%20loudness%20sensor.jpg)

-   使用  USB数据线将 Arduino / Seeeduino 连接到 PC。

#### 程序
-   将下面的代码复制并粘贴到新的 Arduino 编辑页面上。

```
int val;
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    analogRead(0);
    delay(10);
    val = analogRead(0);
    Serial.println(val);
    delay(200);
}
```

-   上传代码
-   然后打开串行监视器观察输出结果。 当向传感器吹气时会看到数值发生了很大变化。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/img/Loudness_Sensor.jpg)


**这是示波器的测试截图**
蓝线是来自麦克风的原始信号，黄色是 Loudness Sensor 输入的信号。 它是模块输出的原始信号。

然后向这个传感器吹气:

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/img/Loudness_Sensor_Test_1.bmp)

向这个传感器说话：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/img/Loudness_Sensor_Test_3.bmp)


### 使用Raspberry Pi

#### 硬件连接

- 首先，你需要准备以下内容。

|  Raspberry pi | Grove - DHT Sensor pro | Grovepi+ |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Loudness_Sensor/raw/master/img/LoudnessSensor_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11zpryre&id=528322046763)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4075f3d30KVeTf&id=45476699231)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e113G7Bdt&id=45506190895)|


- 您需要完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。

-  通过使用grove连接线将传感器插入Grovepi插座 **A0** 端口 。
![](https://github.com/SeeedDocument/Grove-Loudness_Sensor/raw/master/img/pi%20loudness%20sensor.jpg)

#### 程序

- 导航到演示目录：

```
    cd yourpath/GrovePi/Software/Python/
```

-   找到这行代码
```
    nano grove_loudness_sensor.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Loudness Sensor to analog port A0
    # SIG,NC,VCC,GND
    loudness_sensor = 0

    while True:
        try:
            # Read the sound level
            sensor_value = grovepi.analogRead(loudness_sensor)

            print "sensor_value =", sensor_value
            time.sleep(.5)

        except IOError:
            print "Error"
```

- 运行这个示例
```
    sudo python grove_loudness_sensor.py
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/res/Grove-Loudness_Sensor_Eagle_File.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


资源下载
--------

- **【Eagle】** [Grove - Loudness Sensor in Eagle format](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/res/Grove-Loudness_Sensor_Eagle_File.zip)
- **【PDF】** [Grove - loudness sensor Schematic in PDF format](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/res/Grove_loudness_sensor.pdf)
- **【PDF】** [Grove - loudness sensor PCB in PDF format](https://github.com/SeeedDocument/Grove-Loudness_Sensor/raw/master/res/Grove-loudness%20sensor%20PCB.pdf)
- **【Datasheet】** [LM2904DR Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Loudness_Sensor/master/res/LM2904DR.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Loudness_Sensor -->
