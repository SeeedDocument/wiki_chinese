---
title: Grove - Encoder
category: Sensor
bzurl: https://seeedstudio.com/Grove-Encoder-p-1352.html
oldwikiname: Grove_-_Encoder
prodimagename: Encoder2.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/Grove Encoder.jpg
surveyurl: https://www.research.net/r/Grove-Encoder
sku: 111020001
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_wio
---

<table>
    <tr>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/img/Encoder2.jpg">
        </td>
        <td>
            <img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/img/Encoder_back.jpg">
        </td>
    </tr>
</table>

## 简介
Grove – Encoder 是一个增量旋转编码器。它将轴的旋转信号编码成电子脉冲输出信号。这个模块也属于Grove系列，有标准的Grove接口。


当您的项目需要添加一个旋钮时，比如说音量旋钮，数字旋钮等，这个产品是一个不错的选择。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.10.5e47879700GJ3i&id=45502678203)

## 产品特性
--------

* 增量式编码器
* Grove接口
* 360度旋转


!!!小提示 ：
关于Grove接口的更多信息请参考下面链接 [Grove System](http://seeed.wiki/Grove_System/)




规格参数
-------------

<table>
<tr>
<th>
项目
</th>
<th>
最小值
</th>
<th>
典型值
</th>
<th>
最大值
</th>
<th>
单位
</th>
</tr>
<tr align="center">
<td width="150">
电压
</td>
<td width="100">
4.5
</td>
<td width="100">
5
</td>
<td width="100">
5.5
</td>
<td width="100">
V
</td>
</tr>
<tr align="center">
<td>
电流
</td>
<td>
10
</td>
<td>
20
</td>
<td>
30
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<td>
尺寸
</td>
<td colspan="3">
20x 20
</td>
<td>
mm
</td>
</tr>
<tr align="center">
<td>
净重
</td>
<td colspan="3">
12
</td>
<td>
g
</td>
</tr>
</table>

平台支持
-------------------
Intel Edison (with the [seeedstudio library](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Encoder.zip))


Arduino101 (with the [community library](https://github.com/dantler/GroveEncoder))

入门指导
---------------
#### 开始之前
如果您是第一次安装Arduino库文件，请点击 [这里](http://seeed.wiki/How_to_install_Arduino_Library/) 查看库文件的安装方法。

Grove-Encoder 使用的为seeedstudio编写的库简单易用，首先请点击后面的库名下载库 [seeedstudio Encoder Lib](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Encoder.zip), 或者点击这里[community GroveEncoder library](https://github.com/dantler/GroveEncoder).  然后只需要把它接在BaseShield的D2接口上，你就可以开始使用了.

### 环形LED灯条示例
----------------
- 1.接下来的这个示例，就是展示了如何操做一个圆形的LED灯条。
这个圆形的LED灯条由Encoder和  [Grove-CircularLED](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.5e478797WCo1TF&id=45506850976) （可点击查看）两个模块组成 。将这两个模块按照下图所示连接起来:

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/img/Cirhard.jpg)

- 2.这个项目需要先点击安装下面这几个库： [TimerOne Lib](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/TimerOne.zip) 库、 [Encoder Lib](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Encoder.zip) 库和 [CircularLED Library](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/CircularLED.zip)库 。下载完上面几个库后安装在你的Arduino IDE上。

- 3.重启并打开Arduino IDE，打开 **File->Examples->Encoder->EncodeCircuiBar**。代码如下所示

```
#include <CircularLED.h>
#include <Encoder.h>
#include <TimerOne.h>
CircularLED circularLED;
unsigned int LED[24];
int index_LED;
void setup()
{
  encoder.Timer_init();
}
void loop()
{
    if (encoder.rotate_flag ==1)
  {
    if (encoder.direct==1)
    {
      index_LED++;
      if (index_LED>23)
      index_LED=24;
      SenttocircularBar(index_LED);
    }
     else
     {
      index_LED--;
      if(index_LED<0)
      index_LED=0;
      SenttocircularBar(index_LED);
     }
    encoder.rotate_flag =0;
  }
}
void SenttocircularBar(int index)
{
  for (int i=0;i<24;i++)
  {
    if (i<index)
    {
      LED[i]=0xff;
    }
    else
    LED[i]=0;
  }
  circularLED.CircularLEDWrite(LED);
}
```

-   4.下载代码到您的Arduino或Seeeduino板子里。效果如下图所示。如果您不清楚怎么下载代码，请点击[这里](http://seeed.wiki/Upload_Code/)。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/img/EncoderAndCircular_LED.gif)

<div class="admonition note">
<p class="admonition-title">！！！注意</p>

    当Grove – Encoder 被按下时，也会产生一个信号，但是基于Grove线的限制，并没有将该信号引出来。
</div>

资源
---------

-   [Encoder Spec](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Encoder_Spe.zip)
-   [Demo in Arduino forum](http://www.arduino.cc/playground/Main/RotaryEncoders)
-   [TimeOne Lib](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/TimerOne.zip)
-   [seeedstudio Encoder Library](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Encoder.zip)
-   [community Encoder Library](https://github.com/dantler/GroveEncoder/archive/v1.0.0.zip)
-   [Grove-Encoder Eagle files](https://raw.githubusercontent.com/SeeedDocument/Grove-Encoder/master/res/Grove-Encoder_eagle_files.zip)

<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Encoder -->
