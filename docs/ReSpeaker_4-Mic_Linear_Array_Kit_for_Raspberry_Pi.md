---
title: ReSpeaker 4-Mic 线性阵列套件
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

### 准备工作

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


### 软件


**准备**

*方法A 通过[PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)由SSH协议登陆*

通过 Putty 或其他 ssh 工具 来登陆你的树莓派，在开始之前，请确保:

1- 打开树莓派中的 *ssh* 功能，让其能够通过 *putty*登陆. 如果不知道如何打开 *ssh* 功能, 请去百度或者谷歌一下.

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

该方法与方法A不同之处在于可以图形化控制你的树莓派，由于要使这个套件可以与alexa或者dueros一起工作， 需要打开网页来取得授权，所以必须得用图形化界面登陆，这里推荐你用 *VNC Viewer* 来登录树莓派，也是通过SSH协议登陆 ,需要注意的是，在烧录官方镜像后需要先通过方法C来通过图形化界面开启SSH和VNC，之后才能用VNC登陆树莓派。


*方法 C，直接插上外设来控制树莓派*

如果觉得以上步骤太繁杂，你也可以直接将显示器插在HDMI接口，将鼠标键盘插在USB接口来控制树莓派，更为简单


**Step 1. Install seeed-voicecard**

得到seeed voice Card 的源码，安装所有linux内核驱动。

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh
sudo reboot

```

**Step 2. 检查声卡**

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

使用下面的命令来检查声卡.

```
pi@raspberrypi:~ $ aplay -L
```

应该如下所示:

```
null
    Discard all samples (playback) or generate zero samples (capture)
default
playback
dmixed
ac108
multiapps
ac101
sysdefault:CARD=ALSA
    bcm2835 ALSA, bcm2835 ALSA
    Default Audio Device
dmix:CARD=ALSA,DEV=0
    bcm2835 ALSA, bcm2835 ALSA
    Direct sample mixing device
dmix:CARD=ALSA,DEV=1
    bcm2835 ALSA, bcm2835 IEC958/HDMI
    Direct sample mixing device
dsnoop:CARD=ALSA,DEV=0
    bcm2835 ALSA, bcm2835 ALSA
    Direct sample snooping device
dsnoop:CARD=ALSA,DEV=1
    bcm2835 ALSA, bcm2835 IEC958/HDMI
    Direct sample snooping device
hw:CARD=ALSA,DEV=0
    bcm2835 ALSA, bcm2835 ALSA
    Direct hardware device without any conversions
hw:CARD=ALSA,DEV=1
    bcm2835 ALSA, bcm2835 IEC958/HDMI
    Direct hardware device without any conversions
plughw:CARD=ALSA,DEV=0
    bcm2835 ALSA, bcm2835 ALSA
    Hardware device with all software conversions
plughw:CARD=ALSA,DEV=1
    bcm2835 ALSA, bcm2835 IEC958/HDMI
    Hardware device with all software conversions
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


**Step 3. 录音播放测试**

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





### 语音助手示例


**Step 1. 安装python虚拟环境**

```

sudo apt install python-virtualenv          # install python virtualenv tool
virtualenv --system-site-packages ~/env     # create a virtual python environment
source ~/env/bin/activate                   # activate the virtual environment
(env) pi@raspberrypi:~ $

```

**Step 2. 安装 AVS**

```
(env) pi@raspberrypi:~ $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/respeaker/avs
(env) pi@raspberrypi:~ $ cd avs    # install Requirements
(env) pi@raspberrypi:~ $ python setup.py install
(env) pi@raspberrypi:~ $ sudo apt-get install gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gir1.2-gstreamer-1.0 python-gi python-gst-1.0
(env) pi@raspberrypi:~ $ sudo apt remove gstreamer1.0-omx gstreamer1.0-omx-rpi
```

**Step 3.取得 Alexa 或 Baidu 授权**


要获得授权，您需要打开浏览器以登录您的亚马逊或百度ID，因此您需要使用VNC Viewer或通过显示器和键盘进行操作。 与ssh相同，您需要树莓派的IP才能登录VNC。.


####  Alexa 示例

```
pi@raspberrypi:~ $ source ~/env/bin/activate
(env) pi@raspberrypi:~ $ alexa-auth
```

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/raw/master/img/auth.png)


当成功登陆后，可以通过如下命令来打开alexa

```
pi@raspberrypi:~ $ source ~/env/bin/activate
(env) pi@raspberrypi:~ $ alexa-tap
```

这时你可以敲击 enter 键开始与alexa的对话



#### Dueros 示例


如果我们想在 alexa授权和dueros授权之间切换，请x先删除 `/home/pi/.avs.json` . 这个文件是默认隐藏的所以请输入 `ls -la` 才能显示出来
```
rm -f /home/pi/.avs.json
```


这时你可以通过命令行来登录百度

```
pi@raspberrypi:~ $ source ~/env/bin/activate
(env) pi@raspberrypi:~ $ dueros-auth
```
当成功登陆后，输入以下命令

```
pi@raspberrypi:~ $ source ~/env/bin/activate
(env) pi@raspberrypi:~ $ alexa-tap
```
这时你可以敲击回车，并向它提问。

#### snowboy唤醒词检测引擎

开始这部分之前，你首先要取得Alexa或者Dueros的授权.可能如你所见，上面的示例都是由敲击回车键启动Alexa或者Dueros，但是如果你想通过语音唤醒词来启动呢

