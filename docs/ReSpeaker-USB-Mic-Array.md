---
name: ReSpeaker USB Mic Array
category: ReSpeaker
bzurl:
oldwikiname: ReSpeaker USB Mic Array
prodimagename:
surveyurl:
sku: 107990193
---

![](https://github.com/SeeedDocument/ReSpeaker-USB-Mics/raw/master/img/Bazaar/ReSpeaker-USB-Mics-box-preview.jpg)


在过去的一年中，[Respeaker Mic Array V2.0](https://www.seeedstudio.com/ReSpeaker-Mic-Array-v2-0.html) 以开发板的形式出售，销售量超过1万个。客户不断要求带有外壳的完整设备，考虑到声学原理，这对我们的设计提出了挑战。
  
所以Seeed提供了ReSpeaker USB Mic Array这一新的解决方案：

- 具有精心设计的声学结构的开箱即用设备为客户提供了灵活的内置解决方案。
- 提供注模外壳，节省了上市时间和模具成本。

ReSpeaker USB麦克风阵列和Respeaker麦克风阵列V2.0内部的PCBA之间的区别：

- 优化的电源电路
- 将音频插孔和微型USB端口移到背面。


<p style=":center"><a href="https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17798475675.21.79975d19vgzJba&id=604623587054" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>





## 功能

- 远场语音捕获
- 支持USB Audio Class 1.0（UAC 1.0）
- 四个麦克风阵列
- 12个可编程RGB LED指示灯
- 语音算法和功能
    - 语音活动检测
    - 方向检测
    - 波束成形
    - 噪声抑制
    - 去混响
    - 回声消除

## Specification

- XMOS的XVF-3000
- 4个高性能数字麦克风
- 支持远场语音捕获
- 片上语音算法
- 12个可编程RGB LED指示灯
- 麦克风： ST MP34DT01TR-M  
- 灵敏度：-26 dBFS (全向)  
- 声学过载点：120 dBSPL  
- 信噪比： 61 dB  
- 电源： 5V DC from Micro USB
- 尺寸： 70mm (Diameter)  
- 3.5毫米音频插孔输出插座
- 功耗：5V，LED导通时180mA，LED导通时170mA
- 最大采样率：48Khz

## 硬件概述¶

![](https://github.com/SeeedDocument/ReSpeaker-Mic-Array-v2.1/raw/master/img/hardware_overview.jpg)

- <font face="" size=3 font color="ff0000">①</font> **XMOS XVF-3000:**
 它集成先进的DSP算法包括声学回声消除（AEC），波束成形，去混响，噪声抑制和增益控制。

- <font face="" size=3 font color="ff0000">②</font> **Digital Microphone:**
 MP34DT01-M是一款超紧凑，低功耗，全向的数字MEMS麦克风，内置有电容式感应元件和IC接口。

- <font face="" size=3 font color="ff0000">③</font> **RGB LED:**
 三色RGB LED。

- <font face="" size=3 font color="ff0000">④</font> **USB端口:**
提供电源并控制麦克风阵列

- <font face="" size=3 font color="ff0000">⑤</font> **3.5mm毫米耳机插孔:**
输出音频，我们可以将有源扬声器或耳机插入此端口。

- <font face="" size=3 font color="ff0000">⑥</font> **WM8960:**
该WM8960是一个低功率的立体声编解码器设有d类扬声器驱动器

**系统图**
![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/img/system_diag.png)



## 应用

- USB语音捕获
- 智能音箱
- 智能语音助手系统
- 录音机
- 语音会议系统
- 会议通讯设备
- 语音互动机器人
- 汽车语音助手
- 其他语音接口方案

## 入门

!!!Note

    ReSpeaker USB麦克风阵列可与Windows，Mac，Linux系统和Riod兼容。以下脚本已在Python2.7上进行了测试。


### 更新固件

这是差异表。

| 固件名称                             | 通道数 | 备注                                                                                          |
|------------------------------------|----------|-----------------------------------------------------------------------------------------------|
| 1_channel_firmware.bin             | 1        | 为ASR处理的音频                                                                    |
| 1_channel_firmware_6.02dB.bin      | 1        | 与1_channel_firmware.bin相同，但是4个麦克风的增益为6.02dB                        |
| 1_channel_firmware_12.06dB.bin     | 1        | 与1_channel_firmware.bin相同，但是4个麦克风的增益为12.04dB                    |
| 48k_1_channels_firmware.bin        | 1        | 48k采样率，1个输入通道                                                           |
| 48k_1_channel_firmware_6.02dB.bin  | 1        | 48k采样率，1个输入通道，但4个麦克风的增益为6.02dB                       |
| 6_channels_firmware.bin            | 6        | 通道0：为ASR处理的音频，通道1-4：4个麦克风的原始数据，通道5：回放（出厂固件） |
| 6_channels_firmware_6.02dB.bin     | 6        | 与6_channels_firmware.bin相同，但是4个麦克风的增益为6.02dB                        |
| 6_channels_firmware_12.04dB.bin    | 6        | 与6_channels_firmware.bin相同，但是4个麦克风的增益为12.04dB                        |
| 48k_6_channels_firmware.bin        | 6        | 48k采样率，6个输入通道                                                      |
| 48k_6_channels_firmware_6.02dB.bin | 6        | 	48k采样率，6个输入通道，6.02dB增益                                             |


**For Linux:**  Mic阵列支持USB DFU。我们开发了python脚本dfu.py通过USB更新固件。
```python
sudo apt-get update
sudo pip install pyusb click
git clone https://github.com/respeaker/usb_4_mic_array.git
cd usb_4_mic_array
sudo python dfu.py --download 6_channels_firmware.bin  # The 6 channels version 

# if you want to use 1 channel,then the command should be like:

sudo python dfu.py --download 1_channel_firmware.bin

```
下载成功后，会显示下图的内容

![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/img/Download_firmware.png)

**For Windows/Mac:** 我们不建议您使用Windows / Mac和Linux虚拟机来更新固件。

### 开箱即用的演示

这是带有6通道固件的回音消除示例。

- 步骤1.将USB电缆连接到PC，将音频插孔连接到扬声器。

![](https://github.com/SeeedDocument/ReSpeaker-USB-Mics/raw/master/img/Bazaar/_DAS5930.jpg)

- 步骤2.在PC端选择*mic array v2.1*作为输出设备。
- 步骤3.开始大胆录制。
- 步骤4.首先在PC端播放音乐，然后我们进行交谈。
- 步骤5.我们将看到如下所示的Audacity屏幕，请单击Solo收听每个频道的音频。

![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/img/Audacity.png)

Channel0音频（由算法处理）：

<audio controls="controls">
  <source type="audio/wav" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel0_asr.wav"></source>
  <source type="audio/ogg" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel0_asr.ogg"></source>
</audio>

Channel1音频（Mic1原始数据）：

<audio controls="controls">
  <source type="audio/wav" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel1_raw.wav"></source>
  <source type="audio/ogg" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel1_raw.ogg"></source>
</audio>

Channel5音频（播放数据）：

<audio controls="controls">
  <source type="audio/wav" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel5_playback.wav"></source>
  <source type="audio/ogg" src="https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/channel5_playback.ogg"></source>
</audio>

其他的内容参考[ReSpeaker_Mic_Array_v2.0](http://wiki.seeedstudio.com/cn/ReSpeaker_Mic_Array_v2.0/)

## Resource
- **[PDF]** [ReSpeaker USB Mic Array Dimension](https://github.com/SeeedDocument/ReSpeaker-USB-Mics/raw/master/res/dimension.pdf)
- **[DWG]** [ReSpeaker USB Mic Array Case 3D Model](https://github.com/SeeedDocument/ReSpeaker-USB-Mics/raw/master/res/case.dwg)
- **[PDF]** [XVF3000 Product Brief](https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/XVF3000-3100-product-brief_1.4.pdf)
- **[PDF]** [XVF3000 Datasheet](https://github.com/SeeedDocument/ReSpeaker_Mic_Array_V2/raw/master/res/XVF3000-3100-TQ128-Datasheet_1.0.pdf)
- **[WIKI]**[ReSpeaker_Mic_Array_v2.0 WIKI ](http://wiki.seeedstudio.com/cn/ReSpeaker_Mic_Array_v2.0/)


## Tech Support
Please submit any technical issue into our [forum](http://forum.seeedstudio.com/).
<br /><p style="text-align:center"><a href="https://www.seeedstudio.com/act-4.html?utm_source=wiki&utm_medium=wikibanner&utm_campaign=newproducts" target="_blank"><img src="https://github.com/SeeedDocument/Wiki_Banner/raw/master/new_product.jpg" /></a></p>