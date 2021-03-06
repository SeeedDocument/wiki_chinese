---
name: Respeaker 4-Mic Array
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-4-Mic-Array-for-Raspberry-Pi-p-2941.html
oldwikiname:
prodimagename:
wikiurl: https://wiki.seeedstudio.com/cn/Respeaker_4-Mics_Pi_HAT
sku: 103030216
---

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/overview.jpg?raw=true)

基于Raspberry Pi的ReSpeaker 4-Mic阵列是一款适用于AI和语音应用的Raspberry Pi的四通道麦克风扩展板。 这意味着您可以借助它构建一个集成Amazon Alexa语音服务，Google助手等，功能更强大，更灵活的语音产品。

区别于 [ReSpeaker 2-Mics Pi HAT](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.2.48d67e33NrSwXZ&id=553438198956), 该板是基于AC108开发的，这是一款高度集成四通道ADC，具有用于高清晰度语音捕获，I2S / TDM输出，拾取3米半径的声音的语音设备。 此外，这款4-Mics版本提供了超酷LED环，其中包含12个APA102可编程LED。 就像Amazon Echo或 Google assist一样， 使用4个麦克风和LED环，Raspberry Pi具有VAD（语音活动检测），DOA（到达方向），KWS（关键字搜索），并通过LED环显示方向灯功能。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.1-c.w13838425-11172345252.1.542035bczDBegW&id=557884254210)

## 产品特征

* Raspberry Pi兼容（支持Raspberry Pi Zero和Zero W，Raspberry Pi B +，Raspberry Pi 2 B和Raspberry Pi 3 B，Raspberry Pi 4 B，Raspberry Pi 3 B +）
* 4个麦克风
* 3米半径的语音捕捉
* 2个Grove接口
* 12个APA102板载指示灯
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
### 1. 系统配置与驱动安装
**step 1. 把ReSpeaker 2-Mics Pi HAT插入到Raspberry Pi**

把 ReSpeaker 4-Mics Pi HAT 插入到 Raspberry Pi, 确保插入Raspberry Pi的时候针脚对齐。

!!!Note
        不要在上电的时候，热插拔ReSpeaker 4-Mics Pi HAT.

![connection pic1](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/connect1.jpg?raw=true)
![connection pic2](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/connect2.jpg?raw=true)

**step 2. 烧录系统，登陆，换源**

因为当前的Pi内核目前不支持wm8960编解码器，所以我们需要手动构建。

