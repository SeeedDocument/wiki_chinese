---
name: Grove - Protoshield
category: Communication
bzurl: https://www.seeedstudio.com/Grove-Protoshield-p-772.html
oldwikiname:  Grove - Protoshield
prodimagename: Proto1.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Protoshield/
sku:  101020035
---
![](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/img/Proto1.jpg)

该 Grove 模块允许您将自己的电路或组件添加到您的 Grove 系统原中。它可以访问 Grove 连接线 - **S0**，**S1**，**VCC** 和 **GND** 的所有四条线路。还保留了一个常开按钮的安装空间。可以很方便地把标准 2.54mm 间距的普通的 DIP 封装 IC 和其他组件安装到这个模块上。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.45a7b93mjl5aJ&id=534675965071)

##  产品参数
---
*   标准化 Grove 接口
*   面包板风格
*   2.54mm 标准间距
*   有丝印标签
*   保留了常用按钮的安装空间

##  接口
---
![](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/img/Grove-Protoshield_Interface_1.jpg)

Grove 接口的 **VCC** 和 **GND** 被模块边缘两条总线输出，如图所示。你可以在两条电源总线中间看到 **Sig0** 和 **Sig1** 的焊盘。

##  使用方法
---
Grove 接口的 VCC 和 GND 作为两个总线被输出，如上所示。您可以在两条电源总线之间找到用白线标记的 Sig0 和 Sig1 的焊盘。
右侧的正方形区域是一个普通的临时按钮插孔，您可以轻松地将按钮其插入其中，如下所示。

![](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/img/Protoshield1.jpg)

此外，Protoshield 还附带两个 20 针公头。当您需要在其他面包板或扩展板上进行扩展时，您可以将它们分解成较小的部件并将其焊接到 Protoshield 上。他们与常规的面包板具有很好的兼容性。

![](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/img/Protoshield2.jpg)

**示例：点亮 LED 灯**

1. 把 LED 的 **长引脚** 插入 **VCC** 插口，**短引脚** 插入 **Sig0** 插口。

2. 把 LED 焊接在 Protoshield 上。
![](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/img/Proshield3.jpg)

3. 把模块用 4-pin Grove 连接线连接到 Grove - Basic Shield 的 **D8** 端口。

4. 把 Grove - Basic Shield 组装到 Arduino 上，然后用 USB 电缆把 Arduino 连接在电脑上。

5. 把下面代码粘贴到 Arduino IDE 的新窗口中并上传。如果你不知道如何上传代码，请点击[这里](http://wiki.seeedstudio.com/wiki/Upload_Code)。

```
//示例代码：
int led = 8;

// the setup routine runs once when you press reset:
void setup() {
    // 初始化引脚作为输出
    pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
    digitalWrite(led, HIGH);   // 点亮 LED (HIGH 代表高电平)
    delay(1000);               // 等待一秒
    digitalWrite(led, LOW);    // 输出低电平来熄灭 LED 灯
    delay(1000);               // 等待一秒
}
```


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://github.com/SeeedDocument/Grove-Protoshield/raw/master/res/Grove-Protoshield_v1.0_Source_File.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


##  资料下载
---
- **[Eagle 文件]**[Grove_-_Protoshield Eagle File](https://github.com/SeeedDocument/Grove-Protoshield/raw/master/res/Grove-Protoshield_v1.0_Source_File.zip)
