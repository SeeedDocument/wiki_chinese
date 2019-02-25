---
name: Grove - Speech Recognizer
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Speech-Recognizer-p-2708.html
oldwikiname:
prodimagename: cover.png
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Voice_Recognizer
sku: 101020232
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Speech_Recognizer/master/img/cover.jpg)

使用声音与您周围的事物进行交互，这是IOT应用中最有趣的事情之一，我们期望让这变得更加与众不同和炫酷。最近，我们刚刚在 Kickstarter 上隆重推出了 “Respeaker” 语音控制解决方案。然而，并非每个人都需要用 Respeaker 来建立语音控制项目，有时候人们仅仅需要一个简单的解决方案，在此里我们向您介绍第一代 Grove 语音识别器，它可以轻松快速地实现智能家居的梦想。

Grove speech recognizer 是专门为语音控制应用而设计的，如智能家居，智能玩具，语音控制机器人，任何您想要通过语音控制的任何东西，它值得一试。该板包括 Nuvoton ISD9160，麦克风，1 个 SPI flash，1 个 Grove 连接器，1 个扬声器连接器和 1 个指示您的声音的 led。

Nuvoton ISD9160 是基于 Cortex™-M0 的 (SoC) Chipcorder，它为语音控制应用提供了强大的解决方案。ISD9160 不是这个 Grove 模块里唯一令人惊喜的事情，让我们来看看麦克风吧！还记得必须直接地并且尽可能的接近语音识别设备发声，以确保它可以识别，这样的令您非常不舒服的体验吗？这次不会再发生！Grove speech recognizer 上的麦克风是全方位无死角的，这意味着无论用户是从前面，后面，左侧还是右侧向麦克风说话，麦克风将以相等的增益记录信号。

该语音识别器可以识别 22 种命令，包括“start”，“stop”，“play music”等。每当它识别到一个命令时，它将返回一个值，然后与其连接的扬声器将重复命令。该值可用于控制其他设备，如电机，音乐播放器。为了确保它具有高识别率和非常低的误触发，我们已经测试了好几个小时。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.16.4ce6f5cfOyem3s&id=548511321007)

使用须知 :
唤醒词 : Hicell (请将它发音为一个单词)。
当它识别到唤醒词时，LED变成红色，然后您可以说出命令字，如果它识别命令字，LED将变成蓝色。


!!!Note
    该模块的固件是由第三方写的，它不是开源的。该模块暂时只支持英文，因此您的命令也只能是英文。

## 创意应用

* 物联网
* 智能住宅
* 人机界面
* 灯光控制
* 传感器中枢
* 机器人

## 产品特性

* 本地语音识别
* 非常低的误触发率
* 扬声器连接器( JST2.0，扬声器不包括)
* 内置麦克风
* 3.3/5V 工作电压
* 22 个识别项
* 默认波特率 : 9600

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


## Platform Support



## 规格参数

| 项目  |	最小值	|典型值	| 最大值	| 条件 |
|---|-------|-----|--------|-----------|
| 工作电压 |3V	    |3.3V	|5V	|25 ℃|
|工作电流  |25mA   |26.5mA |80mA@playing	|VCC = 3.3V 25℃|
|工作电流  |	25mA |	26.5mA	|130mA@playing|	VCC = 5V 25℃|
|工作温度|	0℃	|25℃	|85℃	| |
|尺寸	| |	40*20mm		| | |
|质量	| |	5g		| |
|Flash	| |	2Mbytes	| |
|麦克风灵敏度 |-43dB | -40dB | -37dB | VCC = 5V 25℃ |
|麦克风 SNR | 58dB  || | |
|麦克风方向性 | |全方向 | | |
|扬声器功率| | |1W	|VCC = 5V 25℃|
|处理器 core| |Cortex-M0| | |
|处理器频率 | |32.768MHz|50MHz|VCC = 5V 25℃|


