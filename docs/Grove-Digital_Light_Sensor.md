---
name: Grove - Digital Light Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Digital-Light-Sensor-p-1281.html
oldwikiname: Grove_-_Digital_Light_Sensor
prodimagename:
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Digital_Light_Sensor
sku: 101020030
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Digital_Light_Sensor.jpg)

该模块基于将光强度转换为数字信号的 I2C光数转换器 TSL2561。 与传统的模拟光传感器不同， [Grove - Light Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.23a22b6bMJgSHP&id=45507034521) 该数字模块由于它有双重光敏二极管：红外和全光谱的，所有具有可择光谱范围功能。

我们可以在三种检测模式之间切换读取数据。 它们是红外模式，全光谱和人类可见模式。 当在人类可视模式下运行时，该传感器显示的读数恰好接近您的眼睛感觉。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.23a22b6bMJgSHP&id=45507034521)


## 产品特性
--------


- 可选择检测模式
- 在 400 kHz I2C 快速模式下，能够保持高分辨率的以 16 位数字信号输出
- 宽动态范围：0.1 - 40,000 LUX
- 宽工作温度范围：-40°C至85°C
- 具有可编程的中断功能，用户可以自行定义上限和下限的阈值

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
--------------

| 项目                    | 最小  |   标准 |  最大  |  单位 |
|----------------------------|------|----------|-------|-------|
| 电源电压，VDD      | 3.3  |     5    |  5.1  |   V   |  
| 工作温度      | -30  |     \    |  70   |   ℃      |
| SCL，SDA输入低电压  | -0.5 |     \    |  0.8  |   V   |
| SCL，SDA输入高电压 | 2.3  |     \    |  5.1  |   V   |

## Platforms Supported
-------------------

## 硬件概述
------------------

![](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/hardware%20overview.jpg)

**U1:** TSL2561 IC，光数字转换器。 这是功能框图
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Functional_Block_Diagram_2.jpg)
- **寄存器图表**

 TSL2561由16个寄存器（3个保留）和通过串行接口访问命令寄存器来实现进行控制和监视的。 这些寄存器提供各种控制功能，可以读取准确的 ADC 转换结果。 寄存器集合如下所示。

  ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Register.jpg)

  -  **频谱响应曲线**

  ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Spectral_responsivity.jpg)

Digital light sensor 的两个通道具有不同的响应特性。 这就是为什么你可以选择它们的工作模式的原因，因为他们可以同时工作，也可以只有其中一个工作。

**U3:** XC6206MR332 IC，正稳压器。

**Q1,Q2:** BSN20 IC，N沟道增强型垂直D-MOS晶体管。

**SCL,SDA:** I2C信号接口


## 入门指导
------

### 使用 Arduino

#### 硬件连接
在这里，我们将通过一个简单的演示向您展示 Grove - Digital light sensor 的工作原理。 首先，我们需要准备以下内容：

| Seeeduino V4 | Grove - Digital light sensor | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/digital%20light%20sensor_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.23a22b6bMJgSHP&id=45507034521)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|



- 将 Grove - Digital light Sensor 连接到 Base shield 的 **I2C** 端口。
- 将 Base shield 插入 Arduino。
- 使用 USB 数据线将 Arduino 连接到 PC。

![](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/arduino%20connection.jpg)

#### 程序

- 从这里下载库文件 [Digital Light Sensor 库](https://github.com/Seeed-Studio/Grove_Digital_Light_Sensor/archive/master.zip);
- 如果您是第一次安装 Arduino 库文件，请点击 [这里](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/) 查看库文件的安装方法。
- 通过路径直接打开代码： **File（文件） -> Example（示例） ->Digital_Light_Sensor->Digital_Light_Sensor**.

![](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/library%20example.jpg)

- 或将以下代码复制到IDE并上传到Arduino。
```      
    /*
     * Digital_Light_Sensor.ino
     * A library for TSL2561
     *
     * Copyright (c) 2012 seeed technology inc.
     * Website    : www.seeed.cc
     * Author     : zhangkun
     * Create Time:
     * Change Log :
     *
     * The MIT License (MIT)
     *
     * Permission is hereby granted, free of charge, to any person obtaining a copy
     * of this software and associated documentation files (the "Software"), to deal
     * in the Software without restriction, including without limitation the rights
     * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     * copies of the Software, and to permit persons to whom the Software is
     * furnished to do so, subject to the following conditions:
     *
     * The above copyright notice and this permission notice shall be included in
     * all copies or substantial portions of the Software.
     *
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

    #include <Wire.h>
    #include <Digital_Light_TSL2561.h>
    void setup()
    {
      Wire.begin();
      Serial.begin(9600);
      TSL2561.init();
    }

    void loop()
    {
      Serial.print("The Light value is: ");
      Serial.println(TSL2561.readVisibleLux());
      delay(1000);
    }
```

- 打开串行监视器来看监视的结果。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Digital_Light_Sensor_Score_Picture.jpg)


