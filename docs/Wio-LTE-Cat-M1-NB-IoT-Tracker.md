---
name: Wio LTE Cat M1/NB-IoT Tracker
category: Actuator
bzurl: https://seeedstudio.com/Grove-Infrared-Emitter-p-993.html
oldwikiname: Grove_-_Infrared_Emitter
prodimagename: Grove-Infrared_Emitter.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/101020026 1.jpg
surveyurl: https://www.research.net/r/Grove-Infrared_Emitter
sku: 101020026
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_wio
---


![](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/img/NBIOT1.JPG)

Seeed的Wio LTE CAT M1/NB-IoT专为需要CAT M1(eMTC)和NB-IoT组合模块的低功耗广域网(LPWAN)而设计. 此外,它还有一个ARM Cortex-M4 MCU和GNSS模块.

它兼容Arduino和Espruino(JavaScript)有助于跟踪地球上几乎所有移动的东西,然后无线上传该数据. 通过集成Grove连接器,Wio LTE CAT M1 / NB-IoT可与Grove系统实现灵活的通信解决方案.

Wio LTE CAT M1/NB-IoT非常适合户外项目,在这些项目中,设备可以连接到卫星导航系统,并提供附加物品的实时位置.

Wio LTE CAT M1/NB-IoT支持Espruino(JavaScript)引擎,任何人都可以快速构建物联网项目,尤其是在您可以使用JavaScript社区的大量资源的情况下.

<p style="text-align:center"><a href="https://item.taobao.com/item.htm?spm=a2oq0.12575281.0.0.53eb1debtmxObD&ft=t&id=575640527352" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>

