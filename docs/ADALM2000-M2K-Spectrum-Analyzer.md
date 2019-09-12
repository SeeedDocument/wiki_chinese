---
name: ADALM2000 M2K Spectrum Analyzer(频谱分析仪)
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 简介

频谱仪可以捕获频域信号（即信号为频率的函数），M2K的频谱仪的探头1和探头2能够测量±20V内的信号。


要切换到此仪器，单击左侧菜单中的 **Spectrum Analyzer**。


!!!Note
        Scopy连接到M2K设备时，示波器会自动校准。


-----

## 频谱仪前面板


![](https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_front-panel.png)




- **1、Spectrum Analyzer Tab - 频谱分析仪选项卡：**  
点击此选项显示频谱仪界面。白色小方块允许用户在其他仪器选项卡打开时运行/停止频谱分析仪。


- **2、Signal Plot - 信号波形：**  
显示频域信号。X轴表示频率，Y轴表示振幅（单位为dBFS）。  
 
- **3、Channel Controls - 通道控制：**  
单击橙色或紫色按钮启用/禁用通道，单击频道右侧的按钮将打开通道设置。  

 
- **4、Sweep - 扫描：**  
单击Sweep按钮进入扫描设置，用户可以修改信号图行窗口显示。 

- **5、Markers - 标记：**  
单击标记按钮显示标记控件。 
 
- **6、Run/Stop and Single Run - 运行/停止和单步运行：**  
单击Run按钮控制频谱分析仪连续捕获数据。单击Single按钮控制频谱分析仪捕获单次数据 
 
- **7、Instrument Settings - 仪器设置：**  
单击以进入仪器设置面板。 
 
- **8、Last opened panel - 上次打开的面板：**  
单击此按钮将显示上次打开的面板。


------

## 通道设置



<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_channel-settings.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_channel-settings.png"  />
  </a>
</figure>
</div>


通道设置中用户可以为待分析的信号设置所需的计算或变化。这里设置合适的FFT计算和需要使用的平均类型。 

- **1、Channel menu button - 通道菜单按钮：**  
此按钮将打开通道1或2的通道设置。

- **2、Type - 类型：**  
下拉菜单中类型选项是频谱仪中可用的几种平均值类型，有助于提高测量的准确性和可重复性。下面是几种类型总览。

- **3、Window - 窗口：**  
确定要使用的FFT计算的类型。

- **4、Averaging - 平均值：**  
设置1-100之间的任意均值。


下面列举几条基于输入信号的窗函数的简单建议：

信号 |	窗函数
---|----
正弦波或正弦波的叠加|	Hann 汉宁窗
高精度幅值正弦波 |	Flat top 
窄带随机信号（振动特性）|	Hann (汉宁窗)
未知信号 |	Hann (汉宁窗)



关于窗口函数的说明[^1]




关于平均值类型的说明[^2]



------


## 仪器设置

![](https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_instrument-settings.png)


仪器设置包含导出数据按钮。


-------


## 扫描设置


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_sweep-settings.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_sweep-settings.png"  />
  </a>
</figure>
</div>


扫描菜单允许用户根据待分析频率在频谱仪的信号图窗口中进行更改，做出的更改都将应用于两个通道。


- 1、扫描菜单按钮：打开扫描设置。
- 2、启动和停止频率：设置范围在0Hz到50MHz之间的待分析的启动和停止频率。
- 3、中心频率：设置要分析的中心频率。
- 4、跨度：设置待分析频谱跨度，范围为0 Hz至50 MHz。
- 5、振幅最值：设置待分析振幅最大值。
- 6、振幅变化：设置要分析的幅度范围。
- 7、单位：将幅度单位设置为_ dBFS，dBu，dBV，Vpeak和Vrms _。
- 8、分辨率带宽：设置两个频谱点之间的频率差。


-------


## 标记


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_markers.png?cache=" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy/sa_markers.png"  />
  </a>
</figure>
</div>


标记功能允许用户测量特定频率的幅度，用户可以在每个通道上有多个标记，使用非常灵活，可以快速进行频谱测量。


