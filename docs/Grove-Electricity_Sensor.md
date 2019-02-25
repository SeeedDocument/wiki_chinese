---
name: Grove - Electricity Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Electricity-Sensor-p-777.html
oldwikiname: Grove_-_Electricity_Sensor
prodimagename: Twig-Electricity-Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Electricity_Sensor
sku: 101020027
tags: grove_analog, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Electricity_Sensor/master/img/Twig-Electricity-Sensor.jpg)

Electricity sensor 模块是 Grove 系列的成员。它基于 TA12-200 型电流互感器，这种电流互感器可将幅度调低。您可以使用它来测试高达 5A 的交流电。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.29.324b4b17X2qweP&id=45558584472)

## 产品特性
--------

-   Grove 接口
-   最大输入 :  5A
-   准确率高
-   体形小巧

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 创意应用
-----------------

-   交流电测量
-   设备状态监测

## 规格参数
-------------

### 关键参数

| **名称**    | **最小值**                |
|--------------|------------------------|
| PCB 尺寸     | 2.0cm\*4.0cm           |
| 接口    | 2.0mm 间距引脚 |
| IO 口 | SIG,NC,NC,GND          |
| RoHS 认证         | 通过                    |

### 电气特性

| **名称**             | **最小值** | **典型值** | **最大值** | **单位**  |
|-----------------------|---------|----------|---------|-----------|
| 转换率  | -       | 2000:1   | -       | -         |
| 输入电流         | 0       | -        | 5       | A         |
| 输出电流        | 0       | -        | 2.5     | mA        |
| 采样电阻   | -       | 800      | -       | Ω         |
| 采样电压      | 0       | -        | 2       | V         |
| 工作频率     | 20      | -        | 20K     | HZ        |
| 非线性尺度       | -       | -        | 0.2%    | -         |
| 相移           | -       | -        | 5'      | -         |
| 工作温度 | -55     | -        | 85      | ℃         |
| 介电强度   | -       | 6        | -       | KVAC/1min |

## Platforms Supported
-------------------

## 使用方法
-----

### 与 [Arduino](/Arduino "Arduino") 一起使用

以下工程演示了测量交流电压幅度的简单应用。SIG引脚将根据测量的交流电流输出交流电压。您可以使用 ADC 来测量该值。

-   将模块连接到 [Grove - Base shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.16cabadcpAFFZr&id=520233320144) 的 **A0**。
-   把交流电线缆穿过电流互感器的孔。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Electricity_Sensor/master/img/Grove-Electricity_Sensor_hardware.jpg)

-   复制并粘贴下面的代码到一个新的 Arduino 工程。

```
    /****************************************************************************/  
    //  Function: Measure the amplitude current of the alternating current and
    //            the effective current of the sinusoidal alternating current.
    //  Hardware: Grove - Electricity Sensor        
    //  Date:    Jan 19,2013
    //  by www.seeedstudio.com
    #define ELECTRICITY_SENSOR A0 // Analog input pin that sensor is attached to

    float amplitude_current;               //amplitude current
    float effective_value;       //effective current

    void setup()
    {
        Serial.begin(9600);
        pins_init();
    }
    void loop()
    {
        int sensor_max;
        sensor_max = getMaxValue();
        Serial.print("sensor_max = ");
        Serial.println(sensor_max);
        //the VCC on the Grove interface of the sensor is 5v
        amplitude_current=(float)sensor_max/1024*5/800*2000000;
        effective_value=amplitude_current/1.414;//minimum_current=1/1024*5/800*2000000/1.414=8.6(mA)
                            //Only for sinusoidal alternating current
        Serial.println("The amplitude of the current is(in mA)");
        Serial.println(amplitude_current,1);//Only one number after the decimal point
        Serial.println("The effective value of the current is(in mA)");
        Serial.println(effective_value,1);
    }
    void pins_init()
    {
        pinMode(ELECTRICITY_SENSOR, INPUT);
    }
    /*Function: Sample for 1000ms and get the maximum value from the SIG pin*/
    int getMaxValue()
    {
        int sensorValue;             //value read from the sensor
        int sensorMax = 0;
        uint32_t start_time = millis();
        while((millis()-start_time) < 1000)//sample for 1000ms
        {
            sensorValue = analogRead(ELECTRICITY_SENSOR);
            if (sensorValue > sensorMax)
            {
                /*record the maximum sensor value*/
                sensorMax = sensorValue;
            }
        }
        return sensorMax;
    }
```

-   上传代码。

<div class="admonition note">
<p class="admonition-title">Note</p>
代码可以检测的最小有效电流可以使用下面的公式计算 : minimum_current=1/1024*5/800*2000000/1.414=8.6(mA)
</div>

-   打开串口监视器，结果如下 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Electricity_Sensor/master/img/Elecricity_Sensor.jpg)

### 与 Raspberry Pi 一起使用

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.


2.完成配置开发环境，否则请遵循 [这里](http://wiki.seeedstudio.com/cn/GrovePi_Plus/)。

3.连接

-   将传感器用 Grove 线缆插入  Grovepi  **A0** 插口。

4.跳转到演示目录 :

       cd yourpath/GrovePi/Software/Python/

-   演示代码如下 :

```
    nano grove_electricity_sensor.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Electricity Sensor to analog port A0
    # SIG,NC,NC,GND
    sensor = 0

    grovepi.pinMode(sensor,"INPUT")

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    while True:
        try:
            # Get sensor value
            sensor_value = grovepi.analogRead(sensor)

            # Calculate amplitude current (mA)
            amplitude_current = (float)(sensor_value / 1024 * grove_vcc / 800 * 2000000)

            # Calculate effective value (mA)
            effective_value = amplitude_current / 1.414

            # minimum_current = 1 / 1024 * grove_vcc / 800 * 2000000 / 1.414 = 8.6(mA)
            # Only for sinusoidal alternating current

            print "sensor_value", sensor_value
            print "The amplitude of the current is", amplitude_current, "mA"
            print "The effective value of the current is", effective_value, "mA"
            time.sleep(1)

        except IOError:
            print "Error"
```

5.运行代码。
```
    sudo python grove_electricity_sensor.py
```
## 资源下载
---------

-   **[Eagle文件]** [Grove -Electricity Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Electricity_Sensor/master/res/Electricity_sensor_v1.0_eagle_files.zip)
-   **[原理图PDF]** [Schematic in PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-Electricity_Sensor/master/res/Electricity_sensor_sch.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Electricity_Sensor -->
