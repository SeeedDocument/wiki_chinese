---
name: Grove - Magnetic Switch
category: Sensor
bzurl: https://seeedstudio.com/Grove-Magnetic-Switch-p-744.html
oldwikiname: Grove_-_Magnetic_Switch
prodimagename: Magnetic_Switch.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Magnetic_Switch
sku: 101020038
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/img/Magnetic_Switch.jpg)

这是一个 Grove 接口兼容的磁性开关模块。 它是基于密封的干簧管开关CT10。 CT10是单刀，单掷（SPST）开关，有常开的钌触点。 传感器是双端型的，可以用电磁铁，永久磁铁或两者的组合来驱动。 磁性开关是一个很好的工具，设计师可以根据接近程度开启或关闭电路。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3235e8fuVLe7e&id=521463829492)

产品特性
--------
-   兼容 Grove 接口
-   2.0cm x 2.0cm Grove 标准模块
-   最小外观尺寸
-   10W 允许功率
-   具有坚固的封装

!!!Tip
    更多关于 Grove 模块的信息请参考 [Grove System](http://wiki.seeed.cc/Grove_System/)

创意应用
-----------------

-   接近传感器
-   安全警报传感器
-   水平传感器
-   流量传感器
-   脉冲传感器

规格参数
-------------

<table border="1">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
正常值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<td>
工作电压
</td>
<td>
4.75
</td>
<td>
5.0
</td>
<td>
5.25
</td>
<td>
V
</td>
</tr>
<tr align="center">
<td>
开关功率
</td>
<td colspan="3">
10
</td>
<td>
W
</td>
</tr>
<tr align="center">
<td>
开关电压 AC，RMS 值（最大值）
</td>
<td colspan="3">
&lt; 140
</td>
<td>
V
</td>
</tr>
<tr align="center">
<td>
直流开关电流
</td>
<td colspan="3">
&lt; 500
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<td>
支持直流电流
</td>
<td colspan="3">
&lt; 0.5
</td>
<td>
A
</td>
</tr>
<tr align="center">
<td>
接触电阻
</td>
<td colspan="3">
&lt;200
</td>
<td>
mΩ
</td>
</tr>
<tr align="center">
<td>
绝缘电阻
</td>
<td colspan="3">
&gt;10<sup>6</sup>
</td>
<td>
MΩ
</td>
</tr>
<tr align="center">
<td>
操作温度
</td>
<td>
-40
</td>
<td>
-
</td>
<td>
125
</td>
<td>
℃
</td>
</tr>
<tr align="center">
<td>
操作范围
</td>
<td>
10
</td>
<td>
-
</td>
<td>
40
</td>
<td>
AT
</td>
</tr>
</table>

支持平台
-------------------

使用方法
-----

### 使用 [Arduino](/Arduino "Arduino")

正常情况下模块的 SIG 引脚输出低电平。当磁铁接近开关时，磁性开关闭合，SIG 引脚输出高电平。

下图演示了使用磁性开关来控制 LED 的简单应用。当放置一个靠近模块的磁力足够的磁铁时，开关闭合，然后 SIG 引脚输出高电平。你可以用它来控制 LED。

如下图所示，磁开关连接到 **Grove - Base Shield** 的 **D9**，LED 连接到 **D13**。当磁铁接近开关时，**SIG** 引脚输出高电平，然后 LED 亮起。硬件安装如下：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/img/Grove-Magnetic_Switch.jpg)

-   把下面的代码复制粘贴到 Arduino 的新窗口中：

```
    /*******************************************************************************/

    /*对 LED 引脚和磁性开关的宏定义*/
    #define MAGNECTIC_SWITCH 9
    #define LED 13// Arduino or Seeeduino 的板载 LED

    void setup()
    {
        pinsInit();
    }

    void loop()
    {
        if(isNearMagnet())  //是否有磁铁靠近开关
        {
            turnOnLED();
        }
        else
        {
            turnOffLED();
        }
    }
    void pinsInit()
    {
        pinMode(MAGNECTIC_SWITCH, INPUT);
        pinMode(LED,OUTPUT);
    }

    /* 如果磁铁靠近了开关，就返回 ture ，否则返回 false */
    boolean isNearMagnet()
    {
        int sensorValue = digitalRead(MAGNECTIC_SWITCH);
        if(sensorValue == HIGH) //如果传感器输出高电平
        {
            return true;        //是，返回 ture
        }
        else
        {
            return false;       //否，返回 false
        }
    }
    void turnOnLED()
    {
        digitalWrite(LED,HIGH);
    }
    void turnOffLED()
    {
        digitalWrite(LED,LOW);
    }
```

-   上传代码
-   当有磁铁靠近开关时，LED 就会亮起。大胆的试试吧！

### 使用 Raspberry Pi

1.你应该准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+。

2.你应该已经搭建好了开发环境，否则参考 [这里](http://wiki.seeedstudio.com/wiki/GrovePi+).

3.连接方法

-   把 Magnet Switch 用 Grove 电缆连接到 Grovepi上。


4.跳转到示例目录：
```
    cd yourpath/GrovePi/Software/Python/
```

-   看如下代码 (这段代码原用于倾斜传感器)
```
    nano grovepi_tilt_switch.py   # "Ctrl+x" 退出 #
```
```
    import time
    import grovepi

    # 把 Grove Tilt Switch 连接到 D3
    # SIG,NC,VCC,GND
    tilt_switch = 3

    grovepi.pinMode(tilt_switch,"INPUT")

    while True:
        try:
            print grovepi.digitalRead(tilt_switch)
            time.sleep(.5)

        except IOError:
            print "Error"
```

5.运行示例。
```
    sudo python grove_tilt_switch.py
```

6.运行结果

把磁铁靠近传感器， SIG 引脚会输出高电平。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/img/Grovepi_tilt_Switch_00.png)

资料下载
---------

-   **[Eagle 文件]**[Grove-Magnetic Switch v0.9 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/res/Magnetic_Switch.zip)
-   **[数据手册]**[CT10 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/res/CT10.pdf)
-   **[Eagle 文件]**[Grove-Magnetic Switch v1.3 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/res/Grove-Magnetic_Switch_v1.3_Eagle_File.zip)
-   **[PDF 文件]**[Grove-Magnetic Switch v1.3 PDF File](https://raw.githubusercontent.com/SeeedDocument/Grove-Magnetic_Switch/master/res/Grove-Magnetic_Switch_v1.3_PDF_File.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Magnetic_Switch -->
