---
name: Grove - Time of Flight Distance Sensor-VL53L0X
category: 传感器
bzurl: https://www.seeedstudio.com/Grove-Temperature%26Humidity-Sensor-Pro-p-838.html
oldwikiname:
prodimagename:
surveyurl: https://www.surveymonkey.com/r/Grove_Temperature_and_Humidity_Sensor_Pro
sku: 101020532
tags: io_3v3, io_5v, plat_duino, plat_pi

---

![](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/img/main.JPG)




Grove - Time of Flight Distance Sensor-VL53L0X 是一款基于VL53L0X的高速，高精度和远程距离传感器。

VL53L0X是新一代飞行时间（ToF）激光测距模块，采用当今市场上最小的封装，无论目标反射率如何，都能提供精确的距离测量，这与传统技术不同。 它可以测量高达2米的绝对距离，为测距性能水平设定新的基准，为各种新应用打开了大门。

VL53L0X集成了领先的SPAD阵列（单光子雪崩二极管），并嵌入了ST的第二代FlightSenseTM专利技术。

VL53L0X的940 nm VCSEL发射器（VerticalCavity表面发射激光器）对人眼完全不可见，与内部物理红外滤光器配合使用，可实现更长距离，更高的环境光抗扰度以及更好的抗玻璃光学串扰。


<p style="text-align:center"><a href="https://www.seeedstudio.com/" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png" /></a></p>

## 产品特性

- **完全集成的微型模块**

	- 940 nm 激光 VCSEL
	- VCSEL 驱动
	- 测距传感器采用先进的嵌入式微控制器

- **快速，准确的距离测距**
	- 测量绝对范围可达2米
	- 报告的范围与目标反射率无关
	- 先进的嵌入式光学串扰补偿，简化了玻璃罩的选择

- **安全可视**
	- Class 1 激光器件  兼容最新的 IEC标准 60825-1:2014 - 3rd edition

- **易于集成**
	- 单可回流组件
	- 没有额外的光学
	- 单电源供电
	- I2C 接口留以控制和数据传输
	- X GPIO包括断电 重启 中断
	- 可编程 I2C地址


## 规格参数

特性|细节
---|---
工作电压|3.3V/5V
工作温度|-20℃ - 70℃
推荐测量距离|30mm-1000mm
分辨率|1mm
红外发射器|940 nm
总线速率最高400 kHz（快速模式）串行总线
IIC 地址|0x52



## 应用

- 用户检测个人电脑/笔记本电脑/平板电脑和物联网（节能）
- 机器人（障碍物检测）
- 白色家电（自动水龙头手动检测，肥皂分配器等）
- 1D 手势识别.
- 激光辅助自动对焦。 增强和加速相机自动对焦系统的性能，尤其是在困难场景（低光照水平，低对比度）或快速移动视频模式下。


## 支持平台


| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo_n.jpg) | ![](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo_n.jpg) |

!!!Caution
  上面提到的支持的平台是模块的硬件或理论兼容性的指示。 在大多数情况下，我们仅为Arduino平台提供软件库或代码示例。 无法为所有可能的MCU平台提供软件库/演示代码。 因此，用户必须编写自己的软件库。




## 入门指导

!!!Note
    如果这是您第一次使用Arduino，我们强烈建议您在开始前阅读[Getting Started with Arduino](http://wiki.seeedstudio.com/Getting_Started_with_Arduino/)



###  Arduino示例

#### 硬件

**物品准备**

| Seeeduino V4.2 | Base Shield| Grove - Time of Flight Distance Sensor |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/img/thumbnail.jpg)|
|<a href="http://www.seeedstudio.com/Seeeduino-V4.2-p-2517.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Base-Shield-V2-p-1378.html" target="_blank">Get One Now</a>|<a href="https://www.seeedstudio.com/Grove-Temperature%26Humidity-Sensor-Pro-p-838.html" target="_blank">Get One Now</a>|



!!!note
    **1** 请轻轻插入USB电缆，否则可能会损坏端口。 请使用4线内的USB线，2线电缆不能传输数据。 如果您不确定自己的电线，可以点击 [here](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) to buy

    **2** 购买时，每个Grove模块都配有Grove电缆。 如果您丢失了Grove电缆，可以单击 [here](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) 购买


	- **Step 1.** 将  Grove - Time of Flight Distance Sensor  与Seeeduino 的 **IIC** 接口连接。

	- **Step 2.** 将 Plug Grove - Base Shield 与seeeduino 拼接

	- **Step 3.** 将seeeduino和PC通过micro-USB连接.


![](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/img/connect.jpg)



!!!Note
如果我们没有Grove Base Shield，我们也可以直接将该传感器连接到Seeeduino，如下所示。


| Seeeduino       | Grove - Time of Flight Distance Sensor |
|---------------|-------------------------|
| 5V           | 红                     |
| GND           | 黑                   |
| SDA            | 白                   |
| SCL            | 黄                  |


#### 软件

- **Step 1.** 点击链接，从githun下载库和源码 [VL53L0X Library](https://github.com/Seeed-Studio/Grove-Ranging-sensor-VL53L0X)

- **Step 2.** 解压 `Grove-Ranging-sensor-VL53L0X-master.zip` 到`Arduino 的 libraries 文件夹`.

!!!Note
	例如，我将此库下载到`D：\ Software \ WorkWork \ arduino-1.8.5 \ libraries`中，因此只需要在此处解压缩zip文件。 总而言之，请确保`Grove-Ranging-sensor-VL53L0X-master`文件夹位于Arduino库文件夹中，如下图所示。

![](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/img/folder.png)


- **Step 3.** 打开刚刚提取的`Grove-Ranging-sensor-VL53L0X-master \ examples`文件夹，您将看到五个子文件夹：

![](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/img/examples.png)

根据自己的需要选择不同的例子。 然后双击`xxx.ino`文件打开Arduino IDE。

!!!Attention
	我们在示例中使用 `high_accuracy_ranging.ino` 文件


- **Step 4.**烧录代码到板子上. 如果您不知道如何烧录代码，请参阅 [How to upload code](http://wiki.seeedstudio.com/Upload_Code/).

- **Step 5. **单击**工具 - >串行监视器**打开Arduino IDE的 ** 串口监视器 **。 或者同时点击++ ctrl + shift + m ++键。 如果一切顺利，你会得到结果。


结果如下所示：

```
time of mesurement: 205
Measured distance:115 mm
time of mesurement: 205
Measured distance:117 mm
time of mesurement: 205
Measured distance:120 mm
time of mesurement: 205
Measured distance:125 mm
time of mesurement: 204
Measured distance:130 mm
time of mesurement: 205
Measured distance:138 mm
time of mesurement: 205
Measured distance:143 mm
time of mesurement: 205
Measured distance:144 mm
time of mesurement: 205
Measured distance:152 mm

```




## 资源下载


- **[ZIP]** [Grove-Time of Flight Distance Sensor VL53L0X Eagle files](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/res/Grove%20-%20Time%20of%20Flight%20Distance%20Sensor%20(VL53L0X).zip)
- **[PDF]** [VL53L0X User Manual](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/res/software-flow.pdf)
- **[PDF]** [VL53L0X Datasheet](https://github.com/SeeedDocument/Grove-Time_of_Flight_Distance_Sensor-VL53L0X-/raw/master/res/vl53l0x-datasheet.pdf)


## 技术支持
如果有问题请发邮件到 [techsupport@seeed.cc](techsupport@seeed.cc) 或者到论坛去提问 [forum](https://forum.seeedstudio.com/).
