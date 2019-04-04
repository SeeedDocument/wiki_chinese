# 基于Arduino的CodecraftS使用指南
Codecraft是一款基于Scratch3.0编程软件，支持图形和文本编程语言。它是STEM教育的多功能软件工具。
通过Codecraft，孩子们可以设计引人入胜的故事，游戏和动画，并使用CH Maker Ed和Seeedstudio提供的各种电子工具包来创建交互式智能应用程序。此外，当您准备好后，那么您可以将代码块转换为Arduino，Python或JavaScript，以了解有关最流行语言的更多信息。Codecraft中有2种模式，分别是分阶段模式和设备模式。在Stage模式中，用户可以通过代码块去控制一个叫做“sprite”的对象。此外，此模式可用于帮助学生了解形状，算术以及其他数学领域。在Device模式中，用户可以简单的拖拽代码块到IDE，同时连接到 Grove Zero 或者 Arduino 去构建他们自己的项目。
## Codecraft

### device模式下的代码块

以下是Codecraft中常用的块类型。

**stack blocks**

Stack blocks为长方形状，顶部有凹槽，底部有突起，既可以接在其他积木前面，也可以接在后面。堆叠积木的典型形状如下：

![stack blocks](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/p1.png)

Stack blocks用来执行主要的命令，也是所有编程积木中数量最多的。

**reporter blocks**

每个reporter blocks都包含一个值，可以是数值也可以是字符串。以下是reporter blocks的典型形状：

![reporter blocks](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/p3.png)

报告积木可以放在任何需要数据的地方，但不能单独使用。只要有对应形状的插槽，报告积木也可以相互叠加。

**boolean blocks**

Boolean blocks包含一个条件，只能是“true”或“false”。Boolean blocks的典型形状是拉长的六边形状，如下：

![boolean blocks](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/p2.png)

Boolean blocks可以放在其他积木的对应六边形插槽中，所以也是不能单独使用的。

**C Blocks**

C Blocks也称为“换行块”，C Blocks可以在将其它代码块放入其中进行循环也可以用来检测检查其他代码块的条件是否为真。C Blocks是采用“C”形状的块，典型形状如下：

![c blocks](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/p4.png)

当然，C Blocks既可以在放在其他积木前面也可以接在其他积木后面。

**Output Boolean Blocks**

Output Boolean Blocks检查条件是“true”或者“false”，同时在不同的条件下执行一次对应的动作。Output Boolean Blocks的典型形状是拉长的六边形状，如下：

![output boolean blocks](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/p5.png)

Output Boolean Blocks可以放在Boolean Blocks和C blocks的里面。

### 基础教程

**Step 1.添加Arduino支持**

Codecraft可以支持Grove Zero和Arduino Uno/Mega，所以在使用基于Arduino的Codecraft之前，你应该在Codecraft内添加Arduino支持。


