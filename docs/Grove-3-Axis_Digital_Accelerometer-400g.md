---
title: Grove - 3-Axis Digital Accelerometer(±400g)
category: Sensor
bzurl: https://seeedstudio.com/Grove-3-Axis-Digital-Accelerometer(±400g)-p-1897.html
oldwikiname: Grove_-_3-Axis_Digital_Accelerometer(±400g)
prodimagename: Grove_3Axis_Accelerometer400g.jpg
bzprodimageurl: http://statics3.seeedstudio.com/images/product/grove 3Axis Accelerometer400g.jpg
wikiurl: http://seeed.wiki/Grove-3-Axis_Digital_Accelerometer-400g
sku: 101020071
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit, plat_bbg
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/img/Grove_3Axis_Accelerometer400g.jpg)

H3LIS331DL 是属于 “nano” 系列的低功耗高性能3轴线性加速度计，它具有 I2C 接口。该模块具有超低功耗操作模式，可实现高级省电和智能睡眠唤醒功能。H3LIS331DL 具有 ±100g/±200 g/±400 g 的用户可选的量程，能够测量加速度并且输出数据速率从 0.5Hz 到 1kHz。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a230r.1.14.11.413793f10ZQExQ&id=531816050963&ns=1&abbucket=1#detail)

## 产品特性
--------

-   工作电压 : 3.3V - 5V
-   Grove 接口
-   3 轴感应
-   小巧的包装 : 3×3×1mm TFLGA
-   低功耗
-   ±100g /±200 g /±400 g 的用户可选的量程
-   I2C 数字输出接口
-   10000 g 冲击承受能力
-   符合 ECOPACK®RoHS 和 “Green” 标准

!!!Tip
    关于 Grove 模块的更多信息请点击 [Grove System](http://seeed.wiki/Grove_System/)

## 创意应用
-----------------

-   冲击探测器
-   震荡探测器

Platforms Supported
-------------------

## 使用方法
-----

下面我们向您展示如何通过这个加速度计读取原始数据。

1. 将其插入 [Grove - Base Shield](http://www.seeedstudio.com/depot/grove-base-shield-p-754.html?cPath=132_134) 的 **I2C** 端口。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/img/Grove-3-Axis_Digital_Accelerometer_connect_BaseBoard.jpg)

2. 下载库文件 [Digital Accelerometer(±400g) Library](https://github.com/Seeed-Studio/Grove_3Axis_Digital_Accelerometer_H3LIS331DL) 并将其解压到 Arduino 安装文件夹中的 **arduino-1.0\\libraries** 中。

3. 通过以下路径 : **File(文件) -> Example(示例) ->Grove_3Axis_Digital_Accelerometer_H3LIS331DL->H3LIS331DL_AdjVal** 打开演示代码。这个示例通过调整 H3LIS331DL 的原始数据以使其更加精确。

4. 上传代码并打开串口监视器。

5. 打开串口监视器得到参考的调整值。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/img/Adjust_value_of_Accelerometer.jpg)

6. 通过以下路径 : **File(文件) -> Example(示例) ->Grove_3Axis_Digital_Accelerometer_H3LIS331DL->H3LIS331DL_Demo** 打开代码。然后根据 H3LIS331DL_AdjVal Sketch 中获得的数据修改 VAL_X_AXIS/VAL_Y_AXIS/VAL_Z_AXIS。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/img/Redefine_the_VAL_of_Accelerometer.jpg)

7. 上传代码并打开串口监视器，打开串口监视器检查结果。
![](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/img/Raw_data_of_H3LIS331DL.jpg)

## 资源下载
---------

-   **[Eagle 文件]** [Grove - 3-Axis Digital Accelerometer(±400g) Eagle File](https://raw.githubusercontent.com/SeeedDocument/Grove-3-Axis_Digital_Accelerometer-400g/master/res/Grove-3-Axis_Digital_Accelerometer-400g-v1.0.zip)
-   **[库文件]** [github repository for 3-Axis Digital Accelerometer(±400g)](https://github.com/Seeed-Studio/Grove_3Axis_Digital_Accelerometer_H3LIS331DL)
-   **[芯片数据手册]** [H3LIS331DL Datasheet PDF](http://www.st.com/web/en/resource/technical/document/datasheet/DM00053090.pdf)


<!-- This Markdown file was created from http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(±400g) -->
