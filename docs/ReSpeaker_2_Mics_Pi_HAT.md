---
title: ReSpeaker 2-Mics Pi HAT
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html
oldwikiname:
prodimagename:
wikiurl: https://wiki.seeedstudio.com/cn/Respeaker_2-Mics_Pi_HAT
sku: 107100001
---

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/2mics-zero-high-res.jpg?raw=true)

ReSpeaker 2-Mics Pi HAT是专为AI和语音应用设计的Raspberry Pi双麦克风扩展板。 这意味着您可以构建一个集成Amazon Amazona语音服务，Google助手等的功能更强大，更灵活的语音产品。

该板是基于WM8960开发的低功耗立体声编解码器。 电路板两侧有两个麦克风采集声音，还提供3个APA102 RGB LED，1个用户按钮和2个板载Grove接口，用于扩展应用程序。 此外，3.5mm音频插孔或JST 2.0扬声器输出均可用于音频输出。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.14.626377d6xcV1p7&id=553438198956&ns=1&abbucket=5#detail)

## 产品特征

* Raspberry Pi兼容（支持Raspberry Pi Zero和Zero W，Raspberry Pi B +，Raspberry Pi 2 B和Raspberry Pi 3 B）
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

### 把ReSpeaker 2-Mics Pi HAT插入到Raspberry Pi

把 ReSpeaker 2-Mics Pi HAT 插入到 Raspberry Pi, 确保插入Raspberry Pi的时候针脚对齐。

!!!Note
    不要在上电的时候，热插拔ReSpeaker 2-Mics Pi HAT.

