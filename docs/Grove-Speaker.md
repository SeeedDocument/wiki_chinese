---
title: Grove - Speaker
category: Actuator
bzurl: https://seeedstudio.com/Grove-Speaker-p-1445.html
oldwikiname: Grove_-_Speaker
prodimagename: Grove_Speaker_01.jpg
wikiurl: http://seeed.wiki/Grove-Speaker
sku: 107020001
tags: grove_digital, io_5v, plat_duino, plat_wio
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/img/Grove_Speaker_01.jpg)

Grove- Speaker 是一个由功率放大器和声音输出部分组成的模块。响度可以通过板载电位器进行调整。在不同的输入频率下，扬声器会产生不同的音调。将音乐编码进 Arduino，DIY 自己的音乐盒吧 !

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.20.12a3e2204K97PC&id=45477159219&ns=1&abbucket=1#detail)

## 产品特性
-------

-   音量可调
-   Grove 接口

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)


## 规格参数
-------------

| 项目            | 最小值 | 典型值 | 最大值 | 单位 |
|-----------------|-----|---------|-----|------|
| 工作电压 | 4.0 | 5.0     | 5.5 | VDC  |
| 电压增益    | -   | -       | 46  | db   |
| 带宽      | -   | -       | 20  | KHz  |

## Platforms Supported
-------------------

## 使用方法
-----

扬声器可以发出各种声音，如汽车喇叭，门铃和点火器。不同的声音是基于输入信号的频率。

您可以使用 Arduino 为该模块提供不同的频率信号。Arduino 通过 PWM 产生这些信号，或者通过数字写入和延迟。在这里我们将向您展示如何使用 *delay()*，产生信号使扬声器发低音 1~7。

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/img/Tone.jpg)

```
/*macro definition of Speaker pin*/
#define SPEAKER 3

int BassTab[]={1911,1702,1516,1431,1275,1136,1012};//bass 1~7

void setup()
{
    pinInit();
}
void loop()
{
        /*sound bass 1~7*/
    for(int note_index=0;note_index<7;note_index++)
    {
        sound(note_index);
        delay(500);
    }
}
void pinInit()
{
    pinMode(SPEAKER,OUTPUT);
    digitalWrite(SPEAKER,LOW);
}
void sound(uint8_t note_index)
{
    for(int i=0;i<100;i++)
    {
        digitalWrite(SPEAKER,HIGH);
        delayMicroseconds(BassTab[note_index]);
        digitalWrite(SPEAKER,LOW);
        delayMicroseconds(BassTab[note_index]);
    }
}
```
<div class="admonition note">
<p class="admonition-title">Note</p>
由于电容的影响，模块只能输出低音信号，不能发出高音。
</div>

## 资源下载
--------

-   **[Eagle文件]** [Grove - Speaker Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/res/Grove-Speaker_Eagle_File.zip)
-   **[PCB图PDF]** [Grove\_-\_Speaker\_v1.0\_brd.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/res/Grove-Speaker_v1.0_brd.pdf)
-   **[原理图PDF]** [Grove\_-\_Speaker\_v1.0\_sch.pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/res/Grove-Speaker_v1.0_sch.pdf)
-   **[芯片数据手册]** [LM386 Low Voltage Audio Power Amplifier Datasheet](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/res/LM386_Low_Voltage_Audio_Power_Amplifier_Datasheet.pdf)
-   **[其他资源]** [How to generate different tone with MCU](https://raw.githubusercontent.com/SeeedDocument/Grove-Speaker/master/res/Tone.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Speaker -->
