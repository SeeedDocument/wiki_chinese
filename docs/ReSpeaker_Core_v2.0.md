---
name: ReSpeaker Core v2.0
category: ReSpeaker
bzurl:
oldwikiname: ReSpeaker Core v2.0
prodimagename: cover.JPG
surveyurl:  https://www.research.net/r/Respeaker_Core
sku: 102990883
---

![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/ReSpeaker_V2_front.JPG)

Seeed 的 ReSpeaker Core v2.0 专为语音接口应用而设计。它基于四核 ARM Cortex A7 的 Rockchip RK3229，运行频率高达 1.5GHz，具有 1GB RAM。集成六个麦克风阵列，语音算法包括 DoA (波达方向定位技术)，BF (波束成形)，AEC (回声消除)等。

ReSpeaker Core v2.0 运行 GNU/Linux 操作系统。得益于功能强大且活跃的社区，可以使用现有软件和工具进行开发，测试和部署，从而实现产品的快速开发。

ReSpeaker Core v2.0 被设计为功能丰富的开发板。电路板由两个主要部分组成，第一部分是包含 CPU，内存 (RAM) 和 PMU 的中央核心模块。第二部分是包含如 eMMC，连接器和无线连接组件等外设的外部载板。可以通过 Seeed 的定制服务来定制其中一部分或两者。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.32b933dbxKpk6v&id=566241590290)

## 产品特性

- 具有高性能SoC的一体化解决方案
- 1GB RAM & 4GB eMMC
- 6 麦克风阵列  
- USB OTG 可外接 USB 设备
- WiFi b/g/n 和 BLE 4.0
- 检测范围 : 约 5 米
- Grove 接口
- 3.5mm 音频插孔和 JST2.0 连接器
- 8 通道 ADC，6 个用于麦克风阵列，2 个用于回采
- 基于 Debian 的 Linux 系统
- C++ SDK 和 Python 封包
- 用于语音算法的 SDK
- 语音算法和功能 :

    - 关键词唤醒
    - BF (波束成形)
    - DoA (波达方向定位技术)
    - NS (噪声抑制)
    - AEC (回声消除) 和 AGC (自动增益控制)

## 规格参数


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#ccc;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#f0f0f0;}
.tg .tg-dc35{background-color:#f9f9f9;border-color:inherit;vertical-align:top}
.tg .tg-l711{border-color:inherit}
.tg .tg-us36{border-color:inherit;vertical-align:top}
.tg .tg-4646{background-color:#f9f9f9;border-color:inherit}
.tg .tg-gcw3{border-color:#000000}
</style>
<table class="tg">
  <tr>
    <th class="tg-gcw3" colspan="3">项目</th>
  </tr>
  <tr>
    <td class="tg-4646" rowspan="6">Soc(Rockchip RK3229)</td>
    <td class="tg-4646">CPU</td>
    <td class="tg-4646">四核 Cortex-A7，运行频率高达 1.5GHz</td>
  </tr>
  <tr>
    <td class="tg-l711">GPU</td>
    <td class="tg-l711">Mali400MP, 支持 OpenGL ES1.1/2.0</td>
  </tr>
  <tr>
    <td class="tg-dc35">内存</td>
    <td class="tg-dc35">1GB RAM(核心模块包括 RAM 和 PMU)</td>
  </tr>
  <tr>
    <td class="tg-us36" rowspan="3">系统</td>
    <td class="tg-us36">工作电压:3.6-5V</td>
  </tr>
  <tr>
    <td class="tg-dc35">板载 80 针</td>
  </tr>
  <tr>
    <td class="tg-us36">板载 PMU</td>
  </tr>
  <tr>
    <td class="tg-dc35" rowspan="7">外设</td>
    <td class="tg-dc35">网络</td>
    <td class="tg-dc35">WiFi b/g/n;<br>BLE 4.0;<br>Ethernet</td>
  </tr>
  <tr>
    <td class="tg-us36">USB</td>
    <td class="tg-us36">2 x USB Host;   1 x USB OTG;    1 x USB power</td>
  </tr>
  <tr>
    <td class="tg-dc35">Grove</td>
    <td class="tg-dc35">1 x Grove 接口 (I2C 和 Digital)</td>
  </tr>
  <tr>
    <td class="tg-us36">视频</td>
    <td class="tg-us36">支持 HDCP 1.4/2.2 协议的 HDMI 2.0，频率高达 4K/60Hz</td>
  </tr>
  <tr>
    <td class="tg-dc35">音频</td>
    <td class="tg-dc35">6 麦克风阵列;<br>3.5mm 音频插孔;<br>JST2.0 音频输出连接器</td>
  </tr>
  <tr>
    <td class="tg-us36">存储</td>
    <td class="tg-us36">板载 4GB eMMC;<br>SD 卡插槽</td>
  </tr>
  <tr>
    <td class="tg-dc35">其他</td>
    <td class="tg-dc35">12 x RGB LED;<br>8 GPIO 引脚</td>
  </tr>
  <tr>
    <td class="tg-us36" rowspan="2">功耗</td>
    <td class="tg-us36">待机模式</td>
    <td class="tg-us36">200mA /5V</td>
  </tr>
  <tr>
    <td class="tg-dc35">使用算法模式</td>
    <td class="tg-dc35">330mA /5V</td>
  </tr>
</table>

!!!Note
    本表仅列出了 ReSpeakser Core v2.0 的基本规格参数，更多专业参数请参考 [Acoustic & Electrical Specification of ReSpeaker Core v2.0](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/Acoustic%26Electrical_Specification_of_ReSpeaker_Core_v2.0.pdf)。

## 硬件概述

**接口和存储**

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/hardware_overview.png)


- <font face="" size=3 font color="ff0000">①</font> **3.5mm 耳机插孔 : **
输出音频。可以将有源扬声器或耳机插入此端口。

- <font face="" size=3 font color="ff0000">②</font> **USB OTG : **
此 USB 端口用于通过 putty (或其他串口工具) 的串口模式连接到您的计算机。

- <font face="" size=3 font color="ff0000">③</font> **USB 电源输入 : **
此端口用于为 Respeaker Core v2.0 供电。

- <font face="" size=3 font color="ff0000">④</font> **扬声器插孔 : **
用于无源音响的输出音频。Jst 2.0 插座。

- <font face="" size=3 font color="ff0000">⑤</font> **UART : **
可以通过此 UART 端口将 ReSpeaker Core v2.0 与您的计算机连接。

- <font face="" size=3 font color="ff0000">⑥</font> **8 GPIO 引脚 : **
用于扩展应用的 GPIO。

- <font face="" size=3 font color="ff0000">⑦</font> **SD 卡槽 : **
插入 micro-SD 卡。

- <font face="" size=3 font color="ff0000">⑧</font> **eMMC : **
Embedded Multi Media Card。您可以将镜像刻录到 eMMC 中，这样 ReSpeaker Core v2.0 可以从 eMMC 引导。

- <font face="" size=3 font color="ff0000">⑨</font> **USB Host : **
您可以通过这两个 USB Host 将 USB 设备 (如 USB 鼠标，USB 键盘和 USB 闪存盘) 插入 ReSpeaker Core v2.0。

- <font face="" size=4 font color="ff0000">Ⓐ</font> **Ethernet : **
访问互联网。

- <font face="" size=4 font color="ff0000">Ⓑ</font> **HDMI : **
输出视频。

- <font face="" size=4 font color="ff0000">Ⓒ</font> **Bluetooth 及 WIFI 天线 : **
用于 WIFI 和蓝牙的板载天线。我们还为 2.4G 天线和 PCB 天线提供了接口。

- <font face="" size=4 font color="ff0000">Ⓓ</font> **Grove 接口 : **
用于数字或 I2C 的 Grove 接口。


**引脚图**

**引脚定义**

| 8 针接头 | Grove 接口 |
|--------------|-------------|
| ![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/GPIO.png)|![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/socketBLACK.png)|

**GPIO 引脚**

MRAA|	接口引脚号 |	SYSFS 引脚	|RK3229 引脚
--|--|--|--
0	|0|	1091|	GPIO2_D3
1	|1|   --|	VCC
2	|2| 1043|	GPIO1_B3
3	|3|	1127|	GPIO3_D7
4 |4|	1017|	GPIO0_C1
5	|5|	1067|	GPIO2_A3
6	|6|	  --| GND
7	|7|	1013| GPIO0_B5
8	|8|	1085|	GPIO2_C5
9	|9|	1084|	GPIO2_C4
10|10|	--|	VCC
11|11|	--|	GND

**I2C 引脚**

|MRAA	|接口引脚号	|SYSFS 引脚|	RK3229 引脚|
|--|--|--|--|
|0	|8	|--	|I2C2_SCL|
|0	|9	|--	|I2C2_SDA|


**尺寸图**

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Dimension_2.png)

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Dimension_1.png)


