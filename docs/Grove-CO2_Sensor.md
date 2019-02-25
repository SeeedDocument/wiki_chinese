---
name: Grove - CO2 Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-CO2-Sensor-p-1863.html
oldwikiname: Grove_-_CO2_Sensor
prodimagename: Grove_CO2_Sensor.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-CO2_Sensor
sku: 101020067
tags: grove_uart, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-CO2_Sensor/master/img/Grove_CO2_Sensor.jpg)

Grove - CO2 Sensor 模块是一款红外的高灵敏度与高分辨率的二氧化碳传感器。红外二氧化碳传感器 MH-Z16 是一种通用的小型传感器，采用非色散红外( NDIR )吸收法检测空气中二氧化碳的原理，具有良好的选择性，氧气依赖，寿命长，内置温度传感器，具有温度补偿，UART 输出便于使用。可广泛应用于高压交流电、室内空气质量检测、工业过程监控与安全、农业与畜牧业生产过程监控。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.2b000cc1zdAduU&id=45476707662)

<div class="admonition warning">
<p class="admonition-title">Caution</p>
请注意传感器值仅反映气体浓度在允许误差范围内的近似趋势，它不表示精确的气体浓度。 空气中某些部件的检测通常需要更精确和更昂贵的仪器，这些仪器不能用单个气体传感器来完成。 如果您的项目旨在以非常精确的水平获得气体浓度，那么我们不推荐使用这种气体传感器。
</div>

## 规格参数
-------------

-   测量的范围 0-2000PPM
-   分辨率为 1PPM 在 0-2000PPM 之间
-   精度 200PPM
-   准备时间 3 分钟
-   反应时间 < 90 秒
-   工作温度 0~50℃
-   工作湿度 0%~90%RH
-   存储温度 -20~60℃
-   工作电压 4.5~6VDC
-   当前最大电流小于 100mA，平均电流小于 50mA
-   UART 输出模式

!!!Tip
     关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## Platforms Supported
-------------------

## 操作示例
-------------

如下图将模块与 Grove Shield 连接使用，并使用下面的程序来获得电压。

请注意，传感器的最佳预热时间约为 180s。 有关传感器的详细信息，请参考芯片数据手册。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-CO2_Sensor/master/img/5.jpg)

```
/*
  This test code is write for Arduino AVR Series(UNO, Leonardo, Mega)
  If you want to use with LinkIt ONE, please connect the module to D0/1 and modify:

  // #include <SoftwareSerial.h>
  // SoftwareSerial s_serial(2, 3);      // TX, RX

  #define sensor Serial1
*/


#include <SoftwareSerial.h>
SoftwareSerial s_serial(2, 3);      // TX, RX

#define sensor s_serial

const unsigned char cmd_get_sensor[] =
{
    0xff, 0x01, 0x86, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x79
};

unsigned char dataRevice[9];
int temperature;
int CO2PPM;

void setup()
{
    sensor.begin(9600);
    Serial.begin(115200);
    Serial.println("get a 'g', begin to read from sensor!");
    Serial.println("********************************************************");
    Serial.println();
}

void loop()
{
    if(dataRecieve())
    {
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.print("  CO2: ");
        Serial.print(CO2PPM);
        Serial.println("");
    }
    delay(1000);
}

bool dataRecieve(void)
{
    byte data[9];
    int i = 0;

    //transmit command data
    for(i=0; i<sizeof(cmd_get_sensor); i++)
    {
        sensor.write(cmd_get_sensor[i]);
    }
    delay(10);
    //begin reveiceing data
    if(sensor.available())
    {
        while(sensor.available())
        {
            for(int i=0;i<9; i++)
            {
                data[i] = sensor.read();
            }
        }
    }

    for(int j=0; j<9; j++)
    {
        Serial.print(data[j]);
        Serial.print(" ");
    }
    Serial.println("");

    if((i != 9) || (1 + (0xFF ^ (byte)(data[1] + data[2] + data[3] + data[4] + data[5] + data[6] + data[7]))) != data[8])
    {
        return false;
    }

    CO2PPM = (int)data[2] * 256 + (int)data[3];
    temperature = (int)data[4] - 40;

    return true;
}
```

![](https://raw.githubusercontent.com/SeeedDocument/Grove-CO2_Sensor/master/img/Uart_co2.jpg)

## 校准
------------
如果您需要校准传感器，请将以下代码上传到您的 Arduino。

```
// Grove - Co2 Sensor calibration

#include <SoftwareSerial.h>
SoftwareSerial sensor(A5, A4);      // TX, RX


const unsigned char cmd_calibrate[] =
{
    0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2
};

void setup()
{
    sensor.begin(9600);
    Serial.begin(115200);
    Serial.println("begin to calibrate");

    for(int i=0; i<sizeof(cmd_calibrate); i++)
    {
        sensor.write(cmd_calibrate[i]);
    }

    Serial.println("calibrate done");
}

void loop()
{
    // nothing to do
}
```

!!!Warning
    请将传感器预热至少 5 分钟再进行校准，并确保传感器在新鲜空气中。

## 参考资料
---------

-   350~450ppm: 一般户外环境
-   350~1000ppm：空气清新，呼吸顺畅
-   1000~2000ppm：空气污浊让人昏昏欲睡
-   5000ppm：8 小时工作日允许接触的极限值

## 资源下载
---------

-   **[芯片数据手册]** [MH-Z16\_CO2 datasheet\_ZH\_CN.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-CO2_Sensor/master/res/MH-Z16_CO2.pdf)
-   **[芯片数据手册]** [MH-Z16\_CO2 datasheet\_EN.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-CO2_Sensor/master/res/MH-Z16_CO2_datasheet_EN.pdf)
-   **[其他资源]** [Health Risk Evaluation for Carbon Dioxide](http://www.blm.gov/style/medialib/blm/wy/information/NEPA/cfodocs/howell.Par.2800.File.dat/25apxC.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_CO2_Sensor -->
