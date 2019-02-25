---
name: Sidekick Basic Kit for Arduino V2
category: Arduino
bzurl: https://www.seeedstudio.com/Sidekick-Basic-Kit-for-Arduino-V2-p-1858.html
oldwikiname:   Sidekick Basic Kit for Arduino V2
prodimagename:  BasicKit.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Sidekick_Basic_Kit_for_Arduino_V2
sku:  110060025
---
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/BasicKit.jpg)

The Arduino Sidekick Basic Kit 旨在与您的 Arduino / Seeeduino / Seeeduino ADK / Maple Lilypad 或任何 MCU 板一起使用。它包含了用户第一次将他们的计算机连接到Arduino所需的一切。 它包括许多 DIY 项目最受欢迎的配件 : 如面包板，跳线，彩色 LED，电阻器，蜂鸣器等。所有这些都带有自己的便利盒，便于使用和避免了杂乱。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.75eb7338caGIyZ&id=531838157675)

##   套件零件
---
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Basic_Kit_for_Arduino_Photo_11.jpg)

1.  面包板 x 1
2.  绿色 LED x 5
3.  红色 LED x 5
4.  RGB 共阳极 LED x 1
5.  陶瓷电容 (10nF x 10+100nF x 10)
6.  铝电容 (100uF x 5)
7.  电阻 (330R x 10+1k x 10+10k x 10)
8.  倾斜开关 x 1
9.  热敏电阻 x 1
10.  光电阻 x 1
11.  二极管 x 1
12.  蜂鸣器 x 1
13.  按键 x 5
14.  开关 x 5
15.  迷你伺服器 x 1
16.  带旋钮的电位器 x 1
17.  面包板跳线 x 25（5x 长线, 20 x 短线） 面包板 x 1
18.  盒 x 4

##   电学基础知识普及
---
### 电流和电压
电流是导体中流动电荷的速率。电压是施加在两点之间用来传导电流的电位差 (电驱动力)。 电流以安培 (A) 为单位，电压以伏特 (V) 为单位。

### 电阻

电阻是导体中流动电流的障碍。它们用于限制电流到诸如灯的电子设备的流动。对于流动电流的阻抗用欧姆 (Ω) 表示，电阻可分为_**固定电阻**_和_**可变电阻( POT )**_。

**连接电阻**

电阻可以以两种不同的方式连接 : 并联或彼此串联。

**串联电阻**

当电阻串联时，总等效电阻将等于串联电阻的所有值的总和。

**并联电阻**

当电阻并联时，总等效电阻的倒数等于每个电阻的倒数之和。

### 欧姆定律

电流，电压和电阻之间的关系由欧姆定律决定 - 其中指出“两点之间的导体电流 ( I 安培) 与两点( V 伏特)之间的电位差或电压成正比， 与它们之间的电阻( R 欧姆)成比例，即 I = V / R。因此 V = IR 或 R = V / I.以下欧姆定律三角形可用于记住 V，I 和 R 之间的关系。垂直线表示乘法运算，水平线表示除法运算。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Ohm-s_law_triange.jpg)

eg : 因此，要知道当前 I，我们将 V 除以 R。

### 面包板

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Breadboard_.jpg)

**面包板**是电子电路的原型设备。连接电子元件和制作电路不需要焊接是非常有用的。面包板由行和列的孔组成，金属触点插入组件。[Arduino Sidekick Basic Kit](/Arduino_Sidekick_Basic_Kit "Arduino Sidekick Basic Kit") 附带的面包板配置有 **2×30 个五孔**列和 **4×25 孔**行。 这些孔以如下所示的方式在内部连接。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_Breadboard_Internal_Connections.jpg)

### 固定电阻

Basic Kit 提供的电阻由碳制成，属于定值电阻类型。电阻值由彩色带标记。您可以从电阻颜色代码表中获取值。

*   第一个环表示电阻值的**第一个数字**。

*   第二个环表示**第二个数字**。

*   第三个环表示电阻的**乘数**值。

*   第四个环带表示**公差值**。

### 电位计 ( POT )

POT是一个可变电阻器，其电阻可以通过旋转旋钮来改变。它有三个端子 - 电阻器两侧的端子连接到由电阻材料制成的导体端。中间端子连接到在电阻材料上移动的滑块。电阻值与旋钮的位置成比例地变化。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_POT.png)

### 热敏电阻

热敏电阻是特殊的电阻，其电阻随温度变化。它们提供非常有用和方便的方法来感测温差。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Thermistor.JPG)

### 光敏电阻 (LDR)

