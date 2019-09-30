
# Getting started with the Crazyflie 2.X

## 打开Crazyflie 2.X的套件

Crazyflie 2.X 套件东西如下下面的清单所述，在你组装之前请先确定清单里面的东西是不是都在套件里面

### 材料清单

*   1 x 安装了所有组件的Crazyflie 2.X控制板
*   5 x CW 螺旋桨
*   5 x CCW 螺旋桨
*   6 x 电机支架
*   1 x LiPo电池(240mAh)
*   5 x 无刷DC电机
*   2 x 扩展连接器短插针 (1×10, 2mm 间距, 8 mm 长度)
*   2 x 扩展连接器长插针 (1×10, 2mm 间距, 14 mm 长度)
*   1 x 电池扩展支架
*   1 x USB线 (只有Crazyflie 2.1才会有)


## 测试


Crazyflie 2.X在生产出来后经过了大量的测试，为了确定在销售和储存过程中没有发生意外，在组装之前我们最好是先测试一下。使用usb线插到usb源(电脑或者电池)给Crazyflie 2.X上电同时检查下面的测试结果。在测试期间一定要保证Crazyflie 2.X稳定，我们也应该远离磁性很强的磁铁。

### 自测


在你组装之前，先通过USB为其上电，Crazyflie 2.X将进行自我测试。通过M1和M4LED灯就可以看到测试的结果。如果
M4LED快速闪烁绿色的灯5次，那么说明Crazyflie 2.X没有问题

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/self_test_pass.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 自测失败


