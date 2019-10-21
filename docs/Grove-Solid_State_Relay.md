---
name: Grove - Solid State Relay
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-Solid-State-Relay-p-1359.html
oldwikiname: Grove - Solid State Relay
prodimagename: Grove_Solid_State_Relay_1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Solid_State_Relay
sku: 103020004
---
![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Grove_Solid_State_Relay_1.jpg)


Grove – Solid State Relay 是具有继电器特性的非接触式电子开关模块。 它基于 S208T02 设计，最大输出为 250VAC/4A，开关速度小于 10ms。 该模块配备了丙烯酸基底和 3D 打印的绝缘护罩来保证用户的安全。继电器接通时有 LED 指示。 可广泛应用于计算机外围接口，温度/速度/调光，伺服控制，石油化工，医疗仪器，金融设备，煤炭，仪表，交通信号灯等各个领域。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.40.10356727aFwCxE&id=45507430313)
## 产品特性
---
- 3D 打印的绝缘保护护罩
- 兼容 3.3V 和 5V 控制电平
- 低开关延迟（≤10ms）
- LED 指示灯
- 有散热器提供更好的稳定性
- 丙烯酸基和绝缘纸增加安全性能
- 兼容 Grove

!!!Tip
    关于 Grove 模块的更多细节请参考 [Grove System](http://wiki.seeed.cc/Grove_System/)


## 创意应用
---

- 需要低开关延迟的操作场合，例如舞台灯光控制
- 需要高稳定性的装置，例如医疗器械，交通信号灯
- 需要防爆，防腐，防潮的情况。 如煤炭，化工等行业。

## 规格参数
---
|项目	|最小值	|典型值	|最大值	|单位|
|---|---|---|---|---|
|输入电压|	3.0|3.3|5.0|VDC|
|输入电流|	16|20|50|mA|
|输出电压	|-|220|250|VAC|
|输出电流	|--|--|4.0|A|
|工作频率|45|50|65|Hz|
|工作温度|-25|25|85|℃|
|闭合时间	|--|10|--|ms|
|断开时间	|--|10|--|ms|
|尺寸	|-|44x44x32|-|mm|
|净重	|-|25.5|-|g|

## 接口功能
---
![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Ssr_interface.jpg)

!!!Cautions
    1. 如果输出电压高于 36V，则在转动螺丝之前，需要确保模块处于关闭状态。
    2. 散热器可能处于非常高的温度，使用时请勿触摸。


## 使用方法

**使用 Arduino**

Grove - Solid State Relay 有各种应用。 这里我们详细说明如何使用它来控制灯泡。

首先，你需要按如下所述连接 Arduino:

1. 使用 Grove 4 pin 电缆把 Grove - Solid State Relay 连接到 Grove-Base Shield 的 **D13** 端口。
2. 将 Grove-Base Shield 插在 Arduino 上，并通过 USB 电缆将 Arduino 连接到电脑。
3. 将灯泡连接到 Grove - Solid State Relay 的 **OUTPUT**。

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Grove_-_SSR2.JPG)