1. 确保您正在您的Pi上运行[最新的Raspbian操作系统（debian 9）](https://www.raspberrypi.org/downloads/raspbian/)，您可以用etcher进行系统烧录

2.  您可以用 [VNC](https://www.raspberrypi.org/documentation/remote-access/vnc/)或者PUTTY连接树莓派，但之前请配置好wifi

3. 在安装驱动之前，请根据以下流程切换源到清华。

```
sudo nano /etc/apt/sources.list
```

如果是用#注释掉原文件内容，用以下内容取代：

```
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib
```

!!!Note

    如果是2019-06-20之前版本 需要将`buster`修改为`Stretch`可以通过`cat /etc/rpi-issue`查看是什么时候发布的版本 

**step 3. 驱动下载并安装**
运行下面命令
```
sudo apt-get update
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard #下载声卡驱动
sudo ./install.sh #安装声卡驱动
reboot  #重启
```


!!!Note

    若驱动安装失败您可以跳转到FAQ的Q1以解决驱动安装失败问题。

**step 4. 检查声卡名称是否与源代码seeed-voicecard相匹配.**


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

如果要更改alsa设置，可以使用`sudo alsactl --file=ac108_asound.state store`保存。 当你需要再次使用这些设置时，将它复制到：`sudo cp ~/seeed-voicecard/ac108_asound.state /var/lib/alsa/asound.state`

### 2. 录音播放测试

  **step 1. 录播测试**
 可以用`arecord`录制，然后用`aplay`播放：(不要忘记插耳机或者喇叭):

```
arecord  |  aplay 
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

```
alsamixer
```

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/alsamixer.png?raw=true)

!!!Note
    首先请用F6选择seeed-4mic的声卡设备。

左和右箭头键用于选择通道或设备，“向上和向下箭头”控制当前所选设备的音量。 退出程序使用ALT + Q或按Esc键。 [More information](https://en.wikipedia.org/wiki/Alsamixer)


### 3. 控制APA102 LED的示例

每个板载APA102 LED都有一个额外的驱动芯片，驱动芯片设置LED的颜色，然后保持该颜色，直到接收到新的命令。

![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/rainbow.jpg?raw=true)

- 请在执行之前打开SPI，具体步骤如下:

    - 输入： `sudo raspi-config`;
    - 选择 "Interfacing Options";
    - 选择 "SPI";
    - 选择 “Yes”  
    - 选择 “OK”
    - 选择 “Finish”

- 配置完后，可以执行下列命令行来运行led示例  

```
pip install spidev gpiozero           # 安装 spidev 和 gpiozero
git clone --depth 1 https://github.com/respeaker/pixel_ring.git   #安装pixel_ring
cd pixel_ring
pip install -U -e .
cd examples/
```

- 在虚拟环境下运行 `python respeaker_4mic_array.py`, 你可以看到LED像Google Assistant灯光一样闪烁。

##  Alexa SDK  和 DuerOs SDK

由于国内登录不上 Google Assisant ，所以使用在国内能连接的 Alexa 和 百度 DuerOs 作为语音引擎，开发出能让大多数人使用的语音互动系统。

###  1. 配置和DOA测试

**step 1. 配置 Voice engine**
```
cd /home/pi
git clone https://github.com/respeaker/4mics_hat.git
cd /home/pi/4mics_hat
cd ~/4mics_hat
sudo apt install libatlas-base-dev     # 安装 snowboy dependencies
sudo apt install python-pyaudio        #安装pyaudio音频处理包
pip install ./snowboy*.whl             # 安装 snowboy for KWS
pip install ./webrtc*.whl              # 安装 webrtc for DoA
cd ~/
git clone https://github.com/voice-engine/voice-engine #write by seeed
cd voice-engine/
python setup.py bdist_wheel
pip install dist/*.whl
cd examples/respeaker_4mic_array_for_pi
```


**step 2. 运行**

  在虚拟环境下运行 `python kws_doa.py`。请用 snowboy 来唤醒，我们就可以看到方位的信息。

### 2. 百度中文语音互动或者alexa英文语音互动

**step 1. 配置和安装相关依赖**
  ```
  cd ~/
  git clone https://github.com/respeaker/avs
  cd avs                                 # install Requirements
  python setup.py install
  pip install avs==0.5.3
  sudo apt install libgstreamer1.0-0
  sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly 
  sudo apt install gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tool
  sudo apt install gstreamer1.0-plugins-good
  sudo apt install python-gi gir1.2-gstreamer-1.0
  pip install tornado==5.1.1
  ```
**step 2. 取得授权**

  在终端运行 `alexa-auth` ，然后登陆获取alexa的授权， 或者运行 `dueros-auth` 获取百度的授权。 授权的文件保存在`/home/pi/.avs.json`。
  （需要关闭自动打开的浏览器，打开树莓派桌面上的浏览器进行授权才能成功）
  
  ![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/raw/master/img/auth_new.png)
  ![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/raw/master/img/auth.png)


!!!Note
      如果我们在 `alexa-auth` 和 `dueros-auth`之间切换, 请先删除 `/home/pi/.avs.json` 。 这个是隐藏文件，请用 `ls -la` 显示文件。


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

**Q1:严格按照本 wiki 操作，驱动还是安装失败，怎么办？**

A1:如果按照上述方法安装驱动均失败，请点击下载下面镜像

[2018-08-06-raspbian-4GB-for-respeaker](https://v2.fangcloud.com/share/7395fd138a1cab496fd4792fe5?folder_id=188000207913)

请执行下面的步骤：

- 第一， 烧写下载好的镜像，烧了镜像后，记得换源。

- 第二， 如果要使用交互功能之前请命令行输入alexa-auth或dueros-auth申请授权，授权成功后会在 /home/pi目录下生成.avs.json文件，这时才能使用交互功能。

- 第三，/home/pi目录下会有 respeaker的例程文件夹,可以根据用的mic不同而使用相应的例程。但是请烧录系统后在respeaker目录下更新下例程，可以在respeaker目录下执行``` git pull origin master ```命令来更新。

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

  A7:请运行audacity以确保4个频道良好。 如果有一个没有数据的频道，当我们说snowboy时就没有回复。

**Q8 怎样更改唤醒词**

  A8:

  step 1. 请到[Snowboy](https://snowboy.kitt.ai/)的官网去自定义一个关键词（当然下载别人定义的关键词也行）。

  step 2. 将自定义或者别人的关键词`.pmdl`文件下载到`/usr/local/lib/python2.7/dist-packages/snowboy/resources/models`路径下。

  step 3. 修改`respeaker/4mic/ns_kws_doa_alexa.py`文件里面的`kws = KWS(model='/usr/local/lib/python2.7/dist-packages/snowboy/resources/models/***.pmdl')`。其中`***.pmdl`为刚刚从`snowboy`官网上面下载的。


## 资源下载

- **[PDF 原理图]** [ReSpeaker 4-Mic Array for Raspberry Pi(PDF)](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/src/ReSpeaker%204-Mic%20Array%20for%20Raspberry%20Pi%20%20v1.0.pdf)