当在其上的光线强度变化时，LDR 会改变电阻。它们也称为光电池。当没有光照射时，它提供最大的电阻，并在暴露于明亮的光线时提供最小的电阻。它由光敏材料如硫酸镉组成，可连接到电路。它可以用作光感测元件。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_LDR.JPG)

### 发光二极管

当 LED 正向通电时将发光亮起。它们被封装在透明的外壳中，并且进入各种颜色，如红色，绿色和蓝色。LED 由砷化镓磷化物制成，并且通过改变砷和磷的比例，可以获得不同的颜色。单色 LED 具有两个引线阳极( +ve )和阴极 ( -ve )。 三色 LED 有四个引线 - 一个阳极和三个对应每个颜色的阴极。LED 可用于显示板。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_RGB_LED_.JPG)

### 开关

开关用于关闭或打开电路。The Arduino Sidekick Basic Kit 提供的开关有两种类型 - 按钮开关和滑动开关。

**按钮开关**

只要按下按钮开关，电路就会关闭。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Push_Button_Switch_.JPG)

**滑动开关**

滑动开关是一个简单的两个位置开关。它可以用于通过将电路设置到适当的位置来打开或关闭电路。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Slide_Switch_.JPG)

**倾斜开关**

倾斜开关包含两个连接到电路的端子，当水平倾斜时，它会闭合电路，同时垂直旋转时打开电路。

### 电容

电容器用于存储电荷。它们分为两种不同类型 : 电解和陶瓷盘式电容器。 电容器以微法拉（uF）为单位。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Capacitor.JPG)

**连接电容**

电容器可以在电路中以两种类型的布置连接，如下所示。

**串联电容**

当两个或更多个电容器彼此串联连接时，总等效电容等于各个电容值的倒数之和。

**并联电容**

当并联连接的两个或多个电容器时，总等效电容等于单独电容的总和。

**电解电容器**

电解电容器通常体积小，电容量大。它们分为极化和非极化电解电容器。使用铝，钽，钒和铋等金属来形成阳极和阴极箔。

**陶瓷盘式电容器**

陶瓷电容器使用具有薄金属膜的陶瓷电介质作为与陶瓷结合的电极。在 Disc 类型中，电容器银固定在陶瓷的两侧以形成导体板。盘式电容器仅用于要求较小的电容值时。

### 蜂鸣器

蜂鸣器是音频信号装置，其可以是机械的，机电的或压电的。 它根据其中使用的材料的振荡产生各种音频信号。 它们通常用于报警和定时器。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Buzzer.png)

将长引脚连接到正电压，将短引脚连接到地。

蜂鸣器可以连接数字输出，输出高电平时会发出一声音。 或者，它可以连接到模拟 PWM 输出以产生各种音调和效果。

### 二极管

二极管是仅在一个方向传导电流的半导体材料。只有在电源电压大于_势垒电位_后才开始导通。它的作用就像正向偏置状态下的闭合开关，当反向偏置时，其作用类似于开路开关。二极管基于半导体材料分类，可用于制造 PN 结二极管，齐纳二极管，发光二极管等。

**偏置二极管**

将二极管施加电压称为偏置二极管。当在两个端子之间施加**正电源**电压时，二极管将获得_**正向偏压**_，并开始对硅二极管施加高于 0.7v 的电流，对于锗二极管开始导通 0.3v。当施加**负电压时**在二极管的端子之间，就说被_**反向偏置**_。当反向偏置电压超过击穿电压时，二极管损坏。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Sidekick_Diode.JPG)

<big>迷你伺服器</big>

伺服系统是具有齿轮和反馈系统的直流电动机，用于机器人的驱动机构。

![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Mini_Servo_Photo.jpg)

##   教程

<big>Hello World! : The Blinking LED</big>

**电路**

*   将 LED 连接到数字引脚 **8**，如下所示。 330 欧姆电阻限制了流向 LED 的电流。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_1LED_Blink.jpg)

**程序**

编译并上传以下代码 :
```
//Blink a LED connected to Digital Pin 8 via a 330 Ohm resitors.

void setup()   {
    pinMode(8, OUTPUT);       // Initialize Arduino Digital Pin 8 as output
}


void loop()
{
    digitalWrite(8, HIGH);   // Switch On LED
    delay(500);              // Wait for half a second
    digitalWrite(8, LOW);    // Switch Off LED
    delay(500);              // Wait for half a second
}
```

###   运行 LED 显示

**电路**

