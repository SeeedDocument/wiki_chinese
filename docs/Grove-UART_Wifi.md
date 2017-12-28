---
title: Grove - UART Wi-Fi
category: Communication
bzurl: https://www.seeedstudio.com/Grove-Uart-Wifi-p-2495.html
oldwikiname:
prodimagename: Grove-uart-wifi-01.jpg
wikiurl: http://seeed.wiki/Grove-UART_Wifi/
sku: 113020010
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove-uart-wifi-01.jpg)

Grove - UART WiFi 是一种串行收发器模块，具有无处不在的 ESP8266 IoT SoC 。 通过集成的 TCP / IP 协议栈，只需几行代码，该模块就可让您的微控制器与 WiFi 网络交互。 每个 ESP8266 模块都使用 AT 命令集固件进行预编程，这意味着您可以发送简单的文本命令来控制设备。 SoC 功能集成的 WEP，WPA / WPA2，TKIP，AES 和 WAPI 引擎，可以充当 DHCP 的接入点，可以加入现有的 WiFi 网络，并具有可配置的 MAC 和 IP 地址。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=527702274067&ali_refid=a3_430582_1006:1121643831:N:grove:4f6e693d96f030e12fcc71d7c48c539a&ali_trackid=1_4f6e693d96f030e12fcc71d7c48c539a&spm=a230r.1.14.6.6f58defaT8cqmN#detail)

## 产品特性

* Grove 4 引脚连接器（RX，TX，VCC，GND）
* 802.11 b / g / n 协议（2.4GHz）
* WiFi Direct（P2P），soft-AP
* 支持AP，STA 和 AP + STA 共存模式三种模式
* 集成 TCP / IP 协议栈
* LwIP （轻量 IP ）
* 集成的低功耗 32 位 CPU 可以作为应用处理器进行重新编程
* 集成温度传感器
* 串行 UART 接口
* 多队列 QoS 管理
* 在 <2ms 内能够激活并发送数据
* 金属屏蔽
* 板上陶瓷天线
* 重置开关

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

## 硬件概述

以下是 Grove-UART WiF 模块的框图，该模块由以下部分组成。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_wiki_hardware_overview.jpg)


* Grove - 用于通过板上的接口将（如 Seeeduino 或 Grove Base Shield ）连接到处理器。
* WiFi 天线 - ESP8266 天线（模块型号）
* 按钮 - 具有多功能
     * 重置 - 按下并快速释放。
     * 将 ESP8266 （模块型号）设置为 UART 引导模式 - 按住按钮，直到中间红色的 LED 指示灯亮起。
* LED 指示灯 - 用于指示用户的工作状态和操作。
     * 左 - 蓝色 LED 指示灯 - 由用户通过命令“ AT + LEDON ”和“ AT + LEDOFF ”控制。
     * 中间 - 红色 LED 指示灯 Wifi 连接时或进入 UART 启动模式时亮起
     * 右 - 绿色 LED 指示灯上电时亮起。

## 规格参数

* 输入电压：3V / 5V
* 波特率：115200
* 基于 ESP8266 ESP-06 SoC
* AT 固件： esp_iot_sdk_v1.1.0 + Seeed 修改：
     * 2x 附加 AT 命令控制蓝色 Link LED 。
     * 注册红色 WiFi LED 到 ESP8266 wifi 状态 LED 。
* AT 命令集
* SDIO 1.1 / 2.0，SPI，UART
* 五个电源状态： OFF，DEEP_SLEEP，SLEEP，WAKEUP 和 ON。
* 待机功耗 <1.0mW（DTIM = 3）
* 集成 TR 开关，平衡 - 不平衡变压器，LNA ，功率放大器和匹配网络
* 集成 PLL ，稳压器， DCXO 和电源管理单元
* 802.11b 模式下输出功率为 + 19.5dBm
* 断电时漏电流 <10uA
* CCMP 硬件加速器（ CBC-MAC ，计数器模式）， TKIP（MIC，RC4），WAPI（SMS4），WEP（RC4），CRC
* WPA / WPA2 PSK 和 WPS 驱动程序
* A-MPDU 和 A-MSDU 聚合和 0.4ms 保护间隔
* 尺寸：25.43mm x 20.35mm

## 超低功耗技术

ESP8266 旨在通过专门的电源管理技术实现非常低的能耗，减少非必要功能并调节睡眠模式。 有五个电源状态：

* 关机
* 深度休眠 - 实时时钟运行，但芯片的所有其他部分都关闭
* 休眠 - 仅实时时钟和看门狗运行时消耗小于 12uA 。 芯片将在 MAC ，主机，RTC 或外部中断唤醒。
* 开机 - 系统正在从睡眠状态变为开状态。 晶振和 PLL 使能。
* 使用中 - 消耗小于 1.0mW （DTIM = 3）或 0.5mW （DTIM = 10）。

实时时钟可以编程为在指定的时间内唤醒 ESP8266 。

DTIM 周期越长，设备可能会睡眠的时间越长，因此设备可能会节省更多的电力。

