---
name: Grove-Round Force Sensor(FSR402)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020553
tags: 
---


![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/main.jpg)

Grove-圆形力传感器(FSR402)是一款力敏模块。在传感器的终端有一个圆形的力敏电阻，其阻值取决于其表面所受压力。简单地说，压力越大电阻越小。然而，该传感器的输出并不是严格的线性，所以我们不建议用来做精确测量。关于该力敏电阻的详细信息，请您参考[FSR402 数据手册](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/res/FSR402.pdf)。

正如您所见，该模块是基于FSR402所设计的，Interlink Electronics FSR® 400系列是 单区域Force Sensing Resistor®系列的一部分。力敏电阻(FSR402)是坚固的聚合物厚膜(PTF)器件，随着施加在传感器表面的力的增加，电阻会减小。该力敏传感器适用于汽车电子、医疗系统、工业控制以及机器人等人机接口设备。



<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-Round-Force-Sensor-%28FSR402%29-p-3110.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特点

- 模拟输出
- 可靠的机械结构  
- 持久耐用：
    
    以4Hz、1Kg的冲击测试下，平均电阻改变-10%
    


## 产品规格

|**项目**|**参数**|
|:----:|:----:|
|工作电压|3.3V/5V|
|力测量范围|0.2N--20N|
|力分辨率|连续 (模拟)|
|模拟输出|0-650|
|无操作阻抗|>10 MΩ|
|最小电阻|1 KΩ|
|设备上升时间|<3 微妙|


!!!**提示**

如果您想要测量无操作阻抗，请将传感器上东西取下。

## 产品应用

- 汽车电子
- 医疗系统
- 工业控制
- 机器人


## 硬件概述


### 引脚映射


![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/pin_map.jpg)



### 原理图




![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/hardware.png)



该模块使用一颗DC-DC芯片（XC6206P332MR）来提供稳定的3.3V，正如您所看到的我们称之为3V3。您可以将这个力传感器 **J1** 看作一个称之为 **R<sub>f</sub>** 的可变电阻。压力越大 **R<sub>f</sub>** 的值越小。


上图中有两部分，左边部分：


<font color =#EE9A00>$VIN = \frac{3.3*30K}{30K+R_f}$</font>

对于右边的部分，它是一个发射极跟随器，我们使用放大器 **U1**来隔离前级和后级电路。

<font color =#EE9A00>$Vout = VIN$</font>

那么，输出就是：

<font color =#EE9A00>$Vout = \frac{3.3*30K}{30K+R_f}$</font>


!!!**提示**

在这一部分我们仅仅展示了部分原理图，完整的原理图文件请您参考 [资源下载](/#resources)



### 机械结构


![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/Mechanical_A.jpg)
![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/Mechanical_B.jpg)
![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/Exploded_View.jpg)





## 兼容平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|:-:|:-:|:-:|:-:|:-:|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo.jpg) |

!!!**注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。



## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**

| Seeeduino V4.2 | Base Shield| Grove-圆形力传感器(FSR402) |Grove-LED|
|:-:|:-:|:-:|:-:|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/thumbnail.jpg)|![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/Red%20LED.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-Round-Force-Sensor-%28FSR402%29-p-3110.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove---Red-LED-p-1142.html" target="_blank">点击购买</a>|



!!!**注**

   **1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。

   **2** 购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。





- **步骤 1.** 将Grove-圆形力传感器(FSR402)连接到Grove - Base Shield的 **A0** 接口。

- **步骤 2.** 将Grove-LED 连接到Grove-Base Shield的 **D3** 。

- **步骤 3.** 将Base Shield插到Seeeduino上。

- **步骤 4.** 通过USB线缆将Seeeduino连接到PC端。

![](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/img/connect.jpg)



!!!**注意**

如果没有Grove Base Shield，我们可以直接按照下面引脚定义将模块连接到Seeeduino上。


| Seeeduino     | Grove-圆形力传感器(FSR402)|
|:-:|:-:|
| 5V | 红|
| GND| 黑|
| 未连接 | 白|
| A0    | 黄|



| Seeeduino     | Grove-LED|
|:-:|:-:|
| 5V | 红|
| GND| 黑|
| 未连接 | 白|
| D3    | 黄|



#### 软件代码

!!!**注意**


如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/).

- **步骤 1.** 打开Arduino IDE，创建一个新文件，然后将以下代码拷贝进去。

```C++
/* How to use a Force sensitive resistor to fade an LED with Arduino
   More info: http://www.ardumotive.com/how-to-use-a-force-sensitive-resistor-en.html
   Dev: Michalis Vasilakis // Date: 22/9/2015 // www.ardumotive.com  */

//Constants:
const int ledPin = 3;     //pin 3 has PWM funtion
const int sensorPin = A0; //pin A0 to read analog input

//Variables:
int value; //save analog value


void setup(){
    
  pinMode(ledPin, OUTPUT);  //Set pin 3 as 'output'
  Serial.begin(9600);       //Begin serial communication

}

void loop(){
  
  value = analogRead(sensorPin);       //Read and save analog value from potentiometer
  Serial.println(value);               //Print value
  value = map(value, 0, 1023, 0, 255); //Map value 0-1023 to 0-255 (PWM)
  analogWrite(ledPin,255-value);          //Send PWM value to led
  delay(100);                          //Small delay
  
}

```

- **步骤 2.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤 3.** 通过点击 **Tool-> Serial Monitor** 打开Arduino IDE的 **Serial Monitor** 。或者同事按下 ++ctrl+shift+m++ 。如果一切运行正常，您将会得到A0的输出结果。此外，当您用力按压圆形力传感器时，LED灯将会变亮。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/res/Grove-Round_Force_Sensor_FSR402.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载

- **[Zip]** [Grove-Round Force Sensor(FSR402) eagle file](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/res/Grove-Round_Force_Sensor_FSR402.zip)
- **[Zip]** [Adafruit_NeoPixel-master](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/Adafruit_NeoPixel-master.zip)
- **[PDF]** [Datasheet of FSR402](https://github.com/SeeedDocument/Grove-Round_Force_Sensor_FSR402/raw/master/res/FSR402.pdf)



## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！
