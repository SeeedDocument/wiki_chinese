---
name: Respeaker Introduction
nointro:
---
# ReSpeaker选型指南
!!! Note
    该网站还在持续建设中

ReSpeaker系列通过硬件组件和软件库来构建支持语音的驱动，简要处理流程如下图：
![](https://raw.githubusercontent.com/respeaker/respeaker.github.io/mkdocs/docs/assets/images/vui.png)

## 硬件

硬件组件包括基于树莓派的I2S麦克风阵列( 2 Mic Array for Pi , 4 Mic Array for Pi , 4 Linear Mic Array for Pi , 6 Mic Array for Pi )，通过USB与 Linux/Windows/macOS 操作系统通信的USB麦克风阵列( ReSpeaker Mic Array,ReSpeaker Mic Array v2 ),以及可自主运行的麦克风阵列开发板( ReSpeaker Core , ReSpeaker Core v2 ).
### 麦克风阵列

|              | 2 Mic Array for Pi | 4 Mic Array for Pi | 4 Linear Mic Array for Pi | 6 Mic Array for Pi | ReSpeaker Mic Array       | ReSpeaker Mic Array v2    |
|:------------:|:------------------:|:------------------:|:-------------------------:|:------------------:|:-------------------------:|:-------------------------:|
||![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/2mics-zero-high-res.jpg?raw=true)|![](https://github.com/SeeedDocument/ReSpeaker-4-Mic-Array-for-Raspberry-Pi/blob/master/img/overview.jpg?raw=true)|![enter image description here](https://github.com/SeeedDocument/ReSpeaker_4-Mics_Linear_Array_Kit/raw/master/img/main_wiki.jpg)|![enter image description here](https://github.com/SeeedDocument/ReSpeaker_6-Mics_Circular_Array_kit_for_Raspberry_Pi/raw/master/img/IMG_6051.jpg)|![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/respeaker_mic_array.jpeg)|![](https://raw.githubusercontent.com/SeeedDocument/ReSpeaker_cn/master/img/ReSpeaker_Mic_Array_v2.png)|
|  麦克风数量   |          2         |          4         |             4             |          6         | 7                         | 4                         |
|     形状     |       线形       |       正方形       |           线形          |       正六边形      | 圆形                  | 圆形                  |
|   接口       |         I2S        |         I2S        |            I2S            |         I2S        | USB                       | USB                       |
|  音频输出     |       Stereo       |         NA         |           Stereo          |       Stereo       | Mono                      | Mono                      |
|   信噪比      |       NA           |         NA         |   59dB                   |59dB                 |       61dB                |           61 dB           |
|   拾音距离    |         3m         |         3m         |          3m              |         3m          |             3m            |           5m              |
|声音处理算法   |   开源软件算法       |  开源软件算法      |          开源软件算法      |  开源软件算法        | 内置闭源硬件算法           | 内置闭源硬件算法            |
|  声源定位    |    不支持            |  支持             |       不支持               |        支持         |      支持                 |         支持               |
|  语音回环    |         NA          |       NA           |             2通道         |         2通道       |           NA              |          2通道            |
|  使用方法    |   需要二次开发       |  需要二次开发       |       需要二次开发        |        需要二次开发   |      即插即用             |         即插即用           |

如果你需要自定义形状而且需求量大于5000片的话，你可以点击这个页面[Seeed's Fusion service](https://www.seeedstudio.com/fusion.html)去简单的完成定制。
!!! Note
    ReSpeaker Mic Array和ReSpeaker Mic Array v2 只是做声卡作用不能像麦克风阵列开发板单独使用
### 麦克风阵列开发板

|             | ReSpeaker Core v1 (MT7688)  | ReSpeaker Core v2 (RK3229)                    | 
|:-------------:|:-----------------------------:|:-----------------------------------------------:|
||![](https://raw.githubusercontent.com/SeeedDocument/ReSpeaker_cn/master/img/ReSpeaker_Core_v1.png)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/ReSpeaker_cn/master/img/ReSpeaker_Core_v2.png)|
| CPU         | MT7688 (MIPS24KEc, 580 MHz) | RK3229 (4 ARM Cortex A7 cores, 1.5GHz)        |
| RAM         | 256 MB                      | 1 GB                                          |
| 形状      | 圆形                    | 正六边形                                      |
| 通信接口  | WiFi, USB             | WiFi, Bluetooth, Ethernet, HDMI, USB otg/host |
| 语音回环   | NA                     | 2 通道                                   |
|   拾音距离    |         3m         |          5m         |
| 声音处理算法  |   开源软件算法         |  闭源软件算法                           |
|  使用方法    |   需要二次开发       |  需要二次开发       |

## 软件

声音处理算法包括,语音活动检测( VAD ) , 波达方向( DOA ) , 波束成形( Beamforming ) , 噪声抑制( NS ) , 声学回声消除( AEC ) 和关键词检测 ( KWS ) .声音处理算法流程如下：
![](https://raw.githubusercontent.com/respeaker/respeaker.github.io/mkdocs/docs/assets/images/mic_array.png)


## 产品清单
---
如果你想了解某款产品更详细的信息你可以在Seeed WiKi中找到，该列表将不断更新。

* [Application_Dueros]()
* [Respeaker_2-Mics_Pi_HAT](https://wiki.seeedstudio.com/cn/Respeaker_2-Mics_Pi_HAT)
* [Respeaker_4-Mics_Pi_HAT](https://wiki.seeedstudio.com/cn/Respeaker_4-Mics_Pi_HAT)
* [ReSpeaker_4-Mic_Linear_Array_Kit_for_Raspberry_Pi](https://wiki.seeedstudio.com/cn/ReSpeaker_4-Mic_Linear_Array_Kit_for_Raspberry_Pi)
* [ReSpeaker_6-Mic_Circular_Array_kit_for_Raspberry_Pi](https://wiki.seeedstudio.com/cn/ReSpeaker_6-Mic_Circular_Array_kit_for_Raspberry_Pi)
* [Respeaker_Core](http://wiki.seeedstudio.com/cn/Respeaker_Core/)
* [Respeaker_Mic_Array](http://wiki.seeedstudio.com/cn/Respeaker_Mic_Array/)
* [ReSpeaker_Mic_Array_v2.0](http://wiki.seeedstudio.com/cn/ReSpeaker_Mic_Array_v2.0/)
* [SoundPi](http://wiki.seeedstudio.com/cn/SoundPi)
* [ReSpeaker_Core_v2.0](http://wiki.seeedstudio.com/cn/ReSpeaker_Core_v2.0/)
