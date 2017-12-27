---
title: Grove - OLED Display 1.12"
category: Display
bzurl: https://www.seeedstudio.com/Grove-OLED-Display-1.12%22-p-824.html
oldwikiname: Grove_-_OLED_Display_1.12"
prodimagename: main.jpg
wikiurl: http://seeed.wiki/Grove-OLED_Display_1.12inch
sku: 104030011
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_bbg, plat_pi, plat_wio, plat_linkit
---

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/main.jpg)

当您需要一个具有 16 个灰度级的小型显示器时，我们的 Grove - OLED Display 1.12" 是您的最佳选择。1.12 英寸的 OLED 屏具有 96×96 灰度像素。由于是 OLED 显示屏，因此它没有背光并且对比度非常高。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?id=531865752955)

该显示屏基于 SSD1327 驱动芯片。您可以通过 4 线 I2C (SCL，SDA，VCC 和 GND 引脚) 与驱动芯片通信。


* 通行协议 : I2C
* 灰度显示 : 16 灰度级
* 支持正常颜色显示和反转颜色显示。
* 支持连续水平滚动
* Grove 接口




## 规格参数
---
|项目|参数|
|-----|------|
|工作电压 | 3.3/5 V|
|点矩阵 | 96x96 |
| 颜色显示| 16 灰度级 |
| OLED 显示屏 | LY120-96096 |
| 驱动芯片 | SSD1327Z |
| 点大小 | 0.15(W)mm x 0.15(H)mm |
| 点间距 | 0.75(W)mm x 0.175(H)mm|
| 工作温度 | -40~70 oC|

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)


## Platforms Supported
---


## 入门指导
---

!!!Note
    本章基于 Win10 操作系统 和 Arduino IDE 1.6.9

### 硬件连接

现在我们将通过一个简单的演示向您展示 Grove - OLED Display 1.12`` 的工作原理。首先，您需要准备下列器材:

| Seeeduino V4 | Grove - OLED Display 1.12`` | Base Shield |
|--------------|----------------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/product.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.44466619EsP2NP&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?id=531865752955)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4496443c3UfY3d&id=520233320144)|

这是一个易于使用的模块，您只需将模块连接到 Base Shield 的 I2C 端口。端口的 4 个引脚定义如下。

|引脚|功能  | 备注   | 线缆颜色 |
|--------|------|-----|---------------|
|pin1	| SCL | I2C 时钟 | 黄 |
|pin2   | SDA| I2C 数据 | 白|
|pin3   | VCC  | 电源，可选 5V/3.3V| 红 |
|pin4	| GND  | 接地 | 黑 |

**Grove - OLED Display 1.12``** 是一个 I2C 模块，本演示中，我们将它连接到 **I2C** 端口。

![](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/images/connection.jpg)

### 软件部分

- 请遵循 [如何安装 arduino 库](http://seeed.wiki/How_to_install_Arduino_Library/) 中的步骤来安装库文件。
- 我们提供了一个 Grove - OLED Display 1.12'' 的 Arduino 库，点击下面的按钮下载。
[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/library.png)](https://github.com/Seeed-Studio/OLED_Display_96X96/archive/master.zip)

- 解压并放到 Arduino IDE 的 **libraries** 文件夹中。这个库中有很多示例，包括 :

    1. OLED_Bitmap_Inverse_Display
    2. OLED_Draw_Bitmap
    3. OLED_Hello_World
    4. OLED_Inverse_Display
    5. OLED_PrintNumbers
    6. OLED_Scroll_Left
    7. OLED_Scroll_Right
    8. OLED_Z_Display_Driver_Test_Suite

- 现在，我们尝试将OLED_Hello_World上传到Seeeduino V4。 打开你的Arduino IDE，点击 **File(文件) > Example(示例) > OLED_Display_96x96-master > OLED_Hello_World**
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/example.png)

- 示例代码打开后，选择正确的控制板和 COM 端口，然后点击 **Upload（上传）** 按钮，这个过程需要几秒钟。
![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/arduino.png)

- 如果代码上传成功，您将在 OLED 上看到 hello world。
  ![enter image description here](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/images/hello_world.png)

- 请读者自己完成其他的示例，看看会发生什么。

### APIs

Seeed Gray OLED 库提供了完整的软件接口，可以使用 96x96 灰阶 OLED 实现 SSD1327Z 驱动器的功能。几乎所有有用的功能都能实现，所有的功能都在公共范围内。这使得 Seeed Gray OLED Library 具有可扩展性。Seeed Gray OLED Library 使用  Arduino Wire library。因此在初始化 Seeed Gray OLED Library 之前先初始化  Arduino Wire library。

#### init()

初始化 Seeed OLED 画面并将显示器设定为 Normal 模式。

示例:

    SeeedGrayOled.init();  //initialze SEEED Gray OLED display

#### clearDisplay()  

清除整个屏幕。应该在重新开始之前或滚动停用后使用。该功能同时也将光标设置在左上角。

