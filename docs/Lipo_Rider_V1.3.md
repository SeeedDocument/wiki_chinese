---
name: Lipo Rider V1.3
category: Essentials
bzurl: https://seeedstudio.com/Lipo-Rider-v1.3-p-2403.html
oldwikiname: Lipo_Rider_V1.3
prodimagename: LiPo-Rider-v1.3.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Lipo_Rider_V1.3/
sku: 106990022
---

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/LiPo-Rider-v1.3.jpg)

用绿色能源为您最喜爱的电子套件供电！ Lipo Rider 板允许使用太阳能来运行 5V 供电的设备。 Lipo Rider 板是您的户外传感器设计的绿色电源解决方案。 将 Lipo Rider 板安装到传感器板上，可以永远使用太阳能发电！

LipoRider 非常实惠，易于使用。 不需要编程。 内部充电处理器 IC 能够处理各种组件之间的所有功率流。

在太阳能发电不足的情况下，micro USB 端口允许您通过 USB 为锂电池充电。 它也可以用于编程您的套件，而不需要把 Lipo Rider 板拆卸掉。

Lipo Rider 可以作为单独的板或套件购买（Lipo Rider +锂电池+太阳能电池板）。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4f2fef16bDMAr3&id=533004136068)

产品特征
--------


- Jst 2.0 连接器
- 提高稳定的 5V USB 电源
- 芯片内置充电/充电算法
- 通过太阳能或 USB 充电锂电池
- 通过锂电池或 USB 连接稳定的电源电压
- 两个 USB 端口可让您在为锂电池充电时对套件进行编程
- 电池充满或充电状态的 LED指示灯
- 简单的设计意味着非常实惠
- 通过简单的最终用户修改可扩展到多个锂电池和大型/多个太阳能电池板

创意应用
-----------------

- 分布式户外传感器网络的绿色电源和备用电源
- 锂电池充电器

<div class="admonition caution">
<p class="admonition-title">警告</p>
<li>供应大负载时，电路板可能会变热。</li>
<li>潜在的短路或触电，特别是当室外放置太阳能集电时，设备会变湿。</li></ol>
</div>

硬件概况
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/Lipo-rider-blockdiagram.JPG)

规格参数
--------------

- 小尺寸 - 尺寸 = L42mm×W34mm×D6.8mm
- 锂电池最大充电电流为 900mA
- 锂电池最大供电电流为 600mA
- 电源二极管，以防止从 USB 设备返回到 Lipo 电池

### 主要规格

<table border="1">
<tr>
<th>
项目
</th>
<th>
最小
</th>
<th>
标准
</th>
<th>
最大
</th>
</tr>
<tr align="center">
<td width="400">
U<sub>in</sub> 太阳能
</td>
<td width="200">
4.8V
</td>
<td width="200">
5.0V
</td>
<td width="200">
6.0V
</td>
</tr>
<tr align="center">
<td>
I<sub>charge</sub> (R<sub>Iset</sub>=2.0kΩ)
</td>
<td>
700mA
</td>
<td>
800mA
</td>
<td>
900mA
</td>
</tr>
<tr align="center">
<td>
I<sub>供给</sub>
</td>
<td>
0mA
</td>
<td>
</td>
<td>
600mA
</td>
</tr>
<tr align="center">
<td>
V<sub>batt</sub>(R<sub>x</sub>=0Ω)
</td>
<td colspan="3" rowspan="1">
4.2V
</td>
</tr>
<tr align="center">
<td>
V<sub>source USB</sub>
</td>
<td colspan="3" rowspan="1">
5.0V
</td>
</tr>
<tr align="center">
<td>
V<sub>destination USB</sub>
</td>
<td colspan="3" rowspan="1">
5.0V
</td>
</tr>
</table>

引脚定义和额定值
-------------------------