![connection picture1](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection1.jpg?raw=true)
![connection picture2](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/connection2.jpg?raw=true)
![connection picture3](https://github.com/yexiaobo-seeedstudio/MIC_HATv1.0_for_raspberrypi/blob/master/img/stack-on-zero.jpg?raw=true)

### 安装驱动

因为当前的Pi内核目前不支持wm8960编解码器，所以我们需要手动构建。

#### 1. 确保您正在您的Pi上运行[最新的Raspbian操作系统（debian 9）](https://www.raspberrypi.org/downloads/raspbian/)。 *（更新于2017.09.15）*

#### 2. 根据以下流程安装驱动：

在安装驱动之前，请根据以下流程切换源到清华。

```
pi@raspberrypi ~ $ sudo nano /etc/apt/sources.list
```

用#注释掉原文件内容，用以下内容取代：

```
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
```

然后运行下面命令

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh
reboot
```

#### 3. 检查声卡名称是否与源代码seeed-voicecard相匹配.

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

####  4. 可以用`arecord`录制，然后用`aplay`播放：(不要忘记插耳机或者喇叭):

```
arecord -f cd -Dhw:1 | aplay -Dhw:1
```


### 用alsamixer配置声音设置和调整音量

**alsamixer** 是用于配置声音设置和调整音量，高级Linux声音体系结构（ALSA）的图形混音器程序。

```
pi@raspberrypi:~ $ alsamixer
```

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/alsamixer.png?raw=true)

!!!Note
    首先请用F6选择seeed-2mic的声卡设备。

左和右箭头键用于选择通道或设备，“向上和向下箭头”控制当前所选设备的音量。 退出程序使用ALT + Q或按Esc键。 [More information](https://en.wikipedia.org/wiki/Alsamixer)


## 让我们开始来玩 **Google Assistant**

!!!Warning
    因为我们在中国，无法直接使用Google的服务。必须搭建可以访问google的路由器，然后连接到路由。


在开始使用[Google Assistant](https://assistant.google.com/)之前，首先您应该将Google Assistant Library整合到您的raspberry pi系统中。 以下是[Google官方指导](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/run-sample)的链接。


以下指南还将向您介绍如何开始使用Google助手。

### 1. 配置开发人员项目，并获取JSON文件

请根据[指南](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/config-dev-project-and-account#config-dev-project) 第一步到第四步在Google Cloud Platform上配置项目，并创建一个OAuth Client ID JSON文件。 不要忘记将JSON文件复制到您的Raspberry Pi。

### 2. 使用Python虚拟环境，隔离SDK与系统Python包关系。

```
sudo apt-get update
sudo apt-get install python3-dev python3-venv # Use python3.4-venv if the package cannot be found.
python3 -m venv env
env/bin/python -m pip install --upgrade pip setuptools
source env/bin/activate
```

### 3. 安装google-assistant-library

Google Assistant SDK软件包，包含在设备上运行Google Assistant所需的所有代码，包括库和示例代码。 使用pip在虚拟环境中安装最新版本的Python包：

```
(env) $ python -m pip install --upgrade google-assistant-library
```

### 4. 授权Google Assistant SDK

授权Google Assistant SDK，使Google Assistant对给定的Google帐户进行查询。 把步骤1中的JSON文件复制到树莓派/home/pi下。

```
pi@raspberrypi:~ $ google-oauthlib-tool --client-secrets /home/pi/client_secret_client-id.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless
```

**/home/pi/client_secret_client-id.json** 是你的JSON文件的路径，确保Json文件的名字匹配。 运行命令后，应该显示如下所示。 复制URL并将其粘贴到浏览器中（这可以在您的树莓派或任何其他电脑上完成）。 同意后，您的浏览器将显示代码，例如“4 / XXXX”。 复制并将此代码粘贴到终端中。

```
Please go to this URL: https://...
Enter the authorization code:
```

这个时候应该显示: OAuth credentials initialized. 如果显示: InvalidGrantError then an invalid code was entered. 请重试, 确保拷贝整个code.

### 5. 安装 **pulseaudio** 并且让他在后台运行

```
pi@raspberrypi:~ $ sudo apt install pulseaudio
pi@raspberrypi:~ $ pulseaudio &
[1] 1244
pi@raspberrypi:~ $ W: [pulseaudio] server-lookup.c: Unable to contact D-Bus: org.freedesktop.DBus.Error.NotSupported: Unable to autolaunch a dbus-daemon without a $DISPLAY for X11
W: [pulseaudio] main.c: Unable to contact D-Bus: org.freedesktop.DBus.Error.NotSupported: Unable to autolaunch a dbus-daemon without a $DISPLAY for X11
E: [pulseaudio] bluez4-util.c: org.bluez.Manager.GetProperties() failed: org.freedesktop.DBus.Error.UnknownMethod: Method "GetProperties" with signature "" on interface "org.bluez.Manager" doesn't exist
```

!!!Note
    请忽略pulseaudio错误信息。

### 6. 开始使用Google Assistant示例

```
pi@raspberrypi:~ $ alsamixer    // To adjust the volume
pi@raspberrypi:~ $ source env/bin/activate
(env) pi@raspberrypi:~ $ env/bin/google-assistant-demo
```

### 7. 唤醒Google Assistant

先说 *Ok Google* 或者 *Hey Google*, 然后说您的询问. 语音助手就会响应您的问题。如果语音助手没有响应， 请按照 [疑难解答说明](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/troubleshooting#hotword).

![run demo](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/okgoogle.jpg?raw=true)

### 8. 常见问题解决方法

如果您遇到问题，请参考 [常见疑难解答说明](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/troubleshooting) 。


### 如何使用板载APA102 LED

每个板载APA102 LED都有一个额外的驱动芯片，驱动芯片设置LED的颜色，然后保持该颜色，直到接收到新的命令。

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/led.gif?raw=true)

#### 1. 打开SPI:
    - 输入： `sudo raspi-config`;
    - 选择 "Interfacing Options";
    - 选择 "SPI";
    - 选择 “Yes”  
    - 选择 “OK”
    - 选择 “Finish”

#### 2. 控制APA102 LED的示例

```
cd ~/
git clone https://github.com/respeaker/mic_hat.git
sudo pip install spidev
cd mic_hat
python pixels.py
```

### 如何使用用户自定义按钮

板子上面有个用户自定义按钮，连接到GPIO17. 我们可以调用python和RPi.GPIO来读取状态。

```
sudo pip install rpi.gpio    // install RPi.GPIO library
nano button.py               // copy the following code in button.py
```

```
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

```
pi@raspberrypi:~ $ python button.py
off
off
on
on
off
```

### 用按钮来触发Google Assisant

您可以用按键来代替"ok google"来激活Google Assisant.

- 更新  `pushtotalk.py`

```
cd /usr/local/lib/python2.7/dist-packages/googlesamples/assistant/grpc
sudo nano pushtotalk.py
```

请到文件第301行, 然后根据下面的code来更新。  

```Python
    with SampleAssistant(conversation_stream,
                         grpc_channel, grpc_deadline) as assistant:
        # If file arguments are supplied:
        # exit after the first turn of the conversation.
        if input_audio_file or output_audio_file:
            assistant.converse()
            return

        # If no file arguments supplied:
        # keep recording voice requests using the microphone
        # and playing back assistant response using the speaker.
        # When the once flag is set, don't wait for a trigger. Otherwise, wait.
        wait_for_user_trigger = not once
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.IN)
        while True:
            if wait_for_user_trigger:
                state = GPIO.input(17)
                logging.info('Press the button to send a new request...')
                if state:
                    continue
                else:
                    pass
               # click.pause(info='Press Enter to send a new request...')
            continue_conversation = assistant.converse()
            # wait for user trigger if there is no follow-up turn in
            # the conversation.
            wait_for_user_trigger = not continue_conversation

            # If we only want one conversation, break.
            if once and (not continue_conversation):
                break


if __name__ == '__main__':
    main()
```

- 运行下面程序来进行测试:

```
$ googlesamples-assistant-pushtotalk
```

- 程序运行的结果如下图所示:

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/button.jpg?raw=true)


