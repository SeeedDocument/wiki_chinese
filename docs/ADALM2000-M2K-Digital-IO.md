---
name: ADALM2000 M2K Digital IO(数字 IO)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---

## 简介

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-15_16-46-33.png?cache=)

1.	数字通道编号 - M2K的物理引脚
2.	通道输入状态 - 表示M2K读取的输入
3.	通道方向 - 指示通道设置：输入/输出
4.	通道输出状态 - 表示由M2K配置的输出值


## 使用示例

###　IO操作

- 1.运行仪器
- 2.将数字通道0连接到通道7
- 3.启动数字IO仪器
- 4.使用电压表/示波器/逻辑分析仪监控通道0
- 5.通过单击方向按钮将通道0设置为输出通道7输入状态与通道0输出状态相同。电压表显示通道0输出状态（5V / 0V）

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-15_16-51-11.png?cache=)

- 6.通过（多次）单击更改通道0输出状态（多次）通道7输入状态与通道0输出状态相同。电压表显示与通道0输出状态相同的状态（5V / 0V）


### 分组操作

- 1.进行以下连接

    - 通道0→通道8
    - 通道1→通道9
    - 通道2→通道10
    - 通道3→通道11
    - 通道4→通道12
    - 通道5→通道13
    - 通道6→通道14
    - 通道7→通道15

- 2.启动数字IO仪器
- 3.还使用逻辑分析仪监控这些连接（使用面包板断开连接）
- 4.将DIO 0-7设置为 Grouped 接口

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/dio-uc/image5.png)

- 5.将所有通道DIO8-15设置为输出
- 6.将 DIO8-15 输出状态设置为 Random (随机)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-15_17-10-13.png)

- 7.将所有通道8-15设置为输入
- 8.将组方向设置为输出
- 9.将“组”值设置为随机值  
通道8-15输入状态应表示二进制值  
逻辑分析仪应显示相同的结果

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-15_17-11-24.png)


### 与 Pattern Generator (模式发生器) 的交互

- 1.启动 Digital IO (数字IO) 仪器
- 2.在通道0和8上生成时钟信号  
在数字IO中，组和通道8应该有一个红色突出显示，表明模式发生器拥有通道的所有权。  
用户无法与这些通道互动。逻辑分析仪显示通道0和8正确生成的时钟信号
- 3.将通道10连接到通道11
- 4.将通道10设置为输出，将通道11设置为输入
- 5.修改通道10输出状态  
通道11输入状态遵循通道10输出状态  
其余通道正常运作。用户可以设置方向和输出状态，也可以读取输入状态
- 6.运行时，在模式发生器的通道10上设置时钟信号。通道10有一个红色高亮显示，用户不能再与它交互。通道11输入状态可能闪烁，表示可以从通道11读取信号。
逻辑分析仪在通道10处生成一个新的时钟信号，该信号也可以在通道11上读取。

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-15_17-13-47.png)

- 7.关闭图形发生器  
红色突出显示从digital IO中消失，通道现在可以正常工作。


**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**





