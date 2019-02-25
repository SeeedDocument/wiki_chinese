---
name: WiFi Serial Transceiver Module
category: MakerPro
bzurl: https://www.seeedstudio.com/WiFi-Serial-Transceiver-Module-w-ESP8266-p-1994.html
oldwikiname: WiFi Serial Transceiver Module
prodimagename: WiFi%20Serial%20Transceiver%20Module.jpg
wikiurl: http://wiki.seeedstudio.com/cn/WiFi_Serial_Transceiver_Module
sku: 114990085
---
![](https://github.com/SeeedDocument/WiFi_Serial_Transceiver_Module/raw/master/img/WiFi%20Serial%20Transceiver%20Module.jpg)

在本教程中，我们将使用一个 seeeduino 来控制 ESP8266 WiFi 模块从互联网上请求静态页面。这是 TCP 套接字的基本使用，其他使用方法法请参考模块的 AT 命令手册。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4995b257N5JMgz&id=535356986264)

**材料清单（可点击购买） :**

- [Seeeduino V4.2](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.21a57a901Lb0a6&id=45721222112) / Arduino Uno
- [ESP8266 Serial WiFi module](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.9.4995b257N5JMgz&id=535356986264)
- [UartSBee v4](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.617dc90bsvOpdF&id=520629042670) / other USB to TTL converter

!!!Note
    由于 seeeduino 板上只有一个硬串口，所以我们使用了一个软件串口来打印一些调试信息。但软件串口的局限性在于它不能以高于 19200 的波特率进行通讯。因此 ESP 模块的部分输出将因为 ESP 模块的波特率 57600 高于软件串口19200的波特率而丢包。如果您的主板有多个硬串口 (例如Arduino Mega 2560)，情况会好很多。

## 使用方法
---
- **步骤 1**: 如下图所示连接模块

![](https://github.com/SeeedDocument/WiFi_Serial_Transceiver_Module/raw/master/img/Wifi_connection.jpg)

- **步骤 2**: 编程

   - 打开 Arduino IDE 然后创建一个新的工程;
   - 编译并上传以下代码 (根据您个人情况设置 SSID 和 PASS 宏命令);

```c
#include <SoftwareSerial.h>
   #define SSID "xxxxxxxx"
   #define PASS "xxxxxxxx"
   #define DST_IP "220.181.111.85" //baidu.com
   SoftwareSerial dbgSerial(10, 11); // RX, TX
   void setup()
   {
     // Open serial communications and wait for port to open:
     Serial.begin(57600);
     Serial.setTimeout(5000);
     dbgSerial.begin(9600); //can't be faster than 19200 for softserial
     dbgSerial.println("ESP8266 Demo");
     //test if the module is ready
     Serial.println("AT+RST");
     delay(1000);
     if(Serial.find("ready"))
     {
       dbgSerial.println("Module is ready");
     }
     else
     {
       dbgSerial.println("Module have no response.");
       while(1);
     }
     delay(1000);
     //connect to the wifi
     boolean connected=false;
     for(int i=0;i<5;i++)
     {
       if(connectWiFi())
       {
         connected = true;
         break;
       }
     }
     if (!connected){while(1);}
     delay(5000);
     //print the ip addr
     /*Serial.println("AT+CIFSR");
     dbgSerial.println("ip address:");
     while (Serial.available())
     dbgSerial.write(Serial.read());*/
     //set the single connection mode
     Serial.println("AT+CIPMUX=0");
   }
   void loop()
   {
     String cmd = "AT+CIPSTART=\"TCP\",\"";
     cmd += DST_IP;
     cmd += "\",80";
     Serial.println(cmd);
     dbgSerial.println(cmd);
     if(Serial.find("Error")) return;
     cmd = "GET / HTTP/1.0\r\n\r\n";
     Serial.print("AT+CIPSEND=");
     Serial.println(cmd.length());
     if(Serial.find(">"))
     {
       dbgSerial.print(">");
       }else
       {
         Serial.println("AT+CIPCLOSE");
         dbgSerial.println("connect timeout");
         delay(1000);
         return;
       }
       Serial.print(cmd);
       delay(2000);
       //Serial.find("+IPD");
       while (Serial.available())
       {
         char c = Serial.read();
         dbgSerial.write(c);
         if(c=='\r') dbgSerial.print('\n');
       }
       dbgSerial.println("====");
       delay(1000);
     }
     boolean connectWiFi()
     {
       Serial.println("AT+CWMODE=1");
       String cmd="AT+CWJAP=\"";
       cmd+=SSID;
       cmd+="\",\"";
       cmd+=PASS;
       cmd+="\"";
       dbgSerial.println(cmd);
       Serial.println(cmd);
       delay(2000);
       if(Serial.find("OK"))
       {
         dbgSerial.println("OK, Connected to WiFi.");
         return true;
         }else
         {
           dbgSerial.println("Can not connect to the WiFi.");
           return false;
         }
       }
```

- **步骤 3**: 打开串口监视器，按下 seeeduino 的复位按钮，将会看到输出。

## 相关项目
---
[Recipe Community](http://www.seeedstudio.com/recipe/) is an awesome place where makers share their amazing works here. Our makers have made a lot of awesome projects with esp8266, check this out!

**WiFi Scanner -Know the WiFi Signal around you**

![](https://github.com/SeeedDocument/WiFi_Serial_Transceiver_Module/raw/master/img/Recipe-WiFi_Scanner-Know_the_WiFi_Signal_around_you.jpg)

Build your own Wifi Scanner with few simple steps, all you need to do is prepare:

- A NodeMcu Dev. Board
- An I2C OLED.
- Some cables
- And most importantly, a HOT HEART ON ESP8266

[So, why not make one for yourself?](http://www.seeed.cc/project_detail.html?id=220)

**Primary IoT Make with NodeMcu >ESP8266<**

![](https://github.com/SeeedDocument/WiFi_Serial_Transceiver_Module/raw/master/img/Recipe-Primary_IoT_Make_with_NodeMcu--ESP8266--.jpg)

An online Temperature&Humidity Monitor made with:

- A NodeMcu Dev. Board
- Grove - Temp&Humi Sensor
- Some cables

Another easy trick, [why not make one for yourself?](http://www.seeed.cc/project_detail.html?id=232)

Na, not enough? More [Awesome Projects with ESP8266](http://www.seeed.cc/discover.html?t=wio).

Even more Awesome Projects On [Recipe](http://www.seeed.cc/projects.html#recipe)