## 硬件概述

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Speech_Recognizer/master/img/hw.png)

1. Grove 接口
2. Red Led - 识别到唤醒词时发光
3. Blue Led - 识别到命令字时发光
4. Speaker Connector - 连接扬声器来获得语音反馈
5. 麦克风
6. ISD9160CFI

## 命令返回值

| 命令 | 返回值 |
|-------------|--------|
|Turn on the light	|1|
|Turn off the light	|2|
|Play music	|3|
|Pause 	|4|
|Next 	|5|
|Previous 	|6|
|Up 	|7|
|Down	|8|
|Turn on the TV	|9|
|Turn off the TV	|10|
|Increase temperature	|11|
|Decrease temperature	|12|
|What’s the time	|13|
|Open the door	|14|
|Close the door	|15|
|Left	|16|
|Right 	|17|
|Stop 	|18|
|Start	|19|
|Mode 1	|20|
|Mode 2	|21|
|Go	|22|

## 入门指导

在这里，我们将通过一个简单的演示向您展示 Grove - Speech Recognizer 的工作原理。 首先需要准备下面的东西 :

| Seeeduino V4 | Grove - Speech Recognizer | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Speech_Recognizer/master/img/stuff1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=2013.1.0.0.5f5a7ac1YZl1kj&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.16.4ce6f5cfOyem3s&id=548511321007)|[点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.21.7f6fe412Eloh8F&id=520233320144&ns=1&abbucket=1#detail)|


**硬件连接**

由于 Grove 系列模块的优点，您不需要焊接或面包板，您只需要将模块连接到 Base Shield 的正确端口。在这个演示中，我们将 Grove - Speech Recognizer 连接到 **D2**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Speech_Recognizer/master/img/connect.jpeg)


**软件部分**

复制下面的代码并粘贴到您的 Arduino IDE，并上传到您的 Seeeduino V4。将代码上传后，打开串口监视器。

```
#include <SoftwareSerial.h>

#define SOFTSERIAL_RX_PIN  2
#define SOFTSERIAL_TX_PIN  3

SoftwareSerial softSerial(SOFTSERIAL_RX_PIN,SOFTSERIAL_TX_PIN);

const char *voiceBuffer[] =
{
    "Turn on the light",
    "Turn off the light",
    "Play music",
    "Pause",
    "Next",
    "Previous",
    "Up",
    "Down",
    "Turn on the TV",
    "Turn off the TV",
    "Increase temperature",
    "Decrease temperature",
    "What's the time",
    "Open the door",
    "Close the door",
    "Left",
    "Right",
    "Stop",
    "Start",
    "Mode 1",
    "Mode 2",
    "Go",
};

void setup()
{
    Serial.begin(9600);
    softSerial.begin(9600);
    softSerial.listen();
}

void loop()
{
    char cmd;

    if(softSerial.available())
    {
        cmd = softSerial.read();
        Serial.println(voiceBuffer[cmd - 1]);
    }
}

```

**唤醒模块**

当有命令 **Hicell** 时，模块会唤醒，然后红灯亮。红灯熄灭后再试试。

!!!Note
    红色 LED 将持续5秒。如果在命令被识别之前红灯熄灭，再次尝试唤醒。

**命令**

模块被唤醒后，您可以发布命令，比如 :

    "turn on the TV"
如果蓝色指示灯是亮的(持续约 1 秒)，则表示该指令被正确识别。检查串口监视器，命令被打印在上面。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Speech_Recognizer/master/img/monitor.png)


## 资源下载

* **[Eagle文件]** [Schematics in Eagle](https://github.com/SeeedDocument/Grove_Speech_Recognizer/raw/master/res/eagle.zip)
* **[原理图PDF]** [Schematics in PDF](https://github.com/SeeedDocument/Grove_Speech_Recognizer/raw/master/res/Grove%20-%20Speech%20Recognizer%20v1.0.pdf)
