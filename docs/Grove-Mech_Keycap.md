---
name: Grove-Mech Keycap
category: 
bzurl: https://www.seeedstudio.com/Grove-Mech-Keycap.html
oldwikiname:
prodimagename:
wikiurl: https://wiki.seeedstudio.com/cn/Respeaker_2-Mics_Pi_HAT
sku:  111020049
---

Grove机械按键拥有一个内置LED的机械开关。255全彩色RGB LED使您可以轻松地显示开关的状态。这款钥匙帽非常可靠，使用寿命为2000万次。
这是一个有趣和稳定的模块，可以用来制作一些有趣的项目或产品。你甚至可以用数个Grove Mech制作一个机械键盘。

![2](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/2.jpg)

!!!Tips

    寿命20000000次是在每分钟300次的速度无负载的情况下测试的。

[![click_to_buy](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.10.715333dbQJ9Qzr&id=577225845793)

## 特征

- 可编程LED
- 可靠的机械结构
- 超长使用寿命

## 具体参数

| 项目 | 值 |
| ------ | ------ |
| 工作电压 | 3V-5V |
| 绝缘电阻 | 100MΩ（最小值）|
| 接触电阻最大 | 200 MΩ |
| 空载使用寿命 | 20000000 |

## 应用

- 汽车设备
- 可视设备
- 家用电器
- 信息设备

## 硬件

### 引脚图

![pin_map](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/pin_map.jpg)

### 原理图

![schametic](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/schametic.jpg)

K1对应机械按键按钮，当按键打开时，sig1被r2拉下，sig1的输出应低。一旦按下按钮，K1将关闭，SIG1将连接到VCC，SIG1的输出变高。

!!!NOTE

    在本节中，我们只向您展示部分示意图，有关完整文档，请参阅[参考资料](http://wiki.seeedstudio.com/cn/Grove-Mech_keycap/#_15)

## 支持的平台

| Arduino                                                                                             | Raspberry Pi                                                                                             | BeagleBone                                                                                      | Wio                                                                                               | LinkIt ONE                                                                                         |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![arduino_logo](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/arduino_logo.jpg) | ![raspberry_pi_logo](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/raspberry_pi_logo.jpg) | ![bbg_logo](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/bbg_logo.jpg) | ![wio_logo](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/wio_logo.jpg) | ![linkit_logo](https://raw.githubusercontent.com/SeeedDocument/wiki_english/master/docs/images/linkit_logo.jpg) |

!!!Caution

    上述支持的平台表示模块的软件或理论兼容性。在大多数情况下，我们只为Arduino平台提供软件库或代码示例。无法为所有可能的MCU平台提供软件库/演示代码。因此，用户必须编写自己的软件库。

## Arduino演示

### 硬件部分

## 启动

!!!Note

    如果这是你第一次使用Arduino,我们强烈建议你在开始前阅读[启动Arduino](http://wiki.seeedstudio.com/cn/Getting_Started_with_Seeeduino/)

### 用Arduino演示

#### 硬件部分

所需材料

| Seeeduino V4 | Grove - DHT Sensor pro | Base Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/thumbnail.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3ff19e11rndqnS&id=45721222112)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3ff19e11ek83a4&id=45754325612)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144)|

!!!note

    **1.** 请轻轻插入USB线，否则可能损坏端口。请使用内置4线的USB电缆，2线电缆无法传输数据。如果您不确定您拥有的电线，可以[单击此处购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.12.6b4f33dbNNLbE4&id=45774308858)

    **2.** 购买时，每个Grove模块都配有Grove插头。如果不慎丢失，您可以[单击此处购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.33.775d33db4mcqCz&id=45575764936)

- **Step 1.** Grove机械键帽连接到Grove底座护罩的D2端口。
- **Step 2.** Plug Grove - Base Shield into Seeeduino.

- **Step 3.** 通过USB电缆将seeeduino连接到PC。

![light1400-1050%C2%B7](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/light1400-1050%C2%B7.jpg)

!!!Note

    如果没有Grove Base Sheild，我们也可以直接连接格Grove机械键帽到seeeduino如下。

| Seeeduino     | Grove-Mech keycap       |
|---------------|-------------------------|
| 5V            | 红                     |
| GND           | 黑                      |
| D3            | 白                      |
| D2            | 黄                   |

#### 软件

- **Step 1.** 从Github下载[adafruit_neopixel-master库](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/Adafruit_NeoPixel-master.zip)

- **Step 2.** 请参阅[如何安装Arduino的库](http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library/)完成安装

- **Step 3.** 打开Arduino IDE并创建一个新文件，然后将以下代码复制到新文件中

```c++
/**
 * This is an exmaple of the Grove - Mech Keycap.
 * Every press of the key will change the color the SK6805 RGB LED. The SK6805 is a NeoPixel compatible chip.
 *
 * Credit:
 * Adafruit_NeoPixel - https://github.com/adafruit/Adafruit_NeoPixel/blob/master/COPYING
 */

#include <Adafruit_NeoPixel.h>

#define BUTTON_PIN   2    // Digital IO pin connected to the button.  This will be
                          // driven with a pull-up resistor so the switch should
                          // pull the pin to ground momentarily.  On a high -> low
                          // transition the button press logic will execute.

#define PIXEL_PIN    3    // Digital IO pin connected to the NeoPixels.

#define PIXEL_COUNT 60

// Parameter 1 = number of pixels in strip,  neopixel stick has 8
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_RGB     Pixels are wired for RGB bitstream
//   NEO_GRB     Pixels are wired for GRB bitstream, correct for neopixel stick
//   NEO_KHZ400  400 KHz bitstream (e.g. FLORA pixels)
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip), correct for neopixel stick
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

bool oldState = LOW;
uint8_t color_pos = 0;
int i=0;
int longpress=2000;
long timecheck;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  strip.begin();
  strip.clear();
  strip.show(); // Initialize all pixels to 'off'
  Serial.begin(9600);
}

void loop()
{
  
  // Get current button state.
  bool newState = digitalRead(BUTTON_PIN);

  // Check if state changed from low to high (button press).
  if (newState == HIGH && oldState == LOW) {
      timecheck = millis();
    // Short delay to debounce button.
    delay(20);
    // Check if button is still low after debounce.
    newState = digitalRead(BUTTON_PIN);
    if (newState == HIGH){
      color_pos+=8;
      strip.setPixelColor(0, Wheel(color_pos));
      strip.show();
    }
  }

 if( millis()-timecheck > 300)
 {
   if (digitalRead(BUTTON_PIN)==HIGH)
   {
 if(millis()-timecheck > longpress)
 {
  while(digitalRead(BUTTON_PIN) == HIGH)
  {
  strip.setPixelColor(0,Wheel(color_pos));
  strip.show();
  delay(300);

  strip.setPixelColor(0,0,0,0);
  strip.show();
  delay(300);
  bool newState = digitalRead(BUTTON_PIN);
  }
  strip.setPixelColor(0,0,0,0);
  strip.show();
   timecheck = millis();
 }
  }
   }

  // Set the last button state to the old state.
  oldState = newState;
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

```

- **Step 4.** 上传演示。如果您不知道如何上传代码，请检查[如何上传代码](http://wiki.seeedstudio.com/cn/Upload_Code/)

- **Step 5.** 每次按下Grove Mech键帽，您都会看到LED颜色变化。如果你按住按钮大约2秒钟，你就会看到呼吸光的效果

### 用树莓派演示

#### 硬件部分

- **Step 1**. 本项目使用的产品：

| Raspberry pi | Grove Base Hat for RasPi| Grove - Mech Keycap|
|--------------|-------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/wiki_english/raw/master/docs/images/rasp.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove_Base_Hat_for_Raspberry_Pi/raw/master/img/thumbnail.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/thumbnail.jpg)|
|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3ff19e11WKMOCW&id=528322046763)|[马上购买](https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi-p-3186.html)|[马上购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.10.715333dbQJ9Qzr&id=577225845793)|