反之，如果M1 LED不断的快速闪烁红色的灯5次，可以去[技术论坛](//forum.bitcraze.io)寻求帮助。


<iframe width="800" height="450" src="https://www.bitcraze.io/videos/self_test_fails.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 组装

组装Crazyflie 2.X可能最多需要10分钟，但是有些地方存在一些陷阱，所以最好是按照下面的指南操作。


### 绞线

将4个电机线绞在一起，一方面是为了减少电气噪声，另一方面是便于在固定在电机之前上。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/twisting_the_wires.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 安装电机

将4个电机推进电机支架上，你将需要一些力气去将他们推进支架中。如果很难如视频中所示进行操作，请尝试将电机罐朝桌面边缘移动，然后将其按在底座上。在插入时，不能按压电机轴，否则可能会损坏电机。电机应完全插入到底座中的挡块上。


<iframe width="800" height="450" src="https://www.bitcraze.io/videos/mount_the_motors.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 固定绞线


将绞线固定到电机安装座子下面的小勾子上面。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/attach_the_twisted%20wire.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



### 插入电机

将装好电机的电机座子插入Crazyflie 2.X的翅膀上面。也有可能需要一点力气去安装它。确定电机座子一直插到了底部。固定好后，将电机连接到Crazyflie 2.X。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/insert_the_motor.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 接上螺旋桨

现在是接螺旋桨的时间了

注意：这个有两种螺旋桨，一个是顺时针方向(CW)的一个是逆时针方向(CCW)螺旋桨，在套件里面的包装袋里可以轻易分辨出。形状由旋转方向的背面的尖角的标志确定，一般情况下，CW螺旋桨使用“A”, “A1” 或 “A2”去标记，CCW螺旋桨则使用 “B”, “B1” 或 “B2”去标记。(编号不影响判断螺旋桨)

也需要去确定正确的一面朝上，顶层是凸起的。

这里是我们接CW螺旋桨的视频

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/attach_the_propellers.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

这里是接CW和CWW螺旋桨的详细图片

![Crazyflie 2.X propeller mounting](https://www.bitcraze.io/images/getting-started/cf2_props.png "Crazyflie 2.X propeller mounting")

### 接上软垫


软垫应该接到Crazyflie 2.X和拓展板之间。使电池与电路板分离起到了保护电路的作用。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/attach_the_rubber_pad.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 连接接头


套件里面有两种接头，一种是长的和一种是短的。将两个短的接口插到拓展板上面。


<iframe width="800" height="450" src="https://www.bitcraze.io/videos/attach_headers.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 连接电池


将电池放置到插入到拓展板链接器的接头和电池支架板之间。搞清楚每个引脚对应的位置。因为摩擦力会将电池固定在某一点所以我们需要将它拧紧。


先接通电池，你将完成所有的组转。电池线最好可以弯曲并放置在PCB下方，以免干扰。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/attach_the_battery.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 上电


完全完成了上述操作后，现在是时候上电了！注意按键是按键，不是滑动按键。上电后自测程序将会运行你会看到每个螺旋桨依次旋转。确定是不是每个都转了没有的话，假如没有的话可以检查一下电机是否接好。


<iframe width="800" height="450" src="https://www.bitcraze.io/videos/power_on.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### 开始学习Crazyflie 2.X


在开始之前，让我们先确定哪里是Crazyflie 2.X正面哪里又是反面，因为在飞行和安装拓展板的过程中是非常重要的。
小“凸起”（天线）在前面，蓝色LED在后面。

![Crazyflie board from the top](https://www.bitcraze.io/images/getting-started/frontCF.png "Crazyflie board from the top")

#### 启动顺序

打开Crazyflie 2.X的电源时，它将自动经历一系列简短的事件，以准备飞行。

1.  **开始自我测试** - Crazyflie 2.X检查硬件是否正常
2.  **传感器校准** - Crazyflie 2.X读取其传感器以获取基本值。
必须绝对不要这样做，因此最好将其放在水平面上一秒钟。
3.  **准备起飞!**

#### LED状态说明

您还需要了解LED的含义。

*   **通电后正常:** 蓝色LED（2和3）已完全点亮，并且右前LED（1）每秒闪烁红色两次。
*   **通电后传感器没有完成校准:** 蓝色的LED（2和3）已完全点亮，并且右前的LED（1）以2秒的间隔闪烁红色。 将Crazyflie 2.X放在水平表面上并使其绝对静止以进行校准。
*   **射频连接成功:** 左前LED（4）以红色和/或绿色闪烁。
*   **电量过低:** 右前LED（1）完全点亮为红色。 现在该着陆并为电池充电了。
*   **充电中:** 当右后方蓝色LED（4）点亮时，左后方蓝色LED（3）闪烁。
*   **Boot loader 模式:** 背面的蓝色LED（2和3）大约每秒闪烁一次。
*   **自我测试失败:** 右前LED（1）反复闪烁五个短的红色脉冲，各组之间的停顿时间更长。

## 控制Crazyflie 2.X[](#controlling-the-crazyflie-2-x)


你可以通过电脑或者手机来控制Crazyflie 2.X飞行


### 选择控制器[](#choose-controller-device)


**1.手机**

使用移动设备是进入空中的最快方法，但可能需要更多的操作技能。继续阅读下一部分，以获取有关如何在手机上安装该应用程序的说明

**2.电脑**

使用计算机需要Crazyradio PA和游戏手柄，但可以提供更多选择和更好的控制。如果要使用计算机，请继续阅读[在计算机上安装](#inst-comp) 部分。


## 在手机上面安装[](#installing-on-a-mobile-device)

安装该应用程序并连接到Crazyflie 2.X真的很容易。您所需要的只是支持蓝牙低功耗（BLE）的Android或iOS设备。


### 安装app[](#install-the-app)

Crazyflie客户端可用于Android和iOS。

[For Android, from Google Play](https://play.google.com/store/apps/details?id=se.bitcraze.crazyfliecontrol2)

[For iPhone, from Apple iTunes](https://itunes.apple.com/us/app/crazyflie-2.0/id946151480?mt=8)

![Crazyflie 2.X app](https://www.bitcraze.io/images/getting-started/cf-mobile-app.png "Crazyflie 2.X app")


### 连接Crazyflie 2.X[](#connect-to-the-crazyflie-2-x)


启动应用程序，然后单击连接按钮。这些按钮在Android和iOS应用中的外观不同，您可以在下面看到它们。

![Connect buttons](https://www.bitcraze.io/images/getting-started/connect-icons.png "Connect buttons")

继续阅读[控制飞行部分](#flying)


## 在电脑上面安装[](#inst-comp)


使用计算机驾驶Crazyflie时，您还需要一个标准的游戏手柄([更多信息](//wiki.bitcraze.io/projects:crazyflie:pc_utils:inputdevices))进行操纵，并需要一个Crazyradio PA进行通信。


### 安装选择


这里是一些怎样运行PC客户端的选项

**1. VM**

我们创建了一个虚拟机使你快速将飞机飞起来。这个虚拟机将关于控制飞行的所以软件和环境都预先配置好了。自从它在虚拟环境运行了后，可以使的大多数操作系统能通过相同的方式去工作，这也是我们文档是基于虚拟环境来写的原因。

**2. Windows**

这个是一个可以在Windows上面安装的安装器。这个选项将安装最新版的可执行软件，同时也使控制飞行的最好的选项，但是没有添加环境配置的支持。

在[Windows上的安装](#inst-win)部分中了解更多信息。

**3. Linux**


在Linux环境下，我们可以通过源代码去运行客户端。你可以通过github去下载源码和安装一些软件包。如果你对此感兴趣你点击[github](https://github.com/bitcraze/crazyflie-clients-python/blob/master/README.md)去深入了解。

当你需要配置客户端，先将Crazyradio PA和游戏手柄插入PC的USB接口,然后阅读[配置客户端](#config-client)
。
**4. OS X**


在OS X上，可以从源代码运行客户端。使用此选项，您需要从git克隆源代码并安装一些软件包。如果您对此解决方案感兴趣，请阅读有关如何在[github](https://github.com/bitcraze/crazyflie-clients-python/blob/master/README.md)上进行设置的更多信息。

当你需要配置客户端，先将Crazyradio PA和游戏手柄插入PC的USB接口,然后阅读[配置客户端](#config-client)
。


## 在VM上面安装[](#inst-virtualmachine)

虚拟机（VM）可帮助您尽快上线，它已预装了飞行和开发所需的所有软件。不幸的是，最近有一些关于使用带有USB的VM的问题的报告。如果您在飞行时遇到问题，请考虑采用本机解决方案。

### 安装VirtualBox[](#inst-virtualbox)

在下载虚拟机​​之前，您必须在计算机上安装VirtualBox或其他虚拟化应用程序。VirtualBox是一个跨平台的虚拟化应用程序，可导入并运行我们的预配置虚拟机。

[下载并安装 Oracle VirtualBox.](https://www.virtualbox.org/)


### 下载Bitcraze虚拟机[](#download-vm)


一旦安装了VirtualBox，就可以从[Bitcraze VM](https://github.com/bitcraze/bitcraze-vm/releases/)发行页面下载虚拟机​​。


### 安装虚拟机[](#inst-vm)

下载虚拟机​​后，双击它。VirtualBox现在将开始，并要求您导入虚拟机。单击导入。


### 启动虚拟机[](#start-the-virtual-machine)

现在是时候启动Bitcraze虚拟机了。在VirtualBox中，突出显示Bitcraze VM并启动它。

### 升级源代码[](#update-src)

在虚拟机中，双击桌面上的“更新所有项目”图标。这会从GitHub提取所有项目的最新源代码。

![Update all projects icon](https://www.bitcraze.io/images/getting-started/update-all-projects-icon.png "Update all projects icon")


### 安装硬件[](#install-hardware-vm)

*  将Crazyradio PA插入USB端口。
*  将游戏控制器插入USB端口。

### 在虚拟机上面配置USB[](#config-usb-vm)

**1. Windows**


*   安装[Crazyradio Windows USB驱动](https://wiki.bitcraze.io/doc:crazyradio:install_windows_zadig).
*   在右下角单击USB图标，然后选择“ Bitcraze Crazyradio PA USB dongle”。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic5Final.png "USB settings")

*   现在，在同一列表中选择您的游戏控制器。

**2. Linux**


*   在右下角单击USB图标，然后选择“ Bitcraze Crazyradio PA USB dongle”。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic5Final.png "USB settings")

*   现在，在同一列表中选择您的游戏控制器。

**3. OS X**


*   在右下角单击USB图标，然后单击“ USB设置”。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic2.1Final.png "USB settings")

*   单击USB过滤器的“ +”图标。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic3Final.png "USB settings")

*   从列表中选择您的游戏控制器。单击确定。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic4Final.png "USB settings")

*   现在，再次单击USB图标，然后选择“ Bitcraze Crazyradio PA USB加密狗”。

![USB settings](https://www.bitcraze.io/images/getting-started/SwPic5Final.png "USB settings")

*   现在，在同一列表中选择您的游戏控制器。


### 启动Crazyflie客户端[](#start-client-vm)

双击VM桌面上的“ Crazyflie客户端”图标

![Crazyflie client icon](https://www.bitcraze.io/images/getting-started/cf-client-icon.png "Crazyflie client icon")

Continue reading about [configuring the client](#config-client)

继续阅读有关[配置客户端](#config-client)的信息


## 在windows上面安装[](#inst-win)

安装程序将Crazyflie客户端安装在Windows计算机上。


### 下载安装程序[](#download-installer)

*   打开网络浏览器，然后转到[https://github.com/bitcraze/crazyflie-clients-python/releases](https://github.com/bitcraze/crazyflie-clients-python/releases).
*   从最新版本下载名为cfclient-win32-install-XXX.exe的文件。


### 安装[](#install)

运行安装程序



### 安装硬件[](#install-hardware-win)

*   将Crazyradio PA插入USB端口。
*   将游戏控制器插入USB端口。


### 安装USB驱动[](#install-usb-drivers)

安装[Crazyradio Windows USB驱动](https://wiki.bitcraze.io/doc:crazyradio:install_windows_zadig)。





### 启动客户端[](#start-client-win)

在开始菜单启动客户端





## 配置客户端[](#config-client)





### 配置你的控制器[](#config-controller)

In the client, open the input device settings. Check if the correct device mapping is chosen, otherwise pick your device type.
在客户端中，打开输入设备设置。检查是否选择了正确的设备映射，另外请选择您的设备类型。

![Controller settings](https://www.bitcraze.io/images/getting-started/configure_your_controller.PNG "Controller settings")





### 下载最新的firmware[](#latest-fw)

*   打开网络浏览器，然后转到[https://github.com/bitcraze/crazyflie-release/releases](https://github.com/bitcraze/crazyflie-release/releases). 如果您在VM上，请在VM中打开浏览器。
*   从最新版本下载名为crazyflie-xxx.zip的zip文件。

!!!note

    注意：您必须具有zip文件，某些浏览器在下载后会自动解压缩。

### [](#update-fw)

*   关闭Crazyflie。
*   按住电源按钮3秒钟，以引导加载程序模式启动Crazyflie。两个蓝色LED都将闪烁。
*   返回Crazyflie客户端，然后单击Connect-> Bootloader菜单。

![Update firmware dialog](https://www.bitcraze.io/images/getting-started/update_firmware.PNG "Update firmware dialog")

*   单击“Initiate bootloader cold boot”按钮。几秒钟后，状态应显示为“已连接到引导加载程序”。
*   单击“Browse”按钮，然后转到主页/ bitcraze /下载，然后选择您先前下载的zip文件。
*   点击“Program”按钮。进度条将从0％变为100％两次，因为两个处理器的固件已上载到Crazyflie。
*   单击“以固件模式重启”按钮。Crazyflie会重新启动，并且马上更新。
*   关闭bootloader窗口





### 连接到Crazyflie[](#connect-pc-client)

*   在Crazyflie客户端中，单击左上角的“扫描”按钮。您的Crazyflie的广播设置显示在下拉列表中。
*   从下拉列表中选择您的Crazyflie。

![Connect dialog](https://www.bitcraze.io/images/getting-started/connect_to_the_crazyflie.PNG "Connect dialog")

*   点击“Connect” 按钮。

现在，您已经将Crazyflie连接到客户端，遥测数据将连续不断地从直升飞机发送到客户端。当您在附近移动Crazyflie时，您会看到航班数据实时更新，以及电池状态和链接质量。





## 起飞[](#flying)

在飞行之前你需要知道一些基本的知识。





### 方向[](#orientation)

首先，当直升机离你很远时，飞行要容易得多。蓝色LED位于背面，因此开始飞行时，请使其始终指向您的方向。





### 操纵四轴飞行器[](#maneuvering)

驾驶四轴飞行器时，控件有四个主要方面，Roll，Pitch，Yaw和Thrust。

![Axis](https://www.bitcraze.io/images/getting-started/AxisImage.png "Axis")

*   **Roll -** 是绕水平轴从后到前穿过四轴飞行器的旋转。从字面上看，这会滚动Crazyflie并将其向左或向右移动。
*   **Pitch -** 是绕水平轴从左到右穿过四轴飞行器的旋转。这会使Crazyflie倾斜并向前或向后移动。
*   **Yaw -** 是绕垂直轴的旋转。这将使四轴飞行器向左或向右旋转。通过将Crazyflie的前部指向不同的方向来更改飞行方向时使用偏航。
*   **Thrust -** 调整Crazyflie的高度。





### 移动应用/游戏控制器[](#the-mobile-app-game-controller)

游戏手柄或移动应用程序上的控件具有以下映射：

![Control mapping](https://www.bitcraze.io/images/getting-started/controller.png "Control mapping")





### 正常飞行[](#normal-flight)

在不触摸任何其他控件的情况下推入时，可能会是这样。Crazyflie通常在没有补偿的情况下会向某个方向漂移，这完全正常。

<iframe width="800" height="450" src="https://www.bitcraze.io/videos/normal_flight.mp4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>








### 地面效应[](#ground-effect)

当直升机靠近地面飞行时（离地面不到几分米），这受所谓的地面效应影响。感觉是空气很滑，几乎就像在冰上滑行一样。为了避免这种情况，尤其是在学习飞行时，刚起飞时要用很多推力，然后再放松以进行水平飞行。





### 如果Crazyflie不平衡[](#unbalanced)

如果起飞时您的Crazyflie漂移很大，则应检查一些事项。

*   确保电池居中。如果它向任一侧滑得太远，则Crazyflie可能很难补偿它。
*   检查螺旋桨旋转自如。轻轻吹动它们，并确认它们转动了。常见的问题是头发卡在螺旋桨和马达之间。如果这是问题所在。只需将螺旋桨从电动机上拉下，去除头发，然后重新安装螺旋桨即可。
*   检查螺旋桨是否平衡，[参见平衡螺旋桨指南](/balancing-propellers/)


### 给电池充电[](#charging)

要为Crazyflie 2.X的电池充电，只需插入micro USB电缆即可。确保Crazyflie已打开电源。电池充电时，左后方的蓝色LED将闪烁。当LED完全点亮时，电池即已充电。


### 开始飞行![](#go-fly-)

祝你玩的愉快



