---
title: Grove - Mini Fan
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-Mini-Fan-p-1819.html
oldwikiname:  Grove - Mini Fan
prodimagename: Mini_Fan%20head.jpg
wikiurl: http://seeed.wiki/Grove-Mini_Fan
sku:  105020004
---


**Grove - Mini Fan** 模块是基于 AVR Atmega168 微控制器的直流电机驱动器。该模块还提供了一个接口，通过它可以更改微控制器代码。 例如，可以更改代码，以便该模块可用于驱动 [伺服电机](http://en.wikipedia.org/wiki/Servomotor)。 默认情况下，该模块设置为运行包装中的直流电机。包装中的软风扇也可以连接到电机上，为孩子们做一个有趣的项目。柔软的风扇是完全安全的，即使高速转动也不会有任何伤害。

![](https://github.com/SeeedDocument/Grove-Mini_Fan/raw/master/img/Mini_Fan%20head.jpg)
[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.6fa0c0bdS8sZCK&id=546834577734)


##  产品特性
---
*   用户友好型输出模块根据从输入传感器或开关模块接收到的信号触发直流电机运行
*   与包装中附带的直流电机配合使用
*   JST 2.0 接口用于连接电机
*   直流电机带有丰富多彩的柔软风扇附件(如图所示)
*   板载微控制器可以重新编程以更改模块操作
*   微控制器运行 [Arduino](/w/index.php?title=Arduino&amp;action=edit&amp;redlink=1 "Arduino&amp;action=edit&amp;redlink=1") 兼容代码
*   更换代码以驱动伺服电机，而不是直流电机
*   使用标准 4 针 Grove 线缆连接到其他 Grove 模块
*   <span style="color: red">注意 : </span>对于最新版本（v1.1），电机的输出电压更新为 3.3 伏。

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-Mini_Fan/raw/master/img/Mini_fan.jpg)

<dl><dt>① UartSBee 接口 : 使用此界面更改微控制器代码。使用 [UartSBee](/UartSBee_V4) 模块的 Uart 接口连接到微控制器。
</dt><dt>② JST 2.0 接口 : 用于连接 3.3V 直流电机(仅 3.3V)
</dt><dt>③ Grove 接口
</dt><dt>④ ICSP 接口
</dt><dt>⑤ Atmega168 微控制器
</dt><dt>⑥ Servo 接口
</dt></dl>

##  使用方法
---
按照以下步骤使用此模块构建示例电路 :

1.首先使用 JST2.0 双线接口将直流电机连接到 **Grove - Mini Fan** 模块。

2.将迷你风扇模块连接到您的电路的输出侧 ( 电源模块右侧 )。在电路的输入端，您可以使用一系列基于传感器的输入模块 ([Grove - Light Sensor](/Grove-Light_Sensor "Grove - Light Sensor"), [Grove - Sound Sensor](/Grove-Sound_Sensor "Grove - Sound Sensor"), [Grove - Button](/Grove-Button "Grove - Button") 或 [Grove - Slide Potentiometer](/Grove-Slide_Potentiometer "Grove - Slide Potentiometer"))。

3.启动电路

4.当输入模块提供触发信号时，直流电机开始旋转:

- 如果使用像 [Grove - Button](/Grove-Button "Grove - Button") 模块那样的瞬时开关，只需按下按钮即可打开电机。

- 如果使用 [Grove - Slide Potentiometer](/Grove-Slide_Potentiometer "Grove - Slide Potentiometer")，将滑块从 GND 位置移动到 VCC，并且随着电源电压的增加可以看到电机的速度增加。 附上软风扇，您就有一个变速的个人风扇，这个风扇使得您可以在任何您想要的速度运行风扇并祛除炎魔 !

- 如果使用直接连接到电路输入侧的 [Grove - Light Sensor](/Grove-Light_Sensor "Grove - Light Sensor")，则应该看到电机在明亮的光线下运行，并在黑暗中停止 :

![](https://github.com/SeeedDocument/Grove-Mini_Fan/raw/master/img/Light_Sensitive_Fan.gif)

- 如果您希望电机仅在黑暗中运行，请在光传感器和电源模块之间添加一个 [Grove - NOT](/Grove-NOT "Grove - NOT") 模块。
- 如果使用 [Grove - Sound Sensor](/Grove-Sound_Sensor "Grove - Sound Sensor")，您应该看到电机在检测到声音时运行。再次，如果要反转功能，换句话说，如果您希望电机始终运行，除非有声音，请在声音传感器和电源模块之间添加一个 [Grove - NOT](/Grove-NOT "Grove - NOT") 模块。
</dd></dl>
</dd></dl>
</dd></dl>

您可以使用 [Grove - USB Power](/Grove-Mixer_Pack#2._USB_Power "Grove - Mixer Pack") 模块或 [Grove - DC Jack Power](/Grove-DC_Jack_Power "Grove - DC Jack Power") 模块用于 Grove 电路。

要构建使用电位器控制伺服电机的电路，请按照以下步骤进行 :

1.  通过路劲打开代码 : **\libraries\Servo\examples\Knob**。

2.  将您的代码上传到板载 MCU。确保在上传时选择正确的电路板类型和 COM 端口。

3.  现在您应该可以使用电位器来控制伺服电机。

##  可用性
---
该 [Grove](/Grove "Grove") 模块可作为以下 [Grove Kit Series](/GROVE_System#GROVE_Kit_Series "GROVE System") 的一部分使用 :

*   [Grove Mixer Pack V2](/GROVE_MIXER_PACK_V2 "GROVE MIXER PACK V2")

或者，可以在 [Seeed Studio Bazaar](http://www.seeedstudio.com/depot/Grove-Mini-Fan-p-1819.html) 单独购买。

##  资源下载
---
*   **[Eagle文件]** [Grove - Mini Fan v1.0 (Eagle Files)](https://github.com/SeeedDocument/Grove-Mini_Fan/raw/master/res/Grove-Mini_Fan_v1.0.zip)

*   **[原理图]** [Grove - Mini Fan v1.0 (pdf)](https://github.com/SeeedDocument/Grove-Mini_Fan/raw/master/res/Grove-Mini_Fan_v1.0.pdf)
