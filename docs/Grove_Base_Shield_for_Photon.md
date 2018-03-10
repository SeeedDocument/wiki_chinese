---
title: Grove Base Shield for Photon
category: Shield
bzurl: https://www.seeedstudio.com/Particle-Photon-Base-Shield-p-2598.html?cPath=98_106_57
oldwikiname:  Grove Base Shield for Photon
prodimagename: Grove_Base_Shield_for_Photon_product_view_1200_s.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove_Base_Shield_for_Photon
sku:  103020031
---
![](https://github.com/SeeedDocument/Grove_Base_Shield_for_Photon/raw/master/img/Grove_Base_Shield_for_Photon_product_view_1200_s.jpg)

Photon Grove Base Shield 是一款集成了 [Grove](sudo apt install python-gi gir1.2-gstreamer-1.0) 端口的扩展板，，您可以利用 Grove 接口构建功能更强大，更具成本效益的 Grove 功能模块，从而构建更强大，更智能的应用。它有三个数字端口，两个模拟端口，两个 I2C 端口和一个 UART 端口。它是一种即插即用的扩展板，可以大幅加速您的原型制作过程。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.4c34c1f5ruuYzj&id=531559461174)

##  产品特性
---
*   兼容 Grove 接口

*   可以连接到大量低成本的 Grove 模块

*   集成 I<sup>2</sup>C, UART 端口

##  创意应用
---
*   例如智能路由器等的紧凑型 IOT 应用。

##  规格参数
---
<table>
<tr>
<td> Grove 接口 </td>
<td> 3 个数字接口，

2 个模拟端口，

2 个 I<sup>2</sup>C 接口，

1 个 UART 接口

</td></tr>
<tr>
<td> 尺寸  </td>
<td> 53  × 53 mm
</td></tr>
<tr>
<td> 重量  </td>
<td> 18 g
</td></tr></table>

##  硬件概述
---
![](https://github.com/SeeedDocument/Grove_Base_Shield_for_Photon/raw/master/img/Grove_Base_Shield_for_Photon_component_diagram_annotated_1200_s.jpg)

###  **包装清单**

<table>
<tr>
<th>部件名称   </th>
<th> 数量
</th></tr>
<tr>
<td> Grove Base Shield for Photon  </td>
<td> 1 片
</td></tr></table>

##  入门指导
---
!!!Note
    在这个例子中，我们会展示一个很普通的应用。

###  需求材料

*   [Particle Photon](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.6b0797bc0szdqk&id=527442781665) × 1

*   [USB 线 (type A 转 micro type-B)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.38.72e7f435sItuSO&id=45774308858) × 1
*   一台电脑

*   [Grove Base Shield for Photon](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.61b4c0a8i33hZv&id=531559461174) × 1

*   [Grove - Buzzer](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.5c4142c61eYvm5&id=520245748676) × 1

###  操作蜂鸣器

<dl><dd> 1. 请参考 [这里](https://docs.particle.io/guide/getting-started/connect/core/) 来链接设备与电脑。
</dd></dl>

!!!Note
    1. 我们建议您选择 **node.js v4.2.3 LTS** ，尤其是 Windows 10 用户。
    2. 在运行命令 **particle setup** 之后，在您的电脑上连接名称中包含 **Photon** 的 Wifi 热点，特别是在Windows 10上。

<dl><dd> 2. 使用 [Web IDE](https://build.particle.io/) 开发您的项目。用您的账户登录并选择您的设备（点击左栏第二个图标）。
</dd></dl>

!!!Note
    如果您的网络连接不太好，我们建议您选择 [Web IDE](https://build.particle.io/) 来编译或者将代码上传到 Photon，这比使用 Particle Dev 快得多。

<dl><dd> 3. 按下图所示连接部件：
</dd></dl>

![](https://github.com/SeeedDocument/Grove_Base_Shield_for_Photon/raw/master/img/Grove_Base_Shield_for_Photon_demo_conneciton_1200_S.jpg)

<dl><dd> 4. 现在您可以复制下面的代码到 Web IDE，并通过单击一个类似灯光的图标（左栏第一个图标）将它们上传到 Photon。
</dd></dl>

!!!Note
    将代码复制到名为 _**filename.ino**_ 的选项卡。

```c
/*
   Buzzing
   Use digital pin D4
   This example code is in the public domain.
   by xiaohe
  */
int led1 = D4; //set D4 as output

void setup() {
    pinMode(led1, OUTPUT);
}

void loop() {
    // enable buzzing
    digitalWrite(led1, HIGH);

    // We'll leave it on for 1 second...
    delay(1000);

    // Then we'll turn it off...
    digitalWrite(led1, LOW);

    // Wait 1 second...
    delay(1000);

    // And it will repeat!
}
```

##  资源下载
---
*   **[原理图]**[Schematic files](https://github.com/SeeedDocument/Grove_Base_Shield_for_Photon/raw/master/res/Schematic_files_for_Grove_Base_Shield_for_Photon.zip)

*   **[参考链接]**[Grove_System](http://wiki.seeedstudio.com/cn/Grove_System/)
