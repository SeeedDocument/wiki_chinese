---
title: Raspberry Pi Magic Mirror
category: Raspberry Pi
bzurl:
oldwikiname:
prodimagename:
surveyurl:
sku:
---

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/first.jpg?raw=true)

在生活中，镜子是我们每天必须面对的一件物品。如果能在早上照镜子整理仪容时，能看到每天的天气信息，是多么一件方便而有趣的事情。于是便利用身边的物品做了一个既能照镜子，又能看天气的“魔镜”出来。
这块“魔镜”由单面镜，显示屏，树莓派和其他材料组成。单面镜是一种很特殊的“镜子”。把它安放在光线亮度截然不同的两个环境之间时，站在亮处的人会在镜子中看到自己的影像，就像普通的镜子一样；而暗处的人则会看到亮出的人，就如同透明玻璃一般。这种镜子长城用在监狱、公检法机构审讯室、医院、大学科研机构研究室、大型会议室等，可达到里面看不到外面，外面可看到里面的效果。


在这个应用里，我们需要把一个显示屏藏在单面镜背后。当显示器呈黑色时，外接看到的就是一面镜子；显示器发白光时，则可以看到显示屏上的内容。如果在显示器上显示天气信息，这样就能在照镜子的同时知天气冷暖，是一个很有趣的应用。

## 准备阶段：

制作魔镜需要以下材料：

1.	[Raspberry Pi Mode 3B](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1e3c1debedYZnz&id=528322046763) 一块，用于驱动显示屏。
2.	[5 inch 显示器一个](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1e3c1debeUNWzG&id=565407471482)。
3.	“魔镜”一面。
4.	短HDMI线一根。
5.	[USB供电线](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.16.6f8a33dbHUp20C&id=521385344999) 一根。
6.	薄木板两块。
7.	厚木棒一根。
8.	热熔胶枪和胶棒。

另外还需要一些工具。我找到了一台激光雕刻机，还有手锯，木工螺钉，M3（推荐M2.5）螺钉，螺帽，铜柱，电钻，尺子，电吹风等。

薄木板是用来挡住镜子背后的光，和安装屏幕。厚木棒是用来做支撑用的。

要让屏幕显示天气信息，首先要更改树莓派的设置让屏幕正常工作。输入：

```
cd /boot
sudo nano config.txt
```

然后在文件中加一行：

```
hdmi_cvt 800 480 60 6 0 0 0
```

然后输入reboot重启。重启后就能完美适配这款显示屏了。

## 开始制作

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/materials.jpg?raw=true)

* 写一个天气显示应用

为了让屏幕能显示天气信息，我使用pygame显示字符和图片。感谢贴吧网友xxx的源代码，我对其做了一些小改动以适应我的屏幕。文件夹中，weatherAPI.py存放API调用地址，key和城市ID。天气API从这个网站调用：。进去后可以获取免费的？？？次的调用次数，一般情况是足够使用的。更改weatherAPI.py里的key和城市ID为你自己的信息。

pygame.py是图形显示应用程序,使用python3写的。里面我增加了一些注释，使更改代码和UI更加容易。前期调试时使用窗口模式，用“ALT+TAB”切换到命令行后可以用“CTRL+C”退出pygame。调试完成后使用全屏模式，此时只能断电退出！
经过调整后，我的UI效果如下图所示：

```
sudo python3 pyGame.py
```

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/9.jpg?raw=true)


* 开始加工

我的镜子尺寸为000mm*000mm，因此我买了很接近镜子尺寸的薄木板。用HDMI线连接好树莓派和屏幕后，我规划了空间位置，然后将屏幕放置在这个位置，树莓派放在背板上。增加了几个安装孔，用于安装背板和树莓派。然后把薄木板放在激光雕刻机中加工。

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/1.jpg?raw=true)

在这个作品中，我使用热熔胶把薄木板，单面镜和屏幕粘在一起。由于要打很多胶进去，我用电吹风对模板和单面镜加热，减缓安装时胶的冷却速度，使粘结更牢固，缝隙更小。然后把屏幕也用胶黏上去。注意，不要在屏幕表面打胶，只在周围的PCB板上粘即可。

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/2.jpg?raw=true)

把木棍锯成比木板略窄的宽度，加热，然后也用胶黏上去。

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/7.jpg?raw=true)

把树莓派用螺丝和铜柱固定在背板上并接好线路。注意，树莓派自己的安装孔直径2.6mm，不能直接装M3的铜柱。我使用丝锥对其进行攻丝，正好可以拧M3螺丝。然后放在两根粘好的木棍上，上下左右对正后，用木工螺钉拧起来。

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/8.jpg?raw=true)

最后一步，把SD卡从圆孔里插入树莓派，USB供电线从椭圆孔插入树莓派，上电，用VNC启动应用，大功告成！

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/4.jpg?raw=true)

最后上一张效果图：

![](https://github.com/SeeedDocument/Raspberry_Pi_Magic_Mirrar/blob/master/img/3.jpg?raw=true)
