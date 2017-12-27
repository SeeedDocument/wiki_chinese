---
title: Shield Bot V1.1
category: Arduino
bzurl: https://www.seeedstudio.com/Shield-Bot-p-1380.html
oldwikiname:  Shield Bot V1.1
prodimagename: 4WD_Mecanum_Wheel_Robot_Kit-RF_Version-.PNG
wikiurl: http://seeed.wiki/Shield_Bot_V1.1
sku:  110060010

---
![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/shield%20bot.jpg)

与以前的版本相比，Shield Bot V1.1 可以使用 PC 的 USB 端口充电。电路优化后充电效率大大提高。您可以使用 Arduino/Seeeduino Vin 引脚快速充电。

注：Arduino 板不包括在内，如有需要可以购买 [Seeeduino](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5543b2c5BbD7Jd&id=45721222112)。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.5bbe7102fPxhGG&id=559366535332)

##  产品特性
---
*   **易于使用** - Shield Bot 即插即用，几分钟内就可以开箱使用。

*   **开源** -  开放式设计，可以改编并转化为您想要的东西。

*   **基于 Arduino** - Shield Bot 是一个 Arduino 扩展板，所以可以通过广泛的扩展板系统进行无尽的扩展。

*   **快速充电** - 可以高效快速充电。

!!!Note
    新版本更新后，输出电压由约 4.0V 变为约 4.5V。

##  规格参数
---

<table>
<tr>
<th> 项目 </th>
<th> 参数
</th></tr>
<tr>
<td width="200"> 传感器 </td>
<td width="300"> 5 个红外线反射传感器，用于线路和边缘跟踪
</td></tr>
<tr>
<td> 锂离子充电电池	</td>
<td> 900 mAh
</td></tr>
<tr>
<td>减速机 </td>
<td>两个耐用的减速比 160:1 的微型金属减速电机
</td></tr>
<tr>
<td> Grove 接口 </td>
<td> 6 x Grove 扩展接口
</td></tr>
<tr>
<td>扩展板针头 </td>
<td> Arduino 扩展板针头
</td></tr></table>

##  充电规格参数
---
充电模式和充电效率如下表所示：

<table>
<tr>
<th> 模式 </th>
<th> 充电电流(A) </th>
<th> 输入功率(W) </th>
<th> 充电功率(W) </th>
<th> 充电效率(%) </th>
<th> 充电时间(h)
</th></tr>
<tr>
<td width="200"> USB 充电	 </td>
<td width="200"> 0.396 </td>
<td width="200"> 3.94	 </td>
<td width="200"> 3.56 </td>
<td width="200"> 90.36 </td>
<td width="200"> 2.50
</td></tr>
<tr>
<td> Vin 充电	 </td>
<td>  0.7	</td>
<td>   6.78		 </td>
<td>  6.30</td>
<td>  92.92 </td>
<td>   1.41
</td></tr></table>

##  接口功能
---
![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Shield_Bot_V1.2_Foto_1.JPG)

*   **IR Line Finder Potentiometer (电源开关)**：当 Shield Bot 关闭时，Shield Bot 停止运行。但是您可以使用 **USB 充电端口** 为电池充电。

*   **USB Charge Port (USB 充电端口)**：USB mini-B 接口，用于电池充电。

*   **Grove Ports (Grove 接口)**：Grove 接口访问引脚 D0，D1，D2，D3，D4，D5，A4，A5。可以将 Grove 模块连接到这些 Grove 接口。

*   **IR Line Finder Potentiometer (红外巡线灵敏度计)**：用于调整巡线灵敏度。顺时针调整，灵敏度增加; 逆时针调整，灵敏度下降。

*   **IR Line Finders (红外巡线灵敏度计)**：S1 to S5. Blue if non reflective surface is detected (ex Black tape line)

