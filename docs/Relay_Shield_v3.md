---
name: Relay Shield v3.0
category: Shield
bzurl: https://www.seeedstudio.com/Relay-Shield-v3.0-p-2440.html
oldwikiname: Relay Shield v3.0
prodimagename: Relay_Shield_L_v3.0.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Relay_Shield_v3
sku: 103030009
---

---
![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Relay_Shield_L_v3.0.jpg)

Relay Shield 是一种能通过高电压和大电流的电子器件，它解决了 Arduino 无法用自身 I/O 口控制高电压或大电流的问题。

Relay Shield 有四个高品质继电器，提供 NO（常开）/ NC（常闭） 接口，有四个动态 LED 指示灯用于显示每个继电器的开/关状态，以及标准化外形尺寸，能与 Arduino / Seeeduino 板或其他 Arduino 开发板组装在一起。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.15.407e78e0WYnEcg&id=520693258153)


## 产品特性
---
- 兼容 Arudino Uno / Leonardo / Seeeduino；其他板或微控制器通过跳线来连接
- 使用了数字 4,5,6 和 7 I/O 端口
- 继电器采用螺丝端子
- 标准化屏蔽壳和设计
- 每个继电器都有 LED 工作状态指示灯
- 高品质继电器
- 每个继电器都有 COM, NO (常开), 和 NC (常闭)
- 更新引脚 SCL, SDA, IOREF, NC。

## 规格参数

|项目|	最小值	|典型值	|最大值	|单位|
|---|:---:|:---:|:---:|:---:|
|工作电压	|4.75	|5|	5.25	|VDC|
|工作电流	|8|	-|	250|	mA|
|允许开关电压|	-|	-|	35|	VDC|
|允许开关电流|	-|	-|	8|A|
|开关频率|	-|	1|	-|	HZ|
|允许通过功率|	-|	-|	70|	W|
|使用寿命|	100,000|	-|	-|周期|
|接触静电放电|-	|±4	|-|KV|
|空气静电放电|-|	±8|-|	KV|
|尺寸|-|	68.7X53.5X30.8|-|	mm|
|净重|-|	55±2|-|	g|

!!!Cautions
    1. 请在 Arduino 的 USB 端口上部放两层绝缘胶带，防止模块短路。
    2. 请不要在模块上接入超过 **35V DC** 的电压。

## 兼容性

我们生产了大量的扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有平台板兼容，我们在这里列了表格来说明这些板与平台板的兼容性。

!!!note
        请注意，“Not recommended”意味着它有可能可以与平台板工作，但需要做额外的操作，如跳线或重写代码。 如果您有兴趣挖掘更多，欢迎与 techsupport@seeed.cc 联系。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 扩展板接口说明
---

![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Relay_Shield_v3.0.png)

- 数字接口 **4** – 控制 RELAY4 的 **COM4** 接口 (位于 **J4** )
- 数字接口 **5** – 控制 RELAY3 的 **COM3** 接口 (位于 **J3** )
- 数字接口 **6** – 控制 RELAY2 的 **COM2** 接口 (位于 **J2** )
- 数字接口 **7** – 控制 RELAY1 的 **COM1** 接口 (位于 **J1** )

**J1接口/端子引脚说明：**

- **COM1 (公共端)** : 继电器的开关输入端口，受数字端口控制。

- **NC1 (常闭)**: 当 RELAY1 控制引脚（数字 **7** I/O 引脚）置为 **低电平** 且 RELAY1 控制引脚设置为高电平时，该端子将连接到 COM1 。

- **NO1 (常开)**: 当 RELAY1 控制引脚（数字 **7** I/O 引脚）置为 **高电平** 且 RELAY1 控制引脚设置为高电平时，该端子将连接到 COM1 。

**端子 J2-4 与 J1 类似，除了它们分别控制 RELAY2-RELAY4 。**

!!!Note
    需要四个 Arduino 数字 I/O 引脚（ **引脚 4-7** ）来控制四个不同的继电器。 另外还需要 **5V** 和两个 **GND** Arduino 引脚为 Relay Shield 供电。

## 继电器工作原理
---
继电器基本上就是电磁开关：当继电器由控制电路通电时（即当对线圈施加电压和电流时），电流和线圈产生磁场将 COM 端子吸引到 NO 端子， 当控制电路去除施加的电压和电流时，COM 端子由于机械力（通常是弹簧）而返回与 NC 端子接触。

