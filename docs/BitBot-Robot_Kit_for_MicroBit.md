---
title: BitBot-Robot Kit for MicroBit
category: Kit
bzurl: https://www.seeedstudio.com/Robot-Kit-for-Micro%3ABit-p-3015.html
oldwikiname:
prodimagename: BitBot-Robot_Kit_for_MicroBit.jpg
wikiurl: http://seeed.wiki/BitBot-Robot_Kit_for_MicroBit
sku: 114991414
---


Bit:Bot – BBC Micro:Bit 集成机器人

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Bitbot1.jpg)

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.6fe1e7d2SkbR2o&id=562940397428)
---------------------------

无论老少都被这款基于 BBC Micro:Bit 的机器人吸引，而且更令人惊叹的是它支持所有语言。图形化编程和文本编程的语言都支持 Bit:Bot。

您还可以使用 Micro:Bit 的无线电或蓝牙功能发送和接收命令和数据。[点击查看蓝牙教程](https://ukbaz.github.io/howto/bitbotRemoteControl.html)

!!!Tip
    现在有一个用于 Bit:Bot 的 Microsoft PXT 软件包 (在此向 Sten Roger Sandvik 表示感谢，他的 Twitter 是 @stenrs)。点击 Advanced tab 或 Tools gear 图标，然后选择 Add Package，然后搜索 BitBot。

!!!Warning
    寻线传感器与按钮共用引脚。当 Micro:Bit 启动或重置时，它将检查这 2 个按钮的状态，如果两个按钮都被按下则开始配对，这和您使用的语言有关。在 Bit:Bot 上，这种情况转化为两个寻线传感器接收到反馈。您可以在开机前释放按钮，避免上述情况的出现。


## 产品特性
---

- 2 个微型金属齿轮马达。无论是速度 (0 至 100%) 还是方向 (正向或反向)，均可完全由软件控制。
- 橡胶轮胎的车轮能提供最大抓地力
- 平滑的金属球前轮
- 12 个迷你 neopixel 以 2 列围绕在车身左右。可以设置任何灯为任意颜色，在 Bit:Bot 移动时产生酷炫的照明效果
- 2 个数字寻线传感器。
- 2 个模拟光传感器 (左前方和右前方)，因此您的 Bit:Bot 可以被编程为跟随光源 (如火炬)，或者您可以通过编程，使它去隐藏在它可以找到的最黑的地方
- 蜂鸣器，所以您可以随时发出哔哔声
- 由集成的带有开关和蓝色 LED 指示灯的 3xAA 电池座供电
- 通过金手指轻松插入取出 BBC micro:bit
- 额外 neopixel 扩展端口 (如 McRoboFace)
- 在车前的用于附加传感器的扩展连接 (在开发中)

## 硬件组装
---
**步骤 0** : 检查以下零部件

- 1 个前轮组件 (金属球或塑料球)
- 2 x 6mm M2 圆头螺钉
- 2 x M2 螺母
- 2 x 12mm 铜柱
- 4 x 8mm M2.5 沉头螺钉

1.使用 M2 6mm 圆头螺钉和螺母固定前脚轮壳体，然后将脚轮球装入壳体

2.使用 M2 6mm 圆头螺钉和 M2.5 8mm 沉头螺钉将电池组安装到 2 个金属支柱上，**确保开关位于 Bit:Bot 的后部**

3.使车轮的光滑面向外。轴应与车轮外侧齐平，不能突出 (或内侧可卡住电机外壳)

4.把您的 BBC Micro:Bit 插入金手指插槽。

**步骤 1** - 安装前轮

使用 M2 6mm 圆头螺钉和螺母固定前脚轮壳体，然后将金属球装入壳体

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step1.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step2.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step3.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step4.jpg)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step5.jpg)

**步骤 2** - 安装电池座

使用 M2 6mm 圆头螺钉和 M2.5 8mm 沉头螺钉将电池组安装到 2 个金属支柱上 : 确保开关位于 Bit:Bot 的后部

此时您应该有 4 个螺钉。 可以是 4 x 8mm 的沉头螺钉，也可以是 2 x 6mm 的圆头螺钉和2 x 8mm 的沉头螺钉。

