# Getting started with the STEM drone bundle

## STEM无人机自动套件[](#the-stem-drone-bundle)

STEM（科学技术工程数学）无人机捆绑包是基于带有Flow Deck的Crazyflie2.X。它是一种自主无人机，可以通过简单的python脚本进行控制，以在3M内操作机器人。

本入门指南将帮助您设置系统并进行首次自主飞行。

### 所需的硬件[](#required-hardware)

*   1 x Crazyflie 2.X 套件
*   1 x Crazyradio PA
*   1 x Flow deck

### 先决条件[](#prerequisites)

本入门指南假定您已经组装了Crazyflie2.X。如果不是这种情况，请学习[ Crazyflie 2.X 入门指南](http://wiki.seeedstudio.com/cn/Getting_started_with_the_Crazyflie_2.X/#crazyflie-2x)

This guide also requires that you have updated the Crazyflie to the latest firmware. For more information on how to update the firmware, see the [download latest firmware](/getting-started-with-the-crazyflie-2-0/#latest-fw) section in our getting started with Crazyflie 2.X tutorial.

本指南还要求您将Crazyflie更新为最新固件。有关如何[更新固件](http://wiki.seeedstudio.com/cn/Getting_started_with_the_Crazyflie_2.X/#firmware)的更多信息，请参阅我们的Crazyflie 2.X入门教程中的“下载最新固件”部分。

### 安装flow deck[](#mounting-the-flow-deck)

使用Crazyflie 2.X套件随附的长针形接头将Flow Deck安装在Crazyflie 2.X下方。

有关如何安装扩展平台的更多信息，请参见[扩展平台入门](https://www.bitcraze.io/getting-started-with-expansion-decks/)教程。

### 安装Python和cflib[](#installing-python-and-the-cflib)

**1. Windows**

用于控制Crazyflie 2.X的后端库称为cflib，是用python 3编写的。要使用它，您必须在计算机上安装Pyhton 3，并且可以在此处[下载](http://www.python.org)。

使用标准设置安装python，为方便起见，勾选Add to PATH复选框。

![Python install](https://www.bitcraze.io/images/tutorials/getting_started_stem/python3_toPATH.png "Python install")

安装python 3后，打开命令提示符并使用pip安装cflib。键入pip3 install cflib在命令提示

![cflib install](https://www.bitcraze.io/images/tutorials/getting_started_stem/pip_cflib.png "cflib install")

**2. Ubuntu**

以下说明已在Ubuntu 16.04上进行了测试。

要安装Python，pip和Crazyflie库，请运行以下命令：

```bash
sudo apt-get install python3 python3-pip python3-usb idle3
pip3 install cflib
```

您的用户需要访问USB设备才能使用Crazyradio，请运行以下行授予访问权限。运行命令后，需要再次插入Crazyradio，以使规则生效。

```bash
sudo groupadd plugdev
sudo usermod -a -G plugdev $USER
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE="0664", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-crazyradio.rules
```

### 运行您的第一个飞行脚本[](#running-your-first-flight-script)

现在，当一切都设置完毕并安装完毕后，启动Python编辑器IDLE3。选择*File->New*，然后将以下脚本复制/ 粘贴到新脚本中。用合适的名称保存脚本。

```python
"""
This script shows a simple scripted flight path using the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. Change the URI variable to your Crazyflie configuration.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/250K'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # We take off when the commander is created
        with MotionCommander(scf) as mc:
            print('Taking off!')
            time.sleep(1)
            
            # There is a set of functions that move a specific distance
            # We can move in all directions
            print('Moving forward 0.5m')
            mc.forward(0.5)
            # Wait a bit
            time.sleep(1)

            print('Moving up 0.2m')
            mc.up(0.2)
            # Wait a bit
            time.sleep(1)

            print('Doing a 270deg circle');
            mc.circle_right(0.5, velocity=0.5, angle_degrees=270)

            print('Moving down 0.2m')
            mc.down(0.2)
            # Wait a bit
            time.sleep(1)

            print('Rolling left 0.2m at 0.6m/s')
            mc.left(0.2, velocity=0.6)
            # Wait a bit
            time.sleep(1)

            print('Moving forward 0.5m')
            mc.forward(0.5)

            # We land when the MotionCommander goes out of scope
            print('Landing!')
```
通过按F5运行脚本。

!!!Note

    如果您打开了python客户端，请确保Crazyflie已从其断开连接。Crazyradio不支持同时来自多个程序的连接，如果Crazyflie仍连接到python客户端，则脚本将无法工作。

```python
Connecting to radio://0/80/250K
Connected to radio://0/80/250K
Taking off!
Moving forward 0.5m
Moving up 0.2m
Doing a 270deg circle
Moving down 0.2m
Rolling left 0.2m at 0.6m/s
Moving forward 0.5m
Landing!
```
