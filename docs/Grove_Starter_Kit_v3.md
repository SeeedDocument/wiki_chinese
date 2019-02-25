---
name: Grove - Starter Kit v3
category: Kit
bzurl: https://www.seeedstudio.com/Grove-Starter-Kit-V3-p-1855.html
oldwikiname: Grove - Starter Kit v3
prodimagename: Grove-Starter_Kit_v2_Photo.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Starter_Kit_v3
sku:  110060024
---

Grove是一个模块化的电子平台，可以方便快速地进行原型设计。即插即用进行组装而无需焊接或面包板。只需将 Grove 模块连接到 Grove 扩展板，并使用为每个 Grove 模块提供的示例代码。Grove Starter Kit 包含多个传感器和执行器，包括对音频，光线，运动，触觉和其他交互模式的支持。所以，您可以开始与各种各样的项目来一次思维的碰撞。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4269038b3GrhsA&id=45574420927)

##  前言

###  关于 Grove

关于 Grove 模块的更多信息请点击 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

###  Arduino 入门指导

!!!Note
    如果这是您第一次使用 Arduino/Seeeduino，请点击 [这里](http://wiki.seeedstudio.com/cn/Seeeduino_v4.2/) 查看开发板使用教程。

本套件中 **不包含 Arduino/Seeeduino** 开发板，如果您没有开发板，点击 [这里](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-14858770850.14.45ee61bb204ZOM&id=45721222112&scene=taobao_shop) 购买 Seeeduino。

点击 [这里](https://github.com/Seeed-Studio/Sketchbook_Starter_Kit_V2.0) 下载 Grove - Starter Kit Sketchbook。

##  产品清单
|零件名|数量|
|---|---|
|[Base Shield](http://wiki.seeedstudio.com/cn/Base_Shield_V2/)|1|
|[Grove - LCD RGB Backlight](http://wiki.seeedstudio.com/cn/Grove-LCD_RGB_Backlight/)|1|
|[Grove - Smart Relay](http://wiki.seeedstudio.com/cn/Grove-Relay/)|1|
|[Grove - Buzzer](http://wiki.seeedstudio.com/cn/Grove-Buzzer/)|1|
|[Grove - Sound Sensor](http://wiki.seeedstudio.com/cn/Grove-Sound_Sensor/)|1|
|[Grove - Touch Sensor](http://wiki.seeedstudio.com/cn/Grove-Touch_Sensor/)|1|
|[Grove - Rotary Angle Sensor](http://wiki.seeedstudio.com/cn/Grove-Rotary_Angle_Sensor/)|1|
|[Grove - Temperature Sensor](http://wiki.seeedstudio.com/cn/Grove-Temperature_Sensor_V1.2/)|1|
|[Grove - LED](http://wiki.seeedstudio.com/cn/Grove-Red_LED/)|1|
|[Grove - Light Sensor](http://wiki.seeedstudio.com/cn/Grove-Light_Sensor/)|1|
|[Grove – Button](http://wiki.seeedstudio.com/cn/Grove-Button/)|1|
|DIP LED Blue-Blue|1|
|DIP LED Green-Green|1|
|DIP LED Red-Red|1|
|[Mini Servo](http://wiki.seeedstudio.com/cn/Grove-Servo/)|1|
|Grove Cables|10|
|9V to Barrel Jack Adapter|1|
|Grove starter kit  Manual|1|
|Green Plastic Box|1|

###  模块详细信息

#### Grove - Base Shield

我们从 Grove - Base Shield 板开始。"Grove - Base Shield" 是 "Electronic Brick Shield" 的新版本。Base Shield 与 Seeeduino v4.2 以及 Arduino UNO 和 Duemilanove 兼容。Grove - Base Shield 上有 16 个 Grove 端口，分为 4 个功能区：模拟 (4)，数字 (7)，I2C (4) 和 UART (1)。

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Base_Shield_IO.jpg)

*   数字端口

如图所示，有七个数字端口，标记为 **D2**-**D8**。每个处理 Arduino Uno 上的一对数字引脚 : (2/3 ... 8/9)。它们可用于读取数字传感器 (例如按钮) 或控制数字 (或模拟，通过PWM) 执行器。在任何情况下，每个端口只能处理两种逻辑状态 : 0 或 1。

*   模拟端口

左边有四个 Grove 端口用于模拟读数。模拟传感器可以返回从 0 到 1023 的读数。与只返回 0 或 1 的数字传感器相比，模拟读数更加精确。

*   I2C 端口

数字端口下方有四个 I2C Grove 端口。I2C 是一种低速总线协议，通过两条线 SCL 和 SDA 传输数据。SCL 是时钟线; SDA 是数据线。

有关如何使用 Grove - Base Shield 的详细信息，请转至 [Base Shield v2](http://wiki.seeedstudio.com/cn/Base_Shield_V2/)。

####  Grove - LCD RGB Backlight

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Serial_LEC_RGB_Backlight_Lcd.jpg)

Grove - LCD RGB Backlight 是一个 16x2 的 LCD 屏幕。它能够显示两行十六个字符的文本，支持英文和日文等语言。点击 [这里](https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip) 可以找到一个自定义字符的例子。同时您能够使用简单的代码设置背光颜色。它通过 I2C 与 Arduino 通信。因此，数据交换和背光控制所需的引脚数量从 10 个减少到 2 个，为其他需求预留更多的 I/O 口。

**示例**

该示例展示了如何在屏幕上打印文本并更改背光的颜色。通过以下路径找到它 :

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_RGB_Backlight_LCD -&gt; HelloWorld**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/RGBbacklight.jpg)

有关如何使用 Grove - LCD RGB Backlight 的详细信息，请转至 [Grove - LCD RGB Backlight](http://wiki.seeedstudio.com/cn/Grove-LCD_RGB_Backlight/)。

####  Grove – Relay

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Twig-Relay.jpg)

Relay 是一个放大 Arduino 的控制能力的有用工具 ! 通过 Grove 接口输入控制信号，继电器打开或关闭连接到螺丝端子的外部电路。外部电路的电压可以达到 220V！继电器是一个电子控制的机械开关。 继电器的大小根据其承载电流的能力而变化。继电器 (主要看塑料盒部分) 越大，可承载的电流就越大。

<font color="red">
使用主电源时请务必小心。如有疑问，请联系专业人士，例如向有执照的电工寻求帮助。
</font>

**示例**

这个例子展示了如何通过一个按钮控制继电器，路径为 : **File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Relay**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Relay_Ex.jpg)

有关如何使用 Grove – Relay 的详细信息，请转至 [Grove – Relay](http://wiki.seeedstudio.com/cn/Grove-Relay/)。

####  Grove – Buzzer

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Buzzer1.jpg)

蜂鸣器是一个简单的 Grove 声音输出模块。它是压电扬声器，加上一个简单的控制电路。如果连接到数字输出，当输出为高电平时，它将发出一个音调。或者，它可以连接到一个模拟 (脉冲宽度调制数字) 输出，以产生各种音调和效果。

**示例**

您可以使用 Grove - Button 的代码使得按下按钮时，蜂鸣器发出蜂鸣声。然而，Grove – Buzzer 可以更有趣，它可以播放歌曲 ! 这是 Oomlout.com 的一个简单的例子，播放家庭童谣 - “Twinkle Twinkle Little Star (一闪一闪的小星星)”。

通过以下路径找到示例 : **File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Buzzer**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Buzzer_Ex.jpg)

压电蜂鸣器如何工作 ? 通常，每个压电蜂鸣器中有两个陶瓷晶片。当给予不同的电压时，它们相互吸引或排斥。这些晶片的移动引起空气振动 (即声音)。当振动的频率发生变化时，声音的频率会相应地改变。

有关如何使用 Grove - Buzzer 的详细信息，请转至 [Grove - Buzzer](http://wiki.seeedstudio.com/cn/Grove-Buzzer/)

####   Grove - Sound Sensor

声音传感器模块是一个简单的麦克风。基于 LM358 放大器和驻极体麦克风，驻极体麦克风收集所有频率的声音强度，可用于检测环境中的声级。

**示例**

Grove - Sound Sensor 的代码可用于控制通过亮度反映环境声音强度的 LED 灯。

通过以下路径找到示例 : **File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Sound_Sensor**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Sound_Sensor_Ex.jpg)

有关如何使用 Grove - Sound Sensor 的详细信息，请转至 [Grove - Sound Sensor](http://wiki.seeedstudio.com/cn/Grove-Sound_Sensor/)

####   Grove - Touch Sensor

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-touch_sensor_Photo.jpg)

Grove - Touch Sensor 使您可以通过在检测表面上的接触来改变按钮上的压力。当手指靠近时，它可以检测电容的变化。因此，无论您的手指是直接触摸垫还是靠近，Grove - Touch Sensor 都会输出 HIGH。

**示例**

Grove - Touch Sensor 的代码可以在这个模块中使用。通过以下路径查找示例 : **File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Touch_Sensor**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Touch_Sensor_Ex.jpg)

这是一个轻触按钮的替代方案。Grove – Touch Sensor 检测底部圆形 (未涂漆) 区域的电容变化：您的手指越靠近这个区域，电容的变化就越大。即使手指和传感器之间有纸张，它仍然可以可靠地工作。

有关如何使用 Grove - Touch Sensor 的详细信息，请转至 [Grove - Touch Sensor](http://wiki.seeedstudio.com/cn/Grove-Touch_Sensor/).

####   Grove - Rotary Angle Sensor

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Potentiometer1.jpg)

Grove potentiometer 产生 0 和 VCC 之间的模拟输出 (3.3 或 5 VDC)。角度范围为 300 度，线性变化。最大电阻值为 10k 欧，非常适合 Arduino 使用。这也可以被称为 “rotary angle sensor”。

**示例**

该示例展示如何读取 Grove - Rotary Angle Sensor 的值 :

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Rotary_Angle_Sensor**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Rotary_Angle_Sensor_Ex.jpg)

旋转式电位器看起来与旋转式编码器非常相似，但它们并不相同。旋转电位计本质上是一个以圆形构成的滑动电位计。它以模拟方式报告滑动接触时所使用的电阻元件的比例。

有关如何使用 Grove - Rotary Angle Sensor 的详细信息，请转至 [Grove - Rotary Angle Sensor](http://wiki.seeedstudio.com/cn/Grove-Rotary_Angle_Sensor/)

####   Grove – Temperature Sensor

[400px](/w/index.php?title=%E7%BC%BA%E5%9B%BE&amp;action=edit&amp;redlink=1 "%E7%BC%BA%E5%9B%BE&amp;action=edit&amp;redlink=1")

Grove - Temperature Sensor 使用一个能够检测环境温度的热敏电阻。然后电路板将模拟输入引脚测量的电压值转换为温度值。温度范围是 -40 到 125 摄氏度。

**示例**

该示例展示如何将传感器的原始输出转换为温度值。您可以在串行监视器中查看以摄氏度显示的数据 :

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Temperature_Sensor**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Temperature_Sensor_Ex.jpg)

有关如何使用 Grove – Temperature Sensor 的详细信息，请转至 [Grove - Temperature Sensor](http://wiki.seeedstudio.com/cn/Grove-Temperature_Sensor_V1.2/)

####   Grove - LED

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-LED_Photo.jpg)

Grove - LED 是为 Arduino/Seeeduino 的初学者设计的，显示端口的电平。它可以很容易地被安装到箱子或桌子的表面，用作电源或信号的指示灯。

**示例**

这个例子我们做了一个带有呼吸效果的 LED 灯 :

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_LED**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-LED_Ex.jpg)

我们为您准备了三种颜色的 LED 灯泡，您可以通过更换 Grove – LED Socket 上的 LED 来得到您期望的颜色。LED 在灯泡底部靠近方轮廓的是阴极，在灯泡底部靠近圆轮廓的是阳极。阳极需要安装到 ‘+’ 号位置，LED 才能正常工作。

有关如何使用 Grove - LED 的详细信息，请转至 [Grove - LED](http://wiki.seeedstudio.com/cn/Grove-Red_LED/)

####   Grove - Light Sensor

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Light_Sensor_photo.jpg)

光传感器也称为光敏电阻 (LDR)。通常，当环境光强度增加时，它的阻值减小。

**示例**

在这个示例中当光强度低于预设的临界值时会点亮一个 LED :

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Light_Sensor**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Light_Sensor_Ex.jpg)

传感器的模拟输出范围从 0 到 1023，但输出相对于环境光强度不是线性的。

有关如何使用 Grove - Light Sensor 的详细信息，请转至 [Grove - Light Sensor](http://wiki.seeedstudio.com/cn/Grove-Light_Sensor/)

####   Grove – Button

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Button1.jpg)

这个新版本的 Grove – Button 模块包含一个配置了下拉电阻的独立按钮，可以作为数字输入与微控制器一起使用。按钮通过 SIG 发送信号，NC 代表没有使用。

**示例**

这个示例展示如何通过按钮点亮或关熄灭一个 LED。

**File (文件) -&gt; Sketchbook (示例) -&gt; Grove_Button**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Button_Ex.jpg)

按钮的 “瞬间” 是指按下后按钮反弹，按下此按钮输出高电平，释放时输出低电平。

####  Grove -  Servo

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Servo_Photo.jpg)

这是一个位置可以精确控制的执行器。

**示例**

这个示例展示如何使用电位器来控制舵机的位置 :

**File (文件) --&gt; Sktechbook (示例) --&gt; Servo**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Grove-Starter_Kit_Servo.jpg)

##  操作示例
---
###  1. A Cup Of Flowers (花海)

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/A_Cup_of_Flower.jpg)

**说明**

想要一束花来慰藉疲惫的心吗 ? 该项目由 Grove - LED 和一个 Grove – Touch Sensor 构成。当触碰到传感器时，那些可爱的 LED 将为您带来温暖舒适的灯光效果。

**器材清单**

<dl><dd>1. Arduino x 1;
</dd><dd>2. Grove – Base Shield x 1;
</dd><dd>3. Grove – LED x 6;
</dd><dd>4. Grove – Touch Sensor x 1;
</dd><dd>5. 6 x 6cm 彩纸 x 6;
</dd><dd>6. 9V 电池 &amp; 9V 电池夹 x 1.
</dd></dl>

!!!Note
    LED 的数量是任意的。套件中有三个。但是，您可以根据花瓶的体积来增加或减少 LED 的数量。我在这里有一个大花瓶，所以我又添加了三个。

**步骤**

**1. 折花**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Fold_the_buds.jpg)

选择一个喜欢的花卉图案，并按照折叠步骤折叠一些。网上搜索可能会帮助找到折叠方法。互联网上有很多折纸爱好者和艺术家分享他们的手工艺术品。

我选择了郁金香，但向日葵，玫瑰和百合也是很不错的选择 !

折叠花蕾时，需要预留一个小孔，让 Grove 线缆通过。

**2. 组装**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Set_up.jpg)