为了满足移动应用和可穿戴电子设备的电源要求，为了降低总体功耗，可以在固件中定制 PA 输出功率。



## 创意应用

* 家庭自动化
* 传感器网络
* 网状网络
* 可穿戴电子产品
* 婴儿监视器
* 网络摄像机
* 工业无线控制
* WiFi 信标
* 智能电源插头
* 位置感知应用程序

## 入门

在此部分之后，您可以使 **Grove - UART WiFi**  仅运行几步。

### 准备工作

现在我们进行无线接入点（AP）扫描的演示，这需要以下模块。

* [Seeeduino Lite](http://www.seeedstudio.com/depot/Seeeduino-Lite-p-1487.html?cPath=6_7)
* [Grove - OLED Display 1.12](http://www.seeedstudio.com/depot/Grove-OLED-Display-112-p-781.html?cPath=34_36)

如果这是你第一次使用 [Seeeduino Lite](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.785a284cYtXcvB&id=45487750521), 请参考 [Seeeduino Lite's wiki](https://seeeddoc.github.io/Seeeduino_Lite)

Seeeduino Lite 与 Arduino 兼容，且与 Arduino 一样简单。

如果你是第一次使用 Arduino, 请点击 [这里](http://arduino.cc) 开始你的  Arduino 的体验。

### 连接硬件

[Seeeduino Lite](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.785a284cYtXcvB&id=45487750521) 使用 Grove 端口连接上述两个模块：Grove - [OLED Display 1.12](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.73a10590K1ZmeC&id=531865752955) 和 [Grove - Uart Wi-Fi](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.36.7e7975c1PHslwB&id=527702274067).

分别是：

* Grove - OLED 显示屏 1.12 ——I2C连接端口
* Grove - UART Wifi ——串口连接端口
* 如下所示：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_connect.jpg)

### 下载

点击 [这里](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/res/Grove_uart_wifi_test.zip) 以下载测试代码并将其解压缩到任何文件夹（例如驱动器 D 或桌面）


现在你需要配置Arduino的 [sketchbook](https://seeeddoc.github.io/How_To_Use_Sketchbook/) .

启动 Arduino IDE ，然后单击文件>首选项，并在 Sketchbook 位置添加下载测试代码的绝对位置。

![在此输入图像说明](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_wiki_sketchbook.png)

配置完成后，请重新启动 Arduino ，单击 **File（文件）>  Sketchbook** ，然后选择 grove uart wifi wiki ，之后将显示测试代码。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_wiki_sketchbook2.png)

单击 **Tools（工具）>bord（板）** 选择 Seeeduino Lite 并选择相应的串行端口。

现在点击上传（CTRL + U）刻录测试代码。 请参考这里的任何错误提示，您也可以在论坛上添加评论


### 审查结果

上传完成后，您可以在 OLED 显示屏上看到 AP 标识符。以下 AP 标识符在我们的 Office 中。

![在此输入图像说明](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_result.jpg)

## 固件升级

我们的模块板可以通过刻录一个固件进行初始化设置，如果你喜欢，也可以刻录其他固件。点击 [这里](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/res/Grove-Uart_Wifi_Firmware-code.zip) 下载出厂设置固件的源代码。

### 准备工作

* 固件更新需要 USB 串口转换器，如果您不知道从哪里获取，可以选择我们提供的 UartSBee V5 。
* 需要一个 Grove-Jump 转换线，我们也提供出售。 点击 [这里](https://item.taobao.com/item.htm?spm=686.1000925.0.0.42953ff6Mx3LsQ&id=45840042878&qq-pf-to=pcqq.c2c) 查看。
* 需要使用微型 USB 数据线。

### 连接硬件

**1.** 将 Grove-Jump 转换连接线的一端与 Grove-Uart Wifi 上 的 Grove 端口连接，并将 UartSBee V5 的另一端连接如下。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_connect.jpg)

**2.** 然后连接线如下图所示：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_connect2.jpg)

### 下载刻录工具

* [FLASH DOWNLOAD TOOLS](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/FLASH_DOWNLOAD_TOOLS_v1.2_150512.zip)
* [Bin files of firmware](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/Grove-uart-wifi-firmware-bin.zip)

### 操作步骤

现在确保您已经下载了刻录软件和固件的 bin 文件。 让我们开始刻录板子。

* 按住按钮，直到红色 LED 指示灯亮起，表示已准备好刻录固件。
* 在 FLASH 中启动可执行文件下载工具文件（双击）进行如下配置：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools1.jpg)

**1.** 从下载的固件 bin 文件中选择所需的文件。

**2.** 检查 SpiAutoSet 。

**3.** 选择相应的 COM 端口和 BAUDRATE 。

### 单击开始刻录固件

* 进度条将在固件刻录过程中显示。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools2.1.jpg)

* 最后，完成固件刻录。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools3.jpg)

## AT 命令

使用 Espressif 系统 ESP8266 AT 指令集版本 0.24 与 SeeedStudio 添加。

### 基本 AT 命令