如果您有 6mm 的圆头螺钉，请使用这些螺钉将 12mm 的铜柱安装到 Bit:Bot 的主板上。

一定使用 8mm 沉头螺钉将电池座安装到铜柱上。

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step6.jpg)

使用 6mm 的圆头螺钉或 8mm 的沉头螺钉将 12mm 的铜柱安装到主板 (如上图所示)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step7.jpg)

使用 8mm 的沉头螺钉将电池座安装到铜柱上。

**步骤 3** - 安装车轮

使车轮的光滑面向外。轴应与车轮外侧齐平，不能突出 (或内侧可卡住电机外壳)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step8.jpg)

移动车轮，使车轴与车轮外侧齐平

**步骤 4** - 安装 BBC Micro:Bit

把您的 BBC Micro:Bit 插入金手指

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Step9.jpg)

## 硬件概述
---
俯视图

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/bb17a.jpg)

俯视可以看到 neopixel (每个手臂上6个)，2 个光传感器，开关和 LED 指示灯

蜂鸣器位于开关的下方，金手指位于电池座前下方

仰视图

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/bb15a.jpg)

仰视图可以看到 2 个寻线传感器，以及用于 neopixel 扩展和通用扩展连接器的端口。

## 软件部分
---
[Microsoft PXT](https://makecode.microbit.org/) 是最适用于 Bit:Bot 的图形化编程语言，因为它可以与所用的扩展引脚无冲工作，并且完全支持 neopixel。

!!!Tip
    现在有一个用于 Bit:Bot 的 Microsoft PXT 软件包 (在此向 Sten Roger Sandvik 表示感谢，他的 Twitter 是 @stenrs)。转到 Advanced tab 或 Tools gear 图标，然后选择 Add Package，然后搜索 BitBot。

文本编程语言推荐使用 micro-python，笔者更喜欢使用 Mu 编辑器离线使用。相对于图形化编程语言，它提供了一个非常简易的方式来连接到 micro:bit。

!!!Note
    在撰写本文时 (2016 年 12 月)，在 Mu 编辑器中使用 neopixel 等的 PWM 时存在问题，所以最好使用在线 micropython 编辑器。

以下示例使用这两种语言来展示代码片段。

!!!Tip
    示例旨在向人们展示如何使用各种功能。我们不会为您编程 — 授人以鱼不如授人以渔。在下面的例子中，我们将给您提供使用 Bit:Bot 的所有功能的工具，但是师傅领进门，修行靠个人。您需要合理运用以通过代码来实现特定的功能。我们提供了一个完整的寻线示例 — 但它是一个非常基本的算法，您可能会对 T-junctions 和交叉点感到困惑，还有它不使用 neopixel。

下载此页面底部的 Python 示例。在此感谢 Mark Atkinson 提供这些优秀的示例。

### 电机

每个电机有两个引脚。一个控制速度，另一个控制方向。

左电机 : 速度引脚 **0**，方向引脚 **8**

右电机 : 速度引脚 **1**，方向引脚 **12**

!!!Tip
    使电机运转的最简单方法是将速度引脚设置为高电平，将方向引脚设置为低电平 (向前全速移动)

在 Python 环境下，左电机正转 (前进) :

```python
- pin0.write_digital(1)
- pin8.write_digital(0)
```

在 PXT 环境下，左电机正转 (前进) :

!!!Note
    您可以在 **advanced(进阶)** 选项卡的 **pins(引脚)** 下找到输出引脚命令

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download0.png)

为了全速运转电机，如图设置引脚

在 Python 环境下，左电机后退 (反转) :

```python
- pin0.write_digital(0)
- pin8.write_digital(1)
```

在 PXT 环境下，左电机后退 (反转) :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download1.png)

