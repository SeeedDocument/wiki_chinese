---
name: ADALM-PLUTO Overview
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 114991964
tags:
---

![](https://github.com/SeeedDocument/ADALM-PLUTO/raw/master/img/20190919162509.jpg)


[ADALM-PLUTO](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.47de33dbtP20su&id=602768931251) 主动学习模块（PlutoSDR）是ADI公司 （ADI） 提供的一种易于使用的工具，该工具可用于向电气工程相关专业的学生介绍 [软件定义无线电 (SDR)](https://en.wikipedia.org/wiki/Software-defined_radio)、[射频 (RF)](https://en.wikipedia.org/wiki/Radio_frequency) 和[通信](https://en.wikipedia.org/wiki/Communication_theory)的基础知识，学生亦可通过自学或者请教讲师深入了解相关内容。该模块能帮助不同层次和背景的学生更好地了解实际生活中RF相关运用，从而为学生攻读理学、技术或工程学学位打下良好的基础。
PlutoSDR主动学习模块将理论和RF的实际运用结合起来，连接上主机时，它就能充当一个便携式实验室，学生甚至能将它带入教室使用。大量的软件，例如MATLAB和simulink，提供了全新的图形用户界面（GUI），使用更加直观、方便，让学习曲线最小化，帮助学生更高效率地学习、工作和探索。


[ADALM-PLUTO](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.47de33dbtP20su&id=602768931251) 主动学习模块适用于所有人。


ADALM-PLUTO主动学习模块基于 [AD9363](http://www.analog.com/AD9363)，分别配备了可在全双工模式下工作的一条接收通道和一条发射通道。该模块能够以高达61.44MSPS的采样速率和20MHz的带宽产生和测量频率范围在325MHz到3800MHz之间的RF模拟信号。PlutoSDR体积小巧，可以轻松装进衣服口袋或者背包中，使用灵活，采用配备默认固件的USB端口供电。该模块支持OS XTM、WindowsTM和LinuxTM，因此使用者可以在不同的时间、不同的设备上学习和探索RF系统。


<div align="center"><a href="https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.9.47de33dbtP20su&id=602768931251" target="_blank"><img src="https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/300px-Get_One_Now_Banner-ragular.png"></a></div>


## 简介

PlutoSDR 是一个自给自足的掌上RF实验室，它不仅仅是零碎部分的简单组合，您需要知道模块当中每一部分的基本操作才能了解模块的功能。不同需求的用户会使用到不同的软件，针对不同用户，我们列出了以下情况。为避免在使用过程中出现一些问题，阅读文档前，请务必仔细确认您的用途。

<div class="tips" style="display: table; table-layout: fixed; background-color: #e3efff; height: auto; width: 100%; ">
<div class="left-icon" style="display: table-cell; vertical-align: middle; background-color: #a3c7ff; padding-top: 10px; box-sizing: border-box; height: auto; width: 38px; text-align: center;"><img style="width: 26px; vertical-align: middle;" src="https://s3-us-west-2.amazonaws.com/static.seeed.cc/seeed/icon/Note.svg" alt="attention icon" /></div>
<div class="right-desc" style="display: table-cell; vertical-align: middle; padding-left: 15px; box-sizing: border-box; width: calc(95% - 38px);">
<p style="font-weight: bold; margin-top: 10px;">Note</p>
<p style="font-size: 14px;">与电脑连接时，PlutoSDR将被识别为一个大容量存储设备，里面包含入门指南（info.html）、设备配置控制文件（config.txt）以及许可证信息（LICENSE.html）。</p>
</div>
</div>

## 目录


### [1.普通用户和学生指南](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-for-End-User/)
- 正常情况下，PlutoSDR用户可以使用USB并通过软件实现与射频信号实现交互。PlutoSDR支持MATLAB、simulink、开源软件无线电、custom C、C++、C#或者Python，支持的系统有Windows(X86)、Linux、Mac或者嵌入式Linux平台（包括 [Raspberry Pi](https://www.raspberrypi.org/)、[Beaglebone](http://beagleboard.org/)、[96boards.org](http://www.96boards.org/) 等以及您常用的一些平台）。
- 如果您想知道 PlutoSDR 是怎样 [产生波形](https://wiki.analog.com/university/tools/pluto/users/iioscope/generate) 和 [捕获射频波形](https://wiki.analog.com/university/tools/pluto/users/iioscope/capture) 的，请看这里。
- 这部分内容阐述了该产品的概况，指导用户正确下载驱动和安装软件，因此我们建议每位用户仔细阅读。
- 这一部分包含大部分用户所需的信息。


### [2.开发者指南](https://wiki.analog.com/university/tools/pluto/developers)
- 硬件描述语言（针对于FPGA）是直接在PlutoSDR上运行的，编写定制的软件会让 PlutoSDR 工作在不同模式下，支持不同的外部USB设备（包括经过USB端口的局域网或WiFi），从而实现设备功能扩展。里面包含了编译HDL工程、编译内核以及为满足定制USB供应商和厂商识别码及运行定制的用户空间应用而作出修改的所有信息。例如，您可以建立：
    - 通过WiFi或局域网联网的独立机场跟踪站。
    - 移动端虚拟键盘。

### [3.SDR 高手指南](https://wiki.analog.com/university/tools/pluto/hackers)
- 您可能希望拿到产品的印制电路板并修改一部分硬件，将通用输入输出口连接上不同的设备，或者尝试让多个的 PlutoSDR 同步运行。实际上我们的产品是开源的，因此我们会提供所有您需要的信息，包括原理图和版图文件。


### [4.SDR 工程师指南](https://wiki.analog.com/university/tools/pluto/engineers)
- 我们不建议您直接使用PlutoSDR，您可以参考我们产品中出现的一些问题，设计并改进自己的SDR。我们也非常欢迎把 PlutoSDR 的硬件、软件或HDL当中的一部分用于其他的产品。您也可以通过观察PlutoSDR里面的 [AD9363](https://www.google.com/search?q=AD9363&btnI=lucky) 芯片对于定制波形的响应情况来决定它是否适用于您的系统。如果您需要一个能够帮助您检测其他 RF 工程是否正常工作、频率在325MHz到3800MHz之间的、低成本的频谱仪，而我们的设备能帮助您解决问题，您可以阅读这部分的内容。



我们希望以上的内容可以对大部分用户的工作和学习起到帮助作用，我们也会不断更新上面的内容，如果您有任何疑问，可以在 [EngineerZone](http://ez.analog.com/community/university-program) 向我们咨询，或者点击 [帮助和支持](https://wiki.analog.com/university/tools/pluto/help_support)。



- 入门指南
    - 1.快速启动
    - 2.硬件细节
    - 3.更新固件
    - 4.支持的驱动和库
    - 5.IIO工具
- 教育
    - 1.面向工程师的SDR技术
    - 2.RF背后的数学原理
- 故障排除和疑难解答
- 软件应用和运行环境
    - 1.MATLAB和simulink（Windows/macOS/Linux）
    - 2.GNURadio（Linux）
    - 3.gqrx（macOS/Linux）
    - 4.SDR Angel（Windows）
    - 5.IIO-Scope（Windows/macOS/Linux）
- 支持的高级语言
    - 1.程序化脚本（Shell scripts）
    - 2.C和C++
    - 3.Python
- 应用说明、示例和测试
    - 1.dump1090（ADS-B）
    - 2.FM收音机
    - 3.simRF模型
    - 4.独立的Pluto
    - 5.Plutogps
- 高级配置
    - 1.基于MATLAB的滤波器设计向导
    - 2.使用USB闪存盘
    - 3.使用无线网卡
    - 4.使用有线以太网适配器
    - 5.构建自定义内核映像
    - 6.构建自定义FPGA映像
- 硬件配件 
    - 1.天线
    - 2.EVAL-CNXXXX：Pluto放大器
- 对外发布
    - 1.GRCon
    - 2.自由及开源软件开发者欧洲会议
    - 3.市场宣传资料




<div class="tips" style="display: table; table-layout: fixed; background-color: #ffdde3; height: auto;  width: 100%;">
<div class="left-icon" style="display: table-cell; vertical-align: middle; background-color: #ff8da4; padding-top: 10px; box-sizing: border-box; height: auto; width: 38px; text-align: center;"><img style="width: 26px; vertical-align: middle;" src="https://s3-us-west-2.amazonaws.com/static.seeed.cc/seeed/icon/Danger.svg" alt="attention icon" /></div>
<div class="right-desc" style="display: table-cell; vertical-align: middle; padding-left: 15px; box-sizing: border-box; width: calc(95% - 38px);">
<p style="font-weight: bold; margin-top: 10px;">Danger</p>
<p style="font-size: 14px;">•上述所有产品中均包含静电敏感元器件。人体或者测试设备中很容易产生4000V甚至更高的静电电压，保护不当可能对元器件造成损害。<br>• 尽管电路板上有静电保护电路，为避免因为高电压而造成的性能下降、功能失效甚至永久性损坏，连接设备前请务必提前做好静电预防工作，例如释放外部设备、导线或者天线自带的静电荷等。
</p>
</div>
</div>







