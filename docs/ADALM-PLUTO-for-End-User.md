---
name: ADALM-PLUTO 终端用户指南
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 114991964
tags:
---


Pluto所有用户请务必仔细阅读以下内容。它们将会演示如何通过USB，以及MATLAB、simulink、GNU Radio、自定义C、C++、C#或Python代码在X86主机或嵌入式平台（树莓派、Beaglebone、96boards等）上实现与RF信号的交互。大量实例证明，MATLAB和simulink可以为无线电的释放提供有利的环境和路径（您可以很轻易地将您的算法嵌入到定制产品中）。


## 目录

### 一、[硬件介绍](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-Introduction)

- [名称来源 PlutoSDR?](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-Name)
- [内部结构](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-Understanding)
- [有效距离和传播速度](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-far-fast)
    - [RF输出](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-Transmit)
        - [1.相位噪声和精度](https://wiki.analog.com/university/tools/pluto/users/phase_noise)
    - [RF输入](https://wiki.analog.com/university/tools/pluto/users/receive)
        - [1.接收灵敏度](https://wiki.analog.com/university/tools/pluto/users/receiver_sensitivity)
        - [2.非正交信号的处理](https://wiki.analog.com/university/tools/pluto/users/non_quad)
    - [天线](https://wiki.analog.com/university/tools/pluto/users/antennas)


### [二、快速开始](https://wiki.analog.com/university/tools/pluto/users/quick_start)


### 三、软件介绍及设备驱动安装

- [Windows 驱动](https://wiki.analog.com/university/tools/pluto/drivers/windows)
- [Linux 驱动](https://wiki.analog.com/university/tools/pluto/drivers/linux)
- [MAC 驱动](https://wiki.analog.com/university/tools/pluto/drivers/osx)


### 四、[更新 ADALM-PLUTO 固件](https://wiki.analog.com/university/tools/pluto/users/firmware)

### 五、[校准ADALM-PLUTO](https://wiki.analog.com/university/tools/pluto/users/calibration)

### 六、[自定义ADALM-PLUTO](https://wiki.analog.com/university/tools/pluto/users/customizing)

### 七、正确加载和配置驱动程序之后，通过以下方式与 ADALM-PLUTO主动学习模块交互

- [IIO示波器](https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope)
- [gqrx](http://gqrx.dk/) -- 一个由GNU Radio提供的开源软件定义无线电接收机。
- [MATLAB和simulink的官方支持和帮助](https://www.mathworks.com/hardware-support/adalm-pluto-radio.html)
- [MATLAB IIO 汇总](https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink)
- [GNU Radio](https://wiki.analog.com/resources/tools-software/linux-software/gnuradio)
- [SDRangel](https://github.com/f4exb/sdrangel) -- 一个开源的Qt5 / OpenGL 3.0+ SDR和硬件前端信号分析仪
- [SDR#](https://airspy.com/download/)（SDRsharp的PlutoSDR前端可在此查询：[sdrsharp-plutosdr](https://github.com/Manawyrm/sdrsharp-plutosdr)）
- [SoapySDR](https://github.com/pothosware/SoapySDR)（PlutoSDR的Soapy SDR插件可在此查询：[SoapyPlutoSDR](https://github.com/jocover/SoapyPlutoSDR)）
- [通过将Python绑定到IIO库获取和控制PlutoSDR硬件](https://github.com/radiosd/PlutoSdr)
- [Python接口](https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio)
