---
name: Grove - Recorder V3
category: Actuator
bzurl:
oldwikiname:
prodimagename: cover.png
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Recorder_v3.0
sku: 107020029
---
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Recorder_V3/master/img/cover.jpg)

这是 Grove-recorder 的最新版本，也是最好的版本，相对上个版本进行了一些更新。

第一个变化是 MCU。 在 V3.0 中，MCU 升级为 ISD9160FI，比旧版 ISD1820PY 更强大。它与新增的 2Mbytes 闪存一起，允许您录音长达 83 秒，比之前的 12 秒录音长得多。

其次，如果您曾经使用过以前的版本，您会知道如果要播放已录制的内容，需要按 Groov 按钮上另一个按钮。 在 V3.0中，我们将记录按钮和播放按钮集成到一个按钮。按住按钮 2 秒，它开始录制，快速按下按钮，它播放已录音的内容。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.7ee3029aN6kF41&id=548475240468)

### V3 版本更新内容

* MCU 从 ISD1820PY 升级到 ISD 9160FI
* 录音和播放按钮集成
* 录音开关
* 2Mbytes flash

## 产品特性

* 录音时间长达 83 秒
* 内置按钮操作
* 内置 LED 指示灯
* 独立或由 MCU 控制
* 内置麦克风

!!!Tip
    更多 Grove 模块的信息请点击 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)

### Platform Support

|Arduino|Wio|BeagleBone|Raspberry Pi|LinkIt|
|---------|-----|-----|------|------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/arduino_logo.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/wio_logo.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/bbg_logo.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/raspberry_pi_logo.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/linkit_logo.jpg)|

## 规格参数

* 工作电压: 3.3/5V
* 工作电流 (@5V, 25℃)
    * 待机: 25-30mA
    * 录音: 29-35mA
    * 播放: 110-150mA
* 工作电流 (@3.3V, 25℃)
    * 待机: 23-25mA
    * 录音: 25-30mA
    * 播放: 70-150mA
* 工作温度: 0~85℃
* 尺寸: 40x20mm
* 重量: 31.5g

## 硬件概述

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Recorder_V3/master/img/hw.png)

1.扬声器接口 - JST2.0

2.麦克风

3.音量旋钮

4.按钮

* 短按按钮：播放
* 长按: 一直播放录音，直到松开按钮

5.Led 指示灯

* 红色 led, 当按钮被按下时亮起

6.Grove 接口

7.REC 开关

* 把开关拨到 ON 位置就可以使用软件控制模块

8.MCU

## 开始使用

在这里，我们将通过一个简单的演示向您展示 Grove - Recorder V3.0 是怎么工作的。首先，您需要准备以下内容：

| Seeeduino V4 | Grove - Recorder | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Recorder_V3/master/img/stuff.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.5d0cd55eL1BrVs&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3e5c146bZiWUJP&id=45505914793)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5f586638hrEBEP&id=520233320144)|


### 硬件连接
由于 Grove 系列模块的优点，您不需要焊接或使用面包板，您需要做的是将模块连接到 Base Shield 的正确端口。对于此演示，我们将 Grove - Recorder 连接到 **D2**。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Recorder_V3/master/img/connection.jpeg)


### 独立使用

这个模块不用编码就可以独立使用。

* **Record** - 按下按钮直到 LED 亮起，此时开始录音。松开按钮停止录音。
* **Play** - 快速按下并松开按钮，播放录音。

如果您想通过代码来控制模块，请继续阅读。

### 软件

把下面的代码复制粘贴到 Arduino IDE，然后上传到 Seeeduino V4。上传到 Arduino 后，打开串口监视器，设置波特率为 115200。

```
/* Grove - Recorder Test Code
+--------------------------------------------------------------------+
|   打开串口监视器，输入命令控制模块：
|   r - 开始录音
|   s - 停止录音
|   p - 播放
+-------------------------------------------------------------------*/

const int pinRec  = 3;
const int pinPlay = 2;

void setup()
{
    Serial.begin(115200);
    Serial.println("Grove - Recorder V3.0 Test Code");
    Serial.println("cmd: \r\nr: record\r\ns: stop recording\r\np: play");

    pinMode(pinRec, OUTPUT);
    pinMode(pinPlay, OUTPUT);
    digitalWrite(pinRec, HIGH);
    digitalWrite(pinPlay, HIGH);
}

void loop()
{
    if(Serial.available())
    {
        char c = Serial.read();
        if(c == 'r')            // 开始录音
        {
            digitalWrite(pinRec, LOW);
            Serial.println("start recording...");
        }
        else if(c == 's')       // 停止录音
        {
            digitalWrite(pinRec, HIGH);
            Serial.println("stop recording...");
        }
        else if(c == 'p')       // 播放
        {
            digitalWrite(pinPlay, LOW);
            delay(100);
            digitalWrite(pinPlay, HIGH);
            Serial.println("play...");
        }
    }
}
```

### 输入命令
你可以往串口监视器中输入以下命令：

* **开始录音** - 输入 'r'
* **停止录音** - 输入 's'
* **播放** - 输入 'p'


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove_Recorder_V3/raw/master/res/eagle.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载

* **[原理图]**[Schematics in PDF](https://github.com/SeeedDocument/Grove_Recorder_V3/raw/master/res/Grove%20-%20Recorder%20v3.0a.pdf)
* **[Eagle 文件]**[Schematics in Eagle](https://github.com/SeeedDocument/Grove_Recorder_V3/raw/master/res/eagle.zip)
