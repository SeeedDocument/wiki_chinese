---
name: ReSpeaker 2-Mics Pi HAT
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html
oldwikiname:
prodimagename:
wikiurl: https://wiki.seeedstudio.com/cn/Respeaker_2-Mics_Pi_HAT
sku: 107100001
---

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/2mics-zero-high-res.jpg?raw=true)

ReSpeaker 2-Mics Pi HAT是专为AI和语音应用设计的Raspberry Pi双麦克风扩展板。 这意味着您可以构建一个集成Amazona语音服务等的功能更强大，更灵活的语音产品。

该板是基于WM8960开发的低功耗立体声编解码器。 电路板两侧有两个麦克风采集声音，还提供3个APA102 RGB LED，1个用户按钮和2个板载Grove接口，用于扩展应用程序。 此外，3.5mm音频插孔或JST 2.0扬声器输出均可用于音频输出。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.14.626377d6xcV1p7&id=553438198956&ns=1&abbucket=5#detail)

!!!Note
      在参考中文wiki的过程中，如果遇到一些疑问，您可以点击页面右上角切换到英文wiki参考，两者有补充。

## 产品特征

* Raspberry Pi兼容（支持Raspberry Pi Zero和Zero W，Raspberry Pi B +，Raspberry Pi 2 B和Raspberry Pi 3 B，Raspberry Pi 4 B，Raspberry Pi 3 B +）
* 2个麦克风
* 2个Grove接口
* 1个自定义按钮
* 3.5mm音频接口
* JST2.0音频输出接口

## 创意应用

* 声音交互应用
* AI助手

## 硬件概述

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/mic_hatv1.0.png?raw=true)

- 按钮：连接到GPIO17的用户自定义按钮
- MIC_L＆MIC_R：左边右边各有一个麦克风
- RGB LED：3个APA102 RGB LED，连接到树莓派的SPI接口
- WM8960：低功耗立体声编解码器
- Raspberry Pi 40针头：支持Raspberry Pi Zero，Raspberry Pi 1 B +，Raspberry Pi 2 B和Raspberry Pi 3 B
- POWER：用于为ReSpeaker 2-Mics Pi HAT供电的Micro USB端口，请在使用扬声器时为电路板供电，以提供足够的电流。
- I2C：Grove I2C端口，连接到I2C-1
- GPIO12：Grove数字端口，连接到GPIO12和GPIO13
- JST 2.0 SPEAKER OUT：用于连接扬声器，JST 2.0连接器
- 3.5mm音频插孔：用于连接带3.5mm音频插头的耳机或扬声器

## 入门指导

### 1. 系统配置与驱动安装

**step 1. 把ReSpeaker 2-Mics Pi HAT插入到Raspberry Pi**

把 ReSpeaker 2-Mics Pi HAT 插入到 Raspberry Pi, 确保插入Raspberry Pi的时候针脚对齐。

!!!Note

    不要在上电的时候，热插拔ReSpeaker 2-Mics Pi HAT.

