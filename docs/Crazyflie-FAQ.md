# 常见问题  

## Crazyflie 2.X 续航时间是多少？  
理论上续航时间最长为 7 分钟，实际上取决于您飞行的方式，时长会有所下降。  

## Crazyflie 2.X 怎样充电？  
充电接口采用智能手机上常见的标准 micro-USB 接口。充电线随处可见，充电电流为 500mA，大部分电脑或适配器均可使用。充电时间约为 40 分钟，蓝色 LED（M3）通过点亮的时长显示充电的情况，常量表示电已充满。  

## Crazyflie 2.X 支持电池热插拔吗？  
是的，Crazyflie 支持电池热插拔。  

## 我可以用大一些的电池吗？  
可以，只要不超重、确保 3.7V 单电池且电极安装正确即可采用其他电池。更大容量的电池提供更长时间的续航，但会降低敏捷性，我们推荐使用连续放电速率 15C 以上的电池。  

## Crazyflie 2.X 使用什么无线电？  
PC 端可以用 Crazyradio 或 Crazyradio PA 控制，或者使用采用低功耗蓝牙模块的移动设备。  

## Crazyflie 2.X 支持什么样的移动设备？  
支持的移动设备要求如下：
- 低功耗蓝牙（BLE），也称蓝牙智能或蓝牙低能耗
- 安卓 4.4 或更新的版本
- iOS 7.1 或更新的版本  

由于安卓系统支持很多不同设备，即使上述要求全部满足也可能会出现问题。谨慎起见，我们列出了部分测试过的安卓设备以供参考，[点击此处查看](https://wiki.bitcraze.io/doc:crazyflie:client:cfandroid:index#android_device_compatibility) 。  

## Crazyradio 范围是多少？  
与其他无线电通信一样，取决于环境、无线电干扰、芯片生产批次等等。此外，使用 Crazyradio、Crazyradio PA 和移动设备的范围也不同。在室外干扰可以忽略时，我们分别对不同配置进行了几组 LOS 测试：
- Crazyradio：250 Kbit 模式下范围约为 100m（Crayradio 上行链路限制了范围）
- Crazyradio PA：250 Kbit 模式下范围约为 1000m（Crazyflie 2.X 下行链路限制了范围）
- 移动设备：范围约为 20m（移动设备上行链路限制了范围）  

## 可以使用普通遥控发射机控制 Crazyflie 2.X 吗？  
使用 BigQuad 扩展板可以实现此功能。这是一种解决方法，但需要用户自己去配置。  

## Crazyflie 2.X 耐用吗？  
Crazyflie 2.X 将 PCB 本身作为结构框架，PCB 采用 FR4 板，强度高、重量轻。电机支架采用比较柔软的材料，猛烈撞击时会损坏但可以保护 PCB 和电子元件，因为电机支架容易更换且价格便宜。我们经过多次碰撞测试（包括从 30m 高处直接摔向混凝土地面），并未出现除支架和电机之外的其他元件损伤。尽管如此，这并不意味着无人机是坚不可摧的，所以使用时请务必小心！  

## Crazyflie 2.X 向后兼容 Crazyflie 1.0（Crazyflie Nano）吗？  
固件和通信协议是向后兼容的。所有的库都是用 Python、Ruby、C、C++、Java 等写的，与 Crazyflie 2.X 控制方式一样。  

## 现在还支持 Crazyflie 1.0（Crazyflie Nano）吗？  
是的，固件和 Python 客户端仍支持 Crazyflie 1.0 。  

## Crazyflie 2.X 可以控制更大一些的 4 轴无人机吗？  
可以，使用 [BigQuad 扩展板](https://www.bitcraze.io/bigquad-deck/) 。  

## Crazyflie 2.X 飞行时可以观看第一人称视角（FPV）吗？  
现在正在进行这方面的研究：  
- [Crazyflie 2.X FPV 设置](https://forum.bitcraze.io/viewtopic.php?f=6&p=8295)  

## Crazyflie 2.X 可以自主飞行吗？  
Crazyflie 2.X 自带的传感器并不能满足这个要求，自主飞行需要更多的信息，例如精确的定位、环境的情况等等。最简单的方法就是使用 [Flow 模块](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17798475675.14.72c61ccc7UjlLV&id=557253255642) ，该模块可以告诉 Crayflie 移动的相对位置，帮助其完成自主飞行。进入 [产品页面](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-17798475675.14.72c61ccc7UjlLV&id=557253255642) 获取更多信息。  

外部的定位系统可以向 Crazyflie 提供绝对位置信息以实现自主飞行。户外可以通过 GPS 接收机实现定位，室内则需要其他的定位系统。  

Bitcraze 研发了一款基于无线电的本地定位系统 —— [Loco 定位系统](https://www.bitcraze.io/loco-pos-system/) 。Crazyflie 2.X 可以借助此系统实现室内自主飞行，进入 [产品介绍页面](https://www.bitcraze.io/loco-pos-system/) 获取更多信息。  

研究人员经常使用运动捕捉系统（如 Qualisys 或 Vicon）实现自主飞行，系统主要依靠外部计算机对其进行控制。例如，麻省理工学院的这项研究正在将这种系统与强大的控制算法结合使用：https://www.youtube.com/watch?v=v-s564NoAu0  

我们一直在使用像 Microsoft Kinect 这样的摄像头系统让无人机在摄像头上方自主飞行： https://www.bitcraze.io/2015/05/autonomous-flight-using-kinect2-for-position-control/  

## Crazyflie 可以集群飞行吗？  
可以使用 Loco 定位系统和 [Python 库](https://github.com/bitcraze/crazyflie-lib-python/blob/master/examples/swarm/swarmSequence.py) 或者 [ROS 及 ROS 驱动](http://wiki.ros.org/crazyflie) 同时控制多架次的 Crazyflie 。使用 ROS 驱动实现集群飞行可参考该视频：[Crazyflie 2.0 Swarm](https://www.youtube.com/watch?v=ezTayb76x9U)  

