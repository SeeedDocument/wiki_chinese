---
title: Grove Indoor Environment Kit for Edison
category: Others
bzurl: https://www.seeedstudio.com/Grove-Indoor-Environment-Kit-for-Intel%C2%AE-Edison-p-2427.html
oldwikiname:  Grove Indoor Environment Kit for Edison
prodimagename: Grove_Indoor_Environment_Kit_for_Edison_with_case.JPG
wikiurl: http://seeed.wiki/Grove_Indoor_Environment_Kit_for_Edison
sku:  110060064
---
![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Grove_Indoor_Environment_Kit_for_Edison_with_case.JPG)

Grove Indoor Environment Kit for Edison 与 Intel @ Edison 和 Arduino 扩展板共同使用便可以轻松创建完整的室内环境应用程序。而且使用 Base Shield V2，开发人员可以快速插入多达11个不同的 Grove 传感器和执行器。我们提供不断更新的炫酷演示代码，以便在您没有任何编程经验的情况下也易于操作。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.5-c.w4002-11172345288.19.4b49a084a6rfk1&id=520772246644)

##   套件清单
---
*   [Base Shield V2](/Base_shield_v2)  x1

*   [Grove - Tempture&amp;Humidity Sensor (High-Accuracy &amp;Mini)](/Grove-TemptureAndHumidity_Sensor-High-Accuracy_AndMini-v1.0)  x1

*   [Grove - Moisture sensor](/Grove-Moisture_sensor)  x1

*   [Grove - Light Sensor](/Grove-Light_Sensor)  x1

*   [Grove - UV Sensor](/Grove-UV_Sensor)  x1

*   [Grove - PIR Motion Sensor](/Grove-PIR_Motion_Sensor)  x1

*   [Grove - Encoder](/Grove-Encoder)  x1

*   [Grove - Button](/Grove-Button)  x1

*   [Grove - LCD RGB Backlight](/Grove-LCD_RGB_Backlight)  x1

*   [Grove - Relay](/Grove-Relay)  x1

*   [Grove - Servo](/Grove-Servo)  x1

*   [Grove - Buzzer](/Grove-Buzzer)  x1

*   [9V to Barrel Jack Adapter](http://www.seeedstudio.com/depot/9V-to-Barrel-Jack-Adapter-p-1481.html)  x1

*   26AWG Grove Cable  x10

*   USB 电缆  x1

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Grove-Indoor-Environment-Kit-for-Edison.jpg)

##   安装 Edison Arduino IDE
---
**[<font color =“Red”>链接失效]**  </font>  请参阅英特尔爱迪生官方网站：[爱迪生入门指南](https://communities.intel.com/docs/DOC-23147)

1.下载 **Edison Arduino IDE**（注意：选择您的操作系统。）

2.打开您下载 **Edison Arduino IDE.zip** 的文件夹。

3.单击 **.7z** 文件，解压缩 **"arduino- ..."** 。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/IndoorKit_Extract_7z.png)

4.单击创建的文件夹，会看到IDE **“arduino.exe”** 文件。双击此文件，打开窗口。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/IndoorKit_ArduinoIDE.png)

##   安装驱动程序
---

1.下载 [FTDI drivers](http://www.ftdichip.com/Drivers/CDM/CDM%20v2.10.00%20WHQL%20Certified.exe)

2.右键单击下载的 **.exe** 文件，该文件应称为 **“CDM...”** ，并选择 **“以管理员身份运行”** 。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Edison_FTDI_Driver.jpg)

3.点击 **“Extract”** 。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Edison_FTDI_Driver_Install.jpg)

4.点击 **“Next”** 。

5.看到下图所示时点击 **"Finish（完成）"** 。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Edison_FTDI_Driver_Install_ok.jpg)

6.下载 [Intel Edison Drivers](https://communities.intel.com/docs/DOC-23242) 安装所需的RNDIS，CDC和DFU驱动程序。

7.双击 **.exe** 文件开始安装。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Intel_Edison_Driver.jpg)

##   硬件连接
---
使用 26AWG Grove Cable 进行以下连接：

