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

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_14-57-31.png?w=600&tok=e70c6f)

信号发生器仪器可用于通过用户可配置参数从M2K生成模拟输出。它由3部分组成：

- Channel selector (通道选择器) - 启用/禁用通道以及每个通道的控制面板。
- Signal Plot (信号图) - 信号的可视化表示
- Control Panel (控制面板)- 更改信号参数


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-25-53.png)

可以生成四种类型的信号。

- 恒定(Constant) - 用户可选振幅的直流信号
- 波形(Waveform) - 具有各种可定制参数的AC信号
- 缓冲器(Buffer) - 从文件导入信号
- 数学(Math) - 信号由数学方程定义


恒定信号只有一个参数，输入信号波形的振幅，信号类型可以是以下之一：

- Sine (正弦波)
- Square (方波)
- Triangle (三角波)
- Trapezoidal (梯形波)
- Rising sawtooth (上升锯齿波)
- Falling sawtooth (下降锯齿波)


所有信号都具有幅度，偏移，相位和频率参数。选择方波将解锁占空比参数。选择梯形波形将禁用频率，因为此参数将根据时序类别中的其他4个值计算 (Rise time, High time, Fall time, Low Time)

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-29-24.png)




缓冲信号类型将文件作为输入。缓冲信号支持的文件类型为：  

- .bin - 32位二进制浮点格式
- .wav - 波形音频文件格式（16位整数）
- .csv - 以逗号分隔的值(Comma separated values)
- .mat - MATLAB Mat格式


CSV文件格式支持原生 CSV (例如：[https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c](https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c)) 以及 scopy 格式的 CSV (例如 ：[https://gist.github.com/adisuciu/5abffa8233707c7b95585e80fbb1dde9](https://gist.github.com/adisuciu/5abffa8233707c7b95585e80fbb1dde9))。这意味着可以在示波器中获取信号并将信号反馈到信号发生器中。MAT 文件格式仅支持实型数组（无复杂波形）


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_16-06-06.png?w=600&tok=99c7a6)

数学信号类型允许生成定义为数学方程的信号。


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_15-25-02.png)


除此之外，还可以添加噪声。通过选择“None”，信号中才不会添加噪声。其他噪声类型包括：

- Uniform (均匀噪声)
- Gaussian (高斯噪声)
- Laplacian (拉普拉斯噪声)
- Impulse (脉冲噪声)




## 使用示例

在示波器的 CH1 和 CH2 与信号发生器之间建立反馈回路。

-----

### 运行单个通道

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-25-33.png?cache=&w=900&h=610&tok=7ce312)


- 禁用通道 2
- 选择 5V 幅度和 10kHz 的正弦波
- 运行信号发生器
- 监控示波器


------


### 运行双通道


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-30-13.png?cache=&w=900&h=607&tok=bae3f8)

- 继续上面的示例
- 启用通道2并选择 5V 幅度和 20kHz 的三角波
- 加入 1V 幅度的高斯噪声
- 监控示波器


-------

### 产生方波

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-33-14.png?cache=&w=900&h=615&tok=835516)


- 选择占空比为25％的方波
- 将噪声幅度降低至200 mV
- 监控示波器


-------

### 产生梯形波

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-34-52.png?cache=&w=900&h=613&tok=3ffab2)


- 选择梯形波形，上升/上升/下降/下降 均设置为 1ms
- 监控示波器


------

### 从wav文件中生成波形

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-36-05.png?cache=&w=900&h=614&tok=8c08f0)


- 选择缓冲模式 (buffer mode) 并选择波形文件。 通常可以在 C:\Windows\Media 中找到合适的 wavefile
- 信号发生器自动选择合适的采样率
- 监控示波器（如果可能，将扬声器连接到输出的通道）


-----


### 生成阶梯波形

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-38-32.png?cache=&w=900&h=613&tok=87a219)


- 选择上面提供的 stairstep csv文件：[https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c](https://gist.github.com/adisuciu/7aa30bc9e545db23a17e86d23ae4f53c)
- 消除噪声，禁用 CH1 并将幅度增加到 5V
- 监控示波器

------

### 通过函数生成波形

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_2018-05-16_17-39-23.png?cache=&w=900&h=614&tok=95ec0f)


- 选择数学模式并输入函数 2*(cos(6*t)*sin(2*t))
- 监控示波器



------


**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**