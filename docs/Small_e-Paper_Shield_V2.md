---
title: Small e-Paper Shield V2
category: Shield
bzurl: https://www.seeedstudio.com/Small-e-paper-Shield-V2-p-2462.html
oldwikiname:  Small e-Paper Shield V2
prodimagename:  Small_e-Paper_shield_b.jpg
wikiurl: http://seeed.wiki/Small_e-Paper_Shield_V2
sku:   104030019
---
 ![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Small_e-Paper_shield_b.jpg)

电子墨水屏也称为电子纸屏幕，它可能是最舒适的阅读材料，因为它反射光而不是发光，阅读感受自然舒适。由于电子墨水屏自己不发光，这样消耗了的电力就很少。Small e-Paper Shield 是小尺寸电子墨水屏的驱动器。 它能够驱动 1.44 英寸，2.0 英寸和 2.7 英寸的电子墨水屏，并支持 170 多种语言。这个驱动器的上表面很平坦，为贴在其上的电子墨水屏提供很好的支持。如果你正在考虑使用一个轻巧舒适的阅读显示器，电子墨水屏将是一个不错的选择。

**注意：** 由于此驱动板支持不同大小的电子纸。电子墨水屏不包含在本产品中。我们同时出售 2.0 英寸和 2.7 英寸的电子纸，您可以选择合适的型号购买。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.7fefca823hoAlv&id=45535333379)

###  选择库函数

您需要先知到您的电子墨水屏的版本，然后选择合适的库文件。屏幕型号在屏幕背面的标签上，为下图的“(2~11)Model Name”。

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Definition_of_Model_Labels.jpg)

**注意您显示屏的型号：**

*   如果型号是 'EG020AS012' 或 'EM027AS011'，那您需要选择老的库函数，点击这里 [Small e-Paper Library](https://github.com/Seeed-Studio/Small_ePaper_Shield) 下载。

*   如果型号是 'EG020BS011' 或 'EM027BS013'，那您需要选择新的库函数，点击这里 [New Panel Library【EPD_V230】](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/EpdV230.rar) 下载。

##  规格参数
---
兼容开发板: Arduino Uno/Leonardo/Arduino Mega/Linkit ONE

工作电压：3.3/5VDC

工作电流（刷新屏幕）：40mA

接口类型：SPI

<font color="Green">与 Arduino 连接的引脚</font>

<table >
<tr>
<th> Arduino
</th>
<th> E-paper
</th></tr>
<tr>
<td width="150px"> D2
</td>
<td width="250px"> M_EPD_PANEL_ON﻿
</td></tr>
<tr>
<td> D3
</td>
<td> M_EPD_BORDER﻿
</td></tr>
<tr>
<td> D4
</td>
<td> M_/SD_CS﻿
</td></tr>
<tr>
<td> D5
</td>
<td> M_EPD_PWM﻿
</td></tr>
<tr>
<td> D6
</td>
<td> M_EPD_/RESET﻿
</td></tr>
<tr>
<td> D7
</td>
<td> M_EPD_BUSY﻿
</td></tr>
<tr>
<td> D8
</td>
<td> M_EPD_DISCHARGE﻿
</td></tr>
<tr>
<td> D9
</td>
<td> M_/WORD_STOCK_CS﻿
</td></tr>
<tr>
<td> D10
</td>
<td> M_/EPD_CS﻿
</td></tr>
<tr>
<td> ICSP PORT
</td>
<td> M_MOSI , M_SCK , M_MISO﻿
</td></tr>
<tr>
<td> A0
</td>
<td> M_TEMP_SEN﻿
</td></tr>
<tr>
<td> A1
</td>
<td> M_OE123﻿﻿
</td></tr>
<tr>
<td> A2
</td>
<td> M_CKV﻿
</td></tr>
<tr>
<td> A3
</td>
<td> M_STV_IN﻿
</td></tr>
<tr>
<td> 3.3V
</td>
<td> M_VCC_3V3﻿
</td></tr>
<tr>
<td> 5V
</td>
<td> M_VCC_5V
</td></tr></table>

##  操作示例
---
小型电子墨水屏可以显示图像，各种图形和文字。库函数里有很多例程可供您参考。

###  硬件连接

*   将电子墨水屏连接到 Small e-Paper Shield 的 FFC 接口。
*   将 Small e-Paper Shield 插入 Arduino / Seeeduino，并使用 USB 电缆将其连接到电脑。

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/E-Paper_Screen.jpg)

