---
name: Grove - Variable Color LED
category: Actuator
bzurl: https://seeedstudio.com/Grove-Variable-Color-LED-p-852.html
oldwikiname: Grove_-_Variable_Color_LED
prodimagename: Variable_Color_LED1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Variable_Color_LED
sku: 104020001
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_pi, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Variable_Color_LED/master/img/Variable_Color_LED1.jpg) ![](https://raw.githubusercontent.com/SeeedDocument/Grove-Variable_Color_LED/master/img/Variable_Color_LED_01.jpg)

这个 Grove 彩色 LED 模块由一个 8mm RGB LED 组成。它工作在 5V DC。当 SIG 引脚为高电平时，RGB LED 将亮起。模块连接 Seeeduino 的数字输出，也可以通过脉宽调制进行控制。它使用三个可调电阻来改变 RGB LED 的颜色。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.678527e0sq5Y7Z&id=45507366183)


产品特性
--------

-   兼容 Grove
-   可调节颜色

!!!Tip
    更多 Grove 模块的信息请参考 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)

创意应用
-----------------

-   玩具
-   装饰品

<div class="admonition danger">
<p class="admonition-title">Caution</p>
调节 R, G, B 三个电位器时请小心操作，不要用力过度。
</div>

规格参数
-------------

| 项目              | 典型值 | 单位 |
|-------------------|---------|------|
| 工作电压   | 5.0     | VDC  |
| 工作电流   | 20      | mA   |
| 可调电位器阻值 | &lt;1   | KΩ   |

Platforms Supported
-------------------

使用方法
-----

模块的三个电位器 RED，GREEN 和 BLUE 分别控制 R，G 和 B 通道。旋转三个电位器可以改变 LED 的颜色。需要注意的是，旋转电位器时请小心操作。


以下例子演示了控制亮度的简单应用。如下图所示，Variable Color LED 连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.22.1a292a359KD7HU&id=520233320144) 的 **D9**。硬件安装如下：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Variable_Color_LED/master/img/Grove-Variable_Color_LED.jpg)

-   把下面的代码复制并粘贴进 Arduino 的新窗口中。

示例代码如下：

```
int ledPin = 9;    // LED connected to digital pin 9

void setup()  {
    // nothing happens in setup
}

void loop()  {
    // fade in from min to max in increments of 5 points:
    for(int fadeValue = 0; fadeValue <= 255; fadeValue +=5) {
        // sets the value (range from 0 to 255):
        analogWrite(ledPin, fadeValue);
        // wait for 30 milliseconds to see the dimming effect
        delay(30);
    }

    // fade out from max to min in increments of 5 points:
    for(int fadeValue = 255; fadeValue >= 0; fadeValue -=5) {
        // sets the value (range from 0 to 255):
        analogWrite(ledPin, fadeValue);
        // wait for 30 milliseconds to see the dimming effect
        delay(30);
    }
}
```
-   上传代码，您就会看到灯明暗闪烁。


资源下载
---------

-   **[Eagle 文件]**[Variable Color LED eagle_file](https://raw.githubusercontent.com/SeeedDocument/Grove-Variable_Color_LED/master/res/Variable_Color_LED_eagle_file.zip)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Variable_Color_LED -->
