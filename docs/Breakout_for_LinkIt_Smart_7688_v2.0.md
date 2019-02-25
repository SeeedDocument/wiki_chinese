---
name: Breakout for LinkIt Smart 7688 v2.0
category: LinkIt
bzurl: https://www.seeedstudio.com/Breakout-for-LinkIt-Smart-7688-v2.0-p-2641.html
oldwikiname: Breakout for LinkIt Smart 7688 v2.0
prodimagename: Breakout_for_LinkIt_Smart_7688_v2.0_product_view_700.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Breakout_for_LinkIt_Smart_7688_v2.0   
sku: 103100022
---

---
**Breakout for LinkIt Smart 7688 v2.0** 是基于 LinkItTM Smart 7688 的开发板，它是具有 Grove 端口的集成扩展板。 这种板子将帮助初学者快速入门，因为它可以节省大量的工作，并通过简化布线使制作更容易。 它配有 USB，以太网 和 3.5mm 音频端口，并支持 I2C，UART 等串行总线。

![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/blob/master/image/Breakout_for_LinkIt_Smart_7688_v2.0_product_view_700.jpg?raw=true)

**版本更新**

|版本 | 发布日期 |支持状况 |备注                 |
|------------------|--------------|---------------|-----------------------|
|版本 1.0       |2015年11月 |支持     |	无                 |
|版本 2.0       | 2016年4月	  |支持     | 参考特性更新|

**特性更新:**

* 支持录音功能。
* 3.5mm 手机连接器（音频插孔），支持 OMTP 和 CTIA 协议。 您可以通过切换交换机使用任一协议。 关于如何切换协议，请下拉本页面并阅读 **如何在 OMTP 和 CTIA 之间切换手机连接器协议**


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4d6f2139A3dPkl&id=533263194788)

## 产品特性
---
* Grove 接口使布线更容易，并允许 Grove 模块扩展。
* USB主机
* 音频输出
* 以太网端口
* 性价比高
* 支持录音功能
* 可在 OMTP 和 CTIA 之间切换

## 创新应用
---
* IoT /网关设备。
* 机器人
* 智能多媒体设备


## 规格参数
---
|输入电压|工作电压|
|:---------------:|:---------------:|
| 5.0V（带 USB 电源端口）| 3.3V |


!!!note
    调试引脚，以太网引脚 和 USB A 类主机引脚与 MT7688 连接，其他引脚与 ATmega32U4 连接。

## 硬件概述
---
![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/blob/master/image/Breakout_for_LinkIt_Smart_7688_v2.0_hardware_connections_1200_s.jpg?raw=true)


|硬件|数量|硬件|数量|硬件|数量|
| ---| ---| ---| ---| ---| ---|
|调试端口| 1 |耳机端口| 1 |辅助引脚| 2 |
|以太网端口| 1 |引脚切换协议| 6 | Grove 连接线| 3 |
| USB A型| 1 |立体声扬声器驱动接口| 1 |耳机端口|1|


### 关于Grove界面

如果您曾经使用过Seeed的 [Grove](http://wiki.seeedstudio.com/cn/Grove_System/) 产品，那么您将会爱上这种模块。 使用这种端口，您可以告别跳线和焊接工作，您可以使用这些功能模块来实现更强大的应用。

### 如何在 OMTP 和 CTIA 之间切换手机连接器协议

![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/Breakout_for_LinkIt_Smart_7688_v2.0_switch_procotol_1200_.jpg)


如果比较 V1.0 和 V2.0 版本，您可以注意到右下角有六个引脚和两个跳线帽。 这些引脚用于切换手机连接器协议。 当您将微型跳线（两者）设置为左边四个引脚时，使用协议 OMTP 。 当您将微型跳线（两者）设置为右边四个引脚（如图所示）时，使用协议 CTIA 。 如下图所示：
LinkIt Smart 7688 v2.0 的 CTIA OMTP 交换机 Manner.JPG
请注意，要使用录音功能时，您需要将板载固件更新为 LinkIt Smart 7688 固件（版本v0.9.2以上）。

![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/Breakout_for_LinkIt_Smart_7688_v2.0_CTIA_OMTP_Switch_Manner.JPG)

!!!note
    由于板载闪存的写入/读取速度有限，建议您使用外部存储设备。


## 入门
---
在本教程中，您将用 LinkIt Smart 7688 V2.0 制作一个简单MP3播放器。

### 材料准备
除了 Linkit Smart 7688 V2.0 外，这个应用程序还需要的其他材料。 在开始之前，请确保您准备了一切，或者访问Seeed [商城](https://shop123145485.taobao.com/?spm=a230r.7195193.1997079397.2.UZu8Jk&qq-pf-to=pcqq.c2c) 来获取它们。

|LinkIt Smart 7688 × 1|USB连接线（A型、微型B）×2|UARTBee × 1 |杜邦线 × 3
|:---:|:---:|:---:|:---:|
|![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/linkit%20smart%207688.jpg)|![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/48cmUSBc.jpg)|![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/UartSBee%20V5_01.jpg)|![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/jw100n.jpg)
|[立即购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.6a77517b8Okzfx&id=524890877407)|[立即购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.32773eecsNElSp&id=521385344999)|[立即购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.36fb87ecjdoIvQ&id=45486590205)|[立即购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.19f0ef48DqRUyt&id=45783422315)|

确保您准备好下面的两个材料
- 立体声扬声器（3.5mm 音频连接线）×1
- USB 闪存盘（内置 MP3 格式的音频文件）×1

**步骤一:**  请参阅[这里](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688#Getting_Started)将 LinkIt Smart 7688 连接到 Internet 。


!!!note
    您可以将跳线连接到 MT7688 UART2 端口，而不用将其焊接到引脚 **8** ，引脚 **9** 和引脚 **GND** 。

!!!note
    在极少数情况下，您可能无法成功连接到Internet，请重新启动操作系统。

**步骤2：** 打开 USB 串口的控制台。

  **步骤3：** 连接所有部件，如下所示：

![](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/raw/master/image/Breakout_for_LinkIt_Smart_7688_demo_connection_New.jpg)

!!!note
    这是 LinkIt Smart 7688（v1.0）的 Breakout 数据。

**步骤4：** 通过控制台中的 **cd /Media/USB-A1** 类型输入文件。

**步骤5：** 通过在控制台中输入 **madplay filename.mp3**，使用应用程序 **Madplay** （安装在 OpenWRT 上）播放音乐。

**步骤6：** 现在你会听到音乐。

## 资源下载
---

* [Schematic files](https://github.com/SeeedDocument/Breakout_for_LinkIt_Smart_7688_v2_0/blob/master/resource/Breakout_for_LinkIt_Smart_7688_v2.0_schematic_files.zip?raw=true)
* [LinkIt smart 7688](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688)
* [OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
* [Link to buy a LinkIt Smart 7688](http://www.seeedstudio.com/depot/LinkIt-Smart-7688-p-2573.html?cPath=122_142)
