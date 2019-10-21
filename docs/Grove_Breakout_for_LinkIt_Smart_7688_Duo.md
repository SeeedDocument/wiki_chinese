---
name: Grove Breakout for LinkIt Smart 7688 Duo
category: LinkIt
bzurl: https://www.seeedstudio.com/Grove-Breakout-for-LinkIt-Smart-7688-Duo-p-2575.html
oldwikiname: Grove Breakout for LinkIt Smart 7688 Duo
prodimagename: Breakout_for_LinkIt_Smart_7688_product_view_1200_s.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Breakout_for_LinkIt_Smart_7688_Duo
sku: 103030032
---

---
![](https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/img/Breakout_for_LinkIt_Smart_7688_product_view_1200_s.jpg)

LinkIt Smart 7688 Duo 的 Grove Breakout 是集成了 Grove 端口的 LinkIt Smart 7688 Duo[1] 的功能扩展板。通过使用这些接口，进行原型设计时可以节省大量的工作，即使是一个没有电子知识的初学者也可以快速开始项目。它支持 I2C，UART 等串行总线，并可访问 LinkItTM Smart 7688 Duo 的引脚。

[1]：LinkItTM Smart 7688 Duo 是一款基于 OpenWrt Linux 系统，MT7688 和 ATmega32u4 的开放式开发板。该板特别设计用于实现智能家居的丰富应用开发原型。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.26.6b0bd85bsPIp0Z&id=524891862285)

## 产品特性
---
- Grove 接口，使接线更容易。
- 更多 Grove 接口，可扩展使用丰富的 Grove 模块。
- 性价比高。

!!!Tip
    想了解更多，请访问 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)

## 创意应用
---
- 智能家居/网管硬件
- 机器人
- 智能多媒体设备
- 教学

## 规格参数
---
- 输入电压：5.0V (使用 USB 接口供电)
- 工作电压：3.3V
- 调试引脚连接到 MT7688，其他引脚连接到 ATmega32U4。


## 硬件概述
 ---
 ![](https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/img/Grove_Breakout_for_LinkIt_Smart_7688_Duo_component_with_text_1200_s.jpg)

 !!!Note
     在插入 LinkIt Smart 7688 Duo 时，注意按照扩展板上丝印标识的方向插入。

**Grove 接口**

连接丰富的 Grove 接口功能模块。使用这种接口，您不需要跳线或焊接，就可以使用这些功能模块制作更丰富的项目。

## 入门指导

**准备材料**

- LinkIt Smart 7688 Duo × 1
- USB 线 (type A 转 micro type-B) × 1
- USB 转串口模块 × 1
- 跳线 × 3
- Grove - Buzzer × 1

**使用 Grove - Buzzer 发出声音**

1. 参考 [wiki of LinkIt Smart 7688 Duo](http://wiki.seeedstudio.com/cn/LinkIt_Smart_7688_Duo/) 把您的 LinkIt Smart 7688 Duo 连接到网络。
!!!Note
    * 您可以在连接 LinkIt Smart 7688 的端口附近找到 8，9 和 GND 引脚。
    * 您可以用跳线连接 MT7688 UART2 端口，而不是将其焊接到引脚 8，引脚 9 和引脚 GND。

2. 将 USB 转串口模块连接到 LinkIt Smart 7688 Duo 后打开控制台。

3. 连接所有部件，如下所示：
![](https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/img/Arduino_Breakout_for_LinkIt_Smart_7688_Duo_demo_connection_view_1200_s.jpg)
!!!Note
  把 Grove - Buzzer 插在 **D4** 口上。

4. 请查看 [这里](http://wiki.seeedstudio.com/cn/LinkIt_Smart_7688_Duo/#arduino) 在主机上为 LinkIt Smart 7688 Duo 平台搭建 Arduino 开发环境。

5. 下载 [firmata](https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/res/Firmata_to_build_Arduino_IDE_for.zip)。参考 [这里](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688_Duo#Installing_Arduino_programming_environment) 安装 Arduino IDE 的 LinkIt Smart 7688 平台，然后把文件 firmata 保存到开发板。
!!!Note
    以下步骤应在嵌入式操作系统（OpenWRT）上执行。 请确保你的系统中有 Python，并且安装了 pip。

6. 在控制台输入 **pip install pyfirmata**，然后按 Enter 安装 python 库 pyfirmata。

7. 在控制台中输入 **vi buzzer.py** 创建一个名为 **buzzer.py** 的文件，将下面的代码复制过去。
```python
from pyfirmata import Arduino, util
from time import sleep
board = Arduino('/dev/ttyS0')
print "Start blinking D4"
while True:
  board.digital[4].write(1)
  sleep(0.5)
  board.digital[4].write(0)
  sleep(0.5)
```

8. 保存 **buzzer.py** 并输入 **python buzzer.py** 来运行示例代码。

9. 现在你会听到蜂鸣器的声音。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/res/Schematic_files_for_Grove_Breakout_for_LinkIt_Smart_7688_Duo.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---
- **[原理图]**[Schematic files](https://github.com/SeeedDocument/Grove-Breakout_for_LinkIt_Smart_7688_Duo/raw/master/res/Schematic_files_for_Grove_Breakout_for_LinkIt_Smart_7688_Duo.zip)
- **[OpenWrt 开发者指南]**[OpenWrt](http://wiki.openwrt.org/doc/howto/user.beginner)
