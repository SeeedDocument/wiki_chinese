---
title: SD Card shield V4.0
category: Shield
bzurl: https://seeedstudio.com/SD-Card-Shield-V4-p-1381.html
oldwikiname: SD_Card_shield_V4.0
prodimagename: SD_Card_Shield-v4.jpg
wikiurl: http://seeed.wiki/SD_Card_shield_V4.0
sku: 103030005
---

![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/SD_Card_Shield-v4.jpg)

SD Card shield V4.0 是给 Arduino 扩展存储空间的扩展板。用户可以通过 Arduino 的内置 SD 库来读/写 SD 卡。它支持 SD，SDHC 和 Micro SD 卡。它只会占用 Arduino 的 SPI 端口。与以前的版本相比，它将标准 SD 插槽和 Micro SD 插槽合并为一个标准插槽，可以通过随附的适配器使用Micro SD卡。您可以把这个扩展板插在使用其他引脚工作的扩展板上。此外，板载的 I2C 和 UART 端口能方便地与 Grove 模块连接。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1b900335pkSc5q&id=520859772674)

##  兼容性
----
我们已经生产了大量的扩展板，可以使您的平台板更加强大，但是并不是每个扩展板都与所有的平台板兼容，这里我们使用表格来说明这些板与平台板的兼容性。

!!!note
    请注意，下表中标识的"Not recommended"并不代表一定就不能兼容，可能您需要一些额外的操作，比如跳线、焊接。如此，部分标识不兼容的也是可能正常使用的。更多兼容性信息请联系我们的技术支持 techsupport@seeed.cc。

