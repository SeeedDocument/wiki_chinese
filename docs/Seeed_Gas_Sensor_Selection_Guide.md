![](https://github.com/SeeedDocument/Seeed_Gas_Sensor_Selection_Guide/raw/master/img/Seeed_Gas_Sensor_Selection_Guide.jpg)

气体传感器能够探测存在于环境中的各种气体
## Operating Principle


可以通过检测的气体和传感器表面发生各种反应来检测气体，主要的反应包括电阻、电容、质量、光学特性的改变等。

| 气体传感器类型       | 工作原理|
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 半导体式|利用一些金属氧化物半导体材料,在一定温度下,电导率随着环境气体成份的变化而变化|
| 催化燃烧式|白金电阻的表面制备耐高温的催化剂层,在一定的温度下,可燃性气体在其表面催化燃烧，燃烧时白金电阻的表面温度升高，重而使电阻发生改变|
| 热导池式| 每一种气体，都有自己特定的热导率，当两个和多个气体的热导率差别较大时，可以利用热导元件，分辨其中一个组分的含量|
| 电化学式 | 相当一部分的可燃性的、有毒有害气体都有电化学活性，可以被电化学氧化或者还原 |
| 红外线 |大部分的气体在中红外区都有特征吸收峰,检测特征吸收峰位置的吸收情况,就可以确定某气体的浓度|
| 磁性氧气式 | 利用空气中的氧气可以被强磁场吸引 |

<div align="center"><b>Table 1.</b><i>气体传感器的分类表 </i></div>




## 应用领域

气体传感器有很多的用途。实际上，利用这些传感器可以预防一些潜在的危险。所以在很多情况下，气体传感器在工业、医疗、以及室内有毒和可燃气体的检测中扮演着重要的角色。下面的表格来自So[^1]。

| 应用领域|功能|被检测的气体|
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|环境|监测由于工业排放产生的有毒气体| CO, CH4, 湿度, CO2, O3, VOCs, SOx|
|工作空间|控制室内的空气质量；监测工作环境中的有毒气体| 有毒气体, 易燃气体, O2|
|室内安全| 监测由于火灾和爆炸产生的有毒气体或烟雾; 智能冰箱或烤箱; 火警; 天然气加热; 泄漏检测; 空气质量控制; 空气净化器; 烹饪控制  | CO, 湿度, CO2, VOCs |
|汽车| 汽车通风控制; 汽油蒸气检测; 酒精呼气测试| CO, LPG, VOCs, CH4 |
|公共安全|控制室内空气质量，检测危害公众安全的物质| 有毒气体, 易燃气体, 炸药, O2 |
| 医疗设备| 诊断（呼吸分析，疾病检测）; 护理点患者监测; 药物监测; 人造器官和假肢; 新药发现| O2, NH, NOx, CO2, H2S, H2, CL2, 麻醉气体|
| 农业| 植物/动物诊断; 水土流失试验; 肉类/家禽检查; 废物/污水监测 | amines, 湿度, CO|
|食品安全| 检测特定分子，这些分子是在食物开始腐烂时形成的，不再适合食用| 湿度, CO2|
| 发电厂| 控制发动机和燃气锅炉中的气体浓度，以保证燃烧过程的最高效率。 同样的概念也可以应用于发电厂，因为能量是通过燃烧产生的| O2, CO, HCs, NOx, SOx, CO2, H2, HCs|
| 工业| 常规污染物| O2, H2, O3, CO2, CL2, CH4,H2S |
| 国防军工| 检测化学，生物和毒素战剂; 条约核查| 代理商，爆炸物，推进剂|
| 航天| 监测环境大气中的氧气和有毒和易燃气体| H2, O2, CO3, 湿度|
| 交通/隧道/停车场| 城市交通管理; 隧道或地下停车库的空气质量监测|                  |


<div align="center"><b>Table 2.</b><i>气体应用的一些例子</i></div>

[^2]: Source: 数据来自Taylor (1996), Stcttcr et al. (2003), Capone ct al. (2003), etc. HCs hydrocarbons, VOCs volatile organic compounds.


## Seeed气体传感器分类

如下表所示：

| 名字 | 检测气体 | 气体传感器原理| 应用场景| 传感器|检测范围 | 精度 |工作电压 | 接口 |
|------|---------|--------------|--------|------|---------|-----|--------|------|
| Grove - Air Quality Sensor v1.3 | alcohol, smoke | 电化学| 智能农业| MP503  | 10-1000ppm(smoke)| NA | 3.3V 5V  | Analog |
| Grove - alcohol Sensor| alcohol| 电化学  | 汽车内环境检测，室内环境检测| MQ303A | 20-1000ppm alcohol | NA | 5V | Analog |
| Grove - CO2 Sensor | CO2| 电化学| 智能农业| MH-Z16 | 0-5000ppm| ±(50ppm +5%)| 5V| UART|
| Grove - CO2 & Temperature & Humidity Sensor (SCD30)| CO2| 光学| 智能农业| SCD30 |0-40000ppm| ±(30 ppm + 3%)| 3.3V 5V| I2C|
| Grove - VOC and eCO2 Gas Sensor (SGP30)| VOC,CO2| 电气学| 智能农业| SGP30      | VOC: 0 ppb to 60000ppb  CO2: 400 ppm to 60000 ppm | VOC: (0-2008ppb/1ppb, 2008-11110ppb/6ppb, 11110-60000ppb/32ppb)  CO2: (400-1479ppm/1ppm, 1479-5144ppm/3ppm, 5144-17597ppm/9ppm, 17597-60000ppm/31ppm) | 3.3V 5V| I2C|
| Grove - Gas Sensor(MQ2)| LPG, i-butane, propane, methane, alcohol, Hydrogen, smoke | 电化学| 室内安全| MQ2| LPG and propane: 200ppm-5000ppm  Butane: 300ppm-5000ppm  Methane: 5000ppm-20000ppm  H2: 300ppm-5000ppm  alcohol:100ppm-2000ppm     | NA| 5V| Analog |
| Grove - Gas Sensor(MQ3)| High sensitivity to alcohol and small sensitivity to Benzine | 电化学| 汽车内环境检测,室内环境检测| MQ3| alcohol: 0.05-10mg/L| NA| 5V | Analog|
| Grove - Gas Sensor(MQ5)| High sensitivity to LPG, natural gas, town gas and Small sensitivity to alcohol, smoke| 电化学 | 工业级检测，汽车内环境检测| MQ5| 200-10000ppm| NA| 5V| Analog|
| Grove - Gas Sensor(MQ9)| High sensitivity to carbon monoxide and CH4，LPG| 电化学| 汽车内环境检测，工业级检测 | MQ9        | Carbon monoxide: 20-2000ppm    CH4: 500-10000ppm  LPG: 500-10000ppm | NA | 5V| Analog|
| Grove - Gas Sensor(O2)| O2| 电化学| 汽车内环境检测，工业级检测 | ME2-O2-Ф20 | 0～25%Vol | NA | 3.3V 5V | Analog |
| Grove - HCHO Sensor| Toluene, methanal, benzene, alcohol, acetone | 电化学 | 环境检测 | WSP2110| 1～50ppm| NA  | 3.3V 5V | Analog|
| Grove - Multichannel Gas Sensor| Carbon monoxide,Nitrogen dioxide, Ethanol, Hydrogen, Ammonia, Methane, Propane, Iso-butane   | 电气学| 环境检测 | MiCS-6814  | CO: 1–1000ppm   NO2: 0.05–10ppm   H2: 10–500ppm   C2H5OH: 1-1000ppm  NH3: 1-500ppm  CH4: >1000ppm  C3H8: >1000ppm  C4H10: >1000ppm | NA| 3.3V 5V | I2C|
| Grove - Temperature, Humidity, Pressure and Gas Sensor (BME680) | IAQ| 电气学| 室内环境检测| BME680 | 0-500| NA | 3.3V 5V | I2C|

<div align="center"><b>Table 3.</b><i>Seeed气体传感器分类表</i></div>


## 技术支持
如果您有任何技术问题，请随时联系[techsupport@seeed.cc](techsupport@seeed.cc)。 或者将问题提交到我们的[论坛](http://forum.seeedstudio.com/)

