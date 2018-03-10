---
title: GPRS Shield V3.0
category: Shield
bzurl: https://www.seeedstudio.com/GPRS-Shield-V3.0-p-2333.html
oldwikiname:  GPRS Shield V3.0
prodimagename:
wikiurl: http://wiki.seeedstudio.com/cn/GPRS_Shield_V3.0
sku:  113030009
---

![](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/img/GPRS_Shield_V3.0_p1.jpg)


这是 GPRS Shield 的 3.0 版本。
您可以用 GPRS Shield 把您的 Arduino 连接到 GSM/GPRS 手机网络！您可以使用您的 Arduino/Seeeduino 或其他主板拨打电话号码或通过简单易用的 AT 命令发送短信给您的朋友。GPRS Shield 采用四频低功耗 GSM/GPRS 模块 SIM900 以及紧凑型 PCB 天线，同时对接口和基本电路进行了改进，使其更加简洁可靠。有两种选择让您将 GPRS Shield 与主板（通过 UART 或 SoftwareSerial 软件串口）进行通信。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1a9a282fzZYsJx&id=520532640849)

##  版本
---
| 版本 | 描述                                              | 发布时间      |
|----------|-----------------------------------------------------------|--------------|
| v0.9b    | 首次公开发布（测试版）                             | 2011年 3 月 3 日 |
| v1.2     | 添加了软件端口以开启/关闭 SIM90             | 2011 年 12 月 2 日  |
| v1.4     | 重新设计电源电路，重新铺设 PCB 布局          | 2012 年 8 月 30 日 |
| v2.0     | 支持四频段和重新设计 PCB 天线               | 2013 年 2 月 3 日  |
| v3.0     | 将 arduino 插口更改为最新的 Arduino Uno 标准  | 2015 年 3 月 20 日 |

**V3.0 版本与之前版本的区别**

 - 更换了板子上的 Arduino 插槽为最新的 Arduino Uno 标准。除此之外没有改变。

!!!Caution
* 确保您的 SD 卡是激活的可以正常使用。
* GPRS Shield 不带 ESD（静电） 防护措施。在干燥的天气下使用时要格外小心。

##  硬件概述
---
![](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/img/Gprs_shield_v3_layout1.png)

请参考 [GPRS Shield V2.0](http://wiki.seeed.cc/GPRS_Shield_V2.0/) 来获得规格说明和应用指南。


##  Resources

- **[Eagle 文件]** [GPRS Shield v3.0 Schematic and PCB in eagle format](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/GPRS_Shield_V3.0_sch_pcb.zip)
- **[PDF 文件]** [GPRS Shield v3.0 Schematic in PDF format](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/GPRS_Shield_v3.0%20sch.pdf)
- **[PDF 文件]** [GPRS Shield v3.0 PCB in PDF format](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/GPRS%20Shield%20v3.0%20PCB.pdf)
- **[库文件]** [GPRS_Shield library on gitHub - based on Suli](https://github.com/Seeed-Studio/GPRS_Shield_Suli)
- **[库文件]** [GPRS_SIM900 library on gitHub - Non Suli ](https://github.com/Seeed-Studio/GPRS_SIM900)
- **[指令文档]** [AT Commands v1.11](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/AT_Commands_v1.11.pdf)
- **[硬件文档]** [SIM900 Hardware Design](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/SIM900_HD_V1.05.pdf)
- **[数据手册]** [Si5902BDC](http://www.vishay.com/docs/70415/si5902bd.pdf)
- **[数据手册]** [SIM900 Datasheeet](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/SIM900datasheeet.zip)
- **[数据手册]** [SIM_900_AGPS_instructions](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/SIM_900_AGPS_instructions.zip)
- **[工具]** [SIM900 firmware and tool(firmware:1137B08SIM900M64_ST)](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/1137B08SIM900M64_ST.zip)
- **[工具]** [SIM900 firmware and tool(firmware:1137B13SIM900M64_ST)](https://github.com/SeeedDocument/GPRS_Shield_V3.0/raw/master/res/1137B13SIM900M64_ST.zip)
