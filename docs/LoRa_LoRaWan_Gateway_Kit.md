---
title: LoRa/LoRaWAN Gateway Kit
category: Wireless
bzurl:  https://www.seeedstudio.com/LoRa-LoRaWAN-Gateway-868MHz-Kit-with-Raspberry-Pi-3-p-2823.html
prodimagename:
other: 
wikiurl: http://seeed.wiki/LoRa_LoRaWan_Gateway_Kit
sku: 110060622
---
![](https://github.com/SeeedDocument/LoRaWAN_Gateway-868MHz_Kit_with_Raspberry_Pi_3/raw/master/img/LoraWan%20Getway%20868MHz.jpg)

LoRa是一个完美的远程无线解决方案，适用于创建低功耗的广域网络。到目前为止，我们已经发布了几个“LoRa”板卡，如Seeeduino LoRaWan和Grove LoRa Radio等。但是，如果您想要建立自己的LoRa网络， 有三件事你应该准备开始：一个网关，至少一个节点和一个本地服务器，准备好这些您就可以监视所有的LoRa设备。

该套件提供了所有您需要的基本元素：Raspberry Pi 3，带有GPS的Seeeduino LoRaWAN以及网关和本地服务器，使您可以在所有LoRa节点之间收集和传输数据。通过将网关与Seeeduino LoRaWAN和Grove模块连接，您可以在几分钟内建立您的物联网原型。


对于网关模块RHF0M301，它是一个10路（8路Multi-SF + 1路标准LoRa + 1路FSK）LoRaWan网关模块，带有一个24针DIP端口，用户可以方便地将RHF0M301与PRI 2网桥RHF4T002连接， 适用于Raspberry Pi 3和RHF0M301。 我们还包括一个868MHz的天线，一个8GB的SD卡和USB电缆，以太网电缆和其他配件。


!!!Warning
    如果USB电源不足，请务必插上3.7V Lipo电池。 这个wiki适用于868MHz套件和915MHz套件。


|868MHz Kit with Raspberry Pi 3|[点击购买](https://item.taobao.com/item.htm?spm=686.1000925.0.0.469201394xUCHl&id=556011454000)|
|---|---|
|**915MHz Kit for Raspberry Pi 3**|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.7b284f1ey1OhJW&id=556004613634)|

## 产品特性
- 低功耗 & 广域
- 工业级稳定性
- 建立 LoRa /LoRaWAN 网络的经济解决方案
- 丰富的传感器和执行器配件
- 实时监测系统

## 创意应用
- 物联网
- 智能家居
- 安保系统
- 智能节点
- 智慧农场
- 智慧公园

## 用户指南
RisingHF的用户手册已经很好地指导了如何使用LoRaWan Getway Kit，它将详细描述这个套件的用法，包括：
-  怎样搭建硬件环境,
-  怎样接入 LoRaWan 网络,
-  怎样测试硬件

请点击这里下载 [用户指南](https://github.com/SeeedDocument/LoRaWAN_Gateway-868MHz_Kit_with_Raspberry_Pi_3/raw/master/res/%5BRHF-UM01649%5DIoT%20Discovery%20User%20Manual-seeed-v2.1.pdf).

!!!note
    请注意，用户手册中的部件列表与LoRaWAN Getway套件不同。 当您运行会话3.1 Loriot服务器网关注册步骤i“./lrt -f -i eth0 -s cn1.loriot.io”时，会出现如下错误。

![](https://github.com/SeeedDocument/LoRaWAN_Gateway-868MHz_Kit_with_Raspberry_Pi_3/raw/master/img/Gateway_error.jpg)

背后的原因是 Loriot 服务器升级，而我们的固件 SDK 尚未升级。 所以请按照以下说明手动升级网关 SDK。 稍后我们将升级固件。

```
cd /home/rxhf/loriot/1.0.2
sudo systemctl stop pktfwd
sudo gwrst
wget https://cn1.loriot.io/home/gwsw/loriot-risinghf-rhf2s008-rhf1257-SPI-0-latest.bin -O loriot-gw.bin
chmod +x loriot-gw.bin
./loriot-gw.bin -f -s cn1.loriot.io

```

## 资源下载
- [用户指南](https://github.com/SeeedDocument/LoRaWAN_Gateway-868MHz_Kit_with_Raspberry_Pi_3/raw/master/res/%5BRHF-UM01649%5DIoT%20Discovery%20User%20Manual-seeed-v2.1.pdf).
- [Wiki of Seeeduino LoRaWAN](/Seeeduino_LoRAWAN/)
- [RisingHF Website](http://www.risinghf.com/product/risinghf-iot-dicovery/?lang=en)
