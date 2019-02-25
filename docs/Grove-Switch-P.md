---
name: Grove - Switch(P)
category: Sensor
bzurl: https://seeedstudio.com/Grove-Switch(P)-p-1252.html
oldwikiname: Grove_-_Switch(P)
prodimagename: GroveSwitchP_01.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Switch-P
sku: 101020004
tags: grove_digital, io_3v3, io_5v, plat_duino, plat_linkit, plat_pi, plat_bbg
---

<table>
    <tr>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Switch-P/master/img/SwitchP.jpg"></td>
        <td><img src="https://raw.githubusercontent.com/SeeedDocument/Grove-Switch-P/master/img/GroveSwitchP_01.jpg"></td>
    </tr>
</table>

这个 Grove - Switch(P) 是一个迷你 SPDT 部件，非常适合运用在 “开/关” 情况中。 这是一个可靠的高质量部件，我们在许多板子上使用它。 您应该为您的 Grove 开发制作系统购置一些。

“P” 是什么意思？  “P” 用于本产品中的 “面板安装” 。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.390686a76gl5mN&id=538862309682)

产品特性
-------

- Grove 接口
- 使用方便
- 基础 Grove 部件

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)

支持平台
-------------------

使用方式
-----

下面是一个简单的示例，显示如何使用开关打开/关闭 LED 。工作原理和使用方式与 [Grove-Button](/Grove-Button) 相同。

1. 将 Grove-LED 连接到 Grove-Basic Shield 的 数字端口 **13** ，并使用两根 Grove 连接线将 Grove -Switch（P） 连接到 [Grove-Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的 数字端口 **2**。
2. 将 Grove-Base Shield 连接到 Arduino ，并使用 USB 数据线将 Arduino 连接到 PC 。
3. 将下面的代码复制并粘贴到新的 Arduino 代码段上。

```
// constants won't change. They're used here to
// set pin numbers:
const int switchPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int switchState = 0;         // variable for reading the pushbutton status

void setup() {
    // initialize the LED pin as an output:
    //pinMode(ledPin, OUTPUT);
    // initialize the switch pin as an input:
    Serial.begin(9600);
    pinMode(switchPin, INPUT);
}
void loop(){
    // read the state of the switch value:
    switchState = digitalRead(switchPin);

    if (switchState == HIGH) {
        // turn LED on:
        // digitalWrite(ledPin, HIGH);
        Serial.println("switch high!");
    }
    else {
        // turn LED off:
        // digitalWrite(ledPin, LOW);
        Serial.println("switch low");
    }
}

```

上传代码后，当开关处于 **high** 端时，您可以看到 LED 将亮起。

资源下载
--------

- [Grove - Switch(P) Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Switch-P/master/res/Grove-Switch-P-Eagle_File.zip)
- [Schematic at Easyeda](https://easyeda.com/Seeed/Grove_SwitchP-434f7707edf74f3c8eb0c4748fdccc5f)
<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Switch(P) -->