点击 [这里](https://github.com/Seeed-Studio/ePaper) 下载示例代码。下载完成后把文件添加到 Arduino IDE 的库中。

###  演示

这里我们以 2.0 英寸的屏幕为例来展示它的显示功能。

####  示例 1：显示文字

*   打开代码 **File（文件）- &gt;Examples（示例）- &gt;ePaper-&gt;text** 如下所示：

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Text_Code.jpg)

<dl><dd><font color="red">在使用时需要注意：</font>
</dd></dl>
<dl><dd>如果您使用 Arduino UNO，Seeeduino 3.0 以及任何使用 Atmega328P 或 Atmega32U4 作为控制器的主板，则应插入SD卡。 由于 Atmega328p 和 Atmega32U4 的存储空间很小，因此 SD 卡用于存储临时数据。
</dd><dd>如果您使用 Arduino Mega 或其他使用 Atmega1280 或 Atmega2560 的主板，则无需插入 SD 卡。
</dd></dl>

*   更改参数以匹配您的屏幕大小。如果您的屏幕是 2.7 英寸，则需要更改 200 到 270。使用其他型号屏幕的更改方法类似。
<pre>#define SCREEN_SIZE 200 // choose screen size: 144, 200, 270</pre>

*   上传代码到开发板上。如果您不知道怎么操作，请点击 [这里](http://seeed.wiki/Upload_Code/)。

*   展示效果如下：

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Display_text.jpg)

*   改变显示的文字和位置，您会发现很多有趣的应用。

####  示例 2：显示图形

例程 **draw** 将是一个显示图形的示。打开里程代码，确定您是否需要插入 SD 卡来工作。并更改参数以匹配您的屏幕大小。

修改并上传代码后，屏幕上将显示一个美丽的图案：

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Display_graphic.jpg)

图片是通过调用绘制图形功能创建的。你可以使你的方法，并尝试在屏幕上绘图。

####  示例 3：显示图片

与 TFT 显示屏和 OLED 显示屏类似，电子墨水屏也支持显示图像。

打开代码 **File（文件）- &gt;Examples（示例）- &gt;ePaper-&gt;image**。

上传代码就可以看到下图：

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Dispaly_image.jpg)

!!!Note
    此 “image” 例程中的默认屏幕尺寸为 2.7 英寸。如果显示不正确，请修改屏幕尺寸设置。

<pre>  #define SCREEN_SIZE 200         // choose screen size here: 144, 200, 270 </pre>

当然，你可以通过改变图像的点阵数据来改变显示的图像。

例如，您的电子纸屏幕是2.7英寸，那么您需要获取 264 X 176 像素的点阵数据，并在 picture.h 中将代码复制到 **static unsigned char image_270 [] PROGMEM = {}**。 当使用 2.0 英寸的屏幕时，您需要将 200x96 像素点阵数据的代码复制到 **static unsigned char image_200 [] PROGMEM = {}**。

####  如何显示图像

您可以使用下图的工具来将图片转换为代码。点击 [这里](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/EpdImageKit.zip) 下载。

![](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/img/Snapshot_epaper_shied_tools.jpg)

##  参考资料
---
Small e-Paper 的库函数提供了很多函数来控制屏幕输出，下面是函数功能介绍。

###  函数描述

**1. void begin(EPD_size sz);**

这个函数设置屏幕尺寸。

*   EPD_size sz 可以设置为：EPD_1_44，EPD_2_0，EPD_2_7

**2. void setDirection(EPD_DIR dir);**

这个函数设置屏幕方向。

*   EPD_DIR dir 可以设置为：DIRLEFT，DIRRIGHT，DIRNORMAL，DIRDOWN

**3. int drawChar(char c, int x, int y);**

这个函数显示字符。

*   c：要显示的字符
*   x：字符的 X 坐标
*   y：字符的 Y 坐标

**4. int drawString(char * string, int poX, int poY);**

这个函数显示字符。

*   *string：要显示的字符串
*   poX：字符串起点的 X 坐标
*   poY：字符串起点的 Y 坐标

**5. int drawNumber(long long_num,int poX, int poY);**

这个函数显示数字。

*   long_num：要显示的整数字符串。数据类型为 long
*   poX：字符串起点的 X 坐标
*   poY：字符串起点的 Y 坐标

**6. int drawFloat(float floatNumber,int decimal,int poX, int poY);**

该函数用来显示浮点数。显示浮点数时据根据设置的小数点进行四舍五入。