如果我们想改变一个电机的速度，使它不是一直在全速运转，我们需要使用 PWM (脉冲宽度调制)。这是一种改变电机获取功率的方法。PWM 的百分比值决定每个周期输出为 ON 的时间。所以 100% 的百分比和上面示例同效。50% 的百分比意味着电机只有一半时间通电，因此速度会变慢。请注意，电机的实际速度与 PWM 的百分比不一样 – 如果 PWM 值太低，电机根本无法转动，并且在某些值下也会出现一些卡顿现象。不过，能够改变速度使得机器人功能更强劲。例如，可以使寻线器平稳地跟随线路，而不是左右晃动。

要更改引脚的 PWM 值，必须使用 analog_write 命令。可以设置为 0 (始终 off) 至 1023 (始终 on) 之间的值，因此 50% 将为511。以下是如何将右侧电机的速度设置为最大速度的约 75% (值为770) 的例程 :

在 Python 环境下，右电机以最大速度的 75% 正转 (前进) :

```python
pin1.write_analog(770)
pin12.write_digital(0)
```

在 PXT 环境下，右电机以最大速度的 75% 正转 (前进) :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download2.png)

这样做是为了使电机反转，这有点令人困惑。请记住我们需要将方向引脚更改为 1 以改变方向。然后我们需要设置的每个周期内速度引脚为低电平的时间量。与电机正转的情况相反，我们只需把这个数字 (本例中 770) 从 1023 中减掉，得到 253。

在 Python 环境下，右电机以最大速度的 75% 反转 (后退) :

```python
pin1.write_analog(253)
pin12.write_digital(1)
```

在 PXT 环境下，右电机以最大速度的 75% 反转 (后退) :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download3.png)

### Neopixels(全彩 LED)

实际上，“neopixel” 这个名字是 Adafruit 创造的，但是像 “hoover” 是吸尘器品牌的名称，现在是所有类似产品的总称。它的通用术语是 “smart RGB pixel”，通常引用芯片 WS2812B 的名称。但是，有许多不同的芯片都以兼容的方式执行。Bit:Bot 上的实际上是 SK6812-3535

这些全彩 LED 能够通过为芯片上的红色，绿色和蓝色 LED 中的每一个选择 0 到 255 的值来显示 1600 万种颜色中的任何一种。整个过程由 BBC micro:bit 上的一个引脚控制。neopixel 库的使用能够使得控制过程变得简单。

全彩 LED 在 Bit:Bot 上排列顺序为 : 左臂从 **0** 到 **5**，右臂从 **6** 到 **11**。如果需要将更多全彩 LED 连接到扩展端口，将从 **12** 开始。

在 Python 环境下，将全彩 LED 2 设置为紫色 (红色和蓝色合成) :

```python
import neopixel
np = neopixel.NeoPixel(pin13, 12)
np[2] = (40, 0, 40)
np.show()
```

第一行调用 neopixel 库。我们只需要在 Python 程序的最上面执行一次。第二行创建一个 Python 列表，列表中每个全彩 LED 对应一个元素。如图所示，它指定连接到引脚 13 的 12 元素。如果需要添加更多的全彩 LED，那么您需要在 12 的基础上加上添加的全彩 LED 数量。例如，如果您添加了一个 McRoboFace，那么总数将是 12 + 17 = 29，所以您可以将这一行改为 : np = neopixel.NeoPixel(pin13, 29)

第三行将我们选择的全彩 LED (本例中的数字2) 设置为由括号中的三个值设置的颜色，每个值从 0 到 255 分别对应红色，绿色和蓝色。在本例中，将红色和蓝色设置为 40。

第四行告诉 neopixel 库将所有数据复制到全彩 LED。只有此刻 LED 才会改变。一般来说您可以得到所有您想要的变化，只有在最后使用 np.show()

在 PXT 环境下，将全彩 LED 2 设置为紫色 :

就像在 Python 中一样，我们需要添加 neopixel 库。从菜单中执行此操作。选择 **add package**，然后选择 **neopixels**

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download4.png)

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download5.png)

### Line Follower Sensors (寻线传感器)

Line Follower Sensors (寻线传感器) 是数字输入并连接到引脚 **11** (左) 和引脚 **5** (右)。它们与按钮使用的相同的引脚，因此按下按钮将具有与寻线相同的效果。这可能会产生意想不到的副作用 – 按下两个按钮时会导致 micro:bit 进入蓝牙配对模式 (取决于安装的软件)。

