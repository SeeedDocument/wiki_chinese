---
name: How to install an Arduino library
category: Tutorial
bzurl: 
oldwikiname:
prodimagename: 
wikiurl: http://wiki.seeedstudio.com/cn/How_to_install_Arduino_Library
sku: 

---

!!!Note
    - 此教程是基于 Arduino 1.6.9.

这里我们将向您介绍如何安装Arduino库。您可能已经注意到，我们几乎所有的库都存储在Github上。当产品需要时，我们将提供Arduino库。对于一些简单的产品，它不需要编写一个库，如Grove - Button。    

首先，产品页面上有一个下载库按钮。类似于以下内容：

[![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Grove_OLED_1.12/master/images/library.png)](https://github.com/Seeed-Studio/OLED_Display_96X96/archive/master.zip)

点击按钮开始下载。数秒后秒你会得到一个数据包。

如果您点击按钮后获得Github页面，则可以单击 **Clond or download > Download ZIP** 按键来获取库文件。

![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Tutorial_Add_Arduino_Library/master/images/github_download.png)

然后打开您的Arduino IDE，单击**Sketch (项目)> Include Library (加载库)> Add .ZIP Library（添加一个zip库）**


![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Tutorial_Add_Arduino_Library/master/images/add_library_1.png)

然后我们检查一下库是否正确安装。

点击 **File（文件） > Example （示例） > OLED_Display_96x96-master > OLED_Hello_World** 打开一个例子，点击验证按钮，如果没有错误，祝贺，库完美安装。


![enter image description here](https://raw.githubusercontent.com/SeeedDocument/Tutorial_Add_Arduino_Library/master/images/add_library_2.png)
