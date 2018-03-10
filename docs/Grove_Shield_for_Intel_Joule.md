---
title: Grove Shield for Intel Joule
category: Others
bzurl: https://www.seeedstudio.com/Grove-Button-p-766.html
oldwikiname:
prodimagename: 3.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Shield_for_Intel_Joule/
sku: 103030095
---


![](https://github.com/SeeedDocument/Grove_Shield_for_Intel_Joule/blob/master/img/1.jpg?raw=true)

在 2016 年英特尔开发者论坛上，英特尔宣布推出了 Joule 模块，该模块是提供高计算能力，RAM 和存储的 Linux 系统模块。 该 Grove Shield 使强大的英特尔 JouleTM 增加了 Grove 模块系列接口，它旨在帮助创作者和 IoT 开发人员更方便快捷地创建项目。

通过简单地将其插入到 Joule board 上，它将拥有 8 个坚固易用的 Grove 连接器，其中包括接口，如I2C，UART，digital I/Os 和 模拟输入。 除了丰富的 Grove 连接器外，它还保留有 2x20 针头来应对您想要更多的 GPIO 用于项目。 板上的集成开关允许您选择 5V 或 3.3V 的工作电压。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.57dd0641qz6eDH&id=548191790361)

## 产品特性

- 接口 : 8 个 Grove 接口

- 即插即用

- 接口详细信息 : I2C x 3, UART x 1, 数字 x 2, 模拟 x 2

- 工作电压 : 5V/3.3V

- 用于选择工作电压的开关。

- 4 通道模拟接口，分辨率: 12 位

- 工作温度 : -40 - 85℃

- 尺寸 : 84.9*51.7mm

## 硬件概述

![](https://github.com/SeeedDocument/Grove_Shield_for_Intel_Joule/raw/master/img/Grove%20Shield%20for%20intel%20Joule%20Pin.png)

- Grove Analog 端口 : ⑥/⑨

- Grove Digital 端口 : ⑧/⑩

- Grove UART 端口 : ⑦

- Grove I2C 端口 : ③/④/⑤

- [Intel Joule 的 1 / J12 裸板 : ①](http://www.intel.com/content/www/us/en/support/boards-and-kits/000022494.html)

- [Intel Joule 的 2 / J13 裸板 : ②](http://www.intel.com/content/www/us/en/support/boards-and-kits/000022494.html)

- 3.3V & 5V 电源开关 : ⑪

### 引脚对引脚图
|Grove Shield 连接器/引脚|SOC (电路图) 信号|TuChuck 连接器/引脚
|:---:|:---:|:---:|
|J1|Breakout1|J12|
|J2|Breakout2|J13|
|J3-1|I2C_0_SCL_H|J12-13|
|J3-2|I2C_0_SDA_H|J12-11|
|J4-1|I2C_1_SCL_H|J13-33|
|J4-2|I2C_1_SDA_H|J13-31|
|J5-1|I2C_2_SCL_H|J13-37|
|J5-2|I2C_2_SDA_H|J13-35|
|J6-1|AIN2|/|
|J6-2|AIN3|/|
|J7-1|UART_0_TXD|J12-7|
|J7-2|UART_0_RXD|J13-28|
|J8-1|Digital_1_PWM_0|J12-26|
|J8-2|Digital_1_PWM_1|J12-28|
|J9-1|AIN0|/|
|J9-2|AIN01|/|
|J10-1|Digital_2_PWM_2|J12-30|
|J10-2|Digital_2_PWM_3|J12-32|


!!!Note
    * 当您插上 shield 时，请注意方向。
    * Libmraa 暂时不支持 Joule 的 UART 引脚。 所以 UART 接口不可用。

## 资源下载

* **[Eagle文件]** [Grove Shield for Intel Joule Schematic files](https://github.com/SeeedDocument/Grove_Shield_for_Intel_Joule/tree/master/res)
