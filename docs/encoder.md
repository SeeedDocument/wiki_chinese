## 简介
Grove – Encoder 是一个增量旋转编码器。它将旋转信号编码成有含义的电子脉冲输出信号。这个模块也属于Grove系列，有标准的Grove接口。
当你的项目需要添加一个旋钮时，比如说音量旋钮，数字旋钮等，这个产品是一个不错的选择。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_Encoder/1.png)
 
## 产品特性

* 增量式编码器
* Grove接口
* 360度旋转


## 规格参数

|项目|最小值|标准值|最大值|单位|
|----|------|------|------|----|
|Voltage|	4.5 |5|	5.5	|V|
|Current|	10	|20|	30|	mA|
|Dimension||	20x 20||	mm|
|Net Weight||	12||	g|

## 使用示例

Grove – Encoder使用SeeedStudio编写的Encoder库还是非常好用的，只需要把它接在BaseShield的D2接口上，你就可以开始使用了
接下来的这个Demo，就是展示了如何做一个圆形的LED灯条。

1.这个圆形的LED灯条由Encoder和Grove – Circular LED两个模块组成，把这两个模块，安装下图所示接在BaseShield上。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_Encoder/2.png)

2.下载TimeOne库、Encoder库、Circular LED库，并安装在你的Arduino库中

3.重启并打开Arduino IDE，打开 **File->Examples->Encoder->EncodeCircuiBar**。代码如下所示

```arduino
#include <CircularLED.h>
#include <Encoder.h>
#include <TimerOne.h>
CircularLED circularLED;
unsigned int LED[24];
int index_LED;
void setup()
{
    encoder.Timer_init();
}
void loop()
{
    if (encoder.rotate_flag ==1)
    {
        if (encoder.direct==1)
        {
            index_LED++;
            if (index_LED>23)
            index_LED=24;
            SenttocircularBar(index_LED);
        }
        else
        {
            index_LED--;
            if(index_LED<0)
            index_LED=0;
            SenttocircularBar(index_LED);
        }
        encoder.rotate_flag =0;
    }
}
void SenttocircularBar(int index)
{
    for (int i=0;i<24;i++)
    {
        if (i<index)
        {
            LED[i]=0xff;
        }
        else
        LED[i]=0;
    }
    circularLED.CircularLEDWrite(LED);
}
```

4.下载代码到你的Arduino或Seeeduino板子里。如果你不知道怎样下载，请点击[这里](http://www.seeedstudio.com/wiki/Upload_Code)。
最终结果如下图所示。

![](https://raw.githubusercontent.com/SeeedDocument/wiki_chinese/master/docs/images/Grove_Encoder/3.png)
 
!!! warning "注意"
    当Grove – Encoder 被按下时，也会产生一个信号，但是基于Grove线的限制，并没有将该信号引出来。
    
## 资源链接

* [传感器参数表](http://www.seeedstudio.com/wiki/File:Encoder_Spe.zip)
* [Arduino 论坛上的示例](http://www.arduino.cc/playground/Main/RotaryEncoders)
* [TimeOne Lib](http://www.seeedstudio.com/wiki/File:TimerOne.zip)
* [Encoder Lib](http://www.seeedstudio.com/wiki/File:Encoder.zip)
* [Grove-Encoder Eagle 文件](http://www.seeedstudio.com/wiki/File:Grove-Encoder_eagle_files.zip)
