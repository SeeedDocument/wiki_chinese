---
name: Grove - Buzzer
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-Buzzer-p-768.html
oldwikiname: Grove - Buzzer
prodimagename: Grove%20Buzzer.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Buzzer/
sku: 107020000
---

---
![](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/images/Grove%20Buzzer.jpg)

 Grove - Buzzer 模块以[压电蜂鸣器](https://en.wikipedia.org/wiki/Buzzer#Piezoelectric)作为主要组件。 它可以连接到数字端口输出，当输出为高电平时，会发出一个音调。 它可以连接到模拟脉冲宽度调制处理器来输出各种音调，能够产生各种不同的效果。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.24142783d0jBoe&id=520245748676)

## 产品特性
---

- 易于使用的压电蜂鸣器
- 使用标准的 4 针 Grove 连接线连接到其他 Grove 模块，例如 -Grove Power Modules 和 Grove - Base Shield

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

## 规格参数
---
- 工作电压：4-8V
- 声音输出：≥85dB
- 共振频率：2300±300Hz


## 使用方法
---
**单独使用**

按照以下步骤，可以使用此模块构建一个采样电路并且不需要使用任何微控制器：

1. 将蜂鸣器模块连接到电路的输出端（电源模块右侧）。 在电路的输入端，您可以使用一系列基于传感器的输入模块 (**Grove - Light Sensor**, **Grove - Button** 和 **Grove - Slide Potentiometer**)。
2. 启动电路。
3. 当输入模块提供触发时，蜂鸣器将开始发出 “蜂鸣” 声：
   - 如果使用像 **Grove - Button module** 那样的瞬间开关，只需按下按钮即可打开蜂鸣器。
   - 如果使用 **Grove - Slide Potentiometer**，将滑块从 GND 位置移动到 VCC，并查看蜂鸣器的音调和频率随供电电压的增加而变化。
   - 如果使用 **Grove - Light Sensor** 直接连接到电路的输入端，您应该在明亮的光线下听到蜂鸣器，并在黑暗中停止 “嗡嗡”。 如果您希望蜂鸣器在黑暗中发出声音，请在光传感器和电源模块之间添加一个 **Grove - NOT** 模块。

您可以使用 **Grove - USB Power**  模块或  **Grove - DC Jack Power** 模块作为 Grove 电路。

**使用 Arduino**

按照以下简单的步骤，使用蜂鸣器构建 Grove 电路：

1.将模块与 Arduino 或 **Seeeduino** 结合使用时，请使用 **Grove - Base Shield**，并使用指定的 Grove 接口将 Grove - Buzzer 模块连接到 Grove - Base Shield，如下所示：

![](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/images/Conn-four.jpg)

2.上传以下程序示例，使蜂鸣器发出哔声：

```c
// Project Four - Noise maker
//

void setup()
{
  pinMode(6, OUTPUT);
}

void loop()
{
  digitalWrite(6, HIGH);
  delay(analogRead(0));
  digitalWrite(6, LOW);
  delay(analogRead(0));
}
```
**使用 TI LaunchPad**

播放音乐（蜂鸣器）

- 此示例演示如何使用 Grove buzzer 模块播放旋律。 它向蜂鸣器发送适当频率的方波，产生相应的音调。

![](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/images/Buzzer.jpg)

```c
/*
  Buzzer
 The example use a buzzer to play melodies. It sends a square wave of the
 appropriate frequency to the buzzer, generating the corresponding tone.

 The circuit:
 * Buzzer attached to pin39 (J14 plug on Grove Base BoosterPack)
 * one side pin (either one) to ground
 * the other side pin to VCC
 * LED anode (long leg) attached to RED_LED
 * LED cathode (short leg) attached to ground

 * Note:
 This example code is in the public domain.

 http://www.seeedstudio.com/wiki/index.php?title=GROVE_-_Starter_Kit_v1.1b#Grove_-_Buzzer

*/

/* Macro Define */
#define BUZZER_PIN               39            /* sig pin of the buzzer */

int length = 15;         /* the number of notes */
char notes[] = "ccggaagffeeddc ";
int beats[] = { 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

void setup()
{
    /* set buzzer pin as output */
    pinMode(BUZZER_PIN, OUTPUT);
}

void loop()
{
    for(int i = 0; i < length; i++) {
        if(notes[i] == ' ') {
            delay(beats[i] * tempo);
        } else {
            playNote(notes[i], beats[i] * tempo);
        }
        delay(tempo / 2);    /* delay between notes */
    }

}

/* play tone */
void playTone(int tone, int duration) {
    for (long i = 0; i < duration * 1000L; i += tone * 2) {
        digitalWrite(BUZZER_PIN, HIGH);
        delayMicroseconds(tone);
        digitalWrite(BUZZER_PIN, LOW);
        delayMicroseconds(tone);
    }
}

void playNote(char note, int duration) {
    char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
    int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };

    // play the tone corresponding to the note name
    for (int i = 0; i < 8; i++) {
        if (names[i] == note) {
            playTone(tones[i], duration);
        }
    }
}
```
**使用 Raspberry Pi**
以下是一个简单的例子来说明如何在 Raspberry Pi 上使用 Grove-Buzzer 模块。 蜂鸣器产生噪音并延迟一秒钟。 然后安静一秒钟。让它重复上述动作。

![](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/images/GrovePi%2B_Grove_buzzer.jpg)

```python
# GrovePi + Grove Buzzer
import time
import grovepi

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8

grovepi.pinMode(buzzer,"OUTPUT")

while True:
    try:
        # Buzz for 1 second
        grovepi.digitalWrite(buzzer,1)
        print 'start'
        time.sleep(1)

        # Stop buzzing for 1 second and repeat
        grovepi.digitalWrite(buzzer,0)
        print 'stop'
        time.sleep(1)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print "Error"
```
**运行这个示例**

找到文件的路径（根据你自己的路径）
```cd GrovePi/Software/Python/
```
运行程序
```sudo python grove_buzzer.py
```

## 项目

![](https://raw.githubusercontent.com/SeeedDocument/Seeeduino_Lotus/master/img/gun.jpg)

Inspired by OVERWATCH, we have made a very cool Wooden Laser Gun toy for fun these day!

The Wooden Laser Gun and the Gun Target are all based on an Arduino board called Seeeduino Lotus. The laser emitter on the Laser Gun is controlled to fire laser pulse to "activate" the Gun Target. And there are 3 light sensors on the Gun Target to detect the laser pulse. It seems very simple right? If you are interested in our project, please make one for yourself or your child! It's worth to spend one day DIY it as a Xmas present.    

[![](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/make.png)](http://www.instructables.com/id/DIY-a-Wooden-Laser-Gun-As-a-Xmas-Present-for-Your-/)


## 资源下载
---
- [Grove - Buzzer Source Files v1.1](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/resources/Grove-Buzzer_V1.1_eagle.zip)
- [Grove - Buzzer Source Files v1.0 (Eagle and pdf)](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/resources/Grove_-_Buzzer_v1.0_Source_File.zip)
- [S9013datasheet](https://github.com/SeeedDocument/Grove_Buzzer/raw/master/resources/S9013.pdf)
- [Schematic at Easyeda](https://easyeda.com/Seeed/Grove_Buzzer_v1_2-c713baf3c1774da39ce0c995544ce5da)
