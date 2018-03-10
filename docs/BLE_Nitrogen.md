---
title: BLE Nitrogen
category: Wireless
bzurl: https://www.seeedstudio.com/BLE-Nitrogen-p-2711.html
oldwikiname:
prodimagename: cover.png
wikiurl: http://wiki.seeedstudio.com/cn/BLE_Nitrogen
sku: 102990629
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/cover.png)

Zephyr 使用 nrf52_nitrogen 配置来实现在 nRF52 上运行。它提供对 Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU 和以下配置的支持 :

* NVIC (Nested Vectored Interrupt Controller)
* SYSTICK (System Tick System Clock)
* UART
* GPIO
* FLASH

本 [Nordic Semiconductor Infocenter](http://infocenter.nordicsemi.com/) 包含处理器信息和数据手册。

强烈建议您使用最新的 [SDK](https://www.zephyrproject.org/downloads/tools) 更新开发环境。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.1.e1c48f5f05C2v&id=548128604806&ns=1&abbucket=1#detail)


## 产品特性

* 具有 512kB Flash，64kB RAM 的 nRF52832 微控制器
    * Cortex M4
    * BLE
    * NFC
* 带电流保护的 USB 电源
* 电池用电管理
    * 板载充电器
    * 电池插头
    * 充电 LED 指示灯
* LPC11U35 板载 SWD 调节器
    * SWD 调节器
    * USB 至 Uart
    * Drag and Drop 固件升级
    * 固件升级后自动重置并运行
* BLE 功耗测量
    * On board 电流测量电路
    * 1uA 测量范围
    * 高达 150mA 电流测量
* 7 LEDs
    * USR1, BT, PWR, CDC, DAP, MSD, Battery charge
* 两个按钮
    * USR 和 RESET(也用于 LPC11U35 固件升级)
* SWD 调试连接器
    * nRF52832 SWD 连接器
    * nRF52832 Uart 连接器
* 板载芯片天线
* 1.8V 工作电压
* 2x20 间距 2.0mm 引脚
* 完全兼容 96Boards IoT 标准


## 规格参数


| 项目 | 参数 |
|-----------|-------|
|芯片	|nRF52832 |
|时钟频率 |	64MHz|
|Flash|	512KB|
|SRAM|	96KB|
|数字输出电压	|1.8V|
|模拟引脚数量|	4|
|模拟输入电压	|1.8V|
|尺寸|	60x30mm|

## 硬件概述

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/hardware_ov.png)

1.**Micro USB** - 用于调试，编程，供电和电池充电。

2.**LED 指示灯**

* ***USR1*** - 用户控制 led，连接到 **P0.29**
* ***BT***  - 蓝牙指示器。连接到设备时此指示灯亮起。
* ***PWR*** - USB 或电池插入时亮起。
* ***CDC*** - Uart 数据指示灯。
* ***DAP*** - SWD 指示灯。
* ***MSD*** - 大容量存储/Drag&Drop 指示灯。

3.**电池连接器**

* **充电指示灯**
    * BLINK: 无电池接入
    * ON: 充电中
    * OFF: 充电完成

4.**重置按钮** - 按下以重置系统

5.**用户按钮** - 连接到 **P0.27**

6.**UART 调试**

7.**天线**

8.**NFC 天线 UFL 连接头**

9.**引脚** 详见引脚图

A.IC - **NRF52832**

B.IC - **LPC11U35**

C.IC - **ETA6003**

## 引脚图


[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/pin_map.png)](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/pin_map.png)

!!!Note
    点击上图查看大图

## 软件

### 安装驱动

点击下载 [driver for Mbed](https://developer.mbed.org/media/downloads/drivers/mbedWinSerial_16466.exe).

通过 micro USB 电缆将板插入 PC，双击 mbedWinSerial_16466.exe 进行安装，然后在设备管理器中找到新的设备。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/install_driver.png)

### 高级功能指南

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/BLE-Nitrogen/master/img/guide.png)](https://www.zephyrproject.org/)


## 资源下载


**[原理图]** [Schematics in Eagle File](https://github.com/SeeedDocument/BLE-Nitrogen/raw/master/res/BLE_Nitrogen_Eagle_File%20V1.1.zip)

**[原理图PDF]** [Schematics in PDF](https://github.com/SeeedDocument/BLE-Nitrogen/raw/master/res/BLE%20Nitrogen%20v1.1%20Sch.pdf)

**[驱动下载]** [Driver for Mbed](https://developer.mbed.org/media/downloads/drivers/mbedWinSerial_16466.exe)