使用 10cm Grove 线缆将 "花茎" 和 Grove – Touch Sensor 连接到 Grove – Base Shield 上。然后将代码上传到主控板。

```
<pre>void setup()
{
    pinMode(2, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(13, OUTPUT);
    pinMode(9, INPUT); //pin of touch sensor
}

void loop()
{
    int switchState = digitalRead(9);
    if(switchState == HIGH)
    {
        digitalWrite(2, HIGH);
        digitalWrite(4, HIGH);
        digitalWrite(6, HIGH);
        digitalWrite(7, HIGH);
        digitalWrite(11, HIGH);
        digitalWrite(13, HIGH);
    }
    else
    {
        digitalWrite(2, LOW);
        digitalWrite(4, LOW);
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(11, LOW);
        digitalWrite(13, LOW);
    }
    delay(100);
}</pre>
```

**3. 上电 &amp; 启动**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Battery.jpg)

使用 9V 电池供电，将花朵放置在花瓶中。大功告成 !

###   2. How You Doing! (你好吗 !)

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/How_you_doing.jpg)

(图片源自 think.bigchief.it)

**说明**

您如何向朋友问好 ? Big Cihef 会说 “当然是一起摇摆 !” 当这些纸制 Big Cihef 玩具中的一个靠在别人身上时，它们会一边摇摆一边说嗨 !

