---
title: Wio LTE Cat.1
category: Wio_Tracker
bzurl: https://www.seeedstudio.com/Wio-LTE-4G%2C-Cat.1%2C-GNSS%2C-Espruino-Compatible-p-2957.html
prodimagename: wio_tracker_lte_1.jpg
wikiurl: http://seeed.wiki/Wio_LTE_Cat.1
sku: 102990837
---

![](https://github.com/SeeedDocument/Wio_Tracker_LTE/raw/master/img/wio_tracker_lte_1.jpg)

[Wio Tracker](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.20.42d35fceZ0FM3L&id=556108791631)（无线输入输出）是一个开源网关，可以实现更快的 IoT GPS 解决方案。 这是兼容 Arduino 和 Grove 的开发板，可以帮助您跟踪地球上几乎任何移动的东西，然后以无线方式上传这些数据。Wio LTE 是 Wio Tracker 的 LTE 版本，所以现在我们已经有了 Wio Tracker 和 LTE 两个版本，而 LTE（4G）版本会有所不同。

比较 Wio LTE 和 2G 版本有三个主要的更新。首先，从它的名字我们知道 Wio LTE 支持比 2G 更快，更流行的 LTE（4G）通信。 其次，Wio LTE 总共支持 4 种不同的 GNSS-GPS，北斗，GLONSS 和伽利略，QZSS 也被支持。有了更多的 GNSS 支持，定位将会更加准确。 第三，Wio LTE 的 MCU 升级为基于 Cortex-M4 的 STM32，使得 Wio LTE 比 2G 版本快 5 倍。更重要的是，闪存和 RAM 也被提升到 1Mbytes 和 192+4k bytes。

除了三个主要更新之外，LTE 版本几乎与 2G 版本相同。 **如果您的项目使用的是 2G 版本，那么更新到 LTE 版本将非常容易，因为我们已经准备了可移植和可扩展的 AT 命令库。** 兼容 Arduino 和 Grove 可以使用众多库和支持社区。可以在板上使用的 GPS 库不仅限于 Arduino--如果您选择使用 C/C++ 进行开发，它也可以正常工作。通过板载的 6 个 Grove 接口，开发人员可以创建 180 多种传感器和执行器的任意组合，以构建项目并解决任何问题。简化原型和开发阶段是我们的目标。

Wio LTE 非常适合户外项目，其自带的 GPS 天线设备可以连接到 GPS 卫星，并提供与其相连的物品的实时位置。LTE 提供了宽带宽，允许用户和设备之间更快的交互。如果您打算建设自行车共享服务，追踪宠物或牲畜，定位车辆，甚至追踪孩子等项目，Wio LTE 是最好的解决方案。

!!!Warning
    请把任意的 3.7V 锂电池插入模块的电池接口，以防 USB 供电不足导致设备出现问题。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.17.7934f791uiTsdV&id=558693123461)