示例:

    SeeedGrayOled.clearDisplay();  //clear the screen and set start position to top left corner

#### setNormalDisplay()  

将显示器配置为 颜色正常 (非反转) 模式。

示例:

    SeeedGrayOled.setNormalDisplay();//Set display to normal mode (i.e non-inverse mode)


#### setContrastLevel(unsigned char ContrastLevel)  
设置 OLED 显示器的对比度。对比度可以是 0-255 之间的任何数字。

示例:

    SeeedGrayOled.setContrastLevel(127); //Set display contrast ratio to half level( i.e 256/2 1 ).

#### setInverseDisplay()
将显示配置为颜色反转模式。

示例:

    SeeedGrayOled.setInverseDisplay();      //Set display to inverse mode

#### setHorizontalMode()  
将显示配置为水平寻址模式。

示例:

    SeeedGrayOled.setHorizontalMode();      //Set addressing mode to Horizontal Mode

#### setVerticalMode()  
将显示配置为垂直寻址模式。文本以垂直模式出现。打印文本之前，请将显示器设置为垂直模式。

示例:

    SeeedGrayOled.setVerticalMode();      //Set addressing mode to Vertical Mode

#### setTextXY(X,Y)  
将文本位置 (光标) 设置为 X 文本行，Y 文本列。96x96 OLED 被分为 12 行和 12 列的文本。这里的行和列不要与 OLED 行和列混淆。

* X 取值范围为 0 - 11。
* Y 取值范围为 0 - 11。

示例:

    SeeedGrayOled.setTextXY(0,0);  //Set the cursor to 0th Text Row, 0th Text Column

#### putChar(unsigned char c)  
从由 setTextXY(X,Y) 设置的当前地址指针开始，将字符打印到 OLED 显示器。这个函数由 putString() 在内部使用。

示例:

    SeeedGrayOled.putChar('S'); //Print the character S

#### putString(cont char *string)  

从由 setTextXY(X,Y) 设置的当前地址指针开始，将字符串打印到 OLED 显示器

示例:

    SeeedGrayOled.putString("Hello World!"); //Print the String

### putNumber(long n)  

从由 setTextXY(X,Y) 设置的当前地址指针开始，将数字打印到 OLED 显示器。 数字可以是 char，int 或 long 数据类型。

示例:

    SeeedGrayOled.putNumber(-56123); //Print number -56123

### drawBitmap(unsigned char *bitmaparray, int bytes)  

在 OLED 矩阵上显示二进制位图。数据由指向维数位图的一维数组的指针提供。位图数据在连续的行列中可用，就像水平寻址模式一样。

示例:

    SeeedGrayOled.drawBitmap(SeeedLogo,96*96/8);   //  Draw binary Bitmap (96 pixels *96 pixels  / 8) bytes

### setHorizontalScrollProperties

设置水平滚动的属性。

* 方向是 Scroll_Left 和 Scroll_Right 二者之一。
* startRow 可以是 0 - 127
* endRow 可以是 0 - 127。它应该大于 startRow
* startColumn 可以是 0 - 63
* endColumn 可以是 0 - 63。它应该大于 startRow
* scrollSpeed 可以是任何定义 : Scroll_2Frames, Scroll_3Frames, Scroll_4Frames, Scroll_5Frames, Scroll_25Frames,Scroll_64Frames, Scroll_128Frames,Scroll_256Frames.

示例:

    SeeedGrayOled.setHorizontalScrollProperties(Scroll_Left,72,95,0,47,Scroll_5Frames);  //Set the properties of Horizontal Scroll

### activateScroll()  
启用滚动。只有在设置水平滚动属性之后才能启用。

示例:

    SeeedGrayOled.activateScroll();   //Enable scrolling.

### deactivateScroll()  

禁用滚动。它应该在 activateScroll() 之后使用。

示例:

    SeeedGrayOled.activateScroll();   //Disable scrolling.

## 资源下载
---------
* **[Eagle 文件]** [Grove-OLED Display 1.12inch in Eagle](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/OLED%20Display.zip)
* **[原理图 PDF]** [Grove-OLED Display 1.12inch Sch](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/Grove%20-%2096x96%20OLED%20Display%20v2.1%20Sch.pdf)
* **[PCB 图 PDF]** [Grove-OLED Display 1.12inch PCB](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/Grove%20-%2096x96%20OLED%20Display%20v2.1%20PCB.pdf)
* **[库文件]** [Github Repository of the Library](https://github.com/Seeed-Studio/OLED_Display_96X96)
* **[芯片数据手册]** [SSD1327 Datasheet](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/SSD1327_datasheet.pdf)
*  **[芯片数据手册]** [LY120 Datasheet](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/308010007_LCD-22P-0.7.pdf)
* **[芯片数据手册]** [SH1107G_datasheet](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/SH1107G_datasheet.pdf)
* **[其他资源]** [Reference for Make a 96x96 Image](https://github.com/SeeedDocument/Grove_OLED_1.12/raw/master/resources/Make_A_96X96_Image1.zip)
