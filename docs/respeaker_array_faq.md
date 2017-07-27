## 远场麦克风矩阵可以用来做什么

获取远场声音(10米以内)，判断声音的方向。它是一个USB声卡设备，可以连接在ReSpeaker Core
或其他支持USB HID协议的设备上。

## 支持哪些操作系统？是否需要安装驱动
支持 **Windows/Linux/macOS** 操作系统，其中 **Windows** 操作系统需要安装驱动。点击[这里](https://github.com/Fuhua-Chen/ReSpeaker_Microphone_Array_Driver/raw/master/ReSpeakerMicrophoneArrayDriver.exe)下载Windows麦克风阵列驱动，双击 ReSpeakerMicrophoneArrayDriver.exe 安装。

## 是否开源？是否支持二次开发

麦克风阵列上的代码(XMOS)**不开源**，如有定制固件需求，请联系: [fae@seeed.cc](fae@seeed.cc)

## 哪里可以找到麦克风阵列的硬件／软件文档？
在ReSpeaker的[Github](https://github.com/respeaker/get_started_with_respeaker)仓库中有[硬件](https://github.com/respeaker/get_started_with_respeaker/blob/master/Introduction.md#respeaker-mic-array)和[HID协议文档](https://github.com/Fuhua-Chen/ReSpeaker-Microphone-Array-HID-tool)。

## 是否可以读出7路麦克风数据

暂时不能，目前麦克风阵列的固件输出的是波束成形融合的2路数据。

## 是否可以获取声源的位置

现在只能判断声源的方向（6个方向），而不能判断声源距离麦克风矩阵的位置。Windows下获取方式请参考[这里](https://github.com/respeaker/get_started_with_respeaker/wiki/Mic-Array)。

## 是否有回声消除功能

麦克风阵列中有回声消除功能，但效果不明显，建议在ReSpeaker Core或其他主控中实现回声消
除。

## 是否有波束成形功能

有，麦克风阵列可以专门收集一个方向的声音。

## 有问题去哪里提问

可以到ReSpeaker Github仓库的[Issues](https://github.com/respeaker/get_started_with_respeaker/issues)提问