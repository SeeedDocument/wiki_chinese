# Raspberry Pi 4串口配置教程

树莓派为我们提供了两个串口分别是PL011 UART（硬件串口）和一个是mini-uart（软件串口）。在树莓派3代之前的版本中，默认将硬件串口映射到了GPIO中的UART(GPIO14&GPIO15)，但是3代以后官方增加了蓝牙模块，为使其稳定工作，官方在设计时将硬件串口分配给了新增的蓝牙模块上。而将一个没有时钟源，必须由内核提供时钟参考源的mini-uart分配给了GPIO中的UART(GPIO14&GPIO15)，这样以来由于内核的频率本身是变化的，就会导致mini-uart的速率不稳定，这样就出现了无法正常使用的情况。

##  硬件说明

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
- 一根杜邦线

建议烧写最新的镜像，以保证更好的配置的串口。详细的教程可以访问[这里](http://wiki.seeedstudio.com/cn/Raspberry_Pi_4_Model_B_start/)，其次将杜邦线UART(GPIO14&GPIO15)引脚进行短接，想要更加详细了解引脚详细信息请参考[这里](https://pinout.xyz/pinout/pin8_gpio14),下面是GPIO14&GPIO15短接图。

![](https://github.com/SeeedDocument/Raspberry_Uart_Introduce/raw/master/IMG/IMG_20191112_114610.jpg)

## 软件配置

通过前面的教程，我相信我们不难使用putty去访问树莓派，然后对其进行配置。

### 配置config.txt

Raspberry Pi 声称是掌上电脑，但是并没有在传统的PC上能找到的BIOS，官方为了解决这一问题，创建了一个名叫config.txt的可选文本文件，该文件的目的是用来配置系统参数。树莓派官方提供了很方便的将硬件串口映射到了GPIO中的UART(GPIO14&GPIO15)的方法。

**1.打开config.txt文件**

`sudo nano /boot/config.txt`，在这里是我使用的是nano文本编辑器,您也可以选择你自己喜欢的编辑器。

**2.在[all]下面添加以下两个参数**

```bash
[all]
#dtoverlay=vc4-fkms-v3d
enable_uart=1
dtoverlay=pi3-miniuart-bt
```
其中`enable_uart=1`不难理解是使能串口映射（在3代以前添加这个命令就可以打开串口了）。`dtoverlay=pi3-miniuart-bt`对于这个参数我们可以简单的理解为在树莓派里面添加了一个特别的驱动代码，这段驱动代码的主要的作用是将蓝牙的串口映射到mini-uart，而将PL011 UART闲置出来留给我们使用。

### 配置cmdline.txt

这里我们摘抄树莓派官网的文字来解释cmdline.txt。Linux内核在引导过程中接受命令行参数。在Raspberry Pi上，此命令行是在引导分区中名为cmdline.txt的文件中定义的。总之，我们需要配置终端的时候就需要修改这个文件。

**1.打开cmdline.txt文件**

`sudo nano /boot/cmdline.txt`，在这里是我使用的是nano文本编辑器,您也可以选择你自己喜欢的编辑器。

**2.找到并删除console=ttyAMA0,115200**

`console=ttyAMA0,115200`这个参数的意思，树莓派默认是支持通过的串口登陆的(假如需要通过串口登陆树莓派只需要执行配置config.txt)。而且树莓派就一组串口引脚，也就是当时我们要使用自定义输出串口信息的话，那么我们必须要吧`console=ttyAMA0,115200`删了，才能失能树莓派串口登陆功能，才能达到我们想要的目的。

### 失能蓝牙服务

由于mini-uart很不稳定，所以要在使用PL011 UART的时候，我们最好使用`sudo systemctl disable hciuart`是把蓝牙服务关闭。

### 重启并使用串口助手测试

重启后，我们运行`sudo miniterm /dev/ttyAMA0 115200`去检测我们的串口是否配置成功，当我们输入什么就打印什么的时候，那么恭喜你配置成功了。

![](https://github.com/SeeedDocument/Raspberry_Uart_Introduce/raw/master/IMG/miniterm.png)

## 技术支持

如果有其他技术问题，请发邮件到techsupport@seeed.cc 或者请到我们的论坛里去参与讨论[forum](http://forum.seeedstudio.com/).
