---
name: Grove - GPS
category: Communication
bzurl: https://seeedstudio.com/Grove-GPS-p-959.html
oldwikiname: Grove_-_GPS
prodimagename: Grove-GPS.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-GPS
sku: 113020003
tags: grove_uart, io_3v3, io_5v, plat_duino, plat_bbg, plat_pi, plat_linkit,
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/img/Grove-GPS.jpg)

这个 Grove - GPS 模块是一款低成本的现场可编程小配件，其配备了 SIM28 ( u-blox 6 是旧版本 ) 和串行通信配置。它配备了一个具有 22 个跟踪通道，66个采集通道的 GPS 接收器。它的跟踪和采集的灵敏度可达到 -160dBm，这使其成为个人导航项目和定位服务的最佳选择，同时也是同类产品中的性价比佼佼者。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.12586056ZVlxk9&id=520282073070&ns=1&abbucket=1#detail)

## 产品特性
--------

-   支持 NMEA 和 u-blox 6 协议。( 截至 2014 年 1 月 10 日，之后 SIM28 )
-   低功耗
-   可配置波特率
-   Grove 兼容接口

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


## 规格参数
-------------

| **项目**    | **范围/值**              |
|------------------|------------------------------|
| 输入电压    | 3.3/5V                       |
| 波特率     | 4800 - 57600 (u-blox 版本) |
| 波特率         | 9600 - 115200 (SIM28 版本) |
| 默认波特率 | 9600                         |

## Platforms Supported
-------------------

## 入门指导
---------------

遵循 [Grove system](http://wiki.seeedstudio.com/cn/Grove_System/) 可以帮助用户实现 Grove 入门。

### 与 Arduino 一起使用
该示例仅使用软件串行从 GPS 读取，并将其发送回串行端口。

#### 连接
在这里，我们将通过一个简单的演示向您展示这个 Grove - GPS 的工作原理。 首先，我们需要准备以下内容：

| Seeeduino V4 | Grove - GPS | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-GPS/raw/master/img/Grove-GPS_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.711ba8e25BFoaP&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a230r.1.14.15.12586056ZVlxk9&id=520282073070&ns=1&abbucket=1#detail)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.151d1972FoOPLp&id=520233320144)|

- 使用 Grove 线缆将 Grove-GPS 连接到 Grove - Base Shield 上的 **数字端口2**。
- 把 base Shield 插入 Seeeduino-V4。
- 使用 USB 线缆将 Arduino 连接到 PC。

![](https://github.com/SeeedDocument/Grove-GPS/raw/master/img/Connection.jpg)

#### 软件部分

!!!Note
    请注意，u-center 软件仅适用于 Windows。

-   安装 [u-center](https://www.u-blox.com/en/product/u-center-windows)。
-   将下面的代码上传到您的Arduino / Seeeduino。

```
#include <SoftwareSerial.h>
SoftwareSerial SoftSerial(2, 3);
unsigned char buffer[64];                   // buffer array for data receive over serial port
int count=0;                                // counter for buffer array
void setup()
{
    SoftSerial.begin(9600);                 // the SoftSerial baud rate
    Serial.begin(9600);                     // the Serial port of Arduino baud rate.
}

void loop()
{
    if (SoftSerial.available())                     // if date is coming from software serial port ==> data is coming from SoftSerial shield
    {
        while(SoftSerial.available())               // reading data into char array
        {
            buffer[count++]=SoftSerial.read();      // writing data into array
            if(count == 64)break;
        }
        Serial.write(buffer,count);                 // if no data transmission ends, write buffer to hardware serial port
        clearBufferArray();                         // call clearBufferArray function to clear the stored data from the array
        count = 0;                                  // set counter of while loop to zero 
    }
    if (Serial.available())                 // if data is available on hardware serial port ==> data is coming from PC or notebook
    SoftSerial.write(Serial.read());        // write it to the SoftSerial shield
}


void clearBufferArray()                     // function to clear buffer array
{
    for (int i=0; i<count;i++)
    {
        buffer[i]=NULL;
    }                      // clear all index of array with command NULL
}
```


-  打开 U-center.
-  点击 **Receiver -> Port**，然后选择 Arduino 正在使用的 COM 端口。
-  点击 **Receiver -> Baudrate** 确保选到 9600。
-  点击 **View -> Text Console** 然后您会得到一个 NMEA 数据流的窗口。
-  打开串行监视器，您可以看到如下所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/img/GPS_result.jpg)


**我们也可以在 Google Earth 中查看数据 :**

1. 点击 **File(文件) -&gt; Database Export -&gt; Google Earth KML**
2. 启动有 u-center 收集了历史的 Google Earth。
3. 或者可以通过按工具栏上的红色圆圈来记录数据，它还会询问您要保存记录的位置。
4. 当我们捕获了足够的数据时，点击黑色的方块来停止录制。
5. 接下来我们可以通过把 ubx 文件上传到 [GPSVisualizer](http://www.gpsvisualizer.com/) ，将生成的 .ubx 文件转换为 KML。

### 与 Raspberry 一起使用

#### 连接
首先，我们需要准备以下内容 :

| Raspberry pi | Grove - GPS | GrovePi_Plus |
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/pi.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-GPS/raw/master/img/Grove-GPS_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/grovepi%2B.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.77d5d79cHzsCBt&id=528322046763)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.70d25d0c57nryX&id=520282073070)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.152743fa5iAkWv&id=45506190895)|

