---
title: Grove-TF Mini LiDAR
category: Sensor
bzurl: https://www.seeedstudio.com/Seeedstudio-Grove-TF-Mini-LiDAR-p-2996.html
oldwikiname: Grove-TF Mini LiDAR
prodimagename:
surveyurl: http://seeed.wiki/Grove-TF_Mini_LiDAR
sku: 114991434
tags: io_5v, plat_duino

---
![](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/img/Grove-TF-Mini-LiDAR.JPG)

该产品基于 ToF (Time of Flight) 原理，结合独特的光电设计，实现稳定，精确，高灵敏度，高速的距离检测。

ToF 是 Time of Flight (飞行时间) 技术的缩写，其工作原理如下 : 即传感器发出经调制的近红外光，遇物体后反射，传感器通过计算光线发射和反射时间差或相位差，来换算被拍摄景物的距离，以产生深度信息。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.64da35a6JET60o&id=561661551086)

!!!Warning
    防止灰尘或其他异物进入镜头; 否则会影响光线传输。


## 版本日志

| 产品版本              | 说明                                                                                                                                                                                    | 发布日期 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Grove-TF Mini LiDAR V1.0 | 首发 | 2017 年 11 月 |


## 规格参数
---
| 参数 | 值 |
|---------------------------------------------|----------------------------------|
| 检测距离范围                             | 0.3m-12m                         |
| 10% 反射率时的最大检测距离范围 | 5m                               |
| 平均功耗                   | 0.6W                            |
| 适用电压范围                    | 4.5V-6V                          |
| 验收角度                            | 2.3°                             |
| 最小分辨率                    | 1cm                              |
| 频率                                   | 100Hz                            |
| 准确度                                    | 1%   (6m 以下), 2% (6m-12m) |
| 距离检测单位                     | cm                               |
| 波长                                  | 850nm                            |
| 尺寸                                        | 42mm×15mm×16mm                   |
| 工作温度                       | -20℃-60℃                       |
| 感光性                           | 70,000lux                        |
| 质量                                      | 4.7g                             |
| 通信接口                     | UART 115200                      |
| LED 峰值电流                           | 800ma                            |
| 串口 TTL 电平               | 3.3V                              |
| 电磁兼容性 (EMC)          | EN 55032 Class B                  |

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

Platforms Supported
-------------------

## 入门指导
---
### 与 Arduino 一起使用

#### 硬件连接

- 步骤 1. 准备以下器材 :

| Seeeduino Lite |  Grove-TF Mini LiDAR |
|--------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/img/Seeed%20lite_S.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/img/Grove-TF-Mini-LiDAR_S.JPG)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.23496284BzrIs0&id=45487750521)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.11393bf8StVqql&id=561661551086)|

- 步骤 2. 将 Grove-TF Mini LiDAR 连接到 Seeeduino Lite 的串口端口。
- 步骤 3. 通过 USB 线缆将 Seeeduino 连接到 PC。

![](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/img/Seeeduino.JPG)

!!!Note
    如果您使用串口监视器来查看数据，请确保您的开发板有两个以上的硬件串口。Grove-TF Mini LiDAR 的 UART 波特率是 115200，但不支持 SoftwareSerial。所以如果我们使用 1 个硬件 UART 来挂接传感器然后其他硬件 UART 来进行串口显示，那么我们至少需要 2 个硬件串口 UART，比如 Arduino mega，Seeeduino lite等等。如果我们只有一个 UART 平台 (即 Seeeduino v4.2，Arduino uno)，我们可以使用 I2C LCD 作为显示器。


#### 软件部分

- 步骤 1. Grove-TF Mini LiDAR 是一个十六进制输出数据模块。每帧数据用 9 个字节编码，包括 1 个距离数据 (Dist)。每个距离数据都有相应的信号强度信息 (Strength)。帧结束是数据奇偶校验位。

| 字节号  | 数据编码解释                |
|-------|---------------------------------------------|
| Byte1 | 0x59, 帧头，所有帧都是一样的 |
| Byte2 | 0x59, 帧头，所有帧都是一样的 |
| Byte3 | Dist_L 距离值是一个低 8 位       |
| Byte4 | Dist_H 距离值是一个高 8 位      |
| Byte5 | Strength_L 是一个低 8 位的值                  |
| Byte6 | Strength_H 是一个高 8 位的值                |
| Byte7 | 积分时间                           |
| Byte8 | 保留字节                             |
| Byte9 | 校验位                             |


- 步骤 2. 复制代码至 Arduino IDE 并上传

```c
unsigned char dta[100];
unsigned char len = 0;

void setup()
{
    Serial1.begin(115200);
    Serial.begin(115200);
}

void loop()
{
    while(Serial1.available()>=9)
    {
        if((0x59 == Serial1.read()) && (0x59 == Serial1.read())) //Byte1 & Byte2
        {
            unsigned int t1 = Serial1.read(); //Byte3
            unsigned int t2 = Serial1.read(); //Byte4

            t2 <<= 8;
            t2 += t1;
            Serial.print(t2);
            Serial.print('\t');

            t1 = Serial1.read(); //Byte5
            t2 = Serial1.read(); //Byte6

            t2 <<= 8;
            t2 += t1;
            Serial.println(t2);

            for(int i=0; i<3; i++)
            {
                Serial1.read(); ////Byte7,8,9
            }
        }
    }
}
```

- 步骤 3. 我们将在串口绘图器上看到检测距离。蓝色曲线是距离，红色曲线是信号强度。

![](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/img/curve.png)

- 步骤 4. 我们也可以通过串口转 USB 转换器将传感器直接连接到 PC 的 USB 端口。我们可以使用 [Grove-TF-Mini-LiDAR Master Computer Software
](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/res/Grove-TF-Mini-LiDAR%20Master%20Computer%20Software.zip) 来监控距离和信号强度。  

## 资源下载
---
- **[芯片数据手册]** [Grove-TF-Mini-LiDAR
](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/res/DE-LiDAR%20TFmini%20Datasheet-V1.6-EN.pdf)
- **[其他资源]** [Grove-TF-Mini-LiDAR Master Computer Software
](https://github.com/SeeedDocument/Grove-TF_Mini_LiDAR/raw/master/res/Grove-TF-Mini-LiDAR%20Master%20Computer%20Software.zip)