### 引脚定义和额定值

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>CH 引脚电平（红色LED状态）</th>
<th>OK 引脚电平（绿色LED状态）</th>
<th>声明</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>低电平（ON）</td>
<td>高级（OFF）</td>
<td>充电</td>
</tr>
<tr class="even">
<td>高级（OFF）</td>
<td>低级（最后开启）</td>
<td>完成</td>
</tr>
<tr class="odd">
<td>脉冲信号（Flash）</td>
<td>脉冲信号（ON）</td>
<td>电池不存在</td>
</tr>
<tr class="even">
<td>高级（OFF）</td>
<td>高级（OFF）</td>
<td>两种情况：
<ul>
<li>输入电压低于门电压</li>
<li>输入电压低于电池电压</li>
</ul></td>
</tr>
</tbody>
</table>

#### 硬件组件

**太阳能板**

太阳能电池板通过下部 JST 连接器连接到电路板。 请注意，太阳能充电器 IC 只接受 4.8-6.0V 范围内的输入电压。 如果充电指示灯不亮，可能是由于：


1.锂电池电量充足
2.太阳能电池板电压超出范围（很可能是由于太阳能发电不足）。


在第二种情况下，如果可能，重新安置太阳能电池板来接受更多的阳光。 上述条件都不会阻止 Lipo Rider 向 USB 提供稳定的 5V 电源。

太阳能电池板方程式

太阳能电池板输出功率 = 输出电流×电源电压

例如 1W =输出电流×5V

Iout = 200mA

因此，充电1小时将给予 200mAh，忽略损失。 对于 1000mAH 的电池，在理想条件下，充电完成需要大约5个小时。

**锂电池**

名称 Lipo Rider 建议使用锂聚合物。 然而，锂聚合物和锂离子电池的化学性能相当于可互换使用的两种电池类型。 如果使用多个电池，则并联而不是串联连接，因为充电器 IC 提供 4.2V。

**滑动开关**

 使用滑动开关控制 USB 5V电源。 ON - 从锂电池和/或太阳能关闭充电 - 锂电池和/或太阳能充电禁用

**USB端口**

 source USB 端口是一个 **micro-USB** 端口，用作普通 USB 端口。source USB 端口可用于通过目标 USB 端口为锂电池充电或连接到目标设备。

**目标USB端口**

目标 USB 端口是目标设备要连接的位置。 到达目的地设备的电源将由 Lipo Rider 板提供。 电源将来自太阳能电池板，锂电池或 USB 端口。

#### 不同连接情况下的连接方式

由于组合数量庞大，我只包括主要场景：

**独立模式**

太阳能充电锂电池。

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/Lipo-Rider-v1.2-standalone.JPG)

**USB模式**

太阳能充电锂电池。 锂电池供应目的地USB设备。

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/Lipo-Rider-v1.2-usb.JPG)

**程式模式**

USB 数据线将为锂电池和目标设备进行充电。 数据线将在电源与目标USB设备之间使用。

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/Lipo-Rider-v1.2-program.JPG)

### 示例

#### 户外传感器设备电源

 Lipo Rider 板的一个重要应用是作为户外传感器的经济实惠的电源。 室外传感器设备将由锂电池供电，由太阳能电池板补充。 请注意，不建议仅在太阳能发电上运行户外传感器，因为这可能会在白天有所变化，并可能导致传感器意外复位/断电。 在这种情况下，设备以“USB模式”运行。

如果需要户外传感器设备的固件重新编程，请简单地将微型 USB 端口连接到 PC，如上所述，将将设备置于“程序模式”下。

可以使用较大/多个电池和/或太阳能电池板，但只能用最终用户进行修改。

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/img/LiPo-Rider-v1.3_example.jpg)

Lipo Rider 为 Arduino Duemilanove 提供动力（在这种情况下，我没有严格使用室外传感器，因为我没有连接任何传感器，并且不是户外的，不过我知道您能理解我的重点）

资源下载
---------

-   [Li-Po Rider v1.3 Schematic and Layout in Eagle format](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_V1.3/master/res/Li-Po_Rider_v1.3_sch_pcb.zip)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Lipo_Rider_V1.3 -->