## 创意应用

- 智能音响
- 智能语音助理系统
- 录音机
- 会议语音系统
- 会议通信设备
- 语音交互机器人
- 汽车语音助手
- 其他需要语音命令的场景


## 入门指导

### 准备工作


**准备材料**

- ReSpeaker Core V2.0
- Wi-Fi 网络
- 4GB (或更大) SD 卡和 SD 读卡器
- PC 或 Mac
- [USB To Uart Adapter](https://www.seeedstudio.com/USB-To-Uart-5V%26amp%3B3V3-p-1832.html) (可选的)
- 用于供电的 5V 1A Micro-USB 适配器 (可选的)
- 两根 Micro-USB 线

<div class="admonition warning">
<p class="admonition-title">注意</p>
请轻轻插入 USB 线，否则可能会损坏接口。请使用内部有 4 根线的 USB 线，2 根线的不能传输数据。如果您不确定您的线，可以点击 <a href="https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html"><B>此处</B></a> 购买
</div>


**镜像安装**

与 Raspberry Pi 类似，您需要从 SD 卡安装 ReSpeaker Core v2.0 映像才能启动并运行。我们提供两种启动 ReSpeaker Core v2.0 的方法。您可以从 SD 卡启动或从 eMMC 启动。

**A. 从 SD 卡启动**

点击此处下载 [固件](https://v2.fangcloud.com/share/7395fd138a1cab496fd4792fe5?folder_id=188000311814)


- **步骤 1.** 点击上面的 OneDrive 图标下载最新的镜像压缩文件 : ```respeaker-debian-9-lxqt-sd-********-4gb.img.xz``` 或 ```respeaker-debian-9-iot-sd-********-4gb.img.xz```.


|选项|说明|
|---|----|
|**iot** / **lxqt**|**lxqt** 版本附带桌面图形用户界面，而 **iot** 版本没有。如果您才接触 ReSpeaker Core v2.0，建议使用 **lxqt** 版本。|
|**flasher** / **sd**|**flasher** 版本用于向板载 eMMC 烧录，烧录完成后可以取出 SD 卡。**sd** 版本要求 SD 卡始终保持插入状态。|

  对于开发用户，我们推荐使用 **lxqt + sd** 版本。所以请下载 **respeaker-debian-9-lxqt-sd-[date]-4gb.img.xz** 文件。

  <div class="admonition warning">
  <p class="admonition-title">注意</p>
  此 wiki 基于 **respeaker-debian-9-lxqt-sd-20180319-4gb.img.xz** 镜像版本.
  </div>

- **步骤 2.** 用 SD 读卡器将 SD 卡接入 PC 或 MAC。需要大于 4G 的 SD 卡。


- **步骤 3.** <font face="">点击此处下载 <a href="https://etcher.io/">Etcher</a>，然后使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡。或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件，然后用其他镜像写入工具将其刻录到 SD 卡。
<br>
<br>点击加号图标添加刚下载的镜像文件，软件会自动选择您插入的 SD 卡。然后点击 Flash！开始写入。大约需要 10 分钟完成。</font>

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/v2-flash-sd.png)


- **步骤 4.** 将镜像写入 SD 卡后，将 SD 卡插入 ReSpeaker Core v2.0。使用 PWR_IN micro USB 端口为主板供电，写入过程中请勿取出 SD 卡。ReSpeaker Core v2.0 将从 SD 卡启动，您可以看到 USER1 和 USER2 LED 点亮。USER1 配置为启动时以心跳模式闪烁，而 USER2 配置为启动时在 SD 卡访问期间亮起。现在，转到下一部分 : 串口控制台。


**B. 从 eMMC 启动**

EMMC 出厂时没有固件，您可以使用 PC 或 Mac 将 ReSpeaker 镜像文件写入到 ReSpeaker 的 eMMC (板载闪存)。然后 ReSpeaker 将从它的 eMMC 启动，而不是 SD 卡。

- **步骤 1.** 在 OneDrive 下载最新镜像压缩文件 : ```respeaker-debian-9-iot-flasher-********-4gb.img.xz``` 或 ```respeaker-debian-9-lxqt-flasher-********-4gb.img.xz```。lxqt 版本附带桌面图形用户界面，而 iot 版本没有. flasher 版本用于向板载 eMMC 烧录, sd 版本从 SD 卡启动。

- **步骤 2.** 使用 Etcher 将 ```*.img.xz``` 文件直接写入到 SD 卡。或者将 ```*.img.xz``` 文件解压缩为 ```*.img``` 文件，然后用其他镜像写入工具将其刻录到 SD 卡。

- **步骤 3.** 将镜像写入 SD 卡后，将 SD 卡插入 ReSpeaker Core v2.0。使用 PWR_IN micro USB 端口为主板供电，写入过程中请勿取出 SD 卡。

在写入过程中，您会看到 USER1 和 USER2 LED 交替闪烁。大约需要 10 分钟完成。当 LED 熄灭后您可以断电，拔出 SD 卡并重新上电。如果 LED 指示灯亮起，表示镜像成功写入到 eMMC。

可以使用以下命令检查映像版本 : cat /etc/issue.net。


**串口控制台**

现在您的 ReSpeaker Core v2.0 可以启动，您可能希望通过控制台访问 Linux 系统，设置 WiFi 等。有两种方法 :

- A. OTG USB 端口 - 需要在电路板上运行 Linux 系统

- B. UART 端口 - 用于调试低级问题


**A. 通过 OTG 连接**

- **步骤 1.** 找一条 micro USB 线，并确保它是数据线，插入 ReSpeaker 的 **OTG**  micro USB 端口 (ReSpeaker 板上有两个 micro USB 端口，有不同的丝印层，一个是 **PWR_IN** ，另一个是 **OTG**)，然后将 micro USB 线的另一端插入电脑。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/lianjiediannan.jpg)

- **步骤 2.** 检查计算机串口是否启用 :

    - Windows : 检查设备管理器，应该有新的串行设备名为 ```COMx```，其中 x 是一个越来越大的数字。如果您使用 windows XP/7/8，也许需要安装 [windows CDC 驱动程序](https://github.com/respeaker/get_started_with_respeaker/blob/master/files/ReSpeaker_Gadget_CDC_driver.7z)。
    - Linux : ls ```/dev/ttyACM*```，应该得到 ```/dev/ttyACMx``` 其中 x 取决于您使用的 USB 端口.
    - Mac : ls ```/dev/cu.usb*```，应该得到 ```/dev/cu.usbmodem14xx``` 其中 xx 取决于您使用的 USB 端口。


- **步骤 3.** 使用您最喜欢的串口调试工具来连接串口，串口有 : 115200 波特率，8 位，奇偶校验无，停止位 1，流量控制无。举些例子 :

    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)，选择 ```Serial``` 协议，填入 ReSpeaker Core v2.0 对应的 COM 端口，```115200``` 波特率，8 位，奇偶校验无，停止位 1，流量控制无。
    - Linux : 取决于 USB To TTL Adapter，应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```
    - Mac : 取决于 USB To TTL Adapter，应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```


