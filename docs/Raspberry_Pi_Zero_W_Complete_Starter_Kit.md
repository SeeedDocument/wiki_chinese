---
title: Raspberry Pi Zero W Complete Starter Kit
category: Raspberry Pi
bzurl: https://www.seeedstudio.com/Seeedstudio-Raspberry-Pi-Zero-W-Complete-Starter-Kit-p-2968.html
oldwikiname: Raspberry_Pi_Zero_W_Complete_Starter_Kit
prodimagename: Raspberry_Pi_Zero_W_Complete_Starter_Kit.jpg
wikiurl: http://seeed.wiki/Raspberry_Pi_Zero_W_Complete_Starter_Kit
sku: 110991029
---

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_Complete_Starter_Kit/raw/master/img/1.jpg)

Pi Zero W 入门套件包含您需要的一切。您可以轻松地与您的 Pi Zero W 组装在一起。

小巧超薄 Raspberry Pi Zero W 是目前市场上最小的外形树莓派，现在又具有了 WiFi 和蓝牙功能。它比原来的树莓派快 40％，但尺寸只有 65 毫米长，30 毫米宽，5 毫米高。Raspberry Pi Zero W 支持迷你连接器以节省空间，而 40 引脚 GPIO 未焊接，因此可以根据您的项目所需的连接灵活使用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.11891debNA69TQ&id=559266384210)

## 产品特性
--------
-   1GHz，单核 CPU
-   512MB RAM
-   迷你 HDMI 端口
-   Micro-USB OTG 端口
-   微型 USB 电源
-   40 针插头，兼容树莓派扩展板
-   合成视频信号和重置引脚
-   CSI 相机连接器 (仅限 v1.3)
-   802.11 b/g/n 无线局域网
-   蓝牙 4.1
-   低功耗蓝牙 (BLE)

## 规格参数
--------

| 零件名称                   | 功能描述                                                                                              |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| Pi Zero W 主控板           | 具有 Pi Zero 的所有功能，且增加了连接功能，包括 802.11 b/g/n 无线局域网，蓝牙 4.1 和低功耗蓝牙（BLE） |
| Mini HDMI OTG 线           | 适用于迷你 HDMI---标准 HDMI 插孔                                                                      |
| Micro USB OTG 线           | Micro USB 转 Type A，可将 Wi-Fi dongle，mouser，touchpad 等与 Pi Zero 连接                            |
| 2x20 引脚公头              | 将其焊接到 Pi HAT，GPIO 等中，就像插入普通的 Pi 模块上一样                                            |
| 2x20 引脚母头              | 将其焊接到 GPIO 端口位置，使其 GPIO 端口被充分利用                                                    |
| 官方 Raspberry Pi 相机带   | 连接相机与 Pi Zero W 板子                                                                             |
| Pi Zero Case               | 三款可选，确保您的 Pi Zero 安全和光滑                                                                 |
| 8Gb Micro TF卡             | NOOBS 预装，Raspbian 不是 Pi 开发板仅有的选择                                                         |
| 5V 1.5A 电源适配器（美标） | 1.5A 电源适配器是 Pi zero W 的理想选择，美标且 FCC 和 CE 认证                                         |

## 配送清单
--------

| 零件名称                   | 数量 |
|----------------------------|------|
| Pi Zero W 主控板           | 1    |
| Mini HDMI OTG 线           | 1    |
| Micro USB OTG 线           | 1    |
| 2x20 引脚公头              | 1    |
| 2x20 引脚母头              | 1    |
| 官方 Raspberry Pi 相机带   | 1    |
| Pi Zero Case               | 1    |
| 8Gb Micro TF卡             | 1    |
| 5V 1.5A 电源适配器（美标） | 1    |

## 使用方法
--------

本指南介绍如何在不需要连接键盘/鼠标/监视器的情况下使用 Raspberry Pi Zero 或 Zero W。感谢 Adafruit 提供的指南。基本设置将通过在首次启动之前使用您的 PC 上的编辑器直接在 SD 卡上编辑文本文件进行配置。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/2.jpg)

!!!Note
    在本指南中，Pi Zero 同时代表 Zero 和 Zero W。

Pi Zero 没有太多闪烁的 LED 给您一种温馨的感觉，它正在工作，甚至还活着。如果 GPU 找不到有效的操作系统映像，它甚至不会点亮绿色的 ACT LED，看起来完全死了。通常这只是 SD 卡有问题。不过，这并不意味着 Pi Zero 已经死了。

!!!Note
    Pi Zero 没有电源 LED 指示灯。

按照以下步骤检验 Pi Zero 的状态 :

-   拿出插槽没插任何东西的 Pi Zero (这个测试不需要 SD 卡)。
-   将一个普通的 micro-USB 转 USB-A DATA SYNC 线缆 (不仅是充电线!请确保它是真正的数据同步线缆!)
-   将 USB 线缆连接到 PC，将 micro-USB 插入 Pi 的 USB 端口 (不是 PWR_IN)。
-   如果 Zero 还活着，那么您的 Windows PC 将会出现新硬件，您会在设备管理器中看到 "BCM2708 Boot"。
-   或者在 Linux 上运行 sudo lsusb 或运行 dmesg 并查找 ID 0a5c:2763  Broadcom Corp 消息。如果您看到了，恭喜您 Pi Zero 还没死。

