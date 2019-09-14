---
name: Scopy Power Supply
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 简介

电源仪器是Scopy仪器菜单列表中的最后一项，默认情况下显示在Scopy窗口的最左侧。



![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply1.png?w=200&tok=33f254)


仪器名称右侧的小白色方块控制仪器的运行/停止功能，允许用户在不打开仪器窗口时运行和停止仪器。单击电源名称将显示顶层电源供应，如下图所示。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply2.png)


该仪器允许您控制M2K 的V +（正输出）和V - （负输出）引脚的电压输出。  
在窗口的中央部分，显示了正输出和负输出的值。当每个输出启用时，Scopy将连续测量V和V +引脚上施加的电压值。  
对于正输出，两个橙色LCD数字表示当前设置的值（单位为伏特）和测量回来的值（单位为伏特）。对于负输出，这些LCD数字为紫色。  
在每个输出的LCD数字下方，刻度将以图形方式显示测量值。


## 控制

### Tracking Ratio Control - 跟踪比值控制


#### Independent Controls - 独立控制

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply3.png?w=200&tok=f40215)

通过选择右侧菜单顶部的“独立控制”（ Independent controls）模式，可以独立控制正负输出，方法是在右侧菜单上设置它们的值，然后单击Enable绿色按钮。
启用后，启用绿色按钮将变为禁用红色/橙色按钮，相应的输出处于活动状态，直到再次单击“禁用”按钮。


#### Tracking - 跟踪

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply4.png?w=200&tok=6b5ebd)

该选项允许您将负输出（V - 引脚）表示为正输出的函数：V- = -(ratio * V+)。例如，正输出为1V而比值为0.7，负输出将为-0.7伏。  
  
在此模式下，负输出通道的启用按钮被禁用;通道启用与否随着正输出动态变化。


### Positive/Negative Output Control - 正/负输出控制

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply5.png?w=200&tok=41fafa)

在“正输出”控制，输出可以被设置为从0至5 V，而在负输出控制，输出可以被设置为从-5至0 V，单位为Volts 或mVolts。您可以直接输入值，或使用+/-控制来更改电压输出值。递增/递减值可以通过执行以下操作来改变：默认递增/递减值是1 V，您可以通过在圆圈内单击将其更改为100 mV，小黑点应更改为橙色/红色。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/powersupply-circle.png)



**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**
