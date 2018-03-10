---
title: Lipo Rider Pro
category: Essentials
bzurl: https://seeedstudio.com/LiPo-Rider-Pro-p-992.html
oldwikiname: Lipo_Rider_Pro
prodimagename: LiPo_Rider_Pro.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Lipo_Rider_Pro
sku: 106990008
---

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/img/LiPo_Rider_Pro.jpg)

用清洁能源为您的电子套件供电！LiPo Rider Pro 是 Lipo Rider 的增强版，它比 Lipo Rider 增加了负载输出（1A 峰值）。LiPo Rider Pro 电路板可以让您用太阳能电池为 5V 设备供电。LiPo Rider Pro 电路板是您户外传感器安装的清洁电源供电解决方案。将 LiPo Rider Pro 板连接到您的传感器板，在有太阳能时就可以持续运行。它也可以用来给手机充电。

LiPo Rider Pro 非常实惠且易于使用。它不需要编程。您只需要将太阳能电池板，锂电池和负载设备插入它，它就可以工作了。内部充电器 IC 负责处理各个组件之间的电力需求。

如果太阳能电力不足，您可以通过 Mini USB 端口为您的锂电池充电。它也可以用来编程你的套件，从而无需拆卸 LiPo Rider Pro 板。

LiPo Rider Pro 可以作为独立的板子购买或者组成套件购买（LiPo Rider Pro + [锂电池](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.33.1418794cfFUEaw&id=534229881706) + [太阳能电池板](https://seeedstudio.taobao.com/search.htm?q=w+%CC%AB%D1%F4%C4%DC&s_from=newHeader&ssid=s5-e&search_type=item&sourceId=tb.item)）。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.522ac30cVyZ1lO&id=45706878029)

## 产品特性
--------

-   最大 1A 负载电流输出
-   锂电池和太阳能电池板的接口为 JST 2.0
-   稳定输出 5V 电压
-   芯片集成充电/放点算法
-   通过太阳能或 USB 电源给锂聚合物电池充电
-   通过锂电池或 USB 提供稳定的电源电压
-   2 个 USB 端口可让您在为锂电池充电时为其他设备编程
-   LED 灯指示电池充电状态
-   通过简单的修改，可扩展到使用多个锂电池和多个太阳能电池板
-   有 4 个绿色 LED 指示锂电池的电量

## 创意应用
-----------------

-   分布式室外传感器网络的绿色能源和备用电源
-   锂电池充电器
-   手机充电器


<div class="admonition caution">
<p class="admonition-title">Caution</p>
<ol><li>LiPo Rider Pro 与 LiPo Rider v1.0 有不同的接口，前者是 JST 2.0 接口，后者是 JST 2.54 接口。</li>
<li>表面有裸露的元器件，使用时小心雨水和短路</li>
<li>负荷较大时板子可能会发热</li>
</div>

## 操作示例
----------

LiPo Rider Pro 的尺寸如下：

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/img/Liporiderprod.jpg)

规格参数
--------------

<table border="1">
<tr>
<th>
项目
</th>
<th>
最小值
</th>
<th>
典型值
</th>
<th>
最大值
</th>
</tr>
<tr align="center">
<td width="400">
太阳能板输入V<sub>in</sub>
</td>
<td width="200">
4.8V
</td>
<td width="200">
5.0V
</td>
<td width="200">
6.5V(10s)
</td>
</tr>
<tr align="center">
<td>
I<sub>charge</sub> (R<sub>Iset</sub>=3.9kΩ)
</td>
<td>
400mA
</td>
<td>
500mA
</td>
<td>
600mA
</td>
</tr>
<tr align="center">
<td>
输出电流 I<sub>load</sub>
</td>
<td>
0mA
</td>
<td>
</td>
<td>
1000mA
</td>
</tr>
<tr align="center">
<td>
电池充电电压 V<sub>batt</sub>(R<sub>x</sub>=0Ω)
</td>
<td colspan="3" rowspan="1">
4.2V
</td>
</tr>
<tr align="center">
<td>
USB 输入电压 V<sub>source USB</sub>
</td>
<td colspan="3" rowspan="1">
5.0V
</td>
</tr>
<tr align="center">
<td>
USB 输出电压 V<sub>destination USB</sub>
</td>
<td colspan="3" rowspan="1">
5.0V
</td>
</tr>
</table>

引脚定义和含义
-------------------------

**引脚和 LED 用途**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>CH 引脚状态 (红色 LED 状态)</th>
<th>OK 引脚状态 (绿色 LED 状态)</th>
<th>状态</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>低电平 (点亮)</td>
<td>高电平 (熄灭)</td>
<td>充电</td>
</tr>
<tr class="even">
<td>高电平 (熄灭)</td>
<td>低电平 (持续点亮)</td>
<td>完成充电</td>
</tr>
<tr class="odd">
<td>脉冲信号 (闪亮)</td>
<td>脉冲信号 (点亮)</td>
<td>电池未连接</td>
</tr>
<tr class="even">
<td>高电平 (熄灭)</td>
<td>高电平 (熄灭)</td>
<td>两种情况：
<ul>
<li>输入电压低于元器件工作电压</li>
<li>输入电压低于电池电压</li>
</ul></td>
</tr>
</tbody>
</table>

**LED 电池状态指示灯**

像手机一样，LiPo Rider Pro 有 4 个 LED 电池状态指示灯。读取电池电压时，只需把像下图那样按一下 **K2** 按键即可。
![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/img/Lipo3.jpg)

**LED 电池状态指示灯状态**

| 点亮的指示灯数量 | 电池剩余电量 |
|-----------------------------------|-----------------------|
| 4                                 | 90~100%               |
| 3                                 | 60~90%                |
| 2                                 | 30~60%                |
| 1                                 | 10~30%                |
| 0                                 | 0~10%                 |

使用方法
-----

**示例**

**户外传感器设备供电方案**

Lipo Rider Pro 板的一个重要应用是作为户外传感器的持续性电源。室外传感器装置将由太阳能电池板供电的锂电池供电。在这种情况下，设备以“USB 供电模式”运行。请注意，不建议仅在太阳能供电时使用室外传感器，因为在没有足够阳光的情况下可能会出现供电不足而导致传感器不能工作。

如果需要对室外传感器设备编程固件，只需简单地将 Mini USB 端口连接到您的电脑上，设备就会以“编程模式”运行。

可以使用更大的或多个电池和太阳能电池板供电，但仅限于用户自行修改。

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/img/Lipo-Rider-pro.JPG)

**使用太阳能电池板给锂电池充电**

![](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/img/LiPo_Rider_Pro1.jpg)

## 资源下载
---

-   **[数据手册]**[CN3065 Datasheet in PDF](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/res/DSE-CN3065.pdf)
-   **[Ragle 文件]**[Schematic and Layout in Eagle format](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/res/Lipo_Rider_Pro_v0.9b.rar)
-   **[PDF 文件]**[Schematic in pdf format](https://raw.githubusercontent.com/SeeedDocument/Lipo_Rider_Pro/master/res/LiPo_Rider_Pro_v0.9b.pdf)
-   **[其他教程]**[Get Lipo rider pro to charge Ipod or Iphone](http://www.seeedstudio.com/forum/viewtopic.php?f=4&t=3575)
