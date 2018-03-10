---
title: LoNet 808 - Mini GSM/GPRS + GPS Breakout
category: MakerPro
bzurl: https://www.seeedstudio.com/LoNet-808-Mini-GSM%26GPRS-%2B-GPS-Breakout-p-2493.html
oldwikiname:  LoNet 808 - Mini GSM/GPRS + GPS Breakout
prodimagename:  113990107%200.jpg
wikiurl: http://wiki.seeedstudio.com/cn/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout
sku:  113990107
---
![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/113990107%200.jpg)

该主板基于最新的 SIMCOM SIM808 GSM/GPS 模块，它提供蜂窝 GSM 和 GPRS 数据以及卫星导航 GPS 定位。

该主板在睡眠模式下具有超低功耗特性，使得其待机时间非常长。此外，它还有一个板载电池充电电路，可以用于给 LiPo 电池充电。

模块的 GPS 接收机灵敏度很高，具有 22 个追踪通道和 66 个采集通道，还支持辅助 GPS（A-GPS）进行室内定位。该板通过 UART 由 AT 命令控制，支持 3.3V 和 5V 逻辑电平。它配备了一个迷你 GPS 和 GSM 天线，电池是可选的。

该板使用 2G（不是 3G 或 LTE）GSM 网络。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.76bb17391UGMz0&id=534736461961)

##   产品特性
---
*   四频 850/900/1800/1900MHz

*   GPRS 多时隙等级 12 连接：可达 85.6kbps（下载/上传）

*   GPRS 手机站点 B 类

*   由 AT 命令控制（3GPP TS 27.007,27.005 和 SIMCOM 增强型 AT 命令）

*   支持锂离子电池的充电控制

*   支持实时时钟

*   电源电压范围 3.4V〜4.4V

*   集成 GPS/CNSS 并支持 A-GPS

*   支持3.0V至5.0V逻辑电平

*   低功耗，睡眠模式下 1mA

*   支持 GPS NMEA 协议

*   尺寸 27mm x 46mm x 10mm

*   标准SIM卡

##   GPS 规格参数
---
*   接收机通道：22 跟踪/ 66 采集

*   捕获码 GPS L1

*   跟踪灵敏度：-165dBm

*   Cold start time（冷启动时间）: 30s (典型值)

*   Hot start time（热启动时间）: 1s (典型值)

*   Warm start time（热启动时间，无星历数据）: 28s (典型值)

*   水平位置精度：<2.5m CEP

*   功耗 - 采集：42mA

*   功耗 - 连续跟踪：24mA

*   刷新率：5Hz

##   接口
---
![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/Mappings-01.png)

① 电源按钮：这是模块的硬件电源开关。给模块供电时，您可以通过按住按钮 2 秒来打开或关闭模块。

② 锂离子电池接口：用锂电池给模块供电，输入电压为 3.4V 至 4.4V。它采用 JST-2.0mm 接口，可以很方便的连接 3.7V Li-Po 电池。

③ 锂离子电池充电接口，输入电压范围为 5V〜7V。

④ GSM 天线：这是一个 uFL GSM 天线接口，只要连接 GSM 天线即可接收 GSM 信号。

⑤ GPS天线：这是一个 uFL GPS 天线接口。您可以连接无源或有源 GPS 天线。有源 GPS 天线在 2.8V 电压下运行。

⑥ 网络指示灯：红色指示灯，显示连接网络的模块状态。

⑦ 状态指示灯：绿色指示灯，模块运行时会亮起。

⑧ 扩展引脚：更多细节参见引脚定义。

⑨ 标准 SIM 卡插槽。

⑩ 电源引脚：用于电源焊接和测试。

###   Pin 定义

<table >
<tr>
<th scope="col"> **丝印名称**
</th>
<th scope="col"> **I（输入）/O（输出）**
</th>
<th scope="col"> **描述**
</th>
<th scope="col"> **备注**
</th></tr>
<tr>
<th scope="row"> BAT
</th>
<td> I/0
</td>
<td> 电源输入/输出
</td>
<td> 3.4V - 4.4V DC
</td></tr>
<tr>
<td> GND
</td>
<td> I/0
</td>
<td> 电源地/逻辑地
</td>
<td>
</td></tr>
<tr>
<td> VIO
</td>
<td> I
</td>
<td> 逻辑参考电压
</td>
<td> 2.8V - 5.0V DC
</td></tr>
<tr>
<td> DTR
</td>
<td> I
</td>
<td> 睡眠模式控制引脚
</td>
<td> 高电平进入睡眠模式
</td></tr>
<tr>
<td> PWR
</td>
<td> O
</td>
<td> 电源开关
</td>
<td> 保持低电平 2s
</td></tr>
<tr>
<td> RI
</td>
<td> O
</td>
<td> 事件/消息引脚
</td>
<td>
</td></tr>
<tr>
<td> TXD
</td>
<td> O
</td>
<td> 发送数据
</td>
<td> SIM808 的 UART 输出
</td></tr>
<tr>
<td> RXD
</td>
<td> I
</td>
<td> 接收数据
</td>
<td> SIM808 的 UART 输入
</td></tr>
<tr>
<td> RST
</td>
<td> I
</td>
<td> 复位引脚
</td>
<td> 低电平有效
</td></tr></table>

