---
name: Scopy Logic Analyzer(逻辑分析仪)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 简介

要切换到此仪器，单击主页左侧菜单中的 `Logic Analyzer` 按钮。
 
通过按下Run按钮仪器可以连续运行,或按下Single按钮，触发单次运行。
 
逻辑分析仪由通道管理器，中央信号图和用于不同设置的控制面板组成。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/la-initial.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/la-initial.png?cache=&w=900&h=518&tok=1114d9"  />
  </a>
</figure>
</div>



### 通道管理器配置

通道管理器允许用户启用或禁用通道，设置触发器，创建信号组或将协议解码器设置为组。可以通过选择通道并按下按钮![](https://wiki.analog.com/_media/university/tools/m2k/scopy/la-group-btn.png)  或将一个通道/组拖动到另一个通道/组上来创建组。拖放机制还允许用户重新排序通道。  
按下位于绘图上方的 ![](https://wiki.analog.com/_media/university/tools/m2k/collapse.png)按钮可以折叠通道管理器。  
  
!!!Tip
        图标介绍从左自右


**引脚的通道管理器配置：** 

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_initial_pin.png)

- 切换启用/禁用通道。
- 通道名称。
- 通道索引。
- 下拉选择触发器。
- 通道的复选框。


**组中引脚的通道管理器配置：**

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_group_pin.png)

- 通道名称。
- 通道索引。
- 解码器角色选择的下拉列表。
- 下拉选择触发器。
- 橙色删除标记，用于从组中删除通道。


**组的引脚的通道管理器配置：**

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_group.png)

- 切换启用/禁用组。
- 用于折叠/扩展组的箭头按钮。
- 组名。
- 解码器选择的下拉列表。
- 橙色删除标记用于删除组
- 选中该组的复选框。  

该图显示在启用的通道上捕获的信号数据和活动组的解码数据。  
按 `Trigger` 设置按钮，`General Settings` 按钮或 `Channel Settings` 按钮可以打开控制面板。如上图所示。


### 通用设置



<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/la-general-settings.png?cache=&w=264&h=609&tok=ffecbb" >

</div>



- **Time Base - 时基：** 可以通过按+/-按钮或在编辑框中写入值来更改。按旋钮的中心可在精细/粗略模式之间切换。
- **Position - 时间触发位置：** 可以通过按+/-按钮或在编辑框中写入值来更改。按旋钮的中心可在精细/粗略模式之间切换。
- **Repeated Mode - 重复模式：** 在此模式下使用仪器包括反复等待，获取和显示一个缓冲区。但是，当时基大于1 s / div时，为了避免缓冲等待太久，时间触发器会移动到屏幕最左边的位置，并且信号会立即从左侧开始绘制。绘制整个屏幕。此时，用户可以控制频率。如果修改了时间触发位置，则无论时基值如何，仪器都将返回等待模式。
- **Stream Mode - 流模式：** 启用流模式时，时间触发器自动移动到屏幕上最左侧的位置，启用频率控制，允许用户以任何选定的频率进行流式传输。在此模式下，信号在右侧连续绘制，不受一个屏幕的限制。如果修改了时间触发位置，则无论时基值如何，仪器都将返回等待模式。
- **Frequency - 频率：** 可以通过按+/-按钮或在编辑框中写入值来更改。按旋钮的中心可在精细/粗略模式之间切换。最大频率为3.03 MHz。
- **Export: 导出：** 逻辑分析器可以以.csv（逗号分隔值）和.vcd（值更改转储）格式导出当前数据。使用Export All，您可以从所有可用通道中选择和导出数据，也可以使用下拉列表创建自定义选择。确定应导出哪些通道后，单击Export并选择一个文件。导出的.csv文件与整个应用程序中的仪器兼容，因此您可以在模式生成器中加载文件。



### 通道设置


如果通道管理器中突出显示某个通道，则该面板中将显示该特定通道的设置。所有通道/组允许用户通过在编辑框中写入值来更改名称。  
  
面板右上角的按钮允许浏览活动通道列表，如下图所示。对于组，如果设置了解码器，则此面板中将显示该解码器的必需/可选角色。



## 使用示例

### 前提

- 通过USB将ADALM2000连接到您的计算机。
- 启动Scopy并连接到设备。
- 从左侧菜单中选择逻辑分析器。



### 启用并运行多个通道

