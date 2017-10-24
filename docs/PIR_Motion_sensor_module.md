---
title: PIR Motion sensor module
category: MakerPro
bzurl: https://www.seeedstudio.com/pir-motion-sensor-module-p-74.html?cPath=84_88&zenid=020999c566d2f31841dc54602b7d02ef
oldwikiname:  PIR Motion sensor module
prodimagename:  Pir_motion_sensor_v1.0.jpg
surveyurl: https://www.research.net/r/PIR_Motion_sensor_module
sku:   113990020
---
![](https://github.com/SeeedDocument/PIR_Motion_sensor_module/raw/master/img/Pir_motion_sensor_v1.0.jpg)

PIR（被动红外检测）用于检测人体运动。该版本有一个可以支持远程和广角测量的大镜头。2.54mm 标准连接器易于在任何位置固定。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.4aedf3e71G3a25&id=45673483594)

##   产品特性
---
*   长距离

*   广角度

*   低消耗

*   DC 3.0-5.5V 电源供应

##   规格参数
---
*   输入电压: DC3.0-5.5V

*   电流: 100uA(最大)

*   检测距离: 9m(最大)

*   输出信号: 0,3 VCC (检测到运动时输出高电平)

*   检测角: 120°

*   接口:3个引脚 2.54mm 间距
*   尺寸： L36*W26*H21(mm)

##   用法
---
以下示例展示了感应单元的简单应用。当有人在其检测范围内移动时，它将通过 **SIG** 引脚输出高电平，LED 将点亮。否则，它将输出低电平。你可以以此用它来检测人的动作。

![](https://github.com/SeeedDocument/PIR_Motion_sensor_module/raw/master/img/PIR_motion_sensor_module_connection.JPG)

###   程序设计

包括重要的代码段。
演示代码如下：
```
/*******************************************************************************/
/*macro definitions of PIR motion sensor pin and LED pin*/
#define PIR_MOTION_SENSOR 8//Use pin 8 to receive the signal from the module
#define LED    4//the Grove - LED is connected to D4 of Arduino

void setup()
{
    pinsInit();
}

void loop()
{
    if(isPeopleDetected())//if it detects the moving people?
    turnOnLED();
    else
    turnOffLED();
}
void pinsInit()
{
    pinMode(PIR_MOTION_SENSOR, INPUT);
    pinMode(LED,OUTPUT);
}
void turnOnLED()
{
    digitalWrite(LED,HIGH);
}
void turnOffLED()
{
    digitalWrite(LED,LOW);
}
/***************************************************************/
/*Function: Detect whether anyone moves in it's detecting range*/
/*Return:-boolean, ture is someone detected.*/
boolean isPeopleDetected()
{
    int sensorValue = digitalRead(PIR_MOTION_SENSOR);
    if(sensorValue == HIGH)//if the sensor value is HIGH?
    {
        return true;//yes,return ture
    }
    else
    {
        return false;//no,return false
    }
}
```

##   资源下载
---
- [PIR Motion sensor Eagle file](https://github.com/SeeedDocument/PIR_Motion_sensor_module/raw/master/res/PIR_sensor_v1.0.zip)
