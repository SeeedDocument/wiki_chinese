---
name: Grove - LED String Light
category: Display
bzurl: https://www.seeedstudio.com/Grove-LED-String-Light-p-2324.html
oldwikiname:  Grove - LED String Light
prodimagename: Grove-led-string-light.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-LED_String_Light
sku:  104020005
---

![](https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/img/Grove-led-string-light.jpg)

Grove - LED String Light 模块本质上是包装中包含 LED 灯串的 LED 驱动器。模块工作电压为 3.3V/5V。然而，LED 灯串要求的工作电压为 12V。 因此，该模块使用基于AIC1896的 DC-DC 升压转换器为 LED 灯条提供正常工作的电压。 LED 灯条的长度为 5 米，并具有相互等距连接的 50 个 RGB LED。您可以使用这些来打扮圣诞树，点亮你的派对或装饰你的房间。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.34.1f45065c9HDQJt&id=45574372169)

##  产品特性
---
*   与 LED 灯条结合使用

*   包括 5 米长的 LED 灯条

*   整个 5 米长度内含有相等间距的 50 个 RGB LED 可以呈现多彩的外观

*   JST 2.0 接口，用于将 LED 灯条与驱动模块连接起来

*   使用标准的 4-pin [Grove 连接线](/Grove_System/#grove-cables) 连接到其他的 [Grove](/Grove_System/) 模块

##  接口功能
---
![](https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/img/LED_String_Light.jpg)

<dl><dt>① JST 2.0接口：用于连接 LED 灯串

</dt><dt>② Grove 接口：SIG（引脚1）高电平时使 LED 串灯亮，低电平关闭
</dt></dl>

##  使用方法
---
按照以下步骤使用此模块构建示例电路：

1.  首先把 LED 灯串连接到 **Grove - LED String Light** 模块的 **JST** 2.0 双线接口。

2.  把  LED 灯串模块连接到电路的输出侧（电源模块右侧）。在电路的输入端，您可以使用一系列传感器作为输入模块，例如 [Grove - Light Sensor](/Grove-Light_Sensor/)，[Grove - Sound Sensor](/Grove-Sound_Sensor/)，[Grove - Button](/Grove-Button/) 或 [Grove - Slide Potentiometer](/Grove-Slide_Potentiometer/)。

3.  启动电路。

4.  当输入模块提供触发信号后，LED 灯串会亮起。


*   如果使用直接连接到电路输入端的光传感器，则应该看到 LED 在明亮的光线下亮起。如果您希望灯光在黑暗中亮起，请在光传感器和电源模块之间添加 [Grove - NOT](/Grove-NOT "Grove - NOT") 模块

*   如果使用声音传感器，则在检测到声音时应看到LED亮起。同样，如果要反转功能，换句话说，如果您希望始终打开灯，除非有声音，请添加 [Grove - NOT](/Grove-NOT "Grove - NOT") 模块。

*   如果使用像 [Grove - Button](/Grove-Button/) 模块那样的瞬间开关，只有按下按钮才能点亮灯串。

*   如果使用滑动电位器，将滑块从 GND 位置移动到 VCC，随着电源电压的增加，灯的亮度会增加。
</dd></dl>
</dd></dl>
</dd></dl>

以下是使用 [Grove - USB Power](/Grove-Mixer_Pack#2._USB_Power "Grove - Mixer Pack") 电源模块构建的 Grove 电路的图示：

![](https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/img/LED_String_Light_Photo.gif)

如果没有 Grove-USB Power 模块，请改用 [Grove - DC Jack Power](/Grove-DC_Jack_Power "Grove - DC Jack Power") 模块来打开 LED 灯串。

##  其他用途
---
这个 [Grove](/Grove_System/) 也可以作为 [Grove Kit Series](/Grove_System/#grove-starter-kit) 中的一个部件来使用：

*   [Grove Mixer Pack V2](/GROVE_MIXER_PACK_V2 "GROVE MIXER PACK V2")

或者，可以在 [Seeed Studio Bazaar](http://www.seeedstudio.com/depot/Grove-LED-String-Light-p-1821.html) 上单独购买。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/res/Grove-LED_String_Light.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


##  资源下载
---
*   **[原理图]**[[Schematic PDF](https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/res/Grove-LED_String_Light.pdf)]

*   **[Eagle 文件]**[[Eagle File](https://github.com/SeeedDocument/Grove-LED_String_Light/raw/master/res/Grove-LED_String_Light.zip)]
