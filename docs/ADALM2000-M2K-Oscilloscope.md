---
name: ADALM2000 M2K Oscilloscope
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


示波器由中央信号波形显示区域和控制面板组成，控制面板内可以对不同仪器选项进行设置，可用范围内的通道上捕获的波形会显示在中央区域内。

要切换到此仪器，单击左侧菜单中的 **Oscilloscope**。


!!!Note
        Scopy连接到M2K设备时，示波器会自动校准。




![](https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-main1.png)


## 通用设置


控制面板从屏幕右侧滑动进出，也可以通过页面底部右侧的多功能按钮 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy_right_panel_settings.png?w=40&tok=147e09) 打开。其中有：


- Channel Settings - 通道设置
- Cursors - 光标
- Measure - 测量
- Trigger - 触发


通道列表在底部菜单栏的左侧，名称左边的按钮用来激活/关闭该通道，点击右边的按钮进入通道设置。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-chn-btn.png?w=115&tok=5f7331)


按压channel处可自定义通道名称。一次只能选择一个通道，光标和测量设置（启用时）将应用于所选的通道。




<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-chn-settings.png" >

</div>

**Time Base - 时间基准**  
它可以通过按下+/-按钮或在编辑框中写入一个值来改变,按压中央旋钮切换精细/粗略模式,下拉菜单以选择合适的测量单位。 


**Position - 水平位置**  
它可以通过按下+/-按钮或在编辑框中写入一个值来改变，按压中央旋钮切换精细/粗略模式，下拉菜单以选择合适的测量单位。

**Volts/Div**  
它可以通过按下+/-按钮或在编辑框中写入一个值来改变，按压中央旋钮切换精细/粗略模式，下拉菜单以选择合适的测量单位。

**Position - 垂直位置**  
通过按下+/-按钮或在编辑框中设置任意电压偏置值。按压中央旋钮切换精细/粗略模式，下拉菜单以选择合适的测量单位。  

**CH Thickness - 波形线宽**  
更改显示区域中的选定通道波形的线条粗细。

**Probe Attenuation - 探头衰减**  
选择探头的衰减倍数  

**Memory depth - 存储深度**  
该参数提供了对应于每个时基值的一对值，它增加了采集的样本数量和采样率。  

**Software AC Coupling - 软件交流耦合**  
启用时起到隔直的作用，当电压值太大而不适合当前图形设置时会十分有用。它只显示信号的波动情况。

**Autoset - 自动设置**  
根据输入信号自动调整偏置值、范围、频率和触发器配置。在使用此功能之前，用户应该启动示波器。




按下右侧面板上的通用设置按钮 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy_wheel.png?w=40&tok=5ec189) 时，将出现一个复选框，提供计算和绘制采集信号的FFT和XY视图的选项。如果启用了XY视图，则会在右侧菜单中显示一个新部分，允许用户选择使用不同的坐标轴和绘图类型的通道。


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-general-settings.png)



示波器可以以 `.CSV` 格式输出当前数据。要打开导出设置面板，请单击位于屏幕右上角的滚轮按钮。点击Export All，从所有可用的通道中导出数据，或者您可以使用下拉菜单创建自定义选择，选定通道后单击“Export”并选择一个文件。  
 

按下两个通道选择按钮右侧的（+）按钮将打开一个面板，允许用户添加数学通道或参考通道。在数学面板中，用户还可以使用通过信道获取的信号来计算不同的方程。定义方程后，按下“应用”按钮，验证函数。然后通过点击Add channe添加一个新的通道，并显示方程曲线图。  
  

仪器名称右侧的小白色方块控制仪器的运行/停止，允许用户在不进入仪器显示界面时运行和停止仪器。点击示波器名称调用Scopy双通道示波器的顶层，如下图所示。

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-main.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-main.png"  />
</figure></a>
</div>


通过单击橙色圆圈打开和关闭通道1，通过单击紫色圆圈打开和关闭通道2。打开的通道由填充圆圈表示，关闭的通道由空心圆圈表示。波形颜色对应圆圈颜色。


## 设置测试信号

为了引入基本的示波器操作，需要一个信号源，我们使用Scopy双通道信号发生器产生正弦波，接入两个示波器通道。示波器有两个平衡输入，信号发生器有两个不平衡输出，我们将示波器输入端正极连接到信号发生器输出，将示波器输入端负极接地。四针单排接头可用于进行这些连接，接线连接如下：

- 黄色到橙色（信号发生器1输出到示波器1正极输入）
- 黑色（与黄色相邻）到橙色/白色（示波器1负极输入接地）
- 黄色/白色到蓝色（信号发生器2输出到示波器2正极输入）
- 黑色（与黄色/白色相邻）到蓝色/白色（示波器2负极输入接地）