一些实用的继电器应用包括：使用低电压控制高压，电机控制，遥控，自动温度报警，孵化器等等。

用一个继电器控制一个电机的电机控制应用如下所示:
![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Low_Level_Control4.jpg)

![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/High_Level_Control3.jpg)

在 Relay Shield 中，四个继电器中的每一个的两个“Control Circuit”端子仅由一个 Arduino 数字 I/O 引脚控制。 **引脚 4,5,6 和 7 分别控制继电器 4,3,2 和 1** 。

## Relay Shield 示例和用法

你知道继电器内部如何工作，现在让我们告诉你如何使用 Relay Shield。

**示例 #1: 控制直流电机**

1.把 Relay Shield 组装在 Arduino 扩展板上。

2.用 USB 电缆把 Arduino 连接到电脑。

3.我们将使用 RELAY3 来控制直流电机。按下图所示连接直流电机和 Relay Shield ，电源线接在 **COM3** 上，电机接在 **NO3** 上。

![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Motor-shield-schematic-drawing.png)

![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Relay_Shield_Connector.jpg)

!!!Note
    上图中的外部电源可以是电池或电源。 外部电源必须能够提供足够的电流并将其设置为电机的正常工作电压。在我们的示例中，我们使用锂电池作为电机的外部电源。

4.打开 Arduino IDE 并把下面的代码下载到 Arduino 中。
```
int MotorControl = 5;    // 设置 MotorControl 为电机控制引脚

// the setup routine runs once when you press reset:
void setup()  {
  // 声明引脚 5 为输出
  pinMode(MotorControl, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop()  {
  digitalWrite(MotorControl,HIGH); // NO3 和 COM3 连通 (电机运转)
  delay(1000);                     // 等待 1000 毫秒 (1 秒)
  digitalWrite(MotorControl,LOW);  // NO3 和 COM3 断开 (电机停转)
  delay(1000);
}
```

当你把程序下载到 Arduino/Seeeduino 板后，电机应该是运行一秒停转一秒，并循环往复。当电机运转时（NO3 和 COM3 连通），NO3 LED 指示灯应该会亮起。

**示例 #2: 如何使用一个 Arduino/Seeeduino 控制多个继电器**

由于 Relay Shield 使用 Arduino 上的单独数字引脚来控制每个继电器，因此控制多个 Relay Shield ，可以使用相同的Arduino板，只需按照以下步骤操作：

1.把一个 Relay Shields（称这个为 **Relay Shield #1**）插在 Arduino 开发板上。

2.把另一个 Relay Shield (称这个为 **Relay Shield #2**) 按下图所示用跳线连接 **Relay Shield #1**。

![](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/img/Two-relay-shields-one-arduino.png)

- 把 Relay Shield #1 **GND** 引脚连接到 Relay Shield #2 的 **GND** 引脚
- 把 Relay Shield #1 **5V** 引脚连接到 Relay Shield #2 的 **5V** 引脚
- 把 Relay Shield #1 的数字引脚 **8, 9, 10, 和 11** 分别连接到 Relay Shield #2 的数字引脚 **7, 6, 5, 和 4** 。

3.现在，您可以使用 Arduino 的引脚 8 , 9 , 10 和 11 来控制 Relay Shield ＃2 中的继电器 1，2，3 和 4。下面的示例代码是用于控制 Relay Shield #2 中的 RELAY1。

```
int relay1inShield2 = 8;    //Arduino 的数字 8 引脚控制 Relay Shield #2 的 RELAY1

// the setup routine runs once when you press reset:
void setup()  {
  // 声明引脚 8 为输出
  pinMode(relay1inShield2, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop()  {
  digitalWrite(relay1inShield2,HIGH); // 继电器接通 (NO 连接到 COM)
  delay(1000);                        // 等待 1000 毫秒 (1 秒)
  digitalWrite(relay1inShield2,LOW);  // NO 和 COM 断开
  delay(1000);
}
```

## 相关阅读
---
- **[常见问题]**[FAQ of Relay Shield ](http://support.seeedstudio.com/knowledgebase/articles/462030-relay-shield-sku-sld01101p)

## 资料下载
---
- **[Eagle 文件]**[Relay Shield v3.0](https://github.com/SeeedDocument/Relay_Shield_v3.0/raw/master/res/Relay_Shield_v3.0.zip)
