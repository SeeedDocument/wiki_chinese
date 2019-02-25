---
name: application Dueros
category: Respeaker
---

![]()

百度 DuerOs 在 2017 年放出了 DuerOs 的 Python 版本，其测试环境为 Ubuntu 系统。为了在树莓派上使用 DuerOs ，本文交叉编译了 OpenSSL 和 Python，使得这个 DuerOs 可以在树莓派上使用。

此文从 [百度开发者中心](https://dueros.baidu.com/forum/topic/list) 搬运，感谢作者 [EddyLiu](http://open.duer.baidu.com/forum/user/center/898378) 的 [原文](http://open.duer.baidu.com/forum/topic/show/244796)。

## 准备 DuerOs 系统

由于现在百度官方的 DuerOs 资源已更新，不能适用于本教程，所以放上了以前操作前的备份。

原版：[DuerOs for Raspberry Pi](https://pan.baidu.com/s/16Z0CLhDMqio_3RjGIPRAbQ)，提取码 221f。这个版本是官方版本，未做修改，需要自己动手完成下面的过程。适用于能解决潜在 BUG 的开发者。

配置完成的镜像：[正在上传中...]()，该镜像是完成下面所有步骤后的 SD 卡镜像，适用于遇到问题无法解决的情况或想直接应用的开发者。在烧录后配置声卡，网络，即可直接唤醒使用。

## 开始配置

下面的步骤适用于原版系统。

### 1.停止现有小度功能，因为会占用 MIC 资源

```
sudo systemctl disable duer
sudo systemctl stop duer
```

### 2.安装依赖包

```
sudo apt-get update
sudo apt-get install python-dateutil
sudo apt-get install gir1.2-gstreamer-1.0
sudo apt-get install python-pyaudio
sudo apt-get install libatlas-base-dev
sudo apt-get install python-dev
sudo pip install tornado
sudo pip install hyper
```

hyper 库用来支持 http2.0 client, pyaudio 用来支持录音，tornado 用来完成 oauth 认证。

### 3.下载编译好的 openssl 和 Python 安装包，并进行安装, 需要更新 openssl 才能支持 python sdk 的使用。

[点击下载 openssl 安装包](https://pan.baidu.com/s/13QSqy22X_vrQhB7C7v-vDQ)，提取码 f3h0。
[点击下载python2.7.14安装包](https://pan.baidu.com/s/1wsAR1LG5O7Zlet_pG4mexQ)，提取码 p91x。

```
sudo tar -zxvf openssl1.1.tar.gz -C /usr
sudo tar -zxvf python2.7.14.tar.gz -C /usr/local/
sudo rm -rf /usr/bin/python
sudo ln -s /usr/local/python2.7.14/bin/python /usr/bin/python
```

### 4.下载 Python SDK 和参考示例代码

```
git clone https://github.com/MyDuerOS/DuerOS-Python-Client.git
cd DuerOS-Python-Client
git checkout raspberry-dev
```

## 运行和测试

### 安装驱动

本文使用 [Respeaker 4-Mics Pi HAT](https://item.taobao.com/item.htm?spm=a1z10.1-c.w13838425-11172345252.1.542035bczDBegW&id=557884254210) 作为麦克风输入。

#### 1.使用前需要线安装麦克风阵列的驱动程序。

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh 4mic
reboot
```

#### 2.选择Raspberry Pi上的耳机插孔进行音频输出：

```
sudo raspi-config
# Select 7 Advanced Options
# Select A4 Audio
# Select 1 Force 3.5mm ('headphone') jack
# Select Finish
```

#### 3.使用 arecord -L 检查声卡名称如下所示：

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

#### 4.测试驱动：用 arecord 录制，然后用 aplay 播放：

```
arecord -Dac108 -f S32_LE -r 16000 -c 4 hello.wav    // 只支持4通道
aplay hello.wav                                      // 确保选择默认设备。声音通过树莓派的 aux 输出
```

### 运行 alsamixer 调整音量

运行 alsamixer 调试输入以及输出声音大小。 利用 2mic/4mic/mic arra y采集数据，4mic 使用树莓派 audio port 作为输出。因为默认的输出声音很小，听不到声音，所以配置好输入输出的音量。

### 授权

```
./auth.sh
```

在树莓派百度授权的时候，无法成功获取授权，请拷贝树莓派上的网页地址，**在 PC 端打开**。然后登陆百度，并且授权。最后生成127.0.0.1/XXX的网址，复制回到树莓派上，并且运行即可。

本文使用使用默认的 client_id 和 client_secret，开发者可以替换为自己的 client_id 和 client_secret，以实现多样化应用。

### 唤醒

输入下面的命令，然后用“小度小度”唤醒它：

```
./wakeup_trigger_start.sh
```

享受你的 DuerOs 吧，还有更多精彩等你发掘。
