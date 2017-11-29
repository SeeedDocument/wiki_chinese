---
title: ReSpeaker Mic Array
category: Respeaker
bzurl: https://www.seeedstudio.com/ReSpeaker-Mic-Array-Far-field-w--7-PDM-Microphones--p-2719.html
oldwikiname: ReSpeaker Mic Array
prodimagename: respeaker_mic_array.jpeg
wikiurl: http://seeed.wiki/Respeaker_Mic_Array/
sku: 107010001
---


![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/respeaker_mic_array.jpeg)

## 产品简介

ReSpeaker麦克风阵列可以堆叠（连接）到ReSpeaker Core的顶部，以显着提高语音交互体验。它是基于XMOS的XVSM-2000智能麦克风开发的。该板集成了7个PDM麦克风，以帮助将ReSpeaker的声学DSP性能提升到更高的水平。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://world.taobao.com/item/539003048162.htm?fromSite=main&spm=a1z10.5-c.w4002-11172345288.13.3c690061fgdpXG)

## 规格参数

- 远场语音捕获
- 声源定位
- 波束成形
- 噪声抑制
- 消混响
- 回音消除

## 技术规格

![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/respeaker_mic_array.jpeg)

- XVSM-2000内置16个内核:
    - 在2个xCore titles上的16个实时逻辑内核
    - 核在dual issue mode下共享2000 MIPS
    - 内部single cycle 512KB SRAM和2MB内置闪存
    - 16KB内部OTP（最大8KB每tile）
    - USB PHY，完全符合USB 2.0规范
    - 可编程 I/O.
    - 提供DFU模式.
- 7 数字麦克风:
    - 用于远场语音识别或声音定位.
    - ST MP34DT01-M.
    - -26 dBFS 灵敏度.
    - 120 dBSPL 声学过载点.
    - 61 dB 信噪比.
    - 全向灵敏度.
    - PDM 输出.
- 12 RGB LEDs:
    - 256级亮度.
    - 800kHz线数据传输.
- 音频输出:
    - 板载3.5mmAUX输出.
    - WOLFSON WM8960.
    - 24 or 16bit 16kHz立体声输出.
    - 40 mW 输出功率 16 Ω @ 3.3 V.
- 时钟同步：
    - 板载 PLL.
    - 用于 DAC,MIC的可编程采样时钟.
    (如果在XVSM-2000中使用DSP，则禁用).
- 电源:
    - Micro USB或扩展接头提供5V电源.
- 尺寸:
    - 直径 70mm.
- 重量:
    - 15.25g

## ReSpeaker 麦克风阵列驱动

