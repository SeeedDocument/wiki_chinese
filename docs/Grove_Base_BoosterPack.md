---
name: Grove Base BoosterPack
category: Others
bzurl: https://www.seeedstudio.com/Grove-Base-BoosterPack-p-2177.html
oldwikiname:  Grove Base BoosterPack
prodimagename: 110020004%205.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Base_BoosterPack
sku:  103020019
---
![](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/img/110020004%205.jpg)

BoosterPacks 是插入式扩展板，可以插在各种 LaunchPad 套件的顶部以扩展出 Grove 接口，例如连接 Grove 传感器，显示器，无线模块和其他模块。Grove Base BoosterPack 是 LaunchPad / BoosterPack 生态系统的一个补充，使得任何 LaunchPad 都能够与 Seeed Studio 提供的 Grove 模块连接。Grove Base BoosterPack 为设计者提供了一个方便快捷的连接方法，可以连接包括传感器，执行器，显示器，灯光模块，电机等在内的一百多个 Grove 模块。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.11.1f44cbf9csqrPK&id=521993888274)

![](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/img/Grove_Web_idea.jpg)

**什么是 Grove？**

Grove是一个模块化的标准连接器原型系统。Grove采用积木式组装电子技术。Grove 系统由一个 Base Shield 和大量具有标准化连接器的模块组成。 Base Shield 允许任何微控制器连接到各种 Grove 模块。 每个 Grove 模块都有自己的对应引脚，整个模块集合具有广泛的功能 - 从简单的按钮到复杂的心率传感器。每个模块都有清晰的文档和演示代码，以帮助您快速入门。如需了解更多请参考 [这里](http://wiki.seeedstudio.com/cn/Grove_System/)。

![](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/img/IMG_GROVE.JPG)

**什么是 LaunchPad？**

LaunchPad 是德州仪器的一套评估套件。为了将新功能引入到 LaunchPad 评估套件中，我们提供了 BoosterPack 作为适合 LaunchPad 基板的扩展板。它为您提供了一个方便，简单的方法，使用标准连接器，包括传感器，执行器，显示器，灯，电机等，超过一百个格罗夫模块。它可以让您方便简单的使用 Grove 接线连接包括传感器，执行器，显示器，灯，电机等超过一百个 Grove 模块。


##   产品特性
---
*   Seeedstudio 推出了 Grove Base BoosterPack，使得德州仪器的 Launchpad 能够与我们的 Groves 模块连接，从而进一步实现与一系列传感器，执行器，显示器，灯，电机等的组合。

*   Grove Base BoosterPack 拥有十三个 Groves 4-pin 标准接口，包括五个模拟，五个数字和三个串行端口。作为基于 MSP430 开发板 Launchpad 上的即插即用扩展模块，它还提供了各种教程与 TI MSP430 连接，共有 11 种不同类型的参考原型项目，为您提供创造性的便捷途径。

*   Grove BoosterPack 上有个红色的电源 LED 指示灯，用来指示通电状态。

![](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/img/BoosterpackpinMapping.jpg)

##   开始使用 Grove Base BoosterPack
---
###   基于 LaunchPad

使用 MSP-EXP430F5529LP, EK-TM4C123GXL 等

BoosterPack 的设计是为了利用“内侧 20 个引脚”中的引脚 [21-40]。引脚连接如下表所示：

示例：使用下表，开发人员能够使用 Energia 的 analogRead（24）API 调用，从 Grove 接口'J6'连接的 Grove 模块（即电位计/旋钮）读取模拟值。

<table>
<tr>
<th> 接口类型 </th>
<th> Grove 接口标签 </th>
<th>   GND   </th>
<th>   VCC   </th>
<th> SIG1 (连接到 BoosterPack 引脚) </th>
<th> SIG0 (连接到 BoosterPack 引脚) *
</th></tr>
<tr>
<td> Analog</td>
<td> J5 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 23 (支持模拟输入) </td>
<td> 22 (支持模拟输入)
</td></tr>
<tr>
<td> Analog</td>
<td> J6 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 25 (支持模拟输入) </td>
<td> 24 (支持模拟输入)
</td></tr>
<tr>
<td> Analog</td>
<td> J7 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 26 (支持模拟输入) </td>
<td> 25 (支持模拟输入)
</td></tr>
<tr>
<td> Analog</td>
<td> J8 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 27 (支持模拟输入) </td>
<td> 26 (支持模拟输入)
</td></tr>
<tr>
<td> Analog</td>
<td> J9 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 28 (支持模拟输入) </td>
<td> 27 (支持模拟输入)
</td></tr>
<tr>
<td> I2C </td>
<td> J10 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 10 (I2C SDA) </td>
<td> 9 (I2C SCL)
</td></tr>
<tr>
<td> UART </td>
<td> J11 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 4 (UART to MCU) </td>
<td> 3 (UART from MCU)
</td></tr>
<tr>
<td> SPI </td>
<td> J12 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 14 (SPI MISO) </td>
<td> 7 (SPI CLK)
</td></tr>
<tr>
<td> Digital </td>
<td> J13 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 39 (Digital/PWM 引脚) </td>
<td> 40 (Digital/PWM 引脚)
</td></tr>
<tr>
<td> Digital</td>
<td> J14 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 38 (Digital/PWM 引脚) </td>
<td> 39 (Digital/PWM 引脚)
</td></tr>
<tr>
<td> Digital</td>
<td> J15 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 37 (Digital/PWM 引脚) </td>
<td> 38 (Digital/PWM 引脚)
</td></tr>
<tr>
<td> Digital</td>
<td> J16 </td>
<td> GND </td>
<td> 3.3V </td>
<td> 36 (Digital/PWM 引脚) </td>
<td> 37 (Digital/PWM 引脚)
</td></tr>
<tr>
<td> Digital</td>
<td> J17 </td>
<td> GND </td>
<td> 3.3V  </td>
<td> 35 (Digital/PWM 引脚) </td>
<td> 36 (Digital/PWM 引脚
</td></tr></table>

###   使用一个 20-pin 的 LaunchPad

如果您使用的是 20-pin LaunchPad，则可以使用跳线或跨接线在 Grove 接口和 BoosterPack 接口之间建立连接。

使用特定的 LaunchPad 引脚图，可以将 Grove 模块连接到适当的引脚。每个 LaunchPad 的引脚定义可以在这里找到：[http://energia.nu/pin-maps/](http://energia.nu/pin-maps/)

在这些引脚图的帮助下，您可以知道哪个引脚具有您需要的功能。如果要将 Grove 接口 J5 连接 Grove 模拟值模块（例如电位计旋钮），则可以使用 Energia 引脚映射来找到 BoosterPack 连接器的模拟引脚。使用跳线可以将 22 引脚连接到可用的模拟引脚。例如，如果您使用的是 MSP-EXP430G2 LaunchPad，则可以使用跳线或电缆将引脚 22 与引脚 2 连接。

##   Supported Products
---
###   Grove 列表

*   [1. Buzzer](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.4e64131f26bDJh&id=520245748676)

*   [2. Relay](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.7be16298TytaHS&id=45670971061)

*   [3. 4-Digital Display ](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.19.4ff6e2d1ejfbBe&id=45908368559)

*   [4. Rotary Angle Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.17634d7dP6qL4N&id=45502678203)

*   [5. Light Sensor](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.23.6a7a1999URFa7k&id=544373791068)

*   [6. Sound Sensor ](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.19.6a7a1999URFa7k&id=45507318433)

*   [7. PIR Motion Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.1a3646352Tecv9&id=45568896887)

*   [8. Moisture Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.12.2684116ePFFANk&id=520170918975)

*   [9. Ultrasonic Ranger Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.102f1732xbTmtM&id=45550924107)

*   [10. Temperature Humidity Sensor ](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.18.2684116ePFFANk&id=520506479798)



## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/res/Grove_Base_BoosterPack_v1.0.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---
- **[Eagle 文件]**[Hardware eagle files](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/res/Grove_Base_BoosterPack_v1.0.zip)
- **[用户手册]**[Grove Starter Kit For LaunchPad User's Manual](https://github.com/SeeedDocument/Grove_Base_BoosterPack/raw/master/res/Grove%20Starter%20Kit%20Manual.pdf)