所以您可以使用正常的按钮输入来读取传感器数据，或者您可以使用 digital_read 命令 (如下所)。如果左边的传感器检测到线，则表示 Bit:Bot 太靠右，所以应该向左移动。如果右侧传感器检测到线，则情况正好相反。下面是 Python 中一些简单的寻线代码 (为了清晰起见，实际的电机命令在单独的函数中)

```python
while True:
    lline = pin11.read_digital()
    rline = pin5.read_digital()
    if (lline == 1):
        spinLeft( )
    elif (rline == 1):
        spinRight( )
    else:
        forward(speed)
```

在 PXT 环境下，看起来比 Python 更复杂，因为所有的代码都是内联的。您可能需要在循环中添加暂停，具体取决于您的寻线轨道。

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download6.png)

### Light Sensors (光传感器)

Light Sensors (光传感器) 是模拟传感器，将会给出 0 到 1023 的值，其中 0 对应完全黑暗的，1023 对应最大亮度。由于 Micro:Bit 上只有 3 个模拟引脚 (不影响 LED 显示)，我们使用其中的 2 个来控制电机，所以我们剩下一个 (引脚 **2**) 来读取来自 2 个光传感器的模拟值。我们应该怎么做 ? Bit:Bot 有一个模拟开关，它使用一个数字输出信号 (引脚 **16**) 来决定我们正在读取的模拟输入是对应左侧传感器的还是右侧传感器的。

因此，要读取光传感器数据，我们需要首先设置选择输出引脚，然后读取模拟数据。

在 Python 环境下，我们可以将值读入到两个名为 leftVal 和 rightVal 的变量中 :

```python
Pin16.write_digital(0) # select left sensor
leftVal = Pin2.read_analog()
Pin16.write_digital(1) # select right sensor
rightVal = Pin2.read_analog()
```

在 PXT 环境下，方法相似 :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download7.png)

### Buzzer (蜂鸣器)

蜂鸣器是一个非常简单的设备，当它被设置为 ON 时输出 2.4kHz 的声音。它不受引脚 **0** 上输出的音频信号控制，因此无需安装任何库

它连接到引脚 **14**。将此引脚设置为 ON (1) 将激活蜂鸣器，设置为 OFF (0) 将关闭蜂鸣器。

在 Python 环境下，一个非常简单但恼人的嘟嘟声如下 :

```python
while True:
    pin14.write_digital(1)
    sleep(400)
    pin14.write_digital(0)
    sleep(400)
```

在 PXT 环境下，如下所示 :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download8.png)

### Ultrasonic Distance Sensor (超声波传感器)

这个可选的 HC-SR04 ultrasonic distance sensor  (超声波传感器) 插件可以在 Microsoft PXT 中很容易地使用。在 MicroPython 中，我们由于缺少微秒分辨率定时器而受阻。(但请参考下面的演示 “Ultrasonic Obstacle Avoider”)

在 PXT 环境下，您需要添加包 ‘Sonar’。您可以从 Advanced (进阶) 选项卡 (位于底部) 或使用 Tool 菜单 (右上齿轮图标) 完成添加。

Ping 和 Echo 在同一个引脚上 (引脚 **15**)。所以可以这样做 :

![](https://raw.githubusercontent.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/master/Img/Download9.png)

这是每 3 秒打印一次传感器测量到的距离

### Example Micropython Programs (示例 Micropython 程序)

- **[代码]**[Simple PWM motor test](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/PWM_Python.py)
- **[代码]**[Neopixel colour test](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/Pixels_Python.py)
- **[代码]**[Light follower](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/LightFollower.py)
- **[代码]**[Larson Scanner example](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/Scanner.py)
- **[代码]**[Line follower](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/LineFollower2.py)
- **[代码]**[Ultrasonic Obstacle Avoider](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/sonic02.py)
- **[代码]**[POST - Power On Self Test. This test is run on each Bit:Bot before shipping](https://github.com/SeeedDocument/BitBot-Robot_Kit_for_MicroBit/blob/master/res/POST.py)
