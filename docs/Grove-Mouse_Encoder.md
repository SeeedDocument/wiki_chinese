---
title: Grove - Mouse Encoder
category: Sensor
bzurl: https://seeedstudio.com/Grove-Mouse-Encoder-p-2607.html
oldwikiname: Grove_-_Mouser_Encoder
prodimagename: Grove-Mouse_Encoder_product_view.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Mouse_Encoder
sku: 103020030
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/img/Grove-Mouse_Encoder_product_view.jpg)

Grove - Mouse Encoder 是一种具有旋转方向和旋转速度<sup>\[1\]</sup>并能够反馈数据的机械增量式旋转编码器。 它有标准的 Grove 接口，可以节省大量的布线和编程工作。 而且，它适应了高负荷和恶劣的环境。 该产品可用作玩具，机器人和消费者输入设备。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.62cef9daU7kaMK&id=531866084012)

<div class="admonition note">
<p class="admonition-title">note</p>
设计的旋转速度应小于1000 rad / min（弧度/分钟）.
</div>

产品特性
--------

- 能够适用于不同的环境。
- 适应高负荷和恶劣环境。
- 具有良好的制动性能。
- 标准 Grove 接口，便于编程和接线。
- 准确可靠。

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

创新应用
------------

它能够适应恶劣环境中的不同应用，如玩具，机器人和消费者输入设备。

规格参数
--------------

| 项目                           |最小值| 标准值 | 最大值 |
|----------------------------------|------|---------|------|
| 工作电压 (V)             |      | 3.3     | 5.5  |
| 工作电流 (mA)            |      | 10      | 13   |
|效率（恒速）             |      | 50%     |      |
| 相位差（恒速） |      | π/4     |      |
| 每圈脉冲               |      | 12      |    -  |

<div class="admonition note">
<p class="admonition-title">注意</p>
<ol><li>产品列表中没有旋钮项。 因为我们认为这样可以使编码器更能适应在不同的环境下工作。</li>
<li>你能找到 <a href="https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/res/Grove-Mouse_Encoder_Dimensions.pdf">dimensions</a> 的 PDF 文件，您可以根据尺寸选择。</li><ol>
</div>

<div class="admonition tip">
<p class="admonition-title">小提示</p>
如果您只是为项目构建样板原型，您可以使用合适的六角螺丝刀刀头调节。
</div>

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/img/Grove-Mouse_Encoder.jpg)

**Grove 界面**   
连接主控板如 **Seeeduino** 板与驱动板。

**六角开口**   
用于通过旋钮的开口

### **零件清单**

| 零件名称                              | 数量 |
|------------------------------------------|----------|
| Grove - Mouse Encoder ( 不包括旋钮 ) | 1 PC     |
| Grove - Universal Cable                  | 1 PC     |

入门指导
-----------

本节将介绍如何使用 Grove - Mouse Encoder 构建 IDE 环境以构建应用程序。

请参阅 [Seeeduino V4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)（可以与 Arduino 板交换），了解如何为应用程序构建完整的 IDE ，如果您使用Arduino原版，请阅读 [Arduino 指南](https://www.arduino.cc/en/Guide/HomePage)

<div class="admonition note">
<p class="admonition-title">注意</p>
<ol><li>如果旋转速度越慢，负荷会越大。</li>
<li>如果旋转速度不恒定，脉冲宽度（PW）不会相同。</li>
<li>旋转速度应低于 1000 rad / min，否则会导致输出脉冲宽度 PW 过窄，或损坏该编码器。</li>
<li>由于该编码器内的脉冲位置不确定，因此不旋转时环境的输出电压将不确定（高或低电压）。</li></ol>
</div>

### 基本演示

此示例演示如何检测位置和检测方向。

#### 材料准备

-   Seeeduino V4.2
-   Base shield V2.0
-   USB 数据线 ( A 型口到 B 型口)

#### 连接方式

连接材料如下图所示：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/img/Grove-Mouse_Encoder_demo_connection.jpg)

#### 代码

```
/* Read Quadrature Encoder
* Connect Encoder to Pins encoder0PinA, encoder0PinB, and +5V.
*
* Sketch by max wolf / www.meso.net
* v. 0.1 - very basic functions - mw 20061220
*
*/  
 
 
int val;
int encoder0PinA = 3;
int encoder0PinB = 4;
int encoder0Pos = 0;
int encoder0PinALast = LOW;
int n = LOW;
 
void setup() {
    pinMode (encoder0PinA,INPUT);
    pinMode (encoder0PinB,INPUT);
    Serial.begin (115200);
}
 
void loop() {
    n = digitalRead(encoder0PinA);
    if ((encoder0PinALast == LOW) && (n == HIGH)) {
        if (digitalRead(encoder0PinB) == LOW) {
            encoder0Pos--;
        } else {
            encoder0Pos++;
        }
        Serial.println(encoder0Pos);
        Serial.println ("/");
    }
    encoder0PinALast = n;
}
```

1. 复制代码并将其载入到控制器板中。
2. 打开监视器窗口。
3. 向左或向右转动螺丝刀，观察现象。

输出：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/img/Grove_mouse_encoder_output_of_demo.png)

资源下载
---------

- [Schematic files](https://raw.githubusercontent.com/SeeedDocument/Grove-Mouse_Encoder/master/res/Grove_Mouse_Encoder_v1.0_Schematic_File.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Mouser_Encoder -->
