---
name: Grove - AND
category: Others
bzurl:  
oldwikiname:  Grove - AND
prodimagename:
surveyurl: 
sku:    110060026
---
# Arduino Grove 入门学习套件使用手册  

Grove 入门学习套件对于初次接触 Arduino 的用户而言是最好的入门学习套件之一，它不需要特别困难的焊接操作和复杂的电路，用户可以专心地学习 Arduino 的使用。该套件包含了一块主控制板，即 Seeeduino Lotus 和 8 个 Grove 模块，涵盖了传感器、驱动器和显示器等功能。用户只需按照指引将模块插入 Seeeduino Lotus 并建立自己的工程文件。  


## 元件清单

 Seeeduino Lotus v1.1  
 Grove - 倾斜开关  
 Grove - 蜂鸣器  
 Grove - 温度和湿度传感器（DHT11）  
 Grove - 3 轴数字加速度计  
 Grove - 光传感器 v1.2  
 Grove - 寻线器 v1.1  
 Grove - 可连接 RGB LED v2.0  
 Grove - 16 x 2 LCD（蓝底白字）  
 

## 关于 Grove

 在我们拥有 Grove 之前，模块每次连接 Arduino 设备都需要电源、信号和地三根连线，因此 Arduino 需要连接大量的导线，操作十分复杂。  
 我们怎样才能简化搭建电路的过程呢？ Grove 生态系统很好地解决了这个问题。每个 Grove 模块实现一个功能，例如感应光线、感应动作等等，用户只需一根 Grove 线连接这些模块并通过 Seeeduino Lotus 在您的设计中实现这些功能。  


## 首次使用 Seeeduino？

如果您之前从未接触过 Seeeduino Lotus 与 Grove 模块，请不用担心，我们有详细教程手把手教您入门。点击 *http://wiki.seeedstudio.com/Grove_Beginner_Kit_for_Arduino/* 进入 Grove - 入门学习套件 wiki 页面的 “Getting Started” 版块查找相关资料。  

我们也有一些有趣的小视频来帮助您更快速和轻松地学习它！  
点击该链接观看视频： *youtu.be/EZVdPm5Y37c*   


## 下载 Sketchbook

如果您成功按照 “Getting Started” 版块里面的说明让内置的 LED 闪烁起来，您就可以着手完善您的 Grove 学习套件了。为了简化编程任务，我们将一些 Grove 学习套件的 demo 打包进了一个 sketchbook 文件内并将其上传至 GitHub。下载连接在这里：  
*https://github.com/Seeed-Studio/Grove_Beginner_Kit_Sketchbook*  




## Grove 数据线

学习套件提供了 4 种不同用途的 Grove 线。对于使用 Seeeduino 或 Base Shield 的一般工程文件而言，您只需标准线就可以了。分支线用于将 Grove 线连接主板的 I2C 端口以连接两台 I2C 设备。如果您的工程需要使用两个伺服电机，您可以选择 Grove - 伺服电机专用分支线。如果您不需要 Base Shield 或 Seeeduino，您可以选择 Grove 转 4-pin 公母跳线连接 Grove 模块和面包板。每种连线都有 5 种不同长度的尺寸，分别是 5cm、20cm、30cm、40cm 和 50cm。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Cables.PNG"/>
</div>  



## 连接示例  

**标准线**  
<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Tilt-Switch2.png" width="400">
</div>  

**分支线**  
<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/branch-cable.PNG" width="600">
</div>

**伺服电机专用分支线**  
<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/servo-cable.PNG" width="600">
</div>

注意：  
驱动伺服电机时推荐使用外部电源供应。  

**Grove 转 4-pin 公母跳线**  
<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/jumper.PNG" width="600">
</div>


## 模块使用说明


<!-- ********************************************************** -->
### Grove - 蜂鸣器  
蜂鸣器可以发出许多声音，是一个很有趣的模块。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Buzzer.png"/>
</div>  

**示例**  
您可以通过编程让蜂鸣器发声，但 Grove - 蜂鸣器可以实现更有趣的功能，例如播放旋律。通过下面的路径找到相关示例：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketch- book-master > tutorial 1 – Buzzer*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Buzzer2.png"/>
</div>  

**小贴士：**  
您可在 Arduino IDE 中设置振荡频率以更改蜂鸣器发出的声音频率。  

<!-- ************************************************************ -->
### Grove - 倾斜开关
改变倾斜开关的摆放角度以控制开关的打开/闭合。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Tilt-Switch.png"/>
</div>  

**示例**  
您可以使用内置的代码实现通过改变摆放的角度控制 Seeeduino Lotus 自带的 LED 灯亮灭。通过下面的路径找到相关示例：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketch-book-master > tutorial 2 - Tilt Switch > 2_tilt_switch_Built- in_LED*
</font> 

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Tilt-Switch2.png"/>
</div>  

