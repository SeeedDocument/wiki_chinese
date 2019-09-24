# ADALM-PLUTO 多远/多快  
无线设备的新手用户一开始提出的两个问题通常是：  
1.*设备传播速度有多块？*  
2.*信号覆盖距离有多远？*  
在 ADALM-PLUTO 或其他 SDR 设备中，传播速度和覆盖距离并不固定。用户可以牺牲数据传输速率增加传播距离，或通过增加带宽和改变调制方案来增加数据传输速率。系统性能（多远/多快）很大程度上取决于用户对于载波频率、调制类型、带宽、天线、当地环境（地形、植被、气候）等参数的选择。  
  
## 数据链路 vs 无线电
从一个初学者的角度来讲，首先要去了解数据链路和无线电之间的区别。  
  
[数据链路](https://en.wikipedia.org/wiki/Data_link)在顶层将两个位置连接起来以供数字信息的发送和接收。在大多数情况下，我们有一个发送器、一个接收器和通道。它们遵循链路协议，该协议允许数字数据从数据源（发送器）传输到数据接收端（接收器）。数据链路指明了发送器和接收器所需的所有信息以便有效的交流，其中包括：  

- [单工](https://en.wikipedia.org/wiki/Simplex_communication)、[半双工](https://en.wikipedia.org/wiki/Duplex_(telecommunications)#HALF-DUPLEX) 或 [全双工](https://en.wikipedia.org/wiki/Duplex_(telecommunications)) 通信链路
- 占用带宽
- 中心频率
- 支持的调制类型
- 调制类型的协调工作（如支持）
- MAC 协议（多主、主从、CSMA 等等）  
  
多远、多快或误比特率——这些都是数据链路的特征，而非无线电。  
ADALM-PLUTO 是无线电设备而非数据链路，这些问题很难回答，  
有关数据链路的信息，用户可以点击 [AFAR 通信](http://www.afar.net/tutorials/how-far/) 阅读相关文章。