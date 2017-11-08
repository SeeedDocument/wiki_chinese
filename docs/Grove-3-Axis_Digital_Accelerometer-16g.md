---
title: Grove - 3 Axis Digital Accelerometer(±16g)
category: Sensor
bzurl: <a href="https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer(%C2%B116g)-p-1156.html">https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer(%C2%B116g)-p-1156.html</a>
oldwikiname: Grove - 3 Axis Digital Accelerometer(±16g)
prodimagename: Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/Grove-3-Axis_16g_v1.3.jpg
wikiurl: http://seeed.wiki/Grove-3-Axis_Digital_Accelerometer-16g
sku: 101020054
---

---
![](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/Grove-3-Axis_16g_v1.3.jpg)


这是一种高精度数字加速度计，可提供最高 3.9mg / LSB 分辨率和高达 ±16g 测量范围。它基于先进的 3 轴 IC ADXL345。您无需担心自由落体实验对该模块造成损坏，它可以承受至多 10000g 的振动。此外，它可以灵敏地检查到相关信号，因而可以用于运动检测、手势检测和机器人学。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.5bd1190VbULj1&id=45505202190)


## 规格参数
---
- 输入电压 : 3.3V, 5V
- 测试范围 : ±16
- 高灵敏度
- 大测量范围
- 低功耗电源 0.1 μA(在标准模式下 VS = 2.5 V (典型值))
- 能承受 10,000 g 振动
- 符合 RoHS/WEEE 无铅标准
- Suli 标准兼容库

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 操作示例
---
**与 Arduino 一起使用**

每个加速度计已经在运送到您之前经过单独测试。但是在极少数情况下，您可能需要自行复位零点偏移。
下面我们将向您展示如何从该加速度计读取原始数据并以g，也就是重力为单位获取数据。

![](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/Grove_-_3-Axis_Digital_Accelerometer_ADXL345_connect_photo.JPG)

