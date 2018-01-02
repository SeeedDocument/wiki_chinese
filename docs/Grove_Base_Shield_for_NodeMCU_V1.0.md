---
title: Grove Base Shield for NodeMCU V1.0
category: Shield
bzurl: https://www.seeedstudio.com/Grove-Base-BoosterPack-p-2177.html
oldwikiname:  Grove Base Shield for NodeMCU V1.0
prodimagename: Base_Shield_for_NodeMCU1.jpg
wikiurl: http://seeed.wiki/Grove_Base_Shield_for_NodeMCU_V1.0
sku:  105020008
---
![](https://github.com/SeeedDocument/Grove_Base_Shield_for_NodeMCU_V1.0/raw/master/img/Base_Shield_for_NodeMCU1.jpg)

NodeMCU 的 Grove Base Shield 是一个扩展板，可以让您使用 NodeMCU 的 ESP8266 WIFI 开发套件中的 Grove 传感器。您可以在 NodeMCU 固件中使用 Lua 脚本语言来使用 Grove 传感器。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.1e96ec99exzogP&id=531812790616)

##   产品特性
---
*   兼容所有Grove模块

*   5 个数字接口 (D3-D8)

*   1 个模拟接口 (A0)

*   2 I2C 接口

*   没有 SPI 接口

*   UART/D9-D10 接口

*   有电源指示 LED

##   接口功能
---

Grove Base Shield 的目的是把任何微控制器的输入和输出引脚简单的连接到 Grove 模块。下图是扩展板的实物图。

![](https://github.com/SeeedDocument/Grove_Base_Shield_for_NodeMCU_V1.0/raw/master/img/Base_Shield_for_NodeMCU2.jpg)

!!!Note
    1. 引脚会在不同的接口被重复使用 - 即 D3 插座含有 D3 和 D5，D5 插座含有 D5 和 D6，下一个插座含有 D6 和 D7 等等。
    2. 扩展板上没有 D4 插座。
    3. UART 接口可以与 D9，D10 端口复用，I2C 接口可以与 D1，D2 端口复用。
    4. 同时使用 4 个 I2C 插槽是不会发生冲突的，因为每个 I2C 器件都有自己的地址。
    5. 由于 Grove 模块都没有使用 SPI 接口，所以本扩展板上也没有 SPI 插座。

##  资源下载
---
- **[Eagle 文件]**[Grove Base Shield for NodeMCU_sch Eagle file](https://github.com/SeeedDocument/Grove_Base_Shield_for_NodeMCU_V1.0/raw/master/res/Grove_Base_Shield_for_NodeMCU_sch_pcb.rar)
- **[PDF 文件]**[Grove Base Shield for NodeMCU v1.0.pdf](https://github.com/SeeedDocument/Grove_Base_Shield_for_NodeMCU_V1.0/raw/master/res/Grove_Base_Shield_for_NodeMCU_pdf_v1.0.rar)