*   通过一个 330 欧姆电阻将 3 个 LED 连接到数字引脚 **9**,**10** 和 **11**。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_3LEDs_Display.jpg)

**程序**

编译并上传以下代码 :
```
//Running LED display: Three LEDs connected to Digital Pin 9, 10 and 11.

void setup()
{
    pinMode(9, OUTPUT);        // Initialize Arduino Digital Pins 9 as output
    pinMode(10, OUTPUT);       // Initialize Arduino Digital Pins 10 as output
    pinMode(11, OUTPUT);       // Initialize Arduino Digital Pins 11 as output
}


void loop()
{

    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);
    delay(250);              // Wait for quarter of a second
    digitalWrite(9, LOW);
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
    delay(250);              // Wait for quarter of a second
    digitalWrite(9, HIGH);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
    delay(250);              // Wait for quarter of a second

}
```

  ###   与Arduino 通话：连接按钮开关

**电路**

*   将 LED 连接到数字引脚 **8**，如下所示。330 欧姆电阻限制了流向 LED 的电流。

*   将一个按钮开关连接到数字引脚 **12**，另一个通过 10K 电阻连接到 **GND**。

*   将按钮的另一端连接到 +5V。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_Pushbutton_LED.jpg)

**程序**

编译并上传以下代码 :
```
//Pushbutton switch demo: LED is connected to digital pin 8 and Pushbutton is connected to digital pin 12.
//The LED glows when the button is pressed.

char inputButtonState;

void setup()
{
    pinMode(8, OUTPUT);        // Initialize Arduino Digital Pins 8 as output for connecting LED
    pinMode(12,INPUT);         // Initialize Arduino Digital Pins 12 as input for connecting Pushbutton
}


void loop()
{
    inputButtonState = digitalRead(12); //Read the Pushbutton state.

    if (inputButtonState == HIGH)
    {
        digitalWrite(8, HIGH);  //Switch on LED
    }
    else
    {
        digitalWrite(8, LOW);   //Switch off LED
    }

}
```

以上确实说明了如何向 Arduino 发送信号。 事实上，如果没有 Arduino，你可以实现同样的目标。 只需按下按钮关闭电路，然后按如下所示翻转 HIGH/LOW 值 :
```
void loop()
{
    inputButtonState = digitalRead(12); //Read the Pushbutton state.

    if (inputButtonState == HIGH)
    {
        digitalWrite(8, LOW);  //Switch on LED
    }
    else
    {
        digitalWrite(8, HIGH);   //Switch off LED
    }
```

当电路闭合时LED 将亮起。

### 3 模拟 : POT

**电路**

*   通过 220 欧姆电阻将 LED 的阳极连接到 **PWM** 引脚。

*   将 LED 的阴极连接到 **GND** 引脚。

*   将 POT 放在面包板上。

*   将 POT 的右脚连接到 +5V。

*   将 POT 的中间脚连接到任何模拟输入引脚 (0-5)。

*   将 POT 的左脚连接到接地端。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_potled1.jpg)

**程序**

将 LED 阳极连接到数字引脚 **5** ( 而不是 5V )。编译并上传以下代码 :
```
//Varying the brightness of the LED using a Pot
int value=0;
int mval;
void setup()
{
    pinMode(5, OUTPUT);
}
void loop()
{
    value=analogRead(A1); //read analog value from input A1
    // PWM output given to the LED
    mval = map(value, 0, 1023, 0, 100);
    analogWrite(5,mval);

}
```

### 4 彩虹台 : 三色 LED

**电路**

The Arduino Sidekick Basic Kit 提供的 RGB LED 是常见的阳极型。最长的铅是阳极。其他三个引线分别是红，绿和蓝的阴极。

*   通过一个 330 欧姆的电阻将 RGB 阴极 LED 连接到数字引脚 **9**,**10** 和 **11**。

*   将阳极连接到 +5v
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_RGB_LED_Display.jpg)

**程序**

编译并上传以下代码 :
```
void setup()  {

}

void loop()  {


    for(int b = 0 ; b <= 255; b=b+5)
    {
        for(int g = 0 ; g <= 255; g=g+5)
        {
            for(int r= 0 ; r <= 255; r=r+5)
            {
                analogWrite(9, b);
                analogWrite(10, g);
                analogWrite(11, r);
                delay(10);

            }
        }
    }

}
```
### 5 音乐 :

**电路**

*   将蜂鸣器阳极连接到数字引脚 **11**。

*   将蜂鸣器阴极接到 **GND**。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_Music.jpg)

**程序**

编译并上传以下代码 :

