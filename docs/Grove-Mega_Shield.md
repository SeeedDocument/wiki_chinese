---
name: Grove - Mega Shield
category: Wireless
bzurl: https://www.seeedstudio.com/Grove-Mega-Shield-v12-p-2539.html
oldwikiname:  Grove - Mega Shield
prodimagename: 500px-Megashieldn1_03.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Mega_Shield
sku:   103020027
---
![](https://github.com/SeeedDocument/Grove-Mega_Shield/raw/master/img/500px-Megashieldn1_03.jpg)

Grove - Mega Shield 是 Arduino Mega 和 Google ADK 的扩展板。我们将所有连接器标准化为 4pin（信号 1，信号 2，VCC 和 GND）的 2mm 接口，并保留 3pin（信号，VCC 和 GND）的 2.54mm 插头用于驱动舵机和电子积木，这样简化了电子线路的接线难度。4pin 接口也使接线更加可靠。Mega Shield 使用了数字端口 0 - 21 和模拟端口 0 - 15 。为了更方便地把 Mega Shield 安装在 Xduino Mega 或 Google ADK 上，数字端口 22 - 53 没有被使用。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.24.33bb79d0opc3Rx&id=45770800195)

## 产品参数
---
- 兼容 Arduino Mega1280/2560
- 兼容 Grove
- 兼容 Google ADK
- 尺寸: 92.8 mm X 57.2 mm.

## 功能模块
---
Grove - Mega Shield 的目的是把 Arduino Mega 或 Google ADK 的输入和输出引脚轻松连接到 Grove 设备。

每个插座都有其匹配的 I/O 引脚。 Grove-Mega Shield 可以分为四个部分：复位按钮，模拟信号区，数字信号区和电源区。

请参考下图：

![](https://github.com/SeeedDocument/Grove-Mega_Shield/raw/master/img/Megashield001.jpg)

根据 GPIO : IIC（3个接口），UART（UART0-3），PWM（PWM 2-13）和 ICSP（不是接口）的不同功能，Grove - Mega Shield 的数字信号区也分为四个部分。请注意，PWM有两种接口：3Pin 2.54mm 接头和我们标准的 4Pin 2mm 接口。 这两种形式的外观不同，4Pin 2mm 接口可以连接到我们的标准 Groves，而 3Pin 2.54mm 接头可连接到舵机，超声波测距模块和电子积木。请注意，同时使用 3pin 和 4pin 的 PWM 时，一定要确保不要使用同一个 GPIO 端口。接口分布请参考下图。

![](https://github.com/SeeedDocument/Grove-Mega_Shield/raw/master/img/Megashield002.jpg)

## 资料下载
---
- **[Eagle 文件]**[Eagle File of Grove - Mega Shield.](https://github.com/SeeedDocument/Grove-Mega_Shield/raw/master/res/Eagle_file_of_Megashield.zip)
- **[Eagle 文件]**[Eagle File of Grove - Mega Shield v1.1.](https://github.com/SeeedDocument/Grove-Mega_Shield/raw/master/res/Eagle_file_of_Megashield_v1.1.zip)
