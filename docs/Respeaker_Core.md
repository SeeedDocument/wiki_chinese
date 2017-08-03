---
title: Respeaker Core
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-Core-Based-On-MT7688-and-OpenWRT-p-2716.html
oldwikiname:  Respeaker Core
prodimagename:  respeaker_core.jpg
surveyurl:  https://www.research.net/r/Respeaker_Core
sku:     102010088
---
![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/respeaker_core.jpg)

ReSpeaker是一个开放的模块化语音接口，用于接入您周围的各种事物。让您通过语音与您的家用电器，您的工厂，办公室，互联网设备或您日常生活中的其他任何事物进行互动。

- **它是您周围物件的语音扩展**

  ReSpeaker支持在线语义识别服务并且拥有离线轻量级语音识别引擎。您可以将ReSpeaker添加到您周围的事物中，使其变得智能或更加智能。

- **它是一个音频流设备**

  语音交互从未与音乐娱乐区分开，ReSpeaker也是如此。ReSpeaker支持Airplay / DLNA无线音乐流。只需使用AUX电缆将ReSpeaker连接到任何普通的扬声器，那么您可以开始享受您所爱的音乐，而无需按任何一个按钮。


- **它是孩子们学习的工具**

  ReSpeaker控制模块是基于ATmega32u4芯片，该芯片完全兼容Arduino驱动。这意味着，我们可以使用ReSpeaker作为强大的Arduino学习板，并做了许多“Arduino”开发板能做的事情。这是为了学习，这是为了练习，这是乐趣。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.5e478797r0BkWN&id=538922110430)

##   产品特性
---
![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/respeaker_core_futures.jpg)

- Set Your Hands Free: Speech recognition with or without the Internet
- Wireless Streaming: stream music via Airplay/DLNA
- Easy-to-use SDK: For Python and C/C++ developers
- Growing Features: Download and plug-in to enrich its features and functionalities.
- Plug-n-play Add-ons: Extendable with Mic Array, Grove Extension Board, Grove Modules.
- Installation-free App: Set all things on webbased App. (Not Available Yet)

##   规格参数
---
![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/respeaker_core_hardware%20overview.jpg)

### 技术规格


- AI7688 Wi-Fi 模块:

    - 操作系统: 基于GNU/Linux 的 OpenWrt
    - wifi支持: 支持802.11b/g and HT 802.11n 模式
    - 扩展性:两排扩展接口，拥有 I2C, GPIO 和 USB 2.0
    - 接口: 3.5mm AUX 音频接口, Micro USB 和 SD card 卡槽

- ATMega32U4 处理器:

    - Linnux平台下的 USB CDC 软串口
    - 12个可编程LED 指示灯
    - 8 个片上触点接口

- Codec WM8960:

    - DAC SNR 98dB (‘A’ weighted), THD -84dB at 48kHz, 3.3V  
    - ADC SNR 94dB (‘A’ weighted), THD -82dB at 48kHz, 3.3V  
    - Stereo Class D Speaker Driver with 87% efficiency (1W output)  
    - On-chip Headphone Driver  
    - 40mW output power into 16Ω at 3.3V  
    - THD -75dB at 20mW, SNR 90dB with 16Ω load  
    - On-chip PLL provides flexible clocking scheme  
    - Sample rates: 8, 11.025, 12, 16, 22.05, 24, 32, 44.1, 48 kHz

- 供电电压: 5V DC  

- 尺寸: 直径 70mm   

- 重量: 17g

### 管脚图

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/respeaker_core_pinmap.png)

-  GPIO0 / I2S_ADC：驱动外部编码器/解码器，ADC信号
-  GPIO1 / I2S_DAC：驱动外部编码器/解码器，DAC信号
-  GPIO2 / I2S_LRCLK：驱动外部编码器/解码器，左/右通道采样时钟
-  GPIO3 / I2S_BCLK：驱动外部编码器/解码器，位时钟
-  MCLK_OUT：外部设备的主时钟
-  HP_SEL：耳机频道选择。如果使用ReSpeaker Mic Array输出音频，请将HP_SEL设置为高电平
-  HP_L：ReSpeaker麦克风阵列的模拟音频左声道
-  HP_R：ReSpeaker麦克风阵列的模拟音频右声道
-  AGND：音频模拟地