- **Step 2**. 把Grove Base Hat插进树莓派里
- **Step 3**. 将Grove - Mech Keycap连接到Grove Base Hat的PWM端口（端口12）

!!!Note

    对于PWM功能，pin可以是pin列中的以下值之一，将设备连接到相应的插槽

|编号| 功能|
|---|---|
|18 |D18|
|12|PWM|

- **Step 4**. 将树莓pi连接到PC

![Mech_Hat](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/img/Mech_Hat.jpg)

#### 软件部分

- **Step 1**. 按照[设置软件](http://wiki.seeedstudio.com/cn/Grove_Base_Kit_for_Raspberry_Pi/#_6) 配置开发环境
- **Step 2**. 通过git clone grove.py库来下载源文件

```bash
cd ~
git clone https://github.com/Seeed-Studio/grove.py

```

- **Step 3**. 使用以下命令运行代码

```bash
cd grove.py/grove
sudo python grove_mech_keycap.py 12

```

!!! Caution

    Unix系统的“安全模组”。普通用户不能访问同一台计算机上其他人的文件，也不能关机。而“dev/mem”允许您进行更多操作，而不仅仅是更改GPIO。所以普通用户无权访问/dev/mem。因此，为了运行此代码，应该在命令行中键入**sudo python grove_mech_keycap.py*

下面是grove_mech_keycap.py代码

```python

import time
from grove.button import Button
from grove.factory import Factory

class GroveKeycap(object):
    def __init__(self, pin):
        # High = pressed
        self.__btn = Factory.getButton("GPIO-HIGH", pin)
        # single WS2812 LED
        self.__led = Factory.getOneLed("WS2812-PWM", pin + 1)
        self.__on_event = None
        self.__btn.on_event(self, GroveKeycap.__handle_event)

    @property
    def on_event(self):
        return self.__on_event

    @on_event.setter
    def on_event(self, callback):
        if not callable(callback):
            return
        self.__on_event = callback

    def __handle_event(self, evt):
        # print("event index:{} event:{} pressed:{}".format(evt['index'], evt['code'], evt['presesed']))
        if callable(self.__on_event):
            self.__on_event(evt['index'], evt['code'], evt['time'])
            return

        self.__led.brightness = self.__led.MAX_BRIGHT
        event = evt['code']
        if event & Button.EV_SINGLE_CLICK:
            self.__led.light(True)
            print("turn on  LED")
        elif event & Button.EV_DOUBLE_CLICK:
            self.__led.blink()
            print("blink    LED")
        elif event & Button.EV_LONG_PRESS:
            self.__led.light(False)
            print("turn off LED")


Grove = GroveKeycap

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.PWM)
    pin = sh.argv2pin()

    ledbtn = GroveKeycap(pin)

    # remove ''' pairs below to begin your experiment
    '''
    # define a customized event handle your self
    def cust_on_event(index, event, tm):
        print("event with code {}, time {}".format(event, tm))

    ledbtn.on_event = cust_on_event
    '''
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()


```

!!!success

    如果一切顺利，您将能够看到以下结果。如果您单击键帽，您将看到“打开LED”，如果您双击键帽，您将看到“闪烁LED”。长按键盖将发出“关闭LED”。

```bash

pi@raspberrypi:~/grove.py/grove $ sudo python grove_mech_keycap.py 12
Hat Name = 'Grove Base Hat RPi'
turn on  LED
turn on  LED
blink    LED
turn on  LED
turn off LED
^CTraceback (most recent call last):
  File "grove_mech_keycap.py", line 98, in <module>
    main()
  File "grove_mech_keycap.py", line 94, in main
    time.sleep(1)
KeyboardInterrupt


```

只需按ctrl+c即可退出此程序


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/Grove-Mech_Keycap_eagle.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源

- **[Zip]** [Grove-Mech Keycap eagle file](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/Grove-Mech_Keycap_eagle.zip)
- **[Zip]** [Adafruit_NeoPixel-master](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/Adafruit_NeoPixel-master.zip)
- **[PDF]** [Product brief of the swith](https://github.com/SeeedDocument/Grove-Mech_Keycap/raw/master/res/DIP_Mech_Key.pdf)

## 技术支持

访问我们的 [论坛](https://forum.seeedstudio.com/)