## 版本

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#ccc;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#fff;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#ccc;color:#333;background-color:#6ab0de;}
.tg .tg-yw4l{vertical-align:top;width:20%}
.tg .tg-yw42{vertical-align:top;width:50%}
.tg .tg-4eph{background-color:#f9f9f9;}
.tg .tg-b7b8{background-color:#f9f9f9;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-yw4l">产品版本</th>
    <th class="tg-yw42">变化</th>
    <th class="tg-yw4l">发布日期</th>
  </tr>
  <tr>
    <td class="tg-4eph">Wio Lte V1.0</td>
    <td class="tg-4eph">初始版本</td>
    <td class="tg-b7b8">2017年7月24日</td>
  </tr>
  <tr>
    <td class="tg-031e">Wio Lte V1.1</td>
    <td class="tg-031e">
    优化生产方法<br>
    <td class="tg-yw4l">2017年10月18日</td>
  </tr>
</table>


## 产品特性

* 为宽带物联网应用优化的低成本，低功耗LTE连接
* 全球 LTE 和 UMTS/HSPA +
* 嵌入式电源管理单元（PMU）具有超低的深度睡眠电流消耗
* GPS/北斗/GLONASS/伽利略/QZSS
* 可移植和可扩展的 AT 命令库兼容 Wio Tracker
* 兼容 Arduino IDE
* 6 个 Grove 接口
* Nano SIM 和 TF 卡二合一插槽


## 规格参数

| 项目            | 内容               | 值                                                                           |
| --------------- | ---------------------- | ------------------------------------------------------------------------------- |
| 微控制器         | 处理器                  | STM32F405RG, ARM 32-bit Cortex-M4, 168MHZ                                       |
|                 | Flash Memory           | 1MB                                                                             |
|                 | SRAM                   | 192+4KB                                                                         |
|                 | 工作电压                | 3.3V                                                                            |
|                 | 每个 I/O 引脚电流        | 7 mA                                                                            |
| LTE             | LTE Cat.1              | AT 命令：3GPP TS27.007 和增强型 AT 命令                              |
|                 | 数据                   | LTE-FDD 最大 10Mbps(DL) 最大 5Mbps (UL)                                           |
|                 |                        | 协议：TCP/UDP/PPP/FTP/HTTP/NTP/PING/QMI/HTTPS*/SMTP*/MMS*/FTPS*/SMTPS*/SSL* |
|                 | 短信                   | 对等消息，SMS 广播，文本和 PDU 模式                        |
|                 | 声音                   | 回声消除，噪音消除                                         |
| 全球导航卫星系统  | 系统                 | GPS/北斗/GLONASS/Galileo/QZSS                                                 |
|                 | 精度              | <2.5 m CEP                                                                      |
| 外部设备      | Grove 接口                | 2 x 数字接口                                                               |
|                 |                        | 2 x 模拟接口                                                              |
|                 |                        | 1 x UART                                                                        |
|                 |                        | 1 x I2C                                                                         |
|                 | 天线                   | 2 x LTE 天线                                                                 |
|                 |                        | 1 x GPS 天线                                                                 |
|                 | 其他                   | USB：供电和上传程序                                         |
|                 |                        | JST 1.0 电池接口                                                 |
|                 |                        | 3.5mm 音频接口                                                                |
|                 |                        | MCU 复位按钮，MCU Boot(DFU) 按钮，C21 电源按钮                       |
|                 |                        | 1 x 用户自定义 RGB LED SK6812                                                         |
|                 |                        | Nano SIM 卡和 TF 卡二合一插槽                                                   |
| 规格参数        | 长                 | 54.7mm                                                                          |
|                 | 宽                  | 48.2mm                                                                          |
|                 | 重量                 |                                                                                 |  |


## 功耗
| 状态                                                                                   | 电流                              |电压                         |
| -------------------------------------------------------------------------------------- | -------------------------------- |--------------------------------|
| 正常启动（启动时）                                                                       | 700mA                            |5V                              |       
| 启动后(IDLE 模式)                                                                       | 300mA                            |5V                              |  
| 启动后正常通信状态（网络传输状态）                                                        | 600mA 到 2A                       |5V                              |  
| 打电话和发短信（信号良好）                                                               | 100-300mA                        |5V                              |  
| 深度睡眠模式，关闭所有功能，需要从外部唤醒（只能通过复位唤醒）                              | 300uA                            |4.2V                            |  
| MCU 深度睡眠模式，唤醒引脚接到 EC21 模块，由 EC21 模块唤醒                                | 至少 300uA (需要测试)    |4.2V                            |  


## 创意应用

* 计步器
* 智能滑雪
* 智能两轮车
* 共享自行车
* 宠物追踪器
* 儿童定位手表
* 智能手表
* 运输定位系统
* 车辆定位系统
* 财产安全


!!!Tip
    可以使用 Grove 模块来扩展您的应用。

板子上有6个 Grove 接口。如果您是第一次听说 Grove，请点击 [Grove 系统](http://seeed.wiki/Grove_System/) 查看更多信息。

## 硬件概述

![](https://github.com/SeeedDocument/Wio_Tracker_LTE/raw/master/img/wio_tracker_lte_v1._top.png)

![](https://github.com/SeeedDocument/Wio_Tracker_LTE/raw/master/img/wio_tracker_lte_v1_buttom.png)

!!!Tip
    如果您需要使用板载 Grove 接口，请把 Stm32 的 PB10 引脚拉高来开启 Grove 接口的 3.3V 电源。

## EC21 模块

这使得它与现有的 EDGE 和 GSM/GPRS 网络向后兼容，确保它可以轻松地从 LTE 迁移到 2G 或 3G 网络。

并且 **EC21-A** 我们用在了 WIO Tracker - LTE 上，支持 AT&T 和 T-mobile SIM 卡。如果您想为其他地区定制 EC21 模块，请随时给我们发电子邮件：fae@seeed.cc

| 频率       | EC21-E                       | EC21-A                         | EC21-V             | EC21-AUT            |
| --------------- | ---------------------------- | ------------------------------ | ------------------ | ------------------- |
| FDD-LTE(4G)     | B1/ B3/ B5/ B7/ B8/ B20      | B2/ B4/ B12                    | B4/ B8             | B1/ B3/ B5/ B7/ B28 |
| TDD-LTE(4G)     |            |    |  |  |
| WCDMA(3G)       | B1/ B5/ B8                   | B2/ B4/ B5                     |                    | B1/ B5              |
| GSM/EDGE(2G)    | B3/ B8                       |                                |                    |                     |
| 嵌入式 GNSS   | 选配                     | 选配                       | 选配           | 选配            |
| Wi-Fi 接口 | Y                            | Y                              | Y                  | Y                   |
| **地区**      | 欧洲、中东和非洲，朝鲜，韩国，泰国，印度 | AT&T, T-mobile                 | Verizon            | 澳洲电信             |
| 认证   | CE/ GCF/ Vodafone*           | FCC/ PTCRB/ AT&T\*/ IC/ ROGERS | FCC/ GCF/ Verizon* | RCM/ Telstra        |

| 频率       | EC21-AUTL    | EC21-AUV            | EC21-AU                         | EC21-KL             |
| --------------- | ------------ | ------------------- | ------------------------------- | ------------------- |
| FDD-LTE(4G)     | B3/ B7/ B28  | B1/ B3/ B5/ B8/ B28 | B1/ B2/ B3/ B4/ B5/ B7/ B8/ B28 | B4/ B8              |
| TDD-LTE(4G)     |              |                     | B40                             |                     |
| WCDMA(3G)       |              | B1/ B5/ B8          | B1/ B2/ B5/ B8                 | |
| GSM/EDGE(2G)    |              |                     | B2/ B3/ B5/ B8                  |                     |
| 嵌入式 GNSS   | 选配     | 选配            | 选配                        | 选配            |
| Wi-Fi 接口 | Y            | Y                   | Y                               | Y                   |
| **地区**      | 澳洲电信      | 澳大利亚 Vodafone | 南美，ANZ，台湾      | 朝鲜，韩国               |
| 认证   | RCM/ Telstra | RCM                 | RCM/ Anatel\*/ NCC\*            | KC/ SKT/KT\*/LGU+\* |

| 频率       | EC21-CT              | EC21-J                          |
| --------------- | -------------------- | ------------------------------- |
| FDD-LTE(4G)     | B1/ B3/ B5/ B7/ B28  | B3/ B7/ B28                     |
| TDD-LTE(4G)     |                      |                                 |
| WCDMA(3G)       | B1/ B5               |                                 |
| GSM/EDGE(2G)    |                      |                                 |
| 嵌入式 GNSS   | 选配             | 选配                        |
| Wi-Fi 接口 | Y                    | Y                               |
| **地区**      | 中国电信        | 日本                           |
| 认证   | CCC\*/ SRRC\*/ CTA\* | JATE/ TELEC/ Softbank\*/ KDDI\* |


## 入门指导

### 安装 USB 驱动

- **Windows 用户**：大多数 Windows 版本不会自动加载 USB 通信端口的内置驱动程序。你需要下载 ST 的 USB 驱动程序：

   - 非 Windows XP 用户：[下载 1.4.0 版本的驱动程序](http://www.espruino.com/files/stm32_vcp_1.4.0.zip)。解压缩文件，运行里面的 .exe 文件，然后在 windows 资源管理器中打开 C:\Program Files (x86)\STMicroelectronics\Software\Virtual comport driver ，然后双击用于 64 位系统的 dpinst_amd64.exe 或用于 32 位系统的 dpinst_x86.exe。

   - Windows XP 用户： [下载 1.3.1 版本的驱动程序](http://www.espruino.com/files/stm32_vcp_1.3.1.zip)。解压缩文件，运行里面的 VCP_V1.3.1_Setup.exe 文件，然后在 windows 资源管理器中打开 C:\Program Files\STMicroelectronics\Software\Virtual comport driver，并双击运行里面的 .exe 文件。

- **Linux 用户**： to ensure that you have the correct permissions to connect as a normal user you'll need to copy the file [45-espruino.rules](https://github.com/espruino/Espruino/blob/master/misc/45-espruino.rules) to /etc/udev/rules.d, reload rules with udevadm control --reload-rules, and ensure your user is in the plugdev group (you can check by typing groups). You add it by typing sudo adduser $USER plugdev and then logging out and back in. Arch Linux users need to add their user to uucp and lock groups instead.
以确保您有正确的权限，以正常的用户连接，你需要复制文件[45-espruino.rules]（https://github.com/espruino/Espruino/blob /master/misc/45-espruino.rules）到/etc/udev/rules.d，用udevadm控制--reload-rules重新加载规则，并确保你的用户在plugdev组（你可以通过输入组来检查）。 您可以通过输入sudo adduser $ USER plugdev来添加它，然后注销并返回。Arch Linux用户需要将其用户添加到uucp并锁定组。

- **Mac OS X 和 Chromebook 用户**：开发板插上去就可以工作，不需要驱动。

### 更新固件

- 第一步：下载 WioLTE 固件 [**v1.93**](https://raw.githubusercontent.com/SeeedDocument/Wio_LTE/master/firmware/espruino_1v93.3171_Wio_LTE.bin) 或者在 [**这里**](http://www.espruino.com/binaries/) 搜索 **espruino_xxx_Wio_LTE.bin**  (**v1.94** 不支持 SD 卡，请使用 **v1.93**).
- 第二步：安装 [dfu-util](http://dfu-util.sourceforge.net/)，然后把 **dfu-util** 添加到 **PATH** 或 **Environment Variables**，所以我们可以在 **命令行** 中使用它。
- 第三步：在断电的情况下按住 **BOOT0** 按钮，上电后松开。
- 第四步：此时 Wio LTE 进入 **DFU mode**。打开设备管理器，如果您看到的是 **STM32 Device in DFU Mode** ，请先按照下文更改 DFU 驱动程序；如果是 **STM32 BOOTLOADER**，则进行下一步。
- 第五步：在命令行中输入 **dfu-util -d 0483:df11 -c 1 -i 0 -a 0 -s 0x08000000 -D C:\XXX\xxx.bin**，其中 **C:\XXX\xxx.bin** 为固件目录和文件名。

![dfu-flash](https://github.com/SeeedDocument/Wio_LTE/blob/master/img/wio_tracker_lte_v1_dfu-flash.png?raw=true)

### 更改 DFU 驱动程序

**对于 windows 用户**：按住 BOOT 按钮并连接到计算机，如果您在设备管理器中看到 **STM32 Device in DFU Mode** 设备，这表示您需要使用 [zadig_xx.exe](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/zadig_2.1.2.exe) 将 DFU 驱动程序从 **STTub30** 更改为 **WinUSB** 。双击打开软件，在 **Options** 菜单点击 **List All Devices**，在中间的下拉菜单里选择 **STM32 Device in DFU Mode**。在下面 **Driver** 一行的绿色箭头右侧选择 **WinUSB**，然后点击 **Reinstall Driver** 按钮更改驱动程序。完成后设备管理器中的 **通用串行总线设备** 中会出现 **STM32 BOOTLOADER**。

![](https://github.com/SeeedDocument/Wio_LTE/raw/master/img/zadig.png)



### 使用 Javascript 编程

感谢 G.Williams 提供 Espruino 的 Javascript 解释器，以便我们可以用 Javascript 来创建原型。

#### 安装 Espruino web IDE

- 第一步：安装 [Chrome Web 浏览器](https://www.google.com/intl/en/chrome/browser/)
- 第二步：[点击这里进入 Espruino Web IDE](https://chrome.google.com/webstore/detail/espruino-web-ide/bleoifhkdalbjfbobjackfdifdneehpo) 并添加。
- 第三步：在 Chrome 的应用中运行 Espruino Web IDE。

![Espruino Web IDE](https://github.com/SeeedDocument/Wio_LTE/blob/master/img/wio_tracker_lte_v1_WebIDE.png?raw=true)

#### 开始使用 Espruino Web IDE

- 第一步：使用 micro USB 电缆将 Wio LTE 电路板连接到电脑。在设备管理器上，您可以看到一个新的 COM 端口设备，在 MacOS 上它是 **STM32 Virtual ComPort**，在 Windows 上是 **STMicroelectronic Virtual COM Port**。

- 第二步：在 Espruino Web IDE 左上角点击连接图标，选择设备并连接。

![](https://github.com/SeeedDocument/Wio_LTE/blob/master/img/wio_tracker_lte_v1_connectWebIDE.png?raw=true)

- 第三步：要了解关于 IDE 的更多信息，可以参考 TOUR。

![](https://github.com/SeeedDocument/Wio_LTE/blob/master/img/wio_tracker_lte_v1_WebIDEGuide.png?raw=true)


#### 如何载入模块

在 Espruino 中，模块是执行常见任务的预先编写的代码（库），例如连接到不同位的硬件。

目前可以通过几种不同的方式使用它们：

##### Espruino Web IDE

如果您使用的是 Espruino Web IDE，只需在右侧输入 require("modulename") - 就像在参考页面中看到的一样。当您点击发送到 Espruino 按钮时，Web IDE将自动在线查找所需模块的缩小版本，下载并加载到电路板上。 您不需要将 SD 卡或 Internet 连接到 Espruino 板本身。

##### 加载模块 - 默认机制

如果您正在使用 Web IDE，则模块将从 http://www.espruino.com/modules/ 加载。 这个URL可以在 Web IDE 设置中更改。

为了节省空间，大多数模块都是作为缩小版本提供的，Web IDE 尝试首先使用默认配置加载缩小版本。

例如，使用 ```require("ADNS5050")```; 将使Web IDE从中加载缩小的模块

##### 从 Github 加载模块

现在，因为你可以在命令行中输入一个 URL，所以你可以直接从 GitHub 中加载一个模块：
```java
require("https://github.com/espruino/EspruinoDocs/blob/master/devices/PCD8544.js");
```

您甚至可以查看 GitHub 上的某些东西的历史记录，然后可以使用该文件的特定版本：
```java
require("https://github.com/espruino/EspruinoDocs/blob/d4996cb3179abe260c030ed02bcb0d2384db6bbd/devices/PCD8544.js");
```


##### 从 NPM 加载模块

如果您在 Web IDE 中激活此选项，则可以从 NPM 存储库加载模块。现在为：

- 只加载最新版本。
- 仅在模块包含单个文件时才有效。
- 可能会导致与 Espruino 的模块冲突，例如时钟混淆。

例如使用 **require("async")**; 将使 Web IDE 从 http://registry.npmjs.org/async 加载模块的 tar.gz 文件（自动提取）。

##### 从本地文件夹加载模块

如果您正在使用本地项目文件夹，则 Web IDE 将自动在其中创建一个空的模块文件夹。把一个模块文件放在那里，你可以加载 **require("myCustomModule");**。

![](https://github.com/SeeedDocument/Wio_LTE/blob/master/img/wio_tracker_lte_v1_projectFiles.png?raw=true)

使用默认的 Web IDE 配置，它将按照以下顺序查找模块：

* 本地缩小版本
* 在线缩小版本
* 当地正常版本
* 在线正常版本

如果您自己的模块与现有模块具有相同的名称，则 Web IDE 将首先使用来自在线的缩小版本。

如果您仍然需要使用它，您可以提供本地缩小版本，或者您可以从 **.min.js|.js to .js|.min.js** 或者 **myCustomModule.js|.min.js|.js** 中更改 Web IDE 配置以使其工作。

##### 独立的 Espruino

如果你有一个带有 SD 卡的 Espruino（但你没有使用 Web IDE），你可以将你需要的模块复制到 SD 卡上名为 “node_modules” 的目录中。现在，只要你写 **require("modulename")**，模块就会被使用。

##### 可连网的 Espruino

现在没有办法让 Espruino 在没有 Web IDE 的情况下从 aaa 上自动加载模块。这可能会在将来被添加，但是在网络连接失败的情况下需要同步的事实使得这难以可靠地执行，直到bbb被添加到解释器中。现在没有办法让 Espruino 在没有 Web IDE 的情况下自动从互联网上加载一个模块，因为在网络连接断开的情况下依旧需要同步。

在此之前，以下不同步的代码将根据需要从 Internet 动态加载模块。
```javascript
function loadModule(moduleName, callback) {
  require("http").get("http://www.espruino.com/modules/"+moduleName+".js", function(res) {
    var contents = "";
    res.on('data', function(data) { contents += data; });
    res.on('close', function() {
      Modules.addCached(moduleName, contents);
      if (callback) callback();
    });
  }).on('error', function(e) {
    console.log("ERROR", e);
  });
}
```

#### 使用板载 RGB LED

- 第一步：配置 LED 的 R，G，B 值，范围为 0~255。
- 第二步：复制代码到 IDE 并上传。
- 第三步：板载 RGB LED 会亮起。

```javascript
WioLTE.setLEDPower(true);
WioLTE.LED(r,g,b); // 请更改 r,g,b 为0-255之间的数值
```

```Javascript
// 动态颜色展示
WioLTE.setLEDPower(true);

var rgb = new Uint8ClampedArray(3);
var pos = 0;
function getPattern() {
  pos++;
  for (var i=0;i<rgb.length;) {
    rgb[i++] = (1 + Math.sin((i+pos)*0.1324)) * 10;
    rgb[i++] = (1 + Math.sin((i+pos)*0.1654)) * 10;
    rgb[i++] = (1 + Math.sin((i+pos)*0.1)) * 10;
  }
  return rgb;
}
setInterval(function() {
  var color = getPattern();
  WioLTE.LED(color[0], color[1], color[2]);
}, 100);
```

####  使用 Grove 模块

##### 使用数字端口
###### [Grove-Button](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.43be6beeZDWgv4&id=531838497696)（输入）
- 第一步：将 Grove-Button 连接到 Wio LTE **D38** 端口。
- 第二步：复制代码到 IDE 并上传。
- 第三步：当我们按下按钮时，我们会看到“Pressed”。否则，我们会在屏幕上看到“Released”。
```javascript
WioLTE.setGrovePower(true);
var button = new (require("GroveButton"))(WioLTE.D38, function(e) {
  if (e.state) console.log("Pressed");
  else console.log("Released");
});
```

###### [Grove-Ralay](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.11.61c5aacdylBRrg&id=45670971061)（输出）
- 第一步：将 Grove-Ralay 连接到 Wio LTE **D38** 端口。
- 第二步：复制代码到 IDE 并上传。
- 第三步：我们会听到继电器开关的声音，并在屏幕上看到“Done”。
```javascript
WioLTE.setGrovePower(true);
var relay = new (require('GroveRelay'))(WioLTE.D38);
setInterval(function() {
  relay.off();
  relay.pulse(1000, function() {
    console.log("Done!");
});
}, 2000);
```

##### 使用模拟端口
###### [Grove-Light Sensor](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.74acd583nFiUyi&id=544373791068)（光线传感器）
- 第一步：将 Grove-Light Sensor 连接到 Wio LTE **A4** 端口。
- 第二步：复制代码到 IDE 并上传。
- 第三步：We will see the numbers printed on screen.
```javascript
WioLTE.setGrovePower(true);
var light = new (require('GroveLightSensor'))(WioLTE.A4);
setInterval(function() {
  console.log(r.read());
}, 500);
```

##### 使用 UART 端口
###### [Grove-GPS](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.13.3752179dZ3hkYf&id=520282073070)
- 第一步：将 Grove-GPS 连接到 Wio LTE **UART** 端口。
- 第二步：复制代码到 IDE 并上传。
```javascript
WioLTE.setGrovePower(true);
Serial1.setup(9600,{tx:WioLTE.UART[1],rx:WioLTE.UART[0]});
var gps = new (require('GPS')).connect(Serial1, function(data) {
  console.log(data);
});
```
- 第三步：我们会看到屏幕上打印出来的时间，纬度，经度，卫星和高度信息。
```
{  "time": "09:35:02", "lat": 30.69766, "lon": 104.05367833333, "fix": 1, "satellites": 6, "altitude": 537.2 }
{  "time": "09:35:03", "lat": 30.69765166666, "lon": 104.05366166666, "fix": 1, "satellites": 6, "altitude": 537.2 }
{  "time": "09:35:04", "lat": 30.69765, "lon": 104.05363833333, "fix": 1, "satellites": 6, "altitude": 537.1 }
```

##### 使用 I2C 端口

###### [Grove 3-Axis Digital Accerlerometer(±16g)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.22.43929309oHBQZU&id=45505202190)（三轴加速度传感器）
- 第一步：将 Grove 3-Axis Digital Accerlerometer(±16g) 连接到 Wio LTE **I2C** 端口。
- 第二步：复制代码到 IDE 并上传。
```javascript
WioLTE.setGrovePower(true);
I2C1.setup({scl:WioLTE.I2C[0], sda:WioLTE.I2C[1]});
var accel = require("ADXL345").connect(I2C1,0,0);
accel.measure(true);
setInterval(function(){
  console.log(accel.read());
},2000);
```
- 第三步：我们会在屏幕上看到 x,y,z 信息如下。
```
{ "x": -0.05859375, "y": -0.46484375, "z": 0.76953125 }
{ "x": -0.0546875, "y": -0.46484375, "z": 0.765625 }
{ "x": -0.0546875, "y": -0.46875, "z": 0.7578125 }
{ "x": -0.05078125, "y": -0.47265625, "z": 0.765625 }
{ "x": -0.0546875, "y": -0.46484375, "z": 0.77734375 }
{ "x": -0.0546875, "y": -0.46875, "z": 0.765625 }
{ "x": -0.0546875, "y": -0.46875, "z": 0.765625 }
{ "x": -0.05078125, "y": -0.47265625, "z": 0.765625 }
```

#### 使用板载 LTE 和 GPS。

当需要使用模块时，Espruino Web IDE 将自动在 [模块库](http://www.espruino.com/modules/) 上搜索模块。
要使用 LTE 和 GPS 功能，您需要通过 **require('wiolte')** **请求模块**。

##### 发送和接收短信
!!!Note
    在使用电话卡相关的功能时，请在板子的 JST 1.0 电池接口上接上 3.7V 的锂电池，以免在使用时因供电不足而出错或重启。
- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：更改发送对象的电话号码和短信内容。
- 第三步：复制代码到 IDE 并上传。
- 第四步：电话号码的拥有者会收到短信。
- 第五步：如果有人发短信给板子里的电话卡，短信内容会在屏幕上打印出来。

```javascript
digitalWrite(B2, 1);
var board;
var APN = "CMAPN";  //网络服务商
var USERNAME = "";
var PASSWORD = "";

function wiolteStart(debug_quectel, debug_at) {
  debug_quectel = debug_quectel || false;
  debug_at = debug_at || false;

  board = require('wiolte').connect(function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    setTimeout(doConnect,3000);
  });

  board.debug(debug_quectel, debug_at);

}

function doConnect() {
  board.connect(APN, USERNAME, PASSWORD, function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    board.getIP(print);

    // 连接后工作
    setTimeout(onConnected, 5000);

  });
}

function onConnected(){
  // 发送短信，请更改电话号码和短信内容
  board.SMS.send("185****6666", "Hello Word!",function(err) {
    console.log(err);
  });

  //接收短信
  board.on('message', function(id){
    board.SMS.read(id, function(d, sms){
      if(d !== "OK") throw new Error(d);
      console.log('SMS from:', sms.oaddr);
      console.log(':', sms.text);
    });
  });

}

wiolteStart();
```


##### 拨打电话
- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：把耳机插入音频口。
- 第三步：更改目标电话号码。
- 第四步：复制代码到 IDE 并上传。
- 第五步：电话号码所有者会接到电话。通过耳机可以通话。

```javascript
digitalWrite(B2, 1);
var board;
var APN = "CMAPN";
var USERNAME = "";
var PASSWORD = "";

function wiolteStart(debug_quectel, debug_at) {
  debug_quectel = debug_quectel || false;
  debug_at = debug_at || false;

  board = require('wiolte').connect(function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    setTimeout(doConnect,3000);
  });

  board.debug(debug_quectel, debug_at);

}

function doConnect() {
  board.connect(APN, USERNAME, PASSWORD, function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    board.getIP(print);

    // 连接后工作
    setTimeout(onConnected, 5000);

  });
}

//请更改目标电话号码
function onConnected(){
  board.Call.call("185****6666");
}

wiolteStart();
```

- 第五步：如果我们在通话过程中看到"Disconnected"，则根本原因是电源不足。请连接电池或连接到有足够电流的供电设备。

```javascript
_____                 _
|   __|___ ___ ___ _ _|_|___ ___
|   __|_ -| . |  _| | | |   | . |
|_____|___|  _|_| |___|_|_|_|___|
         |_| http://espruino.com
1v94 Copyright 2016 G.Williams
Espruino is Open Source. Our work is supported
only by sales of official boards and donations:
http://espruino.com/Donate
>
=undefined
AT passedd
PS attachment succeeded
currently selected operator :+COPS: 0,0,"CHINA MOBILE",7
connectCB entered...
PDP context successfully activated
connectCB entered...
null 10.114.177.248
IP address allocated, modem is ready to use
>
Disconnected
```

##### 接听电话

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：把耳机插入音频口。
- 第三步：复制代码到 IDE 并上传。
- 第四步：它会在有电话打来时自动接听。

```javascript
digitalWrite(B2, 1);
var board;
var APN = "CMNET";
var USERNAME = "";
var PASSWORD = "";

function wiolteStart(debug_quectel, debug_at) {
  debug_quectel = debug_quectel || false;
  debug_at = debug_at || false;

  board = require('wiolte').connect(function(err) {
    console.log("connectCB entered...");

    if (err) throw err;
    setTimeout(doConnect,3000);
  });

  board.debug(debug_quectel, debug_at);

}

function doConnect() {
  board.connect(APN, USERNAME, PASSWORD, function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    board.getIP(print);

    // 连接后工作
    setTimeout(onConnected, 5000);

  });
}

function onConnected(){
  // 有电话时接听
  board.Call.handleRing(true);
  board.on('RING', function(){
    console.log("RING");
    board.Call.answer(function(err){
      print(err);
    });
  });
}

wiolteStart();
```

##### 使用 GPS 定位
- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：复制代码到 IDE 并上传。
- 第三步：如果停止定位，出现 **Geolocalization error : +CME ERROR: 516** ，请输入 **Geoloc()** 来获取 GPS 信息。

```javascript
digitalWrite(B2, 1);
var board;

function wiolteStart(debug_quectel, debug_at) {
  board = require('wiolte').connect(function(err) {
    console.log("connectCB entered...");
    if (err) console.log(err);
    setTimeout(onStart,3000);
  });
  board.debug(debug_quectel, debug_at);
}

function onStart(){
  // 每10秒获取经度，纬度
  board.geoLocStart(10000);
  setInterval(GeoLoc, 2000);
}

function GeoLoc() {
  var coord="";
  board.geoLocGet(function(err, coord) {
    if(err) throw err;
    console.log("longitude latitude = " + coord.lat,coord.lng);
  });
}

wiolteStart();
```

![](https://raw.githubusercontent.com/SeeedDocument/Wio_LTE/master/img/espruino_GPS.png)

##### 打开 Html 网页

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：复制代码到 IDE 并上传。

```javascript
digitalWrite(B2, 1);
var board;
var APN = "CMNET";
var USERNAME = "";
var PASSWORD = "";

function wiolteStart(debug_quectel, debug_at) {
  debug_quectel = debug_quectel || false;
  debug_at = debug_at || false;

  board = require('wiolte').connect(function(err) {
    console.log("connectCB entered...");
    if (err) throw err;
    setTimeout(doConnect,3000);
  });

  board.debug(debug_quectel, debug_at);

}

function doConnect() {
  board.connect(APN, USERNAME, PASSWORD, function(err) {
    console.log("connectCB entered...");

    if (err) throw err;
    board.getIP(print);

    // 连接后工作
    setTimeout(onConnected, 5000);

  });
}

function onConnected(){

  GetHtmlPage("http://www.pur3.co.uk/hello.txt");
}

function GetHtmlPage(html_page){
  require("http").get(html_page, function(res) {
    var contents = "";

    console.log("Response: ",res);

    res.on('data', function(d) {
      contents += d;
    });

    res.on('close', function(d) {
		console.log("Connection closed");
		console.log("full page content ---> \r\n"+contents);
    });
  });
}

wiolteStart();
```

- 第三步：我们可以在屏幕上看到如下信息：

```
_____                 _
|   __|___ ___ ___ _ _|_|___ ___
|   __|_ -| . |  _| | | |   | . |
|_____|___|  _|_| |___|_|_|_|___|
         |_| http://espruino.com
1v94 Copyright 2016 G.Williams
Espruino is Open Source. Our work is supported
only by sales of official boards and donations:
http://espruino.com/Donate
>
=undefined
AT passed
PS attachment succeeded
currently selected operator :+COPS: 0,0,"CHINA MOBILE",7
connectCB entered...
PDP context successfully activated
connectCB entered...
null 10.162.62.37
IP address allocated, modem is ready to use
Response:  httpCRs {
 "headers": {
   "Date": "Thu, 14 Dec 2017 10:25:57 GMT",
   "Server": "Apache/2.4.18 (Ubuntu)",
   "Last-Modified": "Fri, 15 Nov 2013 15:42:26 GMT",
   "ETag": "\"d-4eb390b887c80\"",
   "Accept-Ranges": "bytes",
   "Content-Length": "13",
   "Connection": "close",
   "Content-Type": "text/plain"
  },
 "httpVersion": "1.1",
 "statusCode": "200",
 "statusMessage": "OK"
}
Connection closed
full page content --->
Hello World!
```

#### Javascript APIs

了解更多信息，请访问 [Wio_LTE_Module](http://www.espruino.com/modules/wiolte.js)。

-  `debug(boolean, boolean)`                    - 选择调试等级
-  `reset(callback)`                            - 复位 LTE
-  `init(callback)`                             - 初始化 LTE
-  `getVersion(callback)`                       - 回退 LTE 固件版本
-  `connect(apn, username, password, callback)` - 连接到移动网络
-  `getVersion(callback)`                       - 返回当前版本
-  `getIP(callback)`                            - 获取当前 IP 地址
-  `geoLocStart(period_in_milliseconds)`        - 开始获取地理位置数据
-  `geoLocStop()`                               - 停止获取地理位置数据
-  `geoLocGet(callback)`                        - 获取最后的位置
-  `geoLocConvert(callback(err,latlong))`       - 获取最后的位置作为纬度/经度
-  `board.SMS`                    - SMS 功能函数如下：
  - `init/read/send/list/delete`  - 基于 [[ATSMS]] 模块的功能
-  `board.Call`           - 功能函数如下：
  - `call(number, callback)`
  -  `answer(callback)`
  -  `hangup(callback)`
  -  `handleRing(boolean)` - 如果是，将调用添加的任何函数
    - `board.on('RING', ...)`
-  `sleep(callback)`     - 调制解调器进入睡眠模式，可以节省约100mA
-  `wake(callback)`      - 调制解调器从睡眠模式中唤醒

### 使用 Arduino

#### 软件配置
- 第一步：安装 Arduino IDE，推荐使用 1.8.0 版本的 IDE。
- 第二步：将 Wio_LTE 添加进 Arduino 开发板管理器。点击 **文件（Fail）--> 首选项（Preferences）**，在下面的 URLs 框中添加以下内容：
  `https://raw.githubusercontent.com/Seeed-Studio/Seeed_Platform/master/package_seeeduino_boards_index.json`
  然后选择 **工具（Tools）--> 开发板（Board）--> 开发板管理器（Boards Manager）** ，查找“Wio”并安装。
- 第三步：从 GitHub 上下载 [Wio_LTE 库](https://github.com/Seeed-Studio/Wio_LTE_Arduino_Library) 。
- 参考 [如何安装 Arduino 库](http://wiki.seeed.cc/How_to_install_Arduino_Library) 安装库。

#### 使用 SIM 卡发送短信

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->SMSSend sketch**。
- 第三步：更改电话号码和信息内容。
- 第四步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第五步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第六步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第七步：保持 COM 端口空白。
- 第八步：点击上传按钮上传代码到开发板。
- 第九步：按 **RST** 键启动 COM 端口。

```c++
#include "wio_tracker.h"

char message[128] = "Hello from Wio Traker!";

WioTracker wio = WioTracker();

void setup() {
  wio.Power_On();
  SerialUSB.println("Power On!");

  if(!wio.waitForNetworkRegister())
  {
    SerialUSB.println("Network error!");
    return;
  } else {
    SerialUSB.println("Network ready!");
  }

  // Change xxxxxxxxxxx to your test phone number
  if(wio.sendSMS("185****6666", message))
  {
    SerialUSB.println("Send OK!");
  }
  else
  {
    SerialUSB.println("Send Error!");
  }

}

void loop() {
  AT_bypass();
}
```
- 第十步：使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。
- 第十一步：电话号码所有者会收到消息。

```
Power On!


Network ready!



Send OK!
```

#### 使用 SMS 读取信息

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->SMSRead sketch**。
- 第三步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第四步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第五步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第六步：保持 COM 端口空白。
- 第七步：点击上传按钮上传代码到开发板。
- 第八步：按 **RST** 键启动 COM 端口。

```C++
#include "wiowio_trackerlte.h"

uint16_t newSMSNumber = -1;
char message[128];
char phone[32];
char dateTime[32];


WioTracker wio = WioTracker();

void setup() {
  wio.Power_On();
  SerialUSB.println("Power On!");
  SerialUSB.println("Wait for network registered...");

  if(!wio.waitForNetworkRegister())
  {
    SerialUSB.println("Network error!");
    return;
  } else {
    SerialUSB.println("Network ready!");
  }
  wio.readAllRecUnreadSMS();  // Set all "REC UNREAD SMS" to "REC READ SMS"
}

void loop() {
  int id = wio.detectRecUnreadSMS();
  if(-1 != id){
    newSMSNumber = id;
    wio.readSMS(newSMSNumber, message, 128, phone, dateTime);
    SerialUSB.println("++++++++++++++ Start +++++++++++++++++");
    SerialUSB.print("From: ");
    SerialUSB.println(phone);
    SerialUSB.print("Date: ");
    SerialUSB.println(dateTime);
    SerialUSB.println(message);
    SerialUSB.println("++++++++++++++++ End +++++++++++++++");
  } else {
    SerialUSB.println("Waiting for new SMS!");
  }

  delay(1000);
}

```

- Step 9.使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。
- 第十步：打开串口工具。当看到 **Waitting for new SMS!** 时，发送短信到开发板，新消息将很快被显示出：电话号码，时间，内容。

```
Power On!
Wait for network registered...


Network ready!


Waiting for new SMS!
Waiting for new SMS!
Waiting for new SMS!

++++++++++++++ Start +++++++++++++++++
From: 1375002xxxx
Date: 17/12/20,17:40:38+32
Hello tracker
++++++++++++++++ End +++++++++++++++
Waiting for new SMS!
Waiting for new SMS!
```

#### 使用 GPS

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->GNNS-->GNSS_Show_Coordinate sketch**。
- 第三步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第四步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第五步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第六步：保持 COM 端口空白。
- 第七步：点击上传按钮上传代码到开发板。
- 第八步：按 **RST** 键启动 COM 端口。

```c++
#include "gnss.h"

GNSS gnss = GNSS();

void setup() {
  gnss.Power_On();
  while(false == gnss.Check_If_Power_On()){
    SerialUSB.println("Waitting for module to alvie...");
    delay(1000);
  }
  SerialUSB.println("\n\rPower On!");

  if(!(gnss.open_GNSS())){
    SerialUSB.println("\n\rGNSS init failed!");
    return;
  }

  SerialUSB.println("Open GNSS OK.");
  delay(2000);
}

void loop() {
  if(gnss.getCoordinate()){
    SerialUSB.println();
    SerialUSB.print("GNSS: \r\n");

    // Output double type
    SerialUSB.print("Data type in double: ");
    SerialUSB.print(gnss.longitude, 6);
    SerialUSB.print(",");
    SerialUSB.println(gnss.latitude, 6);

    // Output char* type
    SerialUSB.print("Data type in string: ");
    SerialUSB.print(gnss.str_longitude);
    SerialUSB.print(",");
    SerialUSB.println(gnss.str_latitude);
  } else{
    SerialUSB.print("...");
  }
}

```

- Step 9.使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。
- 第十步：我们将在屏幕上看到经纬度信息。

```
Waitting for module to alvie...
Waitting for module to alvie...
Waitting for module to alvie...

RDY
AT

OK


Power On!


Open GNSS OK.
.................................
GNSS:
Data type in double: 113.966255,22.583820
Data type in string: 113.966255,22.583819

GNSS:
Data type in double: 113.966248,22.583818
Data type in string: 113.966248,22.583818

GNSS:
Data type in double: 113.966248,22.583817
Data type in string: 113.966248,22.583816

GNSS:
Data type in double: 113.966248,22.583820
Data type in string: 113.966248,22.583819
```

#### 使用打电话功能

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->Callup sketch**。
- 第三步：更换电话号码。
- 第四步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第五步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第六步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第七步：保持 COM 端口空白。
- 第八步：点击上传按钮上传代码到开发板。
- 第九步：按 **RST** 键启动 COM 端口。
- 第十步：使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。
- 第十一步：电话号码所有者会接到电话。

```c++
#include "wio_tracker.h"

WioTracker wio = WioTracker();

void setup() {
  wio.Power_On();
  SerialUSB.println("Power On!");

  while(!wio.init()){
    delay(1000);
    SerialUSB.println("Accessing network...");
  }
  SerialUSB.println("Initialize done...");

  bool ret = wio.waitForNetworkRegister();
  if(true == ret){
      SerialUSB.println("Network accessed!");
  }else {
      SerialUSB.println("Network failed!");
      return;
  }

  // Make a phone call
  wio.callUp("xxxxxxxx");
  SerialUSB.println("Calling...");

}

void loop() {
  // Debug
  AT_bypass();
}

```

#### 使用 Socket TCP/UDP 客户端

- 第一步：把一张 Nano SIM 卡插入板子的 SIM 卡插槽内。按照插槽旁边的白色图示插在插槽靠近板子的一侧，SIM 卡缺口指向板子中心。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->TCPConnect**。
- 第三步：更换电话号码。
- 第四步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第五步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第六步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第七步：保持 COM 端口空白。
- 第八步：点击上传按钮上传代码到开发板。

```C++
#include "ethernet.h"

Ethernet eth = Ethernet();


// const char apn[10] = "CMNET";
const char apn[10] = "UNINET";
const char URL[100] = "mbed.org";
char http_cmd[100] = "GET /media/uploads/mbed_official/hello.txt HTTP/1.0\n\r\n\r";
int port = 80;

int ret = 0;


void setup() {
  SerialUSB.println("Begin...");
  eth.Power_On();
  while(false == eth.Check_If_Power_On()){
    SerialUSB.println("Waitting for module to alvie...");
    delay(1000);
  }

  while(!eth.init()){
    delay(1000);
    SerialUSB.println("Accessing network...");
  }
  SerialUSB.println("Initialize done...");

  eth.join(apn);
  SerialUSB.print("\n\rIP: ");
  SerialUSB.print(eth.ip_string);

  if(eth.connect(URL, port, TCP))
  {
    eth.write(http_cmd);
    while(MODULE_PORT.available()){
        serialDebug.write(MODULE_PORT.read());
    }    
    eth.close(1);
  }
  else {
    SerialUSB.println("Connect Error!");
  }

}

void loop() {
  // Debug
  AT_bypass();
}
```
- 第九步：按 **RST** 键启动 COM 端口。
- 第十步：使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。

```
Begin...
Waitting for module to alvie...
Waitting for module to alvie...
Waitting for module to alvie...




Initialize done...





IP: 10.229.226.108




+QIURC: "recv",0,389
HTTP/1.1 200 OK
Server: nginx/1.11.12
Date: Mon, 25 Dec 2017 04:45:01 GMT
Content-Type: text/plain
Content-Length: 14
Connection: close
Last-Modified: Fri, 27 Jul 2012 13:30:34 GMT
Accept-Ranges: bytes
Cache-Control: max-age=36000
Expires: Mon, 25 Dec 2017 14:44:58 GMT
X-Upstream-L1-next-hop: 217.140.101.22:8080
X-Upstream-L1: developer-sjc-cyan-border-nginx

Hello world!


+QIURC: "closed",0
```

#### 使用 SD 卡

- 第一步：将 micro SD 卡插入 SD 卡插槽。
- 第二步：选择 **文件（File）--> 示例（Examples-）->Wio_LTE_Arduino_Library-->SDCard->CardInfo**。
- 第三步：更换电话号码。
- 第四步：按住板子背面的 BOOT 按钮，用 USB 把板子连接到电脑上。
- 第五步：我们会在设备管理器里看到 **STM32 BOOLARDER**。
- 第六步：选择 **工具（Tools）--> 开发板（Boards）-->Wio_Tracker_LTE**。
- 第七步：保持 COM 端口空白。
- 第八步：点击上传按钮上传代码到开发板。

```c++
 // include the SD library:
#include <SD.h>

// set up variables using the SD utility library functions:
Sd2Card card;
SdVolume volume;
SdFile root;

const int chipSelect = 43;

void setup()
{

  SerialUSB.print("\nInitializing SD card...");
  pinMode(SS, OUTPUT);


  // we'll use the initialization code from the utility libraries
  // since we're just testing if the card is working!
  while (!card.init(SPI_HALF_SPEED, chipSelect)) {
    SerialUSB.println("initialization failed. Things to check:");
    SerialUSB.println("* is a card is inserted?");
    SerialUSB.println("* Is your wiring correct?");
    SerialUSB.println("* did you change the chipSelect pin to match your shield or module?");
  }

  // print the type of card
  SerialUSB.print("\nCard type: ");
  switch(card.type()) {
    case SD_CARD_TYPE_SD1:
      SerialUSB.println("SD1");
      break;
    case SD_CARD_TYPE_SD2:
      SerialUSB.println("SD2");
      break;
    case SD_CARD_TYPE_SDHC:
      SerialUSB.println("SDHC");
      break;
    default:
      SerialUSB.println("Unknown");
  }

  // Now we will try to open the 'volume'/'partition' - it should be FAT16 or FAT32
  if (!volume.init(card)) {
    SerialUSB.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card");
    return;
  }


  // print the type and size of the first FAT-type volume
  uint32_t volumesize;
  SerialUSB.print("\nVolume type is FAT");
  SerialUSB.println(volume.fatType(), DEC);
  SerialUSB.println();

  volumesize = volume.blocksPerCluster();    // clusters are collections of blocks
  volumesize *= volume.clusterCount();       // we'll have a lot of clusters
  volumesize *= 512;                            // SD card blocks are always 512 bytes
  SerialUSB.print("Volume size (bytes): ");
  SerialUSB.println(volumesize);
  SerialUSB.print("Volume size (Kbytes): ");
  volumesize /= 1024;
  SerialUSB.println(volumesize);
  SerialUSB.print("Volume size (Mbytes): ");
  volumesize /= 1024;
  SerialUSB.println(volumesize);


  SerialUSB.println("\nFiles found on the card (name, date and size in bytes): ");
  root.openRoot(volume);

  // list all files in the card with date and size
  root.ls(LS_R | LS_DATE | LS_SIZE);
}


void loop(void) {

}
```

- 第九步：按 **RST** 键启动 COM 端口。
- 第十步：使用其他的串口工具来打印串行消息。**请不要使用 Arduino IDE 自带的串口监视器！这可能会导致下次下载失败，重新打开 Arduino IDE 可以解决该问题**。



```

Initializing SD card...
Card type: SDHC

Volume type is FAT32

Volume size (bytes): 2689048576
Volume size (Kbytes): 2626024
Volume size (Mbytes): 2564

Files found on the card (name, date and size in bytes):

```

## 疑难解答
点击 [Wio_LTE](http://support.seeedstudio.com/knowledgebase/articles/1829333-wio-lte-sku-102990925-102990924-102990923-1029) 查看所有的疑难解答。

## 资源下载
- **[Eagle]**[Wio LTE Cat.1 v1.1.SCH](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/Wio%20LTE%20Cat.1%20v1.1.sch.zip)
- **[Eagle]**[Wio LTE Cat.1 v1.1.BRD](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/Wio%20LTE%20Cat.1%20v1.1.brd.zip)
- **[PDF]**[Wio LTE Cat.1 v1.1.SCH](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/Wio%20LTE%20Cat.1%20Sch%20v1.1.pdf.zip)
- **[PDF]**[Wio LTE Cat.1 v1.1.PCB](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/Wio%20LTE%20Cat.1%20PCB%20v1.1.pdf.zip)
- **[Library]**[Wio_LTE_Arduino_Library](https://github.com/Seeed-Studio/Wio_LTE_Arduino_Library)
- **[Library]**[Wio_LTE_JavaScript_Demo](https://github.com/Seeed-Studio/Wio_LTE_JavaScript_Demo)
- **[Datasheet]**[AT Command](https://github.com/SeeedDocument/Wio_LTE/raw/master/res/AT_Command.zip)
