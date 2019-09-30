# **Pluto 内部基本组成**


![](https://wiki.analog.com/_media/university/tools/pluto/users/pluto_simple_block_diagram.png?w=200&tok=118d27)

ADALM-PLUTO 的基本框图很容易理解。它有模拟RF能量流进/流出的两根天线和一个USB连接器，其中数字数据也可以流入/流出主机系统。然而，Pluto能做的不仅仅是RF至比特流。

RF至比特流多年来一直是一项艰巨的任务，其中许多问题已得到解决。从纯粹的模拟问题（和解决方案）开始，人们已经研究了很长时间，去了解人们在这类问题上付出了多少时间和精力是件很有趣的事情。
* James Clerk Maxwell 在1873年出版了《电磁学通论》。
* Heinrich Rudolf Hertz 发送和接收了EM波，并在1887和1890年发表了相关论文。[^1]
* Guglielmo Marconi 在1895年夏天研制出第一台长距离无线电通信装置，发送的无线电信号跨越了山传播到2英里（3.2公里）开外。
* 1900年12月，Reginald A. Fessenden 成为了第一个通过电磁波发送音频（无线电话）的人，传输距离超过了1.6公里。1906年的圣诞节平安夜，他成为第一个发明公共无线电广播的人。
* Edwin Armstrong 在1918年第一次世界大战期间开发了超音速异位接收器，在1928年至1933年间发明了宽带频率调制。

![](https://wiki.analog.com/lib/exe/fetch.php?w=300&tok=133229&media=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fc%2Fce%2FPrototype_Armstrong_superheterodyne_receiver_1920.jpg)

* 英国研究人员试图解决一些超级难题，并于1932年发展出同步检波法。该设计后来被重命名为同步（synchrodyne），现在有时被称作直接转换或zero-IF。

近百年来，无线电设计和结构并没有太大的改变。虽然许多设计师和工程师在器件（从电子管到晶体管再到集成电路）和实现（屏蔽、降噪等）方面有了巨大的改进，但工程师们使用的基本结构依旧是最经典的结构。[^2]


![](https://wiki.analog.com/_media/university/tools/pluto/users/pluto_medium_block_diagram.png?w=200&tok=c0ba78)

ADALM-PLUTO 内的无线电芯片 AD9363，是一款基于直接转换接收器的高性能、高集成度的RF敏捷收发器，
* 接收子系统包括低噪声放大器 （LNA）、直接转换混频器、可配置模拟滤波器、高速模数转换器 （ADC）、数字抽取滤波器和 128-tap 有限脉冲响应 （FIR） 滤波器，可以适当的采样率产生12位输出信号。接收链通过可配置的自动增益控制 （AGC） 或手动增益模式、直流偏置校正、正交校正进行扩大。接收的 I 和 Q 信号传递到数字基带处理器中，在本例中为 Xilinx Zynq SoC。
* 传输子系统还使用直接转换结构。从基带处理器（在本例中同样为 Xilinx Zynq SoC）中接收12位I/Q样本，通过 128-tap 有限脉冲响应 （FIR） 滤波器、数字插值滤波器、高速数模转换器 （DAC）、模拟滤波器、直接转换混频器和小功率放大器（PA）向天线输出。
* AD9363 内集成的相锁环 （PLL） 为接收和传输通道提供时钟和本地振荡器，并为 ADC、DAC 提供时钟和采样频率。

Xilinx Zynq 全部可编程 soc（AP SoC）融入了基于 ARM 处理器的可编程性和 FPGA 硬件可编程性，该器件采用单核ARM Cortex™-A9处理器，与28nm Artix®-7基本可编程逻辑配合。配备常用的硬件外设（USB、SPI 等）。


**[返回终端用户指南主页](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-for-End-User/)**


[^1]: 
>令人吃惊的是，Hertz 认为这些结果没有多少实用价值。

[^2]:
>根据国家史迹名录，一座建筑至少得有50年才能被称为历史性的建筑，所以我认为这是一个很好的形容技术发明的词语。