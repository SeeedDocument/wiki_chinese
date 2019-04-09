---
name: Arch Mix
category: SBC
bzurl: 
oldwikiname: 
prodimagename: 
surveyurl: 
sku: 102080027
---


![](https://github.com/SeeedDocument/Arch_Mix/raw/master/img/main1.jpg)

Arch Mix 是一款基于恩智浦 i.MX RT1052 (3020 CoreMark/1284 DMIPS @ 600 MHz) 处理器的轻量级开发板。该开发板预装了 RT-Thread 实时操作系统并且内置 micro-python。 这使其适用于工业控制，特别是对于具有大代码量和高实时应用要求的场景。

NXP i.MX RT1052 属于全新的处理器系列，采用恩智浦先进的 ArmCortex®-M7 内核实现。目前，i.MX RT1052 是性能最高的 Cortex-M7 解决方案，可提供 3036 个 CoreMark，比 LPC1788 微控制器强 13 倍。 除了高速性能，它还提供快速的实时响应。 i.MX RT1052 还具有丰富的音频和视频功能，包括 LCD 显示屏，基本 2D 图形，相机接口，SPDIF 和 I2S 音频接口。


RT-Thread 是用于嵌入式设备的开源IoT操作系统。 内核具有实时多任务调度，semaphore, mutex, mail box, message queue, signal 等。这是一个快速加载的轻量级系统，可实现秒级开机。有关RTOS的更多详细信息，请参阅 [Github](https://github.com/RT-Thread/rt-thread) 页面。


<p style="text-align:center"><a href="https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.7d7833db3Rkxiy&id=556013757631" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>




## 应用场景

- 工业控制
- 智能建筑
- 工业人机界面
- 自动化与过程控制
- 机器人



## 产品特性

- 基于 ARM® Cortex®-M7 600MHz 微处理器(NXP i.MX RT1052)
- 预装 RT-Thread 实时操作系统
- 自带 micro-python
- 超快的系统开机加载速度
- 丰富的外设接口: RMII, CAN, I2C, UART, CSI, I2S, ADC, SPDIF IN/OUT, SWD
- 比其他 RT1052/1050 开发板更小巧轻便: 67mm x 39mm
- 超高性价比，其他 i.MX RT1052 开发板都在90美元以上价格，Arch Mix只需要30美元




## 规格参数

|参数|内容|
|----|----|
|**处理器: NXP i.MX RT1052**||
|平台|ARM Cortex-M7 MPCore|
|主频|600 MHz|
|Boot ROM|96KB|
|板载 RAM|512KB|
|**存储**||
|SDRAM|32MB|
|QSPI Flash|8MB|
|HyperFlash(可选)|64MB|
|**接口与外设**||
|USB 2.0 Host|x1|
|USB 2.0 OTG, DC 5V 电源输入|x1|
|Boot 配置 DIP 开关|x1|
|LED|电源指示灯 x1<br>用户 RGB LED x1|
|按钮|Reset button (复位按钮) x1, On/Off button (电源开关按钮) x1, User button (用户按钮) x1|
|24bit RGB LCD 接口|x1|
|Micro SD card 插槽|x1|
|RTC 3V 电池接口|x1|
|22Pin 排针|RMII, CAN, I2C, UART, CSI, I2S,<br> ADC, SPDIF IN/OUT, SWD|

<div align="center"><b>表 1.</b><i>规格参数</i></div>




## 硬件概览



<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/pinout_f.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/pinout_f.jpg" /></a></p>
  <figcaption><b>图 1</b>. <i>正面概览</i></figcaption>
</figure>
</div>


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/pinout_b.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/pinout_b.jpg" /></a></p>
  <figcaption><b>图 2</b>. <i>背面概览</i></figcaption>
</figure>
</div>


!!!Annotation
    <font color="red"><b>*0</b></font> 请使用 USB OTG 接口为 Arch Mix 供电. USB HOST 和 USB OTG 之间的区别请参考 [这里](https://www.quora.com/What-is-the-difference-between-USB-host-VS-USB-OTG). 
    
    <font color="red"><b>*1</b></font> Flash 模块可选, 您可以选择 64M HyperFlash (U7 默认不贴) 或者 8M QSPI Flash(U11- 默认Flash). 
    
    <font color="red"><b>*2</b></font> 系统通过 USB OTG 供电之后， 您可以通过长按这个按钮 (大约3 ~ 5秒) 来切换系统的开关状态。

    <font color="red"><b>*3</b></font> 请注意，此端口是1.25mm CR2032电池端口，请勿插入锂电池。 如果您想使用RTC功能，可以在淘宝或其他网站上搜索“CR2032电池引线电池”。



**供电**

请使用 Micro-USB **OTG** 端口供电. 


!!!Danger
        - 电源输入电压为 5V, 不能超过 5.5V。
        - 所有数字和模拟 IO 接口电平均为3.3V。 请不要输入超过3.3V，否则可能会损坏CPU。 
        - RTC的电池供电接口（J6）只能连接一个约3V的纽扣电池，电压不能超过3.6V。


**拨码开关**

Arch Mix 可以配置为三种 boot 模式: HyperFlash, QSPI Flash 以及 SD Card. 板子默认使用 QSPI Flash, 当你修改启动模式时 , 你也需要将 DIP 拨码开关拨动到对应位置.


启动设备 | BOOT_CFG | SW1 拨码值
---|---|---
HyperFlash|0x02_00|0 , 1 , 1 , 0
QSPI Flash|0x00_00|0 , 0 , 1 , 0
SD|0x00_40|1 , 0 , 1 , 0

<div align="center"><b>表 2.</b><i>BOOT 拨码开关配置</i></div>



**按钮**

开发板上有三个按钮，按钮功能您可以参考下表.

按钮名字|功能|细节
---|---|---
SW2|用户按钮|对于用户配置，对于该开发板，125 号引脚对应 SW2
SW3|复位|系统重置，当您按此按钮时，系统将重新启动
SW4|电源 On/OFF|通过按住（约3~5秒）此按钮来打开和关闭系统


<div align="center"><b>表 3.</b><i>按钮功能表</i></div>



**LCD 接口**

如您所见，该主板上有一个50针LCD接口，支持高达1366 x 768 WXGA分辨率。 如果您需要此板的 LCD 屏幕，您可以使用 LCD8000 串行屏幕。 您可以查看以下链接购买。

– 

[LCD from NXP](https://www.nxp.com/support/developer-resources/software-development-tools/i.mx-developer-resources/evaluation-kit-for-the-i.mx-6ull-and-6ulz-applications-processor:MCIMX6ULL-EVK?tab=Buy_Parametric_Tab#/)  
[LCD from Embest](http://www.embest-tech.com/prod_view.aspx?TypeId=118&Id=277)
 


### 引脚定义


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/pinout.png" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/pinout.png" /></a></p>
  <figcaption><b>图 3</b>. <i>引脚图, 点击查看清晰图片</i></figcaption>
</figure>
</div>

!!!Tip
    恩智浦 i.MX RT1050 处理器的大多数引脚都具有多路复用功能，您可以单击下面的附件查看详细的引脚多路复用。

 [Arch Mix Pin Definition Table](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/Arch%20Mix_v1.0_Pin.xlsx)


### 模块图

<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/Block.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/Block.jpg" /></a></p>
  <figcaption><b>图 4</b>. <i>Arch Mix 模块图, 点击查看清晰图片</i></figcaption>
</figure>
</div>


### 尺寸图


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/D1.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/D1.jpg" /></a></p>
</figure>
</div>


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/D2.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/D2.jpg" /></a></p>
  <figcaption><b>图 5</b>. <i>尺寸图, 单位(mm)</i></figcaption>
</figure>
</div>







## 硬件连接


**材料清单**


[Arch Mix x1](https://www.seeedstudio.com/Arch-Mix-p-2901.html)<br> 
[USB 转 串口适配器 x1](https://www.seeedstudio.com/PL2303-USB-to-Serial-TTL-Module-Adapter-p-2358.html)<br> 
[Micro USB 线缆 X1](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)  
[双头母跳线 x4](https://www.seeedstudio.com/1-pin-dual-female-jumper-wire-100mm-50pcs-pack-p-260.html)



- **步骤 1.** 使用跳线将 Arch Mix 和 USB 转串口适配器相连


Module|PIN Connection||||
---|---|---|---|---
Arch Mix|VCC|GND|TXD|RXD
USB to Serial Module|VCC|GND|RX|TX

<div align="center"><b>表 4.</b><i>UART 连接说明</i></div>


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/UART.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/UART.jpg" /></a></p>
  <figcaption><b>图 6</b>. <i>UART 连接</i></figcaption>
</figure>
</div>


- **Step 2.** 将 USB 转串口模块连接到您的电脑 

- **Step 3.** 通过 OTG 口给 Arch Mix 供电。板载的电源 LED 将点亮，RGB LED 将变成绿色.

<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/RTT1.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/on.jpg" /></a></p>
  <figcaption><b>图 7</b>. <i>上电</i></figcaption>
</figure>
</div>


- **Step 4.** 打开您的 **计算机管理**, 找到 **设备管理器**. 您将看到 **RT-Thread Debug Bridge** 和对应的 COM 口, 记住 COM 口的号码. 如您所见，本 wiki 的号码为 COM8.

<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/RTT1.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/RTT1.jpg" /></a></p>
  <figcaption><b>图 8</b>. <i>查看 COM 号</i></figcaption>
</figure>
</div>

- **Step 5.** 使用串口工具软件 (例如: [Putty](https://www.putty.org/)) 来读取串口数据.  选择对应的串口号, 将波特率设置成 **115200**.



<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/COM22.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/COM22.jpg" /></a></p>
  <figcaption><b>图 9</b>. <i>配置串口工具</i></figcaption>
</figure>
</div>


- **Step 6.** 按下 **复位** 按键, 用以初始化串口输出。




## RT-Thread


### 关于 RT-Thread

RT-Thread 诞生于 2006 年，其许可类似于 FreeRTOS，并以开源，免费的方式发布。 与 FreeRTOS 和 uC/OS 不同，RT-Thread 与中间件平台一起发布，其中包括网络，文件系统和 GUI 界面等组件。 经过短暂的过渡期后，Cortex M MCU 在 2009 年得到了支持，并获得了许多开发人员的认可和支持。 2011 年以后，由于其成熟稳定的元件，广泛应用于工业控制，电力，新能源，高铁，医疗设备，水利，消费电子等行业。 我们为这三个 RTOS 制作了一个比较表。


| 项目              | FreeRTOS                                                     | µC/OS                                                        | RT-Thread                                                    |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 内核大小          | 5KB ROM, 2KB RAM                                             | 6KB ROM, 1KB RAM                                             | 3KB ROM,1KB RAM                                              |
| 内核机制          | 邮箱  <font color='red'><b>✘</b></font> <br>事件 <font color='red'><b>✔</b></font> <br>协程<font color='red'><b>✔</b></font> | Mailbox 邮箱 <font color='red'><b>✔</b></font> <br>Event事件 <font color='red'><b>✔</b></font> | 邮箱  <font color='red'><b>✔</b></font> <br>事件 <font color='red'><b>✔</b></font><br/>消息队列<font color='red'><b>✔</b></font> |
| 开发工具支持      | 支持多种主流开发工具，工具链完善                             | 支持多种主流开发工具，工具链完善                             | 支持多种主流开发工具，工具链完善，提供辅助工具               |
| 调试工具          | Shell<br/>SystemView                                         | SystemView                                                   | Shell<br/>Logging system<br/>NetUtils<br/>ADB<br/>SystemView<br/> |
| 测试系统          | 不支持                                                       | 不支持                                                       | 单元测试框架<br/>自动测试系统                                |
| 支持芯片和CPU架构 | 支持ARM、MIPS、RISC-V、Xtensa和其他主流CPU架构               | 支持ARM、MIPS和其他主流CPU架构                               | 支持ARM、MIPS、RISC-V和其他主流CPU架构                       |
| 文件系统          | 支持FAT                                                      | 需要授权                                                     | 提供文件系统层，支持fatfs, littlefs, jffs2, romfs 和其他流行文件系统 |
| 低功耗            | 支持部分                                                     | 支持部分                                                     | 支持                                                         |
| GUI               | 无                                                           | µC/GUI，需授权                                               | 提供GUI引擎                                                  |
| 组件生态          | 提供网络、调试、安全相关组件                                 | 有部分，但需要授权                                           | 提供软件包平台，目前有约100个组件，覆盖面广                  |
| 物联网组件        | TCP/UDP/AWS                                                  | 需要授权                                   | TCP/UDP, Azure, Ayla, Aliyun，onenet, webclient, mqtt， websocket, WebNet... |

<div align="center"><b>表 5.</b><i>三种嵌入式操作系统技术和生态对比</i></div>




### 运行 MicroPython


该开发板预装了 RT-Thread 实时操作系统和内置 micro-python，因此当您按照上述步骤连接系统上的硬件和电源时，您将看到系统日志。 RT-Thread 是一个轻量级系统，加载速度非常快，一两秒钟后，系统启动，您将看到以下界面：



<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/RTT2.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/RTT2.jpg" /></a></p>
  <figcaption><b>图 10</b>. <i>RT-Thread 启动界面</i></figcaption>
</figure>
</div>



在 Finsh/MSH 命令行中输入 `python` 来进入 MicroPython's 命令行界面 : -- REPL(Read-Evaluate-Print-Loop). 您可以在终端中看到如下界面:


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/RTT3.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/RTT3.jpg" /></a></p>
  <figcaption><b>图 11</b>. <i>进入 REPL(Read-Evaluate-Print-Loop)</i></figcaption>
</figure>
</div>


您可以按住键盘 ++ctrl+d++ 也可以输入 `quit()` 或者 `exit()` 来退出 REPL 并且返回 RT-Thread Finsh/MSH.


#### 复制粘粘模式


MicroPython是Python 3编程语言的精简高效实现，包括Python标准库的一小部分，并且经过优化，可在微控制器和受限环境中运行。

- MicroPython有一个特殊的粘贴模式，而不是普通的python交互环境，可以用来一次粘贴多行python代码。
- 在命令提示符下, 同时按下 ++ctrl+e++, 就会出现提示：粘贴模式

- ++ctrl+c++ 取消, ++ctrl+d++ 结束. 当你把需要运行的代码粘贴好后, 按住 ++ctrl+d++ 来退出粘贴模式, 然后你已经粘贴的代码就会自动运行。


<div align="center">
<figure>
  <p style="text-align:center"><a href="https://raw.githubusercontent.com/SeeedDocument/Arch_Mix/master/img/RTT4.jpg" target="_blank"><img src="https://github.com/SeeedDocument/Arch_Mix/raw/master/img/RTT4.jpg" /></a></p>
  <figcaption><b>图 12</b>. <i>粘贴模式</i></figcaption>
</figure>
</div>


### MicroPython 示例程序

#### 闪烁灯

如您所见，此板上有一个RGB LED，通常这个LED显示为绿色。 该演示将向您展示如何控制这个 RGB LED。


!!!Note
        这个 RGB LED 连接到 RT1052 芯片的 No. 52 pin   

- 你可以按下 ++ctrl+e++ 来进入复制粘贴模式。 
- 然后将下面的代码块复制到命令行中 
- 按下 ++ctrl+d++ 来退出粘贴模式，您刚刚粘贴的代码就会运行

```python
import time
from machine import Pin

LED = Pin(("LED1", 52), Pin.OUT_PP)          #Set pin 52 to output mode
while True:
    LED.value(1)
    time.sleep_ms(500)
    LED.value(0)
    time.sleep_ms(500)
```

现在您将看到 LED 灯闪烁


#### 按键灯

在 RGB LED 的旁边, 您可以看到一个 USER button(用户按钮), 此演示将向您展示如何使用 USER按钮 控制 RGB LED。

!!!Note
    - RGB LED 连接到 RT1052 芯片的 No. 52 pin
    - 用户按键连接到 RT1052 芯片的 No. 152 pin


- 你可以按下 ++ctrl+e++ 来进入复制粘贴模式。 
- 然后将下面的代码块复制到命令行中 
- 按下 ++ctrl+d++ 来退出粘贴模式，您刚刚粘贴的代码就会运行


```python
from machine import Pin

led = Pin(("LED1", 52), Pin.OUT_PP)
key = Pin(("KEY", 125), Pin.IN, Pin.PULL_UP) #Set pin 125 to pull-up input mode
while True:
    if key.value():
        led.value(0)
    else:
        led.value(1)

```

现在代码在运行中, RGB LED 将变成黄色, 当你按下用户按钮并保持，RGB LED 将变成绿色。



### 固件升级


这个Arch Mix是预先安装的 RT-Thread 实时操作系统和内置微型python。 如果您需要刻录固件或升级固件，可以参考指南并下载工具。



[Arch Mix 固件指南](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/micropython_firmware.pdf)  
[固件工具](https://github.com/SeeedDocument/GM6020/raw/master/res/Firmware_and_Tools.zip)





## 资源下载


- **[ZIP]** [固件工具和指南](https://github.com/SeeedDocument/GM6020/raw/master/res/Firmware_and_Tools.zip)
- **[PDF]** [PDF 格式 Wiki](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/Arch_Mix.pdf)
- **[PDF]** [i.MX RT1050 Datasheet](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/i.MX%20RT1050.pdf)
- **[PDF]** [尺寸图](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/ARCH%20MIX_V1.0_Dimension.pdf)
- **[xlsx]** [Arch Mix_v1.0_引脚功能](https://github.com/SeeedDocument/Arch_Mix/raw/master/res/Arch%20Mix_v1.0_Pin.xlsx)




## Tech Support
Please submit any technical issue into our [forum](http://forum.seeedstudio.com/) or drop mail to techsupport@seeed.cc. 




