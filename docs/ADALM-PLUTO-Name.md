# 为什么叫做“Pluto”
在地理学中，天体“[冥王星](https://en.wikipedia.org/wiki/Pluto)”（Pluto）是一颗[矮行星](https://en.wikipedia.org/wiki/Dwarf_planet)，它类似于一颗小行星，但缺乏将其归类于此的技术准则。PlutoSDR是一个主动学习模块，类似于[软件定义无线电](https://en.wikipedia.org/wiki/Software-defined_radio)，但在我们看来，它同样缺乏相应的性能表现或技术准则来将其归类于此。

PlutoSDR可以作为打开通信或SDR课程大门的一把钥匙，但它不能替代现有的更加专业的SDR（[例如](https://en.wikipedia.org/wiki/List_of_software-defined_radios)）。PlutoSDR针对学生而设计，价格也更加低廉1[^1]。因此，所有PlutoSDR的用户都应注意它在很多方面的局限性，确保正常的工作和使用。


## 系统相关


## 温度范围 
测试中设备的温度范围在10℃ 到40℃ 之间，在一般教室环境中可以正常使用，但是在极端温度条件的一些商业环境中，设备可能会损坏，这已超出了设计和质量保证的范围。PlutoSDR 内的设备工作温度范围通常指定在 0°C 至 70°C 或 +40°C 至 +85°C之间。  
为避免出现此类情况，请务必确实设备处于合适的温度范围内。


## 相关参数
### USB2.0
[USB2.0](https://en.wikipedia.org/wiki/USB#USB_2.0) 是480 Mbit/s半双工串行协议。

* 利用率为100%时，480兆比特每秒等于60兆字节每秒。

* USB开发者论坛主席指出，“由于存储卡和外设之间的通讯协议开销，宣称最高速度为60MB/s的高速USB中，至少10-15%达不到峰值。”从而导致速度降为约50MB/s。[^2]

* USB有控制传输、中断传输、同步传输和批量传输4种传输模式。当我们使用批量传输时，不可能关闭其他模式，资源会有10%的损耗，因此速度又降至约45MB/s。

* 半双工传输时，发送和接收分别占有约22.5MB/s。

* 单个样本长度为2 byte（12 bit），采样速率就为11MSPS。

实际上在PlutoSDR中采样速率接近7.5 - 12.5 MSPS，但它取决于USB host以及当前的网络状况。实际速率大约是理论速率的65%-100%，说明速率虽然主要取决于主机，但还是有优化空间的。相比现有的商业用的传输速率几个G的以太网、USB 3.0（5 Gbps 全双工）或者PCIe（4 Gbps每通道）解决方案，USB 2.0还是要慢得多。


### FPGA 规格
PlutoSDR内的FPGA（作为Xilinx Zynq 7010的一部分）尺寸很小


属性|尺寸
---|---
逻辑单元|28
块存储器|2.1
DSP组成单元|80


使用部分FPGA的默认设计目标为：
- CMOS接口实现
- I/Q转换（如果用户需要）
- DDS（用于传输端的multi-tone发生器），以及
- 添加8个插值/抽取，使 PlutoSDR 的采样率比 AD9363（520.833kSPS）的最小采样率低8倍（65.104166 kSPS）[^3]

以下的利用率报告是一种比较典型的情况。如果您不需要上述的某些逻辑电路，可以将其关闭并重新利用FPGA作为自定义逻辑电路。

额外的抽取和插值滤波器使用 20 个 DSP slice（总共 40 个）。可选的 DDS 使用 20 个 DSP slice，可选的 2 x 2 矩阵乘法（有时用于 IQ 校正或相位旋转）是每个通道 2 个，DC 滤波器是每个通道 1 个。

使用不同的[Zynq](http://www.xilinx.com//support/documentation/selection-guides/zynq-7000-product-selection-guide.pdf)设备可以很轻易地克服该问题——我们在最小的引脚计数选择了一个设备，这有利于在价格较低时使布局更合理。使用更大的设备和封装，将影响大小和成本。

## RF问题
### 振荡器
PlutoSDR 上的振荡器是特定版本的 Rakon RXO3225M 40.000 MHz （[509336](http://ez.analog.com/servlet/JiveServlet/download/166568-1-29693/Rakon%2520RXO3225M%252040.000%2520MHz%2520(509336)%2520v1.01.pdf)），满足 AD936x 系列的抖动要求。然而，它的频率稳定在±25 ppm（电压、温度、漂移加上初始精度）。

您可能会认为这非常不好，但：
* 它可以通过对XO频率编程进行数字校正。如果您注意到频率为39.987654 MHz（下至 Hz 分辨率），您可以告诉系统，系统将作出反应以更新LO 频率和采样率。通过监视此频率偏移，可以实现动态更新。
* 因为远程发射器不太可能与本地设备相同，大多数接收器都有频率补偿校正算法——您只需确保您的补偿算法能够应对大量问题。
* 作为您自己的发射器和接收器的回路——- 频率和采样率的偏移量在单个设备的两个通道上都是相同的。应该注意 - Tx 和 Rx L 之间仍有随机相位偏移，但它们的频率应该完全相同。

使用一个不同的振荡器可以解决该问题，但可能影响成本。
### 可调范围
我们发现PlutoSDR内的[AD9363](http://www.analog.com/AD9363)的可调范围由325至3800 MHz之间的LO中心频率指定。这个可调范围已经诞生了十多年，覆盖了[美国](https://www.ntia.doc.gov/files/ntia/publications/january_2016_spectrum_wall_chart.pdf)，[欧洲](http://www.erodocdb.dk/docs/doc98/official/pdf/ERCRep025.pdf)，[澳大利亚](http://www.acma.gov.au/webwr/radcomm/frequency_planning/spectrum_plan/aust_rf_spectrum_plan.doc)，[印度](http://www.wpc.dot.gov.in/DocFiles/Book.pdf)，[日本](http://www.tele.soumu.go.jp/e/adm/freq/search/share/plan.htm)等地的频段，但它范围没有[AD9361](http://www.analog.com/AD9361)或[AD9364](http://www.analog.com/AD9364)这类的板子大，这些板子可调范围在70至6000兆赫之间，几乎是它的两倍。

因为器件的引脚几乎相同，通过将AD9363换成AD9364或AD9361，很容易克服这一缺点，但这会增加成本。
### RF屏蔽
PlutoSDR内部没有RF屏蔽模块，这意味着在它附近放置一个强大的发射机（如您的手机）可能会影响PlutoSDR调谐到的频率结果。
通过增加RF屏蔽装置可以克服这一缺点，但会增加成本和体积。
### RF滤波
PlutoSDR 上没有预选或输出滤波器，AD9363的输出是SMA连接器的输出，AD9363的引脚提供的输入进入设备天线。

AD9363 中的射频发射机输出 LO 频率的中度三次谐波。如果您的 LO 为 3 GHz（其中三次谐波为 9 GHz，超出 PlutoSDR 中用于差分到单端转换的balun范围），则该频率将相当低。但是， 如果 LO 为 500 MHz，则第三次谐波将为 1500 MHz，完全在范围内。如果您在 500 MHz 下传输 RF 信号，信号会以 1500 MHz 进行传播。

通过添加特定的预选或输出筛选器，可以轻松克服这一问题。某些您需要的调谐范围可能会使事情变得相当复杂，但这还取决于您使用的天线类型。（天线也是滤波器）
### RF性能
虽然[AD9363](http://www.analog.com/AD9363)的RF性能足以满足许多RF应用，但它与可能其他高性能器件的规格不匹配，如其他商用SDR器件中的[AD9361](http://www.analog.com/AD9361)、[AD9364](http://www.analog.com/AD9364)、[AD9371](http://www.analog.com/AD9371)。

PlutoSDR性能要优于其他许多同类设备，但它不是最好的SDR。

我们做过许多额外的测试，因此在很多应用中不会存在这种问题。

[^1]: 价格比一本好的教材低

[^2]: [USB#Transmission_rates](https://en.wikipedia.org/wiki/USB#Transmission_rates)

[^3]: AD9363 ADC最小采样率为25 MSPS，最大抽取因子为48，25 MSPS÷48等于520833.33 SPS