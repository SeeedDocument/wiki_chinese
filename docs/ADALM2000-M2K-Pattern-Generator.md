---
name: Scopy Pattern Generator(模式发生器)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 简介


要切换到此仪器，单击主页左侧菜单中的 `Pattern Generator` 按钮。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-10_17-26-53.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-10_17-26-53.png"  />
  </a>
</figure>
</div>


利用用户可配置参数，模式发生器仪器可从 M2K 产生输出。它由3部分组成：

- 通道管理器 - Channel manager
- 信号图 - Signals Plot
- 控制面板 - Control Panel


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_2.png)



模式发生器顶部的按钮如下：  

- `RUN` 按钮启动模式发生器。
- `Single`单次运行。
- `gearwheel` 按钮激活控制面板中的通用设置菜单。
- `sliders` 按钮激活控制面板中的图案设置菜单。


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_3.png)


该图显示了模式发生器生成的信号的预览。对于启用的通道，将显示生成的波形。对于信道组（一个或多个信道的组），显示为 `decoder` (解码器)，其目的是以图形方式表示信道组的二进制值。 


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_4.png)

通道管理器面板列出设备上的所有可用通道，并允许用户创建自定义通道配置。  
  
用户可以通过单击 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_5.png) 按钮启用通道，将通道设置为输出。通道名称显示在通道管理器的第二列中，可以从控制面板更改此名称。通道编号位于第三列。这是设备的实际 DIO 编号。`select` 按钮用于将多个通道合并为一个通道组。通道组用于生成跨越多个通道的复杂图案。  
  
要创建通道组，请选择多个通道，然后单击 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_6.png) 按钮。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_7.png)


这些 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_8.png) 按钮可用于从通道组中删除通道或解散通道组（如果单击通道组旁边的按钮）。如果用户选择通道组并单击 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_9.png) 按钮，则通道组也可以解散。类似地，可以将通道组与其他通道或通道组合并，或再分组。您也可以直接拖放元素来分组，如下所示：

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_10.png)

这样做优点是直观方便地对元素重新排序。  
  
![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_11.png) 按钮隐藏未启用的元素，仅显示通道管理器和图形中的已启用元素。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_12.png)




只要单击通道管理器中的元素，它就会突出显示。突出显示的元素在通道管理器中具有较暗的色调，并且图中的相关波形将被白线标记。控制面板中的设置对应突出显示的元素。 


控制面板允许用户设置要生成的波形的参数。 ![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg_13.png) 按钮在信道管理器中起导航作用。Pattern（模式）组合框允许用户选择当前生效的模式。

<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-10_17-33-20.png?cache=" >

</div>

 
  
    


当前模式包括：


- **时钟(Clock)**  
产生用户所选频率，相位和占空比的时钟信号。
- **编号(Number)**  
生成用户所选号码
- **随机(Random)**  
以用户所选频率生成随机值。
- **二进制计数器(Binary Counter)**  
在通道组中的通道上生成二进制计数器。
- **UART**  
生成UART消息
- **SPI**  
生成SPI消息
- **I2C**  
生成I2C消息
- **Gray计数器**  
在通道组中的通道上生成Gray计数器
- **导入(Import)**  
导入CSV文件并输出其内容

输出组合框允许在下列两个驱动器之间选择 Output (输出驱动)  

- PP - pushpull (推挽驱动)
- OD - opendrain (开漏驱动)


`Name` (名称)编辑框更改通道/通道组的名称。`thickness` (粗细)编辑框更改绘图中通道/通道组的粗细。`Color` (颜色)编辑框更改绘图中通道/通道组的颜色。




## 使用示例

-------------------

### 启用并运行一个通道

- 1.启用通道0  - 默认情况下，通道0将生成5khz时钟信号

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image4.png)

- 2.运行模式发生器

- 3.将通道0连接到 oscilloscope (示波器)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-09_16_45_45-ubuntu_running_-_oracle_vm_virtualbox_2.png)

- 4.关闭模式发生器

- 5.修改参数 - 设置频率为1MHz，占空比为70％

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image8.png)


- 6.运行模式发生器

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_12_45_26-ubuntu_running_-_oracle_vm_virtualbox_1.png)


------------------

### 创建一个4通道二进制计数器


- 1.单击通道旁边的空矩形选择多个通道  

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image10.png)

