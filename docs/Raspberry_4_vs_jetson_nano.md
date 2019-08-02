# Raspberry Pi 4 vs NVIDIA Jetson Nano Developer Kit

文章转载至https://buildazure.com，由Chris Pietschmann于2019年6月24日发表；
文章链接：https://buildazure.com/2019/06/24/raspberry-pi-4-vs-nvidia-jetson-nano-developer-kit/

有大量的物联网设备可用于原型设计和物联网（IoT）解决方案。Raspberry Pi 4最近发布，在最新版本的Raspberry Pi中进行了一些非常棒的功能升级。相比之下，NVIDIA Jetson Nano Developer Kit也提供了一个提供类似功能集的电路板。初步比较后，它们的基本功能类似，但Nano在主板上增加了专用的GPU。让我们比较两块开发板，看看到底存在哪些差异。

## Raspberry Pi 4

Raspberry Pi是一款非常棒的小型计算机和物联网开发板。虽然它不是一个低功耗的物联网设备，但是它是一个很好的原型设计工具，甚至可以用于构建物联网网关设备。Raspberry Pi有很多很棒的功能，最近发布了Raspberry Pi 4，针对之前的版本进行了一些非常棒的升级。

与之前的Raspberry Pi 3 B +相比，Raspberry Pi 4 B包含以下升级：

