---
name: Grove - Tilt Switch
category: Sensor
bzurl: https://seeedstudio.com/Grove-Tilt-Switch-p-771.html
oldwikiname: Grove_-_Tilt_Switch
prodimagename: Tilt1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Tilt_Switch
sku: 101020025
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/img/Tilt1.jpg)

Grove-Tilt Switch 相当于一个开关，用作数字输入。 在 tilt switch 内部是一对滚珠，当壳体向上直立时滚珠与引脚接触。当壳体翻转向下时滚珠不接触，因此断开连接。与滚珠接触的引脚连接到 SIG 线，NC 表示不连接，在该传感器上没有用到这个引脚。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.156ac3aD5feFp&id=45477183101&ns=1&abbucket=1#detail)

## 产品特性
--------

-   Grove 接口
-   易于使用
-   简单的 Grove 模块

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
--------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
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
<th scope="row">
连接角
</th>
<td colspan="3">
10° ~170°
</td>
<td>
-
</td>
</tr>
<tr align="center">
<th scope="row">
断开角
</th>
<td colspan="3">
190° ~350°
</td>
<td>
-
</td>
</tr>
<tr align="center">
<th scope="row">
电气寿命
</th>
<td colspan="3">
100,000
</td>
<td>
次
</td>
</tr>
</table>

## Platforms Supported
-------------------

## 使用方法
-----

### 与 Arduino 一起使用

Grove - Tilt Switch 的 SIG 引脚正常输出低。 当 Tilt Switch 向上直立时，倾斜开关内的一对滚珠将与引脚接触，SIG 引脚将输出高电平。

下面演示了使用 Tilt Switch 和 Grove - Button 来控制 LED 的简单应用。

-   如下图所示，Tilt Switch 连接到 Grove-Base Shield 的数字端口 **5**，Grove-Button 连接到数字端口 **7**，LED连接到数字端口 **2**。硬件安装如下 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/img/Digitalv1.0b.jpg)

-   将下面的代码复制并粘贴到新的 Arduino 程序里。

```
void setup()
{
    pinMode(1, OUTPUT);
    pinMode(5, INPUT);
    pinMode(7, INPUT);
}

void loop()
{

    if (digitalRead(5)==HIGH)
    {
        digitalWrite(1, HIGH);
        delay(100);
        digitalWrite(1, LOW);
    }

    if (digitalRead(7)==HIGH)
    {
        digitalWrite(1, HIGH);
        delay(200);
        digitalWrite(1, LOW);
    }

}
```

-   上传代码。
-   然后当您按下按钮或激活 tilt-switch 时，LED将点亮。 您也试试把!

## 参考资料
---------

Grove-Tilt Switch 的操作角度如下图所示 :

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/img/Tilt_Switch_Operate.jpg)

<div class="admonition note">
<p class="admonition-title">Note</p>
Grove 上的标记 **J1** 是参考终端。
</div>

### 与 Raspberry Pi 一起使用

1.你需要一个 Raspberry Pi 和一个 Grovepi 或 Grovepi+。

2.您需要已经完成开发环境的配置，否则请遵循 [这里](/GrovePiPlus)。

3.连接

-   使用 Grove 线缆将 tilt-switch 插入 Grovepi 插座 **D3**。

4.跳转到演示目录 :
```
       cd yourpath/GrovePi/Software/Python/
```
-   可以看到代码
```
    nano grovepi_tilt_switch.py   # "Ctrl+x" to exit #
```
```
    import time
    import grovepi

    # Connect the Grove Tilt Switch to digital port D3
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

5.运行代码。
```
    sudo python grove_tilt_switch.py
```

6.结果 : 将传感器竖直时 SIG 引脚将输出高电平。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/img/Grovepi_tilt_Switch_00.png)

## 资源下载
---------

-   **[原理图文件]** [Grove - Tilt Switch v1.0 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/res/Grove-Tilt_Switch_v1.0_Source_File.zip)
-   **[原理图PDF]** [Grove - Tilt Switch v1.1 PDF File](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/res/Grove-Tilt_Switch_v1.1_PDF_File.pdf)
-   **[Eagle文件]** [Grove - Tilt Switch v1.1 Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/res/Grove-Tilt_Switch_v1.1_Eagle_File.zip)
-   **[芯片数据手册]** [SW200D Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Tilt_Switch/master/res/SW200D_datasheet.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Tilt_Switch -->
