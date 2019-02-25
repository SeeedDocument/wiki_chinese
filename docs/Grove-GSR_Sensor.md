---
name: Grove - GSR Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-GSR-sensor-p-1614.html
oldwikiname: Grove_-_GSR_Sensor
prodimagename: GSR.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-GSR_Sensor
sku: 101020052
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/GSR.jpg)

GSR通过测量皮肤电流反应来测量皮肤电导率。 强烈的情绪会刺激你的交感神经系统，导致汗腺分泌更多的汗水。 Grove - GSR允许您通过简单地将两个电极连接到两个手指来发现这种强烈的情绪，它能够制作与情感有关的项目（如睡眠质量监视器），是一个很有趣的装备。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11uadbTx&id=45507098393)

## 版本信息
----
| 产品               | 发布日期  | 描述                               |
|------------------------|----------------|--------------------------------------------|
| Grove - GSR_Sensor V1.0     | 2013年6月19日      | 初始版本     |
| Grove - GSR_Sensor V1.2  | 2014年7月31日| 在M324PW-TSSOP14和GND之间增加C3 100nf |

## 规格参数
--------------

-   输入电压：5V / 3.3V
-   灵敏度可通过电位器调节
-   配置外部手指指套测量装置

!!!tip
    关于Grove模块的更多细节请参考[Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 支持平台
-------------------

## 入门指导
-------------

### 硬件连接

这里我们将向您展示如何通过一个简单的演示Groove - GSR。 首先，我们需要准备以下内容：


| Seeeduino V4.2 | Grove - GSR | Base Shield |Grove-RGB LCD Backlight |Grove-Buzzer |
|--------------|----------------------|-----------------|-----------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/img/Grove-GSR_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/img/Grove%20-%20LCD%20RGB%20Backlight_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/img/Grove-Button_s.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11uadbTx&id=45507098393)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|[马上购买](https://item.taobao.com/item.htm?spm=a1z09.8149145.0.0.20c2bcb9qprW6D&id=45475311124&_u=e2bmosps4601&qq-pf-to=pcqq.discussion)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11ZLdkgG&id=520245748676)|

- 使用Grove 通用 4针连接线将Grove-GSR连接到Grove - Base Shield上的 **A2**。
- 使用Grove 通用 4针连接线将Grove-Buzzer连接到Grove - Base Shield上的 **D3**。
- 使用Grove 通用 4针连接线将Grove-RGB LCD Backlight连接到Grove - Base Shield上的 **I2C**。
- 将 Base Shield插入到 Seeeduino-V4.2。
- 使用USB数据线将 Seeeduino-V4.2 连接到PC。

 ![](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/img/GSR_arduino_connection.jpg)

!!!Note
    如果没有Base Shield，请不用担心，传感器可以直接连接到Arduino。 请按照下面的表格连接Arduino。



| Grove-GSR Sensor | Arduino       |
|------------------|---------------|
| GND              | GND           |
| VCC              | VCC           |
| SIG              | A2            |
| NC               | 不连接 |


| Grove-Buzzer | Arduino       |
|--------------|---------------|
| GND          | GND           |
| VCC          | VCC           |
| SIG          | 3             |
| NC           |不连接 |

| Grove -RGB LCD Backlight | Arduino Uno |
|---------------------------|---------|
| GND                       | GND     |
| VCC                       | VCC     |
| SDA                       | A4      |
| SCL                       | A5      |

作为参考，下表显示了I2C引脚位于各种Arduino板上的位置。

| Board         | I2C  pins                      |
|---------------|--------------------------------|
| Uno, Ethernet | A4 (SDA), A5 (SCL)             |
| Mega2560      | 20 (SDA), 21 (SCL)             |
| Leonardo      | 2 (SDA), 3 (SCL)               |
| Due           | 20 (SDA), 21 (SCL), SDA1, SCL1 |


### 软件

我们需要下载Grove_LCD_RGB_Backlight库并安装到您的Arduino IDE。

- 请遵循 [如何安装arduino库](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/) 的步骤来安装RGB Backlight库。

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_LCD_RGB_Backlight/master/images/library.png)](https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip)

- 将下面的代码复制并粘贴到新的Arduino编辑器上并将其上传到Arduino。

```
#include <Wire.h>
#include "rgb_lcd.h"

    const int BUZZER=3;
    const int GSR=A2;
    int threshold=0;
    int sensorValue;
    rgb_lcd lcd;

    void setup(){
      long sum=0;
      lcd.begin(16, 2);
      Serial.begin(9600);
      pinMode(BUZZER,OUTPUT);
      digitalWrite(BUZZER,LOW);
      delay(1000);

      for(int i=0;i<500;i++)
      {
      sensorValue=analogRead(GSR);
      sum += sensorValue;
      delay(5);
      }
      threshold = sum/500;
       Serial.print("threshold =");
       Serial.println(threshold);
      }

    void loop(){
      int temp;
      sensorValue=analogRead(GSR);
      Serial.print("sensorValue=");
      Serial.println(sensorValue);
      lcd.setCursor(0, 0);
      lcd.print("GSR Value: ");
      lcd.print(sensorValue);
      temp = threshold - sensorValue;
      if(abs(temp)>50)
      {
        sensorValue=analogRead(GSR);
        temp = threshold - sensorValue;
        if(abs(temp)>50){
        digitalWrite(BUZZER,HIGH);
        Serial.println("YES!");
        delay(3000);
        digitalWrite(BUZZER,LOW);
        delay(1000);}
      }
      }

```

- 戴好指套并且保持放松，我们就可以从Grove_LCD_RGB_Backlight和串口中看到数据：

  ![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/GSR_Result_Data.jpg)


- 然后深吸一口气 蜂鸣器现在应该被触发。 而且应该可以观察到输出的数值有明显的变化。


## 参考
---------

有几个使用GSR数据在excel中创建的图表。 我们可以打开 [GSR sensor data](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/res/GSR_sensor_data.xls)查看详细数据.

- **深呼吸的时候**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/Reference_graphs1.png)

- **饥饿的时候**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/Reference_graphs3.png)

- **放轻松的时候**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/Reference_graphs2.png)

- **看到我老板来的时候**
![](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/img/Reference_graphs4.png)

## 资源下载
---------

- **[Eagle]** [Grove - GSR v1.0 Eagle File](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove-GSR_Eagle_File_V1.0.zip)
- **[PDF]** [Grove-GSR v1.0 Sch](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove%20-%20GSR%20v1.0%20SCH.pdf)
- **[PDF]** [Grove-GSR v1.0 PCB](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove%20-%20GSR%20v1.0%20PCB.pdf)
- **[Eagle]** [Grove - GSR v1.2 Eagle File](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove-GSR_Eagle_File_V1.2.zip)
- **[PDF]** [Grove-GSR v1.2 Sch](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove%20-%20GSR_v1.2_SCH.pdf)
- **[PDF]** [Grove-GSR v1.2 PCB](https://github.com/SeeedDocument/Grove-GSR_Sensor/raw/master/res/Grove%20-%20GSR_v1.2_PCB.pdf)
- **[Datasheet]** [LM324 datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/res/Lm324.pdf)
- **[Document]** [GSR sensor data](https://raw.githubusercontent.com/SeeedDocument/Grove-GSR_Sensor/master/res/GSR_sensor_data.xls "File:GSR sensor data.xls")


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_GSR_Sensor -->
