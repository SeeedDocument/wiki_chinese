---
name: Grove - Hall Sensor
category: Sensor
bzurl: https://seeedstudio.com/Grove-Hall-Sensor-p-965.html
oldwikiname: Grove_-_Hall_Sensor
prodimagename: Grove-Hall_Sensor_New.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Hall_Sensor
sku: 101020046
tags: grove_digital, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/img/Grove-Hall_Sensor_New.jpg)

Grove - Hall Sensor 基于霍尔效应，霍尔效应是横跨导体中的电流和垂直于电流的磁场产生电导体上的电压差。 这个 Grove 有一个 continuous-time 开关。 当垂直于霍尔传感器的磁场（南极性）超过最大值 BOP 时，这些设备的输出切换为低电平（导通），并且当磁场消失时，它会切换高电平（关闭）。 该部件可用于测量 RPM 。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.15f3e5efluXnfn&id=45555333014)


版本更新
---------------

| 版本调整 | 描述         | 发布日期    |
|----------|------------------------|------------|
| v0.9b    | 首次公开发行 | 2011年10月3日|


产品特性
--------

- Grove 兼容接口
- 有 400ns 的上升和下降过渡期。
- 高续航能力霍尔传感器
- 反接电池保护

!!!Tip
    关于Grove模块的更多细节请参考 [Grove System](http://wiki.seeedstudio.com/cn/Grove_System/)


规格参数
-------------

| 项目                 | 最小值 | 标准值 | 最大值 |单位 |
|-----------------------|-----|---------|-----|------|
| 电源电压       | 3.8 | 5.0     | 24  | V    |
| 电源电流       | 4.1 | -       | 24  | mA   |
| 工作温度 | -40 | -       | 85  | ºC   |

支持平台
-------------------

创新应用
-----------------

- 转速仪表。
- 简单直流电机。

入门
---------------

 Grove - Hall Sensor 通过利用 arduino / seeeduino 上可用的外部端口来使用。 在这个例子中，我们使用数字引脚 **2** 上的端口 **0** 。对于其他端口，请参阅 [attachInterrupt()](http://www.arduino.cc/en/Reference/AttachInterrupt)。

- 使用有 4 个引脚的连接线将 Grove - Hall Sensor 连接到 [Grove - Base Shield](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.3ff19e11crrag2&id=520233320144) 的数字端口 **2** ，并将 Grove-LED 连接到数字端口 **4** 。
- 然后使用 USB 数据线将 Arduino 连接到 PC 。
- 下载 [霍尔传感器代码](https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/res/Grove-Hall_Sensor_Demo_Code.zip)
- 打开两个代码之一。 例如演示 **MagnetControlLED**

![](https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/img/Hall_Sensor_Demo_Code.jpg)

- 上传代码。
- 当南极朝上的磁铁接近传感器时， LED 将会亮起。 否则， LED 将被关闭。


## 原理图在线预览


<div class="altium-ecad-viewer" data-project-src="https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/res/Twig_Hall_Sensor_v0.9b.zip" style="border-radius: 0px 0px 4px 4px; height: 500px; border-style: solid; border-width: 1px; border-color: rgb(241, 241, 241); overflow: hidden; max-width: 1280px; max-height: 700px; box-sizing: border-box;" />
</div>


资源下载
---------

-   [Grove-Hall Sensor Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/res/Twig_Hall_Sensor_v0.9b.zip)
-   [Hall Sensor Demo Code](https://raw.githubusercontent.com/SeeedDocument/Grove-Hall_Sensor/master/res/Grove-Hall_Sensor_Demo_Code.zip)
-   [A1101 datasheet](http://www.allegromicro.com/en/Products/Part_Numbers/1101/1101.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_Hall_Sensor -->