- 对于Windows用户, 请单击 [此处](https://github.com/Fuhua-Chen/ReSpeaker_Microphone_Array_Driver) 安装驱动程序
- 对于Linux或Mac用户，不需要安装驱动程序

## 用ReSpeaker Core提取声音

当麦克风阵列堆叠在ReSpeaker Core上时，将自动检测（也可以通过aplay -l来手动检测）。我们建议您可以使用[respeaker_python_library](https://github.com/respeaker/respeaker_python_library)来开发语音交互应用程序，以便您不需要关心Mic Array是否打开。我们的库文件会检查并选择麦克风阵列。

此外，在该库中，基于Pyaudio的麦克风类具有名为listen的方法来提取语音。请参阅我们的示例代码以供使用。


此外，在该库中， [*class Microphone*](https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/microphone.py), 基于 **Pyaudio**, 用 [*listen*](https://github.com/respeaker/respeaker_python_library/blob/master/respeaker/microphone.py#L207), 来提取声音. 请查阅 [example code](https://github.com/respeaker/respeaker_python_library/blob/master/examples/SpeechRecognition_translator.py) 关于如何使用.

## 在PC或Mac或Linux或Raspberry Pi上提取语音

这是一个基于Pyaudio的例子：

首先，您需要运行以下脚本来获取Mic Array的设备索引号：

```Python
import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print "Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name')
```

然后，更改RESPEAKER_INDEX = 1为您的索引号。运行脚本来录制语音。

```Python
import pyaudio
import wave

RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 1
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            input_device_index=RESPEAKER_INDEX,)

print("* recording")

frames = []

for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(RESPEAKER_CHANNELS)
wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
wf.setframerate(RESPEAKER_RATE)
wf.writeframes(b''.join(frames))
wf.close()
```

## ReSpeaker麦克风阵列固件

您可以在[这里](https://github.com/Fuhua-Chen/ReSpeaker_Microphone_Array_Firmware)下载适用于DFU的ReSpeaker麦克风阵列固件。我们提供了两个版本：

- **xvsm版本**：初始版本，支持dsp输出2通道数据。
- **原始版本**：输出8路麦克风原始数据，此固件不支持xvsm dsp，因此不支持某些功能，如DOA，AEC等。

关于请查阅如何在Mac或Linux上更新固件， 请查阅 [这里](https://github.com/respeaker/mic_array_dfu) 。

## 用于控制ReSpeaker麦克风阵列的HID

用户可以通过USB HID控制ReSpeaker麦克风阵列。请参阅我们的[通信协议](https://github.com/Fuhua-Chen/ReSpeaker-Microphone-Array-HID-tool).

请注意，如果您使用 **最新的原始版本**，则只能控制LED。

这里是一个python例子：

```Python
#!/usr/bin/env python

import respeaker.usb_hid as usb_hid

class MicArray:
    def __init__(self):
        self.hid = usb_hid.get()

    def write(self, address, data):
        data = self.to_bytearray(data)
        length = len(data)
        if self.hid:
            packet = bytearray([address & 0xFF, (address >> 8) & 0x7F, length & 0xFF, (length >> 8) & 0xFF]) + data
            packet = list(packet)
            self.hid.write(packet)

    def read(self, address, length):
        self.hid.write(list(bytearray([address & 0xFF, (address >> 8) & 0xFF | 0x80, length & 0xFF, (length >> 8) & 0xFF])))
        for _ in range(6):
            data = self.hid.read()
            # print [int(x) for x in data]
            # skip VAD data
            if int(data[0]) != 0xFF and int(data[1]) != 0xFF:
                return data[4:(4 + length)]

    @staticmethod
    def to_bytearray(data):
        if type(data) is int:
            array = bytearray([data & 0xFF])
        elif type(data) is bytearray:
            array = data
        elif type(data) is str:
            array = bytearray(data)
        elif type(data) is list:
            array = bytearray(data)
        else:
            raise TypeError('%s is not supported' % type(data))
        return array

def main():
    import sys
    import struct

    mic = MicArray()

    print("Using: %s" % usb_hid.usb_backend)

    if len(sys.argv) < 3:
        print('Usage: python {} w 0x0 0x000003'.format(sys.argv[0]))
        sys.exit(1)

    try:
        if sys.argv[2].startswith('0x'):
            address = int(sys.argv[2], 16)
        else:
            address = int(sys.argv[2])

        if sys.argv[1] == 'w':
            if sys.argv[3].startswith('0x'):
                data = int(sys.argv[3], 16)
            else:
                data = int(sys.argv[3])

            if data > 0xFFFF:
                data = struct.pack('<I', data)
            elif data > 0xFF:
                data = struct.pack('<H', data)

            mic.write(address, data)
        else:
            print [int(x) for x in mic.read(address, 4)]
    except Exception as e:
        print(e.message)

if __name__ == '__main__':
    main()
```

## FAQ（常见问题汇总）

### Q1： Respeaker Mic Array驱动安装问题？
Windows需要安装驱动，linux（Ubuntu,Raspberry,MAC等）不需要安装驱动。点击[这里](https://github.com/Fuhua-Chen/ReSpeaker_Microphone_Array_Driver/raw/master/ReSpeakerMicrophoneArrayDriver-20171017.zip)下载驱动。在windows系统的设备管理器，看到麦克风阵列不能被识别，请安装以下流程来操作。

-  [安装驱动](https://github.com/Fuhua-Chen/ReSpeaker_Microphone_Array_Driver/raw/master/ReSpeakerMicrophoneArrayDriver.exe)

-  换USB线

-  [禁用数字签名](http://jingyan.baidu.com/article/624e74594dbc8d34e8ba5aa6.html)

-  换其他电脑尝试

### Q2： Respeaker Mic Array如何采集音频？

- 下载[Audacity](http://www.audacityteam.org/)软件来采集, 在windows下具体参数设置，请参卡![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/audacity.png) 。

如果按照以上设置采集数据失败，请重新安装驱动。

-  利用Python脚本来采集音频数据：

    - XVSM固件采集2通道音频： （支持Unbuntu/Raspberry/Mac）

        - 首先用[XVSM_RecordAudio_Ubuntu_Raspberry_Mac_getDeviceInfo.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/2_Channel_XVSM_firmware_Python_Scripts/Record_Audio/XVSM_RecordAudio_Ubuntu_Raspberry_Mac_getDeviceInfo.py)   检测麦克风阵列的输入通道。

        - 然后更改[XVSM_RecordAudio_Ubuntu_Raspberry_Mac_recordaudio.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/2_Channel_XVSM_firmware_Python_Scripts/Record_Audio/XVSM_RecordAudio_Ubuntu_Raspberry_Mac_recordaudio.py) 的 **RESPEAKER_INDEX = 2** 的 2为检测到的通道， 运行程序来采集音频。

    - RAW固件采集8通道音频：（支持Unbuntu/Raspberry/Mac）

        - 首先用[Raw_RecordAudio_Ubuntu_Raspberry_Mac_getDeviceInfo.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/Record_Audio/Raw_RecordAudio_Ubuntu_Raspberry_Mac_getDeviceInfo.py) 麦克风阵列的输入通道。

        - 然后更改[Raw_RecordAudio_Ubuntu_Raspberry_Mac_recordaudio.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/Record_Audio/Raw_RecordAudio_Ubuntu_Raspberry_Mac_recordaudio.py) 的**RESPEAKER_INDEX = 2** 的 2为检测到的通道 ， 运行程序来采集音频。

### Q3： Respeaker Mic Array如何定位？

- XVSM固件来定位： （支持Unbuntu/Raspberry/Mac）

    - 运行脚本[XVSM_VAD_Ubuntu_Raspberry_Mac_get_direction.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/2_Channel_XVSM_firmware_Python_Scripts/VAD/XVSM_VAD_Ubuntu_Raspberry_Mac_get_direction.py) 来定位

- RAW固件来定位： （支持Unbuntu）
    - 运行脚本[Raw_vad_doa_Ubuntu_get_direction.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/VAD/Raw_vad_doa_Ubuntu_get_direction.py) 来定位， 注意需要下载 [gcc_phat.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/VAD/gcc_phat.py)， [mic_array.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/VAD/mic_array.py)， [pixel_ring.py](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts/8_Channel_Raw_firmware_Python_Scripts/VAD/pixel_ring.py)3个库文件，放在同一个目录下。

### Q4： Respeaker Mic Array Python程序下载？

请点击[这里](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker_Mic_array_Scripts.zip)下载Python采集音频和定位的全部程序。

### Q5： Respeaker Mic Array咪头的物理位置和Audacity的通道位置？

- 咪头位置如下图所示
![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/MIC_Physic_location.png)

- Audacity的通道位置
![](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/img/mic_array_channels_Audacity.png)


## 资源下载

- **[Eagle]**[ReSpeaker Microphone Array SCH](hhttps://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker%20Microphone%20Array%20v1.0.sch.zip)
- **[Eagle]**[ReSpeaker Microphone Array BRD](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker%20Microphone%20Array%20v1.0.brd.zip)
- **[PDF]** [ReSpeaker Microphone Array SCH](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker%20Microphone%20Array%20v1.0%20Sch.pdf)
- **[PDF]** [ReSpeaker Microphone Array PCB](https://github.com/SeeedDocument/ReSpeaker_Mic_Array/raw/master/res/Respeaker%20Microphone%20Array%20v1.0%20PCB.pdf)