- **步骤 4.** 默认用户名是 ```respeaker```，密码也是 ```respeaker```。


**B. 通过 UART 端口连接**

在本节中，我们将引导您使用将连接到 ReSpeaker 的 Uart 端口 (位于 ReSpeaker 扬声器插头左侧) 的 USB 转 TTL 适配器，建立计算机与 ReSpeaker 的连接。

- **步骤 1.** 使用 USB To TTL Adapter 连接 Uart 端口和 PC/Mac。请注意，RX/TX 的电压为 3.3V。如果您没有 USB To TTL Adapter，点击 [此处](https://item.taobao.com/item.htm?id=550981934087) 购买.

- **步骤 2.** 使用以下串口调试工具，波特率为 115200 :
    - Windows : 使用 [PUTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)，选择 ```Serial``` 协议，填入 ReSpeaker Core v2.0 对应的 COM 端口，```115200``` 波特率，8 位，奇偶校验无，停止位 1，流量控制无。
    - Linux : 取决于 USB To TTL Adapter，应该是 ```screen /dev/ttyACM0(,1, and so on) 115200``` 或 ```screen /dev/ttyUSB0(,1, and so on) 115200```。
    - Mac : 取决于 USB To TTL Adapter，应该是 ```screen /dev/cu.usbserial1412(,1422, and so on) 115200``` 或 ```screen /dev/cu.usbmodem1412(,1422, and so on) 115200```。

- **步骤 3.** 登录用户名是 respeaker，密码也是 respeaker。

- **步骤 4.** 如果没有 USB to TTL Adapter，也可以使用 Arduino。如果使用 Arduino，将跳线的一端连接到 Arduino 的 RESET 引脚，另一端连接到 Arduino 的 GND 引脚。这将绕过您的 Arduino 的 ATMEGA MCU，并将您的 Arduino 转换为一个 USB to TTL adapter，请参看 [此处](https://www.youtube.com/watch?v=qqSLwK1DP8Q) 的视频教程。现在将 Arduino 的 GND 引脚连接到 Respeaker 的 Uart 端口的 GND 引脚。将 Arduino 上的 Rx 引脚连接到 Respeaker 的 Uart 端口上的 Rx 引脚。将 Arduino 上的 Tx 引脚连接到 Respeaker 的 Uart 端口上的 Tx 引脚。最后，通过 Arduino 的 USB 电缆将 Arduino 连接到 PC/Mac。现在通过输入以下命令检查您的 PC/Mac 是否找到您的 Arduino :

```
ls /dev/cu.usb* (Mac)
ls /dev/ttyACM* (Linux)
```
应该得到类似这样的反馈 :

```
/dev/cu.usbmodem14XX where XX will vary depending on which USB port you used (on Mac)
/dev/ttyACMX where X will vary depending on which USB port you used  (on Linux)
```
现在按照上述步骤 2 通过此串行连接连接到 Respeaker。并且注意这是一次性过程，因为您将接下来设置 Respeaker 进行 Wi-Fi 连接，然后通过 ssh 或 VNC 进行连接。



**网络设置**

**A. Wi-Fi 设置**

通过网络管理工具 nmtui 配置 ReSpeaker 的网络，nmtui 已经安装在 ReSpeaker 的镜像上。

```
respeaker@v2:~$ sudo nmtui              # respeaker user needs sudo
```
然后会看到这样的配置页面，选择 ```Activate a connection``` 并按下 ```Enter``` 键。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/nmtui1-1.png)

为 ReSpeaker v2.0 选择 Wi-Fi，选 ```Enter``` 键并输入 Wi-Fi 密码，然后再次选 ```Enter``` 键。当您看到 ```*``` 标记时，表示 ReSpeaker 已成功连接到 Wi-Fi 网络。选 ```Esc``` 键两次离开网络管理工具。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/nmtui1-2.png)

现在使用下面的命令找到 ReSpeaker 的 IP 地址。

```
ip address
```
在下面的例子中，我们可以看到这个 ReSpeaker 的 IP 地址是 ```192.168.7.108```

```
root@v2:/home/respeaker# ip address

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1
    link/sit 0.0.0.0 brd 0.0.0.0
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether e0:76:d0:37:38:6d brd ff:ff:ff:ff:ff:ff
    inet **192.168.7.108**/24 brd 192.168.7.255 scope global dynamic wlan0
       valid_lft 604332sec preferred_lft 604332sec
    inet6 2601:647:4680:ebf0:ec0a:5965:e710:f329/64 scope global noprefixroute dynamic
       valid_lft 345598sec preferred_lft 345598sec
    inet6 fe80::64de:cac8:65ef:aac8/64 scope link
       valid_lft forever preferred_lft forever
```


除了有用户界面的网络管理工具外，还有一个命令行式网络管理工具。如果您连接到隐藏的 Wi-Fi 网络，则需要使用以下命令行工具 :

```
nmcli c add type wifi con-name mywifi ifname wlan0 ssid your_wifi_ssid
nmcli con modify mywifi wifi-sec.key-mgmt wpa-psk
nmcli con modify mywifi wifi-sec.psk your_wifi_password
nmcli con up mywifi
```

**B. 以太网连接**

您可以使用以太网线连接到网络。只需插上连接到互联网的以太网线即可。

**通过 SSH & VNC 连接**

**A. SSH**

SSH 在 ReSpeaker v2.0 中自动启动。对于 Windows 用户，可用第三方 SSH 客户端。对于 Linux/Mac 用户，SSH 客户端是内置的。

- Windows 用户 : 使用 PUTTY，选择 SSH 协议，填写正确的 IP 地址并单击 open。用户名和密码都是 respeaker。

- Linux/Mac 用户 :
```
ssh respeaker@192.168.***.***
// password: respeaker
```

<div class="admonition note" >
<p class="admonition-title">Note</p>
请注意，如果使用 SSH 时性能体验下降，请切换到更畅通的 WiFi 网络。
</div>

**B. VNC**

