---
title: Grove - Finger-clip Heart Rate Sensor with shell
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Finger-clip-Heart-Rate-Sensor-with-shell-p-2420.html
oldwikiname:  Grove - Finger-clip Heart Rate Sensor with shell
prodimagename: Grove-Finger-clip_Heart_Rate_Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Finger-clip_Heart_Rate_Sensor_with_shell 
sku: 101020082
---

![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor_with_shell.JPG)

Grove - Finger-clip Heart Rate Sensor with shell 基于 PAH8001EI-2G 研发的。它是一个高性能、低功耗的 CMOS 工艺光学传感器, 它带有绿色 LED，和集成 DSP 来实现心率检测 ( HRD ) 。该模块基于光学技术来测量血管中人体血液运动变化。低功耗和灵活的省电模式使其适用于可穿戴设备。因为心率传感器芯片需要高速处理速度的心率数据算法，这个模块集成了 STM32，保留 SWD 接口，允许用户重新编程 STM32。该模块还配备一个外壳和绷带，可以使用户轻松地将模块固定在手指，手腕或手臂上。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.60432862C4kvRR&id=520041095720)


##  规格参数
---
*   无触摸和移动时的超低功耗省电模式

*   灵活的睡眠率控制

*   集成 STM32F103

*   I2C 接口

*   心率传感器区域只有 3.0 x 4.7mm

*   SWD 接口保留

*   配有绷带和外壳

*   工作温度 : -20 to +60℃

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Finger-clip_Heart_Rate_Sensor_TOP.jpg) ![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Finger-clip_Heart_Rate_Sensor_Bottom.jpg)

*   1: Grove 接口

*   2: 保留 SWD 接口，用于编程到 STM32

*   3: 心率传感器

##  使用方法
---
在这里，我们将在此提供一个示例来向您展示如何使用该传感器。

###  硬件安装

将传感器连接到带有 Grove 线缆的 Seeeduino 的 I2C 端口。

![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor_with_shell_connect.jpg)

使用绷带将此模块固定在手指或手腕上时，请保持传感器区域与皮肤良好地接触并不要有动作，像图片那样。。

![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor_touch.jpg)
![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor_touch2.JPG)

##  软件部分

###  与 [Arduino](/w/index.php?title=Arduino&amp;action=edit&amp;redlink=1 "Arduino&amp;action=edit&amp;redlink=1") 一起使用

将以下代码复制到 Arduino 的新文件中，并上传代码，然后可以从串行监视器获取心率。
手指触摸传感器后可能需要大约一分钟才能获得有效的心率。

```
#include <Wire.h>
void setup() {
    Serial.begin(9600);
    Serial.println("heart rate sensor:");
    Wire.begin();
}
void loop() {
    Wire.requestFrom(0xA0 >> 1, 1);    // request 1 bytes from slave device
    while(Wire.available()) {          // slave may send less than requested
        unsigned char c = Wire.read();   // receive heart rate value (a byte)
        Serial.println(c, DEC);         // print heart rate value
    }
    delay(500);
}
```

###  与 [Mbed](/w/index.php?title=Mbed&amp;action=edit&amp;redlink=1 "Mbed&amp;action=edit&amp;redlink=1") 一起使用

从 I2C 设备读取一个字节 0xA0 ( 8 位地址 )，这就是心率。

```
#include "mbed.h"

I2C i2c(I2C_SDA, I2C_SCL);
const int addr = 0xA0;

int main() {
    char heart_rate;
    while (1) {
        i2c.read(addr, &heart_rate, 1);
        printf("heart rate: = %d\r\n", heart_rate);
    }
}
```

###  更新固件

我们可以通过引导程序来升级心率传感器的固件。

*   引导程序位于 0x08000000 - 0x08002000

*   应用程序位于 0x08002000 - 0x08020000

*   要启动引导程序，需要将 **SWDIO** 连接到 **GND** 并重置运行

![](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/img/Grove-Finger-clip_Heart_Rate_Sensor_boot_set.jpg)

*   接口 : UART ( Grove 接口支持 I2C 和 UART )，升级固件时，Grove 接口以 UART 模式运行。
VCC  -  VCC

GND  -  GND

SDA  -  TX

SCL  -  RX

*   UART 波特率 : 115200

*   协议 : ymodem (推荐工具是 Tera Term)

!!!NOTE
    The Grove - Finger-clip Heart Rate Sensor 提供心率测量。但是它不是医疗器械。要在手腕，手指或手掌上使用心率检测传感器，您必须 :
- (1)使传感器紧密地与您的皮肤接触，并在测量时保持稳定(无运动)以获得准确的心率。如果传感器在测量心率时，不能很好地接触皮肤或进行极端运动，那可能导致不能正确测量。
- (2)传感器的性能会在血流量更大时得到优化。 在寒冷的日子或用户的循环不畅(例如手脚冷)，传感器性能（心率准确度）可能会因测量位置的血流量较低而受到影响。

##  资源下载
---
*   **[Eagle文件]** [Grove - Finger-clip Heart Rate Sensor eagle file](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/res/Grove%20-%20Finger-clip%20Heart%20Rate%20Sensor%20eagle%20file.rar)

*   **[其他资源]** [Grove - Finger-clip Heart Rate Sensor bin file](https://github.com/SeeedDocument/Grove-Finger-clip_Heart_Rate_Sensor_with_shell/raw/master/res/Grove-Finger-clip_Heart_Rate_Sensor_bin.zip)