```
#define NOTE_D0 98
#define NOTE_D1 294
#define NOTE_D2 330
#define NOTE_D3 350
#define NOTE_D4 393
#define NOTE_D5 441
#define NOTE_D6 495
#define NOTE_D7 556
#define NOTE_DL1 147
#define NOTE_DL2 165
#define NOTE_DL3 175
#define NOTE_DL4 196
#define NOTE_DL5 221
#define NOTE_DL6 248
#define NOTE_DL7 278
#define NOTE_DH1 589
#define NOTE_DH2 661
#define NOTE_DH3 700
#define NOTE_DH4 786
#define NOTE_DH5 882
#define NOTE_DH6 990
#define NOTE_DH7 112

#define WHOLE 1
#define HALF 0.5
#define QUARTER 0.25
#define EIGHTH 0.125
#define SIXTEENTH 0.625

// notes in the melody:
int tune[] =
{
    NOTE_D0,NOTE_D1,NOTE_D2,NOTE_D3,NOTE_D4,NOTE_D5,NOTE_D6,NOTE_D7,
    NOTE_DL1,NOTE_DL2,NOTE_DL3,NOTE_DL4,NOTE_DL5,NOTE_DL6,NOTE_DL7,
    NOTE_DH1,NOTE_DH2,NOTE_DH3,NOTE_DH4,NOTE_DH5,NOTE_DH6,NOTE_DH7,
};
/* note durations: 1 = one note*/

float duration[]=
{1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,};
int length;
int tonePin=11;                // buzzer pin
void setup()
{ Serial.begin(9600);
    pinMode(tonePin,OUTPUT);   //  initialize the digital pin as an output
    length = sizeof(tune)/sizeof(tune[0]);
}
void loop()
{
    for(int x=1;x<length;x++)
    {tone(tonePin,tune[x]);
        delay(400*duration[(x%100)]);    // to distinguish the notes, set a minimum time between them.

        noTone(tonePin); // stop the tone playing:
    }
}
```

### 6 迷你伺服器 :

**电路**

*   将伺服的红色线连接到 +5v 电源。
*   将伺服的黑色线连接到地。

*   将伺服的黄色线连接到 Arduino 中的任何 PWM 引脚。

*   将 POT 的右脚连接到 +5v。

*   将 POT 的中间脚连接到任何模拟输入引脚 (0-5)。

*   将 POT 的左脚连接到接地端。
![](https://github.com/SeeedDocument/Sidekick_Basic_Kit_for_Arduino_V2/raw/master/img/Arduino_Sidekick_Mini_Servo.jpg)

**程序**

编译并上传以下代码 :
```
// Controlling a servo position using a potentiometer (variable resistor)
// by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int potpin = 1;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup()
{
    myservo.attach(5);  // attaches the servo on pin 5 to the servo object
    Serial.begin(19200); // some servos doesn't work without Serial
}

void loop()
{
    val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
    val = map(val, 0, 1023, 0, 179);     // scale it to use it with the servo (value between 0 and 180)
    myservo.write(val);                  // sets the servo position according to the scaled value
    delay(15);                           // waits for the servo to get there
}
```

##   使用方法
---
*   有一个无焊面包板，因此，不需要购买烙铁或学习如何焊接。

*   有很多跳线，长而柔软，具有刚性尖端。这些跳线比以往的固定长度实线跳线好得多。

*   您的第一个项目有很多 LED 和电阻，包括一个 RGB LED，它是一个单一的 LED 封装，内部有三个主要的彩色 LED。通过调整不同原色 LED 的强度，颜色将混合在一起并产生彩虹的所有颜色。
*   甚至还有一个教您怎么做来读取电阻值。
*   倾斜开关是一个非常简单的装置，内部有一个小金属球。如果设备倾斜到一侧，金属球将触及电气触点。 该传感器适用于各种项目，如 DIY 防盗报警器。
*   当您想要检测温度时，热敏电阻对于您的项目很有用。
*   光电阻可以检测光，并且可以用灯泡和阳光照射。光电阻通常用于检测黑暗时间，夜间开灯。
*   该套件中的蜂鸣器特别适合演奏马里奥兄弟主题曲。
*   有一个迷你伺服器。您可以使用它来打开和关闭门栓，灯开关或阀门。你甚至可以使用它来制作迷你弹射器。
*   电位器是一个很好的输入设备。 您可以使用它来控制伺服臂的角度或 LED 的强度。

##   外部链接
---
[Arduino Video tutorial series by Jeremy Blum](http://www.youtube.com/playlist?list=PLA567CE235D39FA84)
