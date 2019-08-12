---
name: ReSpeaker 4-Mic 线性阵列套件
category: ReSpeaker
bzurl:
oldwikiname: ReSpeaker 4-Mic 线性阵列套件
prodimagename: cover.JPG
surveyurl:
sku: 107990056
---

![enter image description here](https://github.com/SeeedDocument/ReSpeaker_4-Mics_Linear_Array_Kit/raw/master/img/main_wiki.jpg)

基于Raspberry Pi的ReSpeaker 4-Mic线性阵列套件是一款适用于AI和语音应用的Raspberry Pi的四通道麦克风扩展板。这意味着您可以借助它构建一个集成Amazon Alexa语音服务，Google助手等，功能更强大，更灵活的语音产品。

ReSpeaker 4-Mic线性阵列包含两个板子：一个是适配板，另一个是4mic线性阵列。

ReSpeaker 4-Mic线性阵列支持在Raspian系统下八通道输入输出。其中，前六个麦克风输入通道录音（只有前4个输入通道有效捕获数据），其余2个输入通道是回采通道；输出通道中前2播放输出通道，其余6输出通道是虚拟的。



[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://seeedstudio.taobao.com/search.htm?q=respeaker&s_from=newHeader&ssid=s5-e&search_type=item&sourceId=tb.item)

## 产品特性

- Raspberry Pi兼容（支持Raspberry Pi Zero和Zero W，Raspberry Pi B +，Raspberry Pi 2 B和Raspberry Pi 3 B，Raspberry Pi 4 B，Raspberry Pi 3 B +）
- 2个ADC 芯片和一个 DAC芯片
- 8输入8输出通道
- 四麦克阵列
- 支持Grove接口
- 与树莓派40针接口兼容
- 耳机和扬声器输出

## 规格参数

- 2 x X-Power AC108 ADC
- 4 x高性能贴片模拟麦克
- 1 x X-Power AC101 DAC
- 输出接口:
    - 3.5mm headset audio jack
    - 扬声器接口
- 与树莓派40pin接口兼容
- 麦克风: Knowles SPU0414HR5HSB
- 灵敏度: -22 dBFS (Omnidirectional)
- SNR: 59 dB


## 创意应用

- 智能语音交互
- 智能语音助手
- 录音
- 语音会议系统
- 会议通信设备
- 语音控制机器人
- 汽车语音助手
- 其他需要语音指令的设计





## 硬件概述


![](https://github.com/SeeedDocument/ReSpeaker_4-Mics_Linear_Array_Kit/raw/master/img/Hardware.jpg)


## 安装图示  

![](https://github.com/SeeedDocument/Bazaar_file/raw/master/107990055/img/ab.png)


## 入门指导

### 1. 准备工作

**准备材料**


ReSpeaker 4-Mic 线性麦克阵列    x1

[Raspberry Pi 3B 或 3B+](https://www.seeedstudio.com/Raspberry-Pi-3-Model-B%2B-p-3037.html?utm_source=homepage&utm_medium=homepagebanner&utm_campaign=hp_0605)              x1

[Micro-USB 线](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)                     x1

PC                                  x1

耳机或Speaker               x1


!!!Tips
      实时上该套件支持 Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B, Raspberry Pi 3 B 和 Raspberry Pi 3 model B+, 在这个wiki中我们用的是Raspberry Pi 3 B


**连接**


**Step 1.**  将 *ReSpeaker 适配板* 与 *ReSpeaker 4-Mic 线性阵列* 通过带线连接

**Step 2.**  将 *ReSpeaker 适配板* 插在 *树莓派* 上

**Step 3.** 将 *耳机* 插在 *3.5mm 耳机孔*上 或者 *扬声器* 插在*JST 2.0 speaker jack*上

**Step 4.**  将 *树莓派*与 *PC* 通过micro-USB线连接


![Pics here](https://github.com/SeeedDocument/ReSpeaker_4-Mics_Linear_Array_Kit/raw/master/img/4-mic.jpg)


### 2. 软件


**准备**

*方法A 通过[PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)由SSH协议登陆*

通过 Putty 或其他 ssh 工具 来登陆你的树莓派，在开始之前，请确保:

1- 打开树莓派中的 *ssh* 功能，让其能够通过 *putty* 登陆. 如果不知道如何打开 *ssh* 功能, 请去百度或者谷歌一下

2- 你的树莓派和PC机在同一子网下链接.若不知如何配置wifi，请去百度或者谷歌一下。

3- 查看你的树莓派的IP地址，如果不知道如何操作，请参考[raspberry offical documentation](https://www.raspberrypi.org/documentation/remote-access/ip-address.md)

4- 在PC机端选择SSH登陆，将莓派的地址输入后打开终端

![pic](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/img/putty.png)

进入终端后请输入用户名和密码，分别是‘pi’和‘raspberry’

```
login as: pi
pi@192.168.43.210's password:raspberry

```

此时，登陆树莓派成功，可以通过终端输入命令控制树莓派

*方法B，通过VNC软件由SSH协议登陆树莓派*

[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)

该方法与方法A不同之处在于可以图形化控制你的树莓派，由于要使这个套件可以与alexa或者dueros一起工作， 需要打开网页来取得授权，所以必须得用图形化界面登陆，这里推荐你用 *VNC Viewer*来登录树莓派，也是通过SSH协议登陆 ,需要注意的是，在烧录官方镜像后需要先通过方法C来通过图形化界面开启SSH和VNC，之后才能用VNC登陆树莓派。


*方法 C，直接插上外设来控制树莓派*

如果觉得以上步骤太繁杂，你也可以直接将显示器插在HDMI接口，将鼠标键盘插在USB接口来控制树莓派，更为简单

### 3. 系统配置与驱动安装

**step 1. 烧录系统，登陆，换源**

因为当前的Pi内核目前不支持wm8960编解码器，所以我们需要手动构建。

  1. 确保您正在您的Pi上运行[最新的Raspbian操作系统（debian 9）](https://www.raspberrypi.org/downloads/raspbian/)。 *（更新于2017.09.15）*，您可以用etcher进行系统烧录

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

**step 2. 驱动下载并安装**
运行下面命令

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard #下载声卡驱动
sudo ./install.sh #安装声卡驱动
reboot  #重启
```

**step 3. 检查声卡名称是否与源代码seeed-voicecard相匹配.**

输入以下命令来查看声卡

```
pi@raspberrypi:~ $ arecord -L
```

如果正常，应该是显示以下内容:

```
null
    Discard all samples (playback) or generate zero samples (capture)
default
playback
dmixed
ac108
multiapps
ac101
sysdefault:CARD=seeed8micvoicec
    seeed-8mic-voicecard,
    Default Audio Device
dmix:CARD=seeed8micvoicec,DEV=0
    seeed-8mic-voicecard,
    Direct sample mixing device
dsnoop:CARD=seeed8micvoicec,DEV=0
    seeed-8mic-voicecard,
    Direct sample snooping device
hw:CARD=seeed8micvoicec,DEV=0
    seeed-8mic-voicecard,
    Direct hardware device without any conversions
plughw:CARD=seeed8micvoicec,DEV=0
    seeed-8mic-voicecard,
    Hardware device with all software conversions

```


###  4. 录音播放测试

你可以先录音在播放，或者一边录音一边播放
```
#It will capture sound on AC108 and save as a.wav
arecord -Dac108 -f S32_LE -r 16000 -c 8 a.wav
#Take care of that the captured mic audio is on the first 6 channels

#It will play sound file a.wav on AC101
aplay -D ac101 a.wav
#Do not use -D plughw:1,0 directly except your wave file is single channel only.

#Doing capture && playback the same time
arecord -D hw:1,0 -f S32_LE -r 16000 -c 8 to_be_record.wav &
#mono_to_play.wav is a mono channel wave file to play
aplay -D plughw:1,0 -r 16000 mono_to_play.wav

```

!!!Note
        限制开发人员使用4-Mic线性阵列套件（或4-Mic线性阵列套件）同时进行捕获和回放:

        -1. 捕获必须首先开始，否则捕获通道可能是无序的.

        -2. 播放输出通道必须填充8个相同的通道数据或4个相同的立体声通道数据，否则扬声器或耳机将无法输出任何内容。

        -3. 如果要同时播放和录制，aplay音乐文件必须是单声道，否则您无法使用此命令播放。

您也可以使用Audacity进行播放和录制。

!!!Tips
        你可以通过图形界面手动点击打开audacity或者通过命令行打开



```
$ sudo apt update
$ sudo apt install audacity
$ audacity                      // run audacity

```


![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/audacity.png)




### 5. 安装python和虚拟环境
  这样是是为了隔离SDK与系统Python包关系。
```

pi@raspberrypi:~ $ cd /home/pi
pi@raspberrypi:~ $ git clone https://github.com/respeaker/4mics_hat.git
pi@raspberrypi:~ $ cd /home/pi/4mics_hat
pi@raspberrypi:~/4mics_hat $ sudo apt install python-virtualenv          # 安装 python2 虚拟环境工具
pi@raspberrypi:~/4mics_hat $ virtualenv --system-site-packages ~/env     # 建立虚拟环境，命名位env,放在~目录下
pi@raspberrypi:~/4mics_hat $ source ~/env/bin/activate                   # 激活虚拟环境
(env) pi@raspberrypi:~/4mics_hat $ pip install spidev gpiozero           # 安装需要的工具包
```


##  Alexa SDK 和 Dueros SDK

由于国内登录不上 Google Assisant ，所以使用在国内能连接的 Alexa 和 百度 DuerOs 作为语音引擎，开发出能让大多数人使用的语音互动系统。




**step 1. 配置和安装AVS以及相关依赖**

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


当成功登陆后，可以通过如下命令来打开alexa

```
pi@raspberrypi:~ $ source ~/env/bin/activate
(env) pi@raspberrypi:~ $ alexa-tap
```

这时你可以敲击 enter 键开始语音对话

**step 3. 配置和安装语音引擎**

开始这部分之前，你首先要取得Alexa或者Dueros的授权.可能如你所见，上面的示例都是由敲击回车键启动Alexa或者Dueros，但是如果你想通过语音唤醒词来启动呢


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

```

**Step 4. 配置 Pulse Audio**
```
cd ~
sudo apt install pulseaudio
cd seeed-voicecard
cd pulseaudio
cd pulse_config_6mic
sudo cp seeed-voicecard.conf /usr/share/pulseaudio/alsa-mixer/profile-sets/
```
然后你需要修改 .rules文件。当系统启动时，当检测到卡“seeed8micvoicec”时，将在udev数据库中设置PULSE_PROFILE_SET变量，并强制使用PulseAudio.
```
sudo nano /lib/udev/rules.d/90-pulseaudio.rules

```
然后在大约第87行添加以下行（在某些笔记本电脑的设置后面和行之前 GOTO="pulseaudio_end")
```
# Seeed Voicecard
ATTR{id}=="seeed8micvoicec",ATTR{number}=="1",ENV{PULSE_PROFILE_SET}="seeed-voicecard.conf"

```
应该显示如下:
![](https://github.com/respeaker/seeed-voicecard/raw/master/pulseaudio/udev_rules_6mic.png)
按 ++ctrl+x++退出，然后按 ++y++ 来保存编辑.
ATTR{number}的值可以通过下面的命令找到:
```
udevadm info -a -p /sys/class/sound/card1/:
```

**Step 5. 配置 `default.pa` and `daemon.conf`**
```
sudo cp default.pa /etc/pulse/
sudo cp daemon.conf /etc/pulse/
```

**Step 6. 重启树莓派并检查**
```
sudo reboot
pulseaudio --start  # start pulse at first
pactl info  # check the setting

# The output should be like this
# You could see the default sink is seeed-2ch and default source is seeed-8ch
pi@raspberrypi:~ $ pactl info
Server String: /run/user/1000/pulse/native
Library Protocol Version: 32
Server Protocol Version: 32
Is Local: yes
Client Index: 6
Tile Size: 65496
User Name: pi
Host Name: raspberrypi
Server Name: pulseaudio
Server Version: 10.0
Default Sample Specification: s32le 8ch 96000Hz
Default Channel Map: front-left,front-left-of-center,front-center,front-right,front-right-of-center,rear-center,aux0,aux1
Default Sink: alsa_output.platform-soc_sound.seeed-2ch
Default Source: alsa_input.platform-soc_sound.seeed-8ch
Cookie: 3523:e5af
```


**step 7. 让我们High起来!**
执行下方命令行：
```
source ~/env/bin/activate #打开虚拟环境
cd ~/voice-engine/examples #进入示例文件夹
python kws_alexa_for_4mic_liner_pihat.py #运行例程
```
 我们会在终端看到很多 debug 的消息. 当我们看到 **status code: 204** 的时候, 请说 `snowboy` 来唤醒 respeaker。接下来 respeaker 上的 led 灯亮起来, 我们可以跟他对话, 比如问，"谁是最帅的?" 或者 "播放刘德华的男人哭吧哭吧不是罪"。小伙伴，尽情的 High 起来吧。

!!!Note
      如果使用alexa-auth的话请用英文交互，如果是dueros的话请用中文。





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


**Step 3. 下载源码 [Smart_Fan.py](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/raw/master/src/baidu_STT/Smart_fan.py)**

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


**Q1 驱动安装后无法识别到声卡**

A1: 打开 Preferences --> raspberry Pi config 中的 1-wire 设置成disable


**Q2: 只有4个mic，怎么会有8个通道?**

A2: 该套件集成了2个 AC108在阵列上, 每个 AC108 有4个输出通道. 所以一共有8个输出通道。其中有4个是mic的 ,两个是回采的，剩下两个没有用到。

## 资源下载

- **[PDF]** [AC101 Datasheet](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/reg/AC101_User_Manual_v1.1.pdf)
- **[PDF]** [AC108 Datesheet](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/reg/AC108_Datasheet_V1.2.pdf)



## 技术支持
如果有其他技术问题，请发邮件到 [techsupport@seeed.cc](techsupport@seeed.cc) 或者请到我们的论坛里去参与讨论 [forum](http://forum.seeedstudio.com/).