**您是否正在寻找T-Mobile窄带的Twilio开发人员套件？ [文档](https://www.twilio.com/docs/wireless/nb)**

## 版本
|产品版本 | 改进 | 发布时间 |
|-------------------------------|------------------------------------------|---------------|
| Wio LTE Cat M1/NB-IoT v1.0    | 初代                                  | May 26, 2018  |

## 产品规格

- ARM Cortex-M4微控制器LTE CAT M1和NB-IoT组合(支持全球)
- 支持GPS / GLONASS GNSS
- 兼容Espruino(JavaScript)
- 兼容Arduino IDE(部分)
- 板载6个Grove端口,最多支持180个Grove模块
- 与Wio LTE CAT.1 基本兼容(只需要修改grove接口的电源开关)

## 硬件特征

- STM32F405RG,ARM Cortex-M4, CPU
running up to 168MHZ
- 1Mbytes Flash
- 192+4KBytes RAM
- System
    - Operating voltage: 3.3V
    - Low power: Sleep/Standby modes/Stop
    - CRC-32 generator
- LTE Connectivity
    - LTE CAT M1 and NB-IoT, Cat M1 Half-duplex (375 kb/s DL and UL) Cat NB1 Half-duplex (27.2 kb/s DL, 62.5 UL)
    - Embed protocol: TCP/UDP/FTP/HTTP/HTTPS/FTPS/TLS/MQTT/CoAP
- GNSS
    - GPS/GLONASS
    - 2.5m CEP(GPS), 4.0m CEP(GLONASS)
- Peripheral
    - 1 x USB for power supply and DFU
    - JST 1.0 connector for battery
    - 3 Buttons: 1. for Reset 2. for User
function 3. into upload mode
    - Nano SIM and TF card 2 in 1 socket
- Grove
    - 2 x Digital Port
    - 2 x Analog Port
    - 1 x UART
    - 1 x I2C

!!!Tip

    使用Grove模块扩展您的应用程序. 开发板上面有6个Grove连接. 如果这是您第一次看到Grove,请详细了解[Grove System](http://wiki.seeedstudio.com/Grove_System/). 简而言之,Groves是数百种传感器,采用标准风格,包括传感器,执行器,显示器以及通信.

## 应用

- 智慧城市
- 智能电表
- 智能能源
- 智能农业
- 智能零售
- 智能供应链
- 智能交通
- 连接汽车
- 连接建筑
- 连接健康
- 体育器材
- 宠物追踪
- 财产安全
- 共用自行车
- 物流运输定位系统
- 其他

## 硬件概述

![](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/img/front.png)

![](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/img/back.png)

!!!Tip

    如果您想使用板载Grove连接器,请使用digitalWrite(B10,HIGH)打开3V3_B. 除D38开机默认打开外,其他都需要打开3V3_B.

![](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/img/h3.png)


### 入门

### 安装USB驱动程序

- **Windows用户**：大多数Windows版本不会自动加载USB com端口的内置驱动程序.你必须下载ST的USB驱动程序：

	- 非Windows XP [用户下载1.4.0版驱动程序](http://www.espruino.com/files/stm32_vcp_1.4.0.zip).解压缩文件,运行可执行文件,然后转到Windows资源管理器中的C:\Program Files(x86)\STMicroelectronics\Software\Virtual comport驱动程序,64位系统双击dpinst_amd64.exe或64位系统则双击32位dpinst_x86.exe.

	- Windows XP [用户下载版本1.3.1驱动程序](http://www.espruino.com/files/stm32_vcp_1.3.1.zip).解压缩文件,运行VCP_V1.3.1_Setup.exe,然后在Windows资源管理器中转到C:\Program Files\STMicroelectronics\Software\Virtual comport驱动程序,然后双击`*.exe`文件.

- **Linux用户**:以确保您具有正常用户连接的正确权限,您需要复制文件[45-espruino.rules](https://github.com/espruino/Espruino/blob/master/misc/45-espruino.rules)到/etc/udev/rules.d,用udevadm控制重新加载udevadm control --reload-rules,并确保你的用户在plugdev组中(你可以通过输入组来检查).您可以通过键入sudo adduser $ USER plugdev然后注销并重新登录来添加它.Arch Linux用户需要将其用户添加到uucp并锁定组.
- **Mac OS X和Chromebook用户**：电路板只需插入和工作,无需驱动程序！

### 更改DFU驱动程序

**windows用户**:

- 第1步,按住`BOOT`按钮并连接到计算机,您将在设备管理器上看到 **STM32设备处于DFU模式** ,如下所示.

![](https://github.com/SeeedDocument/Wio_LTE/raw/master/img/before_driver_installation.png)


- 第2步,您需要使用[zadig_xx.exe](https://github.com/seeeddocument/wio-lte/raw/master/res/zadig_2.1.2.exe)将dfu驱动程序从 **sttub30** 更改为 **winusb** ,如下所示.如果在zadig上看不到任何信息,请单击`Options`-->`List All Devices`,然后选择stm32虚拟COM端口.

![](https://github.com/SeeedDocument/Wio_LTE/raw/master/img/zadig.png)

- 第3步,您将在设备管理器上看到 **stMicroelectronics虚拟COM端口** ,如下所示.

![](https://github.com/SeeedDocument/Wio_LTE/raw/master/img/after_driver_installation.png)


### 通过Arduin IDE 编程

**1. 软件配置**

- 步骤1.安装Arduino IDE,在1.8.0上推荐IDE版本.
- 步骤2.按照[如何将看到的板添加到Arduino IDE](http://wiki.seeedstudio.com/Seeed_Arduino_Boards/)将Seeed STM32F4板添加到arduino板管理器中.
- 步骤3.从Github下载[WioLTE_Cat_NB1_Arduino_Library](https://github.com/lanselambor/WioLTE_Cat_NB1_Arduino_Library).
- 步骤4.参考[如何安装库](http://wiki.seeedstudio.com/How_to_install_Arduino_Library)为Arduino安装库.
- 步骤5.在上传草图之前,按住BOOT0和RST按钮,松开RST按钮而不是BOOT0按钮,这样电路板将进入STM BOOLARDER模式.
- 步骤6.不要选择任何串行端口上传工具标签中的草图只需单击上传图标.

**2. 使用板载RGB LED**

 - 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->Seeed_WS2812b.
 - 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
 - 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
 - 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
 - 步骤5.将COM端口保持空白.
 - 步骤6.选择Sketch-->Upload将代码上传到Wio_LTE.
 
```c++
#include <Seeed_ws2812.h>
#include <ublox_sara_r4.h>

#define LEN_NUM 1

Ublox_sara_r4 ublox = Ublox_sara_r4();
WS2812 strip = WS2812(LEN_NUM, ublox.RGB_LED_PIN);

void setup() {
  // Set RGB LED power pin high
  ublox.turnOnRGBPower();
  strip.begin();
  strip.brightness = 20;
}

void loop() {  
  strip.RGBCycle(1000);
  strip.rainbowCycle(20);
}
```

- 步骤7.按 **RST** ,然后您可以看到板载RGB LED工作.

**3. 使用GNSS**

- 步骤1.将Nano SIM卡插入PCB板侧附近的Nano SIM插槽.
- 步骤2.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->GNNS-->GNSS.
- 步骤3.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤4.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤5.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤6.将COM端口保持空白.
- 步骤7.选择Sketch-->Upload将代码上传到Wio LTE Cat NB1.
- 步骤8.按 **RST** 按钮启用COM端口.

```c++
#include <ublox_sara_r4_gnss.h>

UBLOX_SARA_R4_GNSS gnss = UBLOX_SARA_R4_GNSS();

void setup()  
{
  // Open GNSS module
  gnss.open_GNSS();
  delay(3000);
  SerialDebug.println("_Start");
}

void loop() {
  gnss.dataFlowMode();
}
```

- 步骤9.使用COM监视工具打印串行消息. **请不要使用Arduino IDE 串口监视器！ 这可能导致下次下载失败,但重新打开Arduino IDE可以恢复该问题** .
- 步骤10.我们将在屏幕上看到lat,lon信息.

```C++
$GNRMC,,V,,,,,,,,,,N*4D
$GNVTG,,,,,,,,,N*2E
$GNGGA,,,,,,0,00,99.99,,,,,,*56
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GPGSV,1,1,01,30,,,44*7B
$GLGSV,1,1,00*65
$GNGLL,,,,,,V,N*7A
$GNRMC,,V,,,,,,,,,,N*4D
$GNVTG,,,,,,,,,N*2E
$GNGGA,,,,,,0,00,99.99,,,,,,*56
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GPGSV,1,1,04,07,,,43,17,,,38,18,,,39,30,,,44*70
$GLGSV,1,1,00*65
$GNGLL,,,,,,V,N*7A
$GNRMC,,V,,,,,,,,,,N*4D
$GNVTG,,,,,,,,,N*2E
$GNGGA,,,,,,0,00,99.99,,,,,,*56
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GNGSA,A,1,,,,,,,,,,,,,99.99,99.99,99.99*2E
$GPGSV,2,1,06,07,,,44,09,,,41,17,,,40,18,,,41*79
$GPGSV,2,2,06,28,,,40,30,,,45*73
$GLGSV,1,1,00*65
$GNGLL,,,,,,V,N*7A
```

**4. 使用SD Card**

- 步骤1.将micro SD卡插入SD卡插槽.
- 步骤2.选择File--> Examples-->SD-->CardInfo.
- 步骤3.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤4.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤5.选择Tools-->Boards-->Wio Tracker LTE..
- 步骤6.将COM端口保持空白.
- 步骤7.选择Sketch-->Upload将代码上传到Wio_LTE.

```C++
// include the SD library:
#include <SD.h>

// set up variables using the SD utility library functions:
Sd2Card card;
SdVolume volume;
SdFile root;

// change this to match your SD shield or module;
// Arduino Ethernet shield: pin 4
// Adafruit SD shields and modules: pin 10
// Sparkfun SD shield: pin 8
const int chipSelect = 43;

void setup()
{
 // Open serial communications and wait for port to open:
  // SerialUSB.begin(115200);
  //  while (!Serial) {
  //   ; // wait for serial port to connect. Needed for Leonardo only
  // }


  SerialUSB.print("\nInitializing SD card...");
  // On the Ethernet Shield, CS is pin 4. It's set as an output by default.
  // Note that even if it's not used as the CS pin, the hardware SS pin 
  // (10 on most Arduino boards, 53 on the Mega) must be left as an output 
  // or the SD library functions will not work. 
  pinMode(SS, OUTPUT);


  // we'll use the initialization code from the utility libraries
  // since we're just testing if the card is working!
  while (!card.init(SPI_HALF_SPEED, chipSelect)) {
    SerialUSB.println("initialization failed. Things to check:");
    SerialUSB.println("* is a card is inserted?");
    SerialUSB.println("* Is your wiring correct?");
    SerialUSB.println("* did you change the chipSelect pin to match your shield or module?");
  } 
  
  // print the type of card
  SerialUSB.print("\nCard type: ");
  switch(card.type()) {
    case SD_CARD_TYPE_SD1:
      SerialUSB.println("SD1");
      break;
    case SD_CARD_TYPE_SD2:
      SerialUSB.println("SD2");
      break;
    case SD_CARD_TYPE_SDHC:
      SerialUSB.println("SDHC");
      break;
    default:
      SerialUSB.println("Unknown");
  }

  // Now we will try to open the 'volume'/'partition' - it should be FAT16 or FAT32
  if (!volume.init(card)) {
    SerialUSB.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card");
    return;
  }


  // print the type and size of the first FAT-type volume
  uint32_t volumesize;
  SerialUSB.print("\nVolume type is FAT");
  SerialUSB.println(volume.fatType(), DEC);
  SerialUSB.println();
  
  volumesize = volume.blocksPerCluster();    // clusters are collections of blocks
  volumesize *= volume.clusterCount();       // we'll have a lot of clusters
  volumesize *= 512;                            // SD card blocks are always 512 bytes
  SerialUSB.print("Volume size (bytes): ");
  SerialUSB.println(volumesize);
  SerialUSB.print("Volume size (Kbytes): ");
  volumesize /= 1024;
  SerialUSB.println(volumesize);
  SerialUSB.print("Volume size (Mbytes): ");
  volumesize /= 1024;
  SerialUSB.println(volumesize);

  
  SerialUSB.println("\nFiles found on the card (name, date and size in bytes): ");
  root.openRoot(volume);
  
  // list all files in the card with date and size
  root.ls(LS_R | LS_DATE | LS_SIZE);
}


void loop(void) {
  
}
```

- 步骤8.按 **RST** 按钮启用COM端口.
- 步骤9.使用COM监视工具打印串行消息. **请不要使用Arduino IDE 串口监视器！ 这可能导致下次下载失败,但重新打开Arduino IDE可以恢复该问题** .
- 步骤10.打开串口监视器,我们将在屏幕上看到以下信息.

```C++
Initializing SD card...
Card type: SDHC

Volume type is FAT32

Volume size (bytes): 2689048576
Volume size (Kbytes): 2626024
Volume size (Mbytes): 2564

Files found on the card (name, date and size in bytes):
```

**5. 使用Network RSSI**

- 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->RSSI.
- 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤5.将COM端口保持空白.
- 步骤6.选择Sketch- >Upload将代码上传到Wio_LTE.

```c++
#include <ublox_sara_r4.h>
#include <UART_Interface.h>

Ublox_sara_r4 ublox = Ublox_sara_r4();

void setup() {
  
  SerialDebug.println("Begin...");
  ublox.powerOn();
  while(false == ublox.Check_If_Power_On()){
    SerialDebug.println("Waitting for module to alvie...");
    delay(1000);
  }  
  SerialDebug.println("Power On O.K!");

  delay(100);
  check_with_cmd("AT+UGPIOC=23,10\r\n", "OK", CMD);
  check_with_cmd("AT+UGPIOC=16,2\r\n", "OK", CMD);
}

void loop() {
	int signal;
	if(ublox.getSignalStrength(&signal)) {
		SerialDebug.print("RSSI: ");
		SerialDebug.println(signal, DEC);
	} else {
		SerialDebug.print("Error");
	}

	delay(1000);
 
}
```

- Step 7. Press **RST** , then you can see below info on screen.

```c++
AT+CSQ

+CSQ: 99,99

OKRSSI: 99

AT+CSQ

+CSQ: 99,99

OKRSSI: 99

AT+CSQ

+CSQ: 99,99

OKRSSI: 99

AT+CSQ

+CSQ: 99,99
```

**6. 使用TCP协议**

- 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library  - >网络 - > tcp_directLink草图.
- 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤5.将COM端口保持空白.
- 步骤6.选择Sketch-->Upload将代码上传到Wio_LTE.

```c++
#include <ublox_sara_r4.h>

Ublox_sara_r4 ublox = Ublox_sara_r4();

char *server = "www.arduino.cc";
uint16_t port = 80;
int sockId = -1;

void setup() {
	bool network_attached = false;

	Log_info("Begin...");
	
	ublox.powerOn();
	Log_info("Waitting for module to alvie...");
	while(false == ublox.isAlive()){
		Log(".");
		delay(100);
	} 
	Logln(); 

	Log_info("Initializing network..");
	if(!ublox.network_Init(120)) { 
		Log_error("Network initialize timeout.");
		while(1);
	}
	Log_info("APN: " + String(ublox._apn));
	Log_info("Local IP: " + String(ublox._str_ip));
	Log_info("Operator: " + String(ublox._operator));
	Log_info("Network attached.");
	
	// This method is import for setting transparent session
	// use disableDirectLinkMode() to use nontransparent session  
	ublox.enableDirectLinkMode();

	if(-1 == (sockId = ublox.createSocket(TCP))) {
		Log_error("Create socket error!");
		return;
	}
	if(!ublox.sockConnect(sockId, server, port)) {
		Log_error("connect to server failed.");
	}			
	Log_info("Sent TCP message in direct link mode.");
		
}	

void loop() {
	static uint8_t tries = 0;
	String str_msg = "ublox random number " + String(random(0,100));
	// String str_msg = "/txt HTTP"; 

	ublox.socketWrite((uint8_t *)str_msg.c_str(), (uint16_t)str_msg.length());
	Log_info("Send msg: " + str_msg);

	tries++;
	if(tries > 5) {
		if(ublox.sockClose(sockId)) {
			Log_info("Close socket.");
		}
		Log_info("Enter AT command mode.");
		while(true) AT_bypass();
	}

	delay(2000);
}
```

- 步骤7.按 **RST** ,然后您可以在屏幕上看到以下信息.

```c++
[INFO] Begin...
[INFO] Waitting for module to alvie...
...
[INFO] Initializing network..
.............................[INFO] APN: ctnb
[INFO] Local IP: 10.14.8.161
[INFO] Operator: 460 11 ????
[INFO] Network attached.
[INFO] Sent TCP message in direct link mode.
[INFO] Send msg: ublox random number 33
[INFO] Send msg: ublox random number 43
[INFO] Send msg: ublox random number 62
[INFO] Send msg: ublox random number 29
[INFO] Send msg: ublox random number 0
[INFO] Send msg: ublox random number 8
```

**7. 使用UDP协议**

```c++
#include <ublox_sara_r4.h>

Ublox_sara_r4 ublox = Ublox_sara_r4();

char *server = "time.nist.gov";
uint16_t port = 8888;
int sockId = -1;

void setup() {
	bool network_attached = false;

	Log_info("Begin...");
	
	ublox.powerOn();
	Log_info("Waitting for module to alvie...");
	while(false == ublox.isAlive()) {
		Log(".");
		delay(100);
	}  
	Logln("");

	Log_info("Initializing network..");
	if(!ublox.network_Init(120)) { 
		Log_error("Network initialize timeout.");
		while(1);
	}
	Log_info("APN: " + String(ublox._apn));
	Log_info("Local IP: " + String(ublox._str_ip));
	Log_info("Operator: " + String(ublox._operator));
	Log_info("Network attached.");
	
	if(-1 == (sockId = ublox.createSocket(UDP))) {
		Log_error("Create socket error!");
	}
	Log("[INFO] Create socket id: ");
	Logln(sockId);

	ublox.enableDirectLinkMode();
	if(!ublox.sockConnect(sockId, server, port)) {
		Log_error("connect to server failed.");
	}
	Log_info("Sent UDP message in direct link mode.");


		
}	

void loop() {
	static uint8_t tries = 0;

	String str_msg = "ublox random number " + String(random(0,100));

	ublox.socketWrite((uint8_t *)str_msg.c_str(), (uint16_t)str_msg.length());
	Log_info("Send msg: " + str_msg);

	tries++;
	if(tries > 5) {
		if(ublox.sockClose(sockId)) {
			Log_info("Close socket.");
		}
		while(true) AT_bypass();
	}

	delay(2000);
}
```

- 步骤7.按 **RST** ,然后您可以在屏幕上看到以下信息.

```
[INFO] Waitting for module to alvie...
...
[INFO] Initializing network..
....................[INFO] APN: ctnb
[INFO] Local IP: 10.178.48.90
[INFO] Operator: 460 11 ????
[INFO] Network attached.
[INFO] Create socket id: 0
[INFO] Sent UDP message in direct link mode.
[INFO] Send msg: ublox random number 33
[INFO] Send msg: ublox random number 43
[INFO] Send msg: ublox random number 62
[INFO] Send msg: ublox random number 29
[INFO] Send msg: ublox random number 0
[INFO] Send msg: ublox random number 8
[INFO] Close socket.
```

**8.使用MQTT订阅**

- 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->MQTTClient-->mqtt_sub.
- 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤5.将COM端口保持空白.
- 步骤6.选择Sketch-->Upload将代码上传到Wio_LTE.

```c++
#include <Arduino.h>

#include <math.h>

#include <ublox_sara_r4.h>
#include <ublox_sara_r4_mqtt.h>
#include <UART_Interface.h>

#define PRE_FIX  "[MQTT] "

MQTT mqtt;
Ublox_sara_r4 ublox = Ublox_sara_r4();

char *server = "test.mosquitto.org";
uint16_t port = 1883;

void setup() {
	Log_info("Begin...");
	
	ublox.powerOn();
	Log_info("Waitting for module to alive...");
	while(false == ublox.isAlive()) {
		Log(".");
		delay(100);
	}  
	Logln();

	Log_info("Initializing network...");	
	if(!ublox.network_Init()) { 
		Log_error("Network initialize timeout.");
		return;
	}

	// Set MQTT server 
	if(!mqtt.setServer(server, port)) {
		Log_error("Set MQTT server failed");
		return;
	} else {
		Logln(PRE_FIX"Set MQTT server success.");
	}

	// Set will
	if(!mqtt.setWill("Heat", "ublox n/r410")) {
		Log_error("Set MQTT will failed");
		return;
	} else {
		Logln(PRE_FIX"Set MQTT will success.");
	}

	// Connect to server
	Logln(PRE_FIX"Connecting to server: " + String(server));
	while(!mqtt.connect()) {}
	Logln(CRLF PRE_FIX"Connected\n\r");
}	

void loop() 
{				
	static uint8_t tries = 0;	
	const char *topic = "Heat";
	String msg = String(random(2000, 3000)*1.0/100.0) + " degree";
	
		
	if(mqtt.publish(topic, msg.c_str())) {
		Logln(PRE_FIX" published Topic " + String(topic) + " Messagea " + msg);	
	} else {
		Log_error("MQTT publish failed");
		// while(true);
	}

	tries++;
	if(tries > 5)
	{
		if(mqtt.disconnect()) {
			Logln(PRE_FIX"Disconnect.");
		}
		Log_info("Enter AT command loop");
		while(true) AT_bypass();
	}
	
	delay(2000);
}
```

- 步骤7.按 **RST** ,然后您可以在屏幕上看到以下信息.

**9.使用MQTT发布**

- 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->MQTTClient-->mqtt_pub.
- 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤5.将COM端口保持空白.
- 步骤6.选择Sketch-->Upload将代码上传到Wio_LTE.

```c++
#include <Arduino.h>

#include <math.h>

#include <ublox_sara_r4.h>
#include <ublox_sara_r4_mqtt.h>
#include <UART_Interface.h>

#define PRE_FIX  "[MQTT] "

MQTT mqtt;
Ublox_sara_r4 ublox = Ublox_sara_r4();

char *server = "server name or IP";
uint16_t port = 1883;

void setup() {
	Log_info("Begin...");
	
	ublox.powerOn();
	Log_info("Waitting for module to alive...");
	while(false == ublox.isAlive()) {
		Log(".");
		delay(100);
	}  
	Logln();

	Log_info("Initializing network...");	
	if(!ublox.network_Init()) { 
		Log_error("Network initialize timeout.");
		return;
	}

	// Set MQTT server 
	if(!mqtt.setServer(server, port)) {
		Log_error("Set MQTT server failed");
		return;
	} else {
		Logln(PRE_FIX"Set MQTT server success.");
	}

	// Set will
	if(!mqtt.setWill("Heat", "ublox n/r410")) {
		Log_error("Set MQTT will failed");
		return;
	} else {
		Logln(PRE_FIX"Set MQTT will success.");
	}

	// Connect to server
	Logln(PRE_FIX"Connecting to server: " + String(server));
	while(!mqtt.connect()) {}
	Logln(CRLF PRE_FIX"Connected\n\r");
}	

void loop() 
{				
	static uint8_t tries = 0;	
	const char *topic = "Heat";
	String msg = String(random(2000, 3000)*1.0/100.0) + " degree";
	
		
	if(mqtt.publish(topic, msg.c_str())) {
		Logln(PRE_FIX" published Topic " + String(topic) + " Messagea " + msg);	
	} else {
		Log_error("MQTT publish failed");
		// while(true);
	}

	tries++;
	if(tries > 5)
	{
		if(mqtt.disconnect()) {
			Logln(PRE_FIX"Disconnect.");
		}
		Log_info("Enter AT command loop");
		while(true) AT_bypass();
	}
	
	delay(2000);
}
```

 - 步骤7.按 **RST** ,然后您可以在屏幕上看到以下信息.

**10.使用Grove接口**

- 步骤1.选择File-->Examples-->WioLTE_Cat_NB1_Arduino_Library-->Grove_UartGpioI2cAnalog.
- 步骤2.按住Wio LTE Cat NB1背面的BOOT按钮,将USB插入PC.
- 步骤3.我们将在设备管理器中看到 **STM BOOTLARDER** .
- 步骤4.选择Tools-->Boards-->Wio_Tracker_LTE.
- 步骤5.将COM端口保持空白.
- 步骤6.选择Sketch-->Upload将代码上传到Wio_LTE.

```c++
#include <ublox_sara_r4.h>
#include <UART_Interface.h>
#include <Wire.h>

/**
 * In this sketch, we test all peripheral on the board.
 * 1. Grove UART pass through to USB port, you can connect Grove GPS to read message from USB port.
 * 2. External interrupt using pin D38, D20 follow the state of D38.  
 * 3. Read ADC0 ~ ADC3
 * 4. I2C detect using Grove I2C port
 * 5. AT passthrough between USB port and cellular module. 
 * 
 * Notice: before using Grove UART/GPIO/I2C/Analog sockets, need to enable 
 *         its power at first. using Ublox_sara_r4::turnOnGrovePower();
 *         Power supply on D38 is always on.
*/

Ublox_sara_r4 ublox = Ublox_sara_r4();

void setup() {
  SerialGrove.begin(9600);
  SerialDebug.println("Begin...");  
  ublox.turnOnGrovePower();


  //Attach interrupt to Gpio D38, set D20 output follow D38
  pinMode(20, OUTPUT);
  pinMode(38, INPUT);
  attachInterrupt(38, GpioTest, CHANGE);

  //I2C test - Scan I2C device at Grove I2C socket
  i2cScan();

  //Analog test at A4 A5 A6 A7
  pinMode(4, INPUT_ANALOG);
  pinMode(5, INPUT_ANALOG);
  pinMode(6, INPUT_ANALOG);
  pinMode(7, INPUT_ANALOG);
  SerialDebug.print("Read A4: ");
  SerialDebug.println(analogRead(4));  
  SerialDebug.print("Read A5: ");
  SerialDebug.println(analogRead(5));
  SerialDebug.print("Read A6: ");
  SerialDebug.println(analogRead(6));
  SerialDebug.print("Read A7: ");
  SerialDebug.println(analogRead(7));

}

void loop() {
  /* Debug */
  while(SerialGrove.available()) {
    SerialDebug.write(SerialGrove.read());
  }
  while(SerialDebug.available()) {
    SerialGrove.write(SerialDebug.read());
  }
}

void i2cScan(void)
{
  uint8_t address;
  
  Wire.begin();
  for(address = 0; address < 127; address++) {
    Wire.beginTransmission(address);
    if(0 == Wire.endTransmission()) {
      SerialDebug.print("Detected i2c device at 0x");
      SerialDebug.println(address, HEX);
    }
  }
} 

void GpioTest(void)
{
  digitalWrite(20, digitalRead(38));
}
```

- 步骤7.按 **RST** ,然后您可以在屏幕上看到以下信息.

## 资源

- **[Eagle&PDF]** [WioLTE_Cat_NB1](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/res/WioLTE_Cat_NB1_Eagle-master.zip)

- **[Library]** [WioLTE_Cat_NB1_Arduino_Library](https://github.com/Seeed-Studio/WioLTE_Cat_NB1_Arduino_Library)

- **[Datasheet]** [AT Command](https://github.com/SeeedDocument/Wio_LTE_Cat_M1_NB-IoT_Tracker/raw/master/res/SARA-R4-SARA-N4_ATCommands_(UBX-17003787).pdf)


## 技术支持
请将任何技术问题提交到我们的[论坛](http://forum.seeedstudio.com/)或发送邮件至techsupport@seeed.cc.