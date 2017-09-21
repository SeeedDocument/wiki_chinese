---
title: Respeaker 4-Mic Array
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-4-Mic-Array-for-Raspberry-Pi-p-2941.html
oldwikiname:
prodimagename:
wikiurl: https://seeed.wiki/Respeaker_4-Mics_Pi_HAT
sku: 103030216
---

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/overview.jpg?raw=true)

基于Raspberry Pi的ReSpeaker 4-Mic阵列是一款适用于AI和语音应用的Raspberry Pi的四通道麦克风扩展板。 这意味着您可以借助它构建一个集成Amazon Alexa语音服务，Google助手等，功能更强大，更灵活的语音产品。

区别于 [ReSpeaker 2-Mics Pi HAT](https://item.taobao.com/item.htm?spm=a1z10.1-c.w13838425-11172345252.1.542035bczDBegW&id=557884254210), 该板是基于AC108开发的，这是一款高度集成四通道ADC，具有用于高清晰度语音捕获，I2S / TDM输出，拾取3米半径的声音的语音设备。 此外，这款4-Mics版本提供了超酷LED环，其中包含12个APA102可编程LED。 就像Amazon Echo或 Google assist一样， 使用4个麦克风和LED环，Raspberry Pi具有VAD（语音活动检测），DOA（到达方向），KWS（关键字搜索），并通过LED环显示方向灯功能。

[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png)](https://www.seeedstudio.com/ReSpeaker-4-Mic-Array-for-Raspberry-Pi-p-2941.html)

## 产品特征

* Raspberry Pi兼容（支持Raspberry Pi Zero和Zero W，Raspberry Pi B +，Raspberry Pi 2 B和Raspberry Pi 3 B）
* 4个麦克风
* 3米半径的语音捕捉
* 2 Grove接口
* 12 APA102用户指示灯
* 软件算法：VAD（语音活动检测），DOA（到达方向）和KWS（关键词搜索）

!!!Note
        ReSpeaker 4-Mic Array没有任何音频输出接口, 它只用于语音捕获。 您可以使用Raspberry Pi上的[耳机插孔](https://www.raspberrypi.org/documentation/configuration/audio-config.md)进行音频输出。


## 创意应用

* 声音交互应用
* AI助手

## 硬件概述

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/features.png?raw=true)

- MIC：4个模拟麦克风
- LED：12个APA102可编程RGB LED，连接到SPI接口
- Raspberry Pi 40针头：支持Raspberry Pi Zero，Raspberry Pi 1 B +，Raspberry Pi 2 B和Raspberry Pi 3 B
- AC108：具有I2S / TDM输出转换功能的高度集成的四通道ADC
- I2C：Grove I2C端口，连接到I2C-1
- GPIO12：Grove数字端口，连接到GPIO12和GPIO13

!!!Note
        如果要使用APA102 RGB LED，请先将高电平写入“GPIO5”，给LED的VCC供电。

## 入门指导

### 把 ReSpeaker 4-Mic Array 插入到 Raspberry Pi

把 ReSpeaker 4-Mic Array 插入到 Raspberry Pi, 确保插入Raspberry Pi的时候针脚对齐。

!!!Note
        不要在上电的时候，热插拔ReSpeaker 4-Mic Array

![connection pic1](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/connect1.jpg?raw=true)
![connection pic2](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/connect2.jpg?raw=true)

### 安装驱动

因为当前的Pi内核目前不支持AC108编解码器，所以我们需要手动构建。
确保您正在您的Pi上运行[最新的Raspbian操作系统（debian 9）](https://www.raspberrypi.org/downloads/raspbian/)。 *（更新于2017.09.15）*
根据以下流程安装驱动：


```
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh 4mic
reboot
```

然后选择Raspberry Pi上的耳机插孔进行音频输出：

```
sudo raspi-config
# Select 7 Advanced Options
# Select A4 Audio
# Select 1 Force 3.5mm ('headphone') jack
# Select Finish
```

检查声卡名称如下所示：

```
pi@raspberrypi:~/seeed-voicecard $ arecord -L
null
    Discard all samples (playback) or generate zero samples (capture)
playback
capture
dmixed
array
ac108
default:CARD=seeed4micvoicec
    seeed-4mic-voicecard,
    Default Audio Device
sysdefault:CARD=seeed4micvoicec
    seeed-4mic-voicecard,
    Default Audio Device
dmix:CARD=seeed4micvoicec,DEV=0
    seeed-4mic-voicecard,
    Direct sample mixing device
dsnoop:CARD=seeed4micvoicec,DEV=0
    seeed-4mic-voicecard,
    Direct sample snooping device
hw:CARD=seeed4micvoicec,DEV=0
    seeed-4mic-voicecard,
    Direct hardware device without any conversions
plughw:CARD=seeed4micvoicec,DEV=0
    seeed-4mic-voicecard,
    Hardware device with all software conversions
```

如果要更改alsa设置，可以使用`sudo alsactl --file=ac108_asound.state store`保存。 当你需要再次使用这些设置时，将它复制到：`sudo cp ./ac108_asound.state /var/lib/alsa/asound.state`


打开Audacity，选择 **AC108和4通道** 作为输入，**bcm2835 alsa: - (hw：0，0)** 作为输出来测试：

```
$ sudo apt update
$ sudo apt install audacity
$ audacity                      // 运行 audacity
```

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/audacity.png?raw=true)

或者你可以用`arecord`录制，然后用`aplay`播放：

```
arecord -Dac108 -f S32_LE -r 16000 -c 4 hello.wav    // 只支持4通道
aplay hello.wav                                      // 确保选择默认设备
                                                     // 声音通过树莓派的aux输出
```

### 如何使用板载APA102 LED

每个板载APA102 LED都有一个额外的驱动芯片，驱动芯片设置LED的颜色，然后保持该颜色，直到接收到新的命令。

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/rainbow.jpg?raw=true)