- 按照 [说明](http://wiki.seeed.cc/GrovePi_Plus/) 配置开发环境。
- 使用 Grove 线缆将传感器插入 Grovepi + 插座 **RPISER**。

![](https://github.com/SeeedDocument/Grove-GPS/raw/master/img/Pi_Connection.jpg)

#### 软件部分

- 跳转到演示目录 :
```
    cd yourpath/GrovePi/Software/Python/
```
-   找到代码。
```
    nano grove_gps.py   # "Ctrl+x" to exit #
```

```
import serial, time
import smbus
import math
import RPi.GPIO as GPIO
import struct
import sys
 
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 0)   #Open the serial port at 9600 baud
ser.flush()
 
class GPS:
    #The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
    inp=[]
    # Refer to SIM28 NMEA spec file https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/SIM28_DATA_File.zip
    GGA=[]
 
    #Read data from the GPS
    def read(self):
        while True:
            GPS.inp=ser.readline()
            if GPS.inp[:6] =='$GPGGA': # GGA data , packet 1, has all the data we need
                break
            time.sleep(0.1)
        try:
            ind=GPS.inp.index('$GPGGA',5,len(GPS.inp)) #Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
            GPS.inp=GPS.inp[ind:]
        except ValueError:
            print ""
        GPS.GGA=GPS.inp.split(",")   #Split the stream into individual parts
        return [GPS.GGA]
 
    #Split the data into individual elements
    def vals(self):
        time=GPS.GGA[1]
        lat=GPS.GGA[2]
        lat_ns=GPS.GGA[3]
        long=GPS.GGA[4]
        long_ew=GPS.GGA[5]
        fix=GPS.GGA[6]
        sats=GPS.GGA[7]
        alt=GPS.GGA[9]
        return [time,fix,sats,alt,lat,lat_ns,long,long_ew]
 
g=GPS()
f=open("gps_data.csv",'w')   #Open file to log the data
f.write("name,latitude,longitude\n")   #Write the header to the top of the file
ind=0
while True:
    try:
        x=g.read()  #Read from GPS
        [t,fix,sats,alt,lat,lat_ns,long,long_ew]=g.vals() #Get the individial values
        print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",long,long_ew
        s=str(t)+","+str(float(lat)/100)+","+str(float(long)/100)+"\n"   
        f.write(s)   #Save to file
        time.sleep(2)
    except IndexError:
        print "Unable to read"
    except KeyboardInterrupt:
        f.close()
        print "Exiting"
        sys.exit(0)
```

- 运行代码。
```
    sudo python grove_gps.py
```

- 结果如下。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/img/Grovepi_gps_00.jpg)

<div class="admonition note">
<p class="admonition-title">Note</p>
GPS 更适合户外使用。 建议将您的 raspberry pi 放在窗外或室外任何地方。
</div>

## SIM28 模块注意 :
------------------

1. Grove-GPS 将模块更改为 SIM28，与原始版本相同。
2. 我们应该使用 ["SIMCom GPS DEMO"](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/SIMCom_GPS_DEMO_V1.07.zip) 工具来接收 SIM28 模块数据。
3. 打开 SIMCom_GPS_DEMO 工具，转到 **Module->properties->module->select SIM28**。.
4. SIMCom_GPS_DEMO_V1.07 仅适用于 Windows。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/img/SIM28_module_select.jpg)

5. 打开 SIMCom_GPS_DEMO 工具，转到 **Module->connect**。 选择 GPS 模块使用的串行端口。

    ![](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/img/SIM28_module_tools_pannel.jpg)


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/GPS.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---------

-   **[Eagle文件]** [Grove-GPS Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/GPS.zip)
-   **[原理图PDF]** [GPS Schematic(PDF)](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/GPS.pdf)
-   **[芯片数据手册]** [E-1612-UB Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/E-1612-UB_Datasheets_Sheet.pdf)
-   **[芯片数据手册]** [U-Blox6 Receiver Description Protocol Spec](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/U-blox-6-Receiver-Description-Including-Protocol-Specification.zip)
-   **[其他文件]** [U-Blox u-center GPS evaluation software](https://www.u-blox.com/en/product/u-center-windows)
-   **[其他文件]** [SIM28\_DATA\_File](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/SIM28_DATA_File.zip)
-   **[其他文件]** [SIMCom\_GPS\_DEMO\_V1.07](https://raw.githubusercontent.com/SeeedDocument/Grove-GPS/master/res/SIMCom_GPS_DEMO_V1.07.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_GPS -->
