---
title: Grove - Q Touch Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Q-Touch-Sensor-p-1854.html
oldwikiname: Grove_-_Q_Touch_Sensor
prodimagename: Grove-Q_Touch_Sensor.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/Grove-Q Touch Sensor.jpg
surveyurl: https://www.research.net/r/Grove-Q_Touch_Sensor
sku: 101020069
tags: grove_i2c, io_3v3, io_5v, plat_duino
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Grove-Q_Touch_Sensor.jpg)

Grove-Q Touch Sensor 是高灵敏度和高抗噪声触摸输入设备。 它基于 Atmel AT42QT1070 芯片通过扩频的方式调制处理信号，能够抑制外部噪声的影响，并抑制 RF 信号的发射。 QT1070 采用双脉冲采集信号的方式。 这给它提供了更强的抗噪声的能力，并且能够使用单个引脚接收触摸感应信号，减少了对外部采样电容的需求，。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.20452441MTlQfA&id=45475599815)

规格参数
--------------

- 工作电压：3〜5.5V
- 工作电流在 3.3V时：1mA
- 7键触摸：key0，key1，key2位于 Grove PCB 底部
- 通讯协议：I2C
- I2C地址：0x1B

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

支持平台
-------------------

硬件概述
------------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Grove-Q_Touch.png)

① - 板上触摸键0

② - 板上触摸键1

③ - 板上触摸键2

④ - 触摸键 key0〜key6 开发

- 主要电容 Cx 的推荐范围为1 pF - 30 pF。 较大的 Cx 值会降低灵敏度。

⑤ - GND

⑥ - Grove 界面

用法
-----

演示：谁触动我的荔枝？

你有没有听说过荔枝？ 是的，这是中国南方非常有名的水果。 如果你曾尝过，会爱上它。

现在让我们开始我们的演示。 当您碰触击盘（荔枝）时， LED 将会亮起。

### 硬件连接

1. 将 Grove-Q Touch Sensor 的 **I2C** 连接到 Grove Base Shield 上的 **I2C** 端口。
2. 将 Grove-LED 连接到 Grove Base Shield 上的 **D3** （数字引脚 3 ）。
3. 将 Grove-Q Touch 传感器上的 **Key0** （标记为 K0 ）连接到荔枝（或者，您可以在测试时用手指触摸连接线的开口端）。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Grove-Q_Touch_Demo1.JPG)

### 软件部分

1. 下载 [Q Touch 库](https://github.com/Seeed-Studio/Seeed_QTouch).
2. 将其解压到 Arduino IDE 的库文件夹中，例如路径可以是.. \ arduino-1.0.5 \ libraries。

#### **例一**

a. 通过 Arduino 菜单 **“File（文件） - >exsample（示例） - > Seeed_QTouch-master - > Grove_QTouch_demoCode_v_1_0”**  打开示例。

b. 上传代码 请注意，您应该选择正确的电路板类型和 COM 端口。

C. 触摸荔枝时， LED 会发光，如下图所示。


![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Grove-Q_Touch_Demo2.JPG)

#### **例二**

a. 通过 Arduino 菜单 **“File（文件） - >exsample（示例）- > Seeed_QTouch-master - > isTouch”**  打开示例。

b. 上传代码

c. 打开串行监视器。

d. 触摸荔枝后放开; 串行监视器将显示触摸的持续时间，如下面的屏幕截图所示

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Screenshot--QTouch.png)

您也可以尝试下面的[Codebender](http://www.codebender.cc)小部件来上传代码。

<iframe frameborder="0" height="510" src="https://codebender.cc/embed/example/Seeed_QTouch/isTouch" width="800"></iframe>

请打开下面的串行监视器查看数据。

<iframe frameborder="0" height="300" src="https://codebender.cc/embed/serialmonitor" width="800"></iframe>

#### **例三**

a. 通过 Arduino 菜单“文件 - >示例 - > Seeed_QTouch-master - > getTouchNumber” 打开示例。

b. 上传代码

c. 打开串行监视器。

d. 触摸荔枝时，串行监视器将显示已连接的密钥，如下面的截图所示。 可以将水果连接到任何其他键并进行验证。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/img/Screenshot--getTouchNumber.png)

您也可以尝试下面的[Codebender](http://www.codebender.cc)小部件来上传代码。
<iframe frameborder="0" height="510" src="https://codebender.cc/embed/example/Seeed_QTouch/getTouchNumber" width="80%"></iframe>

请打开下面的串行监视器查看数据。

<iframe frameborder="0" height="300" src="https://codebender.cc/embed/serialmonitor" width="100%"></iframe>

资源下载
--------

-   [Q Touch Library](https://github.com/Seeed-Studio/Seeed_QTouch)
-   [Schematic pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/res/Grove-Q_Touch_Sensor_v1.0.pdf)
-   [Eagle file](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/res/Grove_Q－Touch_Sensor_v1.0_sch_pcb.zip)
-   [AT42QT107 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Q_Touch_Sensor/master/res/AT42QT1070-MMH.pdf)
-   [How to detect finger touch?](/How_to_detect_finger_touch?)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Q_Touch_Sensor -->
