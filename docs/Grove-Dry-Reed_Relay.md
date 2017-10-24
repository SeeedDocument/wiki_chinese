---
title: Grove - Dry-Reed Relay
category: Actuator
bzurl: https://seeedstudio.com/Grove-Dry-Reed-Relay-p-1412.html
oldwikiname: Grove_-_Dry-Reed_Relay
prodimagename: DryReed_Relay_01.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/DryReed Relay.jpg
surveyurl: https://www.research.net/r/Grove-Dry-Reed_Relay
sku: 103020014
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Dry-Reed_Relay/master/img/DryReed_Relay_01.jpg)

 **Grove-Dry Reed Relay** 是一个继电器模块，通过线圈中的电流使振动簧片磁化。 与电磁继电器相比，它具有完全密封的触点，这是 Grove - Dry-Reed Relay 的最大特点。 此外，其结构简单，紧凑，速度快，使用寿命长，广泛应用于微电子检测，自动控制等多个领域。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.28e30603LoD7KR&id=45508590653)

产品特性
-------

- Grove 接口
- 高速
- 稳定性好
- 触点寿命长
- 触点完全密封

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://seeed.wiki/Grove_System/)

规格参数
-------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
标准值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
电压
</th>
<td>
4.8
</td>
<td>
5.0
</td>
<td>
5.2
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
线圈电阻
</th>
<td>
225
</td>
<td>
250
</td>
<td>
275
</td>
<td>
Ω
</td>
</tr>
<tr align="center">
<th scope="row">
接触电压
</th>
<td colspan="3">
3.75
</td>
<td>
VDC
</td>
</tr>
<tr align="center">
<th scope="row">
开关电流（最大值）
</th>
<td colspan="3">
0.5
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
开关电压（最大值）
</th>
<td colspan="3">
120 VAC/60VDC
</td>
<td>
-
</td>
</tr>
<tr align="center">
<th scope="row">
负载电流（最大值）
</th>
<td colspan="3">
1.0
</td>
<td>
A
</td>
</tr>
<tr align="center">
<th scope="row">
动作时间（最大值）
</th>
<td colspan="3">
1.0
</td>
<td>
mS
</td>
</tr>
<tr align="center">
<th scope="row">
释放时间（最大值）
</th>
<td colspan="3">
0.5
</td>
<td>
mS
</td>
</tr>
<tr align="center">
<th scope="row">
机械寿命（无负载）
</th>
<td colspan="3">
1×108 operations
</td>
<td>
-
</td>
</tr>
<tr align="center">
<th scope="row">
环境温度
</th>
<td>
-30
</td>
<td>
/
</td>
<td>
70
</td>
<td>
˚C
</td>
</tr>
</table>

Platforms Supported
-------------------

使用方式
-----

### 使用 Arduino


Grove - Dry-Reed Relay 可支持高达 60VDC 1A 的负载。 您可以使用它来控制电阻负载，<font color="red"> **但不适用于有些负载（如 电机 ）**</font>。

这种 Grove - Dry-Reed Relay 的使用方法与普通继电器相似。

- 将电灯连接到 Grove - Dry-Reed Relay 和电源。
- 将 Grove - Dry-Reed Relay 连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的端口 **D2** ，并将其连接到 Arduino / Seeeduino。

- 上传以下代码。

```
    int Relay = 2;

    // the setup routine runs once when you press reset:
    void setup() {                
      // initialize the digital pin as an output.
      pinMode(Relay, OUTPUT);     
    }

    // the loop routine runs over and over again forever:
    void loop() {
      digitalWrite(Relay, HIGH);   //the Relay close(HIGH is the voltage level)
      delay(5000);               // wait for five seconds
      digitalWrite(Relay, LOW);    //the Relay normally open by making the voltage LOW
      delay(5000);               // wait for five seconds
    }
```

-   电灯将反复亮起几秒钟，然后关闭几秒钟。对于特殊应用程序，您可能需要自己编写代码。

### 使用 Raspberry Pi

1.你应该有一个 raspberry pi 和一个 grovepi 或 grovepi + 。

2.您需要完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 完成配置。

3.连接方式

- 使用 grove 连接线将传感器连接到 Grovepi 的 **D4** 端口 。

4.浏览演示目录：
```
    cd yourpath/GrovePi/Software/Python/
```

-   参考代码
```
    nano grove_relay.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Relay to digital port D4
    # SIG,NC,VCC,GND
    relay = 4

    grovepi.pinMode(relay,"OUTPUT")

    while True:
        try:
            # switch on for 5 seconds
            grovepi.digitalWrite(relay,1)
            print "on"
            time.sleep(5)

            # switch off for 5 seconds
            grovepi.digitalWrite(relay,0)
            print "off"
            time.sleep(5)

        except KeyboardInterrupt:
            grovepi.digitalWrite(relay,0)
            break
        except IOError:
            print "Error"
```

5.运行演示
```
    sudo python grove_relay.py
```

资源下载
--------

- [Grove - Dry-Reed Relay Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Dry-Reed_Relay/master/res/Grove-Dry-Reed_Relay_Eagle_File.zip)
- [Dry-Reed Relay Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Dry-Reed_Relay/master/res/Dry-Reed_Relay_Datasheet.pdf)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Dry-Reed_Relay -->