##   入门指导
---

### 第一次拿到Respeaker_Core从哪里开始？

#### 1. 准备
-  ReSpeaker核心板
-  PC或Mac
-  Wi-Fi网络
-  SD卡

#### 2. 连接到串行控制台

- 对于window, 推荐使用 [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)。

    - 通过USB将ReSpeaker连接到PC，勾选COM设备管理器。这里我们的ReSpeaker COM端口是COM31。

    ![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/putty1.png)

    - 在连接类型下选择Serial ,在Serial line中，输入您的ReSpeaker的COM端口号，在波特率选项中，键入57600。

    ![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/putty2.png)

    - 点击 Open.然后您将看到一个黑色的屏幕界面，点击回车键。

    ![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/putty3.png)

- 对于 Linux/Mac


-  通过USB将ReSpeaker连接到PC
-  打开一个终端会话
-  在终端中键入ls /dev/tty.usb*  我们应该看到设备列表。寻找类似tty.usbmodemXXXXX的东西，其中XXXXX通常是一个随机标识符。这是用于访问系统控制台的串行设备。然后使用屏幕实用程序连接到串口，并将波特率设置为57600，这是因为默认情况下系统控制台的波特率为57600

```
$ ls /dev/tty.usb*
/dev/tty.usbmodem14221
$ screen /dev/tty.usbmodem14221 57600
```

#### 3. 设置 Wi-Fi

ReSpeaker默认设置为中继模式，您必须将其连接到现有的无线wifi网络，然后才能使用Internet进行语音识别。

当您首次接通ReSpeaker电源时，它将创建一个名为“ReSpeakerXXXXXX”的Wi-Fi网络。这里“XXXXXX”是您的ReSpeaker MAC地址的最后6位。将您的计算机连接到此网络。

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/wifi1.png)

!!!Note
    如果“ReSpeakerXXXXXX”未出现，但找到“LinkIt_Smart_7688_XXXXXX”。请点击 [这里](http://wiki.seeed.cc/Respeaker_Core/#q20-system-recovery-by-factory-image).


获取IP地址后，打开Web浏览器，然后在地址栏中输入192.168.100.1。几秒钟后，会出现下图所示网页，需要您输入现有Wi-Fi网络的ssid和密码。

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/wifi2.png)

选择要连接的Wi-Fi并输入密码。当您按OK按钮时，ReSpeaker将加入指定的网络。

现在您的ReSpeaker能够访问互联网。

如果您没有弹出wifi登陆页面，可以使用putty串口模式下连接Respeaker_Core, 并且在putty中使用wictl扫描wifi并连接

```
root@mylinkit:~# wictl
0, SEEED-MKT
1, Xiaomi_Youth
2, ChinaNet-Z5C4
3, STU-EE
4, EMBEST_WIFI
5, SEEED-MKT
6, nobody
7, SEEED-MKT
8, se.VPN
9, Moovent_HK_2G
10, LinkIt_Smart_7688_1D917A
11, SEEED-MKT
12, SEEED-MKT
13, zhongrixing
Please choose your wifi: 8
Please input the wifi password: 88888888
udhcpc (v1.23.2) started
Sending discover...
Sending discover...
Sending select for 192.168.199.153...
Lease of 192.168.199.153 obtained, lease time 43200
udhcpc: ifconfig apcli0 192.168.199.153 netmask 255.255.255.0 broadcast 192.168.199.255
udhcpc: setting default routers: 192.168.199.1
success
root@mylinkit:~#
```

!!!注意
    如果您无法使用上述方法连接Wifi，请通过输入firstboot命令进行出厂设置。


启用Wifi功能后，我们可以使用SSH模式通过以下命令连接Respeaker。我们可以从http://192.168.100.1/#!/overview WAN IP获取Respeaker IP地址。密码是root。