![connection picture1](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection1.jpg?raw=true)
![connection picture2](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection2.jpg?raw=true)
![connection picture3](https://github.com/yexiaobo-seeedstudio/MIC_HATv1.0_for_raspberrypi/blob/master/img/stack-on-zero.jpg?raw=true)

**step 2. 烧录系统，登陆，换源**

因为当前的Pi内核目前不支持wm8960编解码器，所以我们需要手动构建。

  1. 确保您正在您的Pi上运行[最新的Raspbian操作系统（debian 9）](https://www.raspberrypi.org/downloads/raspbian/)。 *（更新于2018.06.27）*，您可以用etcher进行系统烧录

  2.  您可以用 [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)或者PUTTY连接树莓派，但之前请配置好wifi

  3. 在安装驱动之前，请根据以下流程切换源到清华。

```
pi@raspberrypi ~ $ sudo nano /etc/apt/sources.list
```

用#注释掉原文件内容，用以下内容取代：

```
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
```
**step 3. 驱动下载并安装**
运行下面命令

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard #下载声卡驱动
sudo ./install.sh #安装声卡驱动
reboot  #重启
```

!!!Note

    若驱动安装失败您可以跳转到FAQ的Q1以解决驱动安装失败问题。

**step 4. 检查声卡名称是否与源代码seeed-voicecard相匹配.**

```
pi@raspberrypi:~/seeed-voicecard $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
  Subdevices: 8/8
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
  Subdevice #7: subdevice #7
card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: seeed2micvoicec [seeed-2mic-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0

pi@raspberrypi:~/seeed-voicecard $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: seeed2micvoicec [seeed-2mic-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
pi@raspberrypi:~/seeed-voicecard $
```

### 2. 录音播放测试

  **step 1. 录播测试**
 可以用`arecord`录制，然后用`aplay`播放：(不要忘记插耳机或者喇叭):

```
arecord -f cd -Dhw:1 | aplay -Dhw:1
```

也可以通过audacity软件测试。打开Audacity后，选择 **AC108和2通道** 作为输入，**bcm2835 alsa: - (hw：0，0)** 作为输出来测试：

```
$ sudo apt update
$ sudo apt install audacity
$ audacity                      // 运行 audacity
```

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/audacity.png?raw=true)

**step 2. 调节音量（可跳过）**

**alsamixer** 是用于配置声音设置和调整音量，高级Linux声音体系结构（ALSA）的图形混音器程序。

```bash
pi@raspberrypi:~ $ alsamixer
```

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/alsamixer.png?raw=true)

!!!Note

    首先请用F6选择seeed-2mic的声卡设备。

左和右箭头键用于选择通道或设备，“向上和向下箭头”控制当前所选设备的音量。 退出程序使用ALT + Q或按Esc键。 [More information](https://en.wikipedia.org/wiki/Alsamixer)

### 3. 安装python和虚拟环境

  这样是是为了隔离SDK与系统Python包关系。

```bash

pi@raspberrypi:~ $ cd /home/pi
pi@raspberrypi:~ $ git clone https://github.com/respeaker/4mics_hat.git
pi@raspberrypi:~ $ cd /home/pi/4mics_hat
pi@raspberrypi:~/4mics_hat $ sudo apt install python-virtualenv          # 安装 python2 虚拟环境工具
pi@raspberrypi:~/4mics_hat $ virtualenv --system-site-packages ~/env     # 建立虚拟环境，命名位env,放在~目录下
pi@raspberrypi:~/4mics_hat $ source ~/env/bin/activate                   # 激活虚拟环境
(env) pi@raspberrypi:~/4mics_hat $ pip install spidev gpiozero           # 安装需要的工具包
```

## 控制APA102 LED的示例

每个板载APA102 LED都有一个额外的驱动芯片，驱动芯片设置LED的颜色，然后保持该颜色，直到接收到新的命令。

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/led.gif?raw=true)

  请在执行之前打开SPI，具体步骤如下:

    - 输入： `sudo raspi-config`;
    - 选择 "Interfacing Options";
    - 选择 "SPI";
    - 选择 “Yes”  
    - 选择 “OK”
    - 选择 “Finish”

  配置完后，可以执行下列命令行来运行led示例  
```
cd ~/
git clone https://github.com/respeaker/mic_hat.git
sudo pip install spidev #安装spi的驱动
cd mic_hat
python pixels.py
```

## 如何使用用户自定义按钮

板子上面有个用户自定义按钮，连接到GPIO17. 我们可以调用python和RPi.GPIO来读取状态。

```
sudo pip install rpi.gpio    // install RPi.GPIO library
nano button.py               // copy the following code in button.py
```

```python
import RPi.GPIO as GPIO
import time

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

while True:
    state = GPIO.input(BUTTON)
    if state:
        print("off")
    else:
        print("on")
    time.sleep(1)
```

Save the code as button.py, then run it. It should display "on" when you press the button:

```bash

pi@raspberrypi:~ $ python button.py
off
off
on
on
off

```

## Alexa SDK 和 DuerOs SDK

由于国内登录不上 Google Assisant ，所以使用在国内能连接的 Alexa 和 百度 DuerOs 作为语音引擎，开发出能让大多数人使用的语音互动系统。

### 1. 配置和DOA测试

**step 1. 配置 Voice engine**
```
pi@raspberrypi:~ $ source ~/env/bin/activate                    # 激活Python虚拟环境, 如果已经激活，调到下一步。
(env) pi@raspberrypi:~ $ cd ~/4mics_hat
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install libatlas-base-dev     # 安装 snowboy dependencies
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install python-pyaudio        #安装pyaudio音频处理包
(env) pi@raspberrypi:~/4mics_hat $ pip install ./snowboy*.whl             # 安装 snowboy for KWS
(env) pi@raspberrypi:~/4mics_hat $ pip install ./webrtc*.whl              # 安装 webrtc for DoA
(env) pi@raspberrypi:~ $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/voice-engine/voice-engine #write by seeed
(env) pi@raspberrypi:~ $ cd voice-engine/
(env) pi@raspberrypi:~ $ python setup.py install
(env) pi@raspberrypi:~ $ cd examples
(env) pi@raspberrypi:~ $ nano kws_doa.py
```

**step 2. 修改`kws_doa.py`的第14-21行，以适应 2-Mics：**

```
from voice_engine.doa_respeaker_4mic_array import DOA


def main():
    src = Source(rate=16000, channels=2)
    ch1 = ChannelPicker(channels=2, pick=1)
    kws = KWS()
    doa = DOA(rate=16000)
```
  然后保存退出。

**step 3. 运行**

  在虚拟环境下运行 `python kws_doa.py`。请用 snowboy 来唤醒，我们就可以看到方位的信息。

### 2. 百度中文语音互动或者alexa英文语音互动

**step 1. 配置和安装相关依赖**

```
pi@raspberrypi:~ $ source ~/env/bin/activate                    # activate the virtual, if we have already activated, skip this step
(env) pi@raspberrypi:~ $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/respeaker/avs
(env) pi@raspberrypi:~ $ cd avs                                 # install Requirements
(env) pi@raspberrypi:~ $ python setup.py install                               
(env) pi@raspberrypi:~/avs $ sudo apt install gstreamer1.0
(env) pi@raspberrypi:~/avs $ sudo apt install gstreamer1.0-plugins-good
(env) pi@raspberrypi:~/avs $ sudo apt install gstreamer1.0-plugins-ugly
(env) pi@raspberrypi:~/avs $ sudo apt install python-gi gir1.2-gstreamer-1.0
(env) pi@raspberrypi:~/avs $ pip install tornado
```
**step 2. 取得授权**

在终端运行 `alexa-auth` ，然后登陆获取alexa的授权， 或者运行 `dueros-auth` 获取百度的授权。 授权的文件保存在`/home/pi/.avs.json`。

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/raw/master/img/auth.png)

!!!Note
    如果我们在 `alexa-auth` 和 `dueros-auth`之间切换, 请先删除 `/home/pi/.avs.json` 。 这个是隐藏文件，请用 `ls -la` 显示文件。

**step 2. 配置**

```
(env) pi@raspberrypi:~ $ cd /home/pi
(env) pi@raspberrypi:~ $ git clone https://github.com/respeaker/respeaker_v2_eval.git
(env) pi@raspberrypi:~ $ cd respeaker_v2_eval/alexa
(env) pi@raspberrypi:~/respeaker_v2_eval/alexa $ cp ~/4mics_hat/pixels.py ./pixels.py
(env) pi@raspberrypi:~/respeaker_v2_eval/alexa $ nano ns_kws_doa_alexa.py
```
按照下面的信息更新第15-50行的设置:

```python
    from voice_engine.kws import KWS
    #from voice_engine.ns import NS
    #from voice_engine.doa_respeaker_4mic_array import DOA
    from avs.alexa import Alexa
    from pixels import pixels

    def main():
        logging.basicConfig(level=logging.DEBUG)

        src = Source(rate=16000, channels=2, frames_size=800)
        ch1 = ChannelPicker(channels=2, pick=1)
        #ns = NS(rate=16000, channels=1)
        kws = KWS(model='snowboy')
        #doa = DOA(rate=16000)
        alexa = Alexa()

        alexa.state_listener.on_listening = pixels.listen
        alexa.state_listener.on_thinking = pixels.think
        alexa.state_listener.on_speaking = pixels.speak
        alexa.state_listener.on_finished = pixels.off

        src.link(ch1)
        ch1.link(kws)
        #ch1.link(ns)
        #ns.link(kws)
        kws.link(alexa)

        #src.link(doa)
        def on_detected(keyword):
            #logging.info('detected {} at direction {}'.format(keyword, doa.get_direction()))
            logging.info('detected {}'.format(keyword))
            alexa.listen()

        kws.set_callback(on_detected)
```
![](待替换)

**step 3. 让我们High起来!**

现在请在虚拟环境下运行 `python ns_kws_doa_alexa.py` , 我们会在终端看到很多 debug 的消息. 当我们看到 **status code: 204** 的时候, 请说 `snowboy` 来唤醒 respeaker。接下来 respeaker 上的 led 灯亮起来, 我们可以跟他对话, 比如问，"谁是最帅的?" 或者 "播放刘德华的男人哭吧哭吧不是罪"。小伙伴，尽情的 High 起来吧。


## STT (语音转文字)

本部分将介绍百度STT（语音到文本）功能以及GPIO控件。 这是GPIO配置。 如果您没有风扇，可以在GPIO12 / GPIO13上连接2个LED进行演示。

| GPIO   | Turn On | Faster | Slower | Turn Off |
|--------|---------|--------|--------|----------|
| GPIO12 | 1       | 0      | 1      | 0        |
| GPIO13 | 0       | 1      | 0      | 0        |


**Step 1. 安装依赖**

```
sudo apt install mpg123
pip install baidu-aip monotonic pyaudio
```

**Step 2. 从百度获取key [Here](https://console.bce.baidu.com/ai/?fromai=1#/ai/speech/overview/index).**


**Step 3. 下载源码并执行 [Smart_Fan.py](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/baidu_STT/Smart_fan.py)**

输入下列命令运行代码
```
cd ~
wget https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/baidu_STT.zip
unzip baidu_STT.zip
cd baidu_STT
python Smart_Fan.py
```

!!!Warning
        请在运行 Smart_Fan.py之前添加百度密钥 @ line 36,37,38。 您还可以通过运行synthesis_wav.py来生成所有者的声音。 请在第6,7,8行添加百度密钥，并将字符串修改为您要生成的内容。

**Step 4. 说 '开风扇'.**

**Step 5. 你会看到风扇开启.**

**Step 6. 可以试试 '快一点', '慢一点' 或 '关风扇'.**




## FAQ(疑问解答)


**Q1:严格按照本 wiki 操作，驱动还是安装失败，怎么办？**

A1:如果按照上述方法安装驱动均失败，请点击下载下面镜像

[2018-08-06-raspbian-4GB-for-respeaker](https://v2.fangcloud.com/share/7395fd138a1cab496fd4792fe5?folder_id=188000207913)

![](https://github.com/SeeedDocument/2mics_hat/raw/master/img/image_select.JPG)

请执行下面的步骤：

- 第一， 烧写下载好的镜像，烧了镜像后，记得换源。

- 第二， 如果要使用交互功能之前请命令行输入alexa-auth或dueros-auth申请授权，授权成功后会在 /home/pi目录下生成.avs.json文件，这时才能使用交互功能。

- 第三，/home/pi目录下会有 respeaker的例程文件夹,可以根据用的mic不同而使用相应的例程。但是请烧录系统后在respeaker目录下更新下例程，可以在respeaker目录下执行``` git pull origin master ```命令来更新。

**Q2: #include "portaudio.h" Error when run "sudo pip install pyaudio".**

A2: 命令行输入如下命令

```
sudo apt-get install portaudio19-dev
```


**Q3 关于安装snowboy时出现不适合该平台的警告提醒**

A3: 目前snowboy只能兼容python2，所以通过在安装python的虚拟环境时，请确保是python2

**Q4 有时候 sudo python file.py 时候会出现依赖问题**

A4:测试时发现sudo执行时候默认从系统环境执行，而wiki中用到的依赖都是装在~/env 下的，可以通过 ```sudo  ~/env/bin/python file.py```来解决


**Q5 可以通过3.5毫米音频插孔的播放来听到声音，但是在运行ns_kws_doa_alexa_with_light.py时听不到声音**

 A5： 我们有3个播放器（mpv，mpg123和gstreamer）可以使用。 mpg123更适合语音识别和唤醒更，它更具响应性； 而AudioPlayer 更适用gstreamer> mpv> mpg123。 Gstreamer支持更多音频格式，并且在raspberry pi上运行良好。 我们还可以使用环境变量PLAYER指定AudioPlayer的播放器。 所以请尝试以下命令启用语音。
```

  sudo apt install mpg123
  PLAYER=mpg123 python ns_kws_doa_alexa_with_light.py
```

**Q6 在运行语音交互时候喊 snowboy 没反应**

A6:请运行audacity以确保4个频道良好。 如果有一个没有数据的频道，当我们说snowboy时就没有回复。

## 资源下载
- **[Eagle]** [Respeaker_2_Mics_Pi_HAT_SCH](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_SCH.zip)
- **[Eagle]** [Respeaker_2_Mics_Pi_HAT_PCB](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_PCB.zip)
- **[PDF]** [Respeaker_2_Mics_Pi_HAT_SCH](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_SCH.pdf)
- **[PDF]** [Respeaker_2_Mics_Pi_HAT_PCB](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_PCB.pdf)