**小贴士：**  
在开关里面是两个成对的小球，当开关处于垂直状态时内部金属球常闭触点闭合。  

<!-- ************************************************************ -->
### Grove - 可连接 RGB LED  
Grove 入门学习套件支持一次性点亮最多达 1024 个 RGB LED 灯！  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/led.png"/>
</div>  

**示例**  
您可以使用内置的代码让 LED 按照要求亮起或熄灭，您甚至可以让它们产生非常漂亮而又魔幻的灯光效果。通过下面的路径找到相关示例：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 3 – LED > 1_CycleThroughColors*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/LED2.png"/>
</div>  

<!-- ************************************************************ -->
### Grove - 光传感器  
通过传感器测量不同光照强度并给予相应的反馈。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Light-sensor.png"/>
</div>  

**示例**  
您可以使用内置的代码让传感器测量环境光或之前讲的 Grove - 可连接 RGB LED。我们还提供了一些其他的示例，您可以通过下面的路径找到相关示例：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 4 – Light Sensor > 1_LightSensorSwitch*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Light-sensor2.png"/>
</div>  

**小贴士：**  
该模块中光敏电阻的阻值随光照强度增加而降低，因此输出值相应改变。  

<!-- ************************************************************ -->  
### Grove - 寻线器  
您可以使用该模块让机器人实现沿着画好的路线行走的功能。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Line-finder.png"/>
</div>  

**示例**  
您可以使用内置的代码控制寻线器处的 Grove - 可连接 LED 亮灭。我们还提供了两个其他的示例，您可以通过下面的路径查找：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 5 – Line Detector > 3_LineDetectorSwitch*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Line-finder2.png"/>
</div>  

**小贴士：**  
寻线器有两个部分组成：一个红外发射 LED 和一个红外接收光敏晶体管，可以让机器人实现在白色地板上沿着黑色路线行走的功能。  

<!-- ************************************************************ -->   
### Grove - 16 x 2 LCD （蓝底白字） 
连接到 Seeeduino Lotus 后，该模块可显示所有来自传感器的数据。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/LCD.png"/>
</div>  

**示例**  
您可以使用内置的代码显示任何字符。我们还提供了三个不同的示例，您可以通过下面的路径查找：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 6 - LCD*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/LCD2.png"/>
</div>  

<!-- ************************************************************ -->  
### Grove - 温度和湿度传感器（DHT11）  
该模块基于广泛使用的 DHT11，可用于测量温度和相对湿度。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Temperature&Humidity-Sensor.png"/>
</div>  

**示例**  
您可以使用内置的代码在 Grove - 16 x 2 LCD 中显示温度和相对湿度信息。您可以通过下面的路径查找相关信息：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 7 - DHT11*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Temperature&Humidity-Sensor2.png"/>
</div>  

**小贴士：**  
测量相对湿度的元件一个特制的电容式传感器，测量温度的元件是一个负温度系数（NTC）很大的热敏电阻。  

<!-- ************************************************************ -->  
### Grove - 3 轴数字加速度计  
该传感器用于检测您的下一个动作或方向，它也能用于感应您的手势。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Accelerometer.png"/>
</div>  

**示例**  
您可以使用内置的代码在 Grove - 16 x 2 LCD 中显示3 轴数字加速度计数据，您可以通过下面的路径查找相关信息：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 8 – Accelerometer*
</font>  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/Accelerometer2.png"/>
</div>  

<!-- ************************************************************ -->  



## 演示项目
 

<!-- ********************************************************** -->  
### 智能花园  
Grove 入门学习套件里的模块可以实现一个拥有感应和提醒系统的智能花园。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/demo-projects/smart-garden(CN).PNG"/>
</div>  

**材料清单**  

- Seeeduino Lotus v1.1  
- Grove – 蜂鸣器  
- Grove – 可连接 RGB LED V2.0  
- Grove – 光传感器 v1.2  
- Grove – 16 x 2 LCD （蓝底白字）  
- Grove – 温度和湿度传感器（DHT11） 
- Grove – 倾斜开关 
- Grove 连接线  

完整的实现方法如下：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 9 – Smart Garden > smartGarden*
</font>  

<!-- ********************************************************** -->  
### 智能水杯  
智能水杯可以实现每隔一段时间提醒您喝水的功能。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/demo-projects/smart-cup(CN).PNG"/>
</div>  

**材料清单**


- Seeeduino Lotus v1.1  
- Grove – 蜂鸣器  
- Grove – 可连接 RGB LED V2.0  
- Grove – 16 x 2 LCD （蓝底白字）  
- Grove – 3 轴数字加速度计 
- Grove 连接线  

完整的实现方法如下：  
<font color=green>
*File > Sketchbook > Grove_Beginner_Kit_Sketchbook-master > tutorial 10 – Smart Cup > smartCup*
</font>  

<!-- ********************************************************** -->   


## Seeeduino Lotus V1.1  

