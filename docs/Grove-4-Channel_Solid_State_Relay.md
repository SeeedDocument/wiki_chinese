---
name: Grove - 4-Channel Solid State Relay
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 103020135
tags:
---

![](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/5.jpg)


固态继电器使用如晶闸管和晶体管之类的电力半导体器件而非线圈。因此它和普通的机械型继电器相比，能提供远远更快的开关速度。**Grove - 4-Channel Solid State Relay** 基于高质量的 **G3MC202P** 模块，让你能够用 5V 直流电控制最大达 240V 的交流电。在 Grove 接口的帮助下，您能非常方便地和 Arduino 一起使用 SSR。

我们使用一块板上芯片 [STM32F030F4P6](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/STM32F030F4P6.pdf) 来分别控制各个通道。来自 Arduino 或是其他主控板的命令通过 I2C 接口传输，板上芯片 STM32F030F4P6 会解析命令，您就可以控制开关了。


基于不同的应用场景，我们为您提供了一系列的固态继电器。


[Grove - Solid State Relay V2](http://wiki.seeedstudio.com/Grove-Solid_State_Relay_V2)

[Grove - 2-Channel Solid State Relay](http://wiki.seeedstudio.com/Grove-2-Channel_Solid_State_Relay)

[Grove - 4-Channel Solid State Relay](http://wiki.seeedstudio.com/Grove-4-Channel_Solid_State_Relay)

[Grove - 8-Channel Solid State Relay](http://wiki.seeedstudio.com/Grove-8-Channel_Solid_State_Relay)



<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-4-Channel-Solid-State-Relay-p-3130.html
" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特性

+ 低功耗
+ 持久性
+ 可选择的 I2C 地址

- 和机械型继电器相比的优点：

    - 和机械型继电器相比，固态继电器拥有远远更快的开关速度。并且不存在物理磨损。
    - 工作时完全安静
    - 没有物理磨损意味着没有火花，使得它能在易爆环境下使用，关键的是即便是在开关时也不会产生火花。
    - 使用寿命增长，即使它被使用了很多次。因为内部没有移动的部件，没有坑接触，也不会碳沉积。
    - 紧凑，轻薄的整体性SSR，含有包括了PCB，终端和散热器的引线框架。因此体积小于机械型继电器并且能整合更多通道。



- 缺点

    - 当 SSR 被关闭时，摩擦力变大，电噪声变大
    - 当 SSR 被打开时，摩擦力降低，出现反向漏电流
    - 只能在直流负载下工作


## 规格参数

|项目|数值|
|---|---|
|工作输入电压|4~6V|
|额定输入电压|5V|
|额定负载电压|100 to 240 VAC 50/60 Hz|
|负载电压范围|75 to 264 VAC 50/60 Hz||
|负载电流|0.1 to 2 A|
|漏电流|1.5 mA max. (at 200 VAC)|
|绝缘电阻|1,000 MΩ min. (at 500 VDC)|
|工作时间|1/2 of load power source cycle +1 ms max.|
|释放时间|1/2 of load power source cycle + 1 ms max.|
|存储温度|-30°C 到 100°C (无结冰或冷凝情况下)|
|工作温度|-30°C 到 80°C (无结冰或冷凝情况下)|
|工作湿度| 45% to 85%RH|
|输入接口|I^2^C|
|默认 I^2^C 地址|0x11 or 0x12|
|可用 I^2^C 地址 |0x00 ~ 0x7F|
|输出接口|DIP Female Blue 2 pin x4|
|Zero Cross|支持|
|认证|UL /  CSA|


!!!Attention
        您可能注意到了上面提到的 **漏电流**，1.5mA 就已足够驱动低功率的 LED，所以当继电器被关闭时，LED 仍可能发出微弱的光。



## 应用场景

- 需要低延迟的开关操作。如楼梯灯光控制。
- 需要高稳定性的设备。如医疗设备，交通信号灯。
- 需要设备防爆，防腐蚀，防潮时。如煤炭业，化学工业。


## 硬件概述


### 引脚定义

![](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/pin_map_1_cn.png)

![](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/pin_map_2_cn.png)


!!!Note
    - 开关 1-4 有同样的功能，所以对所有开关，都可查阅 **LOAD1**/**LOAD2**。
    - 在 PCB 板的背后，有两个接口：SWD 和 I^2^C。当编程固件时，SWD接口默认被使用。如您想要使用I^2^C(实际上作为 boot UART 使用)，只需将 **BOOT** 置高。

### 原理图

**继电器控制**


![](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/img/schematic_.jpg)


**K1** 是继电器模块。当在 **INT+** 和 **INT-** 之间加上 5V 的电压时，继电器将被打开。接着 **LOAD1** 会与 **LOAD2** 连接。我们使用一个 NPN 晶体管 **Q1** 来控制 **INT+** 和 **INT-** 之间的电压。

 **CTR** 是来自 Arduino 或其他主控板的信号。它通过 10k R2 传输而来，若无信号， **Q1** 的栅极（端口1）会变为0V，Q1 被关闭，因此 K1 也被关闭。若 **CTR** 变为5V，Q1 被打开。K1 的 **INT-** 将会与系统的 GND 相连，对 K1 来说， **INT+** 和 **INT-** 之间有5V的电压，所以 K1 被打开， **LOAD1** 和 **LOAD2** 相连接。


**双向电平转换器电路**
![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/schematic_1.jpg)


这是一个用于连接 I^2^C 总线中两个不同电压块的典型双向电平转换器电路。此传感器的 I<sup>2</sup>C 总线使用 3.3V 的电压，若 Arduino 的 I<sup>2</sup>C 总线使用 5V 电压，您就会需要此电路。在上述的原理图中， **Q17** 和 **Q18** 是 N通道的 MOSFET [2N7002A](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/2N7002A_datasheet.pdf)，在这里起到双向开关的作用。为了更好地理解此部分，您可查阅 [AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf)。


!!!NOTE
       在这里我们只展示了部分原理图，完整资料请查看 [此处](/#resources)。


## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg)  |

!!!Caution
    以上列出的支持平台仅代表硬件和理论的兼容性。大部分情况下我们仅提供 Arduino 平台的软件库和代码示例。为所有的MCU平台提供软件库和示例代码是不可能的。因此，使用者可能需要写出自己使用的软件库。


## 入门指导


### 搭配 Arduino 一起使用

#### 硬件连线

**硬件清单**

| Seeeduino V4.2 | Base Shield| Grove - 4-Channel Solid State Relay |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-4-Channel-Solid-State-Relay-p-3130.html" target="_blank">点击购买</a>|


!!!note
    **1** 请小心插入USB线缆，否则您可能会损坏端口。请使用4线的USB线缆，2线的USB线缆无法传输数据。若果您不确定您拥有的是哪种USB线缆，可以[点击此处](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) 购买。
    
    **2** 在您购买时，每个 Grove 模块都附带一根 Grove 线缆。若您丢失了该线缆，可以[点击此处](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) 购买。



- **步骤一** 将 Grove - 4-Channel Solid State Relay 连接到扩展板的 **I^2^C** 端口上。

- **步骤二** 将 Grove - Base Shield 插到 Seeeduino 上。

- **步骤三** 通过 USB 线缆将 Seeeduino 与 PC 连接。


![](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/connect.jpg)


!!!Note
        若您没有 Grove 扩展板，您也可按照以下方式将此模块直接连接到 Seeeduino 上。


| Seeeduino     |  Grove - 4-Channel Solid State Relay           |
|---------------|-------------------------|
| 5V            | 红色                     |
| GND           | 黑色                   |
| SDA           | 白色                   |
| SCL           | 黄色                  |






#### 软件运行

!!!Note
        如果这是您第一次使用 Arduino， 我们强烈推荐您在开始之前阅读 [Arduino 入门](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。



- **步骤一** 从 GitHub 上下载 [Multi_Channel_Relay_Arduino](https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library) 软件库。

- **步骤二** 查阅 [如何安装软件库](http://wiki.seeedstudio.com/How_to_install_Arduino_Library) 后将软件库安装至 Arduino。

- **步骤三** 重启 Arduino IDE。按以下路径打开例子: **File --> Examples --> Multi Channel Relay Arduino Library --> four_channel_relay_control**. 

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/path.jpg)


或者，您可以点击代码块右上角的图标![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg)复制下代码后将其粘贴到 Arduino IDE 的新文件中去

```c++
#include <multi_channel_relay.h>

Multi_Channel_Relay relay;

void setup()
{
  Serial.begin(9600);
  while(!Serial);   

   /* Scan I2C device detect device address */
  uint8_t old_address = relay.scanI2CDevice();
  if((0x00 == old_address) || (0xff == old_address)) { 
    while(1);
  }
    
  Serial.println("Start write address");
  relay.changeI2CAddress(old_address, 0x11);  /* Set I2C address and save to Flash */  
  Serial.println("End write address");

  /* Read firmware  version */
  Serial.print("firmware version: ");
  Serial.print("0x");
  Serial.print(relay.getFirmwareVersion(), HEX);
  Serial.println();
}

void loop()
{

  /** 
   *  channle: 8 7 6 5 4 3 2 1
   *  state: 0b00000000 -> 0x00  (all off)
   *  state: 0b11111111 -> 0xff  (all on)
  */  

  /* Begin Controlling Relay */ 
  Serial.println("Channel 1 on");
  relay.turn_on_channel(1);  
  delay(500);
  Serial.println("Channel 2 on");
  relay.turn_off_channel(1);
  relay.turn_on_channel(2);
  delay(500);
  Serial.println("Channel 3 on");
  relay.turn_off_channel(2);
  relay.turn_on_channel(3);  
  delay(500);
  Serial.println("Channel 4 on");
  relay.turn_off_channel(3);
  relay.turn_on_channel(4);  
  delay(500);
  relay.turn_off_channel(4);

  relay.channelCtrl(CHANNLE1_BIT | 
                    CHANNLE2_BIT | 
                    CHANNLE3_BIT | 
                    CHANNLE4_BIT);
  Serial.print("Turn all channels on, State: ");
  Serial.println(relay.getChannelState(), BIN);
  
  delay(2000);

  relay.channelCtrl(CHANNLE1_BIT |                   
                    CHANNLE3_BIT);
  Serial.print("Turn 1 3 channels on, State: ");
  Serial.println(relay.getChannelState(), BIN);

  delay(2000);

  relay.channelCtrl(CHANNLE2_BIT | 
                    CHANNLE4_BIT);
  Serial.print("Turn 2 4 channels on, State: ");
  Serial.println(relay.getChannelState(), BIN);
  
  delay(2000);


  relay.channelCtrl(0);
  Serial.print("Turn off all channels, State: ");
  Serial.println(relay.getChannelState(), BIN);
  
  delay(2000);
}
```

- **步骤四** 上传您的代码。若您不知道如何上传，请阅读文章 [如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤五** 点击 **Tool-> Serial Monitor** 打开 Arduino IDE 中的 **Serial Monitor**。或同时按下 ++ctrl+shift+m++ 键。

!!!success
     若一切顺利，您将得到结果。同时，您会看到板上的 LED 灯交替闪烁、熄灭。

```c++
Scanning...
I2C device found at address 0x12 !
Found 1 I2C devices
Start write address
End write address
firmware version: 0x1
Channel 1 on
Channel 2 on
Channel 3 on
Channel 4 on
Turn all channels on, State: 1111
Turn 1 3 channels on, State: 101
Turn 2 4 channels on, State: 1010
Turn off all channels, State: 0
Channel 1 on
Channel 2 on
```


![](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/img/gif.gif)


!!!Note
        我们不在此演示中加负载，若您想尝试加上负载，请查阅 [Grove - 2-Channel Solid State Relay](http://wiki.seeedstudio.com/Grove-2-Channel_Solid_State_Relay)。


#### 函数说明

<table style="undefined;table-layout: fixed; width: 749px">
<colgroup>
<col style="width: 233px">
<col style="width: 516px">
</colgroup>
  <tr>
    <th>函数</th>
    <th>描述</th>
  </tr>
  <tr>
    <td><span style="font-weight:bold">changeI2CAddress(uint8_t old_addr, uint8_t new_addr)</span></td>
    <td>更改设备地址，<span style="font-weight:bold">old_addr </span>即当前地址；<span style="font-weight:bold">new_addr </span>是您想要使用的新地址。只有在旧地址输入正确的情况下，才可以成功更改到新地址</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">scanI2CDevice()</span></td>
    <td>得到 <span style="font-weight:700">old_addr </span>(当前地址)</td>
  </tr>
  <tr>
    <td><span style="font-weight:bold">getChannelState()</span></td>
    <td>得到各通道的状态，例如 "State: 1111"，代表所有继电器被打开</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">getFirmwareVersion()</span></td>
    <td>得到被烧写入 MCU 板的固件版本</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">channelCtrl(uint8_t state)</span></td>
    <td>能改变您所选多个或单个通道的状态， <span style="font-weight:600">列出参数表为:</span><br> <br>  <span style="font-weight:bold">CHANNLE1_BIT  </span>或  <span style="font-weight:bold">0x01</span><br>  <span style="font-weight:bold">CHANNLE2_BIT</span>  或  <span style="font-weight:bold">0x02</span><br>  <span style="font-weight:bold">CHANNLE3_BIT</span>  或  <span style="font-weight:bold">0x04</span><br>  <span style="font-weight:bold">CHANNLE4_BIT</span>  或  <span style="font-weight:bold">0x08</span><br><br>例如， <br><span style="font-weight:600">        channelCtrl(CHANNLE2_BIT|CHANNLE3_BIT),</span>将会打开通道2和通道3.<br><span style="font-weight:600">        channelCtrl(0x01|0x02|0x08), </span>将会打开通道1，通道2和通道4.<br><span style="font-weight:600">        channelCtrl(0), </span>将会关闭所有通道.</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">turn_on_channel(uint8_t channel)</span></td>
    <td>打开单个通道<br>例如，<br>        <span style="font-weight:600">turn_on_channel(3), </span>打开通道3.</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">turn_off_channel(uint8_t channel)</span></td>
    <td>关闭单个通道<br>例如，<br><span style="font-weight:600">       turn_off_channel(3), </span>会关闭通道3.</td>
  </tr>
</table>

若您想要改变地址，您需要在使用前设置地址。例如，如我们想将地址改为 0x2f。可用以下代码。


```C++
#include <multi_channel_relay.h>

Multi_Channel_Relay relay;

void setup()
{
  Serial.begin(9600);
  while(!Serial);   

   /* Scan I2C device detect device address */
  uint8_t old_address = relay. ;
  if((0x00 == old_address) || (0xff == old_address)) { 
    while(1);
  }

  Serial.println("Start write address");
  relay.changeI2CAddress(old_address,0x2f);  /* Set I2C address as 0x2f and save it to the EEPRom */  
  Serial.println("End write address");

  /* Read firmware  version */
  Serial.print("firmware version: ");
  Serial.print("0x");
  Serial.print(relay.getFirmwareVersion(), HEX);
  Serial.println();
}


```

## 常见问题

**Q1: 如何烧写固件?**

**A1:** 我们推荐您使用 J-Link 烧写器 和 WSD 接口来烧写固件。 

您可在以下链接下载固件:

[Factory firmware](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/res/Grove-4-Channel-Solid-Relay-Firmware.bin)

我们推荐您使用 J-flash 作为软件:

[J-flash](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)


![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/J-flash.jpg)

## 资源下载

- **[Zip]** [Grove-4-Channel SPDT Relay 原理图](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/res/Grove%20-%204-Channel%20Solid%20State%20Relay.zip)
- **[Zip]** [多通道继电器 Arduino 软件库](https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library/archive/master.zip)
- **[Bin]** [Factory firmware](https://github.com/SeeedDocument/Grove-4-Channel_Solid_State_Relay/raw/master/res/Grove-4-Channel-Solid-Relay-Firmware.bin)
- **[PDF]** [G3MC202P 数据手册](https://github.com/SeeedDocument/Grove-Solid_State_Relay_V2/raw/master/res/G3MC202p.pdf)
- **[PDF]** [STM32 数据手册](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/STM32F030F4P6.pdf)


## 项目

这是本产品的介绍视频，有简单代码展示，您可以一试。

<iframe width="560" height="315" src="https://www.youtube.com/embed/5uBLf_a0DNc?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


## 技术支持
欢迎您将您的问题提交至我们的 [论坛](https://forum.seeedstudio.com/)。

