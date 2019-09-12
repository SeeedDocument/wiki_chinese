---
name: ADALM2000 M2K Network Analyzer(网络分析仪)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 简介

单击菜单列表中的 `Network Analyzer` 切换到此仪器，如图所示。小方块允许您在未打开该仪器界面时运行/停止该仪器。


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_menu.png)


-----

## 前面板

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_controls.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_controls.png"  />
  </a>
</figure>
</div>


### 1. Run/Stop Button (运行/停止按钮)

启动或停止分析仪的捕获工作。用户也可以通过单击左侧菜单上名称右侧的小方块来启动和停止。

### 2. Settings Menu Button (设置菜单按钮)

显示或隐藏通用设置菜单。



<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_control-menu.png?cache=&w=274&h=700&tok=cce758" >

</div>



#### 1.Reference Channel (参考通道)

将示波器探头1+和2+作为相位参考，为网络分析仪设置参考通道。

#### 2.Frequency Sweep Settings (频率扫描设置)
- **Logarithmic/Linear - 对数/线性 ：**   
设置频率轴刻度类型  
- **Min and Max Frequency - 最小和最大频率：**   
设置在波特图中显示的最小和最大频率，最小频率范围为1 mHz至20kHz，最大频率范围为1mHz至20MHz。 
- **Samples Count - 采样计数：**  
设置每次测量的采样数（1-10000）。  


#### 3.Waveform Settings Settings (波形设置)
允许用户更改生成信号的幅度和偏置值。幅度可以设置为 1uV 至 10V 范围内的任何值，偏置值可以从 -5 V 至 +5 V。  

#### 4.Display Settings (显示设置)

允许用户调整波特，奈奎斯特或尼科尔斯显示视图。默认情况下，切换到此仪器时，最小/最大幅度设置为-90 dB / 10dB，可以更改为 -120 dB 至 120 dB 范围内的任何值。最小/最大相位值默认设置为 -180/180 度，也可以更改为 -180 到 180 度之间的任何值。用户可以根据需求自行调整。


### 3.通用设置菜单按钮


<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_gen-settings.png?cache=&w=332&h=300&tok=a27590"  width=275;>

</div>


显示或隐藏控制菜单。`Export` 按钮让您导出网络分析仪数据。

#### 1.Plot (绘图)

您可以选择要在绘图区域中显示的图形（伯德，尼科尔斯或奈奎斯特）

#### 2.Export button (导出按钮)


### 4.Cursors button (光标按钮)

在伯德图上显示或隐藏光标。启用后，光标将显示，您可以通过拖动左\右箭头在图上移动。光标处显示频率，幅度/相位以及Δ幅度/Δ相位


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_bode-cursors.png)


------

## 图形

### Bode Plot (波德图)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_bode.png)


Bode Plot 用两部分显示系统的频率响应，一部分是 Bode 幅度图，其包含在从控制菜单设置的频率上以 dB 表示的幅度, 另一部分是表示相移的 Bode 相图。  
可以从 `Control` 菜单中的 `Frequency Sweep Settings` 和 `Display Settings`中的可用配置修改 Bode 图。



#### 缩放显示

在捕获信号之后，可以按住并拖动频率的最小和最大值来将图形放大到所需的位置，如下所示。这将放大Bode幅度图和Bode相图。要放大或缩小幅度或相位，请使用设置面板中的显示控件。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_bode-zoom.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/na_bode-zoom.png"  />
  </a>
</figure>
</div>

单击鼠标右键返回从控制菜单设置的默认视图。


### Nyquist Plot (奈奎斯特图)


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_nyquist.png)

Scopy 网络分析仪还有另一种显示系统频率响应的方法，就是 Nyquist 图。Nyquist 图是频率响应的极坐标图，它在单个图上显示以dB和相角为单位的幅度，以确定系统是稳定的还是不稳定的。显示设置里通过将最小和最大幅度调整为所需值来控制 Nyquist 图。

要放大或缩小，可以使用+和 - 按钮（参见上图）。放大后，您可以按住左键并拖动图表。


### Nichols Plot (对数幅相图)


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_nichols.png)


Nichols 图是另一种描绘系统频率响应的方法。如图所示，Nichols 图显示了y轴上的对数刻度（dB）和x轴上线性刻度（度）上的相位的增益幅度。您可以使用此图以图形方式轻松确定增益和相位裕度。可以通过获得幅度轴的绝对值相交来以图形方式确定增益裕度。相位裕度由原点和相轴相交之间的距离确定。在 Bode 图或Nyquist 图中绘制时应用于控件的设置也将反映在 Nichols 图中。


------

## 网络分析仪 - 低通滤波器示例


下面的例子我们将展示如何使用网络分析仪来获得低通滤波器电路的频率响应。使用网络分析仪时，需要激励/参考通道（始终为波形输出通道1和示波器通道1）和测量通道（始终为示波器通道2）。


参考下图所示电路：

![](https://github.com/SeeedDocument/ADALM2000-M2K-CN-Version/raw/master/img/Network-Analyzer/na_lpf.png)

为了表征滤波器，我们需要输入/激励(input/stimulus)，以及测量响应的方法，

- 1.参考通道：  
    - 激励：波形发生器通道1（‘w1’）
    - 参考通道测量：示波器正通道1（'+1'）

- 2.响应通道：
    - 滤波器的输出：示波器正通道2（'+ 2'）


由于此示例中的所有内容均以地为参考，因此示波器负输入通道接地。  
 
这种电路的面包板连接如下所示：




<div align="center">
<figure>
  <img src="https://github.com/SeeedDocument/ADALM2000-M2K-CN-Version/raw/master/img/Network-Analyzer/na_lpf_bb.png"  />

</figure>
</div>


在网络分析仪界面中，设置参考：通道1和频率范围：最小频率1kHz和最大频率10MHz。  
  
运行仪器。结果图是低通滤波器对所选元件值的频率响应。  

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/na_lpf_plot.png)


对于大于截止频率的频率，信号的幅度会衰减。


**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**






























<style>
.title{
font-size:22px;
text-indent:20px;  
float:left;
line-height:66px
}
.method1{
  :center;
  float:right;
}
/*vertical-align:middle  是依赖div内子元素最高的行高来实现对某元素居中的，而我们只需要建立一个新元素，给他加上inline-block属性 再把他高度设置为100%就行了,在下面的<img>设置vertical-align就生效了*/
.tiptop{
  height:100%;
  display:inline-block;
  vertical-align:middle;
}
img{
  vertical-align:middle;
}

.text{
  float:left  
}
</style>