###   LED 指示灯

<table >
<tr>
<th scope="col"> **LED 指示灯**
</th>
<th scope="col"> **状态**
</th>
<th scope="col"> **运行状态**
</th></tr>
<tr>
<th scope="row"> 操作指示灯（绿色）
</th>
<td> 熄灭
</td>
<td> SIM808 没有运行
</td></tr>
<tr>
<td>
</td>
<td> 点亮
</td>
<td> SIM808 正在运行
</td></tr>
<tr>
<th scope="row"> 网络知识灯（红色）
</th>
<td> 熄灭
</td>
<td> SIM808 没有运行
</td></tr>
<tr>
<td>
</td>
<td> 点亮 64ms / 熄灭 800ms
</td>
<td> SIM808 没有注册到网络
</td></tr>
<tr>
<td>
</td>
<td> 点亮 64ms / 熄灭 3000ms
</td>
<td> SIM808 注册到网络
</td></tr>
<tr>
<td>
</td>
<td> 点亮 64ms / 熄灭 300ms
</td>
<td> PPP GPRS 通信建立
</td></tr></table>

##    相关配件
---

除了天线，您还可能需要使用 LoNet 808 的以下配件。

<table>
<tr>
<td> <div class="center"><div class="floatnone">![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/Simcard.jpg)</div></div>
<div style="text-align: center;">用于 GSM/GPRS 通信的 SIM 卡 </div>
</td>
<td> <div class="center"><div class="floatnone">[![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/Battery_2200ma.jpg)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.33.76ae956LmbXn2&id=534229881706)</div></div>
<div style="text-align: center;"> 3.7V Li-ion 电池</div>
</td>
<td> <div class="center"><div class="floatnone">![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/Power_Converter.jpg)</div></div>
<div style="text-align: center;">DC/DC 电压转换器</div>
</td></tr>
<tr>
<td> <div class="center"><div class="floatnone">[![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/100cmUSBc.jpg)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.31.51f7113hrPKZJ&id=521385344999)</div></div>
<div style="text-align: center;"> MicroUSB 数据线</div>
</td>
<td> <div class="center"><div class="floatnone">[![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/USB_To_Uart_5V3V3.jpg)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.38dbca0cToa3YN&id=521795408834)</div></div>
<div style="text-align: center;"> USB 转 UART 工具</div>
</td>
<td> <div class="center"><div class="floatnone">[![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/3wsp.JPG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.22.3f8d5d43GiXwEf&id=533271154027)</div></div>
<div style="text-align: center;"> 3W 太阳能电池板 </div>
</td></tr>
</table>

##   使用方法
---
###   参考电路

**&gt; 与 MCU 连接**

![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/C1-01.png)

**&gt; 与电脑连接**

![](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/img/C2-01.png)

###   AT 指令入门指导

模块通过串口由 AT 指令控制，在这里我们使用 Arduino 作为 USB 转串口工具。上传下面的代码，然后打开串口监视器。如果您你使用其他的 USB 转串口工具，你可以使用 [AT Command Tester](/AT_Command_Tester_Application) 或者 [SSCOM32](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/res/Sscom32E.zip) 来测试 AT 指令。

```c
// this sketch is used for testing LoNet with Arduino

// Connect VIO to +5V
// Connect GND to Ground
// Connect RX (data into SIM808) to Digital 11
// Connect TX (data out from SIM808) to Digital 10

#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup()
{
    // Open serial communications and wait for port to open:
    Serial.begin(9600);
    mySerial.begin(9600);

}

void loop() // run over and over
{
    if (mySerial.available())
    Serial.write(mySerial.read());

    if (Serial.available())
    {
        while(Serial.available())
        {
            mySerial.write(Serial.read());
        }
        mySerial.println();
    }
}
```

####   设置波特率和使能充电功能

建议在第一次使用模块时执行此过程。在下表的“串口监视器”列中，AT 命令的输入指令为黑色，模块返回值为橙色。

<table cellpadding="0">
<tr>
<th scope="col" width="50"> 串口监视器
</th>
<th scope="col" width="100"> 描述
</th></tr>
<tr>
<td> AT
<span style="color: rgb(242,133,0)">OK</span> </td>
<td> 发送命令 **AT** 来同步波特率。模块的串口默认设置为自动波特率模式，在此模式下，模块打开时不会有任何输出。
</td></tr>
<tr>
<td> AT+IPR=9600
<span style="color: rgb(242,133,0)">OK</span></td>
<td> 设置波特率为 9600bps, 支持的波特率范围为 1200bps 到 115200bps。
</td></tr>
<tr>
<td> AT+ECHARGE=1
<span style="color: rgb(242,133,0)">OK</span></td>
<td> 发送指令 **AT+ECHARGE=1** 来开启电池充电功能。该功能默认是关闭的。
</td></tr>
<tr>
<td> AT&amp;W
<span style="color: rgb(242,133,0)">OK</span></td>
<td> 保存参数设置。
</td></tr>
<tr>
<td> AT+CPOWD=1
<span style="color: rgb(242,133,0)">NORMAL POWER DOWN</span></td>
<td>关闭模块电源
</td></tr>
<tr>
<td> <span style="color: rgb(242,133,0)">RDY
+CFUN: 1
GPS Ready
+CPIN: READY
Call Ready
SMS Ready</span></td>
<td>按电源按键重新打开模块，它会返回 GPS 和 GSM 的状态信息。
</td></tr>
<tr>
<td> AT+CBC
<span style="color: rgb(242,133,0)"> +CBC: 1,96,4175
 OK</span></td>
<td>查询电池状态和剩余电量信息。
</td></tr>
<tr>
<td> AT+CSQ
<span style="color: rgb(242,133,0)"> +CSQ: 14,0
 OK</span></td>
<td>Inquire GSM signal quality.查询 GSM 信号质量。
</td></tr>
</table>

####   使用 GPS 获取位置信息

<table cellpadding="0">
<tr>
<th scope="col" width="11"> 串口监视器
</th>
<th scope="col" width="700"> 描述
</th></tr>
<tr>
<td> AT+CGPSPWR=1
<span style="color: rgb(242,133,0)">OK</span> </td>
<td> 打开 GPS
</td></tr>
<tr>
<td> AT+CGPSSTATUS?
<span style="color: rgb(242,133,0)"> +CGPSSTATUS: Location Not Fix
OK</span></td>
<td> 获取 GPS 定位状态，**Location Not Fix** 意味着定位不成功。第一次开始时至少需要 30 秒。**GPS 必须伸出窗户或在室外进行测试**。
</td></tr>
<tr>
<td> AT+CGPSSTATUS?
<span style="color: rgb(242,133,0)"> +CGPSSTATUS: Location 3D Fix
OK</span></td>
<td> GPS 已经确定了 3D 位置。
</td></tr>
<tr>
<td> AT+CGPSINF=0
<span style="color: rgb(242,133,0)"> +CGPSINF:
 0,2234.931817,11357.122485,
92.461185,20141031041141.000,
88,12,0.000000,0.000000 </span></td>
<td> 获取当前的GPS位置信息。参数有：&lt;mode&gt;, &lt;altitude&gt;, &lt;longitude&gt;, &lt;UTC time&gt;, &lt;TTFF&gt;, &lt;num&gt;, &lt;speed&gt;, &lt;course&gt;
</td></tr>
<tr>
<td> AT+CGPSOUT=32
<span style="color: rgb(242,133,0)">OK
$GPRMC,043326.000,A,
2234.9414,N,11357.1187,E,
0.000,143.69,311014,,,A*50 </span></td>
<td> 读取 NMEA $ GPRMC 数据，其中“2234.9414 N，11357.1187 E”是位置坐标。有关 NMEA 的更多细节，请 [点击这里](http://www.gpsinformation.org/dale/nmea.htm)。
</td></tr>
<tr>
<td> AT+CGPSRST=0
<span style="color: rgb(242,133,0)"> OK</span></td>
<td>重启 GPS 为 Cold Start Mode.
</td></tr>
<tr>
<td> AT+CGPSRST=1
<span style="color: rgb(242,133,0)"> OK</span></td>
<td>重启 GPS 为 Hot Start Mode.
</td></tr>
<tr>
<td> AT+CGPSPWR=0
<span style="color: rgb(242,133,0)"> OK</span></td>
<td> 关闭 GPS.
</td></tr>
</table>

##   资源下载
---
*   **[PDF 文件]**[LoNet_808_Schematic](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/res/LoNet_808_Schematic.pdf)
*   **[指令手册]**[SIM800_ATCommand_Manual](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/res/SIM800_ATCommand_Manual_V1.02.pdf)
*   **[硬件手册]**[SIM808_HardwareDesign_Manual](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/res/SIM808_Hardware_Design_V1.00.pdf)
*   **[GPS 应用手册]**[SIM808_GPSApplication_Note](https://github.com/SeeedDocument/LoNet_808-Mini_GSM_GPRS_Plus_GPS_Breakout/raw/master/res/SIM808_GPS_Application_Note_V1.00.pdf)
*   **[GPRS_Shield 库]**[GPRS_Shield library on gitHub](https://github.com/Seeed-Studio/GPRS_Shield_Suli)
*   **[GSM Breakout 库]**[Adafruit_FONA_Library](https://github.com/adafruit/Adafruit_FONA_Library/)
