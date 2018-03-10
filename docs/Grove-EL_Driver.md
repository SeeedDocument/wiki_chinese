---
title: Grove - EL Driver
category: Actuator
bzurl: https://seeedstudio.com/Grove-EL-Driver-p-2269.html
oldwikiname: Grove_-_EL_Driver
prodimagename: Grove-EL_Driver.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-EL_Driver
sku: 105020005
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EL_Driver/master/img/Grove-EL_Driver.jpg)

Grove - EL Driver 是专门驱动 EL 灯片的驱动器。它集成了一个非常小的逆变器来驱动 EL 灯片，只需一根 Grove 导线即可轻松点亮 EL 灯片。



[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.26d81fe8snVnnB&id=531816002922)

版本变更
---------------

| 版本 | 描述           | 发行日期      |
|----------|------------------------|--------------|
| v1.0     | 首次公开发布 | 十二月 11, 2014 |


#### **支持 EL 灯片：**

-   [EL Wire-Green 3m](http://www.seeedstudio.com/depot/EL-WireGreen-3m-p-1102.html)
-   [EL Wire-Red 3m](http://www.seeedstudio.com/depot/EL-WireRed-3m-p-1129.html)
-   [EL Wire-Blue 3m](http://www.seeedstudio.com/depot/EL-WireBlue-3m-p-1128.html)
-   [EL Wire-Yellow 3m](http://www.seeedstudio.com/depot/EL-WireYellow-3m-p-1127.html)
-   [EL Wire-White 3m](http://www.seeedstudio.com/depot/EL-WireWhite-3m-p-1130.html)

产品特性
--------

-   兼容 Grove 接口
-   兼容 3.3V / 5V
-   集成变频器
-   输入电流：最大300mA（根据负载决定）
-   支持最大EL电容：15nF

!!!Tip
    有关 Grove 模块的更多细节请参阅 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)

使用方法
-----

这里我们展示如何使用 Arduino 来控制 EL 灯片的状态。

1. 将 Grove - EL Driver 连接到 Base Shield 的 **D2** 接口。如果有必要，您可以更改为其他有效的数字端口，并且也应该更改端口的定义。使用产品包装中的给定的 EL 线把 EL 灯片连接到 EL 驱动器的 **J1** 端口，使用产品包装中的给定电缆。

2. 把驱动器插入 Arduino / Seeeduino。使用 USB 电缆将电路板连接到 PC。

3. 将演示代码复制到 Arduino IED，然后上传到 Arudino 或 Seeeduino 板。你会看到 EL 灯片开始闪烁。

```
/*************************   2014 Seeedstudio   **************************
* File Name          : GroveELDriverDemoCode.ino
* Author             : Seeedteam
* Version            : V1.0
* Date               : 11/12/2014
* Description        : Demo code for Grove - EL Driver
*************************************************************************/
 
#define ELPin 2 //connect EL Driver to digital pin2
void setup() {                
  // initialize the digital pin2 as an output.
  pinMode(ELPin, OUTPUT);     
}
 
void loop() {
  digitalWrite(ELPin, HIGH);   // set the EL Wire on
  delay(500);               // for 500ms
  digitalWrite(ELPin, LOW);   // set the EL Wire off
  delay(500);
}
```

![](https://raw.githubusercontent.com/SeeedDocument/Grove-EL_Driver/master/img/Grove-EL_Driver_usage.jpg)

资源下载
---------

- **[Eagle 文件]**[sch_pcb_eagle](https://raw.githubusercontent.com/SeeedDocument/Grove-EL_Driver/master/res/Grove-EL_Driver_v1.0.zip)
-   **[PDF 文件]**[sch_pdf](https://raw.githubusercontent.com/SeeedDocument/Grove-EL_Driver/master/res/Grove-EL_Driver_v1.0.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_EL_Driver -->
