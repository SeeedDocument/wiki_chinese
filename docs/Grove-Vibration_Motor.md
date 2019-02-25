---
name: Grove - Vibration Motor
category: Actuator
bzurl: https://seeedstudio.com/Grove-Vibration-Motor-p-839.html
oldwikiname: Grove_-_Vibration_Motor
prodimagename: Gvib.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Vibration_Motor
sku: 105020003
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Vibration_Motor/master/img/Gvib.jpg)

这是一种适合作为非听觉指示器的迷你振动电机。 当输入为高电平时，电机将像静音模式下的手机一样振动。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e112wbs3Z&id=45574264986)
版本信息
---------------

| 调整版本 | 描述                                       | 发布日期|
|----------|----------------------------------------------------------------|---------------|
| v0.9b    |  初始版本                         | 2011年5月10日  |
| v1.0     | 能够直接使用I / O端口驱动振动电机          |2011年11月5日  |
| v1.2     | 增加了晶体管，能够使用较大电流驱动振动电机 | 2013年7月11日 |

产品特性
--------


- 能够兼容Grove
- 无声
- 低功耗
- 高可靠性

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

产品规格
--------------

<table border="1" cellspacing="0" width="80%">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小
</th>
<th scope="col">
一般
</th>
<th scope="col">
最大
</th>
</tr>
<tr align="center">
<th scope="row">
工作电压
</th>
<td>
3.0V
</td>
<td>
5.0V
</td>
<td>
5.5V
</td>
</tr>
<tr align="center">
<th scope="row">
控制模式
</th>
<td colspan="3" rowspan="1">
逻辑电平
（当逻辑高电平时，电机为ON，低电平时，电机为OFF。）
</td>
</tr>
<tr align="center">
<th scope="row">
额定转速
</th>
<td colspan="3" rowspan="1">
9000 rpm
</td>
</tr>
</table>

支持平台
-------------------

使用方法
-----

### 使用 Arduino

其实让它振动跟点亮LED一样容易。 以下是显示如何打开振动电机的示例。

1. 使用Grove连接线将其插入Grove - Base Shield的数字端口 **D9** 。
2. 将 Grove - Base Shield插入Arduino。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-Vibration_Motor/master/img/IMG_0506.jpg)
3. 使用USB数据线将Arduino与PC进行连接
4. 将下面的代码复制并粘贴到新的Arduino编辑页面上，并将其上传到您的Arduino。

使用如下所示的示例代码：

```
int MoPin = 9;    // vibrator Grove connected to digital pin 9

void setup()  {
    pinMode( MoPin, OUTPUT );
}

void loop()  {

    digitalWrite(MoPin, HIGH);
    delay(1000);

    digitalWrite(MoPin, LOW);
    delay(1000);
}

```

现在，感受你电机的振动吧！

### 使用Raspberry Pi

1.你应该有一个Raspberry Pi和一个grovepi或grovepi +。

2.您应该已经完成配置开发环境，否则遵循[说明](http://wiki.seeed.cc/GrovePi_Plus/) 进行配置。

3.硬件连接

-   用Grove连接线将传感器插入Grovepi **D8** 接口。

4.导航到示例目录：
```
cd yourpath/GrovePi/Software/Python/
```
-  找到这行代码
```
nano grove_vibration_motor.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi

#将Grove Vibration Motor连接到数字端口D8
#SIG,NC,VCC,GND
vibration_motor = 8

grovepi.pinMode(vibration_motor,"OUTPUT")

while True:
    try:
        # Start vibrating for 1 second
        grovepi.digitalWrite(vibration_motor,1)
        print 'start'
        time.sleep(1)

        # Stop vibrating for 1 second, then repeat
        grovepi.digitalWrite(vibration_motor,0)
        print 'stop'
        time.sleep(1)

    except KeyboardInterrupt:
        grovepi.digitalWrite(vibration_motor,0)
        break
    except IOError:
        print "Error"
```
5.运行这个示例
```
sudo python grove_vibration_motor.py
```

## 项目

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/gun.jpg)

Inspired by OVERWATCH, we have made a very cool Wooden Laser Gun toy for fun these day!

The Wooden Laser Gun and the Gun Target are all based on an Arduino board called Seeeduino Lotus. The laser emitter on the Laser Gun is controlled to fire laser pulse to "activate" the Gun Target. And there are 3 light sensors on the Gun Target to detect the laser pulse. It seems very simple right? If you are interested in our project, please make one for yourself or your child! It's worth to spend one day DIY it as a Xmas present.    

[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/make.png)](http://www.instructables.com/id/DIY-a-Wooden-Laser-Gun-As-a-Xmas-Present-for-Your-/)

资源下载
---------

-   [Grove - Vibration Motor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Vibration_Motor/master/res/Grove-Vibration_Motor_Eagle_Files.zip)
-   [S9013 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Vibration_Motor/master/res/S9013.pdf)
-   [ANDA-B1020 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Vibration_Motor/master/res/ANDA-B1020_datasheet.pdf)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Vibration_Motor -->