- 打开SPI: 
    - 输入： `sudo raspi-config`; 
    - 选择 "Interfacing Options"; 
    - 选择 "SPI"; 
    - 选择 “Yes”  
    - 选择 “OK”
    - 选择 “Finish”

- 控制APA102 LED的示例 

```
pi@raspberrypi:~ $ cd /home/pi
pi@raspberrypi:~ $ git clone https://github.com/respeaker/4mics_hat.git
pi@raspberrypi:~ $ cd /home/pi/4mics_hat
pi@raspberrypi:~ $ sudo apt install python-virtualenv          # 安装 python 虚拟环境
pi@raspberrypi:~ $ virtualenv --system-site-packages ~/env     # 创建 python 虚拟环境
pi@raspberrypi:~ $ source ~/env/bin/activate                   # 激活 python 虚拟环境
(env) pi@raspberrypi:~ $ pip install spidev gpiozero           # 安装 spidev 和 gpiozero
```

- 运行 `python pixels.py`, 你可以看到LED像Google Assistant灯光一样闪烁。

### ReSpeaker 4-Mic Array的DOA功能

使用DoA（到达方向）功能，ReSpeaker 4-Mic Array能够找到声源所在的方向。

```
pi@raspberrypi:~ $ source ~/env/bin/activate                    # 激活Python虚拟环境, 如果已经激活，调到下一步。
(env) pi@raspberrypi:~ $ cd ~/4mics_hat
(env) pi@raspberrypi:~ $ sudo apt install libatlas-base-dev     # 安装 snowboy dependencies
(env) pi@raspberrypi:~ $ sudo apt install python-pyaudio
(env) pi@raspberrypi:~ $ pip install ./snowboy*.whl             # 安装 snowboy for KWS
(env) pi@raspberrypi:~ $ pip install ./webrtc*.whl              # 安装 webrtc for DoA
(env) pi@raspberrypi:~ $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/voice-engine/voice-engine
(env) pi@raspberrypi:~ $ cd voice-engine/
(env) pi@raspberrypi:~ $ python setup.py install
(env) pi@raspberrypi:~ $ cd examples
(env) pi@raspberrypi:~ $ nano kws_doa.py
```

然后修改`kws_doa.py`的第14-21行，以适应4-Mics：

```
from voice_engine.doa_respeaker_4mic_array import DOA


def main():
    src = Source(rate=16000, channels=4)
    ch1 = ChannelPicker(channels=4, pick=1)
    kws = KWS()
    doa = DOA(rate=16000)
```
保存，退出，然后运行 `python kws_doa.py`

## 资源下载

- **[PDF 原理图]** [ReSpeaker 4-Mic Array for Raspberry Pi(PDF)](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/src/ReSpeaker%204-Mic%20Array%20for%20Raspberry%20Pi%20%20v1.0.pdf)