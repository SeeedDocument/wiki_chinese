---
title: Xadow GPS V2
category: Rephone
bzurl: https://www.seeedstudio.com/Xadow-GPS-v2-p-2557.html
oldwikiname: Xadow GPS V2
prodimagename: Xadow_GPS_v2.JPG
wikiurl: http://seeed.wiki/Xadow_GPS_V2
sku: 113040009
---

---
![](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/images/Xadow_GPS_v2.JPG)

Xadow GPS v2 内置 Quectel® 的 GPS L70 模块，并且将先进的 AGPS 技术 EASYTM(Embedded Assist System)与 AlwaysLocateTM 技术相结合，从而获得更好的性能、更低的能耗以及更快的定位效果（即使是处于室内也能检测到）。Xadow GPS v2 还内置了高灵敏度的信号接收器（-163dBm 的探测效果）和一个内置的芯片天线。因此，这个产品能够在 66 个频道搜寻到多达 22 个定位卫星的信号，这些特点让这个产品成为你开发导航设备的关键选择。Xadow GPS v2 还采用了 11 个引脚的 Xadow 接口，来方便与其他模块进行快速连接。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4d812959DUmERG&id=535921210124)

## 产品特性
---

- 采用EASY™，先进的AGPS技术，而不需要外部存储器
- 具备超低功耗的搜寻模式
- 采用AlwaysLocate™，一款可选择工作模式的智能控制器
- 高灵敏度
- 支持QZSS
- 支持 DGPS，SBAS（WAAS / EGNOS / MSAS / GAGAN）
- Anti-Jamming, Multi-tone 有源干扰抵消器
- 内置芯片天线，效率高达 83％
- 配备 11 个引脚 Xadow 连接口，可以与其他 Xadow 模块方便的进行连接
- 可叠加使用，连接或焊接到其他Xadow模块上。

## 规格参数
---

|项目|参数|
|---|---|
|**微控制器**|	Kinetis KL02|
|**内核**|	ARM® 32-bit Cortex® -M0+CPU|
|**输入电压**	|3.3 ~ 6 V (通过扩展板的引脚输入)|
|**Flash**|	32 KB|
|**SRAM**|	4 KB
|**时钟频率**|	48 MHz
|**功耗**	|跟踪时 18ma，捕获时 21mA
|**省电模式**|	典型值：3mA@AlwaysLocateTM, 7uA@Backup<br>Mode, 180uA@Standby Mode
|**频道**|	22(跟踪时) / 66 (捕获时)
|**更新频率**|	1Hz(默认), 最大 10Hz
|**水平位置精度**|	<2.5m CEP
|**速度精度**|	<0.1m/s
|**最大速度**|	最大 515m/s
|**EASYTM 冷启动/热启动时间**|215s/5s
|**捕获灵敏度**|-145dBm
|**跟踪灵敏度**|	-163dBm
|**工作温度**|-40℃ to 85℃
|**NMEA 协议**|0183/PMTK
|**天线类型**|	芯片天线
|**接口**|	通过 I2C (7-bit 地址 0x05) 与 Xadow GSM+BLE 连接
|**尺寸**|	25.37mm X 20.30mm / 1” × 0.8”

## 硬件概览
---
![](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/images/Xadow_GPS_v2.png)

## 关于全球定位系统（GPS）
---
全球定位系统（GPS）是一种基于空间的导航系统，可以提供实时和全天候的地理位置，高度，行驶速度和时间信息，无论在地球上还是在地球附近，都可以在无障碍环境下找到至少 4 颗 GPS 卫星。它以前只用于军事项目，现在任何人都可以免费使用 GPS 接收机。GPS 的典型应用包括汽车导航，时间转换，交通信号定时，防盗和跟踪装置等。

## Rephone Community
---
[![](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/images/300px-RePhone_Community-2.png)](http://www.seeed.cc/discover.html?t=RePhone)

We’ve been looking for a better place where our backers (RePhone Users) can sit together, warmly and comfortably, have conversations about RePhone, discuss technical problems, share ideas/projects, and give feedback on the modules’ development in the future. And then here we go, the [RePhone Community](http://www.seeed.cc/discover.html?t=RePhone).

Now join us in the [RePhone Community](http://www.seeed.cc/discover.html?t=RePhone)! Together we seek answers, make interesting stuff, care about each other, and share our experiences.

**Frequently Asked Questions**

Some frequently asked questions in [RePhone Community](http://www.seeed.cc/discover.html?t=RePhone) are collected and answered to the topic "Frequently Asked Questions of RePhone (FAQ)" , the topic will be kept updating whenever a new FAQ comes out.

## 资源下载
---

- **[代码]**[Source Code for Xadow GPS v2](https://github.com/WayenWeng/Xadow_GPS_v2/)
- **[代码]**[Testing Code for Xadow GPS v2 based on Eclipse IDE](https://github.com/WayenWeng/Xadow_GPS_v2_test/)
- **[原理图]**[Xadow GPS v2 Schematic Files](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/resources/202000729_PCBA%3BXadow%20GPS%20v2.1_schemic%20file.zip)
- **[入门指南]**[Learn how to burn new firmware with a mbed board](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/resources/Burn_to_Xadow_modules.zip)
- **[数据手册]**[Specification for GPS L70 and the chip antenna](https://github.com/SeeedDocument/Xadow_GPS_V2/raw/master/resources/GPS_L70_%26_Chip_Antenna.rar)
