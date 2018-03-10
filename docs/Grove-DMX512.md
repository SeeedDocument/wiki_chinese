---
title: Grove - DMX512
category: Communication
bzurl: https://www.seeedstudio.com/Grove-DMX512-p-1447.html
oldwikiname:  Grove - DMX512
prodimagename: DMX512_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-DMX512/
sku:  103020000
---
![](https://github.com/SeeedDocument/Grove-DMX512/raw/master/img/DMX512_01.jpg)

Grove - DMX512 是从 Grove 接口到 DMX512 接口（工业标准 EIA-485 接口）的适配器。该模块基于可平衡传输线路并符合 ANSI 标准 EIA-485 接口的 SN75176 芯片。对于 Arduino，现在可以方便地控制舞台灯光和 DMX512 控制台。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.4fc177d2QzcFeg&id=45556513422)

## 产品特性
---
*   Grove 接口和标准 EIA-485 接口

*   使用方便

*   实用性强

##  操作示例
---
Arduino 可以使用 Grove - DXM512 模块轻松控制 DMX512 设备。以 LED 水晶魔术灯为例。 具体操作如下：

*   将 Grove-DMX512 的 Grove 接口连接到 [Grove - Base Shield](/Grove-Base_Shield "Grove - Base Shield") 的 **D3** 端口，并将  Grove - Base 扩展版插入 Arduino.

*   使用 DMX 线缆将 Grove-DMX512 的 DMX512 接口连接到 LED 水晶魔术灯的 DMX IN 接口。 并且为 LED 水晶魔球灯提供电源。

*   将 LED 水晶魔球灯设置为 DMX512 控制模式。 此时控制面板显示 “A001”。

![](https://github.com/SeeedDocument/Grove-DMX512/raw/master/img/DMX512_Usage.jpg)

*   下载 [File: DmxSimple Library](https://github.com/SeeedDocument/Grove-DMX512/raw/master/res/DmxSimple.zip) 并通过路径 ：**.. \ arduino-1.0.1 \ libraries** 将其解压缩到 Arduino IDE 的库文件中。

*   直接打开代码的路径 :**File(文件) -&gt; Example(示例) -&gt;DmxSimple-&gt;Fadup1.**

*   你可以看到一个有趣的场景。 尝试根据您个人的喜好来更改代码。

##  资源下载
---
- **[Eagle 文件]**[Grove - DMX512 Eagle File](https://github.com/SeeedDocument/Grove-DMX512/raw/master/res/Grove-DMX512_Eagle_File.zip)

- **[库文件]**[DmxSimple Library](https://github.com/SeeedDocument/Grove-DMX512/raw/master/res/DmxSimple.zip)

- **[芯片数据手册]**[SN75176 Datasheet](https://github.com/SeeedDocument/Grove-DMX512/raw/master/res/Sn75176a.pdf)
