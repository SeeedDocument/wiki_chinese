---
title: Music Shield V2.2
category: Shield
bzurl: https://www.seeedstudio.com/Music-Shield-V2.0-p-1372.html
oldwikiname: Music_Shield_V2.2
prodimagename: Music_Shield_Picture.jpg
bzprodimageurl: https://statics3.seeedstudio.com/images/107020003 1.jpg
surveyurl: https://www.research.net/r/Music_Shield_V2_2
sku: 107020003
---

![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Music_Shield_Picture.jpg)

是时候建立您的实时 MIDI 乐器/音乐播放器了！ 它可以播放多种格式，包括 MP3，WMA，WAV，AAC，MIDI，Ogg Vorbis 。 Music Shield 是与 Arduino，Seeeduino，Seeeduino Mega 和 Arduino Mega 兼容的音频编码器/解码器。 它基于 VC1053B 芯片，使其能够从 SD 卡播放音频文件，并进行短时记录。 您还可以使用它轻松更改其硬件安装来播放 MIDI 音符。 由于 SPI 通信模式，它保留了 IO 端口的最小数量，便于用户自己开发此设备。 此外，新的多功能按钮为用户提供了更大的便利。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.11e6c25ajOVbcq&id=45589232160)


<div class="admonition note">
<p class="admonition-title">注意</p>
录音功能仅适用于 Seeeduino Mega 和 Arduino Mega 。 而您可以使用的最大容量 SD 卡是 2GB 。
</div>

## 兼容性

我们生产了大量的扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里使用表格来说明这些板与平台板的兼容性。

!!!note
    请注意，“不推荐”意味着它可能有机会与平台板兼容，但需要额外的工作，如跳线或重写代码。 如果您有兴趣了解更多，欢迎与techsupport@seeed.cc联系。

**点击查看完整图片**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Music_shield_frame.jpg)

**多功能按钮：** 更改音量并选择歌曲。

**播放/暂停指示灯（绿色）：** 播放时闪烁。

**耳机接口：** 可驱动 16 ohm 或 32ohm 耳机，可作为外部音频输入端口。

**Micro SD卡**：可以是 FAT16 或 FAT32 ，可以使用的最大容量 SD 卡是 2GB。

**U2：** VS1053B IC，Ogg Vorbis / MP3 / AAC / WMA / FLAC / MIDI 音频编解码器。

**U3，U7：** 74VHC125 IC，Quad Buffer

**I2S：** 用于数字音频输入/输出。

**ISP接口**：用于在与 Mega 系列产品一起使用时带来 SPI 端口。

### Arduino 上引脚的使用

**用于播放控制的引脚：**

D3 - 接收增加音量按钮的信号。

D4 - 接收下一首歌曲功能按钮的信号。

D5 - 接收用于播放和停止和录制功能按钮的信号。

D6 - 接收上一首歌曲功能按钮的信号。

D7 - 接收降低音量按钮的信号。

D8 - 绿色指示。

**用于 SPI 接口的引脚:**

D10 - SPI 片选

D11 - SPI MOSI

D12 - SPI MISO

D13 - SPI SCK

**用于VS1053接口的引脚:**

A0 - VS1053 的复位

A1 - VS1053 的数据要求

A2 - VS1053 的数据选择

A3 - VS1053 的芯片选择

## 入门指导
---------------

![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Music_shield4.jpg)

<div class="admonition note">
<p class="admonition-title">注意</p>
<ol><li>如果要使用 MIDI 功能，则需要更改硬件安装。</li>
<li>如果您更改了硬件安装来使用 MIDI 功能，则将其恢复到原始状态之前，您将无法使用播放和录制功能。</li></ol>
</div>


### ** 音乐播放**