<table>
<tr>
<th>  Grove 模块
</th>
<th> 连接到
</th></tr>
<tr>
<td width="200px"> Temperature&amp;Humidity Sensor
</td>
<td width="100px"> I2C
</td></tr>
<tr>
<td width="200px"> Moisture Sensor
</td>
<td width="100px"> A1
</td></tr>
<tr>
<td width="200px"> Light Sensor
</td>
<td width="100px"> A2
</td></tr>
<tr>
<td width="200px"> UV Sensor
</td>
<td width="100px"> A3
</td></tr>
<tr>
<td width="200px"> PIR Motion Sensor
</td>
<td width="100px"> D7
</td></tr>
<tr>
<td width="200px"> Encoder
</td>
<td width="100px"> D2
</td></tr>
<tr>
<td width="200px"> Button
</td>
<td width="100px"> UART(D1)
</td></tr>
<tr>
<td width="200px"> LCD RGB Backlight
</td>
<td width="100px"> I2C
</td></tr>
<tr>
<td width="200px"> Relay
</td>
<td width="100px"> D5
</td></tr>
<tr>
<td width="200px"> Servo
</td>
<td width="100px"> D6
</td></tr>
<tr>
<td width="200px"> Buzzer
</td>
<td width="100px"> D4
</td></tr></table>

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Edison_Indoor_Wire_Figure.png)

##   运行示例
---
1.打开网站 [Grove_Indoor_Environment_Demo](https://github.com/Seeed-Studio/Grove_Indoor_Environment_Demo) 下载整个项目文件。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_Github_Demo.png)

2.单击 **Tools（工具） &gt; Serial Port（端口）** 并选择**Edison所在COM口**。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Import_Indoor_Kit_Demo.png)

3.点击 **Sketch（项目）&gt;Import Library…（加载库）&gt;Add .ZIP Library（添加一个 .ZIP 库）** 并选择步骤 1 中 下载的 **.ZIP** 文件。

4.点击 **File（文件）&gt;Examples（示例）&gt; Grove_Indoor_Environment_Demo** 加载示例，然后点击 **upload（上传）** 按钮。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Upload_Indoor_Kit_Demo.png)

5.打开 **Serial Monitor（串口监视器）**, 它会打印出传感器的信息。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_Serial_Monitor.png)

6.旋转编码器以检查 LCD 上的传感器值。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_Rotate_Encoder.png)

7.在 **“Send TextBox（文本框）”** 中, 您可以输入以下命令来操作传感器和执行器：

_set [sensor][condition:&gt;, &lt; or =][ threshold],[actuator]=[action]_

<table>
<tr>
<th>  示例
</th>
<th> 说明
</th></tr>
<tr>
<td width="300px"> _set temp&gt;40, relay=1_
</td>
<td width="500px"> 如果温度 &gt;40℃，继电器会接通。
</td></tr>
<tr>
<td width="300px"> _set temp&gt;40, sleep=1_
</td>
<td width="500px"> 如果温度 &gt;40℃，进入睡眠状态。
</td></tr>
<tr>
<td width="300px"> _set humi&gt;60, buzzer=1_
</td>
<td width="500px"> 如果湿度 &gt;60%，蜂鸣器鸣叫。
</td></tr>
<tr>
<td width="300px"> _set light&gt;600, servo=90_
</td>
<td width="500px"> 如果光照强度 &gt;600, 舵机转过 90°。
</td></tr>
<tr>
<td width="300px"> _set uv&gt;80, relay=0_
</td>
<td width="500px"> 如果 UV 强度 &gt;80, 继电器会断开。
</td></tr>
<tr>
<td width="300px"> _set pir=1, buzzer=1_
</td>
<td width="500px"> 如果检测到人，蜂鸣器鸣叫。
</td></tr>
<tr>
<td width="300px"> _set ms&gt;40, relay=1_
</td>
<td width="500px"> 如果湿度 &gt;40，继电器会接通。
</td></tr>
<tr>
<td width="300px"> _set ssid=name, psw=password_
</td>
<td width="500px"> 设置WiFi SSID和密码。您可以打开浏览器，跳转到串口监视器或 LCD 上显示的 IP 地址。 默认端口为88。例如：192.168.1.101:88。
</td></tr></table>

!!!Note:

*   命令应以“/ n”结尾，因此需要选中 **“NewLine”** （在串口监视器中）。

*   执行器只能由传感器控制。 如果A传感器想要控制执行器（由B传感器控制），B传感器应设置为 sleep 。

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_command.png)


8.连接好 WiFi。 打开串口监视器，并设置您的 ssid 和密码（如下）。 检查LCD或串行监视器上的本地IP。 在连接在同一网络上的设备上，打开浏览器，并转到上面的 IP 地址，就可以看到传感器的值。

_**警告：当访问Web服务器时，应添加端口号（88），例如：172.20.10.2:88。**_

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_SSID_PSW.png)

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_Local_IP.png)

![](https://github.com/SeeedDocument/Grove_Indoor_Environment_Kit_for_Edison/raw/master/img/Indoor_Kit_Web_Server.png)

##   资源下载
---
*   **[代码]**[Grove Indoor Environment Kit Source Code](https://github.com/Seeed-Studio/Grove_Indoor_Environment_Demo)

*   **[教程]**[Edison Getting Started Guide](https://communities.intel.com/community/makers/edison/getting-started)