**Step 1. 安装 Snowboy**
```
cd ~
git clone https://github.com/respeaker/4mics_hat.git
source ~/env/bin/activate              # activate the virtual, if we have already activated, skip this step
(env) pi@raspberrypi:~ $ cd ~/4mics_hat
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install libatlas-base-dev     # install snowboy dependencies
(env) pi@raspberrypi:~/4mics_hat $ sudo apt install python-pyaudio        # install pyaudio
(env) pi@raspberrypi:~/4mics_hat $ pip install ./snowboy*.whl             # install snowboy for KWS
(env) pi@raspberrypi:~/4mics_hat $ pip install ./webrtc*.whl              # install webrtc for DoA
(env) pi@raspberrypi:~/4mics_hat $ cd ~/
(env) pi@raspberrypi:~ $ git clone https://github.com/voice-engine/voice-engine
(env) pi@raspberrypi:~ $ cd voice-engine/
(env) pi@raspberrypi:~/voice-engine $ python setup.py install

```


**Step 2. 配置 Pulse Audio**
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

**Step 3. 配置 `default.pa` and `daemon.conf`**
```
sudo cp default.pa /etc/pulse/
sudo cp daemon.conf /etc/pulse/
```

**Step 4. 重启树莓派并检查**
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

配置snowboy之后，请照如下所示来做
```
source ~/env/bin/activate
cd ~/voice-engine/examples
python kws_alexa_for_4mic_liner_pihat.py
```
这时你应该能看到LED灯亮，并且你可以通过说唤醒词来唤醒它




## FAQ(疑问解答)

**Q1:严格按照本 wiki 操作，驱动还是安装失败，怎么办？**


A1:如果按照上述方法安装驱动均失败，请点击下面固件安装

[我是固件](https://v2.fangcloud.com/share/7395fd138a1cab496fd4792fe5?folder_id=188000207913)

lite版本是没有图形界面的精简版,并且烧了固件后，记得换源。如果要使用交互功能之前请命令行输入alexa-auth或dueros-auth申请授权，授权成功后会在/home/pi目录下生成.avs.json文件，这时才能使用交互功能。/home/pi目录下会有 respeaker的例程文件夹,可以根据用的mic不同而使用相应的例程。需要注意的是，请烧录系统后在respeaker目录下更新下例程，可以在respeaker目录下执行``` git pull origin master ```命令来更新。

**Q2: 如果我们用aplay可以听到声音，但是运行alexa/dueros不能听到声音。**

A1: 我们有3个播放器（mpv，mpg123和gstreamer）可供使用。 SpeechSynthesizer和Alerts更适应mpg123。 AudioPlayer适合gstreamer> mpv> mpg123。 Gstreamer支持更多的音频格式，并在树莓派上运行良好。 我们也可以使用环境变量PLAYER来指定AudioPlayer的播放器。 所以请尝试下面的命令来启用语音。

```
sudo apt install mpg123
PLAYER=mpg123 python ns_kws_doa_alexa_with_light.py
```

**Q3:运行DOA，说snowboy的时候没有响应。**

A3:运行audacity检查4个麦克风是否多有数据，如果有其中一个麦克风没有数据，就会没有响应。

**Q4 关于安装snowboy时出现不适合该平台的警告提醒**

A4: 目前snowboy只能兼容python2，所以通过在安装python的虚拟环境时，请确保是python2

**Q5 有时候 sudo python file.py 时候会出现依赖问题**

A5.测试时发现sudo执行时候默认从系统环境执行，而wiki中用到的依赖都是装在~/env 下的，可以通过 ```sudo  ~/env/bin/python file.py```来解决


**Q6 可以通过3.5毫米音频插孔的播放来听到声音，但是在运行ns_kws_doa_alexa_with_light.py时听不到声音**

 A6： 我们有3个播放器（mpv，mpg123和gstreamer）可以使用。 mpg123更适合语音识别和唤醒更，它更具响应性； 而AudioPlayer 更适用gstreamer> mpv> mpg123。 Gstreamer支持更多音频格式，并且在raspberry pi上运行良好。 我们还可以使用环境变量PLAYER指定AudioPlayer的播放器。 所以请尝试以下命令启用语音。
```

  sudo apt install mpg123
  PLAYER=mpg123 python ns_kws_doa_alexa_with_light.py
```

**Q7 在运行 kws_doa.py 时候喊 snowboy 没反应**

A7 请运行audacity以确保4个频道良好。 如果有一个没有数据的频道，当我们说snowboy时就没有回复。


**Q8 驱动安装后无法识别到声卡**

A8: 打开 Preferences --> raspberry Pi config 中的 1-wire 设置成disable


**Q9: 只有4个mic，怎么会有8个通道?**

A9: 该套件集成了2个 AC108在阵列上, 每个 AC108 有4个输出通道. 所以一共有8个输出通道。其中有4个是mic的 ,两个是回采的，剩下两个没有用到。

## 资源下载

- **[PDF]** [AC101 Datasheet](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/reg/AC101_User_Manual_v1.1.pdf)
- **[PDF]** [AC108 Datesheet](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/reg/AC108_Datasheet_V1.2.pdf)



## 技术支持
如果有其他技术问题，请发邮件到 [techsupport@seeed.cc](techsupport@seeed.cc) 或者请到我们的论坛里去参与讨论 [forum](http://forum.seeedstudio.com/).