|  命令| 说明|
|-------------|---------------|
|AT	|测试 AT 启动|
|AT+RST|	重新启动模块|
|AT+GMR|	查看版本信息|
|AT+GSLP|	进入深度睡眠模式|
|ATE|启用/禁用 AT 命令 echo |
|AT+RESTORE|	出厂复位|
|AT+UART|	UART 配置（已弃用）|
|AT+UART_CUR|	UART 当前配置（不会保存到 Flash ）|
|AT+UART_DEF| UART 默认配置（保存到 Flash ）|
|AT+SLEEP	|睡眠模式|
|AT+RFPOWER|	设置射频发射功率 |
|AT+RFVDD|	 根据 VDD33 设置射频发射功率|

### WiFi AT 命令

|命令| 说明|
|--------------|-------------|
|AT+CWMODE	|WIFI模式（已弃用）|
|AT+CWMODE_CUR	|当前WIFI模式（不保存到Flash）|
|AT+CWMODE_DEF|	默认WIFI模式（保存到Flash）|
|AT+CWJAP|	连接到AP（已弃用）|
|AT+CWJAP_CUR|	当前连接到AP（不会保存到Flash）|
|AT+CWJAP_DEF|	默认连接到AP（保存到Flash）|
|AT+CWLAP|	列出可用的AP|
|AT+CWQAP|	断开与AP的连接|
|AT+CWSAP|	配置softAP（已弃用）|
|AT+CWSAP_CUR|	配置当前的softAP（不会保存到Flash）|
|AT+CWSAP_DEF|	配置默认的softAP（保存到Flash）|
|AT+CWLIF|	连接到softAP 的列表站|
|AT+CWDHCP|	启用/禁用DHCP（已弃用）|
|AT+CWDHCP_CUR|当前启用/禁用DHCP（不保存到Flash）|
|AT+CWDHCP_DEF|	默认启用/禁用DHCP（保存到Flash）|
|AT+CWAUTOCONN|	上电时自动连接到AP|
|AT+CIPSTAMAC|	设置站mac地址（已弃用）|
|AT+CIPSTAMAC_CUR|	设置站MAC地址（不会保存到Flash）|
|AT+CIPSTAMAC_DEF|	设置站MAC地址（保存到Flash）|
|AT+CIPAPMAC|	设置softAP mac地址（已弃用）|
|AT+CIPAPMAC_CUR|	设置softAP mac地址（不会保存到Flash）|
|AT+CIPAPMAC_DEF|	设置softAP mac地址（保存到Flash）|
|AT+CIPSTA|	设置站IP地址（已弃用）|
|AT+CIPSTA_CUR|	设置站IP地址（不保存到Flash）|
|AT+CIPSTA_DEF|设置站IP地址（保存到Flash）|
|AT+CIPAP|	设置softAP IP地址（已弃用）|
|AT+CIPAP_CUR|	设置softAP IP地址（不保存到Flash）|
|AT+CIPAP_DEF|	设置softAP IP地址（保存到Flash）|
|AT+CWSTARTSMART|	启动SmartConfig|
|AT+CWSTOPSMART|	停止SmartConfig|

### TCP/IP AT 命令

|命令	|说明|
|-------------|--------------|
|AT+CIPSTATUS|	 获取连接状态|
|AT+CIPSTART|	建立TCP连接或注册UDP端口|
|AT+CIPSEND|	发送数据|
|AT+CIPSENDEX|	发送数据，如果满足<length>或“\ 0”，将发送数据|
|AT+CIPSENDBUF|将数据写入TCP-send-buffer|
|AT+CIPBUFRESET|	重新设置段ID数|
|AT+CIPBUFSTATUS|	检查TCP-send-buffer的状态|
|AT+CIPCHECKSEQ|	检查特定段是否发送|
|AT+CIPCLOSE|	关闭TCP / UDP连接|
|AT+CIFSR|	 获取本地IP地址|
|AT+CIPMUX| 设置多个连接模式|
|AT+CIPSERVER|	配置为服务器|
|AT+CIPMODE|	设置传输模式|
|AT+SAVETRANSLINK|	保存透明传输链接到Flash |
|AT+CIPSTO| 当ESP8266作为TCP服务器运行时设置超时|
|AT+CIUPDATE|	通过网络升级固件|
|AT+PING|	Ping IP地址或主机名|


### Seeed AT 命令

|命令	|说明|
|-------------|---------------|
|AT+LEDON|	转动蓝色LINK亮起|
|AT+LEDOFF	|转动蓝色LINK关闭|


## 资源下载

* [Schematic in PDF](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/res/Grove-UART_WiFi_v1.0.pdf)
* [Schematic in Eagle](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/res/Grove-UART_WiFi_sch_pcb.zip)
* [Espressif Systems ESP8266](http://espressif.com/en/products/esp8266/)
* [Espressif Systems ESP8266 AT Instruction Set - v0.24](http://bbs.espressif.com/download/file.php?id=450)
* [http://www.esp8266.com](http://www.esp8266.com)
* [ESP-06](http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family#esp-06)
* [ESP8266 on Hackaday](http://hackaday.com/tag/esp8266/)
* [https://nurdspace.nl/ESP8266](https://nurdspace.nl/ESP8266)