*   **Enable Switch (启用开关)**：将开关转到 "ON" ，将巡线器连接到 Arduino 的 I/O 引脚 (已占用引脚为 A0，A1，A2，A3，D4)。库中的 LineFollowingSimple 演示使用巡线器输出信号来控制 Shield Bot 运行。如果开关处于 "OFF" 状态，Seeeduino/Arduino 无法通过巡线器输出信号控制 Shield Bot。

*   **Arduino Shield Expansion Headers (Arduino 扩展板针头)**：Shield Bot 可以堆叠其他扩展板。

!!!Note
    - 1) 如果启用了 S5，就不能使用 Grove 接口 j14 和 j13。
    - 2) 您只能使用 Arduino 的串行线，UART Grove 端口或 j11 中的一个，因为它们共用 D1/TX 线。


##  状态指示灯
---
Shield Bot 上有许多 LED，通过它们可以知道 Shield Bot 现在的运行状态

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Shield_bot_1.2_LEDs.JPG)

<table>
<tr>
<th> 灯号 </th>
<th> 功能 </th>
<th> 状态
</th></tr>
<tr>
<td width="200"> D22 </td>
<td> 电源</td>
<td> 绿色 - Shieldbot 上电，ShieldBot 断电时, ShieldBot 只能为电池充电。
</td></tr>
<tr>
<td> D23 和 D24	 </td>
<td> 充电状态</td>
<td> 红色 - 充电中，绿色 - 充电完成
</td></tr>
<tr>
<td> D18 </td>
<td> 重置</td>
<td> 红色 - 按钮按下时
</td></tr>
<tr>
<td> D11 和 D12	 </td>
<td> 右电机指示灯	</td>
<td> 绿色 - 前进，红色 - 后退，同时亮 - 停止
</td></tr>
<tr>
<td> D13 and D15		 </td>
<td> 左电机指示灯		</td>
<td> 绿色 - 前进，红色 - 后退，同时亮 - 停止
</td></tr>
<tr>
<td> D5 D10 D14 D17 D19	 </td>
<td> 光传感器指示灯		</td>
<td> 蓝色 - 检测到非反射表面
</td></tr></table>

##  产品结构
---
![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Position_for_seeeduino.jpg)

Part 1，Part 2 和 Part 3 由 3D 打印机打印得到。两个车轮是一样的。打印过程如下所示。

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Print_diagram_1.JPG) ![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/P1018898.JPG)

##  入门指导
---
Shield Bot 的设置快速而简单 !

###  准备工作

*   首先，您需要将 Arduino 插入 Shield Bot 底部，并使用 USB 线缆将其连接到 PC。

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/ShieldBot_Programming2.JPG)

*   上传代码之前，最好将启用开关设置为 _OFF_。否则，它可能突然运行吓到您。

我们为 Shield Bot 建立了库文件，它有很多有用的功能以控制您的 Shield Bot，还有一些示例可以让您快速上手 !

*   从 [这里](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/Shield_Bot_Library.zip) 下载库文件并且解压。在使用库文件之前，请打开 Note.txt 文件。
*   将 Shield Bot 库文件放到 Arduino IDE 的库文件中，路径为 : **..\arduino-1.0.1\libraries**。

###  安装电池

Shield Bot 需要电池才能在地面上运行。请参考下面的图片来安装电池。

![](/w/index.php?title=%E5%9B%BE%E7%89%87&amp;action=edit&amp;redlink=1 "%E5%9B%BE%E7%89%87&amp;action=edit&amp;redlink=1")

安装完成后，您将看到 :

![](/w/index.php?title=%E5%9B%BE%E7%89%87&amp;action=edit&amp;redlink=1 "%E5%9B%BE%E7%89%87&amp;action=edit&amp;redlink=1")

!!!Note
    - 1) 一旦电池完成安装，可以使用 mini-b USB 线缆给电池充电。充电中，红色 LED 亮起。充电完成后，绿色的 LED 亮起。
    - 2) 上传代码时，您需要将 Seeeduino 的 USB 端口连接到PC。Shield Bot 上的 USB 端口仅用于为电池充电。