**器材清单**

<dl><dd>1. Arduini x 1;
</dd><dd>2. Grove – Base Shield x 1;
</dd><dd>3. Grove – Magnetic Switch x 1;
</dd><dd>4. Grove – Vibrator x 1;
</dd><dd>5. 纸制玩具 x 2;
</dd><dd>6. 磁铁 x 1;
</dd><dd>7. 9V 电池 &amp; 9V 电池夹 x 1.
</dd></dl>

**步骤**

**1. 打印折纸 **

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Print_it_out.jpg)

在网上选择一种您喜欢的样式。确保有足够的空间放置磁铁或电磁开关加上振动器。和上面的折纸花一样，您也可以在互联网上找到它们。

**2. 填补装饰**

剪切纸玩具时请集中注意力，只有这样才能得到一个完整干净的玩具。之后，花时间给他们填补一些装饰。 我在 Big Cihef A 的背上贴了一块磁铁 (把这个叫做代号 !)，然后用双面胶粘住。

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Stuck1.jpg)

对于 Big Chief B，我在它的背上贴了一个电磁开关，和 A 的位置相同，在脚上再粘一个振动器。

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Stuck2.jpg)

**3. 粘在一起**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Stuck3.jpg)

仔细按照印刷表格上的说明。将 Grove 线缆插入我们在 Big Chief B 上使用的两个 Grove 模块。然后，您将获得两个像上图那样的可爱纸制玩具。