下面是一个通过 USB 线缆连接到 Linux 计算机的 Pi Zero 以及由此产生的 dmesg 输出。

!!!Note
    没有安装 SD 卡，USB 线缆插在 USB 端口，并且没有灯。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/3.jpg)

以下是Windows PC 显示的内容 :

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/4.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/5.png)

### 安装操作系统

本指南使用 Raspbian Stretch Lite 作为起点。点击 [这里](https://www.raspberrypi.org/downloads/raspbian/) 下载最新版本。

您会得到一个 .zip 文件。解压后得到一个 .img 文件。然后按照这些出色的说明将操作系统映像烧录到 SD 卡上 :

点击 [这里](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) 查看 Raspberry Pi 官方说明。

点击 [这里](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi/make-a-backup-image) 查看 adafruit 说明。

您生活在一个整个操作系统可以在小于您的指尖的塑料薄片上运行的世界。而且您可以在一台 5 美元 (或 10 美元) 的计算机上运行，这台计算机足够小，甚至可以放在杂志封面上。意不意外，惊不惊喜。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/6.jpg)

### 文本文件编辑

如果您成功烧录了操作系统映像，您会在计算机上看到名为 boot 的文件夹。如果没有，请尝试取出并重新插入 SD 卡。如果仍然没有，请尝试重新烧录操作系统映像。

在 boot 文件夹中有三个文本文件我们将创建/编辑。

- 1.wpa_supplicant.conf - wifi settings
- 2.config.txt - global system settings
- 3.ssh - an empty text file to enable ssh

我们将在将它们放入 Pi Zero 之前直接在 SD 卡上编辑。这样，您可以在计算机上使用您最喜爱的图形文本编辑器来编辑这些文件。尽量避免使用文字处理器。

### 配置 Wifi

Pi Zero W 内置 WiFi，因此不需要额外的附件。如果您使用的是 Pi Zero，则需要某种形式的 WiFi 适配器和连接方式 : 线缆或适配器。

WiFi 配置文件不存在，需要创建。该文件的名称是 wpa_supplicant.conf，并且它的内容将在启动时被复制到系统文件夹。然后它将被删除。所以这是一个只有一次的过程。如果您想再次尝试，则必须重新创建该文件并重新启动。

该文件的内容应如下所示。将 YOURSSID 和 YOURPASSWORD 替换为用于您的网络设置的内容。

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="YOURSSID"
    psk="YOURPASSWORD"
    scan_ssid=1
}
```

保存文件并继续下一步。

### 启用 UART

名为 config.txt 的文件已经存在，我们将要编辑它的内容。我们将在底部添加一些文本以启用 GPIO 引脚上的 UART。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/7.jpg)

在文本编辑器中打开文件，并在底部添加以下文本。

```
# Enable UART
enable_uart=1
```

像这样 :

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/8.jpg)

### 启用 SSH

SSH 默认启用，但之后 (2016 年 11 月) 默认关闭。这是由于安全问题，因为 pi 用户 ID 和密码是众所周知的。但是，您也可以启用此功能，以便您可以远程连接到 Pi Zero。

为此，我们只需创建一个名为 ssh 的文件。该文件不存在，需要创建。它可以是空的。系统在启动时查找它，如果它在那里，将启用 ssh。然后它被删除。所以，只需创建一个新文件并将其保存为 ssh 到启动文件夹即可。

### 最终检查

完成上述步骤后，您应该在 SD 卡中的 boot folder 中包含以下文件。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/9.jpg)

从计算机取出 SD 卡并将其安装在 Pi Zero 中。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/10.jpg)

### 赋予 Pi Zero 生命

现在上电，插入 SD 卡后，如图所示，通过 USB 线缆向 POWER IN 接口供电。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/11.jpg)

可以看到绿色的 LED 灯有所反应。这意味着 Pi Zero 找到了一个适用的操作系统映像并且正在启动。

一两分钟后，可以查看它是否已连接到您的网络。您可以使用 mDNS style addressing 访问 Pi Zero。Windows 用户需要一些额外的设置。在 [这里](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/#microsoft-windows) 阅读。

```
ping -c 3 raspberrypi.local
```

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/12.jpg)

您也应该能够通过 SSH 访问 Pi Zero。

```
ssh pi@raspberrypi.local
```

默认密码是 raspberry。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/13.png)

### 建议的初始设置

下一步干什么完全取决于您个人。但是，首先运行系统更新是一个好主意。通过 ssh 连接到 pi 并运行以下命令 :

```
sudo apt-get update
sudo apt-get upgrade
```

这两个命令可能需要一段时间才能完成。Raspbian Lite 是一个非常小的安装，所以您的下一步可能会安装一堆软件包。通过先运行以上，您将安装最新的版本。

### 系统配置

通用系统配置通过运行 raspi-config 工具来完成。

```
sudo raspi-config
```

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/14.png)

这将弹出主菜单。

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/15.png)

现在可以将密码更改为非默认密码。您还可以执行其他操作，例如更改时区，键盘布局，主机名等。

### 启用 SPI 和 I2C

SPI 和 I2C 在很多项目中都会使用，但默认情况下是禁用的。现在启用它们吧!

SPI

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/16.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/17.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/18.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/19.png)

I2C

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/20.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/21.png)

![](https://github.com/SeeedDocument/Raspberry_Pi_Zero_W_with_Official_Case/raw/master/img/22.png)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Raspberry_Pi_Relay_Board_v1.0 -->