**点击查看大图**
[![](https://github.com/SeeedDocument/Seeed-WiKi/raw/master/docs/images/Shield%20Compatibility.png)](https://raw.githubusercontent.com/SeeedDocument/Seeed-WiKi/master/docs/images/Shield%20Compatibility.png)


## 创意应用
-----------------

If you want to make some awesome projects with SD Card Shield, here are some projects for your reference.

Here we introduce a project about [LinkIt ONE](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11172317909.10.129c772bbGNIJU&id=45453335551) using SD Card.

### Music Player with LinkIt One

![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/555a29dc85f7f.png)

This project uses Grove - Water Sensor to create a simple but effective solution to watering plants.

[Make it NOW!](http://www.seeedstudio.com/recipe/246-music-player-with-linkit-one.html)

[***More Awesome Projects by SD Card***](http://www.seeedstudio.com/recipe/index.php?query=SD+Card)

产品特性
--------

-   兼容标准 SD 卡，SDHC 卡和 TF 卡
-   板载 UART Grove 接口和 I2C Grove 接口
-   完全支持 SD 库 函数
-   占用端口最少，使用 SPI 端口
-   可以直接插在 Arduino 上使用

规格参数
--------------

<table border="1" cellspacing="0">
<tr>
<th scope="col">
项目
</th>
<th scope="col">
最小值
</th>
<th scope="col">
典型值
</th>
<th scope="col">
最大值
</th>
<th scope="col">
单位
</th>
</tr>
<tr align="center">
<th scope="row">
电压
</th>
<td>
3.5
</td>
<td>
5.0
</td>
<td>
5.5
</td>
<td>
V
</td>
</tr>
<tr align="center">
<th scope="row">
电流
</th>
<td>
0.159
</td>
<td>
100
</td>
<td>
200
</td>
<td>
mA
</td>
</tr>
<tr align="center">
<th scope="row">
支持卡类型
</th>
<td colspan="3">
SD card(<=32GB); Micro SD card(<=32GB); SDHC card(<=32GB)
</td>
<td>
/
</td>
</tr>
<tr align="center">
<th scope="row">
尺寸
</th>
<td colspan="3">
68.7x53.5x19.00
</td>
<td>
mm
</td>
</tr>
<tr align="center">
<th scope="row">
净重
</th>
<td colspan="3">
14.8
</td>
<td>
g
</td>
</tr>
</table>

硬件概述
-----------------

![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/Interface_FunctionV2.0.png)

**使用的 Arduino 引脚（使用 SD card）**

D4: SD_CS;

D11: SD_DI;

D12: SD_DO;

D13: SD_CLK.

!!!Note
    SD 卡格式可以是 FAT16 或 FAT32，SD 卡和 SDHC 卡大小不超过16GB。

使用方法
-----

下面是 SD card shield 的安装和使用方法。

### 硬件安装

1. 把 SD 卡插入插座，将 SD card shield 插入 Arduino。
2. 用 USB 线把 Arduino 连接到电脑上。

!!!Note
    当您使用 Micro SD 卡时，请将 Micro SD 卡插入适配器，然后将 Micro SD 卡适配器插入到插槽中，如下所示。

![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/SD_card_adopter.JPG)

连接好的硬件如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/Hardware_connection.JPG)

### 上传程序

1. 打开 Arduino IDE，然后进入菜单 **文件（File）>-示例（Example）>- SD >- Cardinfo** 打开例程。

    这个例子展示了如何使用 SD 库来获取您的 SD 卡的信息。当您不确定其工作与否时，这个例程可以用来测试。这个库中还有很多其他的例子，比如“ReadWrite”。你可以尝试一下。

    ![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/Open_SD_Card_code.jpg)

    下面是这段代码的简要介绍：

    首先检查 SD 卡是否工作。如果不是的话，会输出一些可能导致这个结果的原因。

    在 SD 卡正常工作的情况下，会打印 SD 卡的类型，然后打印 FAT-type 的类型和大小。

    最后，获取卡上找到的文件信息，例如名称，日期和大小（以字节为单位）。

2. 上传代码。

3. 观察结果，您可以在串口监视器中看到类似下图的信息。

    ![](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/img/SD_Card_Infor.jpg)

4. 如果发生错误，请检查之前的所有步骤，并确保 SD 卡正常工作。如果没有解决问题，请尝试更换 SD 卡。

!!!Note
    如果你的 SD 卡容量超过 4G，Arduino 默认代码将返回错误的 SD 容量。下面的代码可以解决这个问题。

**<span style="color:#ff0000">以下代码有问题！！！</span>**

```c
    /*
      SD card test

     This example shows how use the utility libraries on which the'
     SD library is based in order to get info about your SD card.
     Very useful for testing a card when you're not sure whether its working or not.

     The circuit:
      * SD card attached to SPI bus as follows:
     ** MOSI - pin 11 on Arduino Uno/Duemilanove/Diecimila
     ** MISO - pin 12 on Arduino Uno/Duemilanove/Diecimila
     ** CLK - pin 13 on Arduino Uno/Duemilanove/Diecimila
     ** CS - depends on your SD card shield or module.
     ** Pin 4 used here for consistency with other Arduino examples


     created  28 Mar 2011
     by Limor Fried
     modified 9 Apr 2012
     by Tom Igoe
     */
    // include the SD library:
    #include <SPI.h>
    #include <SD.h>

    // set up variables using the SD utility library functions:
    Sd2Card card;
    SdVolume volume;
    SdFile root;

    // change this to match your SD shield or module;
    // Arduino Ethernet shield: pin 4
    // Adafruit SD shields and modules: pin 10
    // Sparkfun SD shield: pin 8
    const int chipSelect = 4;

    void setup()
    {
      // Open serial communications and wait for port to open:
      Serial.begin(9600);
      while (!Serial) {
        ; // wait for serial port to connect. Needed for Leonardo only
      }


      Serial.print("\nInitializing SD card...");
      // On the Ethernet Shield, CS is pin 4. It's set as an output by default.
      // Note that even if it's not used as the CS pin, the hardware SS pin
      // (10 on most Arduino boards, 53 on the Mega) must be left as an output
      // or the SD library functions will not work.
      pinMode(10, OUTPUT);     // change this to 53 on a mega


      // we'll use the initialization code from the utility libraries
      // since we're just testing if the card is working!
      if (!card.init(SPI_HALF_SPEED, chipSelect)) {
        Serial.println("initialization failed. Things to check:");
        Serial.println("* is a card is inserted?");
        Serial.println("* Is your wiring correct?");
        Serial.println("* did you change the chipSelect pin to match your shield or module?");
        return;
      } else {
        Serial.println("Wiring is correct and a card is present.");
      }

      // print the type of card
      Serial.print("\nCard type: ");
      switch (card.type()) {
        case SD_CARD_TYPE_SD1:
          Serial.println("SD1");
          break;
        case SD_CARD_TYPE_SD2:
          Serial.println("SD2");
          break;
        case SD_CARD_TYPE_SDHC:
          Serial.println("SDHC");
          break;
        default:
          Serial.println("Unknown");
      }

      // Now we will try to open the 'volume'/'partition' - it should be FAT16 or FAT32
      if (!volume.init(card)) {
        Serial.println("Could not find FAT16/FAT32 partition.\nMake sure you've formatted the card");
        return;
      }


      // print the type and size of the first FAT-type volume

      uint64_t volumesize64;
      uint32_t volumesize32;
      Serial.print("\nVolume type is FAT");
      Serial.println(volume.fatType(), DEC);
      Serial.println();

      volumesize64 = volume.blocksPerCluster();    // clusters are collections of blocks
      volumesize64 *= volume.clusterCount();       // we'll have a lot of clusters
      volumesize64 *= 512;                            // SD card blocks are always 512 bytes

      Serial.print("Volume size (bytes): ");
      printLLNumber(volumesize64, DEC);
      Serial.println();

      Serial.print("Volume size (Kbytes): ");
      volumesize32 = volumesize64/1024;
      Serial.println(volumesize32);

      Serial.print("Volume size (Mbytes): ");
      volumesize32 /= 1024;
      Serial.println(volumesize32);
      /*uint64_t volumesize;
      Serial.print("\nVolume type is FAT");
      Serial.println(volume.fatType(), DEC);
      Serial.println();

      volumesize = volume.blocksPerCluster();    // clusters are collections of blocks
      volumesize *= volume.clusterCount();       // we'll have a lot of clusters
      volumesize *= 512;                            // SD card blocks are always 512 bytes
      Serial.print("Volume size (bytes): ");
      Serial.println(volumesize,DEC);
      Serial.print("Volume size (Kbytes): ");
      volumesize /= 1024;
      Serial.println(volumesize,DEC);
      Serial.print("Volume size (Mbytes): ");
      volumesize /= 1024;
      Serial.println(volumesize,DEC);
    */

      Serial.println("\nFiles found on the card (name, date and size in bytes): ");
      root.openRoot(volume);

      // list all files in the card with date and size
      root.ls(LS_R | LS_DATE | LS_SIZE);
    }


    void loop(void) {

    }
    void printLLNumber(uint64_t n, uint8_t base)
    {
      unsigned char buf[16 * sizeof(long)];
      unsigned int i = 0;

      if (n == 0)
      {
        Serial.print((char)'0');
        return;
      }

      while (n > 0)
      {
        buf[i++] = n % base;
        n /= base;
      }

      for (; i > 0; i--)
        Serial.print((char) (buf[i - 1] < 10 ?
          '0' + buf[i - 1] :
          'A' + buf[i - 1] - 10));
    }
```

资源下载
---------

- [SD Card Shield v4.0 Schematic](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/res/SD_Card_Shiled_v4.0.pdf)

- [SD Card Shield v4.0 Eagle File.zip](https://github.com/SeeedDocument/SD_Card_shield_V4.0/raw/master/res/PCBA-SD%20Card%20shield%20V4.0.zip)

- [SD Card Shield v4.0a Eagle File.zip](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/res/SD_Card_Shield_v4.0a.zip)

- [SD Card Shield v4.3 Eagle file.zip](https://raw.githubusercontent.com/SeeedDocument/SD_Card_shield_V4.0/master/res/SD_Card_Shield_v4.3_eagle_file.zip)



<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/SD_Card_shield_V4.0 -->
