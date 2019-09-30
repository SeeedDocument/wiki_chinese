# Raspberry Pi 4快速入门手册

**Raspberry Pi®** 是 [Raspberry Pi Foundation](http://www.raspberrypi.org) 基于 **ARM** 制造的信用卡大小的 **SBC**（单板计算机）。树莓派运行基于 Debian 的 **GNU / Linux** 操作系统 [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)，并且具有很多其他系统上的端口。

![](https://raw.githubusercontent.com/SeeedDocument/Raspberry-Pi-4/master/img/hardware-overview-1400.jpg)

Raspberry Pi Foundation 宣布了新版本 **Raspberry Pi 4 B** ，详情请查阅 [这里](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)。随着板载 **WiFi** / **Bluetooth** 的支持和新的 64 位处理器，**Raspberry Pi 4 B** 将会成为制造商，工程师和学生最喜爱的开发板。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17798475675.22.41fa7b2dO4iwgp&id=597106720116)

##  Raspberry Pi 4 更新内容

---
|                | 树莓派3B+                   | 树莓派4B                        |
|----------------|-----------------------------|---------------------------------|
| 上市时间       | 2018年3月                   | 2019年6月                       |
| 主芯           | BCM2837B0                   | BCM2711                         |
| CPU            | ARM Cortex-A53 (ARMv8)      | ARM Cortex-A72 (ARMv8)          |
| CPU主频        | 1.4GHz                      | 1.5GHz                          |
| 内存           | 1GB                         | 1GB/2GB/4GB                     |
| USB Host       | 4个2.0                      | 2个2.0和2个3.0                  |
| 显示接口       | 全尺寸HDMI MIPI DSI显示接口 | 2个Micro HDMI 2.0接口(4K 60FPS)   |
| 蓝牙           | BLE 4.2                     | BLE 5.0                         |
| GPIO通用扩展口 | 40Pin                       | 40Pin                           |
| SD卡接口       | Micro SD卡                  | Micro SD卡                      |
| 供电           | 5V/2.5A Micro USB           | 5V/3.0A USB-C                   |

##  入门指导

**准备材料**

- Raspberry Pi 4 B
- Wi-Fi 网络
- 4GB (或更大) SD 卡和 SD 读卡器
- PC 或 Mac
- 用于供电的 5V 3A USB 适配器 (可选的)
- 一根 USB-C 数据线
- 一个Micro HDMI转HDMI接口
- USB键盘和USB鼠标
- 一台带HDMI接口的显示器

<div class="admonition warning">
<p class="admonition-title">注意</p>
请轻轻插入 USB 线，否则可能会损坏接口。请使用内部有 4 根线的 USB 线，2 根线的不能传输数据。如果您不确定您的线，可以点击 <a href="https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html"><B>此处</B></a> 购买
</div>

### 镜像安装

与 Raspberry Pi 3B + 类似，您需要从 SD 卡安装 Raspberry Pi 4 B 映像才能启动并运行。目前我们只提供SD卡启动方式。

**从 SD 卡启动**

**步骤 1.** 点击此处下载 [固件](https://downloads.raspberrypi.org/raspbian_full_latest)


**步骤 2.** 用 SD 读卡器将 SD 卡接入 PC 或 MAC。需要大于 4G 的 SD 卡。


**步骤 3.** <font face="">点击此处下载 <a href="https://etcher.io/">Etcher</a>，然后使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡。或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件，然后用其他镜像写入工具将其刻录到 SD 卡。
<br>
<br>点击加号图标添加刚下载的镜像文件，软件会自动选择您插入的 SD 卡。然后点击 Flash！开始写入。大约需要 10 分钟完成。</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)


**步骤 4.** 将镜像写入 SD 卡后，将 SD 卡插入 Raspberry Pi 4 B。首先接上通过Micro HDMI转HDMI接口将Raspberry Pi 4 B的HDMI接口然后使用USB-C 接口对其进行供电，写入过程中请勿取出 SD 卡。Raspberry Pi 4 B 将从 SD 卡启动。

![](https://projects-static.raspberrypi.org/projects/raspberry-pi-setting-up/e22d152dd4f5bee4e6c932d716bc74c6a2098b69/en/images/pi-desktop.png)

假如您没有无屏幕和键盘也没有关系，您可以接着执行下面的操作也能达到控制访问树莓派的功能。

假如使用我们配套的10寸屏幕，则需要下载 [config.txt](https://github.com/SeeedDocument/Raspberry-4-get-start/blob/master/config.txt),将/boot文件夹下面的config.txt覆盖掉。开机进行下图的屏幕配置即可
![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/Screen-Config.jpg)


### 无屏幕和键盘配置树莓派WiFi和SSH

不算是什么新功能了，在树莓派3B发布后不久，树莓派官方 Raspbian 系统久加入了允许在开机前对 WiFi 网络进行配置的机制。

<div class="admonition warning">
<p class="admonition-title">注意</p>
这个方法仅适用于全新安装树莓派系统到 SD 卡之后没有做过任何 Wi-Fi 配置的情况下有效。如果你之前配置过 Wi-Fi，再用本方法系统会默认使用已有的配置而忽略这里的配置。因此建议使用前重新安装系统。
</div>

**步骤 1.** 用户可以在未启动树莓派的状态下单独修改 /boot/wpa_supplicant.conf 文件配置 WiFi 的 SSID 和密码，这样树莓派启动后会自行读取 wpa_supplicant.conf 配置文件连接 WiFi 设备。

操作方法简单：将刷好 Raspbian 系统的 SD 卡用电脑读取。在 boot 分区，也就是树莓派的 /boot 目录下新建 wpa_supplicant.conf 文件，按照下面的参考格式填入内容并保存 wpa_supplicant.conf 文件。

```bash
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
 
network={
ssid="WiFi名称"
psk="WiFi密码"
key_mgmt=WPA-PSK
priority=1
}
```

如果你不清楚 WiFi 的加密模式，可以在安卓手机上用 root explorer 打开 /data/misc/wifi/wpa/wpa_supplicant.conf，查看 WiFi 的信息。

**步骤 2.** 如果通过 ssh 连接树莓派出现 Access denied 这个提示则说明 ssh 服务没有开启。要手动开启的话，和 WiFi 配置相似，同样在 boot 分区新建一个文件，空白的即可，文件命名为 ssh。注意要小写且不要有任何扩展名。

**步骤 3.** 下载ssh访问工具，一般常使用的是 [putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)。随后即可通过登录路由器找到树莓派的 IP 地址，通过 ssh 连接到树莓派了。

![](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/img/putty.png)

进入终端后请输入用户名和密码，分别是‘pi’和‘raspberry’

```
login as: pi
pi@192.168.43.210's password:raspberry
```

### 树莓派VNC服务

假如您需要远程显示树莓派的桌面，那么我们需要进行vnc的配置。假如上面的教程顺利的话，你已经可以访问树莓派终端了。

**步骤 1.** 在终端输入以下命令进入配置界面

```bash
sudo raspi-config
```
**步骤 2.** 按照图片的顺序进行配置

![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/vnc_1.png)
![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/vnc_2.png)
![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/vnc_4.png)
![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/vnc_3.png)

**步骤 3.** 下载 [Real vnc](https://www.baidu.com/link?url=iW6RVDaZdafJwUX4boQhLuh7MNRw4HkAi4QgoqmnfDXU4bT46q_bCJmDjLUpERyvWlFnof0B4D4VDeaZYD51Ea&wd=&eqid=a185411b00045afd000000065d4beff3)安装并打开，输入树莓派的IP

![](https://github.com/SeeedDocument/Raspberry-4-get-start/raw/master/img/vnc_display.png)