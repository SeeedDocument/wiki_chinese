---
name: Grove - Servo
category: Actuator
bzurl: https://www.seeedstudio.com/Grove-Servo-p-1241.html
oldwikiname:  Grove - Servo
prodimagename: Grove—Servo.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-Servo
sku:  316010005
tags: grove_i2c, io_5v, plat_duino, plat_linkit

---
![](https://github.com/SeeedDocument/Grove-Servo/raw/master/img/Grove—Servo.jpg)

Grove - Servo 是带齿轮和反馈系统的直流电机。它用于机器人的驱动动力。对该 Grove 爱好者而言，该产品是意外的惊喜。我们将三线舵机改造为标准 Grove 接口。您现在可以将其作为典型的 Grove 模块进行即插即用，无需使用混乱的跳线。

但如果您感觉更喜欢原来的舵机，请查看 EMAX 9g ES08A 高灵敏度小型舵机。他们的型号与我们的相同，质量好，价格又适中，也可以作为一个选择。


[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.59514eadoScgxN&id=45554357772)

产品特性
---
*   模块小巧
*   兼容 Grove 接口
*   易于使用

规格参数
---
<table  cellspacing="0" width="80%">
<tr>
<th scope="col"> 项目
</th>
<th scope="col"> 最小值
</th>
<th scope="col"> 典型值
</th>
<th scope="col"> 最大值
</th>
<th scope="col"> 单位
</th></tr>
<tr>
<th> 工作电压
</th>
<td> 4.8
</td>
<td> 5.0
</td>
<td> 6.0
</td>
<td> V
</td></tr>
<tr>
<th> 扭矩
</td>
<td colspan="3"> 1.5/1.8
</td>
<td> Kg.cm
</td></tr>
<tr>
<th scope="row"> 速度
</th>
<td colspan="3"> 0.12/0.16
</td>
<td> s/60°
</td></tr>
<tr>
<th scope="row"> 尺寸
</th>
<td colspan="3"> 32X11.5X24
</td>
<td> mm
</td></tr>
<tr>
<th scope="row"> 重量
</th>
<td colspan="3"> 8.5
</td>
<td> g
</td></tr></table>

Platforms Supported
-------------------

开始使用
---
### 连接

在这里我们向您展示 Grove - Servo 工作的简单实例。首先，要准备以下材料：

| Seeeduino V4 | Grove - Servo | Base Shield |
|--------------|-------------|-----------------|
|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_1.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-Servo/raw/master/img/Grove%20Servo_s.jpg)|![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_Light_Sensor/master/images/gs_4.jpg)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.20.5d0cd55eL1BrVs&id=45721222112)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.14.25a75ea3sLKfGE&id=45554357772)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.5f586638hrEBEP&id=520233320144)|

舵机有三根线：电源，地和信号。电源线通常为红色，应连接到 Arduino / Seeeduino 板上的 **5V** 引脚。接地线通常为黑色或棕色，应连接到 Arduino 板上的 **GND** 引脚。信号线通常为黄色，橙色或白色，应连接到 Arduino 板上的数字 **9**。 我们可以根据需要改变数字端口，同时不要忘了在演示代码的定义中更改端口号。

-   将模块连接到 Base Shield 的 **D9** 端口。
-   把 Grove- Base Shield 插在 Arduino 上。
-   把 Arduino 用 USB 数据线连接到电脑。


### 软件

- 通过使用 [Adruino Servo 库](http://arduino.cc/en/Reference/Servo) 来使舵机摇臂向前和向后旋转 180°。
- 按照一下路径打开代码： **File（文件） -> Examples（示例） ->Servo->Sweep**.

  ![](https://github.com/SeeedDocument/Grove-Servo/raw/master/img/library%20example.jpg)

```
/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // 创建舵机控制对象来控制舵机
// 大多数板子都可以控制 12 个舵机

int pos = 0;    // 舵机位置

void setup() {
  myservo.attach(9);  // 把舵机连接到引脚 9 上
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // 从 0° 动作到 180°
    // in steps of 1 degree
    myservo.write(pos);              // 告诉舵机旋转到角度“pos”
    delay(15);                       // 等待 15ms 让舵机旋转到位
  }
  for (pos = 180; pos >= 0; pos -= 1) { // 从 0° 动作到 180°
    myservo.write(pos);              // 告诉舵机旋转到角度“pos”
    delay(15);                       // 等待 15ms 让舵机旋转到位
  }
}
```

- 上传代码，可以看到舵机左右旋转。

资源下载
---------

- **[文档]** [Understanding RC Servos](http://www.rchelicopterfun.com/rc-servos.html)
- **[库函数]**[Arduino Tutorial - Servo Library](https://www.arduino.cc/en/Reference/Servo)
- **[例程]** [Digital/Analog Clock - Arduino + PaperCraft](http://www.instructables.com/id/DigitalAnalog-Clock-Arduino-PaperCraft/?ALLSTEPS)
- **[例程]** [Low Cost Hobby Servo XY Table](http://www.instructables.com/id/Low-Cost-Hobby-Servo-XY-Table/?ALLSTEPS)
