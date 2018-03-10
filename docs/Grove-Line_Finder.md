---
title: Grove - Line Finder
category: Sensor
bzurl: https://www.seeedstudio.com/Grove-Line-Finder-p-825.html
oldwikiname: Grove - Line Finder
prodimagename: Grovelinefinder1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Line_Finder
sku: 101020009
---

---
![](https://github.com/SeeedDocument/Grove_Line_Finder/raw/master/images/Grovelinefinder1.jpg)

Grove-Line finder 为线跟随机器人设计。它具有红外发射 LED 和红外敏感光电晶体管。它可以将数字信号输出到微控制器，这样机器人可以稳定地跟随白色背景上的黑线，反之亦然。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.42e899986GihNh&id=540386082647)

## 规格参数
---
- 电源 : 5V 直流电
- 数字输出模式 : TTL ( 检测到黑色时为高电平，检测到白色时为低电平 )
- 连接器 : 4 引脚扣 Grove 接口
- 尺寸 : 20mm * 20mm
- 满足限制有害物质指令
- 比测仪 : MV358
- 光反射二极管 : RS-06WD

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 操作示例
---
**与 Arduino 一起使用**

当检测到黑线时，Brick 将返回 HIGH，当检测到白线时，返回 LOW。 使用可调电阻，检测范围可以从 1.5cm 变化到 5cm。 如果传感器在黑色和白色表面之间无法辨别，还可以使用可调电阻来设置合适的参考电压。

演示代码如下 :

```
Demo code
{

//------------------------------------------------------------
//Name: Line finder digital mode
//Function: detect black line or white line
//Parameter:   When digital signal is HIGH, black line
//             When digital signal is LOW, white line
//-------------------------------------------------------------
int signalPin =  3;    // connected to digital pin 3
void setup()   {
  pinMode(signalPin, INPUT); // initialize the digital pin as an output:
  Serial.begin(9600);  // initialize serial communications at 9600 bps:
}
// the loop() method runs over and over again,
// as long as the Arduino has power
void loop()
{
  if(HIGH == digitalRead(signalPin))
    Serial.println("black");
    else  Serial.println("white");  // display the color
  	//delay(1000);                  // wait for a second
}

}
```

**与 Raspberry Pi 一起使用**

1. 你需要有 Raspberry pi 和 Grovepi 或 Grovepi+。
2. 您需要完成配置开发环境，否则请遵循 [这里](http://wiki.seeedstudio.com/wiki/GrovePi+#Introducing_the_GrovePi.2B)。
3. 连接
  - 使用 Grove 线缆将传感器插入 Grovepi 的插座 **D7**。
4. 跳转到演示目录 :

```
 cd yourpath/GrovePi/Software/Python/
```

演示代码如下 :

```
   nano grove_line_finder.py   # "Ctrl+x" to exit #
```
```
import time
import grovepi

# Connect the Grove Line Finder to digital port D7
# SIG,NC,VCC,GND
line_finder = 7

grovepi.pinMode(line_finder,"INPUT")

while True:
    try:
        # Return HIGH when black line is detected, and LOW when white line is detected
        if grovepi.digitalRead(line_finder) == 1:
            print "black line detected"
        else:
            print "white line detected"

        time.sleep(.5)

    except IOError:
        print "Error"
```

5.运行代码。

```
   sudo python grove_line_finder.py
```

## 资源下载
---
- **[原理图文件]** [Eagle files](https://github.com/SeeedDocument/Grove_Line_Finder/raw/master/res/202000970_Grove%20-%20Line%20Finder%20v1.0_eagle%20files.zip)
- **[芯片数据手册]** [LMV358.PDF](https://github.com/SeeedDocument/Grove_Line_Finder/raw/master/res/Lmv358.pdf)
- **[其他资源]** [Schematic at Easyeda](https://easyeda.com/Seeed/Grove_Line_Finder_v1_1-dfc99c72325e41ff93a451882fd2e143)