```
ssh root@ssh *.*.*.*

```

#### 4. 使用SD卡来扩展存储

通常情况下，嵌入式设备可以使用有限的存储空间（ReSpeaker仅为用户提供了5M的板载Flash存储空间）。为应用或者数据提供更大的存储空间可以激发ReSpeaker的潜力，所以使用SD卡扩展存储作为extroot是一个看起来还不错的选择哟。

通过使用extroot，添加外部SD卡存储设备来实现根文件系统的存储容量的扩展。在引导过程中，外部存储空间作为根文件系统启动，或者以原始文件系统的覆盖配置进行启动。

- 确保您的SD卡已插入ReSpeaker，并且/ dev / mmcblk0p1可以通过df -h或ls / dev进行检测。

```
root@ReSpeaker:/# df -h
Filesystem                Size      Used Available Use% Mounted on
rootfs                    1.8M    832.0K    960.0K  46% /
/dev/root                29.0M     29.0M         0 100% /rom
tmpfs                    61.7M    276.0K     61.5M   0% /tmp
/dev/mtdblock6            1.8M    832.0K    960.0K  46% /overlay
overlayfs:/overlay        1.8M    832.0K    960.0K  46% /
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/mmcblk0p1            7.4G      2.5M      7.4G   0% /tmp/run/mountd/mmcblk0p1
```

- 将SD卡格式化为两个分区，一个是FAT32，另一个是EXT4。EXT4文件系统将作为一个外接程序，而FAT32将作为正常的存储设备，可以在ReSpeaker和PC之间传输文件。

```
	umount /dev/mmcblk0p1
	fdisk /dev/mmcblk0
	 ------------------ fdisk ------------------------
	>Command (m for help):o
	>Created a new DOS disklabel
	>Command (m for help):n
	>Partition type
	p   primary (0 primary, 0 extended, 4 free)
	e   extended (container for logical partitions)
	>Select (default p):p
	>Partition number (1-4, default 1):1
	>First sector (2048-15523839, default 2048):
	>Last sector, +sectors or +size{K,M,G,T,P} (2048-15523839, default 15523839): +2G
	>Command (m for help):n
	>Partition type
	p   primary (1 primary, 0 extended, 3 free)
	e   extended (container for logical partitions)
	>Select (default p):p
	>Partition number (1-4, default 2):2
	>First sector (4196352-15523839, default 4196352):
	>Last sector, +sectors or +size{K,M,G,T,P} (4196352-15523839, default 15523839):
	>Command (m for help):w
	>The partition table has been altered.
	>Calling i[  292.010000]  mmcblk0: p1 p2
	>octl() to re-read partition table.
	>Syncing disks.
	 ------------------ end ------------------------

	mkfs.fat /dev/mmcblk0p1
	mkfs.ext4 /dev/mmcblk0p2

	# reload mtk_sd kernel module
	rmmod mtk_sd
	insmod mtk_sd

```

- 准备您的外部存储root overlay。

```
mount /dev/mmcblk0p2 /mnt ; tar -C /overlay -cvf - . | tar -C /mnt -xf - ; umount /mnt
```

- 使用以下命令创建fstab。此命令将创建一个启用所有分区并将'/ mnt / mmcblk0p2'分区设置为'/ overlay'分区的fstab模板

```
	block detect > /etc/config/fstab;
	sed -i s/option$'\t'enabled$'\t'\'0\'/option$'\t'enabled$'\t'\'1\'/ /etc/config/fstab;
	sed -i s#/mnt/mmcblk0p2#/overlay# /etc/config/fstab;
	cat /etc/config/fstab;
```

- 检查是否安装到 overlay.

