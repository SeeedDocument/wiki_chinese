---
name: Grove - Ear-clip Heart Rate Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Ear-clip-Heart-Rate-Sensor-p-1116.html
oldwikiname: Grove_-_Ear-clip_Heart_Rate_Sensor
prodimagename: Heart_rate_ear_clip_kit.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Ear-clip_Heart_Rate_Sensor
sku: 101020033
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Ear-clip_Heart_Rate_Sensor/master/img/Heart_rate_ear_clip_kit.jpg)

耳夹心率套件包含一个耳夹和一个接收器模块。 心率测量套件可用于监测患者和运动员的心率。 结果可以通过串行端口显示在屏幕上，可以保存分析。 整个系统具有高灵敏度，低功耗和便携性的优点。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11ExZaxd&id=45556645088)

产品特性
--------

- 低功耗
- 方便使用
- 高灵敏度
- 完全符合RoHS标准

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

规格参数
-------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小
</th>
<th scope="col">
标准
</th>
<th scope="col">
最大
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
3.0
</td>
<td>
5.0
</td>
<td>
5.25
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
工作电流
</th>
<td colspan="3">
6.5
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
耳夹长度
</th>
<td colspan="3">
120
</td>
<td>
cm
</td>
</tr>
<tr align="center">
<th scope="row">
测量范围
</th>
<td colspan="3">
≥30/min
</td>
<td>
-
</td>
</tr>
</table>

创意应用
-----------------

-   心率监测器。

Platform Support
-------------------

使用方法
-----

以下示例展示了使用耳夹式心率传感器来测量心率的简单应用。

-   将此模块连接到 [Grove-Base shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 上的数字端口 **D2** 。 并将Grove-LED连接到数字端口 **D4**。
-   将Grove-Base shield插入Arduino / Seeeduino。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Ear-clip_Heart_Rate_Sensor/master/img/Ear_Clip_Heart_Rate.jpg)

-   将下面的代码复制并粘贴到新的Arduino编辑页面上。

```
    // Function: This program can be used to measure heart rate, the lowest pulse in the program be set to 30.
    //         Use an external interrupt to measure it.
    // Hardware: Grove - Ear-clip Heart Rate Sensor, Grove - Base Shield, Grove - LED
    // Arduino IDE: Arduino-1.0
    // Author: FrankieChu       
    // Date: Jan 22, 2013
    // Version: v1.0
    // by www.seeedstudio.com
    #define LED 4//indicator, Grove - LED is connected with D4 of Arduino
    boolean led_state = LOW;//state of LED, each time an external interrupt
                                    //will change the state of LED
    unsigned char counter;
    unsigned long temp[21];
    unsigned long sub;
    bool data_effect=true;
    unsigned int heart_rate;//the measurement result of heart rate

    const int max_heartpluse_duty = 2000;//you can change it follow your system's request.
                            //2000 meams 2 seconds. System return error
                            //if the duty overtrip 2 second.
    void setup()
    {
        pinMode(LED, OUTPUT);
        Serial.begin(9600);
        Serial.println("Please ready your chest belt.");
        delay(5000);
        arrayInit();
        Serial.println("Heart rate test begin.");
        attachInterrupt(0, interrupt, RISING);//set interrupt 0,digital port 2
    }
    void loop()
    {
        digitalWrite(LED, led_state);//Update the state of the indicator
    }
    /*Function: calculate the heart rate*/
    void sum()
    {
     if(data_effect)
        {
          heart_rate=1200000/(temp[20]-temp[0]);//60*20*1000/20_total_time
          Serial.print("Heart_rate_is:\t");
          Serial.println(heart_rate);
        }
       data_effect=1;//sign bit
    }
    /*Function: Interrupt service routine.Get the sigal from the external interrupt*/
    void interrupt()
    {
        temp[counter]=millis();
        Serial.println(counter,DEC);
        Serial.println(temp[counter]);
        switch(counter)
        {
            case 0:
                sub=temp[counter]-temp[20];
                Serial.println(sub);
                break;
            default:
                sub=temp[counter]-temp[counter-1];
                Serial.println(sub);
                break;
        }
        if(sub>max_heartpluse_duty)//set 2 seconds as max heart pluse duty
        {
            data_effect=0;//sign bit
            counter=0;
            Serial.println("Heart rate measure error,test will restart!" );
            arrayInit();
        }
        if (counter==20&&data_effect)
        {
            counter=0;
            sum();
        }
        else if(counter!=20&&data_effect)
        counter++;
        else
        {
            counter=0;
            data_effect=1;
        }

    }
    /*Function: Initialization for the array(temp)*/
    void arrayInit()
    {
        for(unsigned char i=0;i < 20;i ++)
        {
            temp[i]=0;
        }
        temp[20]=millis();
    }
```

- 上传代码
- 确保传感器接触到您的耳朵皮肤。 当我们测量心率时，这是输出的信号：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Ear-clip_Heart_Rate_Sensor/master/img/GROVE_heart_rate_chest_belt.bmp)

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Ear-clip_Heart_Rate_Sensor/master/img/Grove-heart_rate_serial.jpg)

在第一个图中，检测到的是心跳的波形图，当跳动时出现高脉冲。

<div class="admonition note">
<p class="admonition-title">Note</p>
如果串行监视器返回错误信息，请更改传感器的位置。
</div>

资源下载
---------

- [Grove - Ear-clip Heart Rate Sensor Demo code](https://raw.githubusercontent.com/SeeedDocument/Grove-Ear-clip_Heart_Rate_Sensor/master/res/Grove-Heart_rate_chest_belt_V1.0.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Ear-clip_Heart_Rate_Sensor -->
