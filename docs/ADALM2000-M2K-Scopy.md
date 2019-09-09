---
name: ADALM2000-M2K Scopy
category: 
bzurl: 
oldwikiname: 
prodimagename:
surveyurl: 
sku: 102991188
tags:
---


## 关于 Scopy

Scope是一个具有强大信号分析能力的多功能软件工具包。

## 下载 Scopy

**Window 用户**

- 下载：[Installer for latest release (Windows 64/32-bit)](https://github.com/analogdevicesinc/scopy/releases/latest)
- 下载：[nstaller for latest (nightly) build (Windows 64-bit)](https://tinyurl.com/yyfa4ytt) -- 需要编译
- 下载：[Installer for latest (nightly) build (Windows 32-bit)](https://tinyurl.com/y3gj3547)  -- 需要编译


**Linux 用户** 
 
- 下载：[Scopy Flatpak installer](https://github.com/analogdevicesinc/scopy/releases/latest)


**OSX 用户**   

- 下载：[OSX installer](https://github.com/analogdevicesinc/scopy/releases/latest)


!!!Attention
        为保证scopy正常工作，请确认驱动程序已安装。查询相关指南点击： 
         
        - [ADALM2000 学生和普通用户指南](http://wiki.seeedstudio.com/cn/ADALM2000-for-End-Users/)


## 安装

**Windows 用户**

下载并运行安装包，完成所有步骤后需要重启系统。

**Linux 用户**

下载和解压scopy_v1.0-linux.zip文件之前，请按照指南安装针对您的Linux版本的Flatpak。  

对于Ubuntu用户，步骤如下：

```
sudo add-apt-repository ppa:alexlarsson/flatpak
sudo apt update
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

```

完成后，从下载的文件中提取并执行Scopy.flatpak文件。 

```
flatpak install Scopy.flatpak

```

**OSX 用户**  

双击下载的.dmg文件使其内容可见，scopy将显示在查找器侧边栏中并弹出一个显示内容的窗口。  
 
将应用程序从.dmg窗口拖动到Applications中，安装并等待其完成。


## 启动

从桌面快捷方式/开始菜单/安装文件夹运行scopy。  

在Linux系统中，您也可以使用：

```
flatpak run org.adi.Scopy

```



## 软件界面说明


### 软件主页

主页界面分为四个部分：

- 1.设备：Scope可以连接到的设备（USB或远程设备）列表。USB设备在启动时自动检测，Add按钮用于在列表中添加远程设备。
- 2.仪器菜单：软件提供的仪器列表。
- 3.信息窗口：包含“欢迎”、“添加设备”页面和每个设备的概况。
- 4.通用设置菜单：保存及加载会话、首选项菜单。

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_media/university/tools/m2k/scopy_home_view.png?cache=&w=899&h=527&tok=c73f5f" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_home_view.png" alt="scopy home" title="scopy home" />
  <figcaption><b>图 1</b>. <i>Scopy 主页</i></figcaption></a>
</figure>
</div>


### 连接USB设备



如果兼容　USB　设备可用，它将显示在　**Devices**　区。

若要连接到该设备，请点击该设备，然后点击 **信息窗口** 内的 **Connect** 按钮。  

建立连接后，设备下方将出现一条绿线。点击 **同一窗口** 中 **Disconnect** 即可断开连接。



<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/device_connected.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/device_connected.png" alt="scopy 连接 USB 设备" title="连接 USB 设备" />
  <figcaption><b>图 2</b>. <i>连接 USB 设备</i></figcaption></a>
</figure>
</div>


### 连接远程设备

要连接远程设备，单击 **+** 图标。在 **Hostname** 处输入远程设备的 IP，点击 **Connect**。如果在这个 IP 上成功检测到设备，**Connect** 按钮将变为 **Add** 按钮，您可以点击并将其添加到设备列表中。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy_add_device_page1.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_add_device_page1.png" alt="scopy 连接远程设备" title="连接远程设备 -1" />
  <figcaption><b>图 3</b>. <i>连接远程设备 -Add</i></figcaption></a>
</figure>
</div>


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy_add_device_page2.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_add_device_page2.png" alt="scopy 连接远程设备" title="连接远程设备 -2" />
  <figcaption><b>图 4</b>. <i>连接远程设备 -Connect</i></figcaption></a>
</figure>
</div>


点击 **Forget Device** 即可从列表中删除设备。点击 **Identify** 会使设备指示灯闪烁。



## 通用设置菜单


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy_general_settings1.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_general_settings1.png" alt="scopy 通用菜单设置" title="通用菜单设置" />
  <figcaption><b>图 5</b>. <i>通用菜单设置 -Save/Load</i></figcaption></a>
</figure>
</div>


点击 **save/load** 按钮保存当前会话或加载其他会话。点击 **preferences** 按钮进入首选项页面，修改不同工具的各种选项。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/preferences1.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/preferences1.png" alt="scopy 通用菜单设置" title="通用菜单设置-2" />
  <figcaption><b>图 6</b>. <i>通用菜单设置 -Preference</i></figcaption></a>
</figure>
</div>


点击 **Reset Scopy** 将软件重置为默认配置。

点击user notes preference将启用一个工具，用户可以在该工具中添加具有HTML格式文本的不同页面。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/notes1.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/notes1.png" alt="scopy 通用菜单设置" title="通用菜单设置-Note" />
  <figcaption><b>图 7</b>. <i>通用菜单设置 -Note</i></figcaption></a>
</figure>
</div>


## 使用指南

Scopy一次只能与一个硬件设备交互。选择该设备后，该设备可用的仪器列表将会启用。在左边菜单中选择打开仪器，仪器名称右边的图标表示仪器可用，点击图标选择打开/关闭仪器。
 
点击左上角窗口附近的 **Scopy** 按钮，可将仪器菜单最小化。


<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/notes1.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/min_menu.png" alt="scopy 最小化窗口" title="最小化窗口" />
  <figcaption><b>图 8</b>. <i>最小化窗口</i></figcaption></a>
</figure>
</div>



### 分离仪器窗口

Scopy为每个可用仪器提供了分离窗口的功能，优化视图，方便操作。  
 
下面提供两种方法：

- 1、**拖放** — 选择所需的仪器，将其拖动到仪器菜单区之外，然后将其放到应用程序窗口区内。

<div align="center">
<figure>
 <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_drag_n_drop.gif" alt="scopy 分离仪器" title="scopy 分离仪器" />
  <figcaption><b>图 9</b>. <i>分离仪器 - 拖动释放</i></figcaption>
</figure>
</div>


- 2、**双击** — 先确保在 **Preferences** 菜单中启用了 **Double click to detach a tool** 选项；双击所需的工具以将其分离。


<div align="center">
<figure>
 <img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_dc_detach.gif" alt="scopy 分离仪器" title="scopy 分离仪器" />
  <figcaption><b>图 10</b>. <i>分离仪器 - 双击</i></figcaption>
</figure>
</div>


### 仪器概述

<div align="center">
<figure>
  <a href="https://wiki.analog.com/_detail/university/tools/m2k/scopy_instruments_menu.png?id=university%3Atools%3Am2k%3Ascopy" target="_blank"><img src="https://wiki.analog.com/_media/university/tools/m2k/scopy_instruments_menu.png" alt="scopy 仪器列表" title="仪器列表" />
  <figcaption><b>图 11</b>. <i>仪器列表</i></figcaption></a>
</figure>
</div>



各个仪器用户指南：

- [1.Oscilloscope(示波器)](http://wiki.seeedstudio.com/cn/ADALM2000-M2K-Oscilloscope)
- 2.Spectrum Analyzer(频谱分析仪)
- 3.Network Analyzer(网络分析仪)
- 4.Signal Generator(信号发生器)
- 5.Logic Analyzer(逻辑分析仪)
- 6.Pattern Generator(模式发生器)
- 7.Digital IO(数字输入输出控制)
- 8.Voltmeter(电压表)
- 9.Power Supply(电源)


### 脚本

关于如何使用 Scopy脚本 的用户指南：

- [Scopy - 脚本指南](https://wiki.analog.com/university/tools/m2k/scopy/scripting-guide)


## 编译

完整的 Scopy 编译指南：

- [1.Window](https://wiki.analog.com/university/tools/m2k/scopy/build-windows)
- [2.Linux](https://wiki.analog.com/university/tools/m2k/scopy/build-linux)
- [3.OSX](https://wiki.analog.com/university/tools/m2k/scopy/build-osx)



## 源代码

查询软件全部源代码点击 [github](https://github.com/analogdevicesinc/scopy)。