点击仪器菜单中的 **Signal Generator** 调用信号发生器，信号发生器初始化时两个通道都打开，只需要选择波形，幅度和频率。单击通道1菜单，将波形 Waveform 设置为 `Sine`(正弦)，振幅设置为 4伏，频率设置为 1 kHz，偏置设置为 2伏。设置完成后，点击 `Run`，如下图所示。用户可以通过直接输入数字并点击 `Enter` 或 `+` 和  `-` 进入，也可以直接在数字下选择单位。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/sig-gen.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/sig-gen.png"  />
</figure></a>
</div>


## 设置水平和垂直量程

单击仪器菜单中 `Oscilloscope` 打开双通道示波器，示波器初始化时两个通道都处于激活状态，因此应关闭通道2以查看通道1。打开通道1的通道设置并禁用软件交流耦合，然后将时基设置为 `500μs / Div`，将垂直刻度设置为 `1 V / Div`，然后单击 `Run`，如下图所示。

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-sig-1.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-sig-1.png"  />
</figure></a>
</div>


为了去掉信号的直流分量，启用第一个通道的交流耦合功能使得信号直流分量为零。您还可以使用下拉列表更改存储深度，增加样本数和采样率，如下图所示。如果在存储深度模式下水平触发位置被修改，则存储深度将设置为默认，因为触发前的样本数限制为 8k。



<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-sig-2.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-sig-2.png"  />
</figure></a>
</div>


## 示波器触发

通过单击 `Trigger` 菜单进行基本示波器触发设置，如下图所示。在本例中，我们将示波器配置为在通道1输入信号的上升沿触发，阈值为0V，同时提供滞后功能以改善示波器对于噪声触发信号的触发性能。滞后值将作为触发源随后设置在通道中


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-trigger.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-trigger.png"  />
</figure></a>
</div>


## 使用光标测量信号

测量光标可用于时基和垂直刻度，可通过单击Scopy显示屏右下方的 `Cursors` 进行设置，单击 `Cursors` 图标旁边的菜单图标可访问光标菜单。光标菜单显示在Scopy显示屏的右侧，允许单独打开和关闭每个光标对。时基光标显示当前水平位置设置下的绝对时间，表示为 Δt，频率为 1/Δt。垂直刻度光标显示绝对电压值，表示为ΔV。通过拖动位于光标末端的向上/向下箭头来移动光标。  
  
使用右侧菜单中的位置控制，可以在任何角落显示光标读数。此外，可以使用右侧菜单中的相应控件修改读数的透明度。下图显示了垂直和水平光标打开时的 4V 1KHz 信号。

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-cursors-sig.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-cursors-sig.png"  />
</figure></a>
</div>



## 使用内置信号测量功能


通过 Scopy 可以直接对采样数据进行数学计算，并通过单击位于Scopy显示屏右下方的Measure进行访问。单击Measure标签旁边的菜单图标可访问测量菜单。测量菜单显示在Scopy显示区的右侧，并为用户提供了各种信号测量，点击Display All以显示所有可用信号测量值，也可以使用自定义下拉菜单单独显示测量和统计数据。如图所示：


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-measure.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-measure.png"  />
</figure></a>
</div>


## 使用 Math 通道

通过单击底部菜单栏中 `CH 2` 旁边的 `+` 按钮，可以将数学通道添加到仪器中。菜单提供了添加数学通道和参考通道的控制选项，点击数学选项卡时，数学配置菜单，用户可向通道中添加数学方程。表达式可以直接输入或使用小键盘进行编辑，小键盘里包含数字，各种数学函数，数学运算和下拉选项 `t`。其中下拉选项包含来自硬件通道的数据。单击 `Apply` 按钮，检查表达式是否有效。表达式下方线条绿色表示有效，红色表示无效。在此例中，设置 `f(t) = sqrt(t0 * t0)` 以创建包含通道1的绝对值的数学通道，然后点击 `Add channel` 以添加数学通道。新添加的频道将显示在底部菜单栏中，并随时可以通过单击频道名称旁边的X按钮删除。如图所示：


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-math.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-math.png"  />
</figure></a>
</div>


将通道添加到列表后，可以编辑 Math 通道的表达式。如图所示，您只需打开数学通道设置。数学通道设置中包含方程式和 `Edit function` 按钮，点击 `Edit function` 打开一个类似于添加通道的面板。您可以修改函数并点击 `Save` 保存和更新所有设置。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-math-edit.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-math-edit.png"  />
</figure></a>
</div>


## 使用参考通道

使用上一节中描述的相同 `+` 按钮，选择 `Reference` 选项卡，加载配置面板，您可以从 `.csv` 文件中加载之前捕获的信号。选择文件和要导入的通道（或全部导入）后，点击 `Import selected channels` ，在底栏菜单中添加一个新通道。与 Math 通道类似，您随时可以通过单击名称旁边的 `X` 按钮删除参考通道。

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy/osc-ref.png?id=university%3Atools%3Am2k%3Ascopy%3Aoscilloscope" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/osc-ref.png"  />
</figure></a>
</div>



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