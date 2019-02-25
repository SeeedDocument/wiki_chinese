---
name: Tiny BLE
category: mbed
bzurl: https://www.seeedstudio.com/Seeed-Tiny-BLE-BLE-%2B-6DOF-Mbed-Platform-p-2268.html
oldwikiname:  Tiny BLE
prodimagename:  BLE_Smurfs_Photo.png
wikiurl: http://wiki.seeedstudio.com/cn/Tiny_BLE
sku: 102080005
---

|![](https://github.com/SeeedDocument/Tiny_BLE/raw/master/img/BLE_Smurfs_Photo.png)

|![](https://github.com/SeeedDocument/Tiny_BLE/raw/master/img/Ble_smurfs_interface.png)

|![](https://github.com/SeeedDocument/Tiny_BLE/raw/master/img/Ble_smurfs_ble.png)

Tiny BLE 是一款体积小的低功耗蓝牙开发板。它集成了测量模块，以提供实时的能量消耗数据，这对于开发人员优化软件以设计长电池寿命设备至关重要。它支持带有便于使用的 C/C++ SDK 和大量的开源库的 ARM mbed cloud-based IDE，这使得原型开发非常容易。

通过其模块化设计，我们可以将其分为两部分 - CMSIS DAP 接口部分和 BLE 部分。CMSIS DAP 接口设计就像瑞士军刀多功能组合一样。它提供模块化编程，CMSIS DAP 调试，USB 虚拟串口，电流测量和电池充电。BLE 部分建立在 Nordic nRF51822 上，Nordic nRF51822 搭载蓝牙低功耗 2.4GHz 多协议无线电，运行 16MHz 的 32 位 ARM Cortex-M0 内核，和具有 3D 加速度计和 3D 陀螺仪的 6 自由度的 MPU6050。这些集成在一起，能提供运动检测功能。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.3509dc58tF2w4b&id=45771776143)

##    产品特性
---
*   nRF51822 : ARM Cortex-M0 + 2.4GHz 无线电 (BLE 或 ANT+)

*   MPU-6050 : 3d 加速度计 + 3d 陀螺仪

*   LPC11U35FHI33 : CMSIS DAP

*   电流测定

*   CN3065 : USB部分的电池充电端

*   电源 : USB/battery(3.5-4.2V)
*   输入电压:3.3V

*   4个 I/O 口, 全部可用作模拟输入，数字输入/输出，I2C，SPI 或 UART

*   VCC 输出控制

##   规格参数
---
<table>
<tr>
<th> 项目
</th>
<th> 值
</th></tr>
<tr>
<td width="200px"> 微控制器
</td>
<td width="400px"> nRF51822QFAA; LPC11U35FHI33
</td></tr>
<tr>
<td> 外形尺寸
</td>
<td> 43.3mm x 29.0mm x 4.3mm
</td></tr>
<tr>
<td> 电源
</td>
<td> USB/Battery (JST-1.0 电池座)
</td></tr>
</table>

##   入门指导
---
![](https://github.com/SeeedDocument/Tiny_BLE/raw/master/img/Get_started_with_mbed.png)

1.  点击 [此链接](https://developer.mbed.org/compiler/#import:/teams/mbed/code/mbed_blinky/;platform:Seeed-Tiny-BLE) **注册或登录 mbed**。

2.  [导入 mbed_blinky 程序](https://developer.mbed.org/compiler/#import:/teams/mbed/code/mbed_blinky/;platform:Seeed-Tiny-BLE) 并更改 main.cpp 的代码如下。

3.  单击顶部工具栏的**编译**图标编译程序，然后下载一个编译的十六进制文件。

4.  将下载的十六进制文件拖放到 MBED 磁盘中。

5.  蓝色 LED 将闪烁。

```
#include "mbed.h"

DigitalOut red(p22);           // RED LED
DigitalOut green(p21);         // GREEN LED
DigitalOut blue(p23);          // BLUE LED

int main()
{
    while (true) {
        blue = !blue;
        wait(0.1);
    }
}
```

[Seeed_Tiny_BLE_Get_Started program](http://developer.mbed.org/teams/Seeed/code/Seeed_Tiny_BLE_Get_Started/) 程序包括检测动作，按钮和电池电量。这对于入门大有帮助。

###   调试

要通过 USB Virtual Serial 启动 SWD 调试和调试消息，请安装驱动程序 [the driver from mbed](https://developer.mbed.org/handbook/Windows-serial-configuration)。

###   能量监测

将 USB 虚拟串口的波特率更改为 4000000+ 将触发电流测量。 我们设计了一个工具 - Tiny BLE MONITOR使您可以轻松获取功耗信息。

*   [适用 Windows 的 Tiny BLE MONITOR](http://tangram.qiniudn.com/ble_smurfs_monitor_v0.1.exe)

*   [适用 Linux/Mac OS 的 Tiny BLE MONITOR](https://github.com/Seeed-Studio/Tiny_BLE/tree/master/utils)，附加要求 : pyqtgraph

![](https://github.com/SeeedDocument/Tiny_BLE/raw/master/img/Ble_smurfs_monitor_preview.png)

###   更新或恢复固件

Arch BLE 的最新固件版本是建于 2015 年 2 月 6 日的 v0221。要检查固件版本和建立日期，请在文本编辑器中打开 MBED 磁盘的 MBED.HTM 或 DETAILS.TXT。

更新日志 :

*   2015-02-07 修复 Mac OS X 10.10 问题

固件 :

*   [最新的界面固件 v221 2015-02-06](https://github.com/Seeed-Studio/Tiny_BLE/raw/master/seeed_tiny_ble_interface_latest.bin)

###   Over-The-Air

我们定制了一个 DFU 引导加载程序，以便通过 Over-The-Air ( OTA ) 更新应用程序。 它在 [github.com/Seeed-Studio/nrf51_dfu_bootloader](https://github.com/Seeed-Studio/nrf51_dfu_bootloader)。另见 [mbed.org FOTA](https://developer.mbed.org/teams/Bluetooth-Low-Energy/wiki/Firmware-Over-the-Air-FOTA-Updates)。

##  资源下载
---
*   **[Eagle文件]** [Tiny BLE V1.0 eagle file](https://github.com/SeeedDocument/Tiny_BLE/raw/master/res/BLE_Smurfs_v1.0.zip)

*   **[原理图PDF]** [Tiny BLE V1.0.pdf](https://github.com/SeeedDocument/Tiny_BLE/raw/master/res/BLE_Smurfs_v1.0_PDF.pdf)

*   **[库文件]** [MPU6050 library](http://developer.mbed.org/teams/Seeed/code/eMPL_MPU6050/)

*   **[其他资源]** [Resources on github](https://github.com/Seeed-Studio/Tiny_BLE)

*   **[其他资源]** [frizting part](https://github.com/Seeed-Studio/Tiny_BLE/blob/master/tiny_ble.fzpz?raw=true)
