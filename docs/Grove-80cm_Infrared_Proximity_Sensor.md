---
title: Grove - 80cm Infrared Proximity Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-80cm-Infrared-Proximity-Sensor-p-788.html
oldwikiname: Grove_-_80cm_Infrared_Proximity_Sensor
prodimagename: Image_of_PSD.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-80cm_Infrared_Proximity_Sensor
sku: 101020042
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-80cm_Infrared_Proximity_Sensor/master/img/Image_of_PSD.jpg)

Grove - 80cm Infrared Proximity Sensor 是一种通用型距离测量传感器。这款传感器基于 SharpGP2Y0A21YK，具有小型封装和低功耗的特点，可连续读取距离，并返回相应的模拟电压，范围为 : 10cm (4") 至 80cm (30")。可用于电视机，个人电脑，汽车等。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=45459991191)


## 产品特性
--------

-   易于使用
-   电源电压范围 : 2.5V–7V
-   Grove 接口

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 创意应用
-----------------

-   节水器具
-   玩具
-   机器人

## 规格参数
-------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
2.5V
</td>
<td>
5V
</td>
<td>
7V
</td>
</tr>
<tr align="center">
<th scope="row">
模拟输出电压 (80cm)
</th>
<td>
0.25V
</td>
<td>
0.4V
</td>
<td>
0.5V
</td>
</tr>
<tr align="center">
<th scope="row">
平均电流消耗
</th>
<td>
-
</td>
<td>
33mA
</td>
<td>
50mA
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 使用方法
-----

### 与 Arduino 一起使用

Grove - 80cm Infrared Proximity Sensor 使用很方便。电压读数与距离的关系如下所示。我们读取的电压可以表明从前面物体到这个传感器的距离。

-   将 3 针接口连接到传感器，并将 4 针接口连接到 **Grove-Base Shield** 的 **A1** 端口。

!!!Note
    这种传感器非常小，使用 JST 接口。这种接口有三根线 : GND，Vcc 和输出信号。由于这个传感器连续工作，并且不需要任何时钟来启动一个读取周期，所以很容易与任何微控制器接合。对于 Arduino & Seeeduino，我们准备了一个 4 针到 3 针的线缆，将传感器上的 3 针连接口接到 **Grove-Base Shield** 上的 4 针接口，以便与 Grove 接口兼容。

-   使用 USB 线缆连接 Arduino/Seeeduino 到电脑。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-80cm_Infrared_Proximity_Sensor/master/img/80cm_Infrared.jpg)

-   复制并粘贴代码至 Arduino IDE 中

```
    #define IR_PROXIMITY_SENSOR A1 // Analog input pin that  is attached to the sensor
    #define ADC_REF 5//reference voltage of ADC is 5v.If the Vcc switch on the Seeeduino
                     //board switches to 3V3, the ADC_REF should be 3.3
    float voltage;//the sensor voltage, you can calculate or find the distance
                    // to the reflective object according to the figures
                    //on page 4 or page 5 of the datasheet of the GP2Y0A21YK.

    void setup()
    {
        // initialise serial communications at 9600 bps:
        Serial.begin(9600);
    }

    void loop()
    {
        voltage = getVoltage();
        Serial.print("sensor voltage  = " );                       
        Serial.print(voltage);
        // wait 500 milliseconds before the next loop
        delay(500);
    }
    /****************************************************************************/
    /*Function: Get voltage from the sensor pin that is connected with analog pin*/
    /*Parameter:-void                                                       */
    /*Return:   -float,the voltage of the analog pin                        */
    float getVoltage()
    {
        int sensor_value;
        int sum;  
        // read the analog in value:
        for (int i = 0;i < 20;i ++)//Continuous sampling 20 times
        {
            sensor_value = analogRead(IR_PROXIMITY_SENSOR);
            sum += sensor_value;
        }
        sensor_value = sum / 20;
        float voltage;
        voltage = (float)sensor_value*ADC_REF/1024;
        return voltage;
    }
```

-   上传代码
-   打开串口监视器，可以得到电压值。您可以根据下图计算传感器到反射物体的距离。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-80cm_Infrared_Proximity_Sensor/master/img/Infrared_Proximity.jpg)

!!!Note
    由于输出是由发射器到反射点再到接收器的三角形计算出的，所以传感器的输出相对于正在测量的距离是非线性的

### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.

2.完成配置开发环境，否则请按照 [这里](http://wiki.seeedstudio.com/cn/GrovePi_Plus/) 操作。

3.连接

-   将传感器用 Grove 线缆插入 Grovepi 插口 **D4**。

4.跳转到演示目录 :

       cd yourpath/GrovePi/Software/Python/

-   演示代码如下 :

```
    nano grove_infrared_distance_interrupt.py    # "Ctrl+x" to exit #
```

```
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

5..运行代码。

```
    sudo python grove_infrared_distance_interrupt.py
```

## 参考资料
---------

这种新的检测器使用三角测量和一个小型的线性 CCD 阵列来计算视野中物体的距离。其基本思想是 : 发射器发射一束红外光。这个光线在视场中传播，遇到屋里就会反射回来。在没有物体的情况下，光线不会被反射，读数也不会显示任何物体。当光线从物体反射回来返回到探测器后，在反射点，发射器和探测器之间建立一个三角形。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-80cm_Infrared_Proximity_Sensor/master/img/Theory_of_PSD.jpg)

这个三角形中的角度根据到物体的距离而变化。这些新型检测器的接收器部分实际上是精密透镜，其基于上述三角形的角度将反射光透射到封闭的线性 CCD 阵列的各个部分上。然后，CCD 阵列可以确定反射光返回的角度，因此可以计算检测器到物体的距离。

这种新的测距方法几乎不受环境光线的干扰，对被测物体的颜色有着惊人的抗干扰能力。现在在阳光下检测黑色的墙也是可能的。


## 资源下载
---------

- **[数据手册]** [GP2Y0A21YK datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-80cm_Infrared_Proximity_Sensor/master/res/GP2Y0A21YK.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_80cm_Infrared_Proximity_Sensor -->
