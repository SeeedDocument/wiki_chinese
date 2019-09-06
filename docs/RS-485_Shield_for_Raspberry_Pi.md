---
name: RS-485 Shield for Raspberry Pi
category:
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 103030295
tags:
---

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/main.jpg)

RS-485是串行通信网络中经济高效的解决方案。它可以用于10 Mbit / s的数据速率或低速时最远1200 m的距离。这款RS-485 Shield是Raspberry Pi的标准附加板。它集成了简单的螺丝端子和DB9接口。


<p style="text-align:center"><a href="https://www.seeedstudio.com/RS-485-Shield-for-Raspberry-Pi.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>


## 功能

- 每个部件一个驱动器和一个接收器
- EMI噪声最小化
- 传输速率高达2.5Mbps
- 无驱动器转换速率限制
- 短路电流有限
- 支持Raspberry Pi 3B / 3B + / 4


<div class="page"/></div>


## Specification

|目标|数值|
|:---|:---|
|工作电源电压|3.3V|
|接口|	RS-485 DB9接口X1 <br> RS-485螺丝接口X1  <br>2×13母头到Raspberry X1 <br>  2×13扩展母头X1 <br>  Grove I2C接口X1
|数据速率|2.5Mbps|
|接收器数量|32|
|存储温度范围|-65～160℃|
|通道数|8|
|分辨率|12-Bit|
|能量消耗|不同的功耗取决于传输速率|
|尺寸|L：62mm W：39.2mm H：21.8mm|
|重量|23克|


<div class="page"/></div>


## 典型应用

- 低功耗RS-485收发器
- 电平转换
- 用于EMI敏感应用的收发器工业控制局域网
- 半双工应用


## 硬件概述

### 引脚

**概观**

![Pin_map](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/Pin_map.jpg)



<div class="page"/></div>


---
**RS-485 DB9接口和RS-485螺钉接口**


![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/pin_out/8.jpg)

485接口使用差分信号传输。请确保端口A连接到485设备的端口A，端口B连接到485设备的端口B

>485-A：RS485数据传输线的A端，连接到MAX485芯片的引脚A. 
>485-B：RS485数据传输线的B端，连接到MAX485芯片的引脚B. 
>GND：连接到Raspberry Pi GND。


[![](https://raw.githubusercontent.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/master/img/schematic_1.jpg)](https://raw.githubusercontent.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/master/img/schematic_1.jpg)

<p style="text-align:center"><font color="green">您可以单击图片查看原始文件</font></p>


如您所见，GPIO14和GPIO15用于数据传输，我们使用GPIO18作为使能信号。


有关逻辑信号的定义，请参阅下表。

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/function_table.jpg)


---
**树莓派的母头**

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/pin_out/5.jpg)

我们使用2X13母头将此模块插入Raspberry Pi，请确保引脚对齐。

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/Pin_map_2.jpg)




---
**扩展树莓派的母头**

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/pin_out/6.jpg)

这个RS-485 Shield占用26个Raspberry Pi引脚，实际上只使用了5个GPIO引脚。如果您需要这些引脚用于其他目的，我们将这26个引脚取出。

>GPIO占用列表

GPIO编号|功能
:---:|---
GPIO02|	适用于Grove I2C端口的SDA
GPIO03|	用于Grove I2C端口的SCL
GPIO14|连接到Max485芯片的引脚DI，进行数据传输。
GPIO15|连接到Max485芯片的引脚RO，进行数据传输。
GPIO18|连接到Max485芯片的引脚RE和DE，用作使能信号。


---
**Grove I2C 接口**

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/pin_out/3.jpg)

我们保留了I2C接口，以便您可以轻松地将其与I2C设备配合使用。需要注意的是，该端口的VCC为5V，需要确认模块是否与5V电压兼容。

>SCL: I2C串行时钟，连接到Raspberry Pi的GPIO03。
>SDA: I2C串行数据，连接到Raspberry Pi的GPIO02。 
>VCC: 连接到Raspberry Pi 5V引脚。 
>GND: 连接到Raspberry Pi GND引脚。


