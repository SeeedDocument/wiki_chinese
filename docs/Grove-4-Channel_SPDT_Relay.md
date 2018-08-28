---
title: Grove - 4-Channel SPDT Relay
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 103020133
tags:
---

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/main.jpg)

Grove - 4-通道 SPDT继电器 有四个单刀双掷（SPDT）开关。开关。它只需要通过低电压和低电流信号来控制通断。具体地讲，您可以使用 **5V DC** 来控制最大 **250V AC** 或者 **110V DC**。

我们使用板载STM32F030F4P6分别控制各个通道。从Arduino或者其他的板子指令通过IIC接口传输，板载 STM32F030F4P6 将会解析指令，因此您可以根据需要控制开关。


<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-4-Channel-SPDT-Relay-p-3119.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 产品特点

+ 耐高温塑料外壳
+ 高电压负载
+ 低功耗
+ 持久工作
+ 可选IIC地址
    - 0x00 ~ 0x7F


## 产品规格

|**项目**|**参数**|
|:----:|:----:|
|工作电压|5V|
|额定线圈电流|89.3mA|
|TUV认证负载|10A 250VAC/10 30VDC|
|UL认证负载|10A 125VAC/10A 28VDC|
|最大允许电压|250VAC/110VDC|
|功耗|约 0.45W|
|接触电阻|最大100mΩ|
|绝缘电阻|最小100MΩ（500VDC）|
|最大开关频率|30次操作/分钟|
|环境温度|-40℃ 到 +85℃|
|工作湿度|45% 到 85%（相对湿度）|
|触点材料|银氧化镉|
|输入接口|IIC|
|默认 IIC 地址|0x11 或者 0x12|
|可用IIC地址 |0x00 ~ 0x7F|
|输出接口|3引脚直插式绿色端子|


!!!**提示**
        对于负载参数，我们提供两组认证数据。实际上，最大负载为10A 250VAC/10A 30VDC.


## 产品应用

- 家用电器
- 办公设备
- 遥控电视接收器
- 监视器显示
- 音响设备高冲电流应用


## 硬件概述


### 引脚映射

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/pin_map_front.jpg)

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/pin_map_back.jpg)


!!!**注意**
   - 开关1-4具有相同的引脚功能，因此对于其他开关，您可以参考 **NC1**/**COM1**/**NO1**.
   - 在PCB的背面，有两个接口：SWD和IIC。在编程烧写固件时，默认使用SWD接口。如果要使用IIC接口（实际用作引导UART），则应将 **BOOT** 置高。

### 原理图


**继电器控制 **

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/schematic.jpg)

**K2**是继电器模块，在K2的 **引脚1** 和 **引脚3** 之间有一个线圈。默认情况下，**COM2**与 **NC2**连通。如果K2的引脚3连接到地，那么线圈将会‘打开’，**COM2**将会连接到 **NO2**；

开启此线圈，需要约90mA的电流，然而，一般情况下Arduino的GPIO引脚只能提供20mA（最大40mA）。因此我们使用了一个可以提供500mA的NPN三极管[S9013](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/Transistors_NPN_25V-500mA.pdf) 。

当 **PA7** 通过10K电阻R2拉低时，如果没有信号， **Q2** 的基极是0V，Q2关闭，那么K2将处于关闭状态。当 **PA7** 是5V时，Q2将被打开。K2的 **引脚3** 会被连接到系统的GND，那么K2的 **引脚3** 和 **引脚1** 之间将会有5V的压差，线圈会被打开，然后 **COM2** 将会与 **NO2** 连接。


!!!**提示**