- 2.通过点击 `Group with selected` 按钮创建组  

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image11.png)

- 3.确保通道组已启用, 它应如下图所示。 如果未启用，请单击左侧启用按钮启用它。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image12.png)

- 4.从右侧菜单选择 `Binary Counter` 模式  

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image13.png)

- 5.该图应该类似于二进制计数器

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image14.png)

- 6.运行模式发生器  

- 7.使用 scopy 验证通道 0 和通道 1.

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_14_43_46-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 8.使用 scopy logic analyzer(逻辑分析仪) 或者其他工具验证通道 0,1,2,3

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_14_53_31-ubuntu_running_-_oracle_vm_virtualbox_1.png)


--------------

### 通道组编排

- 1.请确保仪器处于上一章节-- 创建一个4通道二进制计数器 的状态。  

- 2.将通道6拖放到通道组内的通道1和2之间，就像下列gif中一样

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/pg-1.gif)

- 3.将通道3从通道组拖放到通道0和1之间，如下列gif中一样

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/pg-2.gif)

- 4.之后仪器应该如下图所示：  

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image17.png?cache=)

- 5.选择通道组和通道4和5，然后单击 `Group with selected` （已选中的组）

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image18.png?w=500&tok=2c7684)

- 6.使用 logic analyzer(逻辑分析仪) 验证通道 0-6

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_15_17_46-ubuntu_running_-_oracle_vm_virtualbox_2.png)

-----------------------

### 使用拖放操作创建通道组

- 1.将通道12拖放到通道9上，当蓝色突出显示时，您应该松开鼠标按钮。  

- 2.选择新创建的通道组10和11并对它们进行分组（如前面的步骤）

- 3.使能这个通道组  

- 4.在频道管理器中单击选择频道组  

- 5.在设置中选择 random pattern(随机模式)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_16_43_01-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 6.运行 pattern generation (模式发生器)

- 7.使用逻辑分析仪验证通道 9,10,11,12。 生成的模式应与 Scopy 中的模式相同

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_16_43_23-ubuntu_running_-_oracle_vm_virtualbox_1.png)

--------------------

### 隐藏非活动和颜色以及其他UI

- 1.通过在频道管理器中单击选择一个频道组。 将通道组设置中的名称设置为“BinCntGrp”

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_16_52_38-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 2.在频道管理器中选择一个频道。 在频道设置中将名称更改为“DIOZERO”。  

- 3.在 `channel setting`(通道设置) 中将 `LOW Color` 设置为白色，将 `HIGH Color` 设置为橙色。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_16_52_54-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 4.选择 `Hide Inactive` 在 Scopy 中应该如下显示：

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image21.png)

- 5.运行模式发生器之后，即使缺少非活动通道，也应以相同的方式生成信号。  

- 6.全部显示全部显示频道。 信号以相同的方式生成


---------------------

### 运行时更改设置

运行时可以修改/启用/禁用通道。 模式发生器将重新配置并恢复运行模式。 在重新配置时，M2K的所有引脚在此期间都将采用高阻抗。


--------------------


### 单次运行

- 1.选择 Single (单次运行)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/image23.png)

单击单次触发将生成单个缓冲区，然后将所有引脚切换为高阻态。

-----------------

### 特殊模式

- 1.使能一个通道并且将之设置为 `UART` 模式  

- 2.设置参数 `9600, 8 bits, 1 stop bit(1 停止位), no parity (无奇偶校验) ` 输入文本 **HELLO**

- 3.仅选择通道15并点击 `Group with selected`（这将创建带解码器的单通道组）UART解码器应通过通道15弹出.

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/pg-uc/2017-06-12_18_24_32-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 4.监视逻辑分析仪中的通道。 使用UART解码器。 或者使用连接到通道的串行终端。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/2017-06-12_18_26_40-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 5.创建一个包含3个通道的组并选择 `SPI` 模式。 随意设置SPI参数，但请确保发送一些数据。

![](https://wiki.analog.com/_media/university/tools/m2k/2017-06-12_18_28_54-ubuntu_running_-_oracle_vm_virtualbox_1.png)

- 6.监控通道并使用SPI解码器  

- 7.通道应类似于SPI模式。

![](https://wiki.analog.com/_media/university/tools/m2k/2017-06-12_18_30_01-ubuntu_running_-_oracle_vm_virtualbox_1.png)




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