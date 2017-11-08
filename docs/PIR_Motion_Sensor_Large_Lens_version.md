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

PIR（被动红外探测）用于检测人体的运动。这个版本具有一个广角镜头可以用于长距离大范围检测。模块上的2.54mm 标准连接头使得它可以轻松地安装在任何地方。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.7033c493EiedM2&id=45673483594)

## 产品特性
---
*  测量距离长

*   测量角度大

*   低功耗

*   3.0-5.5V直流电源供电

## 规格参数
---
*   输入电压: DC3.0-5.5V

*   电流: 最大100uA

*   检测距离: 最大9m

*   输出信号: 待机0V；检测到热源运动后3V

*   敏感角度: 120°

*   连接器:3针2.54mm 引脚
*   尺寸： 36mm长*26mm宽*21mm高

## 使用说明
---

下面的工程演示了一个简单的运动感应示例。当有人在检测范围内移动时，通过 **SIG** 引脚输出高电平，LED灯亮。 否则，它将输出低电平。 然后你可以用它来检测人的动作。

![](https://github.com/SeeedDocument/PIR_Motion_sensor_module/raw/master/img/PIR_motion_sensor_module_connection.JPG)

### 程序代码

示例代码如下：
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

## 资源下载
---
- **[原理图PCB文件]**[PIR Motion sensor Eagle file](https://github.com/SeeedDocument/PIR_Motion_sensor_module/raw/master/res/PIR_sensor_v1.0.zip)
