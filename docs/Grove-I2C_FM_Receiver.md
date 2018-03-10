---
title: Grove - I2C FM Receiver
category: Sensor
bzurl: https://seeedstudio.com/Grove-I2C-FM-Receiver-p-1953.html
oldwikiname: Grove_-_I2C_FM_Receiver
prodimagename: Grove-I2C_FM_Receiver_Photo.jpg
wikiurl: http://wiki.seeedstudio.com/cn/Grove-I2C_FM_Receiver
sku: 107020006
tags: grove_i2c, io_3v3, io_5v, plat_duino, plat_linkit
---

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/img/Grove-I2C_FM_Receiver_Photo.jpg)

Grove-I2C FM Receiver 是一款宽带 FM 接收模块，该模块基于 RDA5807M。RDA5807M 系列是具有完全集成的合成器的最新一代单芯片广播 FM 立体声收音机调谐器。RDA5807M 系列具有功能强大的低中频数字音频处理器。Grove-I2C FM Receiver 有一个耳机插孔，因此可以连接到耳机或有源音箱。

[![](https://github.com/SeeedDocument/wiki_chinese/raw/master/docs/images/click_to_buy.PNG)](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1b276672htFUhC&id=45506822801)

版本
---------------

| 版次                      | 描述             | 发布日期  |
|-------------------------------|-------------------------|---------------|
| Grove - I2C FM Receiver v1.0  | 初始版本  |               |
| Grove - I2C FM Receiver v1.1  | 修复了J3的错误 - DFM  | 2011 年 12 月 2 日   |


产品特性
--------

-   Grove 接口
-   支持全球频段：50-115MHz
-   支持 RDS / RBDS
-   低功耗
-   耳机接口
-   数字自动增益控制
-   输入电压：3.3V - 5V

!!!Tip
    有关 Grove 模块的更多信息，请参考 [Grove 系统](http://wiki.seeedstudio.com/cn/Grove_System/)。

Platforms Supported
-------------------

快速入门
-----

### 连接
在这里，我们将向您展示 Grove - I2C FM Receiver 如何工作。首先，你需要准备下面的东西：

| Seeeduino Lotus | Grove - I2C FM Receiver | Grove - Button |Grove - Rotary|耳机|
|--------------|----------------------|-----------------|----------------------|-----------------|
|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/img/lotus_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/img/Grove%20I2C%20FM_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/img/bgpush%20_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/img/rotary_s.jpg)|![enter image description here](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/img/eraphone_s.png)|
|[点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10678284.0.0.6730c62206p61l&id=555795386924)|[点击购买](https://item.taobao.com/item.htm?spm=a1z38n.10677092.0.0.1b276672htFUhC&id=45506822801)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.15.2d0274adEibROB&id=531838497696)|[点击购买](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-17789056523.13.4b89b371gSKuDj&id=45531021242)|NA|


![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/img/Grove-I2C_FM_Receiver_Usage.jpg)

### 软件
- 请参考 [如何安装 Arduino 库](http://wiki.seeed.cc/How_to_install_Arduino_Library/) 来安装库。

- 下载 [Grove-I2C FM Receiver library](https://github.com/mathertel/Radio/) 然后安装库。

- 复制下面的代码到 Arduino IDE 的新窗口并上传到 Seeeduino Lotus。

```c++
/*
 * I2C_FM.ino
 * Demo code for the Grove-I2C_FM_Receiver module
 *
 * Copyright (c) 2012 seeed technology inc.
 * Website    : www.seeed.cc
 * Author     : Jack Shao (jacky.shaoxg@gmail.com)
 * Create Time: Jul 2014
 * Change Log :
 *
 * The MIT License (MIT)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
//
/*
 * Modifications to the I2C_FM.ino by Mel Patrick - Wabbit Wanch Design
 * Modified routines for scanning UP or DOWN through the FM band
 * Modified routine to test for signal strength of received station
 * Modified routines to support bass boost and MONO signal
 * RSSI, read it too soon after setting a station and you get a small value
 * so it's better to wait a bit (50ms) and try it. minSignalStrength will
 * skip locking on a station with a weak signal (you could set the MONO bit) to get
 * better reception on these stations.
 */
#include <Arduino.h>
#include <Wire.h>
#include <EEPROM.h>

#define BTNUP          2// used for seeking UP (normally CLOSED push button)
#define VOL_POT        A0// volume POT LOG taper 10K
#define BTNDN          3// used for seeking DOWN (normally CLOSED push button)

uint16_t gChipID = 0;
uint8_t RDA5807P_REGW[10];

#define I2C_ADDR       0x10

#define READ	        1
#define WRITE	        0

#define ADRW 	        0x20
#define ADRR 	        0x21
//

//#define                 _SHARE_CRYSTAL_24MHz_
//#define                 _SHARE_CRYSTAL_12MHz_
#define                 _SHARE_CRYSTAL_32KHz_
//#define                 _FM_STEP_50K_

//5807M,5807FP,5807NN,5807NP
uint8_t RDA5807N_initialization_reg[]={
#if defined(_SHARE_CRYSTAL_24MHz_)
  0xC4, 0x51, //02H:
#elif defined(_SHARE_CRYSTAL_12MHz_)
  0xC4, 0x11, //02H:
#elif defined(_SHARE_CRYSTAL_32KHz_)
  0xC4, 0x01,//change 01 to 05 enables the RDS/RBDS
#else
  0xC0, 0x01,
#endif
  0x00, 0x00,
  0x04, 0x00,
  0xC3, 0xad,  //05h
  0x60, 0x00,
  0x42, 0x12,
  0x00, 0x00,
  0x00, 0x00,
  0x00, 0x00,  //0x0ah
  0x00, 0x00,
  0x00, 0x00,
  0x00, 0x00,
  0x00, 0x00,
  0x00, 0x00,
  0x00, 0x00,  //0x10h
  0x00, 0x19,
  0x2a, 0x11,
  0xB0, 0x42,
  0x2A, 0x11,  //
  0xb8, 0x31,  //0x15h
  0xc0, 0x00,
  0x2a, 0x91,
  0x94, 0x00,
  0x00, 0xa8,
  0xc4, 0x00,  //0x1ah
  0xF7, 0xcF,
  0x12, 0x14,  //0x1ch
  0x80, 0x6F,
  0x46, 0x08,
  0x00, 0x86,  //10000110
  0x06, 0x61,  //0x20H
  0x00, 0x00,
  0x10, 0x9E,
  0x23, 0xC8,
  0x04, 0x06,
  0x0E, 0x1C,  //0x25H     //0x04 0x08
};

int16_t freq = 10110;
uint16_t vol = 1;
//
// added items - Mel
boolean bassBit = true;// bass boost
boolean monoBit = false;// force MONO not stereo
const boolean seekUP = true;
const boolean seekDN = false;
uint8_t minSignalStrength = 36;// anything below this probably set a MONO flag for better reception
uint8_t signalStrength;
long previousMillis = 0;// last time the function was called
long interval = 2000;// interval for the signal level function (2 seconds)
int8_t stationStep = 10;// kHz steps bewteen the stations (North America = 10)
boolean hasVolumePot = false;// flag if you have a POT attached or not
//
void setup()
{
  Wire.begin();
  loadDefaults();// load any defaults from previous radio settings
  Serial.begin(9600);
  Serial.println("Started");
  //=======================
  //rda5807 power on
  RDA5807P_PowerOnReset();
  RDA5807P_SetMute(false);

  //=======================
  pinMode(BTNUP, INPUT_PULLUP);
  pinMode(VOL_POT, INPUT);
  pinMode(BTNDN, INPUT_PULLUP);
  //=======================
  RDA5807P_SetVolumeLevel(vol);// use this if you don't have a POT for volume attached (0-15)
  RDA5807P_SetFreq( freq );
}

void loop()
{
  unsigned long currentMillis = millis();

  if(currentMillis - previousMillis > interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;
    showSignalStrength();
  }
  //
  if (digitalRead(BTNUP) == 1)
  {
    delay(100);
    if (digitalRead(BTNUP) == 1)
      fmSeek(seekUP);
    while(digitalRead(BTNUP) == 1);
  }
  if (digitalRead(BTNDN) == 1)
  {
    delay(100);
    if (digitalRead(BTNDN) == 1)
      fmSeek(seekDN);
    while(digitalRead(BTNDN) == 1);
  }
  if (hasVolumePot == true) setVolume();// use this to read the POT
}
//
void setVolume() {
  unsigned int temp_vol;
  temp_vol = analogRead( VOL_POT );
  if (abs(temp_vol - vol)>5)
  {
    if (vol != temp_vol) {// don't bother changing the volume if unless the pot moves
      vol = temp_vol;
      unsigned char hex_vol = map(vol, 0, 1023, 0, 0xf);
      RDA5807P_SetVolumeLevel(hex_vol);
      saveDefaults();// save new volume to EEPROM
    }
  }
}
//
void fmSeek(boolean theDir) {
  int signalStrength;
  if (!theDir) {
    Serial.println("Start seeking down...");
  }
  else
  {
    Serial.println("Start seeking up...");
  }
  do {
    do{
      if (theDir == seekUP) {
        freq += stationStep;
      }
      else
      {
        freq -= stationStep;
      }
      if (freq > 10800) freq = 8800;
      if (freq < 8800) freq = 10800;
      //Serial.println(freq);
    }
    while(!RDA5807P_ValidStop(freq));
    delay(50);
    signalStrength = RDA5807P_GetSigLvl(freq);// max is 63 according to Data sheet, but I've seen more
  }
  while (signalStrength < minSignalStrength);// minimum signal strength, keep looking
  showRadioStation();
  saveDefaults();// save new station selection to EEPROM
}
//
void showRadioStation() {
  Serial.print("Stable Freq:");
  Serial.print(((float)freq)/100.0f);
  Serial.println("MHz");
}
//
void showSignalStrength() {
  signalStrength = RDA5807P_GetSigLvl(freq);// max is 63...as noted
  Serial.print("Signal Strength: ");
  Serial.println(signalStrength);
}

//===========================================================
// FM functions
//===========================================================
unsigned char OperationRDAFM_2w(unsigned char operation, unsigned char *data, int numBytes)
{
  if(operation == READ)
  {
    Wire.requestFrom(I2C_ADDR, numBytes);
    for(int i=0;i<numBytes;i++)
    {
      *data++ = Wire.read();
    }
  }
  else
  {
    Wire.beginTransmission(I2C_ADDR);
    for(int i=0;i<numBytes;i++)
    {
      Wire.write(*data++);
    }
    Wire.endTransmission();
  }
  return 0;
}


/**
 * @brief Reset RDA5807P while power on RDA5807P
 * @author RDA RDA Ri'an Zeng
 * @date 2008-11-05
 * @param void
 * @return void
 * @retval
 */
void  RDA5807P_PowerOnReset(void)
{
  RDA5807P_Intialization();
}

/**
 * @brief RDA5807P power off function
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param void
 * @return void
 * @retval
 */
void  RDA5807P_PowerOffProc(void)
{
  RDA5807P_REGW[1] &= (~1);
  OperationRDAFM_2w(WRITE, &(RDA5807P_REGW[0]), 2);
}

/**
 * @brief Set RDA5807P into mute mode
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param bool mute: if mute is true,then set mute; if mute is false,then set no mute
 * @return void
 * @retval
 */
void RDA5807P_SetMute(boolean mute)
{
  if(mute)
    RDA5807P_REGW[0] &=  ~(1<<6);
  else
    RDA5807P_REGW[0] |= 1<<6;
  RDA5807P_REGW[0] |= monoBit<<5;
  RDA5807P_REGW[0] |= bassBit<<4;
  OperationRDAFM_2w(WRITE, &(RDA5807P_REGW[0]), 2);//RDA5807M_REGW
  delay(50);    //Dealy 50 ms
}
//
/*************************************************
 * @brief Set frequency function
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param int16_t curFreq:frequency value
 * @return void
 * @retval
 ***********************************************/
void RDA5807P_SetFreq(int16_t curFreq)
{
  uint16_t curChan;
  curChan=RDA5807P_FreqToChan(curFreq);

  if((curFreq >= 6500)&&(curFreq < 7600))
  {
    RDA5807P_REGW[3] = 0x0c;
  }
  else if((curFreq >= 7600)&&(curFreq < 10800))
  {
    RDA5807P_REGW[3] = 0x08;// sets the BAND bits (00xx = 87-108, 01xx=76-91, 10xx=76-108, 11xx=65-76
    // for north america this must be set to 10xx for some unknown reason
  }
  //SetNoMute
  RDA5807P_REGW[0] |= 1<<6;
  RDA5807P_REGW[0] |= monoBit<<5;
  RDA5807P_REGW[0] |= bassBit<<4;
  //handleBits();
  RDA5807P_REGW[2]=curChan>>2;
  RDA5807P_REGW[3]=(((curChan&0x0003)<<6)|0x10) | (RDA5807P_REGW[3]&0x0f);    //set tune bit

  OperationRDAFM_2w(WRITE, &(RDA5807P_REGW[0]), 4);
  delay(50);     //Delay five ms
  showRadioStation();
}
//
/**
 * @brief Station judge for auto search
 * @In auto search mode,uses this function to judge the frequency if has a station
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param int16_t freq:frequency value
 * @return bool: if return true,the frequency has a true station;otherwise doesn't have a station
 * @retval
 */
boolean RDA5807P_ValidStop(int freq)
{
  uint8_t RDA5807P_reg_data[4]={
    0                                                  };
  uint8_t falseStation = 0;
  uint8_t i=0;
  uint16_t curChan;

  if((freq >= 6500)&&(freq < 7600))
  {
    RDA5807P_REGW[3] = 0x0c;
  }
  else if((freq >= 7600)&&(freq < 10800))
  {
    RDA5807P_REGW[3] = 0x08;// sets the BAND bits (00xx = 87-108, 01xx=76-91, 10xx=76-108, 11xx=65-76
    // for north america this must be set to 10xx for some unknown reason
  }
  curChan=RDA5807P_FreqToChan(freq);
  //SetNoMute bit 9 is seek direction (0=seek down, 1=seek up).
  //02H 14
  RDA5807P_REGW[0] |=	1<<6;// reg zero is bits 15 to bit 8 (this shifts to bit 14)
  RDA5807P_REGW[0] |= monoBit<<5;
  RDA5807P_REGW[0] |= bassBit<<4;
  //handleBits();
  RDA5807P_reg_data[0]=RDA5807P_REGW[0];
  RDA5807P_reg_data[1]=RDA5807P_REGW[1];
  RDA5807P_reg_data[2]=curChan>>2;//03H 15:8 CHAN
  RDA5807P_reg_data[3]=(((curChan&0x0003)<<6)|0x10) | (RDA5807P_REGW[3]&0x0f);//
  OperationRDAFM_2w(WRITE,&(RDA5807P_reg_data[0]), 4);

  delay(50);    //Dealy 25 ms

  if (0x5808 == gChipID)
    OperationRDAFM_2w(READ,&(RDA5807P_reg_data[0]), 4);	//
  else
  {
    do
    {
      i++;
      if(i>5) return 0;

      delay(30);
      //read REG0A&0B
      OperationRDAFM_2w(READ,&(RDA5807P_reg_data[0]), 4);
    }
    while((RDA5807P_reg_data[0]&0x40)==0);
  }

  //check FM_TRUE
  if((RDA5807P_reg_data[2] &0x01)==0) falseStation=1;//0B 8  FM TRUE

  if(freq==9600) falseStation=1;// North America - if scanning DOWN, the radio will lock on 9600 for some reason!
  delay(50);
  if (falseStation==1)
    return 0;
  else
    return 1;
}

/**
 * @brief Get the signal level(RSSI) of the current frequency
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param int16_t curf:frequency value
 * @return uint8_t: the signal level(RSSI)
 * @retval
 */
uint8_t RDA5807P_GetSigLvl( int16_t curf )
{
  uint8_t RDA5807P_reg_data[4]={
    0                                                  };
  OperationRDAFM_2w(READ,&(RDA5807P_reg_data[0]), 4);
  delay(50);    //Delay 50 ms
  return  (RDA5807P_reg_data[2]>>1);  /*??rssi*/
}

/**
 * @brief Set FM volume
 * @It has better use the system volume operation to replace this function
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param uint8_t level: volume value
 * @return void
 * @retval
 */
void RDA5807P_SetVolumeLevel(uint8_t level)
{
  uint8_t RDA5807P_reg_data[8];
  uint8_t i = 0;

  for (i=0;i<8;i++)
    RDA5807P_reg_data[i] = RDA5807P_REGW[i];

  RDA5807P_reg_data[7]=(( RDA5807P_REGW[7] & 0xf0 ) | (level & 0x0f));

  RDA5807P_reg_data[3] &= (~(0x10));//disable tune

  OperationRDAFM_2w(WRITE, &(RDA5807P_reg_data[0]), 8);
  delay(50);    //Dealy 50 ms
}

/**
 * @brief Initialize RDA5807P
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param void
 * @return bool:if true,the operation is successful;otherwise is failed
 * @retval
 **/
boolean  RDA5807P_Intialization(void)
{
  uint8_t error_ind = 0;
  uint8_t RDA5807P_REGR[10]={
    0x0                                                  };
  uint8_t i = 0;

  RDA5807P_REGW[0] = 0x00;
  RDA5807P_REGW[0] |= monoBit<<5;
  RDA5807P_REGW[0] |= bassBit<<4;
  RDA5807P_REGW[1] = 0x02;

  error_ind = OperationRDAFM_2w(WRITE, (uint8_t *)&RDA5807P_REGW[0], 2);//soft reset
  delay(50);

  error_ind = OperationRDAFM_2w(READ, (uint8_t *)&RDA5807P_REGR[0], 10);
  delay(50);

  gChipID = RDA5807P_REGR[8];
  gChipID = ((gChipID << 8) | RDA5807P_REGR[9]);

  Serial.print("Chip ID: 0x");
  Serial.println(gChipID, HEX);

  for (i=0;i<8;i++) {
    RDA5807P_REGW[i] = RDA5807N_initialization_reg[i];
  }

  error_ind = OperationRDAFM_2w(WRITE, (uint8_t *)&RDA5807N_initialization_reg[0], 2); //power up
  delay(600);
  //Serial.println(sizeof(RDA5807N_initialization_reg));
  error_ind = OperationRDAFM_2w(WRITE, (uint8_t *)&RDA5807N_initialization_reg[0], sizeof(RDA5807N_initialization_reg));

  delay(50);         //Dealy 50 ms

  if (error_ind )
    return 0;
  else
    return 1;
}
//
/**
 * @brief Cover the frequency to channel value
 * @author RDA Ri'an Zeng
 * @date 2008-11-05
 * @param uint16 frequency:covered frequency
 * @return uint16: channel value
 * @retval
 * In the United States, frequency-modulated broadcasting stations operate in a frequency band extending from 87.8 MHz to 108.0 MHz,
 * for a total of 20.2 MHz. It is divided into 101 channels, each 0.2 MHz wide, designated "channel 200" through "channel 300."
 * In actual practice, no one (except the FCC) uses these channel numbers; the frequencies are used instead.
 */
uint16_t RDA5807P_FreqToChan(uint16_t frequency) {
  uint8_t channelSpacing = 10;
  uint16_t channel = 0;

  if((frequency >= 6500)&&(frequency < 7600))
  {
    channel = (frequency - 6500)/channelSpacing;
  }
  else if((frequency >= 7600)&&(frequency < 10800))
  {
    channel = (frequency - 7600)/channelSpacing;
  }
  return (channel);
}
//
void loadDefaults() {
  char myCode[9] = "Grove_FM";
  char myInit[9] = "blank123";
  /*
  * byte map in EEPROM
   * 8, 9 the default frequency for a reboot
   * 10, 11 current preset volume of the radio (used if no pot is attached)
   */
  for (int i=0; i < 8; i++) {
    myInit[i] = EEPROM.read(i);// read out to see if the thing is INITIALIZED
  }
  if (strcmp(myCode, myInit) == 0) {// if this is ZERO (we previously wrote some), then read the values
    freq = epReadINT(8);// read back the INT for frequency from eeprom 8 and 9 (two bytes for an INT)
    if (!hasVolumePot) vol = epReadINT(10);// read back the volume setting but don't use it unless flag is false
  }
  else// we don't have any defaults, so we have to save some first
  {
    for (int i=0; i < 8; i++) {
      EEPROM.write(i, myCode[i]);// write this to EEPROM to show we have it saved
    }
    saveDefaults();// write the current default settings
  }
}
//
void saveDefaults() {
  epWriteINT(8, freq);// write the two bytes for INT for a reboot
  epWriteINT(10, vol);// write the current volume POT setting
}
//
void epWriteINT(int where, int theVal) {
  union uData
  {
    byte stuff[2];
    int f1;// 2 bytes of memory
  }
  u;
  u.f1 = theVal;// copy into the union
  for (int j=0; j < 2; j++) {// now we have to write out 2 bytes of memory
    EEPROM.write(where + j, u.stuff[j]);// write it to EEPROM
  }
}
//
long epReadINT(int where) {
  union uData
  {
    byte stuff[2];
    int f1;// 2 bytes of memory
  }
  u;
  for (int j=0; j < 2; j++) {
    u.stuff[j]=EEPROM.read(where + j);// read back the 2 bytes at this memory location
  }
  return u.f1;
}
//
void epWriteLong(int where, long theVal) {
  union uData
  {
    byte stuff[4];
    long f1;// 4 bytes of memory
  }
  u;
  u.f1 = theVal;// copy into the union
  for (int j=0; j < 4; j++) {// now we have to write out 4 bytes of memory
    EEPROM.write(where + j, u.stuff[j]);// write it to EEPROM
  }
}
//
long epReadLong(int where) {
  union uData
  {
    byte stuff[4];
    long f1;// 4 bytes of memory
  }
  u;
  for (int j=0; j < 4; j++) {
    u.stuff[j]=EEPROM.read(where + j);// read back the 4 bytes to this memory location
  }
  return u.f1;
}
```

- 我们可以看到中心频率：

![](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/img/Grove-I2C_FM_Receiver_com.jpg)

- 我们可以通过 Grove - Button 更改频道，并通过 Grove - Rotary 调整音量。享受您自己的 FM 接收器。

资源下载
---------
-   **[Eagle 文件]**[Grove - I2C FM Receiver v1.1 原理图和 PCB，Eagle 格式](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/res/Grove_I2C_FM_Receiver_v1.1_Eagle.zip)
-   **[PDF 文件]**[Grove - I2C FM Receiver v1.1 PCB，PDF 格式](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/res/Grove%20I2C%20FM%20Receiver%20v1.1%20PCB.pdf)
-   **[PDF 文件]**[Grove - I2C FM Receiver v1.1 原理图，PDF 格式](https://github.com/SeeedDocument/Grove-I2C_FM_Receiver/raw/master/res/Grove%20I2C%20FM%20Receiver%20v1.1%20Sch.pdf)
-   **[Eagle 文件]**[Grove - I2C FM Receiver v1.0 Eagle 文件](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/res/Grove_I2C_FM_Receiver_v1.0.zip)
-   **[数据手册]**[RDA5807M 数据手册](https://raw.githubusercontent.com/SeeedDocument/Grove-I2C_FM_Receiver/master/res/RDA5807M_datasheet_v1.1.pdf)