您需要上传以下代码。 如果你不知道如何上传代码，请点击 [这里](http://wiki.seeedstudio.com/wiki/Upload_Code) 。

```
/*
  Grove - Solid State Relay 示例代码
  ssr 会打开 5 秒然后关闭 5 秒，并循环。
  http://www.seeedstudio.com
*/

int ssrControlPin = 13;
void setup() {
    // 初始化数字引脚作为输出
    pinMode(ssrControlPin, OUTPUT);
}

void loop() {
    digitalWrite(ssrControlPin, HIGH);      // 把 ssr 打开
    delay(5000);                            // 等待 5 秒
    digitalWrite(ssrControlPin, LOW);       // 把 ssr 关闭
    delay(5000);                            // 等待 5 秒
}
```

上传代码后, 你会看到灯泡先亮 5 秒然后熄灭 5 秒，并循环下去。

**使用 Raspberry Pi**

1 你应该有一个 Raspberry pi 和一个 Grovepi 或 Grovepi+.  
2 您应该已经完成配置开发环境，否则按照 [这里](http://wiki.seeedstudio.com/wiki/GrovePi+#Introducing_the_GrovePi.2B) 配置。  
3 连接 - 使用 Grove 电缆将传感器连接到 Grovepi 的插座 D4。  
4 跳转到演示目录:  

```
cd yourpath/GrovePi/Software/Python/
```

- 看代码

```
   nano grove_solid_state_relay.py   # "Ctrl+x" to exit #
```

```
import time
import grovepi

# Connect the Grove Solid State Relay to digital port D4
# CTR,NC,VCC,GND
relay = 4

grovepi.pinMode(relay,"OUTPUT")

while True:
    try:
        # switch on for 5 seconds
        grovepi.digitalWrite(relay,1)
        print "on"
        time.sleep(5)

        # switch off for 5 seconds
        grovepi.digitalWrite(relay,0)
        print "off"
        time.sleep(5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print "Error"
```

5 运行演示。  

```
   sudo python grove_solid_state_relay.py
```

## 测试结果
---
**1.实验目的**
- Grove – Solid State Relay(S208T02) 的散热性能。
- Grove – SSR 的极限负载电流。
- 提高极限载荷电流的措施。

**2.实验原理**

通过记录不同电流和不同时间点的 SSR 芯片温度，分析数据并得出结论。

图 1 是 S208T02 数据表的截图，可以看出，在不同散热片和不同温度下，SSR 的电流不同。

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Figure_1.jpg)

这里需要一个温度传感器来获得芯片的温度。 我使用 DS18B20，其检测范围为 -25-125℃，可以满足要求。

图 2 显示了实验设备和安装方案，将温度传感器连接到散热器的右侧，使18b20检测到的温度尽可能接近散热器温度，传感器和散热器之间使用热塑性塑料。 散热片和SSR之间使用热塑性塑料涂层。 因此，18b20的温度等于SSR的温度。

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Grove-ssr-report-image2.JPG)

**3.实验数据**

|电流	|1 分钟	|5 分钟|	10 分钟|	20 分钟	|稳定时间|
|---|---|---|---|---|---|
|0.5A|	31.40|	33.75	|34.75|	35.00	|15  分钟|
|1A|	31.8	|36.75	|39.6|	40.56	|18 分钟|
|2A|	34.5|	46.6|	48.88	|51.13	|20 分钟|
|3A	|35.56|	52.81|	58.88	|60.06|	17 分钟|
|4A|	38.00	|57.88|	63.88	|67.00	|19 分钟|
|5A|	44.00|	66.00|	73.12|	75.37|	19 分钟|

!!!Note
    1. 表中温度单位为℃
    2. 室温为28℃

**4.扩展实验**

  为了证明提高散热器的散热性能将提高SSR限制工作电流，我做了一个扩展实验。

  因为我手上没有更大的散热器，所以我在SSR上安装了一个风扇（从我电脑的 CPU 上拿下来的）。 如图 3 所示。

![](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/img/Grove-ssr-report-image3.JPG)

我只测试不同工作电流的稳定温度，如表 2 所示。

|-|	6.0A|	6.5A	|7.0A|	7.5A|
|---|---|---|---|---|
|稳定温度|	54.44℃|	57.63℃	|60.06℃|	62.38℃|

**5.结论**

  从上述实验结果可以得出以下结论：

  - 当电流固定时，随着时间的推移，温度将稳定在一定值。 该值与当前状态相关，电流增加，稳定后的温度也增加。 在2A电流时，温度稳定在 50℃ 以上，所以不要在 SSR 工作时碰它。

  - 结合图 1 和我们的数据，我认为 Grove-SSR 的最大负载电流为 4A。

  - 如果负载电流大于 5A，如 7A，你应该安装其他的降温设备，但并不推荐。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/Ssr_eaglefile.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


## 资源下载
---
- **[Eagle 文件]**[Grove - Solid State Relay Eagle File](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/Ssr_eaglefile.zip)
- **[代码]**[Grove - Solid State Relay Demo Code](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/SSR_Demo_Code.rar)
- **[数据手册]**[S208T02 Datasheet](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/S208t02_datasheet.pdf)
- **[PDF文件]**[Grove - Solid State Relay in PDF](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/SSR_v0.9b.pdf)
- **[实验报告]**[Grove - Solid State Relay Test Report](https://github.com/SeeedDocument/Grove-Solid_State_Relay/raw/master/res/Grove-SSR_Test_Report_V0.3.pdf)