- **步骤 1 :** 将其插入您的 Grove - Base Shield 的 I2C 端口。
- **步骤 2 :** 下载 [Digital Accelerometer(±16g) Library](https://github.com/Seeed-Studio/Accelerometer_ADXL345) 并将其解压缩到 Arduino 安装文件夹中的 **arduino-1.0\libraries** 中。如果您不知道如何安装 Arduino 的库文件，请按照 [如何安装Arduino的库文件](/Tutorial/How_to_Install_an_Arduino_Library/) 进行操作。
- **步骤 3 :** 如果您安装了该库，请通过路径直接打开演示代码 :
** File(文件) -> Example(示例) ->DigitalAccelerometer_ADXL345->ADXL345_demo_code. **
- **步骤 4 :** 上传代码并打开串行监视器 ( 通常位于右上角 )。如果您不知道如何上传，请参阅 [上传代码指南](http://wiki.seeedstudio.com/wiki/Upload_Code) 。
- **步骤 5 :** 结果将显示为下图中的格式，摇动 Grove，您会发现数字变化。

![](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/Digital_Accelerometer.jpg)

该传感器的输出由两部分组成 : 原始数据和转换为以重力 'g' 为单位的 3 轴加速度信息。

**与 Raspberry Pi 一起使用**

- **步骤 1 :** 准备一个 Raspberry Pi 和 Grovepi 或 Grovepi +。

- **步骤 2 :** 您应该完成配置开发环境，否则请遵循[此处](http://wiki.seeedstudio.com/wiki/GrovePi+#Introducing_the_GrovePi.2B)。

![](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/C9-create-tab.png)

![](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/images/C9_newfile.jpg)

- **步骤 3 :** 连接
   - 将传感器用 Groov 线将插入 Grovepi 插座 i2c-x(1~3)。

- **步骤 4 :** 跳转到演示目录

```python
cd yourpath/GrovePi/Software/Python/
```
代码如下 :

```
  nano grovepi_tilt_switch.py   # "Ctrl+x" to exit #
```

```python
import smbus
from time import sleep

# select the correct i2c bus for this revision of Raspberry Pi
revision = ([l[12:-1] for l in open('/proc/cpuinfo','r').readlines() if l[:8]=="Revision"]+['0000'])[0]
bus = smbus.SMBus(1 if int(revision, 16) >= 4 else 0)

# ADXL345 constants
EARTH_GRAVITY_MS2   = 9.80665
SCALE_MULTIPLIER    = 0.004

DATA_FORMAT         = 0x31
BW_RATE             = 0x2C
POWER_CTL           = 0x2D

BW_RATE_1600HZ      = 0x0F
BW_RATE_800HZ       = 0x0E
BW_RATE_400HZ       = 0x0D
BW_RATE_200HZ       = 0x0C
BW_RATE_100HZ       = 0x0B
BW_RATE_50HZ        = 0x0A
BW_RATE_25HZ        = 0x09

RANGE_2G            = 0x00
RANGE_4G            = 0x01
RANGE_8G            = 0x02
RANGE_16G           = 0x03

MEASURE             = 0x08
AXES_DATA           = 0x32

class ADXL345:

    address = None

    def __init__(self, address = 0x53):
        self.address = address
        self.setBandwidthRate(BW_RATE_100HZ)
        self.setRange(RANGE_2G)
        self.enableMeasurement()

    def enableMeasurement(self):
        bus.write_byte_data(self.address, POWER_CTL, MEASURE)

    def setBandwidthRate(self, rate_flag):
        bus.write_byte_data(self.address, BW_RATE, rate_flag)

    # set the measurement range for 10-bit readings
    def setRange(self, range_flag):
        value = bus.read_byte_data(self.address, DATA_FORMAT)

        value &= ~0x0F;
        value |= range_flag;
        value |= 0x08;

        bus.write_byte_data(self.address, DATA_FORMAT, value)

    # returns the current reading from the sensor for each axis
    #
    # parameter gforce:
    #    False (default): result is returned in m/s^2
    #    True           : result is returned in gs
    def getAxes(self, gforce = False):
        bytes = bus.read_i2c_block_data(self.address, AXES_DATA, 6)

        x = bytes[0] | (bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)

        y = bytes[2] | (bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1<<16)

        z = bytes[4] | (bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1<<16)

        x = x * SCALE_MULTIPLIER
        y = y * SCALE_MULTIPLIER
        z = z * SCALE_MULTIPLIER

        if gforce == False:
            x = x * EARTH_GRAVITY_MS2
            y = y * EARTH_GRAVITY_MS2
            z = z * EARTH_GRAVITY_MS2

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        return {"x": x, "y": y, "z": z}

if __name__ == "__main__":
    # if run directly we'll just create an instance of the class and output
    # the current readings
    adxl345 = ADXL345()

    axes = adxl345.getAxes(True)
    print "ADXL345 on address 0x%x:" % (adxl345.address)
    print "   x = %.3fG" % ( axes['x'] )
    print "   y = %.3fG" % ( axes['y'] )
    print "   z = %.3fG" % ( axes['z'] )
```

- **步骤 5 :** 运行代码

```
    sudo python grove_tilt_switch.py
```

**与 Beaglebone Green 一起使用**

可以使用 Cloud9 IDE 开始编辑 BBG 上的程序。
作为熟悉 Cloud9 IDE 的简单练习，可以以创建一个简单的应用程序来闪烁 BeagleBone 上的 4 个用户可编程 LED 之一作为好的开始。

如果这是您第一次使用 Cloud9 IDE，请按照以下步骤。

- **步骤 1 :** 将 Grove - UART 插座设置为 Grove - GPIO 插座，只需按照此步骤即可。

- **步骤 2 :** 点击右上角的 "+" 创建一个新文件。

- **步骤 3 :** 将以下代码复制并粘贴到新选项卡中。

```python
import smbus
import time

bus = smbus.SMBus(1)

# ADXL345 device address
ADXL345_DEVICE = 0x53

# ADXL345 constants
EARTH_GRAVITY_MS2   = 9.80665
SCALE_MULTIPLIER    = 0.004

DATA_FORMAT         = 0x31
BW_RATE             = 0x2C
POWER_CTL           = 0x2D

BW_RATE_1600HZ      = 0x0F
BW_RATE_800HZ       = 0x0E
BW_RATE_400HZ       = 0x0D
BW_RATE_200HZ       = 0x0C
BW_RATE_100HZ       = 0x0B
BW_RATE_50HZ        = 0x0A
BW_RATE_25HZ        = 0x09

RANGE_2G            = 0x00
RANGE_4G            = 0x01
RANGE_8G            = 0x02
RANGE_16G           = 0x03

MEASURE             = 0x08
AXES_DATA           = 0x32

class ADXL345:

    address = None

    def __init__(self, address = ADXL345_DEVICE):
        self.address = address
        self.setBandwidthRate(BW_RATE_100HZ)
        self.setRange(RANGE_2G)
        self.enableMeasurement()

    def enableMeasurement(self):
        bus.write_byte_data(self.address, POWER_CTL, MEASURE)

    def setBandwidthRate(self, rate_flag):
        bus.write_byte_data(self.address, BW_RATE, rate_flag)

    # set the measurement range for 10-bit readings
    def setRange(self, range_flag):
        value = bus.read_byte_data(self.address, DATA_FORMAT)

        value &= ~0x0F;
        value |= range_flag;
        value |= 0x08;

        bus.write_byte_data(self.address, DATA_FORMAT, value)

    # returns the current reading from the sensor for each axis
    #
    # parameter gforce:
    #    False (default): result is returned in m/s^2
    #    True           : result is returned in gs
    def getAxes(self, gforce = False):
        bytes = bus.read_i2c_block_data(self.address, AXES_DATA, 6)

        x = bytes[0] | (bytes[1] << 8)
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)

        y = bytes[2] | (bytes[3] << 8)
        if(y & (1 << 16 - 1)):
            y = y - (1<<16)

        z = bytes[4] | (bytes[5] << 8)
        if(z & (1 << 16 - 1)):
            z = z - (1<<16)

        x = x * SCALE_MULTIPLIER
        y = y * SCALE_MULTIPLIER
        z = z * SCALE_MULTIPLIER

        if gforce == False:
            x = x * EARTH_GRAVITY_MS2
            y = y * EARTH_GRAVITY_MS2
            z = z * EARTH_GRAVITY_MS2

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        return {"x": x, "y": y, "z": z}

if __name__ == "__main__":
    # if run directly we'll just create an instance of the class and output
    # the current readings
    adxl345 = ADXL345()

    while True:
        axes = adxl345.getAxes(True)
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )
        time.sleep(2)
```

- **步骤 4 :** 单击磁盘图标以 .py 扩展名保存文件。

- **步骤 5 :** 将 Grove - 3-Axis Digital Accelerometer(±16g) 连接到 BBG 上的 Grove I2C 插座。

- **步骤 6 :** 运行代码，你会发现终端每 2 秒输出一次重力信息。

## 资源下载
---
- **[Eagle文件]** [Eagle file.zip](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/resources/202000067_PCBA-Grove%203%20Axis%20Digital%20Accelerometer%C2%B116g%20v1.2.zip)
- **[库文件]** [Suli-compatible Library](https://github.com/Seeed-Studio/ACC_Adxl345_Suli)
- **[芯片数据手册]** [ADXL345 datasheet.pdf](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/res/ADXL345_datasheet.pdf)
- **[其他文件]** [github repository for 3-Axis Digital Accelerometer(±16g)](https://github.com/Seeed-Studio/Accelerometer_ADXL345)
- **[其他文件]** [Grove - 3-Axis Digital Accelerometer(±16g)](https://github.com/SeeedDocument/Grove_3_Axis_Digital_Accelerometer_Plus_Minus_16g/raw/master/resources/DigitalAccelerometer_ADXL345.zip)