!!!Note
    因为我们要更改 Shield Bot v1.1的驱动程序引脚。因此，在使用 Shield Bot 库文件之前，请确保已经修改了 .cpp 文件以匹配 Shield Bot 版本。修改步骤在 Note.txt 中有描述。

###  示例1：Shield Bot 运行

*   打开 Arduino IDE 并跳转到 : **File (文件)-&gt;Examples (示例)-&gt;Shieldbot-&gt;drive to load the first Shield Bot example**。确保选择了正确的 Arduino 板和串口。
*   然后上传代码到 Arduino 中。上传完成后，控制台应显示 "Done Uploading"。
*   完成上传后可以拔下 USB 线缆。
*   然后将 Shield Bot 放在宽敞的地方，并将电源开关打到 **'ON'**。
*   现在 Shield Bot 将以一定的速度运行。

###  示例2：跟随黑线运行

Shield Bot 可以根据巡线传感器 (s1,s2,s3,s4,s5) 检测反射表面。如果检测到非反射表面，蓝色指示灯将亮起。现在让我们用它来跟随黑线。

!!!Note
    确保拨码开关已打到 'ON'，并且没有扩展板使用引脚 A0，A1，A2，A3 或 D4。

*   使用 USB 电缆将 Seeeduino 连接到 PC 后，重新上传新演示 : LineFollowingSimple。

*   完成上传后。将 Shield Bot 放置在预先搭建的黑色跑道上 然后会出现令人惊叹的一幕 :

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Shield_Bot_Line_Finder.jpg)

*   您可以调整红外巡线灵敏度计来改变巡线灵敏度。顺时针调整，灵敏度增加; 逆时针调整，灵敏度下降。

###  Appatation Instances

**1. Clock**

This is a  incredibly simple, working clock. The wheels turn one forward and one reverse, spinning the reflectance sensors around the wheel indicating the minutes. Upon the hour mark the bot drives forward and advances the linear slide to indicate hours. Extra credit for the free linear rails made out of laser cut scrap and cellophane tape!

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Team1_2.jpg)

**2. Shot.Bot**

It was a really gorgeous device that many people in the event remarked they'd like to buy. The line following robot would take orders then drive the track to the dispenser where it would use a servo to actuate an amount of either of 3 beverages, before driving back to the patron

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Team7_2.jpg)

**3. Simon**

There has a a beautifully designed, though not quite finished, 2 player heads up simon clone. The bot plays out a tune with lights and you use the laser cut puck, complete with braille so even the sight impaired could play, to mark the tones on the whiteboard. The Shieldbot then drives forward and uses the sensors to see if you've marked correctly. You want to get more right answers than your opponent so the bot drives towards their goal!


![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Team6_2.jpg)



**4. HackPHX-Plotter**

The device is very close to knocking off the Der Kritzler 2d drawing machine which is a vertical x,y table with makerslide and had the ingenious idea of bolting the tires of the Shield bot down such that when it was put in reverse, it lifted the pen off the drawing surface :) They even worked with the designer to come up with a PC side user interface!


![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/Team8.jpg)



##   参考资料
---
要使用 Shield Bot 库，只需添加 Shield Bot 库，并在 void setup() 之前在 Arduino 代码的顶部声明 Shield Bot 对象。

```c
#include <Shieldbot.h>	//includes the Shield Bot Library
Shieldbot shieldbot = Shieldbot(); //decares a Shieldbot object
```

<u> **setMaxSpeed(int both)**</u>

<dl><dd>_说明_ : 设置两台电机的最大速度。
</dd><dd>_both_ :  在 0 (静止) 和 255 (全速) 之间。
</dd></dl>

<u> **setMaxSpeed(int left, int right)** </u>

<dl><dd>_说明_: 向左右电机写入最大速度。
</dd><dd>_left,right_: left 是左侧电机的速度。right 是右侧电机的速度。 在 0 (静止) 和 255 (全速) 之间。
</dd></dl>