- **1、Marker Settings - 标记设置：**  
此按钮相关显示标记设置。

- **2、Marker Enable button - 标记启用按钮：**  
启用/禁用标记按钮。当方框填充颜色时，标记打开。Scopy允许同时打开5个标记。

- **3、Marker Control - 标记控制**：  
允许用户在指定的频率位置移动标记。

- **4、Automatic Marker Control - 自动标记控制：**  
根据功能自动放置标记：
    - Peak - 峰值：标记图上的最高峰值。
    - ← Peak / → peak - ←峰值/→峰值：将标记移动到信号中的左/右峰值处。
    - Dn Ampl：将标记移动到信号中幅值第二低的位置。
    - Up Ampl：将标记移动到信号中幅值第二高的位置。

- **5、Marker Table - 标记表：**  
该功能启用标记表以更好地查看频谱频率。标记表使用户能够识别每个通道上的标记位置，尤其是当两个通道都处于激活状态时。它列出了标记号，当前测量的通道，频率，幅度和标记类型。



<div class="tips" style="display: table; table-layout: fixed; background-color: #e3efff; height: auto; width: 100%; ">
<div class="left-icon" style="display: table-cell; vertical-align: middle; background-color: #a3c7ff; padding-top: 10px; box-sizing: border-box; height: auto; width: 38px; text-align: center;"><img style="width: 26px; vertical-align: middle;" src="https://s3-us-west-2.amazonaws.com/static.seeed.cc/seeed/icon/Note.svg" alt="attention icon" /></div>
<div class="right-desc" style="display: table-cell; vertical-align: middle; padding-left: 15px; box-sizing: border-box; width: calc(95% - 38px);">
<p style="font-weight: bold; margin-top: 10px;">Note</p>
<p style="font-size: 14px;">对于其他标记控制。可以通过在信号图窗口上拖动来移动每个标记。</p>
</div>
</div>



**返回 [Scopy](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Scopy) 主页**



[^1]:  
> **Hanning:** The most commonly used window. It has an amplitude variation about 1.5dB for signals between bins and provides reasonable selectivity. Its filter roll off is not particularly steep. Hanning windows can limit the performance of the analyzer when looking at signals close together in frequency with very different amplitude.  
> **Flattop:** The Flattop window improves on the amplitude accuracy of the Hanning window. Its between-bin amplitude variation is about 0.02 dB. However, the selectivity is a little worse. Unlike the Hanning, the Flattop window has a wide pass band and very steep rolloff on either side. Thus, signals appear wide but do not leak across the whole spectrum.  
> **Blackman-Harris:** The Blackman-Harris window is a very good window to use with FFT analyzers. It has better amplitude accuracy than the Hanning, very good selectivity, and the fastest filter rolloff. The filter is steep and narrow and reaches a lower attenuation than the other windows. This allows signals close together in frequency to be distinguished, even when their amplitudes are very different.  
> **Kaiser:** The Kaiser window, combines excellent selectivity and reasonable accuracy. The Kaiser window has the lowest side-lobes and the least broadening for non-bin frequencies. Because of these properties, it is the best window to use for measurements requiring a large dynamic range.


[^2]:
> **RMS Averaging:** Reduces fluctuations in the data but does not reduce the actual noise floor. With a sufficient number of averages, a very good approximation of the actual random noise floor can be displayed. RMS averaging involves magnitudes only and has no phase information.  
- RMS Linear Averaging: n samples all added together then divided by n.  
- RMS Exponential Averaging: 1/nth of current magnitude, added together with n-1 of previous magnitude.  
> **Peak hold:** The new spectral magnitudes are compared to the previous data, and if the new data is larger, the new data is stored. The resulting display shows the peak magnitudes which occurred in the previous group of spectra.  
> **Peak hold continuous:** Similar with the peak and hold averaging except it looks at the number of instantaneous spectra recorded until measurement is restarted.  
> **Min hold:** The new spectral magnitudes are compared to the previous data, and if the new data is lower, the new data is stored. The resulting display shows the peak magnitudes which occurred in the previous group of spectra.






























