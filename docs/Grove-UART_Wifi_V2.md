---
name: Grove - UART WiFi V2 (ESP8285)
category: Communication
bzurl: https://www.seeedstudio.com/Grove-Uart-Wifi-p-2495.html
oldwikiname:
prodimagename: Grove-uart-wifi-01.jpg
surveyurl: https://www.surveymonkey.com/r/grove_uart_wifi
sku: 113020011
---


![enter image description here](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/V2/Main.JPG)


Grove - UART WiFi是一个串行收发器模块，具有无处不在的ESP8285 IoT SoC。 通过集成的TCP / IP协议栈，该模块可让您的微控制器只需几行代码即可与WiFi网络进行交互。 每个ESP8285模块都预编程了AT命令集固件，这意味着您可以发送简单的文本命令来控制设备。 SoC具有集成的WEP，WPA / WPA2，TKIP，AES和WAPI引擎，可以作为DHCP的接入点，可以加入现有的WiFi网络，并具有可配置的MAC和IP地址。

<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-UART-WiFi-V2-%28ESP8285%29-p-3054.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>



## 版本

| Parameter     | V1.0     |V2.0     |
| :------------- | :------------- |:------------- |
| 产品发布日期       | 24th Jue 2016       |26th Mach 2018|
|WiFi 芯片|ESP8266| ESP8285|
|天线类型| External |On-board|
|LEDs| 3 LEDs-Power/WiFi/AT Command|2 LEDs- Power/WiFi|
|按键|1 Button: <br>短按 **重启** <br> 长按进入 **UART boot 模式**</br>|这两个功能的按键|


![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/Version_tracker.jpg)



!!!Note
        你可能会问ESP8266和ESP8285有什么区别。 ESP8285是ESP8266的更新版本，增加了内置的1MB闪存。 除此之外，它们几乎相同。

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

    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


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