```
	root@mylinkit:/# mount /dev/mmcblk0p2 /overlay/
	root@ReSpeaker:/# df -h
  Filesystem                Size      Used Available Use% Mounted on
  rootfs                    1.8M    832.0K    960.0K  46% /
  /dev/root                29.0M     29.0M         0 100% /rom
  tmpfs                    61.7M    276.0K     61.5M   0% /tmp
  /dev/mtdblock6            5.2G     11.8M      4.9G   0% /overlay
  overlayfs:/overlay        1.8M    832.0K    960.0K  46% /
  tmpfs                   512.0K         0    512.0K   0% /dev
  /dev/mmcblk0p2            5.2G     11.8M      4.9G   0% /tmp/run/mountd/mmcblk0p2
  /dev/mmcblk0p1            2.0G      4.0K      2.0G   0% /tmp/run/mountd/mmcblk0p1
  /dev/mmcblk0p2            5.2G     11.8M      4.9G   0% /overlay
```

-  重启ReSpeaker并重新检查。如果SD卡自动安装，就完成了。更多关于extroot的信息，请点击 [这里](https://wiki.openwrt.org/doc/howto/extroot).

#### 5. 在ReSpeaker上安装软件

使用SD卡扩展存储后，有足够的存储空间可以在ReSpeaker上安装软件。

安装git

```
	opkg update
	opkg install git git-http
```

#### 6. 更新 Python 库

```
git clone https://github.com/respeaker/respeaker_python_library.git
cd respeaker_python_library
python setup.py install
```

### 与Respeaker的第一次互动 - ReSpeaker, play music!

使用Bing Speech API，ReSpeaker可以实时打开并识别来自麦克风的音频，或从文件识别音频。

要使用Bing Speech API，首先必须从 [这里](https://www.microsoft.com/cognitive-services/en-us/speech-api) 获取Microsoft Cognitive Services的密钥，并将其复制到BING_KEY =“'，然后将以下代码保存在playmusic.py中并运行

```
//stop mopidy and alexa to avoid USB device occupation
/etc/init.d/mopidy stop
/etc/init.d/alexa stop
python playmusic.py
```

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/getbingapi.png)

```
import logging
import time
import os
from threading import Thread, Event
from respeaker import Microphone
from respeaker.bing_speech_api import BingSpeechAPI

# use madplay to play mp3 file     
os.system('madplay')               

# get a key from https://www.microsoft.com/cognitive-services/en-us/speech-api
BING_KEY = ''      


def task(quit_event):                                                         
    mic = Microphone(quit_event=quit_event)                                   
    bing = BingSpeechAPI(key=BING_KEY)                                        

    while not quit_event.is_set():
        if mic.wakeup('respeaker'):        
            print('Wake up')               
            data = mic.listen()            
            try:                      
                text = bing.recognize(data)
                if text:           
                    print('Recognized %s' % text)
                    if 'play music' in text:
                        print('I will play music!')
                        os.system('madplay Tchaikovsky_Concerto_No.1p.mp3')
            except Exception as e:               
                print(e.message)                 

def main():                                                              
    logging.basicConfig(level=logging.DEBUG)                                                           
    quit_event = Event()        
    thread = Thread(target=task, args=(quit_event,))
    thread.start()                          
    while True:                             
        try:                                
            time.sleep(1)                           
        except KeyboardInterrupt:                   
            print('Quit')                           
            quit_event.set()
            break        
    thread.join()                

if __name__ == '__main__':       
    main()                  
```

在"INFO:mic:Start Detecting" 出来之后，尝试说“ReSpeaker”唤醒程序，唤醒后说“playmusic”让它播放音乐。然后ReSpeaker将使用madplay工具在当前路径中播放“Tchaikovsky_Concerto_No.1p.mp3”

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/bingplaymusic.png)

如果您看到以下错误代码，那么mopidy正在后台运行，并且正在占用USB设备。所以尝试运行 /etc/init.d/mopidy，停止mopidy，然后再重新运行命令。