<u> **rightMotor(char mag)** </u>

<dl><dd>_说明_: 启用右电机，负数倒退，正数前进。如果使一个电机变慢，它将朝那个方向转动。如果使电机反方向，则会旋转。
</dd><dd>_mag_: 旋转右侧电机的方向 : -128 : 倒退 ; 0 : 停转 ; 127 : 前进。
</dd></dl>

<u> **leftMotor(char mag)** </u>

<dl><dd>_说明_: 启用左电机，负数倒退，正数前进。
</dd><dd>_mag_: 旋转右侧电机的方向 : -128 : 倒退 ; 0 : 停转 ; 127 : 前进。
</dd></dl>

<u> ** forward() ** </u>

<dl><dd>_说明_: 电机以 setSpeed() 设定的速度带动小车直线前进。
</dd></dl>

<u> ** backward()** </u>

<dl><dd>_说明_: 电机以 setSpeed() 设定的速度带动小车直线后退。
</dd></dl>

<u> ** drive(char left, char right)** </u>

<dl><dd>_说明_: 通用驱动调用。直接调用 leftMotor 和 rightMotor。
</dd><dd>_left_: 在 -128 (左电机最大后退速度)，0 (静止) 和 127 (左电机最大前进速度) 之间。
</dd><dd>_right_: 在 -128 (右电机最大后退速度)，0 (静止) 和 127 (右电机最大前进速度) 之间。
</dd></dl>

<u> **stop()** </u>

<dl><dd>_说明_: 禁用电机。您也可以使用 drive(0,0)。
</dd></dl>

<u> **stopLeft()** </u>

<dl><dd>_说明_: 禁用左侧电机。您也可以使用驱动器 drive(0,X)。
</dd></dl>

<u> **stopRight()** </u>

<dl><dd>_说明_: 禁用右侧电机。您也可以使用驱动器 drive(X,0)。
</dd></dl>

<u> **fastStopLeft()** </u>

<dl><dd>_说明_: 快速禁用左侧电机。这可能对马达芯片产生不良影响，请酌情使用
</dd></dl>

<u> **fastStopRight()** </u>

<dl><dd>_说明_: 快速禁用右侧电机。这可能对马达芯片产生不良影响，请酌情使用
</dd></dl>

<u>**readS1(), readS2(), readS3(), readS4(), readS5()** </u>

<dl><dd>_说明_: 读取板上 5 个光传感器中的任何一个。注意，需要使用拨码开关块将传感器连接到 Arduino 端口。如果您不想使用光传感器，拨码开关块可以使您通过这些引脚来处理其他事情。
</dd><dd>_Returns_: 如果表面反光 (如白色) 则为 LOW，如果表面不反光 (如黑色) 则为 HIGH。
</dd></dl>

![](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/img/ShieldBot_driveLibrary.png)

##  资源下载
---
*   **[Eagle 文件]** [Shield Bot Eagle Files](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/Shield_Bot_Eagle_Files.zip)

*   **[原理图 PDF]** [ShieldBot Schematic](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/ShieldBotv0.9b_Schematic.pdf)

*   **[库文件]** [Shield Bot Library](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/Shield_Bot_Library.zip)

*   **[芯片数据手册]** [RPR-220 Datasheet](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/RPR-220.pdf) IR Reflectance Sensor

*   **[芯片数据手册]** [ISL97516 Datasheet](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/ISL97516.pdf) Step up regulator

*   **[芯片数据手册]** [BQ2057 Datasheet](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/BQ2057.pdf) Li-ion charger

*   **[芯片数据手册]** [L298 Datasheet](https://github.com/SeeedDocument/Shield_Bot_V1.1/raw/master/res/L298.pdf) H-Bridge Motor Driver

*   **[芯片数据手册]** [358 Datasheet](http://www.ti.com/product/lmv358) Op-Amp as a comparator for reflectance sensors