## 使用 Alexa 和 DuerOs

由于国内登录不上 Google Assisant ，所以使用在国内能连接的 Alexa 和 百度 DuerOs 作为语音引擎，开发出能让大多数人使用的语音互动系统。

### ReSpeaker 2-Mics Pi HAT 的 DOA 功能

使用DoA（到达方向）功能，ReSpeaker 2-Mics Pi HAT 能够找到声源所在的大概方向。

#### 1. 配置 Voice engine
```
pi@raspberrypi:~ $ source ~/env/bin/activate                    # 激活Python虚拟环境, 如果已经激活，调到下一步。
(env) pi@raspberrypi:~ $ cd ~/4mics_hat
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install libatlas-base-dev     # 安装 snowboy dependencies
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install python-pyaudio
(env) pi@raspberrypi:~/4mics_hat $ pip install ./snowboy*.whl             # 安装 snowboy for KWS
(env) pi@raspberrypi:~/4mics_hat $ pip install ./webrtc*.whl              # 安装 webrtc for DoA
(env) pi@raspberrypi:~ $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/voice-engine/voice-engine
(env) pi@raspberrypi:~ $ cd voice-engine/
(env) pi@raspberrypi:~ $ python setup.py install
(env) pi@raspberrypi:~ $ cd examples
(env) pi@raspberrypi:~ $ nano kws_doa.py
```

#### 2. 修改`kws_doa.py`的第14-21行，以适应 2-Mics：

```
from voice_engine.doa_respeaker_4mic_array import DOA


def main():
    src = Source(rate=16000, channels=2)
    ch1 = ChannelPicker(channels=2, pick=1)
    kws = KWS()
    doa = DOA(rate=16000)
```

#### 3. 保存，退出，然后在虚拟环境下运行 `python kws_doa.py`。请用 snowboy 来唤醒，我们就可以看到方位的信息。

### 用百度来进行语音互动

#### 1. 百度授权

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
用 [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)连接树莓派, 在终端运行 `alexa-auth` ，然后登陆获取alexa的授权， 或者运行 `dueros-auth` 获取百度的授权。 授权的文件保存在`/home/pi/.avs.json`。

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/raw/master/img/auth.png)

!!!Note
    如果我们在 `alexa-auth` 和 `dueros-auth`之间切换, 请先删除 `/home/pi/.avs.json` 。 这个是隐藏文件，请用 `ls -la` 显示文件。

#### 2. 配置

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

#### 3. 让我们High起来!

现在请在虚拟环境下运行 `python ns_kws_doa_alexa.py` , 我们会在终端看到很多 debug 的消息. 当我们看到 **status code: 204** 的时候, 请说 `snowboy` 来唤醒 respeaker。接下来 respeaker 上的 led 灯亮起来, 我们可以跟他对话, 比如问，"谁是最帅的?" 或者 "播放刘德华的男人哭吧哭吧不是罪"。小伙伴，尽情的 High 起来吧。

### 为树莓派和 2mic 做一个专属音箱

由于 2mic 板本身带有喇叭接口，因此可以购买一个小喇叭，再结合 3D 打印，激光切割即可打造一款专属小音箱。行动起来吧！

#### 准备阶段

为了能制作出自己的造型，我选择 3D 打印制作音箱主体。然后使用激光雕刻薄木板制作出顶部盖板，底板和前面板。然后购买了一个2寸的全频喇叭，喇叭参数为 4Ω ，3W。


### 开始制作

设计音箱造型。普通的小音箱只要设计成密封的即可。我采用圆形造型，喇叭向前发声，这样声音效果较好。

首先是 3D打印。设计好安装孔位和形状。

然后设计顶部和底部盖板。也是设计好安装孔位和形状。

最后设计前面板，需根据喇叭尺寸设计。我在面板下方增加了两个小的凸起，用于倾斜音箱，提升视觉效果。

大功告成！享受属于自己的智能音箱吧！





## FAQ(疑问解答)
1.


Q:严格按照本 wiki 操作，驱动还是安装失败，怎么办？


A:如果按照上述方法安装驱动均失败，请点击下面固件安装

[我是固件](https://pan.baidu.com/s/1c1WqaWC)


下载密码：cn78



## 资源下载
- **[Eagle]** [Respeaker_2_Mics_Pi_HAT_SCH](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_SCH.zip)
- **[Eagle]** [Respeaker_2_Mics_Pi_HAT_PCB](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_PCB.zip)
- **[PDF]** [Respeaker_2_Mics_Pi_HAT_SCH](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_SCH.pdf)
- **[PDF]** [Respeaker_2_Mics_Pi_HAT_PCB](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/ReSpeaker%202-Mics%20Pi%20HAT_PCB.pdf)