```
root@ReSpeaker:~# python playmusic.py
Usage: madplay [OPTIONS] FILE [...]
Try `madplay --help' for more information.
Exception in thread Thread-2:
Traceback (most recent call last):
File "/usr/lib/python2.7/threading.py", line 810, in __bootstrap_inner
```


## 应用实例
---

### 水果钢琴

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/fruitpiano.PNG)

  ReSpeaker控制模块是基于ATmega32u4芯片，该芯片完全兼容Arduino驱动。这意味着，我们可以使用ReSpeaker作为强大的Arduino学习板，并做了许多“Arduino”开发板能做的事情。

举个例子，您可以使用Arduino IDE对其进行编程，来实现创意DIY钢琴，该钢琴搭配8个樱桃西红柿连接到ReSpeaker的8个触摸传感器。

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/fruitpiano2.PNG)

  -  1. 在respeaker上输入 git clone https://github.com/respeaker/piano.git      下载库
  -  2. 在您的计算机中下载[ReSpeaker Arduino Library](https://github.com/respeaker/respeaker_arduino_library)
  -  3. 上传piano.ino到ReSpeaker的Arduino Leonardo（ATmega32U4）
  -  4. 在ReSpeaker的串行控制台上运行python piano.py

### 天气云

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/weathercloud.jpg)

天气云是很棒的一个ReSpeaker项目。这个很酷的创意将ReSpeaker变成了一个天气云，它能够显示出生动的光线和声音。

在这个项目中，Openwrt负责从互联网获取实时天气信息，进行语音交互和音频输出，而Arduino负责控制彩色RGB LED。

1. 在respeaker上输入 git clone https://github.com/jerryyip/WeatherCloud.git, 下载项目库文件。
2. 点击下载 [ReSpeaker Arduino Library](https://github.com/respeaker/respeaker_arduino_library) 到您的电脑上，并安装。
3. 通过Arduino IDE将 [pixels_pattern.ino](https://github.com/respeaker/respeaker_arduino_library/blob/master/examples/pixels_pattern/pixels_pattern.ino) 上传到respeaker。
4. 从这里获取OpenWeatherMap appid ，并将其复制到main.py中的appID =“”，不要忘记将您的城市添加到city =“”

5. 在使用SPI之前请终止mopidy service在OpenWrt中的进程，respeaker在控制台上键入
/etc/init.d/mopidy stop
6. 运行python main.py 然后对着它喊 "ReSpeaker, what is the weather like?"
7. 有关如何制作天气的更多详细信息，请点击 [这里](http://www.instructables.com/id/How-to-DIY-an-in-House-Weather-telling-Cloud/).


##   ReSpeaker Mic Array（ReSpeaker 麦克风阵列）
---
### [ReSpeaker Mic Array](https://www.seeedstudio.com/ReSpeaker-Mic-Array-Far-field-w%2F-7-PDM-Microphones--p-2719.html)

ReSpeaker麦克风阵列可以堆叠（连接）到ReSpeaker Core的顶部，以显着提高语音交互体验。它是基于XMOS的XVSM-2000智能麦克风开发的。该板集成了7个PDM麦克风，以帮助将ReSpeaker的声学DSP性能提升到更高的水平

##   关于软件
---
您可页面以点击下列标题来跳转到对应
### [ReSpeaker Arduino 库](https://github.com/respeaker/get_started_with_respeaker/blob/master/ReSpeakerArduinoLibrary.md#respeaker-arduino-library)

ReSpeaker Arudino库提供以下功能：

- 支持电容式触摸感应
- 实现了WS2812 RGB LED驱动
- 构建了从Arduino (ATmega32U4)到基于Linux的OpenWrt (MT7688)之间的USB到串口和USB到SPI通道。                           

### [ReSpeaker Python 库](https://github.com/respeaker/respeaker_python_library)

ReSpeaker是一个支持语音交互的开放项目。ReSpeaker python库是一个开源的python库，用于提供语音交互的基本功能。
它使用PocketSphinx进行关键字查找，并使用webrtcvad进行语音活动检测。



### [更多的信息请点击这里查看我们的github资料库](https://github.com/respeaker)


##   FAQ
---
### Q1: 如何恢复出厂设置?

- 打开串行控制台或ssh会话并运行 firstboot. [更多细节点击这里](https://github.com/respeaker/get_started_with_respeaker/wiki/factory-reset).

### Q2: 如果升级失败了，怎么抢救?

- 升级失败后，当重新启动进入openwrt系统时，我们无法通过网络终端，ssh或串行控制台访问系统。我们可以按照

 [Rescue instruction](https://github.com/respeaker/get_started_with_respeaker/wiki/Rescue-from-a-failed-upgrade) 指令进行恢复。

### Q3: ReSpeaker找不到我的Wi-Fi

- 请先尝试 [恢复出厂设置](https://github.com/respeaker/get_started_with_respeaker/blob/master/faq.md#factory-reset) 。
- ReSpeaker不支持Wi-Fi频道12。确保您的路由器没有使用该通道。.

### Q4: 如何进行Wifi配置

- 我们建议您通过[WEB-UI](https://github.com/respeaker/get_started_with_respeaker/blob/master/QuickStart.md#setup-wi-fi)配置Wi-Fi ，如果无法使用，请在控制台上尝试命令行工具[wictl](https://github.com/respeaker/get_started_with_respeaker/wiki/WiFi) 。


### Q5: 如何改变BING Speech api 的识别语言

- 如果您不需要更改唤醒字，只需将text = bing.recognize（data）更改为text = bing.recognize（data，language =“zh-CN”）就可以了。 [更多信息请点击这里](https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/bing_speech_api.py).


### Q6: 收到SD卡警告消息“卷未正确卸载。某些数据可能已损坏。请运行fsck”

- 如果SD卡上的文件正常，请忽略它。否则，尝试使用[sd卡格式化程序进行格式化](https://www.sdcard.org/downloads/formatter_4/).


### Q7: 错误提示 “Bad flash from Arduino”

- 按照下面代码，在openwrt中重新烧写 bootloade。

```
/etc/init.d/mopidy stop  # stop mopidy if it's running, mopidy-hallo plugin will use SPI
/etc/init.d/alexa stop      # stop alexa if it's running
mt7688_pinmux set ephy gpio
cd /etc/arduino
avrdude -c linuxgpio -p m32u4 -e -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCB:m  -U flash:w:Caterina-ReSpeaker.hex -u -U lock:w:0xEF:m
```

### Q8: 忘记了WebUI的密码

- 重置 juci 密码

```
orangectl passwd root 12345678  //replace 12345678 with the password you want to set
```

### Q9: 如何支持谷歌语音或其他Speach to Text（STT）引擎?

- 按照[指南](https://github.com/respeaker/get_started_with_respeaker/wiki/Use-speech_recognition-python-library)安装speech_recognition库


### Q10: 运行Alexa 错误，提示"IOError: [Errno -9998] Invalid number of channels"

- 还有另一个应用程序或alexa实例使用音频输入设备。运行/etc/init.d/alexa stop和/etc/init.d/mopidy stop 停止它们。要禁用mopidy启动，请运行/etc/init.d/mopidy disable。


### Q11: 无法运行python playmusic.py

- 应该是mopidy在后台运行，并且正在使用USB设备。尝试运行/etc/init.d/mopidy stop, 停止mopidy并再次运行您的命令。


### Q12: 没有RPC连接

- 您需要重新刷固件，点击查看 [指南](https://github.com/respeaker/get_started_with_respeaker/blob/master/QuickStart.md#update-for-old-version)

### Q13: SFTP & FTP
- 我们没有FTP，只有SFTP。


### Q14: 串口控制台被锁定

- 尝试更新 [arduino code](https://github.com/respeaker/respeaker_arduino_library/blob/master/examples/pixels_pattern/pixels_pattern.ino)。

### Q15:如何禁用'ap'模式
- 我们可以在vi / etc / config / wireless 中修改如下 'ssid' flag of the 'ap' interface to '' 。也就是将'ap'改为''。然后就会隐藏ap。

### Q16: I2C声卡问题
- 我们需要检查编解码器驱动程序兼容名以及编解码器i2c地址 然后重建image固件。

### Q17: 即使没有声音，Respeaker也经常被唤醒

- 我们可以通过增加keyword.txt中的阈值来减少误识别率，但也会降低敏感度。
- 另一种方法是将您的声音与当前的声学模块进行匹配，更多的细节参考这里 http://cmusphinx.sourceforge.net/wiki/tutorialadapt。
- 这种方法将有效提高个人关键字识别率，但可能让其他人不被识别。

### Q18: 如何控制Respeaker的GPIO引脚？

- 您可以使用这里的代码 https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/gpio.py
- 以及用这里的例程来通过GPIO模拟SPI https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/spi.py

### Q19: 如何改变唤醒词？

- 在respeaker的 /usr/lib/python2.7/site-packages/respeaker-0.6.0-py2.7.egg/respeaker/pocketsphinx-data  目录下找到并打开[keywords.txt](https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/pocketsphinx-data/keywords.txt)

	```
	respeaker /1e-30/
	alexa /1e-30/
	play music /1e-40/
	```

	respeaker 是关键词, 1e-30 是其阈值。为了提高敏感度，我们可以降低阈值，例如1e-20。值得注意的是，为了提高灵敏度而降低阈值同时会增加错误接受率。

  如果要添加新的关键字，应该首先将关键字添加到 [dictionary.txt](https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/pocketsphinx-data/dictionary.txt) 。dictionary.txt 里的内容如下所示：

	```
	respeaker	R IY S P IY K ER
	alexa	AH L EH K S AH
	play	P L EY
	music	M Y UW Z IH K
	```

	每行的第一部分是关键词的名字 (respeaker, alexa or music), 第二部分是它的音素。你可以在 [这里](https://github.com/respeaker/pocketsphinx-data/blob/master/dictionary.txt) 的字典中找到单词。


  -  然后更改代码： .

	```
	if mic.wakeup('respeaker'):
	```

  小结:如果您想要添加关键词，按照下面的3步。比如添加good morning  

    -  1、在[官方字典](https://github.com/respeaker/pocketsphinx-data/blob/master/dictionary.txt)中查找并添加关键词，以及它对应的音素。
    -  2、在keyword.txt中给 good morning设置一个阈值
    -  3、在您的python代码中添加调用if mic.wakeup('good morning'):

### Q20: 通过出厂固件恢复系统
注意：如果您无法通过网络更新您的ReSpeaker或无法访问http://192.168.100.1/home.html ，请点击[这里](https://s3-us-west-2.amazonaws.com/respeaker.io/firmware/ramips-openwrt-latest-LinkIt7688-squashfs-sysupgrade.bin) 。要将电脑上最新的固件下载到SD卡上，并将SD卡插入ReSpeaker。

连接到respeaker的 [串行控制台](https://github.com/respeaker/get_started_with_respeaker/blob/master/QuickStart.md#serial-console) ，键入以下命令行来更新固件：

```
mount /dev/mmcblk0p1 /mnt
cd /mnt
sysupgrade -n -F ramips-openwrt-latest-LinkIt7688-squashfs-sysupgrade.bin
```
ReSpeaker安装固件和重启大约需要3分钟，更新时**请勿关闭** ReSpeaker。

![](https://github.com/SeeedDocument/Respeaker_Core/raw/master/img/systemupdate2.png)

## 资源下载
----

- **[Eagle原理图]** [ReSpeaker Core v1.0 SCH](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/RespeakerCorev1.0_SCH.sch)
- **[Eagle PCB图]** [ReSpeaker Core v1.0 BRD](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/RespeakerCorev1.0_BRD.brd)
- **[PDF 原理图]** [ReSpeaker Core v1.0 Schematic(pdf)](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/RespeakerCorev1.0_Schematic.pdf)
- **[PDF PCB底板图]** [ReSpeaker Core v1.0 PCB bottom(pdf)](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/RespeakerCorev1.0_PCB_bottom.pdf)
- **[PDF PCB顶板图]** [ReSpeaker Core v1.0 PCB top(pdf)](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/RespeakerCorev1.0_PCB_top.pdf)
