---
title: Grove - IMU 9DOF (lcm20600+AK09918)
category: Sensor
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 101020585
tags:
---

![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/Main.jpg)

 Grove - IMU 9DOF (lcm20600+AK09918) 是拥有9个自由度的 [IMU](https://en.wikipedia.org/wiki/Inertial_measurement_unit) (惯性测量单元)，它集合了陀螺仪、加速规和电子罗盘的功能。我们使用了两个芯片 LCM20600+AK09918 来实现这三种功能。

 LCM20600 是一个6轴运动跟踪装置，它集合了3轴陀螺仪和3轴加速规。[陀螺仪](https://en.wikipedia.org/wiki/Gyroscope) 是用来测量或保持方向和角速度的装置，通常情况下，我们用它来测量旋转和扭曲。[加速规](https://en.wikipedia.org/wiki/Accelerometer) 是用于测量一定范围内加速的装置。

 AK09918 是一个3轴的 [电子罗盘](https://en.wikipedia.org/wiki/Magnetometer) 集成电路，它拥有高敏感度的霍尔传感器。我们使用电子罗盘来测量磁力，磁力为我们提供了方向信息。

 正如它的名字提示的，这一个小小的模块可以测量9个自由度：x/y/z 轴上的角速度，x/y/z 轴上的加速的，x/y/z 轴上的磁力。
 
 这是一个非常神奇的模块，马上开始用这个模块制作你的运动和定向系统吧😄




<p style="text-align:center"><a href="https://www.seeedstudio.com/Grove-IMU-9DOF-%28lcm20600%2BAK09918%29-p-3157.html" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>



## 产品特性


- 包含 ±250 dps, ±500 dps, ±1000 dps 和 ±2000 dps 可编程 FSR 的3轴陀螺仪
- 包含 ±2g, ±4g, ±8g 和 ±16g 可编程 FSR 的3轴加速规
- 精度为0.15 μT/LSB (典型值) 的 3轴电子罗盘
- 使用者可编程的中断
- 加速度测量有16位 ADC 解析度和可编程滤波器
- 磁测量有16位 ADC 解析度
- 1 KB 的 FIFO 缓冲区
- 内置的温度传感器
- 磁力传感器溢出监测功能
- 内置的振荡器提供了内部时钟信号


## 规格参数

|项目|数值|
|---|---|
|工作电压|3.3V / 5V|
|工作温度|-30°C 到 +85°C|
|陀螺仪满量程|±250 dps, ±500 dps, ±1000 dps, ±2000 dps|
|陀螺仪灵敏度比例因子|131 LSB/(dps)@±250 dps <br>65.5 LSB/(dps)@±500 dps <br>32.8 LSB/(dps)@±1000 dps <br>16.4 LSB/(dps)@±2000 dps|
|加速规满量程|±2g, ±4g, ±8g, ±16g|
|加速规灵敏度比例因子|16384 LSB/g@±2g <br>8192 LSB/g@±4g <br>4096 LSB/g@±8g <br>2048 LSB/g@±16g|
|磁力传感器满量程|±4912μT (典型值)|
|磁力传感器灵敏度|0.15μT (典型值)|
|接口|I^2^C|
|I^2^C 地址|**LCM20600** <br> 0x69(默认) <br> 0x68(可选) <br> **AK09918** <br> 0x0C|

## 应用场景

- 智能手机和平板电脑
- 可穿戴设备


## 硬件概述

### 引脚图

![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/pin_map_1_cn.png)

![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/pin_map_2_cn.png)



!!!Danger
        LCM20600 的默认 I2C 地址为 0x69，您可将其更改为 0x68。 中央的焊盘已连接到地址线，您可以通过切断并重焊连线来改变 I2C 地址。为了您与他人的安全，请小心使用刀具和焊枪。


### 原理图

**电源**

![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/schematic.jpg)

因为 LCM20600 的工作电压为 1.71V 到 3.45V，AK09918 的工作电压为 1.65V 到 1.95V，我们使用一电压转换芯片 **XC6206P182MR** 来为他们提供稳定的 1.8V 电压。

**双向电平转换电路**

![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/schematic_1.jpg)


这是一个典型的双向电平转换器电路，用来连接 I2C 总线的两个不同的电压区。此感应器中的 I2C 总线使用 1.8V 电压, 若 Arduino 中的 I2C 总线使用 5V 或 3.3V 电压, 您就会需要此电路。上面的原理图中， Q1 和 Q2 是一个N通道的 MOSFET [CJ2102](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/res/CJ2102.pdf)，在这里承担双向开关的角色。为了更好地理解此部分，您可以查阅 [AN10441](https://github.com/SeeedDocument/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/raw/master/res/AN10441.pdf).


## 支持平台

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |


!!!Caution
    以上列出的支持平台仅代表硬件和理论的兼容性。大部分情况下我们仅提供 Arduino 平台的软件库和代码示例。为所有的MCU平台提供软件库和示例代码是不可能的。因此，使用者可能需要写出自己使用的软件库。



## 入门指导


### 搭配 Arduino 一起使用


#### 硬件连线

**硬件清单**

| Seeeduino V4.2 | Base Shield | Grove - IMU 9DOF |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">点击购买</a>|<a href="https://www.seeedstudio.com/Grove-IMU-9DOF-%28lcm20600%2BAK09918%29-p-3157.html" target="_blank">点击购买</a>|


!!!note
    **1** 请小心插入USB线缆，否则您可能会损坏端口。请使用4线的USB线缆，2线的USB线缆无法传输数据。若果您不确定您拥有的是哪种USB线缆，可以 [点击此处](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) 购买。
    
    **2** 在您购买时，每个 Grove 模块都附带一根 Grove 线缆。若您丢失了该线缆，可以 [点击此处](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) 购买。



- **步骤一** 将 Grove - IMU 9DOF (lcm20600+AK09918) 连接到 Grove-Base Shield（扩展板）的 **I^2^C** 端口。

- **步骤二** 将 Grove - Base Shield 插到 Seeeduino 上。

- **步骤三** 通过 USB 线缆将 Seeeduino 连接到 PC。


![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/connect.jpg)


!!!Note
        如果您没有 Grove Base Shield，您也可以按照以下方式将此模块连接到 Seeeduino 上


| Seeeduino     |  Grove - IMU 9DOF       |
|---------------|-------------------------|
| 5V            | 红色                     |
| GND           | 黑色                  |
| SDA           | 白色                   |
| SCL           | 黄色                  |


#### 软件运行


!!!Note
        如果这是您第一次使用 Arduino， 我们强烈推荐您在开始之前阅读 [Arduino 入门](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)。


- **步骤一** 从 GitHub 下载 [Grove - IMU 9DOF (lcm20600+AK09918)](https://github.com/Seeed-Studio/Seeed_ICM20600_AK09918) 软件库。

- **步骤二** 查阅 [如何安装软件库](http://wiki.seeedstudio.com/How_to_install_Arduino_Library) 后安装软件库到 Arduino IDE。

- **步骤三** 重启 Arduino IDE。您可按照以下三种方式打开示例：
    1. 通过路径 **File --> Examples --> Grove IMU 9DOF ICM20600 AK09918 --> compass** 在 Arduino IDE 中直接打开。
    ![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/path.jpg)
    
    2. 在文件夹  **XXXX\Arduino\libraries\Seeed_ICM20600_AK09918-master\examples\compass** 中点击打开 **compass.ino**，**XXXX** 是您安装 Arduino IDE 的目录。
    ![](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/img/path_1.jpg)
    
    3. 又或者，您可以点击代码块右上角的图标 ![](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/copy.jpg) 将代码复制到 Arduino IDE 的新文件中去。


```C++
#include "AK09918.h"
#include "ICM20600.h"
#include <Wire.h>

AK09918_err_type_t err;
int32_t x, y, z;
AK09918 ak09918;
ICM20600 icm20600(true);
int16_t acc_x, acc_y, acc_z;
int32_t offset_x, offset_y, offset_z;
double roll, pitch;
// Find the magnetic declination at your location
// http://www.magnetic-declination.com/
double declination_shenzhen = -2.2;

void setup()
{
    // join I2C bus (I2Cdev library doesn't do this automatically)
    Wire.begin();

    err = ak09918.initialize();
    icm20600.initialize();
    ak09918.switchMode(AK09918_POWER_DOWN);
    ak09918.switchMode(AK09918_CONTINUOUS_100HZ);
    Serial.begin(9600);

    err = ak09918.isDataReady();
    while (err != AK09918_ERR_OK) 
    {
        Serial.println("Waiting Sensor");
        delay(100);
        err = ak09918.isDataReady();
    }

    Serial.println("Start figure-8 calibration after 2 seconds.");
    delay(2000);
    calibrate(10000, &offset_x, &offset_y, &offset_z);
    Serial.println("");
}

void loop()
{
    // get acceleration
    acc_x = icm20600.getAccelerationX();
    acc_y = icm20600.getAccelerationY();
    acc_z = icm20600.getAccelerationZ();

    Serial.print("A:  ");
    Serial.print(acc_x);
    Serial.print(",  ");
    Serial.print(acc_y);
    Serial.print(",  ");
    Serial.print(acc_z);
    Serial.println(" mg");

    Serial.print("G:  ");
    Serial.print(icm20600.getGyroscopeX());
    Serial.print(",  ");
    Serial.print(icm20600.getGyroscopeY());
    Serial.print(",  ");
    Serial.print(icm20600.getGyroscopeZ());
    Serial.println(" dps");

    ak09918.getData(&x, &y, &z);
    x = x - offset_x;
    y = y - offset_y;
    z = z - offset_z;

    Serial.print("M:  ");
    Serial.print(x);
    Serial.print(",  ");
    Serial.print(y);
    Serial.print(",  ");
    Serial.print(z);
    Serial.println(" uT");

    // roll/pitch in radian
    roll = atan2((float)acc_y, (float)acc_z);
    pitch = atan2(-(float)acc_x, sqrt((float)acc_y*acc_y+(float)acc_z*acc_z));
    Serial.print("Roll: ");
    Serial.println(roll*57.3);
    Serial.print("Pitch: ");
    Serial.println(pitch*57.3);

    double Xheading = x * cos(pitch) + y * sin(roll) * sin(pitch) + z * cos(roll) * sin(pitch);
    double Yheading = y * cos(roll) - z * sin(pitch);
    

    double heading = 180 + 57.3*atan2(Yheading, Xheading) + declination_shenzhen;

    Serial.print("Heading: ");
    Serial.println(heading);
    Serial.println("--------------------------------");
  
    delay(500);
    
}

void calibrate(uint32_t timeout, int32_t *offsetx, int32_t *offsety, int32_t*offsetz)
{
  int32_t value_x_min = 0;
  int32_t value_x_max = 0;
  int32_t value_y_min = 0;
  int32_t value_y_max = 0;
  int32_t value_z_min = 0;
  int32_t value_z_max = 0;
  uint32_t timeStart = 0;

  ak09918.getData(&x, &y, &z);

  value_x_min = x;
  value_x_max = x;
  value_y_min = y;
  value_y_max = y;
  value_z_min = z;
  value_z_max = z;
  delay(100);

  timeStart = millis();
  
  while((millis() - timeStart) < timeout)
  {
    ak09918.getData(&x, &y, &z);
    
    /* Update x-Axis max/min value */
    if(value_x_min > x)
    {
      value_x_min = x;
      // Serial.print("Update value_x_min: ");
      // Serial.println(value_x_min);

    } 
    else if(value_x_max < x)
    {
      value_x_max = x;
      // Serial.print("update value_x_max: ");
      // Serial.println(value_x_max);
    }

    /* Update y-Axis max/min value */
    if(value_y_min > y)
    {
      value_y_min = y;
      // Serial.print("Update value_y_min: ");
      // Serial.println(value_y_min);

    } 
    else if(value_y_max < y)
    {
      value_y_max = y;
      // Serial.print("update value_y_max: ");
      // Serial.println(value_y_max);
    }

    /* Update z-Axis max/min value */
    if(value_z_min > z)
    {
      value_z_min = z;
      // Serial.print("Update value_z_min: ");
      // Serial.println(value_z_min);

    } 
    else if(value_z_max < z)
    {
      value_z_max = z;
      // Serial.print("update value_z_max: ");
      // Serial.println(value_z_max);
    }
    
    Serial.print(".");
    delay(100);

  }

  *offsetx = value_x_min + (value_x_max - value_x_min)/2;
  *offsety = value_y_min + (value_y_max - value_y_min)/2;
  *offsetz = value_z_min + (value_z_max - value_z_min)/2;
}
```


!!!Note
        软件库中有三份示例代码：
        **test_6axis**
        >此示例展示了如何从 ICM20600 得到陀螺仪和加速度数据。
        
        **test_magnet**  
        >此示例展示了如何从 AK09918 得到磁力数据。
        
        **compass**  
        >此示例得到磁力和加速度数据后，计数 pitch 和 roll，制作出一个罗盘应用。



- **步骤四** 上传您的代码。若您不知道如何上传，请阅读文章 [如何上传代码](http://wiki.seeedstudio.com/Upload_Code/)。

- **步骤五** 点击 **Tool-> Serial Monitor** 打开 Arduino IDE 中的 **Serial Monitor**。或同时按下 ++ctrl+shift+m++ 键。将波特率设为 **9600**.

!!!success
     若一切顺利，当您打开 Serial Monitor，将有提示信息弹出--*Start figure-8 calibration after 2 seconds.* 也就是说为了校准此模块，您应当移动它并在空中移动一个数字 8 的轨迹。当出现 “.......” 时，即可开始校准。 


```C++
Start figure-8 calibration after 2 seconds.
.......................................................................
A:  -362,  -205,  738 mg
G:  -45,  12,  -1 dps
M:  -6,  -23,  -33 uT
Roll: -15.53
Pitch: 25.30
Heading: 23.99
--------------------------------
A:  -269,  583,  61 mg
G:  102,  377,  -2 dps
M:  18,  -21,  -18 uT
Roll: 84.03
Pitch: 24.65
Heading: 215.58
--------------------------------
A:  -495,  229,  37 mg
G:  -43,  -231,  201 dps
M:  7,  -30,  6 uT
Roll: 80.83
Pitch: 64.90
Heading: 21.76
--------------------------------

```



!!!Note
        如您所见，罗盘示例的结果包含了三个参数：Roll（翻滚角），Pitch（俯仰角） 和 Heading（方位角）。它们是 **[姿态角](https://en.wikipedia.org/wiki/Euler_angles)** 中的术语(点击查阅信息).



#### 函数表

|函数|说明|
|---|---|
|**ICM20600**|| 
|initialize()|初始化芯片 LCM20600，默认情况下： <br> 陀螺仪的测量范围为 ±2000 dps <br> 加速规的测量范围为 ±16g|
|setGyroScaleRange(gyro_scale_type_t range)|初始化之后，您可以设置您需要的陀螺仪测量范围。参数 gyro_scale_type_t 范围表为:<br> **RANGE_250_DPS** <br> **RANGE_500_DPS** <br> **RANGE_1K_DPS** <br> **RANGE_2K_DPS**  <br> 如， <br>  **icm20600.setGyroScaleRange(RANGE_1K_DPS);** <br> 此行代码将陀螺仪的测量范围设定为 ±1000dps|
|setAccScaleRange(acc_scale_type_t range)|初始化之后，您可以设置您需要的加速规测量范围，参数 acc_scale_type_t 范围表为:<br> **RANGE_2G** <br> **RANGE_4G** <br> **RANGE_8G** <br> **RANGE_16G**  <br> 如， <br>  **icm20600.setAccScaleRange(RANGE_8G);** <br> 此行代码将加速规的测量范围设为 ±8g|
|getGyroscope(int16_t* x, int16_t* y, int16_t* z))|通过此函数，您可以同时得到陀螺仪在 X/Y/Z 3个轴上的数据，此数据的单位为 **dps**|
|getGyroscopeX(void)<br> getGyroscopeY(void) <br> getGyroscopeZ(void)|或者，您可以使用这3个函数分别得到陀螺仪 X/Y/Z 3个轴上的数据，此数据的单位为 **dps** |
|getRawGyroscopeX(void) <br> getRawGyroscopeX(void) <br> getRawGyroscopeX(void)|这三个函数得到 ICM20600 寄存器上的原始数据，且并未将单位转换为 **dps**|
|getAcceleration(int16_t* x, int16_t* y, int16_t* z)|通过此函数，您可以同时得到在 X/Y/Z 3个轴上的加速度数据，此数据的单位为 **mg**|
|getAccelerationX(void)<br> getAccelerationY(void) <br> getAccelerationZ(void)|或者，您可以使用这3个函数分别得到 X/Y/Z 3个轴上的加速度数据，此数据的单位为 **mg** |
|getRawAccelerationX(void) <br> getRawAccelerationY(void) <br> getRawAccelerationZ(void)|这三个函数从 ICM20600 的寄存器得到原始数据，且并未将其单位转换为 **mg**|
|getTemperature(void)|您可通过此函数得到温度数据|
|**AK09918**||
|getData(int32_t *axis_x, int32_t *axis_y, int32_t *axis_z)  |您可通过此函数得到3个轴上的磁力大小|



## 资源下载

- **[Zip]** [Grove - IMU 9DOF (lcm20600+AK09918) 原理图](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/res/Grove%20-%20IMU%209DOF%20(ICM20600%20%26%20AK09918).zip)

- **[Zip]** [Seeed ICM20600+AK09918 软件库](https://github.com/Seeed-Studio/Seeed_ICM20600_AK09918/archive/master.zip)

- **[PDF]** [ICM-20600 数据手册](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/res/ICM-20600.pdf)

- **[PDF]** [AK09918 数据手册](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/res/AK09918.pdf)

- **[PDF]** [CJ2102 数据手册](https://github.com/SeeedDocument/Grove-IMU_9DOF-lcm20600_AK09918/raw/master/res/CJ2102.pdf)


## 项目

这是本产品的介绍视频，有简单代码展示，您可以一试。

<iframe width="560" height="315" src="https://www.youtube.com/embed/oFmvKxoZIuw?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


## 技术支持
欢迎您将您的问题提交至我们的 [论坛](https://forum.seeedstudio.com/)。
