
# Jetson Nano串口通信

通过电线进行串行传输可以追溯到100年。在我的视野中，Ferdinand Magellan 是一个发明串行线的人，但是由于在1521年Mactan的战争中，这项发明被丢失了。显然它后来在美国被重新发现，电传打字机通过电报线进行串行通信。在1916年，第一项关于串行通信的专利被授权，该项专利的主要内容是围绕停止和启动串行线同步的方法。

串行通信在电脑行业中是普遍存在的，在这种情况下，我们准备通过Jetson Nano Developer Kit上面的J44 UART 与电脑进项连接。UART是Jetson Nano上面的串行控制台，它允许直接访问调试控制台。当系统变成砖，这个是一个非常方便的调试方式。
这是嵌入式设备提供的一个典型的控制台，在很多情况下，它是非常有用的。串行控制台不仅可以进行不同的镜像（liunx的内核镜像）选择，还可以访问没有键盘、鼠标和显示器的Nano。

## 安装

因为Nano只需要最基本的串行线进行通信，所以绝大多数的电脑通过串口终端软件都可以与Nano进行通信。而且有大量的上位机软件可以适合我们的要求。在这里，我们使用在windows10上面运行的putty进行访问。

Jetson Nano J44 接线帽采用TTL逻辑电平。很多种方式去连接它。我们采用很多种方式去访问，我们采用将TTL信号变成USB信号方式与电脑进行通信。在这里我们选择的是seeed的[USB转串口芯片](https://www.seeedstudio.com/USB-to-TTL-Serial-Cable-Debugger-for-Dev-Board-p-1642.html)

## 接线

接线是非常直接的，确定Nano没有上电和J44没有接上其他的线，安装下面的指示对应接线

Jetson Nano J44 Pin 2 (TXD) → Cable RXD (White Wire)

Jetson Nano J44 Pin 3 (RXD) → Cable TXD (Green Wire)

Jetson Nano J44 Pin 6 (GND) → Cable GND (Black Wire)

实物连接如图所示

![](https://i0.wp.com/www.jetsonhacks.com/wp-content/uploads/2019/04/J44Wiring.jpg?resize=768%2C451&ssl=1)

## 软件

在你在使用其他电脑上面的上位机连接Nano之前，你需要先找到Nano对应的COM口。那个COM的编号跟你的电脑有关

![](https://github.com/SeeedDocument/Jetson-Nano--Uart-Console/raw/master/img/Device-Select.png)

我们使用putty软件进行方式，假如您的电脑上面还没有的话。这是[下载地址](https://www.putty.org/)

## 配置

两个设备要想成功的通信，软件的配置是非常重要的一部分。连接的波特率为115200，8位，无奇偶校验，一位停止位(115200 8N1)。我们一般都是3线的串口所以是软件流控制，当我们使用5线的串口进行通信存在RTS和CTS，则是硬件流控制，具体配置如下

![](https://github.com/SeeedDocument/Jetson-Nano--Uart-Console/raw/master/img/Putty-Config.png)

## 成果

在这个控制台我们还可以修改Nano的bootloader配置，我们可以是通过按键中断启动进程来与bootloader进行交互。通过这个程序我们可以选择SD里面存在的不同的内核，如果在次期间你没有按下按键那么Nano将自动启动。

![](https://github.com/SeeedDocument/Jetson-Nano--Uart-Console/raw/master/img/Console-Content.png)