1. 确保 micro SD 卡中有歌曲。
2. 下载 [Music shield V2.0 库](https://github.com/Seeed-Studio/Music_Shield)
3. 将文件夹解压缩并复制到 Arduino 的库路径：**.. \ arduino-1.0 \ libraries**。

<div class="admonition note">
<p class="admonition-title">注意</p>
<ol><li>如果 Arduino 在加载时发生错误，请更改提取的库的文件夹名称。</li>
<li>如果在编译时存在<span style =“font-style：italic”>'arduino.h：没有这样的文件或目录'</ span>错误，请更改示例文件中包含的标题（to Arduino.h）。</li></ol>
</div>

**演示1：播放歌曲（例如以随机播放模式播放）**

为了使用播放功能，您需要先创建一个播放列表。

1. 重新启动 Arduino IDE 。 通过路径打开 “creatList” 示例 : **File（文件） --> Examples（示例） --> MusicPlayer --> creatList as below**.

    ![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/OpenCreatListCode.jpg) 

2. 设置播放模式。 在 “creatList” 中，我们使用的功能描述如下。

    **名称:** setPlayMode(unsigned char playmode);

    **功能:** 设置播放模式。 可以设置四种模式： MODE_NORMAL，MODE_SHUFFLE，MODE_REPEAT_LIST，MODE_REPEAT_ONE。  每种模式代表不同的播放顺序。

    ![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Play_Mode.jpg)

3. 选择您正在使用路径的 Arduino 板的类型： **Tools（工具） --> Board（板） --> Arduino UNO.**
4. 选择路径正在使用的正确的串口: **Tools（工具） --> Serial Port（串行端口） -->  COM3.**
5. 上传代码。当“完成上传”出现时，点击串行监视器，您会发现歌曲的顺序是在列表中随机化的。

    ![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Play_List.jpg)

当按下多功能按钮时，音量将会改变。 当然，你也可以尝试别的播放模式。

**演示2：播放所选歌曲**

1. 本演示将向您展示如何播放 SD 卡中所有歌曲的部分歌曲。 通过路径打开 “addToList” 示例： **File（文件） --> Examples（示例） --> MusicPlayer -->  addToList .**

    ![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Select_play.jpg)

2. 从播放列表中选择歌曲。您只需要在函数 addToPlayList（char * songName） 中按名称正确列出要播放的歌曲。
但您必须确保该歌曲已存储在SD卡中，并且这些歌曲的格式必须是 MP3，WMA，WAV，AAC，MIDI，Ogg Vorbis 之一。

3. 上传代码。 完成上传后，将播放新的添加歌曲。

**演示3：从模拟端口控制音量**

1. 将 Grove-Base Shield 连接到 Music shield 上，使用 Grove 连接线连接 Rotary 的 Grove 端口和 Base Shield 的模拟端口 **4** 。 您也可以更改为数字端口。 但是不要忘了在演示代码的定义中同时更改端口号。

    ![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Music_shield_5.jpg)

2. 打开 “analogInputControl” 示例并将其上传到您的 Arduino 板上。

3. 旋转旋钮更改音乐音量。

**演示4：录音：（仅支持 ATmega1280 和 ATmega2560 ）**

1. 在 Music Shield 库中上传程序，例如程序 “creatList” 。 打开串行监视器，它将在 SD 卡上播放音频文件。
2. 按下多功能按钮 5 秒钟，然后指示灯将熄灭。
3. 再次按下多功能按钮 5 秒钟，然后音乐屏幕开始录制，绿色指示灯将闪烁。
4. 再次快速按下多功能按钮，将停止录制。
5. 记录将在最后一个地方播放。

### **使用 MIDI ，无需修改硬件**

VS1058X 的实时 MIDI 模式：

通过 SPI 或 UART 发送的 MIDI 命令即可实现“实时 MIDI 模式”，可通过以下方法启用：

方法：一开始，通过 SPI 端口发送一个小的软件补丁。

```
    /*software patch for MIDI Play*/
const unsigned short gVS1053_MIDI_Patch[28]={
    /*if you don't let GPIO1 = H,please send this patch by spi*/
    0x0007, 0x0001, 0x8050, 0x0006, 0x0014, 0x0030, 0x0715, 0xb080, /* 0 */
    0x3400, 0x0007, 0x9255, 0x3d00, 0x0024, 0x0030, 0x0295, 0x6890, /* 8 */
    0x3400, 0x0030, 0x0495, 0x3d00, 0x0024, 0x2908, 0x4d40, 0x0030, /* 10 */
    0x0200, 0x000a, 0x0001, 0x0050,
};
using that function to load:
    /*
    **@ function name: loadMidiPatch
    **@ usage:load a software patch for vs10xx
    **@ input:none
    **@ retval:none
    */
void VS10XX::loadMidiPlugin(void)
{
    int i=0;
    Serial.print("load MIDI Plugin...\r\n");
    while(i < sizeof(gVS1053_MIDI_Patch)/sizeof(gVS1053_MIDI_Patch[0]))
    {
        unsigned short addr, n, val;
        addr = gVS1053_MIDI_Patch[i++];
        n = gVS1053_MIDI_Patch[i++];
        while(n--)
        {
            val = gVS1053_MIDI_Patch[i++];
            writeRegister(addr, val >> 8, val&0xff);
        }
    }
    Serial.print("done\r\n");
}
```

您需要知道的是，有一个名为 jdksmidi 的开放源码库，您可以通过一些小的更改来制作自己的 MIDI 解码器。 [jdksmidi git-hub page](https://github.com/jdkoftinoff/jdksmidi) 为您提供了一些实时模式的 MIDI API （MusicPlayer.cpp）：
```
     midiNoteOn()
     midiNoteOff()
     midiWriteData()
```
现在是以任何模式（单通道或多通道）构建您的实时 MIDI 乐器/音乐播放器的时候了。 对于您的贡献我们将不胜感激。 演示 MIDI 播放器被添加到最新的库。  MIDI 演示（上传代码，完成后，您将听到 Fancy MIDI 音乐）：

![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/Music_shield_midi_demo.jpeg)

供参考
---------

**MIDI 号码备注参考列表**

![](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/img/MIDIlist.gif)

## 资源下载
---------

- [Music Shield V2.2 Eagle Files](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/res/Music_Shield_v2.2.zip)
- [Music Shield V2.2 Schematic.pdf](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/res/Music_Shield_v2.2_pdf.pdf)
- [VS1053 Datasheet](https://raw.githubusercontent.com/SeeedDocument/Music_Shield_V2.2/master/res/VS1053.pdf)
- [Music Shield libraries](https://github.com/Seeed-Studio/Music_Shield)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Music_Shield_V2.2 -->