- 使用位于绘图左侧的通道管理器禁用8个通道。禁用通道使用 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/la-onoff.png)。
- 使用 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy_hide_inactive.png) 隐藏已禁用通道。该图将仅包含已启用的通道。
- 要获取1 s数据，请使用右侧菜单中的时基选择器将时基更改为100 ms。使用通用设置按钮打开右侧菜单。
- 运行，1秒后您将看到8个信号。


### 创建通道组，解码和改变UI元素

- 1.创建一个包含3个通道的通道组。

使用 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy_select_channel.png) 选择通道。  
选择3个通道后，使用Group按钮创建一个组.

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/create-group.gif)


- 2.为该组设置并行解码器。使用位于组名称右侧的下拉列表来设置解码器。
这3个通道的角色会自动分配给这个解码器。


- 3.使用 `Run` 按钮开始采集。图中 3个通道上方，解码的信息应如下图所示。  


- 4.更改现有组的名称。  
选择组。使用Channel Settings 按钮打开右侧菜单。  
使用鼠标滚轮滚动，直到 `Name` 文本框可见。将组的名称更改为 `GROUP 1`。  
  

- 5.创建另一个包含3个通道的通道组。（见步骤1）。合并两个通道组。
要合并两个通道组，请使用拖放操作。选择一个通道组，然后将其拖动到另一个通道组中。
在第一个通道组（“GROUP1”）中应该有5个通道，第二个通道组应保持不变。  


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/merge-groups.gif)




- 6.应自动分配 `GROUP1` 中剩余通道的角色。观察解码值的变化。  

 
- 7.改变信号颜色和粗细。  
选择 GROUP1。使用 `Channel Settings` 按钮打开右侧菜单。使用鼠标滚轮滚动，直到 `Thickness` 下拉列表。将粗细设置为3。这将更改组中每个通道的粗细。



### 触发设置

- 1.从左侧菜单中，选择 `Pattern Generator`工具。  
选择通道0并创建一个组。  
选择组并使用右侧菜单设置时钟（Clock）模式。  
不要启动 `Pattern Generator`(模式生成器)。
 
- 2.从左侧菜单中，选择 `Logic Analyzer` (逻辑分析仪) 工具。  
使用 `General Settings button` (通用设置按钮) 打开右侧菜单。  
使用时基选择器将时基设置为 1 ms。  
使用时间位置选择器将时间位置设置为 0 ms。
 
- 3.使用图表左侧的通道管理器在通道0上设置触发条件  
![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_initial_pin.png)


- 4.按 `Single` 按钮获取一个数据缓冲区。
图应该保持不变，没有任何信号。


- 5.现在使用左侧菜单启动 `Pattern Generator`。  
模式生成器（Pattern Generator）在第一个通道上生成一个时钟，因此逻辑分析仪（Logic Analyzer）应该触发，现在信号应该在图上可见。


### 与 Scopy Pattern Generator(模式生成器) 的交互

- 1.从左侧菜单中，选择 `Pattern Generator`工具。  
选择通道0并创建一个组。  
选择组并使用右侧菜单设置 UART 模式。设置以下参数：
    - 1.波特baud：115200
    - 2.要发送的数据（data to send） =“hello”。
- 2.使用右上角按钮启动 `Pattern Generator`。
- 3.从左侧菜单中选择逻辑分析仪（Logic Analyzer）。
创建一个包含通道0的组。该组将在通道管理器的底部创建。选择组并使用 `Channel Settings` 按钮打开右侧菜单。
- 4.将 UART 解码器设置到该组。
- 5.将 RX Role 设置到通道0。
- 6.按 Single 按钮来只获取一个数据缓冲区。
根据时基，显示的数据可能会发生变化。在 500μs / div 的时基下，结果如下。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_uart.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_uart.png"  />
  </a>
</figure>
</div>


解码后的数据不可见，不妨使用“缩放”功能查看绘图的特定区域。请将鼠标放在绘图表上并使用鼠标滚轮放大或者缩小。



<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_zoom.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_zoom.png"  />
  </a>
</figure>
</div>


- 7.使用 `Cursors`(光标) 标签左侧的框启用游标。启用光标后，您还可以使用 `Cursors` 标签右侧的锁定图标启用/禁用锁定，如下图所示。  
使用绘图中的手柄移动光标。通过通道管理器下方的光标状态检查其位置和测量信号。  


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_cursors2.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_cursors2.png"  />
  </a>
</figure>
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

