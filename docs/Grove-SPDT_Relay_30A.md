---
title: Grove - SPDT Relay(30A)
category: Others
bzurl: https://www.seeedstudio.com/Grove-SPDT-Relay(30A)-p-1473.html
oldwikiname: Grove - SPDT Relay(30A)
prodimagename: SPDT_Relay_01.jpg
wikiurl: http://seeed.wiki/Grove_SPDT_Relay_30A
sku: 103020012
---

![](https://github.com/SeeedDocument/Grove-SPDT_Relay_30A/raw/master/img/SPDT_Relay_01.jpg)

Grove - SPDT Relay(30A) 是一个高品质的单刀双掷继电器 (SPDT)。这个继电器包含了一个线圈，一个公共端，一个常闭端，一个常开端。当线圈未通电时，公共端和常闭端连接。当线圈通电时，公共端和常开端连接。线圈的额定电压是 5V，额定电流是 30A (@250VAC, 30VDC)，这个继电器可以用来控制高电流设备。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.16.2c083744k8U2id&id=520666199351&ns=1&abbucket=1#detail)

## 产品特性
---
- 高合闸电流
- 单刀双掷继电器
- 常闭继电器

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)


## 规格参数
---
|项目|	最小值|	典型值	|最大值	|单位|
|---|---|---|---|---|
|工作电压|	4.75|	5.0|	5.25	|VDC|
|电流	|-|185|-|	mA|
|吸合电压 (Max)	|-|3.75|-|	VDC|
|动作时间 (Max)|-|	15|-|	ms|
|释放时间 (Max)|-|	10|-|	ms|
|工作温度范围|	-25| -	|70	|°C|


## 使用方法
---
**与 Arduino 一起使用**

为什么我们要用继电器，我们真的需要吗？如果您想开关控制一个需要更大电流或高压下工作的设备，则需要使用继电器。也就是说，继电器是"以低压控制的高压或高电流的开关"。最常用的 SPDT 继电器线圈的电流很小 ([Grove - Relay](http://wiki.seeed.cc/Grove-Relay/) 支持 10A)。现在，使用这个支持 30A 的继电器，您可以控制更多的高电流开关设备。

SPDT 继电器内部结构 :

![](https://github.com/SeeedDocument/Grove-SPDT_Relay_30A/raw/master/img/Relay_Struction.jpg)

当线圈未通电时，公共端和常闭端连接。

当线圈通电时，公共端和常开端连接。

硬件连接参考下图 :

![](https://github.com/SeeedDocument/Grove-SPDT_Relay_30A/raw/master/img/SPDT_Relay.jpg)

此继电器的控制代码与 [Grove - Relay](http://wiki.seeed.cc/Grove-Relay/) 相同

**与 Raspberry Pi 一起使用**

1.准备一个 Raspberry pi 和一个 Grovepi 或 Grovepi+。

2.完成配置开发环境，否则请遵循 [这里](http://seeed.wiki/GrovePi_Plus/)。

3.连接
- 将传感器用 Grove 线缆插入  Grovepi 插口 **D4**。

4.跳转到演示目录 :
```
   cd yourpath/GrovePi/Software/Python/
```
演示代码如下 :
```
   nano grove_spdt_relay.py   # "Ctrl+x" to exit #
```
```
import time
import grovepi

# Connect the Grove SPDT Relay to digital port D4
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

5.运行代码。
```
   sudo python grove_spdt_relay.py
```

## 资源下载
---
- **[Eagle文件]** [Grove - SPDT Relay(30A) Eagle File](https://github.com/SeeedDocument/Grove-SPDT_Relay_30A/raw/master/res/Grove_-_SPDT_Relay(30A)_Eagle_File.zip) 
- **[芯片数据手册]** [SLA-05VDC-SL-C Datasheet](https://github.com/SeeedDocument/Grove-SPDT_Relay_30A/raw/master/res/SLA-05VDC-SL-C_Datasheet.pdf)