为了获得 Alexa 的授权，需要使用 VNC Viewer，系统已内置 VNC。VNC 将启动 **lxqt** 桌面 GUI，这是一个轻量级的 Qt 桌面环境。VNC 服务也将自动启动。使用 [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) 或 [VNC Viewer for Google Chrome](https://chrome.google.com/webstore/detail/vnc%C2%AE-viewer-for-google-ch/iabmpiboiopbgfabjmgeedhcmjenhbla?hl=en) 来连接到 ReSpeaker Core v2.0 的桌面。

要使用 VNC，请将 PC/Mac 和 ReSpeaker v2.0 连接到相同的 Wi-Fi 网络。然后打开 VNC Viewer，在地址栏中输入 ```192.168.xxx.xxx``` 。```192.168.xxx.xxx``` 是该板的 IP 地址，您可以使用命令 **ifconfig** 来检查。如果您遇到 ```Unencrypted connection```，请单击 Continue 以继续。密码是 ```respeaker```。

![](https://user-images.githubusercontent.com/5130185/34665797-93b222d6-f49c-11e7-8112-704f91163038.png)


<div class="admonition note" >
<p class="admonition-title">Note</p>
请注意，VNC 连接需要高质量的网络。
</div>

**连接到扬声器或耳机**

该主板使用 SOC 的内置编解码器进行回放。JST 扬声器端口和耳机端口都由它们自己的放大器驱动，并且两个放大器都连接到 SOC 的同一个编解码器。声卡驱动程序同时驱动捕获设备和播放设备。所以 ALSA 设备列表中没有单独的采集或回放声卡。它们都被命名为 seeed-8mic-voicecard。

从电路板听到声音的最简单方法是插入耳机。如果您更喜欢用扬声器，也是完全OK的，电路板可以输出高达 8W 的负载。

**蓝牙设置**

**激活蓝牙**

请输入以下命令更新并激活 ReSpeaker Core v2.0 的蓝牙 :

```
sudo apt update
sudo apt upgrade
```

<div class="admonition note" >
<p class="admonition-title">Note</p>
如果更新失败，请更换为网络良好的另一个 WiFi，然后再次进行更新。
</div>

然后通过以下命令激活蓝牙 :

```
sudo systemctl enable bt-auto-connect.service
sudo reboot -f
```

**将 ReSpeaker Core v2.0 用作蓝牙音响-从属设备**

当 ReSpeaker Core v2.0 重新启动时，打开手机或计算机的蓝牙，您会发现名为 **ReSpeaker-xxxx** 的蓝牙设备。选择并连接到它。连接扬声器或耳机到 ReSpeaker Core v2.0，然后播放音乐。


![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Bluetooth_connect.png)

**将 ReSpeaker Core v2.0 用作蓝牙播放器-主设备**

除了作为蓝牙音响使用外，它还可以作为蓝牙播放器来连接蓝牙耳机或蓝牙音响。

- **步骤 1.** 输入 `bluetoothctl` 打开蓝牙对话框。

- **步骤 2.** 输入 `scan on` 扫描蓝牙设备。

- **步骤 3.** 当 ReSpeaker Core v2.0 找到您的目标设备时，输入 `scan off`。此处 MDR-1000X 耳机是我们的目标，标记设备 ID 为 `04:5D:4B:81:35:84`。

```
respeaker@v2:~$ bluetoothctl
[NEW] Controller 43:43:A0:12:1F:AC ReSpeaker-1FAC [default]
Agent registered
[bluetooth]# scan on
Discovery started
[CHG] Controller 43:43:A0:12:1F:AC Discovering: yes
[NEW] Device C8:69:CD:BB:9B:B3 C8-69-CD-BB-9B-B3
[NEW] Device E1:D9:68:0E:51:C0 MTKBTDEVICE
[NEW] Device 62:15:9C:3F:40:AA 62-15-9C-3F-40-AA
[NEW] Device 56:AF:DE:C0:34:25 56-AF-DE-C0-34-25
[NEW] Device B8:86:87:99:FB:10 SOLARRAIN
[CHG] Device B8:86:87:99:FB:10 Trusted: yes
[NEW] Device 04:5D:4B:81:35:84 MDR-1000X
[CHG] Device 04:5D:4B:81:35:84 Trusted: yes
[CHG] Device 4C:04:59:38:D3:25 ManufacturerData Key: 0x004c
[CHG] Device 4C:04:59:38:D3:25 ManufacturerData Value:
  10 05 0b 10 99 18 0a                             .......
[bluetooth]# scan off
[CHG] Device 04:5D:4B:81:35:84 RSSI is nil
[CHG] Device B8:86:87:99:FB:10 TxPower is nil
[CHG] Device B8:86:87:99:FB:10 RSSI is nil
[CHG] Device 4C:04:59:38:D3:25 RSSI is nil
[CHG] Device 58:44:98:93:35:24 RSSI is nil
Discovery stopped
[bluetooth]#

```

- **步骤 4.** 现在使用命令 `pair + device ID` 将蓝牙设备与 ReSpeaker Core v2.0 匹配。

- **Step 5.** 当看到消息 `Pairing successful` 时，输入 `connect + device ID`。

```
[bluetooth]# pair 04:5D:4B:81:35:84
Attempting to pair with 04:5D:4B:81:35:84
[CHG] Device 04:5D:4B:81:35:84 Connected: yes
[CHG] Device 04:5D:4B:81:35:84 UUIDs: 00001108-0000-1000-8000-00805f9b34fb
[CHG] Device 04:5D:4B:81:35:84 UUIDs: 0000110b-0000-1000-8000-00805f9b34fb
[CHG] Device 04:5D:4B:81:35:84 UUIDs: 0000110c-0000-1000-8000-00805f9b34fb
[CHG] Device 04:5D:4B:81:35:84 UUIDs: 0000110e-0000-1000-8000-00805f9b34fb
[CHG] Device 04:5D:4B:81:35:84 UUIDs: 0000111e-0000-1000-8000-00805f9b34fb
[CHG] Device 04:5D:4B:81:35:84 ServicesResolved: yes
[CHG] Device 04:5D:4B:81:35:84 Paired: yes
Pairing successful
[CHG] Controller 43:43:A0:12:1F:AC Discoverable: no
[CHG] Device 04:5D:4B:81:35:84 ServicesResolved: no
[CHG] Device 04:5D:4B:81:35:84 Connected: no
[CHG] Controller 43:43:A0:12:1F:AC Discoverable: yes
[bluetooth]# connect 04:5D:4B:81:35:84
Attempting to connect to 04:5D:4B:81:35:84
[CHG] Device 04:5D:4B:81:35:84 Connected: yes
Connection successful
[CHG] Device 04:5D:4B:81:35:84 ServicesResolved: yes
[CHG] Controller 43:43:A0:12:1F:AC Discoverable: no
[MDR-1000X]#
```

如果 `Connection successful` 弹出，配置成功了!

可以输入 `exit` 或 `quit` 以退出 shell，然后使用以下命令测试蓝牙设备。

```
arecord bluetoothtest.wav
aplay bluetoothtest.wav

```


**录音和播放**

**1.通过 ALSA 测试**

由于这是开发阶段的技术文档，声音设备的索引可能会随版本而变化。因此，首先使用以下命令检查正确的设备索引 :

```
respeaker@v2:~$ arecord -l
**** List of CAPTURE Hardware Devices ****
card 0: seeed8micvoicec [seeed-8mic-voicecard], device 0: 100b0000.i2s1-ac108-pcm0 ac108-pcm0-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0

respeaker@v2:~$ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: seeed8micvoicec [seeed-8mic-voicecard], device 1: 100b0000.i2s1-rk3228-hifi rk3228-hifi-1 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0

```

找到名称有 **seeed** 前缀的声卡。在上面的例子中，捕获设备是 **hw:0,0**，这意味着 card **0**/device **0**。回放设备是 **hw:0,1**，这意味着 card **0**/device **1**。然后通过以下命令测试录音和播放声音 :

```
# record & playback 2 channels audio
arecord -Dhw:0,0 -f S16_LE -r 16000 -c 2 hello.wav
aplay -Dhw:0,1 -r 16000 -c 2 hello.wav

# If you want to output the sound by the bluetooth device, you need to use the command below to play
aplay -r 16000 -c 2 hello.wav

# record 8 channels audio
# there are 6 microphones on board, and ac108 compose the 2 remaining channels.
arecord -Dhw:0,0 -f S16_LE -r 16000 -c 8 hello_8ch.wav
```

此外，您还可以同时录制和播放。

```
arecord | aplay
```


**2. 通过 PulseAudio 测试**

首先检查 PulseAudio 是否在运行 :

```
respeaker@v2:~$ ps aux|grep pulse|grep -v grep
respeak+  1109  0.0  0.7 363272  7932 ?        S<l  01:01   0:00 /usr/bin/pulseaudio --start --log-target=syslog
```
如果没有，请参阅 PulseAudio 的文档以启用 PulseAudio 的自动生成。然后测试 :
```
parecord --channels=8 --rate=16000 --format=s16le hello2.wav
paplay hello2.wav
```
此外，默认的 ALSA 设备现在挂接到 PulseAudio，因此还可以通过 PulseAudio 使用以下命令播放/记录声音 :
```
arecord -v -f cd hello3.wav
aplay hello3.wav
```

到目前为止，我们了解了 ReSpeaker Core v2.0 的基本操作，接下来看看其他的。我们可以使用 ReSpeaker Core v2.0 构建我们自己的 AVS (Alexa 语音服务) 设备或 Dueros (百度语音助手)设备。

### Out of Box 示例

这部分包括基于 librespeaker 的闭源解决方案。librespeaker 是一个音频处理库，它可以执行 :

- 噪声抑制
- 波达方向定位技术
- 波束成形
- 热词搜索
- 回声消除

它从 linux 声音服务器读取语音流，例如 pulseaudio 的。它公开了一些 API，它们使用户能够在说出热词时获得指示，以及以 PCM 格式已处理的语音数据，这些语音数据可以发送到像 Alexa 等的云服务进行进一步处理。

在开始体验这个强大的解决方案之前，请确保已经完成了以下所有内容。

- 系统镜像刻录 - 此示例需要 lxqt 版本系统镜像
- 通过 OTG USB 端访问串行控制台
- 设置 Wi-Fi / ethernet
- SSH
- VNC

OK，现在开始吧。

我们制作了一键安装脚本。有关此解决方案和逐步配置的更多详细信息，请参阅 [此处](https://github.com/respeaker/respeakerd)

**步骤 1. 下载软件包**
```
curl https://raw.githubusercontent.com/respeaker/respeakerd/master/scripts/install_all.sh|bash
```

出现提示时，输入权限密码 ：respeaker。等待脚本安装一些软件包。


**步骤 2. 对 Alexa 授权**

通过 [VNC](https://github.com/respeaker/get_started_with_respeaker/blob/master/docs/ReSpeaker_Core_V2/getting_started.md#ssh--vnc) 连接到电路板。在 VNC 桌面中，打开浏览器，地址栏输入 `127.0.0.1:3000`。浏览器将显示一个登录页面。使用您的亚马逊账户登录 :

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/aus-1.png)

成功后会出现 ：

![](https://github.com/respeaker/get_started_with_respeaker/raw/master/img/aus-2.png)

现在可以关闭 VNC。以下命令可以在 SSH 中执行 (VNC 桌面中也可以)。


**步骤 3. 运行代码**

完成上述步骤后，运行 :

```
python /home/respeaker/respeakerd/clients/Python/demo_respeaker_v2_vep_alexa_with_light.py

```

说 `snowboy`，唤醒 Alexa，尽情享受吧！

<div class="admonition note" >
<p class="admonition-title">Note</p>
您是否看到 ReSpeaker Core v2.0 背面的彩色 LED ? 仔细看看绿色 LED，它直接指向声源。这就是 DOA。</div>

## 闭源解决方案

### Librespeaker 的 API

闭源解决方案使用 librespeaker。Librespeaker 是一个音频处理库，可以实现噪声抑制，波达方向定位，波束成形，热词搜索。它从 linux 声音服务器读取语音流，例如 pulseaudio 的。

**关键词唤醒**

**BF (波束成形)**

  - 主要作用是提高麦克风的信噪比
  - 只听特定方向的声音

**DoA (波达方向定位)**

  - 通过 LED 灯环显示声音的方向

**NS (噪声抑制)**

  - 滤除电路引入的噪音
  - 滤除环境中的稳态噪声，例如电风扇的声音。

**AEC (声学回声消除)**

  - 从麦克风收集的声音中去除扬声器本身产生的声音。

**AGC (自动增益控制)**

  - 自动调节麦克风音量，最大限度地提高麦克风的拾音能力。

我们提供了一些 API，它们使用户能够在说出热词时获得指示，以及以 PCM 格式已处理的语音数据，这些语音数据可以发送到像 Alexa 等的云服务进行进一步处理。您可以点击 [APIs Docs](http://respeaker.io/librespeaker_doc/) 查看。


### 用 AVS 进行语音互动 (C++)




本指南将向您展示如何使用 respeakerd 运行 Amazon 官方 AVS C++ SDK。这部分要求您具有关于 Linux 的一定技术背景。

**第一部分. 准备工作**

如果您已经做过了 Out of Box 示例，请阅读下一部分。

如果您刚收到 ReSpeaker Core v2.0 并且不知从何下手，请学习 ReSpeaker Core v2.0的 [基本操作](http://wiki.seeedstudio.com/ReSpeaker_Core_v2.0/#preparation) :

- 系统镜像刻录 - 此示例需要 lxqt 版本系统镜像
- 通过 OTG USB 端访问串行控制台
- 设置 Wi-Fi / ethernet
- SSH
- VNC

然后安装基本软件包 :

```
## install deps
sudo apt update
sudo apt install -y librespeaker git cmake
sudo apt install -y python-mraa python-upm libmraa1 libupm1 mraa-tools
sudo pip install pixel_ring pydbus

cd /home/respeaker
git clone https://github.com/respeaker/respeakerd.git

cd /home/respeaker/respeakerd

sudo cp -f build/respeakerd /usr/local/bin
sudo cp -f scripts/respeakerd_safe /usr/local/bin
sudo chmod a+x /usr/local/bin/respeakerd
sudo chmod a+x /usr/local/bin/respeakerd_safe
sudo mkdir -p /usr/local/etc/respeakerd
sudo cp -Rf build/resources /usr/local/etc/respeakerd/
sudo cp -f scripts/respeakerd.service /etc/systemd/system/


#enable system service
sudo systemctl enable respeakerd
sudo systemctl start respeakerd


```

**第二部分. 配置 respeakerd**

2.1 PulseAudio 配置

使用您最喜欢的文本编辑器编辑 `default.pa`，我们使用的 **vim 编辑器**。请输入下面的命令

```
sudo vim /etc/pulse/default.pa

```

然后 Vim 编辑器会打开这个文件，按 ** i** 进入编辑模式。将以下行复制并粘贴到该文件的末尾 :

```
load-module module-pipe-source source_name="respeakerd_output" rate=16000 channels=1
set-default-source respeakerd_output

```

- 点 ** esc** 退出编辑模式
- 点 ** colon** 访问命令模式，点 ** w** 然后点 ** enter** 来保存修改。
- 保存后请点 ** q** 然后点 ** enter** 退出 vim。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/c1.png)


现在输入

```
sudo reboot -f #重启电路板
```

!!! Note
  上面的vim编辑器操作比较复杂，也许对新手来说不是太友好， 我们可以直接通过图形化界面来编辑 /etc/pulse/default.pa 文件，也可以通过nano编辑器来编辑，可以通过以下命令打开Nano编辑器

  ```
  sudo nano /etc/pulse/default.pa
  ```




2.2 在 PulseAudio 模式下启动 respeakerd


当 respeakerd 在 PulseAudio 模式下工作时，它将处理后的音频流输出到由 PulseAudio 的 module-pipe-source 创建的已命名通道中。

```
sudo systemctl stop respeakerd
sudo vim /usr/local/bin/respeakerd_safe
```
像下面的代码一样来修改这个文件的内容，可以参考先前 vim 编辑器的操作。

```
#!/bin/bash

pulseaudio --check

while [ $? == 1 ]; do
    sleep 1
    pulseaudio --check
done

while [ ! -p /tmp/music.input ]; do
   sleep 1
done

sleep 5

/usr/local/bin/respeakerd --snowboy_res_path="/usr/local/etc/respeakerd/resources/common.res" --snowboy_model_path="/usr/local/etc/respeakerd/resources/snowboy.umdl" --snowboy_sensitivity="0.4" --source="alsa_input.platform-sound_0.seeed-8ch" --mode=pulse
```

!!!Note
    请确保像上面的代码一样修改了这个文件，尤其是最后一行 **/usr/local...--mode=pulse**。

重新启动服务 :

```
sudo systemctl start respeakerd

```

或者您想手动启动 respeakerd 以进行调试 :

```
sudo systemctl stop respeakerd
/usr/local/bin/respeakerd --snowboy_res_path="/usr/local/etc/respeakerd/resources/common.res" --snowboy_model_path="/usr/local/etc/respeakerd/resources/snowboy.umdl" --snowboy_sensitivity="0.4" --source="alsa_input.platform-sound_0.seeed-8ch" --mode=pulse --debug
```

**第三部分. 编译并运行 AVS C++ SDK**

3.1 下载并安装必要的文件

```
$ cd /home/respeaker/ && mkdir sdk-folder && cd sdk-folder && mkdir sdk-build sdk-source third-party application-necessities && cd application-necessities && mkdir sound-files
$ sudo apt-get -y install git gcc cmake build-essential libsqlite3-dev libcurl4-openssl-dev libfaad-dev libsoup2.4-dev libgcrypt20-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-good libasound2-dev doxygen
$ cd /home/respeaker/sdk-folder/third-party && wget -c http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz && tar zxf pa_stable_v190600_20161030.tgz && cd portaudio && ./configure --without-jack && make
$ sudo pip install commentjson
$ sudo pip install flask
$ cd /home/respeaker/sdk-folder/sdk-source && git clone git://github.com/respeaker/avs-device-sdk.git
$ cd /home/respeaker/sdk-folder/sdk-build && cmake /home/respeaker/sdk-folder/sdk-source/avs-device-sdk -DCMAKE_BUILD_TYPE=DEBUG -DRESPEAKERD_KEY_WORD_DETECTOR=ON -DGSTREAMER_MEDIA_PLAYER=ON -DPORTAUDIO=ON -DPORTAUDIO_LIB_PATH=/home/respeaker/sdk-folder/third-party/portaudio/lib/.libs/libportaudio.a -DPORTAUDIO_INCLUDE_DIR=/home/respeaker/sdk-folder/third-party/portaudio/include
$ make SampleApp -j2

```

3.2 获取 AVS 授权

在本节中，我们将设置并运行一个本地授权服务器，我们将使用它来获取刷新令牌。此刷新令牌与您的 **Client ID** 和 **Client Secret** 一起交换为访问令牌，示例应用程序需要将它们与每个事件 (请求) 发送给 Alexa。

步骤 1. 向 Amazon 注册您的产品

首先，请按照这些 [说明](https://github.com/alexa/alexa-avs-sample-app/wiki/Create-Security-Profile) 注册您的产品并创建安全配置文件。如果您有已注册的测试产品，则可以跳过此步骤。

!!!Note
    确保已经从 **Product information** 选项卡中保存 **Product ID**，并从 **Security Profile** 选项卡中保存 **Client ID** 和 **Client Secret**。需要这些参数来配置授权服务器。


步骤 2. 升级 AlexaClientSDKConfig.json


通过以下命令打开 `/home/respeaker/sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json`。

```
vim /home/respeaker/sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json

```

用这个 JSON blob 替换 AlexaClientSDKConfig.json 的内容 :

```
{
    "authDelegate":{
        "clientSecret":"YOUR_CLIENT_SECRET",
        "deviceSerialNumber":"123456",
        "refreshToken":"",
        "clientId":"YOUR_CLIENT_ID",
        "productId":"YOUR_PRODUCT_ID"
   },
   "alertsCapabilityAgent":{
        "databaseFilePath":"/home/respeaker/sdk-folder/application-necessities/alerts.db"
   },
   "settings":{
        "databaseFilePath":"/home/respeaker/sdk-folder/application-necessities/settings.db",
        "defaultAVSClientSettings":{
            "locale":"en-US"
        }
   },
   "certifiedSender":{
        "databaseFilePath":"/home/respeaker/sdk-folder/application-necessities/certifiedSender.db"
   },
   "notifications":{
       "databaseFilePath":"/home/respeaker/sdk-folder/application-necessities/notifications.db"
   }
}

```

输入在设备注册过程中保存的 **clientId**，**clientSecret** 和 **productId** 并保存。

!!!warning
    不要删除引号并确保没有多余的字符或空格！所需值是字符串。最好保存此文件的备份。后续版本可能会覆盖 **AlexaClientSDKConfig.json** 中的值。

!!!note
    deviceSerialNumber 为预设值，但是，商业产品应使用为设备标识的序列号或其他唯一标识。

!!!Tip
    示例 JSON 中的语言环境默认设置为 US English，但支持 [其他语言环境](https://developer.amazon.com/docs/alexa-voice-service/settings.html#settingsupdated)。请随意测试每种语言。


步骤 3. 获取刷新令牌

在更新 **AlexaClientSDKConfig.json** 之后，运行 **AuthServer.py** 来启动令牌交换 :

```
cd /home/respeaker/sdk-folder/sdk-build && python AuthServer/AuthServer.py

```
!!!Note
    您可能需要更改 ReSpeaker 的语言环境设置，因为某些 Raspbian 镜像默认为 **amazon.co.uk** 至 **amazon.com**。


打开浏览器并导航到 http://localhost:3000。使用 Amazon 账户登录并按照提供的说明操作。

![](https://camo.githubusercontent.com/f4d1060ce3223a028af83c4743b4caee28ff107d/68747470733a2f2f6d2e6d656469612d616d617a6f6e2e636f6d2f696d616765732f472f30312f6d6f62696c652d617070732f6465782f6176732f73646b2f332e706e67253232)

步骤 4. AVS 配置测试

输入下面的命令来测试 AVS 配置。

```
/home/respeaker/sdk-folder/sdk-build/SampleApp/src/SampleApp /home/respeaker/sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json

```
如果一切顺利，您将看到 **Sample APP**。现在您可以与 Alexa 进行对话，但所有用户体验都是通过命令行消息完成的。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/SDK_app.png)

**第四部分. LED 灯环灯光效果**

要激活板载 LED 灯环灯光效果，只需输入下面的命令即可。

```
$ sudo cp -f /home/respeaker/respeakerd/scripts/pixel_ring_server /usr/local/bin/
$ sudo chmod a+x /usr/local/bin/pixel_ring_server
$ pixel_ring_server

```
现在您会看到 LED 灯环闪烁。


**Part 5. 启动**

完成此部分后，能够通过关键字唤醒 ReSpeaker Core v2.0。

输入以下命令。

```
$ sudo cp -f /home/respeaker/respeakerd/scripts/avs_cpp_sdk_safe /usr/local/bin
$ sudo chmod a+x /usr/local/bin/avs_cpp_sdk_safe
$ sudo cp -f /home/respeaker/respeakerd/scripts/pixel_ring_server.service /etc/systemd/system/
$ sudo cp -f /home/respeaker/respeakerd/scripts/avs_cpp_sdk.service /etc/systemd/system/
$ sudo systemctl enable pixel_ring_server
$ sudo systemctl enable avs_cpp_sdk
$ sudo systemctl start pixel_ring_server
$ sudo systemctl start avs_cpp_sdk

```

最后，呼叫 Snowboy，它会给您一个惊喜 !


## 开源解决方案

**算法**

- NS
- Key Word


### 用 AVS 进行语音互动

本指南将向您展示如何构建基于 ReSpeaker Core V2.0 的 AVS 设备。


- **步骤 1. 安装 AVS library (Python)**

```
respeaker@v2:~$ sudo apt update
respeaker@v2:~$ pip install avs
```

这也会将以下可执行文件安装到 **~/.local/bin** : alexa-audio-check, alexa-auth, dueros-auth, alexa-tap 和 alexa。

输入下面的命令来检查音频配置 :
```
respeaker@v2:~$ ~/.local/bin/alexa-audio-check
```
该脚本计算麦克风记录的声音的 RMS。

- **Step 2. 对 Alexa 授权**

通过 [VNC](https://github.com/respeaker/get_started_with_respeaker/blob/master/docs/ReSpeaker_Core_V2/getting_started.md#ssh--vnc) 连接到电路板。在 VNC 桌面，打开 terminal 并执行 :

```
respeaker@v2:~$ ~/.local/bin/alexa-auth
```
该脚本将自动打开浏览器，浏览器将显示登录页面。使用您的亚马逊账户登录 :

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/aus-1.png)

成功后会出现 :

![](https://github.com/respeaker/get_started_with_respeaker/raw/master/img/aus-2.png)

现在可以关闭 VNC。以下命令可以在 SSH 中执行 (VNC 桌面中也可以)。

- **步骤 3. 与 Alexa 应用嗨起来**

我们提供基于 Alexa 的三个 python 文件，您可以自由选择它们。

  - Alexa-tap.py : 使用 **Enter** 唤醒 Alexa，我们称它为 Alexa Tap to Play。
  - ns_kws_alexa.py : 使用关键字 **Alexa** 来唤醒 Alexa，我们称之为 Alexa Hands-Free。
  - ns_kws_alexa_with_light.py : 与 ns_kws_alexa.py 相同，增加 LED 效果，我们称之为 Alexa with light。

**Alexa Tap to Play**

在 Putty 中输入下面的命令 (建议使用SSH)。

```
respeaker@v2:~$ ~/.local/bin/alexa-tap
```

等到您在打印日志中看到 **on_ready**。按电脑上的 **Enter** 键并与 Alexa 聊天(现在只支持英文)。

**Alexa Hands-Free with Snowboy**

```
sudo apt install libatlas-base-dev                # required by snowboy
git clone https://github.com/respeaker/respeaker_v2_eval.git
cd respeaker_v2_eval
pip install --no-deps snowboy*.whl           # install pre-build snowboy
pip install webrtc_audio_processing*.whl
pip install voice-engine
python ns_kws_alexa.py
```
等到您在打印日志中看到 **on_ready**，说 **Alexa** 来触发与 Alexa 的对话。

**Alexa with Light Effect**

```
pip install pixel-ring
python ns_kws_alexa_with_light.py
```
与前一个一样，说 Alexa 来触发与 Alexa 的对话。程序运行时，会看到 LED 闪烁。




### 用 Dueros 进行语音互动

与 AVS 相同，唯一的区别是您需要删除一个配置文件。在获得授权之前，需要输入以下命令以删除 **avs.json**。

```
rm -f ~/.avs.json
```
然后可以通过输入下面的命令行获得百度的授权 :

```
respeaker@v2:~$ ~/.local/bin/dueros-auth
```
![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/dueros.jpg)



登录后，接下来的步骤与AVS相同。

当您运行 python 程序时，您可以说 **Alexa** 唤醒百度语音助手。

## GPIO

本部分将介绍如何使用 **MRAA** 和 **UPM** 来控制 Respeaker Core v2.0 上的 GPIO 和 Grove Socket。

- **步骤 1. 将 MRAA 和 UPM 库更新到最新版本**

首先，我们需要安装最新的 MRAA 和 UPM 软件包。

```
sudo apt install  python-mraa python-upm libmraa1 libupm1 mraa-tools
```
- **步骤 2. 检查设备信息**

```
#only have bus 0 and id=03(/dev/i2c-3), 0 is the i2c number for mraa and upm
respeaker@v2:~$ mraa-i2c list
Bus   0: id=03 type=linux

#mraa gpio numbers and system gpio numbers and it's pinmux
respeaker@v2:~$ mraa-gpio list
00      GPIO91: GPIO
01         VCC:
02      GPIO43: GPIO
03     GPIO127: GPIO
04      GPIO17: GPIO
05      GPIO67: GPIO
06         GND:
07      GPIO13: GPIO
08    I2C2_SCL: I2C  
09    I2C2_SDA: I2C  
10         VCC:
11         GND:
12      GPIO66: GPIO
```
关于 ReSpeaker Core v2.0 的引脚定义请参考引脚图


- **步骤 3. 用 MRAA 或 UPM 进行演示**

#### A. 使用 MRAA 库


**直接控制 GPIO**

准备以下器材


| ReSpeaker Core v2.0 |  Grove - Buzzer |
|--------------|-------------|
|![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/ReSpeaker_V2_back_little.jpg)|![enter image description here](https://github.com/SeeedDocument/Base_Shield_V2/raw/master/img/Buzzer.png)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.2b0633dbkl2fFa&id=566241590290)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.752a33dbFTaTFF&id=520245748676)|

使用跳线将 Grove - Buzzer 的 **SIG** 引脚连接到 ReSpeaker Core v2.0 的 **GPIO0**。不要忘记连接 VCC 和 GND。然后在控制台输入下面的代码。

``` python
respeaker@v2:~$ python
Python 2.7.13 (default, Jan 19 2017, 14:48:08)
[GCC 6.3.0 20170118] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mraa
>>> x = mraa.Gpio(0)
>>> x.dir(mraa.DIR_OUT)
0
>>> x.write(0)
0
>>> x.write(1)
0
>>>
```
当输入 **x.write(1)**，您会听到蜂鸣器发出尖叫声。


**PIR Motion Sensor 示例**


准备以下器材

| ReSpeaker Core v2.0 |  Grove -  PIR Motion Sensor |
|--------------|-------------|
|![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/ReSpeaker_V2_back_little.jpg)|![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Grove%20-%20PIR%20Motion%20Sensor.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.2b0633dbkl2fFa&id=566241590290)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.10.411333dbeKBsuf&id=45568896887)|


在这个示例中，我们用 Python 代码来监听 Grove - PIR Motion Sensor 的触发器。

使用跳线将 Grove - PIR Motion Sensor 的 **D1** 引脚连接到 ReSpeaker Core v2.0 的 **GPIO0**。不要忘记连接 VCC 和 GND。然后将下面的代码复制到一个新文件中，并将其另存为一个 python 文件，名称为 **mraa_pir.py**。将此文件复制到您的 ReSpeaker Core v2.0。

``` python
import mraa

def on_trigger(gpio):
    print("pin " + repr(gpio.getPin(True)) + " = " + repr(gpio.read()))

pin = 0

try:
    x = mraa.Gpio(pin)
    print("Starting ISR for pin " + repr(pin))
    x.dir(mraa.DIR_IN)
    # respeaker v2 only support EDGE_BOTH
    x.isr(mraa.EDGE_BOTH, on_trigger, x)
    var = raw_input("Press ENTER to stop")
    x.isrExit()
except ValueError as e:
    print(e)

```

然后使用下面的命令运行代码。(确保此时位于包含刚刚保存的 mraa_pir.py 的文件夹中)

``` python
sudo python mraa_pir.py
```

结果如下 :
```
$ sudo python mraa_pir.py
Starting ISR for pin 0
Press ENTER to stoppin 1091 = 0
pin 1091 = 0
pin 1091 = 1
...
```


#### B. 使用 UPM 库

UPM 执行基于 MRAA 库的传感器驱动程序，因此我们不再需要关心 GPIO 编程或传感器的 I2C 地址，每个传感器的所有默认信息和逻辑都已封装到 UPM 库中。UPM 支持大量的传感器。https://iotdk.intel.com/docs/master/upm/modules.html。但是请注意，我们尚未确认是否每个传感器都可以在 ReSpeaker Core v2.0 上工作。

**Grove - Digital Light Sensor 示例**


准备以下器材

| ReSpeaker Core v2 |  Grove - Digital Light Sensor |
|--------------|-------------|
|![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/ReSpeaker_V2_back_little.jpg)|![enter image description here](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Digital_Light_Sensor.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.2b0633dbkl2fFa&id=566241590290)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.10.4bd333dbSHts2a&id=45507034521)|

这是 Grove - Digital Light Sensor 的一个示例，从 UPM github repo 搬运而来。

请通过 Grove 插座将传感器插入 Respeaker Core v2.0。然后将下面的代码复制到一个新文件中，并将其保存为 python 文件，命名为 **tsl2561.py**。将此文件复制到 ReSpeaker Core v2.0。

``` python
#!/usr/bin/env python
# Author: Zion Orent <zorent@ics.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_tsl2561 as upmTsl2561

def main():
    # Instantiate a digital light sensor TSL2561 on I2C
    myDigitalLightSensor = upmTsl2561.TSL2561()

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit, including functions from myDigitalLightSensor
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    while(1):
        print("Light value is " + str(myDigitalLightSensor.getLux()))
        time.sleep(1)
if __name__ == '__main__':
    main()
```

结果如下:

``` python
respeaker@v2:~$ python tsl2561.py       
Light value is 0
Light value is 38
Light value is 20
Light value is 54
Light value is 13
Light value is 44
Light value is 31  
```

## FAQs

Q1: 如何使用 Audacity 录音并播放?

  **A1:** **lxqt** 版本预安装了 Audacity，请点击左下角的 **Bird button**，您将在 **Sound & Video -> Audacity** 中找到它。

  当打开 Audacity 时，请点击小黑箭头选择录音和播放设备并设置如下图所示。

  ![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/audacity.png)

  为录音和播放设备选择 Seeed-8mic-voicecard。您可以选择 1/2/4/6/8 通道来录音和播放。正如您所看到的，图片中有 8 个通道，但通道 7 和 8 中没有数据。这是因为这两个通道是回放通道。通道 7 用于 3.5mm 耳机，通道 8 用于 JST2.0 扬声器 (如果没有 JST 线缆，也可以使用跳线)。我们使用 JST 扬声器 :

  - 步骤 1. 像上图设置，点击 **Record** 按钮，录制一段音频。
  - 步骤 2. 点击 **Stop** 按钮，然后会看到通道 7 和 8 是空的。
  - 步骤 3. 再次点击 **Record** 按钮，这次会发现通道 8 已更改。

  ![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/audacity_playback.png)

Q2: 如何访问 ReSpeaker Core v2.0 的 AP？

**A2:** 您可以使用两根线缆为 ReSpeaker Core v2.0 供电。系统运行时，Respeaker Core v2.0 可以充当 AP。您可以使用计算机访问此 AP。如图所示。您可以按照步骤配置 ReSpeaker Core v2.0 的WiFi。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Ap.png)

- **步骤 1.** 输入以下命令激活 ReSpeaker Core v2.0 的 AP。

```
sudo systemctl enable re-wifi.service
sudo reboot -f

```

- **步骤 2.** 访问 ReSpeaker Core v2.0 的 AP。在 ReSpeaker Core v2.0 重新启动后，使用您的手机或电脑搜索 WiFi。您会发现 AP 的名字类似 **ReSpeaker_xxxx**，用户名是 **respeaker**，密码也是 **respeaker**。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/AP2.png)

- **步骤 3.** 进入串口控制台后，可以设置 WiFi

Q3: 如何调音量?

**A3:** 您可以使用 Alsamixer 来调整音量和捕捉灵敏度。

- **步骤 1.** 输入以下命令打开 Alsamixer :

```
alsamixer
```

- **步骤 2.** 按键盘上的 **F6** 选择 **Seeed-8mic-voicecard**。
- **步骤 3.** 出现如下图所示的界面。可以通过按左右键选择播放语音或录音通道。可以通过按上下键来调整音量。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/Alexamixer.png)

Q4: 如何使用用户按钮 ?

**A4:** 如您所见，ReSpeaker Core v2.0 背面有一个用户按钮。在这里我们提供了一个 python 演示来展示如何使用它。

- **步骤 1.** 输入以下命令 :

```
sudo pip install evdev
```

- **步骤 2.** 复制下面的代码并将其保存为 python 文件，我们将其命名为 **usrer_button.py**。

```
from evdev import InputDevice,categorize,ecodes

key = InputDevice("/dev/input/event0")
for event in key.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
```

- **步骤 3.** 输入以下命令运行这个演示。

```
sudo python usrer_button.py
```

结果如下 :

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/userbutton.png)

Q5: 电脑无法识别 ReSpeaker Core v2.0，是驱动程序有问题吗 ?

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/CDC_Driver.png)

**A5:** 当通过 OTG 或 UART 将 ReSpeaker Core v2.0 连接到电脑时，可能会发生这种情况。这是因为 CDC 串行驱动程序与其他 OTG 驱动程序有冲突。请卸载冲突的驱动程序并重新连接 ReSpeaker Core v2.0。

Q6: 如果我想使用外部天线怎么办 ?

**A6:** ReSpeaker Core v2.0 使用 **AP6212** 来提供 WiFi 和蓝牙，它们共用相同的天线。除了板载天线外，您还可以使用外部天线。为此，您需要移除一个电阻并将其焊接在新焊盘上，如下所示 ：

- 首先移除橙框中的电阻。
- 然后把它焊在绿框上。

![](https://github.com/SeeedDocument/Respeaker_V2/raw/master/img/ant.png)

**A7:** ReSpeaker Core v2.0怎么更改关键词？

step 1. 请到[Snowboy](https://snowboy.kitt.ai/)的官网去自定义一个关键词（当然下载别人定义的关键词也行）。

step 2. 将自定义或者别人的关键词`.pmdl`文件下载到`/usr/share/respeaker/snowboy/resources`路径下。

step 3. 修改`/etc/respeaker/respeakerd.conf`文件里面的`snowboy_model_path = /usr/share/respeaker/snowboy/resources/***.pmdl`。其中`***.pmdl`为刚刚从`snowboy`官网上面下载的。

**A8:** ReSpeaker Core v2.0里面的火狐浏览器不能使用了怎么办？

Q8：

运行
```
sudo apt install midori 
```
重新安装以一个浏览器来代替火狐浏览器

## 资源下载
- **[PDF]** [Download PDF of This Wiki](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/ReSpeaker_Core_v2.pdf)
- **[PDF]** [Rockchip RK3229 Datasheet V1.1](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/Rockchip%20RK3229%20Datasheet%20V1.1%2020151209.pdf)
- **[PDF]** [Dimensions for Board](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/ReSpeaker_Core_v2_Demensions.pdf)
- **[ZIP]** [3d Models For ReSpeaker Core v2.0](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/Respeaker_Core_v2_3D_SKP.zip)
- **[DXF]** [ReSpeaker Core v2.0 CASE](https://github.com/respeaker/get_started_with_respeaker/raw/8111196e821fec10c65b00d96cf011dc90111546/files/RESPEAKER_CORE_V2_CASE.dxf)
- **[PDF]** [ReSpeaker Core v2.0 CASE Assembly drawing](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/ReSpeaker_Core_v2.0_case_Assembly.pdf)
- **[PDF]** [Acoustic & Electrical Specification of ReSpeaker Core v2.0](https://github.com/SeeedDocument/Respeaker_V2/raw/master/res/Acoustic%26Electrical_Specification_of_ReSpeaker_Core_v2.0.pdf)
- **[MoreReading]** [Mraa Python documents page](http://iotdk.intel.com/docs/master/mraa/python/)
- **[MoreReading]** [Intel Mraa SDK](https://software.intel.com/en-us/mraa-sdk/documentation )



## Tech Support
Please do not hesitate to contact [techsupport@seeed.cc](techsupport@seeed.cc) if you have any technical issue. Or submit the issue into our [forum](http://seeedstudio.com/forum/).