请点击[Codecraft](https://ide.chmakered.com/)，然后点击界面左边的`sidebar`点击去选择"Arduino Uno/Mega"。

![add device](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/add_device.png)

**Step 2. 安装Codecraft助手**


Codecraft Assistant能帮助你通过Codecraft将代码下载到Arduino上面，请参考[CH MAKER Ed-Documents](http://docproxy.chmakered.com/web/#/2?page_id=173) 去下载和安装它。

**Step 3. Arduino主程序**

通常，Arduino的主程序包含两个部分，他们分别叫做`setup`和`loop`。其中在`setup`里面的代码，只能在Arduino初始化的时候运行，当然在`loop`里代码可以一直运行，直到电源断电。主程序块包含在左侧的`Start`选项卡中，你可以使用鼠标将其拖动到工作区域。

![main procedure](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/main_procedure.png)

**Step 4. 闪烁LED**

我们通常通过闪烁LED来学习Arduino，并且Arduino板有一个内置的LED，它连接到Arduino的D13引脚上面。可以在Grove Digital选项卡中找到`LED`块，将其拖动到`loop`程序，它们将自动组合。将LED引脚从D2更改为D13，以便使它可以控制D13引脚中的LED，然后拖动其下方的另一个`LED`块，并将其设置为OFF。主要程序如下：

![blink led](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/blink_led.png)

为了看到LED闪烁，我们应该在LED开启和关闭之间添加`Delay ms`块。`Delay ms`块可以在`Control`选项卡中找到，它用于延时。在两个`LED`块之间拖动两个`Delay ms`块，并将间隔设置为1000ms（1000ms = 1s）。

![blink demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/blink_demo.png)

那么程序部分就完成了。

**Step 5. 上传到Arduino**

我们可以将完成的程序上传到Arduino以使其生效，因此请将您的Arduino连接到您的PC。 您可以在设备管理器中找到Arduino的串口号，记住它以备将来使用。现在单击Codecraft右下角的`Upload`，选择Arduino串口号。 确认并等待一段时间后，您会看到Arduino中的LED在闪烁。

![upload](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/upload.png)


## 适用于Arduino的Grove Start Kit

以下10节课将帮助您掌握Codecrft这款软件。这些课程中的Grove模块都可以在Grove - Arduino入门套件中找到。

### Lesson 1. 使用 Grove - LCD RGB Backlight

![Grove - LCD RGB Backlight](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_lcd.jpg)

Grove - LCD RGB Backlight支持用户自定义字符进行文本显示。它可以让你使用简单的Grove界面设置背光颜色。它使用I2C通信与Arduino通信。因此，数据交换和背光控制所需的引脚数量从10个减少到2个，从而为其他具有挑战性的任务留下了更多的I/O口。

![lcd color block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/lcd_color_block.png)

`LCD RGB setColor`块可根据R，G和B值来设置LCD的背光颜色。它可以在`Grove I2C`选项卡中找到。

![lcd print block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/lcd_print_block.png)

`LCD RGB print`块可用于将字符串打印到LCD的指定位置上，可以在`Grove I2C`选项卡中找到。

**目标** 

将Grove - LCD RGB Backlight的背光颜色改成你喜欢的颜色，同时在Grove - LCD RGB Backlight上面显示"hello, world!"。

**硬件**

**Step 1.** 使用Grove线将Grove - LCD Backlight连接到Base Shield的I2C接口上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 2.** 通过USB线将Seeedino / Arduino连接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 将`LCD RGB setColor`块和`LCD RGB print`块拖放到`setup`，具体配置如下：

![lcd_setup](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/lcd_setup.png)

**Step 3.**拖拽另一个`LCD RGB print`块到`loop`，让其显示运行时间，具体配置如下：

![lcd_demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/lcd_demo.png)

!!!成功
    当代码完成上传后，您可以看到Grove - LCD RGB Backlight的背光颜色变成你自己设置的颜色，并且在LED的第一行显示“hello,world” ，第二行显示系统的运行时间。

### Lesson 2. 使用 Grove - Relay

![Grove - Relay](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_relay.jpg)

Relay是放大Arduino控制能力的有用工具！通过Grove接口输入控制信号，Relay打开或关闭连接到螺丝端子的外部电路。外部电路的电压最高可达220V！利用这个Relay，开始一些非常艰难的项目吧！

![relay block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/relay_block.png)

`Relay block`可以被用来控制Relay的开关状态，我们可以在`Grove Digital`选项卡中找到它。

**目标**

使用Grove - Button去控制一个Grove - Relay，当Grove - Button被按下，打开Grove - Relay，反之亦反。

**硬件**

![relay demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/relay_demo.jpg)

**Step 1.** 使用两根Grove电缆将Grove - Button连接到Base Shield的端口D3上，将Grove - Relay连接到Base Shield的端口D8上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 创建一个变量来存储按钮的状态,转到`Variables`选项卡，单击`Make a Variable`按钮，然后命名我们将创建的变量，如buttonState。

![create variable](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/create_variable.png)

点击OK，`buttonState`将出现在`Variables`选项卡中。

**Step 3.** 拖动`set 我的变量 to 0`块到`loop`，配置如下图所示：

![button variable](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/relay_buttonState.png)


**Step 4.** 我们需要在按下Grove - Button时打开Grove - Relay，否则关闭它。 所以我们需要在`Control`选项卡中的`if ... then ... else`块和`Operator`选项卡中的`Equal`块，将它们拖动到`loop`，然后让它们与`buttonState`变量结合使用,配置如下图所示：

![relay if](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/relay_if.png)

**Step 5.** 最后将`Relay block`拖动到`loop`，然后上传到Arduino。具体配置如下图所示：
![relay demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/relay_demo.png)

!!!成功
    当代码成功下载到arduino上面，如果你按下Grove - Button，Grove - Relay将被打开，反之亦反。
### Lesson 3. 使用 Grove - Sound Sensor

![Grove - Sound Sensor](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_sound.jpg)

Grove - Sound sensor 是一个基于LM358运放的简单麦克风，它可以用来探测环境中的声音等级。

![sound block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/sound_block.png)

`Sound block`可以用来探测环境中声音的大小,它可以在`Analog`选项卡中找到。

**目标**

监控环境中的声级。 如果声音太大，则将LED闪烁作为警报。

**硬件**

![sound demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/sound_demo.jpg)

**Step 1.** 使用两根Grove电缆将Grove - Sound Sensor连接到Base Shield的端口A0上，将Grove - Red LED连接到Base Shield的端口D7上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 请参考“使用Grove - Relay”部分创建一个变量来存储声音的大小，然后在`control`选项卡中使用`if ... then`块确定声音大小是否超过阈值，配置如下。

![sound loop](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/sound_loop.png)

**Step 3.** 如果声音的大小超过了阈值，LED闪烁，配置如下：

![sound demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/sound_demo.png)

!!!成功
    当代码上传成功, 如果环境中的声音太大，LED会闪烁。
### Lesson 4. 使用 Grove - Touch Sensor

![Grove - Touch Sensor](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_touch.jpg)

Grove - Touch Sensor使您可以检测表面上的接触来替换按钮上的压力。当手指在附近时，它可以检测到电容的变化。因此，无论您的手指是直接接触焊盘还是仅靠近焊盘，Grove - Touch Sensor都会输出HIGH。

![touch block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/touch_block.png)

`Touch`块可以用来读取Grove - Touch Sensor的状态, 它可以在`Digital`选项卡中找到.

**目标**

使用Grove - Touch Sensor去控制Grove - Red LED. 当Grove - Touch Sensor被触摸Grove - Red LED打开, 反之亦反。

**硬件**

**Step 1.** 使用 使用两根Grove电缆将Grove - Touch Sensor连接到Base Shield的端口D3上，将Grove - Red LED连接到Base Shield的端口D7上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 具体操作可以参考`使用Grove - Relay`部分，唯一的差别就是变量不同，具体配置如下：

![touch demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/touch_demo.png)

!!!成功
    当代码上传成功, 使用Grove - Touch Sensor去控制Grove - Red LED. 当Grove - Touch Sensor被触摸Grove - Red LED打开, 反之亦反。

### Lesson 5. 使用 Grove - Rotary Angle Sensor

![Grove - Rotary Angle Sensor](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_rotary.jpg)

Grove - Rotary Angle Sensor可在0和VCC（3.3或5 VDC）之间产生模拟输出。角度范围为300度，值线性变化。电阻值为10k欧姆，非常适合Arduino使用。这也可称为“旋转角度传感器”。

![rotary block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/rotary_block.png)

`Rotation`块可以读取Grove - Rotary Angle Sensor的数值, 它可以在`Analog`选项卡中找到。

**目标**

通过串口打印出Grove - Rotary Angle Sensor的数值。

**硬件**

![rotary demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/rotary_demo.jpg)

**Step 1.** 使用Grove线缆将Grove - Rotary Angle Sensor连接到Base Shield的A0端口上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 在使用`Serial port`之前我们应设置其波特率，将`Serial baud rate`块从`Serial port`选项卡拖到`setup`，然后选择9600 bps。

![rotary setup](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/rotary_setup.png)

**Step 3.** `serial println`块可用于在串口中显示新行，我们可以将它与Grove - Rotary Angle Sensor块结合使用，具体配置如下：

![rotary demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/rotary_demo.png)

**Step 4.** 上传程序后，单击Codecraft左侧的`Connect`按钮，选择Arduino的端口，然后选择`Connect`。
![connect serial](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/connect_serial.png)


!!!成功
    你能在串口显示窗口中看到Grove - Rotary Angle Sensor输出的数据。

![serial monitor](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/serial_monitor.png)

### Lesson 6. 使用 Grove - LED

![Grove - LED](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_led.jpg)

Grove - LED专为Arduino / Seeeduino的初学者设计，用于监控数字端口的控制。它可以很容易地安装在您的盒子或桌子的表面，并用作电源或信号的指示灯。

![led block digital](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_block_digital.png)

![led block analog](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_block_analog.png)

`LED`块可用作数字输出或模拟输出，当作为模拟输出时，您可以控制其亮度。

**目标**

制作呼吸灯。

**硬件**

![led demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_demo.jpg)

**Step 1.** 使用Grove线缆将Grove - LED连接到Base Shield的D3端口上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 
通过使用`Analog`选项卡中的`LED`块，可以非常简单地进行Grove - LED呼吸。除此之外，我们还需要在`Control`选项卡中`count with...from...to...step`块来计算Grove - LED的亮度。拖动它与`loop`结合,具体配置如下：

![led count](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_count.png)

**Step 3.** 确保将变量i从0（黑暗）变为255（最亮），然后将`LED`块和`Delay ms`块添加到其中，并将LED的亮度变为i,具体配置如下：

![led loop](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_loop.png)

**Step 4.** 上面的程序使Grove - LED从最暗到最亮，现在我们可以添加程序让它从最亮到最暗。

![led demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/led_demo.png)

!!!成功
    当代码上传成功, 你将看到LED呼吸。

### Lesson 8. 使用Grove - Light Sensor

![Grove - Light Sensor](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_light.jpg)

Grove - Light Sensor，也称为光敏电阻（LDR）。通常，当环境光强度增加时，Grove - Light Sensor的电阻将减小。

![light block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/light_block.png)

`Light`块可通过模拟输入来检测环境中的光强度, 它可以在`Analog`选项卡中找到。

**目标**

建立智能光照系统，当光强度低于预设阈值时，打开Grove - Red LED。

**硬件**

![light demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/light_demo.jpg)

**Step 1.** 使用两根Grove电缆将Grove - Red LED连接到Base Shield的端口D7上，将Grove - Light Sensor连接到Base Shield的端口A0上。

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 
            指南我们可以参考“使用Grove - Touch Sensor”部分，下图是详细的配置：
![lighe demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/light_demo.png)

!!!成功
    当代码上传成功，挡住Grove - Light Sensor的光线，Grove - Red LED点亮。

### Lesson 9. 使用 Grove - Button

![Grove - Button](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_button.jpg)

这个新版本的Grove - Button包含一个独立按钮，配有下拉电阻可以与我们的微控制器一起用作数字输入。其中NC引脚是不是使用的意思。

![button block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/button_block.png)

`Button` 块可用于通过数字输入检测Grove - Button的状态, 它可以在`Digital`选项卡中找到。

**目标**

使用Grove - Button控制Grove - Red LED。按下按钮时，打开Grove - Red LED，反之则反。

**硬件**

![button demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/button_demo.jpg)

**Step 1.** 使用两根Grove电缆将Grove - Button连接到Base Shield的端口D3上，将Grove - Red LED连接到Base Shield的端口D7上

**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.** 我们参考“使用Button - Relay部分”，现在让我们将Grove - Relay更改为Grove - Red LED，然后使用Grove - Button来控制它，具体配置如下:

![button demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/button_demo.png)

!!!成功
    如果Grove - Button被按下，则打开Grove - Red LED，反之则反。

### Lesson 10. 使用 Grove - Servo

![Grove - Servo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/grove_servo.png)

Grove - Servo是一个可以精确控制位置的执行器。

![servo block](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/servo_block.png)

`Servo`块可以通过分配旋转量和每次旋转之间的延迟来控制伺服, 它可以在`Analog`选项卡中找到。

**目标**

使用Grove - Rotary Angle Sensor去控制Grove - Servo。

**硬件**

![servo demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/servo_demo.jpg)

**Step 1.** 使用两根Grove电缆将Grove - Servo连接到Base Shield的端口D3上，将Grove - Rotary Angle Sensor连接到Base Shield的端口A0上。
**Step 2.** 将Base Shield插入Seeeduino / Arduino。

**Step 3.** 通过USB线将Seeeduino / Arduino链接到您的PC。

**软件**

**Step 1.** 打开[Codecraft](https://ide.chmakered.com/)，添加Arduino支持，然后将主程序块拖到工作区。

**Step 2.**我们可以使用Grove - Rotary Angle Sensor来控制Grove - Servo，但由于“旋转”块的值是0到1023，所以我们需要除以一个数字，让它在0到180之间,具体配置如下。
![servo demo](https://github.com/SeeedDocument/Guide_for_Codecraft_using_Arduino/raw/master/img/servo_demo.png)

!!!成功
    当代码上传成功,旋转Grove - Rotary Angle Sensor，Grove - Servo将会做出相应的动作。
