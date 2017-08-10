---
title: 2KM Long Range RF link kits w/ encoder and decoder
category: MakerPro
bzurl: https://www.seeedstudio.com/2km-long-range-rf-link-kits-w-encoder-and-decoder-p-321.html?cPath=139_140
oldwikiname:  2KM Long Range RF link kits w/ encoder and decoder
prodimagename:  2kmrf.jpg
wikiurl: http://seeed.wiki/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder
sku:   113990018
---
##  1.	简介

![](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/img/2kmrf.jpg)

这是一款超长距离的433MHz RF通信模块套件，通信距离可达2公里，包含发射和接收两个模块。模块内置VCO, PLL技术，频率稳定以及抗干扰能力强。你可以在需要无线数据传输和远程控制等应用使用本模块。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5e478797pm0Yu9&id=527004631129)

##   2.	规格参数
---
| 参数         | 值                       |
|--------------|--------------------------|
| 工作电压     | 接收器：3~5V，发射器3~9V |
| 工作电流     | ≤2.5mA（@5V）            |
| 工作原理     | "超外差（VCO,PLL)        |
| 调制方式     | OOK/ASK                  |
| 工作频段     | 433.92MHz                |
| 带宽         | 1.5MHz                   |
| 灵敏度       | -105dBm(50Ω)             |
| 解码方式     | PT2272                   |
| 天线长度     | 18cm                     |
| 最大通信距离 | 2Km                      |

##   3. 创意应用
---
*   无线开关
*   远程传输
*   无线控制

##   4. 硬件概述
---
![](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/img/433rf5.png)

![](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/img/433rf6.png)

##  5.入门指导
---

- 请根据以下 [流程](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/res/2KM_RF.rar) 来搭建系统.
- 连接电池, 按钮和发射板.
![](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/img/2KM_TX.JPG)

!!!note
    - 请使用3-5V电源！ 9V电源会损坏接收板.
    - 连接电池, LEDs and 接收板.
![](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/img/2KM_RX.JPG)

!!!warning
    - 不要把RX 模块和 TX模块靠的很近: 这将阻止他们正常工作。 确保RX模块和TX模块距离至少1米。
    - 当我们按发射机侧的按钮时，接收机侧的相关LED将被打开。

## 6. 资源
---
- **[流程]**   [Transmitter and receiver Setup Manual](https://github.com/SeeedDocument/2KM_Long_Range_RF_link_kits_w_encoder_and_decoder/raw/master/res/2KM_RF.rar)

- **[数据手册]**   [Datasheet for PT2272 and PT2262](http://www.datasheetcatalog.org/datasheet/PrincetonTechnologyCorporation/mXusxsq.pdf)
