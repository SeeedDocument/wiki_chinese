---
name: Scopy Voltmeter(电压表)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---

## 简介

电压表仪器显示 ADC 两个通道的电压读数。  
 
单击 Scopy 窗口最左侧显示的 `Voltmeter` 按钮打开 Voltmeter 仪器。电压表仪器使用 M2k 中的示波器探头1和2，能够测量±20V的DC/AC信号的电压。

!!!Note
    当Scopy连接到M2k设备时，Voltmeter仪器会自动启动校准功能，不需要手动校准。


## 主窗口

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dmm1.png)


## 历史图形

显示每个通道的电压值随时间变化的图形。历史图以条形图的形式展示，其中电压值绘制在x轴上，时间绘制在y轴上。这可以在控制菜单中关闭。 

## 数字显示

显示两个通道的电压数值。显示的电压值可以是直流模式或交流模式有效值。

## 运行/停止按钮

Scopy窗口右上角的 Run/Stop 可用于启动和停止两个通道的测量。停止时会保存两个通道的最后读数。用户也可以通过单击左侧菜单中仪器名称右侧的小白色方块来启动和停止。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dmm2.png?cache=)


## AC/DC 模式

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/ac_modes.png?cache=)

可以为每个通道独立设置AC / DC模式。AC模式将显示信号的VRMS值，并针对20Hz至40kHz之间的频率进行优化，此频率范围分为两个选项。  
  
第一种选择是20Hz至800Hz的频率范围，第二种选择是800Hz至40kHz。当信号的频率不在所选选项的范围内时，仪器中将没有读数。 
 
DC模式将显示-20V至20V信号的直流电压值。


## History 历史

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dmm3.png?cache=)

电压表每个通道具有一个电压随时间变化的历史曲线图。可以通过切换右侧菜单上的ON / OFF开关来独立启用和禁用它们。ON / OFF开关下方有一个选择器。   
  
默认情况下，绘图展示10秒的数据。此选择器允许您选择三个选项之间的历史持续时间：1秒，10秒，60秒。


## Data logging 数据记录

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dmm-logging.png)

可以使用右侧菜单中的ON / OFF开关启用或禁用数据记录。单击Browse可以选择文件。  
  
通过选中文件选择器下方的选项之一，电压表可以覆盖或附加到所选文件。   
  
位于右侧菜单底部的计时器控件控制准备记录的数据量。此控件的可接受值范围介于0秒和1小时之间。默认情况下，spinbox设置为0。在这种情况下，LCD上显示的每个值都将写入所选文件。如果该值例如为4，则电压表将每4秒记录一次文件。


## 峰值保持

可以使用右侧菜单中的ON / OFF开关启用或禁用峰值保持功能。  
  
最小值和最大值在数字显示屏上可见，可以点击reset重置。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dmm7.png)


**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**