### Play With Arduino
!!!Note

    如果你是第一次使用 Arduino, 请点击 [这里](http://arduino.cc) 开始你的  Arduino 的体验。


### 准备工作

| Seeeduino Lite | Grove-OLED |Grove-UART Wifi|
|--------------|-----------------|-----|
|![enter image description here](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/lite.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_OLED_Display_0.96/raw/master/images/grove%20oled%200.96_s.jpg)|![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/V2/thumbnail.jpg)|
|<a href="https://www.seeedstudio.com/Seeeduino-Lite-p-1487.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Grove---OLED-Display-0.96%22-p-781.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Grove-Uart-Wifi-p-2495.html" target="_blank">Get One Now</a>|


!!!note
      **1** 请小心插拔microUSB连接线，否则将可能会对接口造成破坏。另外，请使用4线microUSB，2线的只能用来充电，不能作为数据线。如果没有请点击下面链接购买。
     [here](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html)


    **2** 每个Grove 模块在购买时会带有连接线，若丢失连接线，您可以点击下面链接购买。
     [here](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html)



#### Hardware

- **Step 1.** 将 Grove-UART Wifi 与Seeeduino 的 **SERIAL** 接口连接。

- **Step 2.** 将 Grove-OLED  与Seeeduino 的 **I2C** 接口连接。

 - **Step 3.** 将seeeduino和PC通过micro-USB连接.


![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/V2/Arduino_connect.jpg)



#### 软件


- **Step 1.** 从github上下载OLED需要的 [128X64 OLED库文件](https://github.com/Seeed-Studio/OLED_Display_128X64/archive/master.zip)

- **Step 2.** 参考[如何安装库文件](http://wiki.seeedstudio.com/How_to_install_Arduino_Library) to install library for Arduino.

- **Step 3.** 打开arduino IDE并新建文件，将下列代码复制进去


```
// test grove - uart wifi
// scan ap and display on Grove - OLED 0.96'
// Loovee @ 2015-7-28

#include <Wire.h>
#include <SeeedOLED.h>

char ap_buf[30][16];
int ap_cnt = 0;

void setup()
{
    Serial1.begin(115200);

    delay(3000);
    Wire.begin();
    SeeedOled.init();                   // initialze SEEED OLED display

    SeeedOled.clearDisplay();           // clear the screen and set start position to top left corner
    SeeedOled.setNormalDisplay();       // Set display to normal mode (i.e non-inverse mode)
    SeeedOled.setPageMode();            // Set addressing mode to Page Mode

}


void loop()
{
    ap_cnt = 0;
    SeeedOled.clearDisplay();
    SeeedOled.setTextXY(3,0);    
    SeeedOled.putString("Wifi Scan...");

    cmd_send("AT+CWLAP");
    wait_result();

    display_ap();
    delay(5000);
}

// send command
void cmd_send(char *cmd)
{
    if(NULL == cmd)return;
    Serial1.println(cmd);
}


// wait result of ap scan
// +CWLAP:(3,"360WiFi-UZ",-81,"08:57:00:01:61:ec",1)
void wait_result()
{
    while(1)
    {
LOOP1:
        char c1=0;
        if(Serial1.available()>=2)
        {
            c1 = Serial1.read();
            if(c1 == 'O' && 'K' == Serial1.read())return;       // OK means over
        }

        if('('==c1)
        {
            while(Serial1.available()<3);
            Serial1.read();
            Serial1.read();
            Serial1.read();

            int d = 0;
            while(1)
            {
                if(Serial1.available() && '"' == Serial1.read());      // find "
                {
                    while(1)
                    {
                        if(Serial1.available())
                        {
                            char c = Serial1.read();
                            ap_buf[ap_cnt][d++] = c;
                            if(c == '"' || d==16)
                            {
                                ap_buf[ap_cnt][d-1] = '\0';
                                ap_cnt++;
                                goto LOOP1;
                            }
                        }
                    }
                }
            }
        }
    }
}

// display
void display_ap()
{
    char strtmp[16];
    sprintf(strtmp, "get %d ap", ap_cnt);

    SeeedOled.clearDisplay();           // clear
    SeeedOled.setTextXY(3,3);           // Set the cursor to Xth Page, Yth Column
    SeeedOled.putString(strtmp);        // Print the String

    delay(2000);

    int cnt = ap_cnt;
    int offset = 0;
    while(1)
    {
        SeeedOled.clearDisplay();
        if(cnt>=8)
        {
            for(int i=0; i<8; i++)
            {
                SeeedOled.setTextXY(i,0);           // Set the cursor to Xth Page, Yth Column
                SeeedOled.putString(ap_buf[8*offset+i]);        // Print the String
            }
            cnt-=8;
            offset++;
        }
        else
        {
            for(int i=0; i<cnt; i++)
            {
                SeeedOled.setTextXY(i,0);           // Set the cursor to Xth Page, Yth Column
                SeeedOled.putString(ap_buf[8*offset+i]);        // Print the String
            }

            return;
        }

        delay(2000);
    }
}

```

- **Step 4.** 烧录 demo. 如果不知道如何烧录，请参考 [如何烧录代码](http://wiki.seeedstudio.com/Upload_Code/).


这时你将会看到OLED显示你周围的wifi的AP

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_result.jpg)




## 固件升级
我们的模块在出厂前已经烧录过固件了，但是你也可以自己烧录，点击 [这里](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/res/Grove-Uart_Wifi_Firmware-code.zip) 来烧录固件


### 准备工作

* 一根USB转串口线，用来固件升级[UartSBee V5](https://www.seeedstudio.com/UartSBee-V5-p-1752.html) if you don't know where to get one.
* 一个，点击 [这里](https://www.seeedstudio.com/Grove-4-pin-Female-Jumper-to-Grove-4-pin-Conversion-Cable-%285-PCs-per-PAck%29-p-1020.html) 购买

* 一根 micro USB 线(type A to type C)

### 硬件
  将与
**Step 1.** 将 Grove-跳线与Grove - Uart Wifi 的Grove接口连接起来并连接另一端到UartBee如下图所示



![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/V2/UART_V2.jpg)


**Step 2.** 连接线如下所示

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_connect2.jpg)




### 软件

**Step 1.** 下载烧录工具和固件

* [FLASH DOWNLOAD TOOLS](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/FLASH_DOWNLOAD_TOOLS_v1.2_150512.zip)
* [Bin files of firmware](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/Grove-uart-wifi-firmware-bin.zip)


**Step 2.** 按住按钮直到红色LED指示灯亮起，这表明它已准备好刻录固件。


**Step 3.** 在FLASH DOWNLOAD TOOLS文件中启动可执行文件（双击）以进行如下步骤的配置：

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools1.jpg)
** 1. ** 从下载的固件bin文件中选择所需的文件。

** 2. ** 选择 ** SpiAutoSet **复选框。

** 3. ** 选择COM端口和BAUDRATE。

** 4. ** 点击 **开始**按钮

*进度条将显示在固件刻录过程中。
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools2.1.jpg)

* 最后，固件刻录完成。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove-Uart_Wifi/master/img/Grove_uart_wifi_firmware_tools3.jpg)




## AT 命令

### 快速开始AT 指令

#### 硬件

 **准备工作** 和 **硬件连接**  [固件升级](http://wiki.seeedstudio.com/Grove-UART_Wifi/#firmware-update)一样的


让我们开始软件部分

#### 软件

   您可以使用任何您喜欢的串行工具，我们在这里使用Arduino。 请确保已将** USB转串口转换器**连接到PC。



**Step 1.** 打开Arduino IDE，单击**工具**选择相应的**端口**。

![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/1.png)


**Step 2.** 这时点击Arduino 右上角的串口监视器 <embed src="https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/COM.png"> 的按钮

**Step 3.** 将串行监视器设置为以下图片。 尤其:<font color="17a1a5"><b>2-</b></font> Select **Both NL & CR**, <font color="17a1a5"><b>3-</b></font>设置 ** 波特率 ** 为 115200


![](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/img/result.png)

**Step 4.** 输入你需要的AT指令 <font color="17a1a5"><b>1-</b></font> **指令行**  然后点击 <font color="17a1a5"><b>4-</b></font> **Send** 按钮. 你将会看到返回信息如上图所示



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

- **[PDF]** [Schematic in PDF](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/Grove%20-%20Uart%20Wifi%20v2%20sch.pdf)
* **[Zip]** [Schematic in Eagle](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/Uart_Wifi_V2_Eagle_file.zip)
* **[Datasheet]** [Espressif Systems ESP8285](https://github.com/SeeedDocument/Grove-Uart_Wifi/raw/master/res/ESP8285_datasheet.pdf)
* **[PDF]** [Espressif Systems ESP8266 AT Instruction Set - v0.24](http://bbs.espressif.com/download/file.php?id=450)
* **[MoreReading]** [http://www.esp8266.com](http://www.esp8266.com)
* **[MoreReading]** [ESP-06](http://www.esp8266.com/wiki/doku.php?id=esp8266-module-family#esp-06)
* **[MoreReading]** [ESP8266 on Hackaday](http://hackaday.com/tag/esp8266/)
* **[MoreReading]** [https://nurdspace.nl/ESP8266](https://nurdspace.nl/ESP8266)


## 技术支持

如果你有文档或者技术上的任何疑问，请联系 [techsupport@seeed.cc](techsupport@seeed.cc) 或者在[论坛](https://forum.seeedstudio.com/)询问。