* 更快的处理器 - CPU已升级为四核Cortex-A72（ARM v8）64位SoC @ 1.5 Ghz
* 更多内存 - LPDDR4-2400 SDRAM提供1 GB，2 GB或4 GB RAM选项的多种型号
* 双4K视频 - 现在有2个微型HDMI端口，都可以输出4K视频;甚至可以利用双显示器进行显示
* 2个USB3和2个USB2端口 - 现在不仅仅是4个USB2端口，现在有2个可以更高速地连接到外围设备USB3端口和2个USB2端口。
* USB-C电源 - 电路板的电源连接器已从micro-USB更改为USB-C连接器
* I / O - [40引脚GPIO接头](https://buildazure.com/2018/08/08/raspberry-pi-gpio-pin-reference/)（支持I2C，SPI和UART）

这些是最新版的Raspberry Pi 4和老版的 Raspberry Pi 3主要的不同。因此，新的Raspberry Pi 4与以前版本的主板相比，具有更高的处理能力，以及其他优势。

## NVIDIA Jetson Nano

NVIDIA发布了一些不同的物联网开发板。NVIDIA Jetson Nano是他们发布的最新的开发板。该板可作为开发人员工具包提供，其中包含将其用于原型设计物联网解决方案所需的所有输入和连接。
以下是NVIDIA Jetson Nano Developer Kit的一些关键特征：

* CPU  - 四核ARM Cortex-A57 MPCore处理器
* GPU  -  NVIDIA Maxwell w / 128 NVIDIA CUDA核心
* 内存 -  4 GB 64位LPDDR4
* 显示 -  HDMI和DisplayPort输出
* USB -  4个USB 3端口
* I / O  -  I2C，SPI，UART和Raspberry Pi兼容的GPIO接头

NVIDIA Jetson Nano Developer Kit提供完整的计算（集成GPU），可用于原型物联网解决方案。

## 规格比较

从上面两个板的初始规格列表中​​可以看出，肯定存在一些相似性。我们制作出一张表格来详细展示它们直接的差异：

|              | Raspberry Pi 4                            | NVIDIA Jetson Nano                              |
|--------------|-------------------------------------------|-------------------------------------------------|
| CPU          | Quad-core ARM Cortex-A72 64-bit @ 1.5 Ghz | Quad-Core ARM Cortex-A57 64-bit @ 1.42 Ghz      |
| GPU          | Broadcom VideoCore VI (32-bit)            | NVIDIA Maxwell w/ 128 CUDA cores @ 921 Mhz      |
| Memory       | 4 GB LPDDR4**                             | 4 GB LPDDR4                                     |
| Networking   | Gigabit Ethernet / Wifi 802.11ac          | Gigabit Ethernet / M.2 Key E (for Wifi support) |
| Display      | 2x micro-HDMI (up to 4Kp60)               | HDMI 2.0 and eDP 1.4                            |
| USB          | 2x USB 3.0, 2x USB 2.0                    | 4x USB 3.0, USB 2.0 Micro-B                     |
| Other        | 40-pin GPIO                               | 40-pin GPIO                                     |
| Video Encode | H264(1080p30)                             | H.264/H.265 (4Kp30)                             |
| Video Decode | H.265(4Kp60), H.264(1080p60)              | H.264/H.265 (4Kp60, 2x 4Kp30)                   |
| Camera       | MIPI CSI port                             | MIPI CSI port                                   |
| Storage      | Micro-SD                                  | Micro-SD                                        |
|              | [购买](https://item.taobao.com/item.htm?spm=a2oq0.12575281.0.0.46251deb4zsXaZ&ft=t&id=597106720116&qq-pf-to=pcqq.c2c)| [购买](https://item.taobao.com/item.htm?spm=a2oq0.12575281.0.0.46251deb4zsXaZ&ft=t&id=589438093531)|

** Raspberry Pi 4有不同型号，配备1 GB，2 GB或4 GB RAM。

如您所见，Raspberry Pi 4和NVIDIA Jetson Nano的主要功能非常相似。请记住，未列出一些差异，因为这不是每个开发板功能的完整列表。但是，大多数功能都相同或相似，只有一个除外。


两者都是使用ARM处理器构建的完整计算机，4 GB RAM，以及一系列外围设备连接。两者之间最大的区别在于NVIDIA Jetson Nano包含性能更高，功能更强大的GPU（图形处理器），而Raspberry Pi 4则具有低功耗的VideoCore多媒体处理器。虽然NVIDIA Jetson Nano的价格较高，但要获得Maxwell GPU的价格肯定要付出代价。

请注意：NVIDIA Jetson Nano中具有128个CUDA核心的NVIDIA Maxwell GPU实际上与Nintendo Switch游戏机中的GPU相同。Nintendo Switch也是Cortex-A57 CPU。NVIDIA Jetson Nano CPU和GPU硬件类似于Nintendo Switch；
除了Nintendo Switch在其NVIDIA Tegra X1 SoC（片上系统）硬件上还有四个Cortex-A53内核。这无疑增加了对NVIDIA Jetson Nano硬件可行性的更多看法。
![Raspberry Pi 4 vs NVIDIA Jetson Nano Developer Kit 2](https://i0.wp.com/upload.wikimedia.org/wikipedia/commons/thumb/8/88/Nintendo-Switch-wJoyCons-BlRd-Standing-FL.jpg/220px-Nintendo-Switch-wJoyCons-BlRd-Standing-FL.jpg?w=900&ssl=1 "Raspberry Pi 4 vs NVIDIA Jetson Nano Developer Kit 2")

## Cortex-A57 vs Cortex-A72 CPU

Raspberry Pi 4和NVIDIA Jetson Nano都使用ARM CPU（处理器）。Raspberry Pi 4实际上有一个较新的ARM Cortex-A72 CPU;而不是NVIDIA Jetson Nano中稍微老一点的ARM Cortex-A57。然而，NVIDIA Jetson Nano中的A57仍然是比较老的Raspberry Pi 3中使用的A53更新的CPU。
让我们来看看两个CPU的异同：

|                       | Cortex-A72                                                            | Cortex-A57                                                            |
|-----------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Board used            | Raspberry Pi 4                                                        | NVIDIA Jetson Nano                                                    |
| Microarchitecture     | ARMv8-A 64-bit                                                        | ARMv8-A 64-bit                                                        |
| Cores                 | 4                                                                     | 4                                                                     |
| Clock speed           | 1.5 Ghz                                                               | 1.42 Ghz                                                              |
| Manufacturing process | 28 nm                                                                 | 20 nm                                                                 |
| L1 cache              | 80 KiB (48 KiB I-cache with parity, 32 KiB D-cache with ECC) per core | 80 KiB (48 KiB I-cache with parity, 32 KiB D-cache with ECC) per core |
| L2 cache              | 512 KiB to 4 MiB                                                      | 512 KiB to 2 MiB                                                      |
| L3 cache              | None                                                                  | None                                                                  |
| Year CPU Released     | 2015                                                                  | 2013                                                                  |

从表面上看，两个CPU看起来几乎完全相同。事实上他们真的很相似。Raspberry Pi 4中的Cortex-A72仅比NVIDIA Jetson Nano中的Cortex-A57新一代。较新的A72具有稍高的时钟速度，只是制作芯片时，使用的功率比A57低20％或性能提高90％。

在性能方面，值得注意的是Raspberry Pi声称Raspberry Pi 4 Cortex-A72比Raspberry Pi 3 B + Cortex-A53处理器快约50％。由于NVIDIA Jetson Nano使用的Cortex-A57位于Raspberry Pi两代CPU之间，因此Raspberry Pi 4和NVIDIA Jetson Nano之间的性能差异可能不大。

与NVIDIA Jetson Nano中的Cortex-A57相比，Raspberry Pi 4中较新的Cortex-A72 CPU似乎表明CPU处理能力更强。
这可能意味着Raspberry Pi 4更适合用作通用计算机或低成本的迷你桌面替代品。然而，NVIDIA Jetson Nano中更强大的GPU为图形工作甚至人工智能（AI）和机器学习（ML）使用提供了更强大的功能。

## 结论

显然，硬件规格，当然还有价格，只是初始区域，有助于确定哪种板最适合您的需求。操作系统和软件功能肯定也会对此产生影响。这两个板都运行Linux并具有几乎相同的功能。因此，如果一切都相同，那么对电路板的编程和SDK支持也会对决策产生影响。但是，如果您需要构建人工智能（AI）和机器学习（ML）项目，那么拥有完整GPU的NVIDIA Jetson Nano可能会被选中。

您希望购买这两块板中的哪一块？或者，你已经购买了一个？请发表评论，让我们知道您的想法！