### 使用 Raspberry Pi

#### 硬件连接

首先，我们需要准备以下内容：

| Raspberry pi | Grove - Digital light sensor | GrovePi_Plus |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/digital%20light%20sensor_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11zpryre&id=528322046763)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.23a22b6bMJgSHP&id=45507034521)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e113G7Bdt&id=45506190895)|


- 您需要完成配置开发环境，否则遵循 [说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。
- 使用 grove 连接线将传感器插入 Grovepi + 插座 **I2C**。

![](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/img/pi%20connection.jpg)

#### 程序

- 导航到演示目录：
```
    cd yourpath/GrovePi/Software/Python/grove_i2c_digital_light_sensor/
```
-   找到这行代码

```
    nano grove_i2c_digital_light_sensor.py  # "Ctrl+x" to exit #
```
```
    import time
    import smbus
    from Adafruit_I2C import Adafruit_I2C
    import RPi.GPIO as GPIO
    import grovepi
    from smbus import SMBus

    global I2C_ADDRESS
    global I2C_SMBUS
    global _CMD
    global _CMD_CLEAR
    global _CMD_WORD
    global _CMD_BLOCK
    global _REG_CONTROL
    global _REG_TIMING
    global _REG_ID
    global _REG_BLOCKREAD
    global _REG_DATA0
    global _REG_DATA1
    global _POWER_UP
    global _POWER_DOWN
    global _GAIN_LOW
    global _GAIN_HIGH
    global _INTEGRATION_START
    global _INTEGRATION_STOP
    global _INTEGRATE_13
    global _INTEGRATE_101
    global _INTEGRATE_402
    global _INTEGRATE_DEFAULT
    global _INTEGRATE_NA
    global _GAIN
    global _MANUAL
    global _INTEG
    global _CHANNEL0
    global _CHANNEL1
    global _D0
    global _D1
    global _LUX


    # bus parameters
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        I2C_SMBUS = smbus.SMBus(1)
    else:
        I2C_SMBUS = smbus.SMBus(0)

    # Default I2C address
    I2C_ADDRESS = 0x29

    # Commands
    _CMD       = 0x80
    _CMD_CLEAR = 0x40
    _CMD_WORD  = 0x20
    _CMD_BLOCK = 0x10

    # Registers
    _REG_CONTROL   = 0x00
    _REG_TIMING    = 0x01
    _REG_ID        = 0x0A
    _REG_BLOCKREAD = 0x0B
    _REG_DATA0     = 0x0C
    _REG_DATA1     = 0x0E

    # Control parameters
    _POWER_UP   = 0x03
    _POWER_DOWN = 0x00

    # Timing parameters
    _GAIN_LOW          = 0b00000000
    _GAIN_HIGH         = 0b00010000
    _INTEGRATION_START = 0b00001000
    _INTEGRATION_STOP  = 0b00000000
    _INTEGRATE_13      = 0b00000000
    _INTEGRATE_101     = 0b00000001
    _INTEGRATE_402     = 0b00000010
    _INTEGRATE_DEFAULT = _INTEGRATE_402
    _INTEGRATE_NA      = 0b00000011

    # Testing parameters
    ambient  = None
    IR       = None
    _ambient = 0
    _IR      = 0
    _LUX     = None


    class Tsl2561(object):
            i2c = None

            def _init__(self, bus = I2C_SMBUS, addr = I2C_ADDRESS, debug = 1, pause = 0.8):  # set debug = 0 stops debugging output on screen
                    assert(bus is not None)
                assert(addr > 0b000111 and addr < 0b1111000)

                    self.i2c     = Adafruit_I2C(addr)
                    self.pause   = pause
                    self.debug   = debug
                    self.gain    = 0
                self._bus    = bus
                    self._addr   = addr

                ambient        = None
                    IR             = None
                self._ambient  = 0
                    self._IR       = 0
                self._LUX      = None
                    self._control(_POWER_UP)
                    self._partno_revision()

    #        @property

            def _lux(self, gain):
                    '''
                    Returns a lux value.  Returns None if no valid value is set yet.
                    '''
                    var = readLux(gain)
                    ambient = var[0]
                    IR = var[1]
                    self._ambient = var[2]
                    self._IR = var[3]
                    self_LUX = var[4]
                    return (ambient, IR, self._ambient, self._IR, self._LUX)


            def setGain(self, gain = 1):
                    """ Set the gain """
                    if (gain != self.gain):
                            if (gain==1):
                                    cmd = _CMD | _REG_TIMING
                                    value = 0x02
                                    self.i2c.write8(cmd, value)  # Set gain = 1X and timing = 402 mSec
                                    if (self.debug):
                                            print "Setting low gain"
                            else:
                                    cmd = _CMD | _REG_TIMING
                                    value = 0x12
                                    self.i2c.write8(cmd, value)  # Set gain = 16X and timing = 402 mSec
                                    if (self.debug):
                                            print "Setting high gain"
                            self.gain=gain;  # Safe gain for calculation
                            time.sleep(self.pause)  # Pause for integration (self.pause must be bigger than integration time)


            def readWord(self, reg):
                    """ Reads a word from the TSL2561 I2C device """
                    try:
                            wordval = self.i2c.readU16(reg)
                            newval = self.i2c.reverseByteOrder(wordval)
                            if (self.debug):
                                    print("I2C: Device 0x%02X: returned 0x%04X from reg 0x%02X" % (self._addr, wordval & 0xFFFF, reg))
                            return newval
                    except IOError:
                            print("Error accessing 0x%02X: Chcekcyour I2C address" % self._addr)
                            return -1


            def readFull(self, reg = 0x8C):
                    """ Read visible + IR diode from the TSL2561 I2C device """
                    return self.readWord(reg);

            def readIR(self, reg = 0x8E):
                    """ Reads only IR diode from the TSL2561 I2C device """
                    return self.readWord(reg);

            def readLux(self, gain = 0):
                    """ Grabs a lux reading either with autoranging (gain=0) or with specific gain (1, 16) """
                    if (self.debug):
                            print "gain = ", gain
                    if (gain == 1 or gain == 16):
                            self.setGain(gain)  # Low/highGain
                            ambient = self.readFull()
                            IR = self.readIR()
                    elif (gain == 0):  # Auto gain
                            self.setGain(16)  # First try highGain
                            ambient = self.readFull()
                            if (ambient < 65535):
                                    IR = self.readIR()
                            if (ambient >= 65535 or IR >= 65535):  # Value(s) exeed(s) datarange
                                    self.setGain(1)  # Set lowGain
                                    ambient = self.readFull()
                                    IR = self.readIR()

                    # If either sensor is saturated, no acculate lux value can be achieved.
                    if (ambient == 0xffff or IR == 0xffff):
                    self._LUX = None
                    self._ambient = None
                    self._IR = None
                    return (self.ambient, self.IR, self._ambient, self._IR, self._LUX)
                    if (self.gain == 1):
                            self._ambient = 16 * ambient  # Scale 1x to 16x
                            self._IR = 16 * IR            # Scale 1x to 16x
                    else:
                            self._ambient = 1 * ambient
                            self._IR = 1 * IR
                    if (self.debug):
                            print "IR Result without scaling: ", IR
                            print "IR Result: ", self._IR
                            print "Ambient Result without scaling: ", ambient
                            print "Ambient Result: ", self._ambient

                    if (self._ambient == 0):
                    # Sometimes, the channel 0 returns 0 when dark ...
                    self._LUX = 0.0
                    return (ambient, IR, self._ambient, self._IR, self._LUX)

                    ratio = (self._IR / float(self._ambient))  # Change to make it run under python 2

                    if (self.debug):
                            print "ratio: ", ratio

                    if ((ratio >= 0) and (ratio <= 0.52)):
                            self._LUX = (0.0315 * self._ambient) - (0.0593 * self._ambient * (ratio ** 1.4))
                    elif (ratio <= 0.65):
                            self._LUX = (0.0229 * self._ambient) - (0.0291 * self._IR)
                    elif (ratio <= 0.80):
                            self._LUX = (0.0157 * self._ambient) - (0.018 * self._IR)
                    elif (ratio <= 1.3):
                            self._LUX = (0.00338 * self._ambient) - (0.0026 * self._IR)
                    elif (ratio > 1.3):
                            self._LUX = 0

                    return (ambient, IR, self._ambient, self._IR, self._LUX)

            def _partno_revision(self):
                    """ Read Partnumber and revision of the sensor """
                    cmd = _CMD | _REG_ID
                    value = self.i2c.readS8(cmd)
                    part = str(value)[7:4]
                    if (part == "0000"):
                            PartNo = "TSL2560CS"
                    elif (part == "0001"):
                            PartNo = "TSL2561CS"
                    elif (part == "0100"):
                            PartNo = "TSL2560T/FN/CL"
                    elif (part == "0101"):
                            PartNo = "TSL2561T/FN/CL"
                    else:
                            PartNo = "not TSL2560 or TSL 2561"
                    RevNo = str(value)[3:0]
                    if (self.debug):
                            print "responce: ", value
                            print "PartNo = ", PartNo
                            print "RevNo = ", RevNo
                    return (PartNo, RevNo)

            def _control(self, params):
                    if (params == _POWER_UP):
                            print "Power ON"
                    elif (params == _POWER_DOWN):
                            print "Power OFF"
                    else:
                            print "No params given"
                    cmd = _CMD | _REG_CONTROL | params
                    self.i2c.write8(self._addr, cmd)  # select command register and power on
                time.sleep(0.4)  # Wait for 400ms to power up or power down.



    def main():
            TSL2561 = Tsl2561()
            TSL2561._init__(I2C_SMBUS, I2C_ADDRESS)
            while (True):
                    gain=0
                    val = TSL2561.readLux(gain)
                    ambient = val[0]
                    IR = val[1]
                    _ambient = val[2]
                    _IR = val[3]
                    _LUX = val[4]
                    if (ambient == 0xffff or IR == 0xffff):
                            print ("Sensor is saturated, no lux value can be achieved:")
                    print ("ambient = " + ambient)
                        print ("IR = " + IR)
                            print ("light = " + _LUX)
                elif (_ambient == 0):
                        print ("It's dark:")
                            print ("ambient = " + str(ambient))
                    print ("IR = " + str(IR))
                        print ("_ambient = " + str(_ambient))
                            print ("_IR = " + str(_IR))
                    print ("Light = " + str(_LUX) + " lux.")
                    else:
                            print ("There is light:")
                    print ("ambient = " + str(ambient))
                            print ("IR = " + str(IR))
                            print ("_ambient = " + str(_ambient))
                            print ("_IR = " + str(_IR))
                            print ("Light = " + str(_LUX) + " lux.")
                    time.sleep(2)
                    ambient  = None
                    IR       = None
                    _ambient = 0
                    _IR      = 0
                    _LUX     = None
                TSL2561._control(_POWER_DOWN)


    if __name__=="__main__":
            main()
```

- 运行这个示例
```
    sudo python grove_i2c_digital_light_sensor.py
```

- 这个就是得到的结果

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/img/Grovepi_digital_light_sensor_00.png)


## 资源下载
--------

- **[Eagle]** [Grove - Digital Light Sensor Eagle File](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/res/Grove-Digital%20%20light%20%20sensor%20v1.0%20eagle%20file.zip)
- **[PDF]** [Grove - Digital Light Sensor Sch PDF File](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/res/Digital%20light%20sensor%20v1.0%20Sch.pdf)
- **[PDF]** [Grove - Digital Light Sensor PCB PDF File](https://github.com/SeeedDocument/Grove-Digital_Light_Sensor/raw/master/res/Digital%20light%20sensor%20v1.0%20PCB.pdf)
- **[Library]** [Library Github Grove-Digital Light](https://github.com/Seeed-Studio/Grove_Digital_Light_Sensor/archive/master.zip)
- **[Datasheet]** [TSL2561 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Digital_Light_Sensor/master/res/TSL2561T.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Digital_Light_Sensor -->