<div class="page"/></div>

---
**Max485芯片**

![](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/pin_out/7.jpg)


我们使用MAX485ESA IC作为此屏蔽，有关该IC的更多详细信息，请查看 [MAX485数据手册](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/res/RS-485.pdf)



## 平台支持

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |



<div class="page"/></div>




## 入门

### 硬件

**所需材料**

|Raspberry pi|RS-485 Shield for Raspberry Pi|
|------------|-------------|
|![enter image description here](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/rasp.jpg)|![enter image description here](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/img/thumbnail.jpg)|
|[Get ONE Now](https://www.seeedstudio.com/Raspberry-Pi-3-Model-B-p-2625.html)|[Get ONE Now](https://www.seeedstudio.com)|



- **Step 1.** 将Raspberry Pi的RS-485 Shield插入Raspberry Pi。

- **Step 2.** 将485-A连接到485线A，将485-B连接到485线B.


!!!Note
        如果电线反转，则无法进行通信。


- **Step 3.** 使用micro-usb电缆为Raspberry Pi供电。



### 软件

#### 树莓派的串口配置

- **Step 1.** 运行`sudo raspi-config`去打开串口

![](https://github.com/SeeedDocument/RS-485-Shield-for-Raspberry-Pi/raw/master/img/Raspberry-Serial-Config-step1.png)

![](https://github.com/SeeedDocument/RS-485-Shield-for-Raspberry-Pi/raw/master/img/Raspberry-Serial-Config-step2.png)

- **Step 2.** 禁用系统服务以使用UART0

```bash
sudo systemctl disable hciuart 
```

!!!Note

    禁用蓝牙设备并将UART0 / ttyAMA0恢复为GPIO 14和15.还必须禁用初始化调制解调器的系统服务，以便它不使用UART

- **Step 3.** 删除cmdline.txt中的console = serial0,115200。

```bash
sudo nano /boot/cmdline.txt
```

然后从字符串中删除console = serial0,115200。

- **Step 4.** 重新启动

```bash
sudo reboot
```

#### 通信测试代码


您可以创建新的python文件并将以下代码复制到新文件中，也可以在资源下载区域下载源文件。然后在您的终端中运行它。



<div class="page"/></div>



**发送代码**


```Python

#!/usr/bin/env python

import time
import serial
import os
from gpiozero import LED

send_str = "*******rs485888888--\n"

ser = serial.Serial(port='/dev/ttyS0',baudrate =115200)

Tx_Enable = LED(18)
Tx_Enable.on()

while 1:
    ser.write(send_str)
    time.sleep(1)

```


<div class="page"/></div>


**接收代码**

```Python

#!/usr/bin/env python

import time
import serial
import os
from gpiozero import LED

ser = serial.Serial(port='/dev/ttyS0',baudrate =115200,timeout=1)
data = ''

Rx_Disable = LED(18)
Rx_Disable.off()

while True:
    str = ser.readall()  
    if str:  
        print str 

```


您需要两个shield和两个树莓来测试上面的代码，或者您可以使用PC中的串行工具与您的树莓派进行通信。

<div class="page"/></div>

## Resources

- **[Zip]** [RS-485 Shield for Raspberry Pi Eagle Files](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/res/RS485%20Shield%20for%20Raspberry%20Pi.zip)

- **[Zip]** [Python Test Code](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/res/Python_test.zip)

- **[PDF]** [MAX485 Datasheet](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/res/RS-485.pdf)

- **[PDF]** [PDF Format Wiki](https://github.com/SeeedDocument/RS-485_Shield_for_Raspberry_Pi/raw/master/res/RS-485_Shield_for_Raspberry_Pi.pdf)




## 技术支持

请不要犹豫，将问题提交到我们的[forum](https://forum.seeedstudio.com/) 或发送邮件至[techsupport@seeed.cc](techsupport@seeed.cc).
