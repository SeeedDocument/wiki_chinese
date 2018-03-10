---
title: Grove Base Cape for BeagleBone v2
category: BeagleBone
bzurl: https://www.seeedstudio.com/Grove-Base-Cape-for-Beaglebone-v2.0-p-2644.html
oldwikiname:  Grove Base Cape for BeagleBone v2
prodimagename: Grove_Base_Cape_for_BeagleBone_v2_product_view_1200.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Base_Cape_for_BeagleBone_v2
sku:  103030035
---

![](https://github.com/SeeedDocument/Grove_Base_Cape_for_BeagleBone_v2/raw/master/img/Grove_Base_Cape_for_BeagleBone_v2_product_view_1200.jpg)

**Grove Base Cape for BeagleBone** v2 是用于 BeagleBone 平台的 [Grove system](/Grove_System) 扩展板。这个扩展板可以方便地将许多转换器(传感器和执行器)作为 Grove 模块与 BeagleBone 平台连接。该板还包括一个 256kb Serial EEPROM。在无焊设计和紧凑的即插即用端口的产品开发过程中，将为您节省大量的工作量。

扩展板提供了 12 个易于使用的 Grove 连接器，可与广大的 Grove 模块实现即插即用。连接器包括 2x UART，2x ADC，4x Digital I/O 和 4x I2C，它们与 Beaglebone 板上的引脚相连，提供几乎所有你需要的东西。在地址冲突的情况下，有两个开关用于重置 I2C 地址。该电路板还集成了一个电压转换开关 - 从 5V 到 3.3V。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.15.5de8fe29eump0C&id=533254309967&ns=1&abbucket=1#detail)


##  产品特性
---
*   BeagleBone 与 Grove 模块间的连接更简单
*   无焊
*   省时省钱

##  规格参数
---
<table>
<tr>
<td> 输出电压 </td>
<td> 3.3 V or 5 V(switchable)
</td></tr>
<tr>
<td>  最大输出电流 </td>
<td> 500 mA at 3.3V, 500 mA at 5V
</td></tr>
<tr>
<td> 数字 Grove 端口 </td>
<td> 6 , 与 UART1 和 UART4 共用引脚
</td></tr>
<tr>
<td> 模拟 Grove 端口 </td>
<td> 2
</td></tr>
<tr>
<td> I<sup>2</sup>C Grove 端口 </td>
<td> 4
</td></tr>
<tr>
<td> UART Grove 端口 </td>
<td> 2 (UART1, UART4)
</td></tr>
<tr>
<td> EEPROM </td>
<td> 256kb (Model: CAT24C256WI)
</td></tr>
<tr>
<td> 尺寸 </td>
<td> 70 mm(Length) × 50 mm(width)
</td></tr></table>

###   产品清单
<table>
<tr>
<th>产品名称   </th>
<th> 数量
</th></tr>
<tr>
<td>Grove Base Cape for BeagleBone v2 </td>
<td> 1 PCS
</td></tr></table>

##  硬件概述
---
![](https://github.com/SeeedDocument/Grove_Base_Cape_for_BeagleBone_v2/raw/master/img/Grove_Base_Cape_for_BeagleBone_v2_hardware_overview_1200.jpg)

**Output voltage switch**，控制 Grove 端口输出电压的开关。

**USER button**， 可用作 BeagleBone 用户自定义按键。

**Cape address switch**，是一个选择扩展板地址的开关(使用多个扩展板时有用)，以避免 I2C 地址冲突。 有关使用多个扩展板的详细信息，请访问 [http://beagleboard.org/Support/bone101/#capes](http://beagleboard.org/Support/bone101/#capes) 和 [http://elinux.org/BeagleBone_Community#Capes](http://elinux.org/BeagleBone_Community#Capes)。您可以使用此开关选择从 **00** (二进制) 至 **11** (二进制) 的地址，对应于所有扩展板的 0x54 到 0x57。

**Write protection pin**，引脚连接的情况下禁用扩展板的 EEPROM 的写入保护。默认情况下，它没有连接。

**LMV324 operational amplifier **，是一款低电压轨对轨输出运算放大器，用于控制模拟电压。[更多信息点击这里](http://www.ti.com/lit/ds/symlink/lmv324.pdf)

**TXB0108PW**，是一个 8 位双向电压电平转换器。[更多信息点击这里](http://www.electroensaimada.com/uploads/9/0/8/9/9089783/txb0108.pdf).

!!!Note
    您可以在 Grove Base Cape for BeagleBone v2.0 的一端找到两个凹槽(带孔的圆角)。这对应于 BeagleBone Green 上的相同凹槽。您可以使用这些凹槽来确保正确的安装方向。

##  入门指导

在本节中，我们将向您展示使用此板的基本示例。您可以在 [BeagleBone Recipes](http://www.seeedstudio.com/recipe/index.php?query=beaglebone) 页面找到更多的演示。只需将 Grove Base Cape for BeagleBone v2 添加到这些项目中，便于连接线缆。

###  参考资料

*   [BeagleBone Green](/BeagleBone_Green)

*   [BeagleBone community](http://beagleboard.org/)

*   [BeagleBone 101](http://beagleboard.org/support/bone101)

*   [BoneScript](http://beagleboard.org/support/bonescript)

###  所需材料

*   Grove Base Cape for BeagleBone v2 × 1

*   [Grove - Button](https://www.seeedstudio.com/item_detail.html?p_id=766) × 1

*   [BeagleBone Green](https://www.seeedstudio.com/item_detail.html?p_id=2504) (无 HDMI 输出下完全与 BeagleBone Black 兼容)

*   USB 线缆 (用于 Arduino 的 A 型口 至 B型口) × 1 或 USB 线缆 (用于 Seeeduino 的 A型口 至 micro B型口) × 1

*   [Grove cable](http://www.seeedstudio.com/depot/Grove-Universal-4-Pin-Buckled-5cm-Cable-5-PCs-Pack-p-925.html?cPath=98_106_57) × 1

###  编程工作

1.通过 USB 线缆将 BeagleBone Green 连接到您的 PC 或 MAC。 点击[http://192.168.7.2:3000/ide.html](http://192.168.7.2:3000/ide.html) 打开 Cloud9 IDE。</dd></dl>

2.通过 Grove 线缆将 Grove - Button(P) 连接到 BeagleBone v2 的 Grove Base Cape。将 Grove 线缆连接到 GPIO 引脚 **51**。
![](https://github.com/SeeedDocument/Grove_Base_Cape_for_BeagleBone_v2/raw/master/img/Grove_Base_Cape_for_BeagleBone_v2_wiki_demo_1200.jpg)
</dd></dl>

3.将以下代码复制到 Cloud9，将其保存为 **.js** 文件。
```
var b = require('bonescript');
b.pinMode('P9_16', b.INPUT);//GPIO 51 correspond to P9_16. More details at http://beagleboard.org/Support/bone101/#headers

setInterval(check,1000);

function check(){
    b.digitalRead('P9_16', checkButton);
}

function checkButton(x) {
    console.log(x.value);
    if(x.value == 1){
        console.log("you are pressing Grove button");
    }
    else{
        console.log("you are not pressing Grove button");
    }
}
```

4.单击 Cloud9 IDE 中的 **Run** 在 BeagleBone Green 上运行该程序。


5.等待大约 10 秒钟，查看 Cloud9 IDE 的输出。输出结果可能像下面的屏幕截图 :


![](https://github.com/SeeedDocument/Grove_Base_Cape_for_BeagleBone_v2/raw/master/img/Grove_Base_Cape_for_BeagleBone_v2_wiki_demo_result_600_s.png)

##  资源下载
---
*   **[Eagle文件]** [EAGLE Schematic &amp; PCB files and PDF format Schematic](https://github.com/SeeedDocument/Grove_Base_Cape_for_BeagleBone_v2/raw/master/res/Grove_Base_Cape_for_BeagleBone_v2.0_Schematics.zip)

*   **[芯片数据手册]** [TXB0108PW datasheet](http://www.electroensaimada.com/uploads/9/0/8/9/9089783/txb0108.pdf)

*   **[芯片数据手册]** [LMV324 datasheet](http://www.ti.com/lit/ds/symlink/lmv324.pdf)

*   **[其他资源]** [BeagleBone Green](/BeagleBone_Green)

*   **[其他资源]** [BeagleBone community](http://beagleboard.org/)

*   **[其他资源]** [BeagleBone 101](http://beagleboard.org/support/bone101)

*   **[其他资源]** [BoneScript](http://beagleboard.org/support/bonescript)

*   **[其他资源]** [Cloud9](https://c9.io/)

*   **[其他资源]** More demos at [http://www.seeedstudio.com/recipe/index.php?query=beaglebone](http://www.seeedstudio.com/recipe/index.php?query=beaglebone) and [http://www.seeedstudio.com/recipe/index.php?query=beaglebone](http://www.seeedstudio.com/recipe/index.php?query=beaglebone)