*   floatNumber：要显示的浮点数
*   decimal：设置小数点位
*   poX：字符串起点的 X 坐标
*   poY：字符串起点的 Y 坐标

**7. int drawUnicode(unsigned int uniCode, int x, int y);**

该函数可以使用 unicode 来显示一个字符，例如中文。查看 [GT20L16P1Y datasheet](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/GT20L16P1Y_Datasheet.pdf) 数据表的第 18 至 24 页，查找 char unicode，字符包括拉丁文，希伯来文，泰文，希腊文和阿拉伯文等。中文 Unicode 可以查看 [GB2312 (简体中文) 字符代码表](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/Character_code_table.pdf) 。

*   uniCode：一个字符或一个中文的机器码。
*   x：字符的 X 坐标
*   y：字符的 Y 坐标

!!!Note
    0x0020 到 0x007E 之间的字符可以通过键盘直接输入。如显示字符'G'的函数可以是 drawUnicode（0x0047，3,10）或 displayChar（'s',3,10）。

**8. int drawUnicodeString(unsigned int *uniCode, int len, int x, int y);**

该函数可以用来显示几个字符或汉字。

*   *uniCode：一个 unicode 数组，包含了要显示字符的 unicode 码
*   len：字符串长度
*   x：字符串起点的 X 坐标
*   y：字符串起点的 Y 坐标

**9. void drawLine(int x0, int y0, int x1, int y1);**

这个函数绘制一条直线。

*   x0：直线起点的 X 坐标
*   y0：直线起点的 Y 坐标
*   x1：直线终点的 X 坐标
*   y1：直线终点的 Y 坐标

**10. void drawCircle(int poX, int poY, int r);**

这个函数绘制一个圆。

*   poX：圆心的 X 坐标
*   poY：圆心的 Y 坐标
*   r：圆的半径

**11. void drawHorizontalLine( int poX, int poY, int len);**

这个函数绘制一条水平线。

*   poX：直线起点的 X 坐标
*   poY：直线起点的 Y 坐标
*   len：直线的长度

**12. void drawVerticalLine( int poX, int poY, int len);**

这个函数绘制一条垂直线。

*   poX：直线起点的 X 坐标
*   poY：直线起点的 Y 坐标
*   len：直线的长度

**13. void drawRectangle(int poX, int poY, int len, int width);**

这个函数绘制一个矩形。

*   poX：矩形起点的 X 坐标
*   poY：矩形起点的 Y 坐标
*   len：矩形的长
*   width：矩形的宽

**14. void fillRectangle(int poX, int poY, int len, int width);**

这个函数绘制一个实心矩形。

*   poX：矩形起点的 X 坐标
*   poY：矩形起点的 Y 坐标
*   len：矩形的长
*   width：矩形的宽

**15. void fillCircle(int poX, int poY, int r);**

这个函数绘制一个实心圆。

*   poX：圆心的 X 坐标
*   poY：圆心的 Y 坐标
*   r：圆的半径

**示例：**

```
    EPAPER.drawRectangle(10, 10, 100, 80);
    EPAPER.fillCircle(50, 50, 30);
    EPAPER.fillRectangle(50, 65, 50, 20);
    EPAPER.drawCircle(150, 50, 10);
    EPAPER.fillCircle(150, 50, 5);
    EPAPER.drawHorizontalLine(120, 50, 60);
    EPAPER.drawVerticalLine(150, 20, 60);
```

**16. void drawTraingle( int poX1, int poY1, int poX2, int poY2, int poX3, int poY3);**

这个函数绘制一个三角形，三角形由三个端点构成。

*   poX1(poX2,poX3): 三角形一个端点的 X 坐标。
*   poY1(poY2,poY3): 三角形一个端点的 Y 坐标。

##  资源下载
---
- **[Eagle 文件]**[Small e-Paper Shield Eagle File](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/Small_e-Paper_Shield_v2.2_Eagle_Files.zip)

- **[库函数]**[Small e-Paper Library](https://github.com/Seeed-Studio/Small_ePaper_Shield)

- **[数据手册]**[e-Paper panels Datasheet](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/4P008-00_02_COG_Driver_Interface_Timing_for_smallPlussize.pdf)

- **[工具]**[epdImageKit Tool](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/EpdImageKit.zip)

- **[库函数]**[New Panel Library【EPD_V230】](https://github.com/SeeedDocument/Small_e-Paper_Shield_V2/raw/master/res/EpdV230.rar)
