---
title: Grove - Vibration Sensor (SW-420)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020586
tags:
---

![](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/img/main.jpg)



Grove - Vibration Sensor (SW-420) 是一个高敏感度的非定向的振动传感器。 当模块处于稳定状态下，电路被打开且输出处于高电平状态。当出现移动或是振动时，电路会短暂地断开且输出变低。 并且，您可以根据自己的需求将模块的灵敏度设置调高或者调低。

总之，它是感知振动或者倾斜的绝佳模块。


<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-Vibration-Sensor-%28SW-420%29-p-3158.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>



## 产品特性

- 非定向
- 高灵敏度
- 可感知振动和倾斜
- 防水 
- 耐压


## 规格参数

|项目|数值|
|---|---|
|工作电压|3.3V / 5V|
|接口|数字型|


## 应用场景

- 汽车，自行车，摩托车的防盗警报
- 游戏控制
- 振动监测

## 硬件概述

### 引脚定义

![](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/img/pin_map_cn.png)


### 原理图
![](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/img/Schematic.jpg)



首先，让我们关注左下角的 **SW1**。实际上，**SW1** 就是振动检测模块 **SW-420**。当模块处于稳定状态时，模块被打开。**U1A** 上的引脚2通过 **SW1** 连接到 **GND**。


**VR1** 是电位器，电位器的引脚2连接到 **U1A** 的引脚3上


**U1A** 是[比较器](https://en.wikipedia.org/wiki/Comparator)。对比较器来说， 


$$
V_{out} = 
\begin{cases} 
High,  & \mbox{if }V_+ > V_-  \\
Low,  & \mbox{if }V_+ < V_- 
\end{cases}
$$

**V+** 连接到 **引脚3** , **V-** 连接到 **引脚2**， **V<sub>out</sub>** 连接到 **引脚1**.


你可以通过旋转电位器来调整 **V+**。比如说，可以通过调整使它变成$VCC/2$


而 **V-** 由 **SW1(SW-420)** 而决定：


- 若模块处于稳定状态， **SW1** 被打开， **U1A** 的 **引脚2** 通过 **SW1** 连接到 **GND**。会变成：

$$
\left. \begin{array}{l}  & V- = 0V \\ & V+ = VCC/2 \end{array} \right\}  V_{out} = High
$$

- 若模块感知到振动或者倾斜， **SW1** 会关闭， **V-** 的电压会经由R1提升到 **VCC**。当 **V-** 的电压高于 VCC/2，那么：

$$
\left. \begin{array}{l}  & V- > VCC/2 \\ & V+ = VCC/2 \end{array} \right\}  V_{out} = Low
$$


现在您可通过设置 **V+** 来调整传感器的灵敏度了。只需明白： **V+** 的电压越低，传感器的灵敏度越高😆


## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg)  |


!!!Caution
    以上列出的支持平台仅代表硬件和理论的兼容性。大部分情况下我们仅提供 Arduino 平台的软件库和代码示例。为所有的MCU平台提供软件库和示例代码是不可能的。因此，使用者可能需要写出自己使用的软件库。



## 入门指导


### 搭配 Arduino 一起使用


#### 硬件连接

**材料需求**

| Seeeduino V4.2 | Base Shield | Grove - Vibration Sensor|Grove - Buzzer|
|--------------|-------------|-----------------|----|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/img/thumbnail.jpg)|![](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/img/buzzer_s.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-Vibration-Sensor-%28SW-420%29-p-3158.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-Buzzer-p-768.html" target="_blank">点击购买</a>|


!!!note
    **1** 请小心插入USB线缆，否则您可能会损坏端口。请使用4线的USB线缆，2线的USB线缆无法传输数据。若果您不确定您拥有的是哪种USB线缆，可以[点击此处](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)购买。
    
    **2** 在您购买时，每个 Grove 模块都附带一根 Grove 线缆。若您丢失了该线缆，可以[点击此处](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)购买。



- **步骤一** 将 Grove - Vibration Sensor (SW-420) 连接到扩展板的 **D2** 端口上。

- **步骤二** 将 Grove - Buzzer 连接到扩展板的 **D3** 端口上。

- **步骤三** 将 Grove - Base Shield 插在 Seeeduino 上。

- **步骤四** 通过USB线缆将 Seeeduino 连接到您的电脑。

![](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/img/connect.JPG)

!!!Note
        如果您没有 Grove Base Shield，您也可以按照以下方式将此模块连接到 Seeeduino 上



| Seeeduino     |  Grove - Vibration Sensor         |
|---------------|-------------------------|
| 5V            | 红色                     |
| GND           | 黑色                   |
| NC           | 白色                    |
| D2           | 黄色                   |



| Seeeduino     |  Grove - Buzzer         |
|---------------|-------------------------|
| 5V            | 红色                     |
| GND           | 黑色                   |
| NC           | 白色                    |
| D3           | 黄色                   |


#### 软件运行

!!!Note
        如果这是您第一次使用 Arduino， 我们强烈推荐您在开始之前阅读[Arduino 入门](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。


- **步骤一** 打开您的 Arduino IDE，新建一个文件

- **步骤二** 复制以下所有代码，您也可以点击代码块右上角的图标![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg)将这些代码复制到您创建的新文件中去

```C++
// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int buzzer =  3;      // the number of the buzzer pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(buzzer, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(buzzer, LOW);
  } else {
    // turn LED off:
    digitalWrite(buzzer, HIGH);
  }
}
```

- **步骤三** 上传您的代码。若您不知道如何上传，请阅读文章 [如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

!!!success
    若以上一切顺利，在您每次移动，摇晃或者倾斜 Grove - Vibration Sensor 的时候，Grove - buzzer 会发出声音。


## 资源下载

- **[Zip]** [Grove - Vibration Sensor (SW-420) 原理图文件](https://github.com/SeeedDocument/Grove-Vibration_Sensor-SW-420/raw/master/res/Grove%20-%20Vibration%20Sensor%20(SW-420)%20v1.1.zip)



## 项目

这是本产品的介绍视频，有简单代码展示，您可以一试。

<iframe width="560" height="315" src="https://www.youtube.com/embed/oFmvKxoZIuw?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



## 技术支持
欢迎您将您的问题提交至我们的[论坛](https://forum.seeedstudio.com/)。