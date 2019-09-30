---
name: ADALM-PLUTO 简介
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 114991964
tags:
---


![](https://github.com/SeeedDocument/ADALM-PLUTO/raw/master/img/20190919162509.jpg)


使用[ADALM-PLUTO](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADALM-PLUTO.html)主动学习模块时，您需要：

* 两台[SMA连接器](https://en.wikipedia.org/wiki/SMA_connector)来连接仪器或天线

    。发送（标记为“Tx”）
    
    。接收（标记为“Rx”）
    
    。300 MHz - 3.8 GHz
    
    。200 kHz - 20 MHz信道带宽
* 连接主机的USB（用于数据传输）

    - USB 2（480 兆比特/秒）
    
    - 与RF设备进行交互的libiio USB设备
    
    - 网络设备
        - 远程网络驱动接口规范 ([RNDIS](https://en.wikipedia.org/wiki/RNDIS))
        - 默认情况下IP地址为192.168.2.1
    
    - USB串行设备
        - 通过USB通信设备类抽象控制模型（[USB CDC ACM](https://en.wikipedia.org/wiki/USB_communications_device_class))  
        - 规范访问Pluto设备上的Linux控制台
    
    。大容量存储设备：主机会将其识别为一个磁盘，磁盘里您将能看见软件更新链接和设备序列号

* 外部电源

    。进行设计开发工作时，USB 2上负载可能会超过5个单位。考虑到这种情况，我们预留了一个备用电源连接口。备用连接口在正常使用时不是必要的，一旦设备无限重启，或者主机报告问题时，请务必向我们反馈。
    
    。外部转接器或转接头。（[例如此款来自 Seeed 的充电头](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17798475645.15.1aa233dbQEH4K5&id=600378966158)）
    
    。电源处的标识为 “on/off”，一旦标识模糊不清，请向我们反馈。