**4. 上传程序**

![](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/img/Stuck4.jpg)

上传代码到您的 Arduino。它们会被你赋予生命

```
<pre>void setup()
{
    pinMode(11, INPUT);
    pinMode(9, OUTPUT);
}

void loop()
{
    int sensorState = digitalRead(11);
    if (sensorState == 1) digitalWrite(9, HIGH);
    else digitalWrite(9, LOW);
    delay(100);
}</pre>
```

##   产品特性
---
*   **标准化** – 可扩展的拼图形状，统一的 4 针连接器，螺孔网格，边缘焊盘，减少重复开发，在不同项目中重复使用以减少环境影响

*   **紧凑** – 尺寸从 2cm * 2cm，无缝组合，表面安装元件，2.0mm 节距线缆

*   **人性化** – 连接简单，防潮，各种扩展模式，开放式 DIY，库文件和演示代码

*   **以社区为基础** – 通过投票满足需求，民主化设计，项目共享，利润分享业务模式，租赁和重用

##   资源下载
---
*   **[原理图 PDF]** [Sch pdf](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Starter_Kit_v3_sch_pdf.zip)

*   **[原理图]** [Sch Eagle](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Starter_Kit_Eagle.zip)

*   **[Eagle 文件]** [Grove - Button Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Button_v1.0_Source_File.zip)

*   **[Eagle 文件]** [Grove - LED Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-LED_v1.0_Source_File.zip)

*   **[Eagle 文件]** [Grove - Buzzer Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Buzzer_v1.0_Source_File.zip)

*   **[Eagle 文件]** [Grove - Rotary Angle Sensor Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Rotary_Angle_Sensor_v1.2.zip)

*   **[Eagle 文件]** [Grove -  Relay Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Relay_v1.2_Eagle.zip)

*   **[Eagle 文件]** [Grove - Base Shield Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Base_Shield_v2.zip)

*   **[Eagle 文件]** [Grove - Sound Sensor Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Sound_Sensor_v1.3_eagle.zip)

*   **[Eagle 文件]** [Grove - Buzzer Source File](https://github.com/SeeedDocument/Grove_Starter_Kit_v3/raw/master/res/Grove-Buzzer_V1.1_eagle.zip)

##   Acknowledgement
We would like to express our gratitude to Rich Morin who modified this document with more appropriate grammar and words.