Seeeduino Lotus 是一个带有 ATMEGA328P AVR 微控制器的开发板，由 Seeeduino 和 Grove Base Shield 组成。它使用了一个 ATmege328P-MU 微控制器和一个 CP2102N 芯片。ATmege328P-MU 是一款高性能、低功耗的 AVR 8 位微控制器，而 CP2102N 则是一块 USB 转串行数据线的转换器芯片，确保用户可以使用电脑通过 micro-USB 数据线与 Seeeduino
Lotus 进行交互。  
Seeeduino Lotus 拥有 14 个数字输入/输出端口（其中 6 个能以作为 PWM 输出）以及 7 个模拟输入/输出端口、一个 micro USB 接头、一个 ICSP 排针、12 个 Grove 连接器和一个 reset 按键。Seeeduino Lotus 上的 Grove 端口分别是数字（6）、模拟（3）、I2C（2）、UART（1）。  



## Arduino UNO vs Seeeduino Lotus 

相比于 Arduino，Seeeduino Lotus 则是在 Arduino  的基础上增加了一些功能。下图的表格展示了它们之间的一些区别。  

---|Seeeduino Lotus V1.1|Arduino UNO R3
---|---|---
发布时期|2018/0.3|2016/02
微控制器|ATMega328P|ATMega328P
工作电压|5V|5V
闪存|32KB|32KB
SRAM|2KB|2KB
EEPROM|1KB|1KB
供电接口|Micro USB|USB、DC 端口
Grove 连接器|12|无

Grove 模块通过不同协议进行通信，您可以通过学习每个模块的通信方式快速了解它们的使用方法。  


### 1.数字端口  
Seeeduino Lotus 有 6 个数字 Grove 端口，它们分别对应了板子上的 digital pin 0 到 7。通常情况下这些端口用于读取数字传感器 0 到 1 之间的输出值或打开/关闭驱动器。其中有些端口为多用途，例如用于 PWM（脉冲宽度调制）输出。多用途端口分别是端口 3、端口 5 和端口 6。当驱动一个伺服电机或者控制 LED 逐渐变暗时，您将会用到这些端口。  
数字端口对于串行通信同样必不可少，UART 是一个端口 1 上的内置硬连线串行端口，这是 Seeeduino 与 PC 进行串行通信的默认端口。  
当您需要至少两台串行设备或额外的串行端口来调试程序时，其他数字端口、软件串行端口均可作为串行端口使用。在 Grove 系统中我们将遇到很多次这样的情况。  


### 2.模拟输入端口  
Seeeduino Lotus 有 3 个用于读取模拟数据的 Grove 端口。模拟传感器可以返回范围在 0 - 1024 之间的读取值，相比于只能返回 0 或 1 的数字传感器，模拟读取值更加具体和精确。  

### 3.I2C 端口  
Seeeduino Lotus 有 2 个 I2C Grove 端口，I2C 是通过 SCL 和 SDA 两根线传输数据的一个低速总线协议。时钟线 SCL 用于在 I2C 总线上同步数据传输，SDA 就是数据线。下图展示了一个 I2C 总线的框架结构。  

<div align=center>
<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Beginner-Kit/master/I2C-bus.PNG"/>
</div>  

您可以在 I2C 总线上连接多达 128 台设备，但其中只能有一台工作在 master 模式下而其余设备则工作在 slave 模式下。对于 Grove 而言，master 设备是 Arduino。  
它产生时钟信号，也负责将命令发送至所有设备和从设备接收数据信息。理论上每台 slave 设备的硬件地址都是独一无二的，master 设备可通过该地址找到 slave 设备。  
当数据量超过单个数字和模拟端口时，I2C 端口将会派上用场。例如当我们需要获取比较复杂的信息（如角加速度），或者一个 RTC 模块当前时间时，我们将会使用 I2C 端口。  


### 4.UART 端口  
开发板上有一个 UART 端口。UART 用于在各个设备之间建立串行通信。您可以从电脑中发送命令至开发板，反之亦然。  

<!--********************************************************************-->


## 相关资料
  

- [Arduino 网站](https://www.arduino.cc/)
- [Seeed bazaar](https://www.seeedstudio.com/)
- [Seeed 维基主页](http://wiki.seeedstudio.com/)
- [拆箱 & 入门视频](https://youtu.be/EZVdPm5Y37c)
- [技术支持](https://forum.seeedstudio.com)
- [Grove Beginner Kit manual Chinese Online.pdf](https://github.com/SeeedDocument/Grove-Beginner-Kit/raw/master/res/Grove%20Beginner%20Kit%20manual%20Chinese%20Online.pdf)
- [Grove Beginner Kit manual Chinese Printable.pdf](https://github.com/SeeedDocument/Grove-Beginner-Kit/raw/master/res/Grove%20Beginner%20Kit%20manual%20Chinese%20Printable.pdf)