**D1**是一个 [反激二极管（反冲二极管）](https://en.wikipedia.org/wiki/Flyback_diode)。反激二极管是连接在电感上的二极管，用于消除当电源电流突然降低或者中断时突然出现在感性负载上的电压尖峰。它被用于由开关控制的感性负载、开关电源和逆变器的电路中。


**双向电平转换电路**
![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/schematic_1.jpg)

这一个连接在IIC总线差分电压部分的典型双向电平转换电路。传感器的IIC总线使用3.3V，而Arduino的IIC总线使用的是5V，因此这个电路是必须的。如上面的原理图所示，**Q17** 和 **Q18** 是作为双向开关的N沟道场效应管[2N7002A](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/2N7002A_datasheet.pdf)。为了更好地理解这一部分，您可以参考[AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf)


!!!**提示**

在这一部分我们仅仅展示了部分原理图，完整的原理图文件请您参考 [资源下载](/#resources)


## 兼容平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|:-:|:-:|:-:|:-:|:-:|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg)  |

!!!**注意**

以上所提到的兼容平台指的是硬件模块在理论上可以兼容。然而在大多数情况下，我们仅仅为Arduino平台提供软件库或者代码示例。无法为所有的MCU平台提供提供库/代码示例。因此，用户在使用其他平台时需要自己编写软件库。





## 入门指导


### 使用Arduino

#### 硬件连接

**材料需求**


| Seeeduino V4.2 | Base Shield| Grove - 4-通道 SPDT 继电器 |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买/a>|<a href="https://www.seeedstudio.com/Grove-4-Channel-SPDT-Relay-p-3119.html" target="_blank">点击购买</a>|

!!!**注**

  **1** 请轻轻地插入USB线缆，否则可能会损坏端口。请使用内部有4根线的USB线缆，2根线的无法传输数据。如果你无法确认你的线缆类型，请点击[这里](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)进行选购。
    
  **2**  购买时，每个Grove模块都配有Grove线缆。如果您不慎丢失了Grove线缆，可以点击[这里](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)选购。




- **步骤 1.** 将Grove - 4-Channel SPDT 继电器连接到Base Shield的 **IIC** 接口。

- **步骤 2.** 将Base Shield插到Seeeduino上。

- **步骤 3.** 通过USB线缆将Seeeduino连接到PC端。


![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/8.22%E8%BF%9E%E6%8E%A51.jpg)


!!!**注意**

如果没有Grove Base Shield，我们可以直接按照下面引脚定义将模块连接到Seeeduino上。


| Seeeduino     |  Grove - 4-通道 SPDT 继电器|
|:-:|:-:|
| 5V            | 红                     |
| GND           | 黑                   |
| SDA           | 白                   |
| SCL           | 黄                  |






#### 软件代码

!!!**注意**

如果这是您第一次使用Arduino，我们强烈建议您先看一下[Arduino 入门指导](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/).



- **步骤 1.** 从Github上下载[Multi_Channel_Relay_Arduino](https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library) 库。

- **步骤 2.** 请参考如何为Arduino安装库[如何安装库文件](http://wiki.seeedstudio.com/How_to_install_Arduino_Library)。

- **步骤 3.** 重启Arduino IDE。 通过路径：**File --> Examples --> Multi Channel Relay Arduino Library --> four_channel_relay_control**打开示例程序。

![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/path.jpg)


或者，您可以点击这个位于代码块右上方的图标![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg)将以下代码拷贝进Arduino IDE。

```c++
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

- **步骤 4.** 上传代码。如果您不知道如何上传代码，请点击[如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。
- **步骤 5.** 通过点击 **Tool-> Serial Monitor** 打开Arduino IDE的 **Serial Monitor** 。或者同事按下 ++ctrl+shift+m++ 。如果一切运行正常，您将会看到以下运行结果。

!!!**成功**

如果一切运行正常，您将会看到以下运行结果。同时，您也会看到板载LED灯交替闪烁。

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


![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/_DAS5552.MOV_20180822_104218.gif)



!!!**注**


在这个例程里面我们没有添加负载，如果您想要知晓如何添加负载，请点击[Grove - 4-通道 SPDT 继电器](http://wiki.seeedstudio.com/Grove-2-Channel_SPDT_Relay/).


#### 功能说明

<table style="undefined;table-layout: fixed; width: 749px">
<colgroup>
<col style="width: 233px">
<col style="width: 516px">
</colgroup>
  <tr>
    <th>功能</th>
    <th>描述</th>
  </tr>
  <tr>
    <td><span style="font-weight:bold">changeI2CAddress(uint8_t old_addr, uint8_t new_addr)</span></td>
    <td>改变设备地址， <span style="font-weight:bold">old_addr </span>是当前地址； <span style="font-weight:bold">new_addr </span>是您想要使用的新地址。只有当输入正确的旧地址，新地址才能够被成功设置。</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">scanI2CDevice()</span></td>
    <td>获得<span style="font-weight:700">old_addr </span>(当前地址)</td>
  </tr>
  <tr>
    <td><span style="font-weight:bold">getChannelState()</span></td>
    <td>获得每个通道的状态，例如"State: 1111", 表示所有继电器都是开通状态</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">getFirmwareVersion()</span></td>
    <td>获得板载MCU的固件版本</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">channelCtrl(uint8_t state)</span></td>
    <td>立即更改您所选择的通道状态，<span style="font-weight:600">状态参数列表：</span><br> <br>  <span style="font-weight:bold">CHANNLE1_BIT  </span>或者  <span style="font-weight:bold">0x01</span><br>  <span style="font-weight:bold">CHANNLE2_BIT</span>  或者  <span style="font-weight:bold">0x02</span><br>  <span style="font-weight:bold">CHANNLE3_BIT</span>  或者  <span style="font-weight:bold">0x04</span><br>  <span style="font-weight:bold">CHANNLE4_BIT</span>  或者  <span style="font-weight:bold">0x08</span><br><br>例如： <br><span style="font-weight:600">        channelCtrl(CHANNLE2_BIT|CHANNLE3_BIT),</span>将会打开通道2和通道3<br><span style="font-weight:600">        channelCtrl(01|02|08), </span>将会打开通道1、通道2和通道4<br><span style="font-weight:600">        channelCtrl(0), </span>将会关闭所有通道.</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">turn_on_channel(uint8_t channel)</span></td>
    <td>打开单通道<br>例如：<br>        <span style="font-weight:600">turn_on_channel(3), </span>将会打开通道3</td>
  </tr>
  <tr>
    <td><span style="font-weight:600">turn_off_channel(uint8_t channel)</span></td>
    <td>关闭单个通道<br>例如：<br><span style="font-weight:600">       turn_off_channel(3), </span>将会关闭通道3</td>
  </tr>
</table>


如果您想更改地址，则需要在使用前设置地址。 例如，我们想将其更改为0x2f。 我们可以使用以下代码。

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

## FAQ

**Q1: 如何烧写固件？**

**A1:** 我们建议您使用J-LINK下载器通过SWD接口烧写固件。

您可以点击[出厂固件](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/Grove-4-Channel-SPDT-Relay-Firmware.bin)进行下载。

我们建议您使用
[J-flash](https://www.segger.com/downloads/jlink#J-LinkSoftwareAndDocumentationPack)软件。


![](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/img/J-flash.jpg)

## 资源下载

- **[Zip]** [Grove-4-Channel SPDT Relay eagle files](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/Grove-4-Channel_SPDT_Relay.zip)
- **[Zip]** [Multi Channel Relay Arduino Library](https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library/archive/master.zip)
- **[Bin]** [Factory firmware](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/Grove-4-Channel-SPDT-Relay-Firmware.bin)
- **[PDF]** [Datasheet of SRD 05VDC-SL-C Relay](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/SRD_05VDC-SL-C.pdf)
- **[PDF]** [Datasheet of S9013](https://github.com/SeeedDocument/Grove-2-Channel_SPDT_Relay/raw/master/res/Transistors_NPN_25V-500mA.pdf)
- **[PDF]** [Datasheet of STM32](https://github.com/SeeedDocument/Grove-4-Channel_SPDT_Relay/raw/master/res/STM32F030F4P6.pdf)


## 技术支持
请您不要犹豫，来我们的[论坛](https://forum.seeedstudio.com/)提出问题吧！

