
# Getting started with the Loco Positioning system

## 介绍[](#introduction)

loco定位系统可以配置为两种模式。两路测距（TWR）模式和到达时差（TDoA）模式。在TWR模式下，设置过程更加简单；如果您打算在TDoA模式下使用系统，我们也建议您也使用此模式，因为设置后很容易切换到TDoA。本指南介绍了使用TWR模式的过程，最后介绍了如何切换到TDoA模式。

为了说明锚点的位置，我们记录了两个参考系统，一个带有6个锚点，一个带有8个锚点。6个锚点设置主要用于TWR，而我们建议TDoA模式使用8个锚点。



### 将Crazyflie更新为最新的loco定位firmware[](#update-the-crazyflie-to-the-latest-loco-positioning-firmware)


为了能够使用Loco定位系统，您需要将Crazyflie[更新为最新的固件](https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/#latest-fw)。有关如何更新固件的更多信息，请参见我们的[Crazyflie 2.X入门教程](https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/)中的下载最新固件部分。

您还需要最新版本的[Crazyflie客户端](https://github.com/bitcraze/crazyflie-clients-python/releases)。

要安装Loco定位台，请查看[“扩展台入门”教程](https://www.bitcraze.io/getting-started-with-expansion-decks/)。

## 准备anchors[](#preparing-the-anchors)

在设置系统之前，您需要更新固件并配置节点。

### 下载LPS配置工具[](#download-the-lps-configuration-tool)

**1.Windows安装程序安装**

下载并运行[LPS配置工具](https://github.com/bitcraze/lps-tools/releases).exe安装程序以安装LPS工具。

**2.通过源代码安装(Linux/Mac/Windows)**

Clone the [LPS configuration tool GIT repo](https://github.com/bitcraze/lps-tools) and follow the [readme instruction](https://github.com/bitcraze/lps-tools#running-instruction) to run the tool.

从[github仓库](https://github.com/bitcraze/lps-tools)colneLPS配置工具，并按照[readme](https://github.com/bitcraze/lps-tools#running-instruction)里面所描述的那样去运行该工具。

### 下载LPS的固件[](#download-the-lps-node-firmware)

要获取最新的LPS节点固件，[请转到此处](https://github.com/bitcraze/lps-node-firmware/releases)并下载**lps-node-firmware.dfu**文件。


### 更新节点[](#update-the-nodes)

* 要更新节点，请先打开LPS配置工具。通过USB连接到计算机时，请按住节点上的DFU按钮。这将以DFU模式启动节点。

* 如果您使用的是Windows，则该节点将不会首次被识别。您需要按照[说明](https://wiki.bitcraze.io/misc:usbwindows)使用Zadig安装其USB驱动程序。在DFU模式下，该节点在Zadig中将显示为**STM32 BOOTLOADER**。

![LPS configuration tool](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/press_dfu.png "LPS configuration tool")

*   点击浏览去选择LPS节点固件

![LPS configuration tool](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/browse.png "LPS configuration tool")

*  现在更新节点的固件

![LPS configuration tool](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/update.png "LPS configuration tool")

*  当都更新完后，按一下复位

![LPS configuration tool](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/reset.png "LPS configuration tool")

断开节点与USB的连接，并对所有节点重复相同的步骤，然后再进行配置。

### 将节点配置为anchors[](#configuring-the-nodes-into-anchors)

现在是时候为节点设置模式，将其转换为锚，并为每个锚设置单独的ID。锚点应从0开始向上编号。


!!!note

    为了便于将来识别锚点和管理系统，最好在锚点上标记其ID。

![LPS configuration tool](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/configure.png "LPS configuration tool")

1. 将第一个锚连接到USB（无需按任何按钮）
2. 选择一个合适的**ID**选择
3. **锚定（TWR**模式
4. 单击**应用**将设置写入锚点
5. 对所有锚点重复该过程

## 在房间内布置anchors[](#place-the-anchors-in-the-room)

### Anchor的位置[](#anchor-positions)

为了获得良好的结果，Anchor的放置有一些经验法则：

*   锚应均匀分布在飞行体积周围，并且至少相距2m。
*   锚点应锚点直接尽量在一条直线上。
*   锚定天线应放置在距墙壁，天花板或金属物体15cm处，以免产生反射干扰。在我们的参考设置中，我们通过使用这些[3D打印支架](https://github.com/bitcraze/bitcraze-mechanics/blob/master/LPS-anchor-stand/anchor-stand.stl)来完成此任务。在存储库中，单击**Raw**，然后选择**save as**，然后将文件另存为stl文件。

**1. 6 anchors**

在我们的6个锚点参考设置中，我们在飞行区域上方放置了3个锚点，在飞行区域下面放置了3个锚点，形状为倒三角形。

![reference system](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/loco_ref_system_6_anchors.png "reference system")

**2. 8 anchors**

在我们的8个anchors参考设置中，我们将节点放置在盒子的八个角上，因为这样测量TDoA的位置的效果最好。请注意ID的顺序。

![reference system](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/loco_ref_system_8_anchors.png "reference system")

如果您有8个以上的锚点，建议您先设置一个包含8个锚点的系统，然后再将系统切换到TDoA3，以向该系统添加更多的锚点。有关更多信息，请参见Wiki上的[tdoa3设置页面](https://wiki.bitcraze.io/doc:lps:toda3)。

### 为anchors上电[](#powering-the-anchors)

anchor可以通过下面几种方式供电。

![Powering the anchors](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/power.png "Powering the anchors")

*   **Micro USB** 使用外部电池或电源适配器时，适合固定和便携式设置。
*   **DC接口**使用电源适配器时，适合固定和便携式设置。
*   **螺丝接口**适合固定安装和链接。电缆尺寸最大为0.5mm2。

它们可以同时连接，因此当连接微型USB电缆进行更新或更改配置时，锚点仍可通过螺钉端子供电。所有电源选项都可以处理5-12V的电压，电源应至少能够提供150mA的电流。

## 配置和验证系统[](#configure-and-verify-the-system)

下一节将显示8锚系统，但是6锚设置的过程非常相似，但锚6和7将变灰。

### 打开Crazyflie客户端[](#open-the-crazyflie-client)

现在，当一切都安装完毕并启动电源后，就可以配置系统了，这是通过Crazyflie客户端完成的。客户端和锚点之间的通信通过Crazyflie和LPS平台进行中继。

*  将您的Crazyflie 2.X放在飞行区域的中央。
*  打开CF客户端并连接到Crazyflie 2.X
*  如果尚未完成，请在2Mbit无线电模式下[配置](https://wiki.bitcraze.io/doc:crazyflie:client:pycfclient:index#firmware_configuration)Crazyflie2.X。这样可以减少对UWB无线电的干扰。如果更改了配置，则需要重新启动Crazyflie2.X。
![open the crazyflie client](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/open_the_crazyflie_client.PNG "open the crazyflie client")

### 单击LPS选项卡[](#click-the-lps-tab)

选择LPS选项卡。您可能需要在菜单 View -> Tabs ->Loco Positioning Tab 标签中选中它才能使其可见。

![click the lps tab](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Click%20the%20LPS%20tab.png)

### 检测anchor的状态[](#check-anchor-status)


在“锚定范围”状态框中，检查是否有与Anchor一样多的绿色框。红色框表示Crazyflie 2.X无法与该Anchor通信，也无法获取任何测距数据。在这种情况下，请确认Anchor配置正确，通电且在检测范围内。


![check the anchor status](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Check%20anchor%20status.png "check the anchor status")

### 编辑anchor的坐标[](#enter-anchor-positions)


通过点击**Configure positions**去配置的anchor的坐标

![click configure positions](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Click%20configure%20positions.png "click configure positions")

将会出现一个弹出窗口。单击按钮**Get from anchors**以获取锚点列表，并使用当前存储在锚点中的值填充位置。

![click get from anchors](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Click%20get%20from%20anchors.png "click get from anchors")
![enter anchor positions](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Enter%20anchor%20positions.png "enter anchor positions")

输入系统中锚点的位置（坐标）。注意：以米为单位。

输入新值时，该框会变成红色，表示它与锚中存储的当前值不同。


### 写入坐标到anchors[](#write-position-to-anchors)

*   要将新的锚点位置保存在锚点中，请按下**Write to anchors** 按键。
*   是否从红色变为绿色，这表示新位置已写入锚，红色已写入客户端。回读过程最多可能需要5秒钟，请耐心等待。如果5到10秒后未发生任何更改，则可能无法对所有锚点进行写入，请单击**Write to anchors**按钮尝试再次写入。

![write position to anchors](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Write%20position%20to%20anchors.png "write position to anchors")

### 验证anchor的位置[](#verify-anchor-positions)

验证anchor的位置有助于排除以后的定位问题。

*   将图形设置模式切换为“Anchor identification”
*   将Crazyflie移动到靠近一个锚点的位置
*   验证图中是否显示了正确的锚点
*   对所有anchor重复上述步骤，并更正所有错误配置的anchor地址

![Verify anchors position](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Verify%20anchors%20position.png "Verify anchors position")

### 验证估计坐标[](#verify-estimated-position)

*   将图形设置模式切换回“Position estimate”
*   移动Crazyflie并验证图中的移动是否与物理移动相对应

![Verify estimated position](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/Verify%20estimated%20position.png "Verify estimated position")


### 校准完成[](#calibration-finished)

恭喜，Loco定位系统现已校准！

## 将系统模式切换为TDoA[](#switching-system-mode-to-tdoa)

如果您打算在TDoA模式下使用该系统飞行多个Crazyflie，现在该更改系统模式了。存在两种版本的TDoA测距协议。

*   TDoA 2与8个anchor一起使用。
*   TDoA 3对anchor的数量没有任何限制，因此可以用于更大的系统，因为对于8个anchors的系统而言，它会带来更多的噪音。

### 强制Crazyflie使用TWR模式[](#force-the-crazyflie-to-use-twr-mode)

在crazyflie status部分中，选中TWR单选按钮。
这将启用anchor状态部分中的TDoA2按钮。


![Force TWR mode](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/lps-system-mode-switch-1.png "Force TWR mode")


### 将anchors切换到TDoA模式[](#switch-anchors-to-tdoa-mode)

按下**TDoA 2**按钮，将anchors切换到TDoA模式。

几秒钟后，所有anchors状态框应变为红色，以指示Crazyflie 2.X不再从锚点接收TWR数据。

![Switch anchors to TDoA mode](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/lps-system-mode-switch-2.png "Switch anchors to TDoA mode")

有关系统模式切换和故障排除的详细信息，请参阅[wiki](https://wiki.bitcraze.io/doc:lps:configure-mode)。

### 将Crazyflie切换回自动模式[](#switch-the-crazyflie-back-to-auto-mode)

最后一步，在Crazyflie状态部分中勾选Auto单选按钮，以确认TDoA模式，并确认TDoA2框变为绿色。当Crazyflie切换到TDoA模式并开始从锚点接收数据时，锚点框也应变为绿色。

![Switch to auto mode](https://www.bitcraze.io/images/tutorials/getting_started_with_lps/lps-system-mode-switch-3.png "Switch to auto mode")

如果并非所有锚定框都变成绿色，请参阅[Wiki进行故障排除](https://wiki.bitcraze.io/doc:lps:configure-mode)。

## 下一步[](#next-step)

现在，当您启动并运行了系统的基本功能时，您可能想尝试[使用Loco Positioning](https://www.bitcraze.io/getting-started-with-assisted-flight-position-hold)进行飞行。要阅读更多技术文档，请转到Loco定位[Wiki页面](https://wiki.bitcraze.io/doc:lps:index)。