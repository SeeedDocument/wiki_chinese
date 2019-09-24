
# ADALM-PLUTO 发送

## 发送器结构

AD9363传输链基于[直接转换](https://en.wikipedia.org/wiki/Direct-conversion_receiver)技术。虽然此框图属于 [AD9361](http://www.analog.com/AD9361)，但它也适用于在 ADDALM-PLUTO 中的 [AD9363](http://www.analog.com/AD9363)。两者的区别在于可调范围及次要功能缺失（DCXO、无外部LO、RF 通道带宽变窄）。   


<div width="100%" style="overflow-x: auto;"> 
<svg xmlns:v="http://schemas.microsoft.com/visio/2003/SVGExtensions/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="100%" height="100%" id="svg2" viewBox="0 0 1129 782" preserveAspectRatio="xMidYMid slice">
  <defs
     id="defs4">
    <linearGradient
       id="linearGradient4472">
      <stop
         id="stop4474"
         style="stop-color:#000000;stop-opacity:1"
         offset="0" />
    </linearGradient>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow2Lstart"
       style="overflow:visible">
      <path
         d="M 8.7185878,4.0337352 -2.2072895,0.01601326 8.7185884,-4.0017078 c -1.7454984,2.3720609 -1.7354408,5.6174519 -6e-7,8.035443 z"
         transform="matrix(1.1,0,0,1.1,1.1,0)"
         id="path4489"
         style="fill-rule:evenodd;stroke-width:1;stroke-linejoin:round" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow2Lend"
       style="overflow:visible">
      <path
         d="M 8.7185878,4.0337352 -2.2072895,0.01601326 8.7185884,-4.0017078 c -1.7454984,2.3720609 -1.7354408,5.6174519 -6e-7,8.035443 z"
         transform="matrix(-1.1,0,0,-1.1,-1.1,0)"
         id="path4492"
         style="fill-rule:evenodd;stroke-width:1;stroke-linejoin:round" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mstart"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(0.4,0,0,0.4,4,0)"
         id="path4427"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Lend"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.8,0,0,-0.8,-10,0)"
         id="path5610"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Lstart"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(0.8,0,0,0.8,10,0)"
         id="path4421"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <linearGradient
       id="linearGradient6068">
      <stop
         id="stop6070"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="0" />
      <stop
         id="stop6072"
         style="stop-color:#ffffff;stop-opacity:0"
         offset="1" />
    </linearGradient>
    <linearGradient
       id="linearGradient6018">
      <stop
         id="stop6020"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="0" />
      <stop
         id="stop6022"
         style="stop-color:#ffffff;stop-opacity:0"
         offset="1" />
    </linearGradient>
    <linearGradient
       id="linearGradient4486">
      <stop
         id="stop4488"
         style="stop-color:#000000;stop-opacity:1"
         offset="0" />
      <stop
         id="stop4490"
         style="stop-color:#000000;stop-opacity:0"
         offset="1" />
    </linearGradient>
    <clipPath
       id="clipPath4422">
      <path
         d="m 251.97824,282.86127 178.90065,0 c 14.55023,0 26.26396,11.71373 26.26396,26.26396 l 0,121.75779 c 0,14.55024 -11.71373,26.26397 -26.26396,26.26397 l -178.90065,0 c -14.55023,0 -26.26396,-11.71373 -26.26396,-26.26397 l 0,-121.75779 c 0,-14.55023 11.71373,-26.26396 26.26396,-26.26396 z"
         id="path4424"
         style="fill:#4e9a06;fill-opacity:1;stroke:#2e3436;stroke-width:7;stroke-linejoin:round;stroke-miterlimit:4;stroke-dashoffset:0" />
    </clipPath>
    <clipPath
       id="clipPath4428">
      <rect
         width="231.42857"
         height="174.28572"
         ry="26.263966"
         x="225.71428"
         y="282.86127"
         id="rect4430"
         style="fill:#4e9a06;fill-opacity:1;stroke:#2e3436;stroke-width:7;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0" />
    </clipPath>
    <linearGradient
       x1="186.5"
       y1="-92.495667"
       x2="370.5"
       y2="-92.495667"
       id="linearGradient4510"
       xlink:href="#linearGradient4486"
       gradientUnits="userSpaceOnUse" />
    <radialGradient
       cx="278.5"
       cy="-92.495667"
       r="111.17406"
       fx="278.5"
       fy="-92.495667"
       id="radialGradient6024"
       xlink:href="#linearGradient6018"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.97313035,0,-2.4853262)"
       spreadMethod="repeat" />
    <radialGradient
       cx="466"
       cy="386.99097"
       r="116.51675"
       fx="466"
       fy="386.99097"
       id="radialGradient6074"
       xlink:href="#linearGradient6068"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.77453986,0,87.25104)" />
    <radialGradient
       cx="466"
       cy="386.99097"
       r="116.51675"
       fx="466"
       fy="386.99097"
       id="radialGradient6105"
       xlink:href="#linearGradient6068"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.77453986,0,87.25104)" />
    <radialGradient
       cx="466"
       cy="386.99097"
       r="116.51675"
       fx="466"
       fy="386.99097"
       id="radialGradient6107"
       xlink:href="#linearGradient6068"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.77453986,0,87.25104)" />
    <radialGradient
       cx="466"
       cy="386.99097"
       r="116.51675"
       fx="466"
       fy="386.99097"
       id="radialGradient6110"
       xlink:href="#linearGradient6068"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.77453986,-1.7111816e-5,101.86116)" />
    <radialGradient
       cx="466"
       cy="386.99097"
       r="116.51675"
       fx="466"
       fy="386.99097"
       id="radialGradient6126"
       xlink:href="#linearGradient6068"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(1,0,0,0.77453986,-1.7111816e-5,101.86116)" />
    <v:userDefs>
      <v:ud
         v:nameU="visVersion"
         v:prompt=""
         v:val="VT0(14):26" />
      <v:ud
         v:nameU="msvStructureType"
         v:prompt=""
         v:val="VT4(Callout)" />
      <v:ud
         v:nameU="msvSDTargetIntersection"
         v:prompt=""
         v:val="VT6(PNT(-0.92259821217652,-3.4255522747157)):40" />
      <v:ud
         v:nameU="msvSDCalloutNoHighlight"
         v:prompt=""
         v:val="VT0(0):5" />
      <v:ud
         v:nameU="msvSDCalloutStyle"
         v:prompt=""
         v:val="VT0(11):26" />
      <v:ud
         v:nameU="msvSDCalloutStyleCount"
         v:prompt=""
         v:val="VT0(20):26" />
      <v:ud
         v:nameU="msvShapeCategories"
         v:prompt=""
         v:val="VT0(0):26" />
      <v:ud
         v:nameU="Orientation"
         v:prompt=""
         v:val="VT0(0):26" />
      <v:ud
         v:nameU="HideLeader"
         v:prompt=""
         v:val="VT0(1):5" />
      <v:ud
         v:nameU="AttachToSide"
         v:prompt=""
         v:val="VT0(1):5" />
      <v:ud
         v:nameU="ResizeWithText"
         v:prompt=""
         v:val="VT0(1):5" />
      <v:ud
         v:nameU="Side"
         v:prompt=""
         v:val="VT0(4):26" />
      <v:ud
         v:nameU="LeaderBegin"
         v:prompt=""
         v:val="VT4(Unused)" />
      <v:ud
         v:nameU="LeaderEnd"
         v:prompt=""
         v:val="VT6(PNT(-0.92259821217652,-3.4255522747157)):40" />
      <v:ud
         v:nameU="WHBoxIntersection"
         v:prompt=""
         v:val="VT6(PNT(0.93503937007874,0)):40" />
      <v:ud
         v:nameU="IsEndInterior"
         v:prompt=""
         v:val="VT0(0):5" />
      <v:ud
         v:nameU="Extension"
         v:prompt=""
         v:val="VT0(0.0625):0" />
      <v:ud
         v:nameU="Inset"
         v:prompt=""
         v:val="VT0(0.046875):0" />
      <v:ud
         v:nameU="SideMidpoint"
         v:prompt=""
         v:val="VT6(PNT(0.93503937007874,0)):40" />
      <v:ud
         v:nameU="fnMidpointOffset"
         v:prompt=""
         v:val="VT6(PNT(0.93503937007874,0)):40" />
      <v:ud
         v:nameU="msvThemeColors"
         v:val="VT0(36):26" />
      <v:ud
         v:nameU="msvThemeEffects"
         v:val="VT0(16):26" />
    </v:userDefs>
    <marker
       markerUnits="strokeWidth"
       refX="-24.6"
       orient="auto"
       id="mrkr13-239"
       style="overflow:visible">
      <use
         transform="scale(-8.2,-8.2)"
         id="use128"
         x="0"
         y="0"
         width="3"
         height="3"
         xlink:href="#lend13" />
    </marker>
    <marker
       markerUnits="strokeWidth"
       refX="-24.6"
       orient="auto"
       id="mrkr13-245"
       style="overflow:visible">
      <use
         transform="scale(-8.2,-8.2)"
         id="use131"
         x="0"
         y="0"
         width="3"
         height="3"
         xlink:href="#lend13" />
    </marker>
    <v:userDefs>
      <v:ud
         v:nameU="msvThemeColors"
         v:val="VT0(36):26" />
      <v:ud
         v:nameU="msvThemeEffects"
         v:val="VT0(16):26" />
    </v:userDefs>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-7"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-8"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-9"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-7"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-0"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-78"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-6"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-6"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-6-0"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-6-4"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-6-8"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-6-5"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-6-9"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-6-3"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-6-6"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-6-9"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-8"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-85"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5920"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5922"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5924"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5926"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5928"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5930"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient6661"
       xlink:href="#grad30-12"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12">
      <stop
         id="stop13"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient6661-3"
       xlink:href="#grad30-12-3"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3">
      <stop
         id="stop13-4"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient13296"
       xlink:href="#grad30-12-3"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-0"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-3"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-7"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-30"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-4"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-7"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient13296-2"
       xlink:href="#grad30-12-3-9"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-9">
      <stop
         id="stop13-4-9"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-4"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient13296-3"
       xlink:href="#grad30-12-3-2"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-2">
      <stop
         id="stop13-4-1"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-43"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3579"
       xlink:href="#grad30-12-3-2"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3579-1"
       xlink:href="#grad30-12-3-2-5"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-2-5">
      <stop
         id="stop13-4-1-9"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-43-0"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3638"
       xlink:href="#grad30-12-3-2-5"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-5"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-82"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-1"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-9"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mstart-6"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(0.4,0,0,0.4,4,0)"
         id="path4427-3"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-3"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-2"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-5"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-6"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-9"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-1"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-6"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-0"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-42"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-8"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-60"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-5"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-3"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-9"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-1"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-14"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-54"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-99"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-08"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-65"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-55"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-55"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-36"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-78"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-64"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-783"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-4"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-5"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3649"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3651"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3653"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3655"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3657"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3659"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3661"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3663"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-69"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-95"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3925"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3927"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3929"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3931"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3933"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3935"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker3937"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path3939"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-10"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-0"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5526"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5528"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5530"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5532"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5534"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5536"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker5538"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5540"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3579-6"
       xlink:href="#grad30-12-3-2-3"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-2-3">
      <stop
         id="stop13-4-1-1"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-43-8"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient5812"
       xlink:href="#grad30-12-3-2-3"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-2"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-3"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6025"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6027"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6029"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6031"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6033"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6035"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-695"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-01"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6418"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6420"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-04-17"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-60-80"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6424"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6426"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-17"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-1"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6669"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6671"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="marker6673"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path6675"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3579-5"
       xlink:href="#grad30-12-3-2-1"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-2-1">
      <stop
         id="stop13-4-1-4"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-43-5"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3805"
       xlink:href="#grad30-12-3-2-1"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient6661-4"
       xlink:href="#grad30-12-8"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-8">
      <stop
         id="stop13-9"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-4"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient5179"
       xlink:href="#grad30-12-8"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient5179-4"
       xlink:href="#grad30-12-8-0"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-8-0">
      <stop
         id="stop13-9-4"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-4-5"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-0.17557821"
       y1="599.45868"
       x2="-0.17557821"
       y2="586.46588"
       id="linearGradient3814"
       xlink:href="#grad30-12-8-0"
       gradientUnits="userSpaceOnUse"
       gradientTransform="scale(0.7119335,1.4046256)" />
    <linearGradient
       x1="0"
       y1="1"
       x2="0"
       y2="0"
       id="grad30-12-3-2-1-6">
      <stop
         id="stop13-4-1-4-2"
         style="stop-color:#f0f0f0;stop-opacity:1"
         offset="0" />
      <stop
         id="stop15-0-43-5-9"
         style="stop-color:#ffffff;stop-opacity:1"
         offset="1" />
    </linearGradient>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-45"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-77"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-82"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-54"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-35"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-4"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-25"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-68"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-16"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-73"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-51"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-64"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-41"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-21"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-44"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-05"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-174"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-62"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-22"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-14"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend-30"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path4430-29"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend9"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path5449"
         style="fill:#404040;fill-rule:evenodd;stroke:#404040;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend9c"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path7196"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend0"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path7199"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Menda"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8954"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mendd"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8957"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendC"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8960"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mendv"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8963"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendZ"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8966"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend0w"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8969"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mendu"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8972"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Menduy"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8975"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mendz"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8978"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend9cR"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8981"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendW"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8984"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendO"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8987"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mend1"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path8990"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendR"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path14405"
         style="fill:#af00af;fill-rule:evenodd;stroke:#af00af;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendaB"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path16216"
         style="fill:#af00af;fill-rule:evenodd;stroke:#af00af;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Mendp"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path16219"
         style="fill:#af00af;fill-rule:evenodd;stroke:#af00af;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendH"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path16222"
         style="fill:#00c800;fill-rule:evenodd;stroke:#00c800;stroke-width:1pt" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1MendHS"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.4,0,0,-0.4,-4,0)"
         id="path16225"
         style="fill:#af00af;fill-rule:evenodd;stroke:#af00af;stroke-width:1pt" />
    </marker>
  </defs>
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     transform="translate(-335.89352,247.83673)"
     id="layer1">
    <rect
       width="939.2597"
       height="759.99915"
       ry="16.735245"
       x="424.41556"
       y="-236.83629"
       id="rect3195"
       style="fill:#e6e6e6;fill-opacity:1;stroke:#000000;stroke-width:2.00088286;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 549.99996,173.37499 c 0,-37 0,-37 0,-37"
       id="path5884-8"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,-121.62501 c 82.00002,0.40582 82.00002,0.40582 82.00002,0.40582"
       id="path3794-9-8-1-4-2-0-2-3"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,409.37499 c 140,0.29286 140,0.29286 140,0.29286"
       id="path3794-9-8-1-4-2-0-2-6-6"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="655"
       height="207.99998"
       x="525"
       y="285.375"
       id="rect4346-4-8"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.34430432;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1160,363.37499 c 64,0 64,0 64,0"
       id="path3999-9-3-8-0-6-96-9-4-7-9-7"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1160,483.37499 c 64,0 64,0 64,0"
       id="path3999-9-3-8-0-6-96-9-4-7-9-7-4"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,358.37499 c 150,0.40582 150,0.40582 150,0.40582"
       id="path3794-9-8-1-4-2-0-2-0-2-7"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="655"
       height="209.99998"
       x="504.99997"
       y="303.375"
       id="rect4346-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.35907197;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="730"
       height="280"
       x="514"
       y="-224.62502"
       id="rect4346-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.30414653;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,-23.625011 c 82.00002,0.40582 82.00002,0.40582 82.00002,0.40582"
       id="path3794-9-8-1-4-2-0-2-1-3"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,-72.625011 c 82.00002,0.40582 82.00002,0.40582 82.00002,0.40582"
       id="path3794-9-8-1-4-2-0-2-0-1"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,24.374991 c 206,0.40582 206,0.40582 206,0.40582"
       id="path3794-9-8-1-4-2-0-2-1-4-4"
       style="fill:none;stroke:#ff0000;stroke-width:2.00487208;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 788.94547,-147.52608 c 0,31.90107 0.15134,38.97909 0.15134,38.97909"
       id="path4355-0-2-7-1"
       style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-end:url(#Arrow1Mend-04)" />
    <path
       d="m 1155.8065,35.374992 c 0,-168.495822 -0.036,-177.170762 -0.036,-177.170762"
       id="path4355-0-2-7-49-8-6-7"
       style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-end:url(#Arrow1Mend-04)" />
    <path
       d="m 492.99996,-204.62501 0,280.000002 731.00004,0 0,-280.000002 -731.00004,0 z"
       id="rect4346"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 609.99996,-146.62501 0.35383,80"
       id="path1398-4-1-7"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend9cR)" />
    <path
       d="m 563.99996,-28.822085 c 80.30728,0 80.30728,0 80.30728,0"
       id="path3999-9-3-8-0-5"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,-102.03083 c 82.00002,0.40582 82.00002,0.40582 82.00002,0.40582"
       id="path3794-9-8-1-4-2-0-2"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="translate(76,-121.59418)"
       id="g15806-8">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="44.374992"
         id="rect15599-3-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,44.37499 c 10,10 10,10 10,10"
         id="path15601-7-6"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,44.37499 c -10,10 -10,10 -10,10"
         id="path15603-4-8"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="matrix(-1,0,0,1,1193.9999,-175)"
       id="g3841-3-2">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-2-6"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-4-6"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <g
       transform="translate(76,-121.59418)"
       id="g15801-9">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="-5.6250076"
         id="rect15599-1-8"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,-5.62501 c 10,10 10,10 10,10"
         id="path15601-8-6"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,-5.62501 c -10,10 -10,10 -10,10"
         id="path15603-6-5"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <path
       d="m 544.99998,-101.62501 c 13.99998,0 13.99998,0 13.99998,0"
       id="path3999"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="10"
       height="10"
       x="418.99997"
       y="-25.219181"
       id="rect15599-96-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,-4.030831 c 82.00002,0.405823 82.00002,0.405823 82.00002,0.405823"
       id="path3794-9-8-1-4-2-0-2-1"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 418.99996,-25.219191 c 10,10 10,10 10,10"
       id="path15601-2-4"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <g
       transform="matrix(-1,0,0,1,1193.9999,-76.999999)"
       id="g3841-3-2-9">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-2-6-8"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-4-6-6"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 428.99996,-29.219191 c -10,10 -10,10 -10,10"
       id="path15603-15-5"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 544.99998,-3.625008 c 14.55926,0 14.55926,0 14.55926,0"
       id="path3999-2"
       style="fill:none;stroke:#0000ff;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <g
       transform="translate(76,-125.59418)"
       id="g15811-8">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="144.375"
         id="rect15599-35-4"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,144.37499 c 10,10 10,10 10,10"
         id="path15601-88-8"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,144.37499 c -10,10 -10,10 -10,10"
         id="path15603-0-6"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <path
       d="m 423.99996,-53.030832 c 82.00002,0.405823 82.00002,0.405823 82.00002,0.405823"
       id="path3794-9-8-1-4-2-0-2-0"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-1,0,0,1,1193.9999,-126)"
       id="g3841-3-2-3">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-2-6-3"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-4-6-5"
         style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 544.99998,-52.625009 c 14.55926,0 14.55926,0 14.55926,0"
       id="path3999-9"
       style="fill:none;stroke:#0000ff;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="508.99997"
       y="-98.625023"
       id="text3191-1-6-8"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="508.99997"
         y="-98.625023"
         id="tspan3193-7-0-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RxA</tspan></text>
    <text
       x="508.99997"
       y="-48.625008"
       id="text3191-1-6-8-5"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="508.99997"
         y="-48.625008"
         id="tspan3193-7-0-2-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RxB</tspan></text>
    <text
       x="508.99997"
       y="1.3750019"
       id="text3191-1-6-8-5-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="508.99997"
         y="1.3750019"
         id="tspan3193-7-0-2-2-1"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RxC</tspan></text>
    <path
       d="m 594.19848,4.677642 28.83853,-58.466977"
       id="path1398-4-1"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend0w)" />
    <g
       transform="matrix(-1,0,0,1,1279.9999,-102)"
       id="g3841-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-0"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-0"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 423.99996,175.37499 c 30,0 30,0 30,0"
       id="path3999-9-3-8-0-6-96-2-5"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,195.37499 c 30,0 30,0 30,0"
       id="path3999-9-3-8-0-6-96-2-5-0"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="745.99994"
       y="181.375"
       id="text3191-1-6-3-4-0"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="745.99994"
         y="181.375"
         id="tspan6501"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Baseband</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="438.8826"
       y="-185.74237"
       id="rect3066-5-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="444.8826"
       y="-162.74237"
       id="text3191-8-1"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="444.8826"
         y="-162.74237"
         id="tspan3193-5-7"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">GPO</tspan></text>
    <text
       x="503.99997"
       y="-190.62498"
       id="text3191-1-6-8-5-1"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="503.99997"
         y="-190.62498"
         id="tspan3193-7-0-2-2-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Rx Channel 1</tspan></text>
    <text
       x="522"
       y="-210.62502"
       id="text3191-1-6-8-5-1-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="522"
         y="-210.62502"
         id="tspan3193-7-0-2-2-5-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Rx Channel 2</tspan></text>
    <path
       d="m 485.59443,464.37499 0,38.00001 -28,0 -18,-18 19,-20.00001 z"
       id="path4566-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="481.99997"
       y="487.375"
       id="text3191-1-6-8-8-4"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="481.99997"
         y="487.375"
         id="tspan3562"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">12-bit</tspan></text>
    <path
       d="m 478.67855,-165.97544 c 93.32141,0 93.32141,0 93.32141,0"
       id="path3999-9-3-5"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 423.99996,-166.62501 c 14.55926,0 14.55926,0 14.55926,0"
       id="path3999-9-3-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 423.67241,303.37499 c 29.32755,0 29.32755,0 29.32755,0"
       id="path3999-9-3-6-3"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 425.26688,484.375 c 14.55926,0 14.55926,0 14.55926,0"
       id="path3999-9-3-6-3-8"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 598.99996,137.37499 c 35,0 35,0 35,0"
       id="path3999-9-3-3"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,429.96917 c 140,0.29286 140,0.29286 140,0.29286"
       id="path3794-9-8-1-4-2-0-2-6"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="10"
       height="10"
       x="418.99997"
       y="352.78082"
       id="rect15599-31-7"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,378.96917 c 150,0.40582 150,0.40582 150,0.40582"
       id="path3794-9-8-1-4-2-0-2-0-2"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 623.99994,417.37498 c 17.00002,0 17.00002,0 17.00002,0"
       id="path3999-9-3-8-0-5-8"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:3.9000001;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="511.99997"
       y="319.375"
       id="text3191-1-6-8-5-1-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="511.99997"
         y="319.375"
         id="tspan3193-7-0-2-2-5-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Tx Channel 1</tspan></text>
    <text
       x="532"
       y="297.375"
       id="text3191-1-6-8-5-1-6-1"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="532"
         y="297.375"
         id="tspan3193-7-0-2-2-5-3-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Tx Channel 2</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304"
       y="294.25763"
       id="rect3066-2-2"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1324.2799"
       y="318.11014"
       id="text3191-1-7"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1324.2799"
         y="318.11014"
         id="tspan3193-7-4"
         style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">SPI</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304.8826"
       y="396.25763"
       id="rect3066-2-2-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1324"
       y="419.375"
       id="text3191-1-7-9"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1324"
         y="419.375"
         id="tspan3193-7-4-8"
         style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Reset</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304.8826"
       y="344.25763"
       id="rect3066-2-2-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1324.4525"
       y="368.11014"
       id="text3191-1-7-2"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1324.4525"
         y="368.11014"
         id="tspan6455"
         style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">CTRL</tspan></text>
    <path
       d="m 914.3795,-76.625009 c 0,243.705679 0,261.999999 0,261.999999"
       id="path3999-9-3-8-0-6-96-9-9-5-3"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 877.99996,184.37499 c 0,250.21691 0,269 0,269"
       id="path3999-9-3-8-0-6-96-9-9-5-3-5"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="38"
       height="38"
       ry="0"
       x="857.99994"
       y="223.375"
       id="rect3066-2-5-5-0-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="862.99994"
       y="246.375"
       id="text3191-1-6-23-0-9"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="862.99994"
         y="246.375"
         id="tspan3193-7-0-4-6-7"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DIV</tspan></text>
    <path
       d="m 423.99996,43.969172 c 206,0.40582 206,0.40582 206,0.40582"
       id="path3794-9-8-1-4-2-0-2-1-4"
       style="fill:none;stroke:#ff0000;stroke-width:2.00487208;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-1,0,0,1,1192.9999,-28.999998)"
       id="g3841-3-2-9-4"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-2-6-8-5"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-4-6-6-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="507.99997"
       y="41.375"
       id="text3191-1-6-8-5-6-0"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="507.99997"
         y="41.375"
         id="tspan3193-7-0-2-2-1-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Tx</tspan><tspan
         x="507.99997"
         y="51.375"
         id="tspan15284"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Mon</tspan></text>
    <path
       d="m 665.46478,-20.625008 c 13.84248,0 13.84248,0 13.84248,0"
       id="path3999-9-3-8-0-5-3"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 627.99996,-8.822088 c 16.30728,0 16.30728,0 16.30728,0"
       id="path3999-9-3-8-0-5-7"
       style="fill:none;stroke:#ff0000;stroke-width:2.17076993;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-2.3611049,0,0,2.8493069,665.99996,-2392.1053)"
       id="shape256-1500-9"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-0">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-6"
         style="fill:url(#linearGradient13296);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 628.99996,-9.62501 c 0,54 0,54 0,54"
       id="path3999-9-3-8-0-5-3-4-2"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1225.2334,-100.96082 c 58.7666,0 58.7666,0 58.7666,0"
       id="path3999-9-3-8-0-6-96-9-4-7-9-2"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:none" />
    <rect
       width="119.99998"
       height="40"
       ry="0"
       x="1023.9999"
       y="193.37498"
       id="rect3066-2-5-5-0-5-7"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1.78825831;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1083.9999"
       y="209.37498"
       id="text3191-1-6-23-0-69"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1083.9999"
         y="209.37498"
         id="tspan3193-7-0-4-6-6"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Calibration and</tspan><tspan
         x="1083.9999"
         y="224.37498"
         id="tspan15529"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Correction</tspan></text>
    <path
       d="m 1344,363.37499 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1344,415.37499 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-7"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1344,313.37499 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-6"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="358.375"
       id="rect15599-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,358.37499 c 10,10 10,10 10,10"
       id="path15601-1"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,358.37499 c -10,10 -10,10 -10,10"
       id="path15603-7"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="308.375"
       id="rect15599-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,308.37499 c 10,10 10,10 10,10"
       id="path15601-3"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,308.37499 c -10,10 -10,10 -10,10"
       id="path15603-72"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="410.375"
       id="rect15599-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,410.37499 c 10,10 10,10 10,10"
       id="path15601-4"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,410.37499 c -10,10 -10,10 -10,10"
       id="path15603-3"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <g
       transform="translate(76,-102)"
       id="g15806">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="44.374992"
         id="rect15599-3"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,44.37499 c 10,10 10,10 10,10"
         id="path15601-7"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,44.37499 c -10,10 -10,10 -10,10"
         id="path15603-4"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(76,-102)"
       id="g15801">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="-5.6250076"
         id="rect15599-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,-5.62501 c 10,10 10,10 10,10"
         id="path15601-8"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,-5.62501 c -10,10 -10,10 -10,10"
         id="path15603-6"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(76,-138)"
       id="g15796">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="-35.625008"
         id="rect15599-6"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,-35.62501 c 10,10 10,10 10,10"
         id="path15601-34"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,-35.62501 c -10,10 -10,10 -10,10"
         id="path15603-1"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <rect
       width="10"
       height="10"
       x="418.99997"
       y="-9.6250057"
       id="rect15599-96"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 418.99996,-9.625008 c 10,10 10,10 10,10"
       id="path15601-2"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 428.99996,-9.625008 c -10,10 -10,10 -10,10"
       id="path15603-15"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <g
       transform="translate(76,-106)"
       id="g15811">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="144.375"
         id="rect15599-35"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,144.37499 c 10,10 10,10 10,10"
         id="path15601-88"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,144.37499 c -10,10 -10,10 -10,10"
         id="path15603-0"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(75.999991,-40.000009)"
       id="g15816">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="209.375"
         id="rect15599-7"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,209.37499 c 10,10 10,10 10,10"
         id="path15601-33"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,209.37499 c -10,10 -10,10 -10,10"
         id="path15603-2"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(75.999991,-37.999994)"
       id="g15821">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="229.37498"
         id="rect15599-30"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99995,229.37498 c 10,10 10,10 10,10"
         id="path15601-24"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99995,229.37498 c -10,10 -10,10 -10,10"
         id="path15603-26"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(77.594473,209)"
       id="g15826">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="269.375"
         id="rect15599-33"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,269.37499 c 10,10 10,10 10,10"
         id="path15601-45"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,269.37499 c -10,10 -10,10 -10,10"
         id="path15603-5"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(76,-26)"
       id="g15831">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="324.375"
         id="rect15599-8"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,324.37499 c 10,10 10,10 10,10"
         id="path15601-29"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,324.37499 c -10,10 -10,10 -10,10"
         id="path15603-35"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <path
       d="m 418.99996,352.78081 c 10,10 10,10 10,10"
       id="path15601-79-5"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="418.99997"
       y="373.375"
       id="rect15599-31"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 428.99996,352.78081 c -10,10 -10,10 -10,10"
       id="path15603-71-0"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 418.99996,373.37499 c 10,10 10,10 10,10"
       id="path15601-79"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="419.99997"
       y="404.78082"
       id="rect15599-2-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 428.99996,373.37499 c -10,10 -10,10 -10,10"
       id="path15603-71"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="419.99997"
       y="425.375"
       id="rect15599-2"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 419.99996,425.37499 c 10,10 10,10 10,10"
       id="path15601-455"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 429.99996,425.37499 c -10,10 -10,10 -10,10"
       id="path15603-73"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304"
       y="-115.74237"
       id="rect3066-2-2-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304.8826"
       y="-175.74237"
       id="rect3066-2-2-0-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304.8826"
       y="-55.742371"
       id="rect3066-2-2-6-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1344,-36.625009 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-68"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1344,-156.62501 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-7-2"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1344,-96.62501 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-6-4"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="-41.625"
       id="rect15599-0-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,-41.625009 c 10,10 10,10 10,10"
       id="path15601-1-7"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,-41.625009 c -10,10 -10,10 -10,10"
       id="path15603-7-1"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="-101.625"
       id="rect15599-5-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,-101.62501 c 10,10.000001 10,10.000001 10,10.000001"
       id="path15601-3-9"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,-101.62501 c -10,10.000001 -10,10.000001 -10,10.000001"
       id="path15603-72-9"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="-161.625"
       id="rect15599-9-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,-161.62501 c 10,10 10,10 10,10"
       id="path15601-4-2"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,-161.62501 c -10,10 -10,10 -10,10"
       id="path15603-3-9"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="603.99994"
       y="155.37498"
       id="text3191-1-6-3-4-2-7-4"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="603.99994"
         y="155.37498"
         id="tspan5013"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">70MHz - 6GHz</tspan></text>
    <path
       d="m 600.99996,235.37499 c 28,0 28,0 28,0"
       id="path3999-9-3-3-8"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="646.99994"
       y="-6.6250057"
       id="text3191-1-6-5-2-4"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="646.99994"
         y="-6.6250057"
         id="tspan3193-7-0-6-6-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Tx</tspan></text>
    <text
       x="646.99994"
       y="-24.625008"
       id="text3191-1-6-5-2-1"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="646.99994"
         y="-24.625008"
         id="tspan3193-7-0-6-6-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Rx</tspan></text>
    <path
       d="m 675.99996,63.37499 c 20,-10 20,-6.551717 20,-6.551717 l -40,0 0,-53.448281"
       id="path4570"
       style="fill:none;stroke:#000000;stroke-width:1.21498585;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 550.99996,235.37499 c 21,0 21,0 21,0"
       id="path3999-9-3-8-0-6-96-9-2-0-9-7"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
       transform="matrix(1.1937524,0,0,0.42082333,-95.54176,137.47195)"
       id="path3969-0-5-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.82177877;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 704.99996,63.37499 c 0,184 0,184 0,184"
       id="path3999-9-3-8-0-5-3-4-2-3"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="57.374981"
       y="-1268"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-70-9-9"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="57.374981"
         y="-1268"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-92"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Ch1 I/Q</tspan></text>
    <text
       x="57.374981"
       y="-1288"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-70-9-9-0"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="57.374981"
         y="-1288"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-92-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Ch2 I/Q</tspan></text>
    <text
       x="283.91553"
       y="-1209.3218"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-70-9-9-4"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="283.91553"
         y="-1209.3218"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-92-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Ch1 I/Q</tspan></text>
    <text
       x="283.91553"
       y="-1229.3218"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-70-9-9-0-1"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="283.91553"
         y="-1229.3218"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-92-4-1"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Ch2 I/Q</tspan></text>
    <path
       d="m 697.99996,-24.625008 c 0,77.999998 0,77.999998 0,77.999998"
       id="path3999-9-3-8-0-5-3-11"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="120.00002"
       height="39.999996"
       ry="0"
       x="1023.9999"
       y="133.37497"
       id="rect3066-2-5-5-0-5-7-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.27062678;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1081.9999"
       y="149.37498"
       id="text3191-1-6-23-0-69-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1081.9999"
         y="149.37498"
         id="tspan15529-1"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Temperature</tspan><tspan
         x="1081.9999"
         y="164.37498"
         id="tspan5125"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Sensor</tspan></text>
    <path
       d="m 643.99996,117.37499 c 40,0 40,0 40,0"
       id="path3999-9-3-56"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-2.3611049,0,0,2.8493069,645.2499,-2255.428)"
       id="shape256-1500-9-4"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-0-5">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-6-8"
         style="fill:url(#linearGradient3579);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 548.99996,137.37499 c 28,0 28,0 28,0"
       id="path3999-9-3-8-0-6-96-9-2-0-1"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
       transform="matrix(1.1937524,0,0,0.42082333,-95.54176,39.471952)"
       id="path3969-0-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.82177877;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 569.69492,138.36695 c 14.30504,-29.99196 14.30504,30.00804 26.6755,-1.9671"
       id="path3999-9-3-8-0-6-5-8-7-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 705.99996,195.54967 c -20.64306,-10.08734 0,-20.17468 0,-20.17468"
       id="path4478"
       style="fill:#e6e6e6;fill-opacity:1;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 478.99996,185.28626 c 823.20404,0 885.00004,0 885.00004,0"
       id="use4633"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
       transform="matrix(1.1937524,0,0,0.42082333,-95.54176,87.471952)"
       id="path3969-0-5-1"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.82177877;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,101.37499 c 200,0 200,0 200,0"
       id="path3999-9-3-3-9"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 423.99996,263.37499 c 203,0 203,0 203,0"
       id="path3999-9-3-3-9-1"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 648.99996,246.37499 c 55,0 55,0 55,0"
       id="path3999-9-3-3-8-0"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-2.3611049,0,0,2.8493069,649.2499,-2123.428)"
       id="shape256-1500-9-4-7"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-0-5-7">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-6-8-3"
         style="fill:url(#linearGradient3638);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="603.99994"
       y="218.37498"
       id="text3191-1-6-3-4-2-7-4-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="603.99994"
         y="218.37498"
         id="tspan5015"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">70MHz - 6GHz</tspan></text>
    <text
       x="625.99994"
       y="123.08749"
       id="text3191-1-6-3-4"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="625.99994"
         y="123.08749"
         id="tspan3193-7-0-5-7"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Rx</tspan></text>
    <text
       x="629.99994"
       y="255.375"
       id="text3191-1-6-3-4-2"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="629.99994"
         y="255.375"
         id="tspan3193-7-0-5-7-6"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Tx</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="821.99994"
       y="165.37498"
       id="rect3066-2-5-5-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="828.99994"
       y="188.37497"
       id="text3191-1-6-23-0"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="828.99994"
         y="188.37497"
         id="tspan3193-7-0-4-6"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;font-family:Sans;-inkscape-font-specification:Sans Bold">DIV</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="935.99994"
       y="165.37498"
       id="rect3066-2-5-5-0-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="942.99994"
       y="188.37497"
       id="text3191-1-6-23-0-6"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="942.99994"
         y="188.37497"
         id="tspan3193-7-0-4-6-79"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DIV</tspan></text>
    <g
       transform="translate(75.99999,-133.99999)"
       id="g15821-4">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="229.37498"
         id="rect15599-30-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99995,229.37498 c 10,10 10,10 10,10"
         id="path15601-24-7"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99995,229.37498 c -10,10 -10,10 -10,10"
         id="path15603-26-6"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <g
       transform="translate(75.99999,28.000012)"
       id="g15821-4-3">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="229.37498"
         id="rect15599-30-2-3"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99995,229.37498 c 10,10 10,10 10,10"
         id="path15601-24-7-4"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99995,229.37498 c -10,10 -10,10 -10,10"
         id="path15603-26-6-8"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <text
       x="1168"
       y="113.37499"
       id="text3191-1-6-3-4-2-7-4-5-2-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1168"
         y="113.37499"
         id="tspan4977"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Rx 61.44 MSPS</tspan></text>
    <rect
       width="120.00002"
       height="39.999996"
       ry="0"
       x="1023.9999"
       y="83.374992"
       id="rect3066-2-5-5-0-5-7-5-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.27062678;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1083.9999"
       y="99.374992"
       id="text3191-1-6-23-0-69-3-8"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1083.9999"
         y="99.374992"
         id="tspan5125-4"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Enable State</tspan><tspan
         x="1083.9999"
         y="114.37499"
         id="tspan3627"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Machine (ENSM)</tspan></text>
    <path
       d="m 828.99992,-144.62501 c 307.00008,0 307.00008,0 307.00008,0 l 0,0 0,0 0,0"
       id="path4683-3"
       style="fill:none;stroke:#000000;stroke-width:1.03787863;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:url(#Arrow1Mstart)" />
    <path
       d="m 419.99996,404.78081 c 10,10 10,10 10,10"
       id="path15601-455-4"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <g
       transform="matrix(-1,0,0,1,983.9999,-5)"
       id="g6319"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 431.99994,405.37499 c -0.0109,-39.93275 0,-40 0,-40 l 38,19"
         id="path3051-2-6-6"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 469.99994,384.37499 c -38,21 -38,21 -38,21"
         id="path3071-4-6-0"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 429.99996,404.78081 c -10,10 -10,10 -10,10"
       id="path15603-73-6"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="528.00476"
       y="382.37497"
       id="text3191-1-6-8-4"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="528.00476"
         y="382.37497"
         id="tspan3193-7-0-2-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TxA</tspan></text>
    <g
       transform="translate(-135.00484,356.99999)"
       id="g3841-3-2-3-1"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-2-6-3-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-4-6-5-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="528"
       y="434.375"
       id="text3191-1-6-8-5-3"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="528"
         y="434.375"
         id="tspan3193-7-0-2-2-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TxB</tspan></text>
    <path
       d="m 601.20274,436.1594 28.75863,-58.31837"
       id="path1398-4-1-2"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <path
       d="m 624.99994,399.37498 c 16.00002,0 16.00002,0 16.00002,0"
       id="path3999-9-3-8-0-5-8-4"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:3.9000001;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 582.99996,407.37499 c 23,0 23,0 23,0"
       id="path3999-9-3-3-8-3"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="translate(-57,335)"
       id="g3841-5-2"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-0-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-0-6"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="1256"
       y="-206.62502"
       id="text3191-1-6-8-5-1-67"
       xml:space="preserve"
       style="font-size:22px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1256"
         y="-206.62502"
         id="tspan3193-7-0-2-2-5-2"
         style="font-size:22px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">AD9361</tspan></text>
    <path
       d="m 538.99996,173.37499 c 12,0 12,0 12,0"
       id="path3999-9-3-8-0-6-96-9-2-0"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="38"
       height="38"
       ry="0"
       x="503.99997"
       y="166.37497"
       id="rect3066-2-5-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="510.99997"
       y="189.375"
       id="text3191-1-6-23"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="510.99997"
         y="189.375"
         id="tspan3193-7-0-4"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DIV</tspan></text>
    <g
       transform="matrix(0.31989691,0,0,0.31989691,1196.1574,418.49848)"
       id="g3">
      <path
         d="M 118.296,264.038 V 159.531 H 222.245 V 264.038 H 118.296 z m 21.392,-88.241 v 74.981 l 65.177,-38.326 -65.177,-36.655 z m 117.541,87.126 h -17.938 v -46.572 h 18.049 c 13.37,0 21.392,10.584 21.392,24.065 0,13.482 -7.13,22.507 -21.503,22.507 z m 15.933,-57.156 -3.565,-10.361 h -17.158 l -3.119,10.361 h -9.359 l 15.709,-46.682 h 9.47 l 17.603,46.682 h -9.581 z m -16.712,18.495 h -7.353 v 31.419 h 7.911 c 10.472,0 12.032,-8.913 11.921,-15.709 -10e-4,-5.348 -2.564,-15.71 -12.479,-15.71 z m 9.915,-38.215 -5.904,-17.157 -5.236,17.045 -0.334,2.897 h 11.586 c 0,-1.559 0.112,-1.894 -0.112,-2.785 z m 15.71,76.876 v -46.572 h 34.315 v 7.8 h -24.956 v 9.916 h 22.06 v 8.467 h -21.949 v 12.479 h 25.626 v 7.911 h -35.096 z m 32.31,-57.156 -20.5,-31.53 v 31.53 h -9.358 v -46.682 h 9.581 l 19.721,31.084 v -31.084 h 9.359 v 46.682 h -8.803 z m 29.303,57.044 h -8.914 l -15.375,-44.008 v -2.451 h 9.359 l 10.473,34.094 10.25,-33.981 h 9.136 v 2.45 l -14.929,43.896 z m 14.817,-57.044 -3.565,-10.361 h -17.158 l -3.118,10.361 h -9.359 l 15.709,-46.682 h 9.471 l 17.604,46.682 h -9.584 z m -6.685,-19.497 -5.904,-17.603 -5.905,17.603 v 2.563 h 11.81 0.223 c -10e-4,-1.56 -10e-4,-1.783 -0.224,-2.563 z m 9.693,76.541 v -46.347 h 9.916 v 46.347 h -9.916 z m 8.58,-57.044 v -46.682 h 9.247 v 38.772 h 20.834 v 7.91 h -30.081 z m 25.959,58.271 c -25.514,0.556 -29.97,-48.688 0.111,-48.355 16.713,0 19.609,13.928 20.278,16.044 h -9.248 c -1.449,-2.896 -5.236,-8.467 -9.916,-8.802 -16.489,-1.114 -16.489,33.76 0,33.76 7.911,0 9.805,-7.911 10.25,-8.802 h 9.024 c 0.001,0.111 -1.113,15.931 -20.499,16.155 z m 25.625,-57.49 c -29.97,0 -28.855,-48.354 0.335,-48.131 28.187,0.222 28.967,48.131 -0.335,48.131 z m -0.334,-7.8 c 17.269,0.111 17.269,-32.198 0.334,-32.421 -16.823,-0.112 -17.381,32.31 -0.334,32.421 z m -3.12,64.175 v -46.572 h 33.091 v 8.468 h -24.177 v 9.582 h 21.391 v 8.356 h -21.279 v 12.255 h 25.18 v 7.911 h -34.206 z m 62.838,-58.27 v -4.457 c -1.002,0.892 -5.458,6.573 -13.815,6.351 -28.522,-0.668 -28.634,-47.462 1.337,-48.02 7.242,0 13.258,4.568 15.598,7.799 2.785,3.677 3.01,6.796 3.121,7.576 h -7.911 c -1.783,-2.897 -4.567,-7.799 -11.141,-7.799 -17.381,-0.223 -18.495,32.644 -0.113,32.979 8.136,0.223 12.256,-8.244 12.256,-8.356 v -2.451 h -11.141 v -7.242 h 19.163 v 23.619 h -7.354 z m -8.691,59.495 c -19.72,0 -19.497,-15.152 -19.497,-15.152 h 8.914 c 0,0 -0.669,7.354 9.245,8.022 2.453,0.111 10.475,-0.892 10.475,-6.462 0,-6.462 -8.133,-6.128 -13.258,-7.577 -5.126,-1.336 -14.818,-3.565 -14.818,-12.589 0,-7.911 6.461,-14.708 18.939,-14.708 16.712,0.112 16.602,13.036 16.712,13.816 h -8.579 c -0.556,-1.894 -1.113,-6.461 -8.577,-6.685 -3.677,0 -9.248,1.225 -9.248,5.57 0,5.459 6.24,6.239 12.813,7.242 9.915,1.894 15.598,4.902 15.262,14.038 -0.222,8.023 -7.354,14.485 -18.383,14.485 z"
         id="path5" />
    </g>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1304.8826"
       y="4.2576313"
       id="rect3066-2-2-0-99"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1324"
       y="27.375002"
       id="text3191-1-7-9-8"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1324"
         y="27.375002"
         id="tspan3193-7-4-8-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:125%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">GND</tspan></text>
    <path
       d="m 1344,23.37499 c 20,0 20,0 20,0"
       id="path3999-9-3-8-0-5-3-2-7-0"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="10"
       height="10"
       x="1359"
       y="18.375002"
       id="rect15599-9-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1359,18.37499 c 10,10.000001 10,10.000001 10,10.000001"
       id="path15601-4-9"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1369,18.37499 c -10,10.000001 -10,10.000001 -10,10.000001"
       id="path15603-3-0"
       style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 423.67241,319.37499 c 23.32755,0 23.32755,0 23.32755,0"
       id="path3999-9-3-6-3-3"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="translate(76,-10)"
       id="g15831-4">
      <rect
         width="10"
         height="10"
         x="342.99997"
         y="324.375"
         id="rect15599-8-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 342.99996,324.37499 c 10,10 10,10 10,10"
         id="path15601-29-1"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 352.99996,324.37499 c -10,10 -10,10 -10,10"
         id="path15603-35-1"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <path
       d="m 483.99996,291.37499 0,38 -28,0 -18,-18 19,-20 z"
       id="path4566"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="481.53635"
       y="308.375"
       id="text3191-1-6-8-8-4-8"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="481.53635"
         y="308.375"
         id="tspan3193-7-0-2-8-7-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">Dual</tspan><tspan
         x="481.53635"
         y="318.375"
         id="tspan4971"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">10-bit</tspan><tspan
         x="481.53635"
         y="328.375"
         id="tspan3579"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:100%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold" /></text>
    <path
       d="m 735.64613,-166.62501 0.35383,60"
       id="path1398-4-1-7-4"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mendu)" />
    <path
       d="m 1127.6461,-166.62501 0.3539,60"
       id="path1398-4-1-7-4-2"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mendv)" />
    <path
       d="m 789.99996,-166.62501 0.35383,60"
       id="path1398-4-1-7-4-8"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendZ)" />
    <path
       d="m 849.64613,-168.62501 0.35383,60"
       id="path1398-4-1-7-4-6"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Menda)" />
    <rect
       width="631.13348"
       height="39.999996"
       ry="0"
       x="572.86646"
       y="-183.625"
       id="rect3066-5-9-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="633.99994"
       y="-170.62502"
       id="text3191-8-1-2"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="633.99994"
         y="-170.62502"
         id="tspan3193-5-7-9"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Automatic</tspan><tspan
         x="633.99994"
         y="-159.82501"
         id="tspan4839"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Gain</tspan><tspan
         x="633.99994"
         y="-149.02501"
         id="tspan4841"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Control</tspan></text>
    <text
       x="993.99994"
       y="-170.62502"
       id="text3191-8-1-2-5"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="993.99994"
         y="-170.62502"
         id="tspan4835"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">□ Manual</tspan><tspan
         x="993.99994"
         y="-161.62502"
         id="tspan4833"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">□ Slow</tspan><tspan
         x="993.99994"
         y="-152.62502"
         id="tspan4837"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:89.99999762%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">□ Fast</tspan></text>
    <path
       d="m 678.99996,-80.412585 c 585.00004,0 585.00004,0 585.00004,0"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="M 775.19899,-53.164865 804.11,-111.63025"
       id="path1398-4-3"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendH)" />
    <g
       transform="matrix(-1,0,0,1,1460.9997,-153.84192)"
       id="g3841-2"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-5"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-6"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 832.14184,-53.410625 28.87138,-58.466445"
       id="path1398-9"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend1)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="828.99976"
       y="-99.466927"
       id="rect3066-2-5-7-5-8"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 844.99986,-76.466925 c 5.34591,-5.34592 5.34591,-5.34592 5.34591,-5.34592"
       id="path3999-9-3-8-0-6-9-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="93.374992"
       y="-919.99994"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-2-53"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="93.374992"
         y="-919.99994"
         id="tspan3193-7-0-5-7-3-2-6-0-5-07"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">25 - 640 MSPS</tspan></text>
    <path
       d="m 1169.0887,-51.001545 28.9111,-58.465385"
       id="path1398-4-0-3-9"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1163.6929"
       y="-99.466927"
       id="rect3066-23-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1172"
       y="-77.625076"
       id="text3191-2-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1172"
         y="-77.625076"
         id="tspan3193-4-0"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">FIR</tspan></text>
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="998.99976"
       y="-99.466927"
       id="rect3066-5-8"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1002.9998"
       y="-77.466873"
       id="text3191-8-7"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1002.9998"
         y="-77.466873"
         id="tspan3193-5-9"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;font-family:Sans;-inkscape-font-specification:Sans Bold">HB2</tspan></text>
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1053.9998"
       y="-99.466927"
       id="rect3066-2-7"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1056.9998"
       y="-77.625076"
       id="text3191-1-0"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1056.9998"
         y="-77.625076"
         id="tspan3193-7-65"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB1</tspan></text>
    <path
       d="m 1109.0888,-52.001535 28.9111,-58.465385"
       id="path1398-4-0-8"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendW)" />
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1108.9725"
       y="-99.466927"
       id="rect3066-85"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1109.9998"
       y="-77.466873"
       id="text3191-29"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1109.9998"
         y="-77.466873"
         id="tspan3193-1"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">GAIN</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="943.99976"
       y="-99.466927"
       id="rect3066-2-5-75"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="946.99976"
       y="-77.466873"
       id="text3191-1-6-55"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="946.99976"
         y="-77.466873"
         id="tspan3193-7-0-07"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB3</tspan></text>
    <text
       x="1209.9728"
       y="-90.570747"
       id="text3191-1-6-3-4-2-7-4-5-70-1-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1209.9728"
         y="-90.570747"
         id="tspan3193-7-0-5-7-3-2-6-0-84-8-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">I</tspan></text>
    <path
       d="m 927.99986,-99.46693 0,38.000005 -28,0 -18,-18 19,-20.000005 z"
       id="path4566-9-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 834.99986,-88.46693 c 13,-14 13,13.000005 26.64281,0"
       id="path3999-9-3-8-0-6-5-5"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 835.99986,-78.466925 c 13,-14.000005 13,13 26.64281,0"
       id="path3999-9-3-8-0-6-5-0-9"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 835.99986,-67.466925 c 13,-14 13,13 26.64281,0"
       id="path3999-9-3-8-0-6-5-8-74"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 844.65395,-86.121 c 5.34591,-5.34593 5.34591,-5.34593 5.34591,-5.34593"
       id="path3999-9-3-8-0-6-9-3-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 736.97266,29.429226 c 0,-105.000001 0,-105.000001 0,-105.000001"
       id="path3999-9-3-8-0-6-96-5-7-0"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 721.96254,-53.429605 28.86667,-58.439325"
       id="path1398-4-9-2"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendO)" />
    <g
       transform="matrix(0.43250065,0,0,0.43250492,331.61459,-151.33255)"
       id="g3993-0"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
         transform="matrix(2.7601169,0,0,0.97299086,-634.46397,-63.11085)"
         id="path3969-10"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 903.66697,130.71785 c 59.94441,59.18055 63.69637,62.93251 63.69637,62.93251"
         id="path3973-5"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 964.4662,130.03877 c -59.1806,59.9444 -62.9325,63.69631 -62.9325,63.69631"
         id="path3973-6-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="893.99976"
       y="-77.466873"
       id="text3191-1-6-8-8-6-4-7"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="893.99976"
         y="-77.466873"
         id="tspan3193-7-0-2-8-3-3-3"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">ADC</tspan></text>
    <path
       d="m 698.99996,-23.625008 c 32,0 32,0 32,0"
       id="path3999-9-3-56-2-2"
       style="fill:none;stroke:#0000ff;stroke-width:2.35907125;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="38"
       height="38"
       ry="0"
       x="715.9726"
       y="-41.570747"
       id="rect3066-2-5-75-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 944.25152,-53.736675 a 6.5491208,9.3105191 0 0 0 6.5393,9.32409 l 117.55158,0 a 6.5491208,9.3105191 0 0 1 6.5392,9.2965 6.5491208,9.3105191 0 0 1 6.5587,-9.2965 l 117.5323,0 a 6.5491208,9.3105191 0 0 0 6.5583,-9.32409"
       id="path3578-9"
       style="fill:none;stroke:#404040;stroke-width:0.99999982;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 819.99996,33.37499 -0.35383,-175"
       id="path1398-4-1-7-4-3"
       style="stroke:#af00af;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendR)" />
    <rect
       width="20"
       height="50"
       x="810.99994"
       y="-46.625011"
       id="rect5968"
       style="fill:#ffffff;fill-opacity:1;stroke:none" />
    <path
       d="m 771.51224,-54.364185 a 2.4641228,9.5028 0 0 0 2.46042,9.51665 l 44.22904,0 a 2.4641228,9.5028 0 0 1 2.46042,9.4885 2.4641228,9.5028 0 0 1 2.46773,-9.4885 l 44.22174,0 a 2.4641228,9.5028 0 0 0 2.46773,-9.51665"
       id="path3578-7-1"
       style="fill:none;stroke:#404040;stroke-width:0.85967529;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <text
       x="826.79138"
       y="-23.306892"
       id="text4366-8-0"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><tspan
         x="826.79138"
         y="-23.306892"
         id="tspan6278-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">RF Channel Bandwidth</tspan></text>
    <text
       x="771.97253"
       y="-12.412544"
       id="text3191-1-6-3-4-2-7-4-5-8"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="771.97253"
         y="-12.412544"
         id="tspan3193-7-0-5-7-3-2-6-0-0"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">200kHz - 56MHz (I/Q)</tspan></text>
    <text
       x="953.99988"
       y="-123.625"
       id="text3191-1-6-3-4-2-7-4-5-1-6"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="953.99988"
         y="-123.625"
         id="tspan3193-7-0-5-7-3-2-6-0-8-7"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷1</tspan><tspan
         x="953.99988"
         y="-114.625"
         id="tspan4715-3"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷2</tspan><tspan
         x="953.99988"
         y="-105.625"
         id="tspan4717-1"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷3</tspan></text>
    <text
       x="1005.9998"
       y="-114.625"
       id="text3191-1-6-3-4-2-7-4-5-1-8-6"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1005.9998"
         y="-114.625"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-8"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷1</tspan><tspan
         x="1005.9998"
         y="-105.625"
         id="tspan4715-5-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷2</tspan><tspan
         x="1005.9998"
         y="-96.625"
         id="tspan4717-2-2"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans" /></text>
    <text
       x="1061.9998"
       y="-114.625"
       id="text3191-1-6-3-4-2-7-4-5-1-8-1-0"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1061.9998"
         y="-114.625"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-5-2"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷1</tspan><tspan
         x="1061.9998"
         y="-105.625"
         id="tspan4715-5-5-3"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷2</tspan><tspan
         x="1061.9998"
         y="-96.625"
         id="tspan4717-2-9-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans" /></text>
    <text
       x="1174"
       y="-122.625"
       id="text3191-1-6-3-4-2-7-4-5-1-8-8-0"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1174"
         y="-122.625"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-4-5"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷1</tspan><tspan
         x="1174"
         y="-113.625"
         id="tspan4715-5-0-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷2</tspan><tspan
         x="1174"
         y="-104.625"
         id="tspan4717-2-8-9"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">÷4</tspan></text>
    <path
       d="m 679.97266,-79.625009 c 0,115.000001 0,115.000001 0,115.000001"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-6"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 698.99996,43.54967 c -20.64306,-10.08734 0,-20.17468 0,-20.17468"
       id="path4478-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 678.99996,34.587416 c 585.00004,0 585.00004,0 585.00004,0"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-5"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="M 775.19899,61.835136 804.11,3.369756"
       id="path1398-4-3-7"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mendz)" />
    <g
       transform="matrix(-1,0,0,1,1460.9997,-38.841875)"
       id="g3841-2-8"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-opacity:1">
      <path
         d="m 686.99996,94.37499 c 0.0109,-39.93275 0,-40 0,-40 l -38,19"
         id="path3051-5-0"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 648.99996,73.37499 c 38,21 38,21 38,21"
         id="path3071-6-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="M 832.14184,61.589376 861.01322,3.122936"
       id="path1398-9-8"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendC)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="828.99976"
       y="15.533133"
       id="rect3066-2-5-7-5-8-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1169.0887,63.998456 28.9111,-58.46538"
       id="path1398-4-0-3-9-4"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1163.6929"
       y="15.533133"
       id="rect3066-23-0-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1172"
       y="37.374985"
       id="text3191-2-3-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1172"
         y="37.374985"
         id="tspan3193-4-0-9"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">FIR</tspan></text>
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="998.99976"
       y="15.533133"
       id="rect3066-5-8-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1002.9998"
       y="37.533188"
       id="text3191-8-7-6"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1002.9998"
         y="37.533188"
         id="tspan3193-5-9-3"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;font-family:Sans;-inkscape-font-specification:Sans Bold">HB2</tspan></text>
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1053.9998"
       y="15.533133"
       id="rect3066-2-7-9"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1056.9998"
       y="37.374985"
       id="text3191-1-0-4"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1056.9998"
         y="37.374985"
         id="tspan3193-7-65-1"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB1</tspan></text>
    <path
       d="m 1109.0888,62.998466 28.9111,-58.46538"
       id="path1398-4-0-8-0"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Menduy)" />
    <rect
       width="38.054348"
       height="38.054352"
       ry="0"
       x="1108.9725"
       y="15.533133"
       id="rect3066-85-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1109.9996"
       y="37.533188"
       id="text3191-29-0"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1109.9996"
         y="37.533188"
         id="tspan3193-1-0"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">GAIN</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="943.99976"
       y="15.533133"
       id="rect3066-2-5-75-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="946.99976"
       y="37.533188"
       id="text3191-1-6-55-6"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="946.99976"
         y="37.533188"
         id="tspan3193-7-0-07-5"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB3</tspan></text>
    <text
       x="1209.9728"
       y="29.429247"
       id="text3191-1-6-3-4-2-7-4-5-70-9-7-6-8"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1209.9728"
         y="29.429247"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-0-9-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Q</tspan></text>
    <path
       d="m 927.99986,15.533076 0,38 -28,0 -18,-18 19,-20 z"
       id="path4566-9-0-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 834.99986,26.533076 c 13,-14 13,13 26.64281,0"
       id="path3999-9-3-8-0-6-5-5-9"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 835.99986,47.533076 c 13,-14 13,13 26.64281,0"
       id="path3999-9-3-8-0-6-5-8-74-8"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 844.65395,28.878996 c 5.34591,-5.34592 5.34591,-5.34592 5.34591,-5.34592"
       id="path3999-9-3-8-0-6-9-3-6-2"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="M 721.96254,61.570396 750.82921,3.131076"
       id="path1398-4-9-2-8"
       style="stroke:#00c800;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mendd)" />
    <g
       transform="matrix(0.43250065,0,0,0.43250492,331.61459,-36.332575)"
       id="g3993-0-5"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
         transform="matrix(2.7601169,0,0,0.97299086,-634.46397,-63.11085)"
         id="path3969-10-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 903.66697,130.71785 c 59.94441,59.18055 63.69637,62.93251 63.69637,62.93251"
         id="path3973-5-4"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 964.4662,130.03877 c -59.1806,59.9444 -62.9325,63.69631 -62.9325,63.69631"
         id="path3973-6-2-3"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="893.99976"
       y="37.533188"
       id="text3191-1-6-8-8-6-4-7-9"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="893.99976"
         y="37.533188"
         id="tspan3193-7-0-2-8-3-3-3-4"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">ADC</tspan></text>
    <path
       d="m 1206.5309,8.883916 a 6.5491208,9.3105191 0 0 0 -6.5393,-9.32409 l -117.5515,0 a 6.5491208,9.3105191 0 0 1 -6.5392,-9.2965 6.5491208,9.3105191 0 0 1 -6.5587,9.2965 l -117.53239,0 a 6.5491208,9.3105191 0 0 0 -6.5583,9.32409"
       id="path3578-9-7"
       style="fill:none;stroke:#404040;stroke-width:0.99999982;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 869.81931,8.640966 a 2.4641228,9.5028 0 0 0 -2.46042,-9.51665 l -44.22904,0 a 2.4641228,9.5028 0 0 1 -2.46042,-9.4885 2.4641228,9.5028 0 0 1 -2.46773,9.4885 l -44.22174,0 a 2.4641228,9.5028 0 0 0 -2.46773,9.51665"
       id="path3578-7-1-1"
       style="fill:none;stroke:#404040;stroke-width:0.85967529;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <text
       x="735.08075"
       y="-23.570747"
       id="text3191-1-6-8-8-6-4-7-98"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="735.08075"
         y="-23.570747"
         id="tspan5791"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Phase</tspan><tspan
         x="735.08075"
         y="-14.570747"
         id="tspan5793"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Splitter</tspan></text>
    <g
       transform="matrix(0,2.3611049,2.8493069,0,-1678.4803,48.37499)"
       id="shape256-1500-9-4-2"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-0-5-4">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-6-8-7"
         style="fill:url(#linearGradient5812);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="678.99994"
       y="63.374985"
       id="text3191-1-6-5"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="678.99994"
         y="63.374985"
         id="tspan3193-7-0-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Rx</tspan></text>
    <text
       x="698.99994"
       y="63.374985"
       id="text3191-1-6-5-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="698.99994"
         y="63.374985"
         id="tspan3193-7-0-6-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Tx</tspan></text>
    <path
       d="m 843.99986,39.533071 c 5.34591,-5.34592 5.34591,-5.34592 5.34591,-5.34592"
       id="path3999-9-3-8-0-6-9-6-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 834.99986,37.533071 c 13,-14 13,13 26.64281,0"
       id="path3999-9-3-8-0-6-5-0-9-0"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1100,33.37499 -0.3539,-176"
       id="path1398-4-1-7-4-3-5"
       style="stroke:#af00af;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mendp)" />
    <rect
       width="70.000084"
       height="25"
       x="1088.9999"
       y="-34.625008"
       id="rect5968-5"
       style="fill:#ffffff;fill-opacity:1;stroke:none" />
    <text
       x="1080.6195"
       y="-25.306953"
       id="text4366-5"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><tspan
         x="1082.3578"
         y="-25.306953"
         id="tspan4368-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Rx Decimation </tspan><tspan
         x="1080.6195"
         y="-14.306953"
         id="tspan4370-9"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Digital Filtering and Equalization</tspan></text>
    <path
       d="m 638.99996,462.85004 c 565.00004,0 565.00004,0 565.00004,0"
       id="path3999-9-3-8-0-6-1-8-0-1"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 795.22245,489.78084 28.75893,-58.43912"
       id="path1398-5-8"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="789.99988"
       y="442.52246"
       id="rect3066-2-5-7-5-9-8"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 796.00002,452.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-3-1"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 797.00002,462.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-0-2-3"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 797.00002,473.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-8-2-5"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 806.00002,464.37499 c 5.3459,-5.34592 5.3459,-5.34592 5.3459,-5.34592"
       id="path3999-9-3-8-0-6-9-5-1"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 805.65402,454.72091 c 5.346,-5.34592 5.346,-5.34592 5.346,-5.34592"
       id="path3999-9-3-8-0-6-9-3-7-5"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 914.72182,435.56585 a 5.5092993,9.3105191 0 0 1 5.501,-9.32409 l 98.88758,0 a 5.5092993,9.3105191 0 0 0 5.501,-9.2965 5.5092993,9.3105191 0 0 0 5.5173,9.2965 l 98.8713,0 a 5.5092993,9.3105191 0 0 1 5.5172,9.32409"
       id="path3578-3-1"
       style="fill:none;stroke:#404040;stroke-width:0.92528909;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 726.36376,434.86349 a 2.6401967,9.5028 0 0 1 2.63622,-9.51665 l 47.38943,0 a 2.6401967,9.5028 0 0 0 2.63622,-9.4885 2.6401967,9.5028 0 0 0 2.64407,9.4885 l 47.3816,0 a 2.6401967,9.5028 0 0 1 2.64406,9.51665"
       id="path3578-7-8-9"
       style="fill:none;stroke:#404040;stroke-width:0.88985944;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 735.19411,489.78084 28.75893,-58.43912"
       id="path1398-5-7-7"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="729.99988"
       y="442.52246"
       id="rect3066-2-5-7-5-9-2-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 736.00001,452.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-3-3-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 737.00001,462.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-0-2-9-5"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 737.00001,473.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-8-2-6-0"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 746.00001,464.37499 c 5.3459,-5.34592 5.3459,-5.34592 5.3459,-5.34592"
       id="path3999-9-3-8-0-6-9-5-3-2"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 745.65401,454.72091 c 5.346,-5.34592 5.346,-5.34592 5.346,-5.34592"
       id="path3999-9-3-8-0-6-9-3-7-2-3"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="789.99988"
       y="401.375"
       id="text4366-8-9-0"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><tspan
         x="789.99988"
         y="401.375"
         id="tspan6278-6-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">RF Channel Bandwidth</tspan></text>
    <text
       x="1024.2617"
       y="399.375"
       id="text4366-6-5"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><tspan
         x="1026"
         y="399.375"
         id="tspan4368-4-1"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Tx Interpolation </tspan><tspan
         x="1024.2617"
         y="410.375"
         id="tspan4370-0-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">Digital Filtering and Equalization</tspan></text>
    <text
       x="728.99994"
       y="412.375"
       id="text3191-1-6-3-4-2-7-4-5-7-3"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="728.99994"
         y="412.375"
         id="tspan3193-7-0-5-7-3-2-6-0-3-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">200kHz - 56MHz (I/Q)</tspan></text>
    <text
       x="926"
       y="491.375"
       id="text3191-1-6-3-4-2-7-4-5-1-3-3"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="926"
         y="491.375"
         id="tspan3193-7-0-5-7-3-2-6-0-8-9-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">1x</tspan><tspan
         x="926"
         y="500.375"
         id="tspan4715-9-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">2x</tspan><tspan
         x="926"
         y="509.375"
         id="tspan4717-5-7"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">3x</tspan></text>
    <text
       x="987.99994"
       y="491.375"
       id="text3191-1-6-3-4-2-7-4-5-1-8-7-8"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="987.99994"
         y="491.375"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-6-7"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">1x</tspan><tspan
         x="987.99994"
         y="500.375"
         id="tspan4717-2-5-8"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">2x</tspan></text>
    <text
       x="1054"
       y="491.375"
       id="text3191-1-6-3-4-2-7-4-5-1-8-1-5-3"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1054"
         y="491.375"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-5-1-7"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">1x</tspan><tspan
         x="1054"
         y="500.375"
         id="tspan4717-2-9-2-1"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">2x</tspan></text>
    <text
       x="1112"
       y="491.375"
       id="text3191-1-6-3-4-2-7-4-5-1-8-8-2-7"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1112"
         y="491.375"
         id="tspan3193-7-0-5-7-3-2-6-0-8-3-4-1-2"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">1x</tspan><tspan
         x="1112"
         y="500.375"
         id="tspan4715-5-0-8-2"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">2x</tspan><tspan
         x="1112"
         y="509.375"
         id="tspan4717-2-8-8-4"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">4 x</tspan></text>
    <text
       x="1144"
       y="339.375"
       id="text3191-1-6-3-4-2-7-4-5-70-3-5"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1144"
         y="339.375"
         id="tspan3193-7-0-5-7-3-2-6-0-84-7-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">I</tspan></text>
    <text
       x="1140"
       y="450.375"
       id="text3191-1-6-3-4-2-7-4-5-70-9-6-8"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1140"
         y="450.375"
         id="tspan3193-7-0-5-7-3-2-6-0-84-0-9-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">Q</tspan></text>
    <path
       d="M 1101.0889,489.84038 1130,431.37499"
       id="path1398-4-0-3-0-2"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1094.72"
       y="442.52246"
       id="rect3066-8-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1102.9999"
       y="466.2168"
       id="text3191-6-1"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1102.9999"
         y="466.2168"
         id="tspan3193-2-2"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">FIR</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1033.72"
       y="442.52246"
       id="rect3066-2-57-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1039.9999"
       y="466.2168"
       id="text3191-1-3-0"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1039.9999"
         y="466.2168"
         id="tspan3193-7-6-7"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB1</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="973.99988"
       y="442.52246"
       id="rect3066-5-2-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="979.99988"
       y="466.375"
       id="text3191-8-9-4"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="979.99988"
         y="466.375"
         id="tspan3193-5-1-4"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB2</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="914.99988"
       y="442.52246"
       id="rect3066-2-5-7-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="919.99988"
       y="466.375"
       id="text3191-1-6-27-2"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="919.99988"
         y="466.375"
         id="tspan3193-7-0-3-8"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB3</tspan></text>
    <path
       d="m 893.99998,442.52246 0,38 -28,0 -18,-18 19,-20 z"
       id="path4566-7-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="860.76825"
       y="466.375"
       id="text3191-1-6-8-8-6-6"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="860.76825"
         y="466.375"
         id="tspan3193-7-0-2-8-3-7"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DAC</tspan></text>
    <path
       d="m 695.97268,458.42922 c 0,-105 0,-105 0,-105"
       id="path3999-9-3-8-0-6-96-5-7-0-9"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 680.96256,375.57039 28.86667,-58.43932"
       id="path1398-4-9-2-4"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <path
       d="m 659.99996,246.37499 c 0,160 0,160 0,160"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-6-4-7"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 660.99996,356.37499 c -20.64306,-10.08734 0,-20.17468 0,-20.17468"
       id="path4478-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 638.99996,346.85004 c 565.00004,0 565.00004,0 565.00004,0"
       id="path3999-9-3-8-0-6-1-8-0-1-8"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(0.43250065,0,0,0.43250492,290.61461,277.66745)"
       id="g3993-0-0"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
         transform="matrix(2.7601169,0,0,0.97299086,-634.46397,-63.11085)"
         id="path3969-10-3"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 903.66697,130.71785 c 59.94441,59.18055 63.69637,62.93251 63.69637,62.93251"
         id="path3973-5-8"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 964.4662,130.03877 c -59.1806,59.9444 -62.9325,63.69631 -62.9325,63.69631"
         id="path3973-6-2-6"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 659.99996,405.37499 c 30.00002,0 30.00002,0 30.00002,0"
       id="path3999-9-3-56-2-2-6"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="38"
       height="38"
       ry="0"
       x="674.9726"
       y="387.42926"
       id="rect3066-2-5-75-5-1"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 680.96256,490.57039 28.86667,-58.43932"
       id="path1398-4-9-2-8-4"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <g
       transform="matrix(0.43250065,0,0,0.43250492,290.61461,392.66742)"
       id="g3993-0-5-3"
       style="fill:#ffffff;fill-opacity:1">
      <path
         d="m 584.38177,232.64642 a 15.943601,45.227764 0 1 1 -31.8872,0 15.943601,45.227764 0 1 1 31.8872,0 z"
         transform="matrix(2.7601169,0,0,0.97299086,-634.46397,-63.11085)"
         id="path3969-10-2-1"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-miterlimit:0;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 903.66697,130.71785 c 59.94441,59.18055 63.69637,62.93251 63.69637,62.93251"
         id="path3973-5-4-5"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 964.4662,130.03877 c -59.1806,59.9444 -62.9325,63.69631 -62.9325,63.69631"
         id="path3973-6-2-3-2"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:4.62424755;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="694.08075"
       y="405.42926"
       id="text3191-1-6-8-8-6-4-7-98-2"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="694.08075"
         y="405.42926"
         id="tspan5791-0"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Phase</tspan><tspan
         x="694.08075"
         y="414.42926"
         id="tspan5793-0"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Splitter</tspan></text>
    <path
       d="m 639.99999,346.37499 c 0,52 0,52 0,52"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-6-4"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 795.22245,373.78084 28.75893,-58.43912"
       id="path1398-5-8-3"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="789.99988"
       y="326.52246"
       id="rect3066-2-5-7-5-9-8-1"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 796.00002,336.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-3-1-1"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 797.00002,346.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-0-2-3-0"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 797.00002,357.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-8-2-5-4"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 806.00002,348.37499 c 5.3459,-5.34592 5.3459,-5.34592 5.3459,-5.34592"
       id="path3999-9-3-8-0-6-9-5-1-2"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 805.65402,338.72091 c 5.346,-5.34592 5.346,-5.34592 5.346,-5.34592"
       id="path3999-9-3-8-0-6-9-3-7-5-6"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 1134.5172,370.94526 a 5.5092993,9.3105191 0 0 1 -5.501,9.32409 l -98.8876,0 a 5.5092993,9.3105191 0 0 0 -5.501,9.2965 5.5092993,9.3105191 0 0 0 -5.5173,-9.2965 l -98.87129,0 a 5.5092993,9.3105191 0 0 1 -5.5172,-9.32409"
       id="path3578-3-1-7"
       style="fill:none;stroke:#404040;stroke-width:0.92528909;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 831.69535,369.85834 a 2.6401967,9.5028 0 0 1 -2.63622,9.51665 l -47.38943,0 a 2.6401967,9.5028 0 0 0 -2.63622,9.4885 2.6401967,9.5028 0 0 0 -2.64407,-9.4885 l -47.3816,0 a 2.6401967,9.5028 0 0 1 -2.64406,-9.51665"
       id="path3578-7-8-9-8"
       style="fill:none;stroke:#404040;stroke-width:0.88985944;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none" />
    <path
       d="m 735.19411,373.78084 28.75893,-58.43912"
       id="path1398-5-7-7-0"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="729.99988"
       y="326.52246"
       id="rect3066-2-5-7-5-9-2-4-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 736.00001,336.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-3-3-6-9"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 737.00001,346.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-0-2-9-5-7"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 737.00001,357.37499 c 13,-14 13,13 26.6428,0"
       id="path3999-9-3-8-0-6-5-8-2-6-0-7"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 746.00001,348.37499 c 5.3459,-5.34592 5.3459,-5.34592 5.3459,-5.34592"
       id="path3999-9-3-8-0-6-9-5-3-2-9"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 745.65401,338.72091 c 5.346,-5.34592 5.346,-5.34592 5.346,-5.34592"
       id="path3999-9-3-8-0-6-9-3-7-2-3-2"
       style="fill:none;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="382.375"
       y="-882.99994"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-3-4-2-7-4-5-2-5-9-0"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="382.375"
         y="-882.99994"
         id="tspan3193-7-0-5-7-3-2-6-0-5-0-0-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">320 MSPS</tspan></text>
    <path
       d="M 1101.0889,373.84038 1130,315.37499"
       id="path1398-4-0-3-0-2-6"
       style="stroke:#404040;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1Mend)" />
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1094.72"
       y="326.52246"
       id="rect3066-8-5-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1102.9999"
       y="350.2168"
       id="text3191-6-1-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1102.9999"
         y="350.2168"
         id="tspan3193-2-2-9"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">FIR</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="1033.72"
       y="326.52246"
       id="rect3066-2-57-0-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1039.9999"
       y="350.2168"
       id="text3191-1-3-0-2"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1039.9999"
         y="350.2168"
         id="tspan3193-7-6-7-2"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB1</tspan></text>
    <rect
       width="39.117367"
       height="39.117363"
       ry="0"
       x="973.99988"
       y="326.52246"
       id="rect3066-5-2-4-4"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="979.99988"
       y="350.375"
       id="text3191-8-9-4-4"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="979.99988"
         y="350.375"
         id="tspan3193-5-1-4-5"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB2</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="914.99988"
       y="326.52246"
       id="rect3066-2-5-7-3-0"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="919.99988"
       y="350.375"
       id="text3191-1-6-27-2-7"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="919.99988"
         y="350.375"
         id="tspan3193-7-0-3-8-4"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">HB3</tspan></text>
    <path
       d="m 893.99998,326.52246 0,38 -28,0 -18,-18 19,-20 z"
       id="path4566-7-0-7"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="860.76831"
       y="350.375"
       id="text3191-1-6-8-8-6-6-6"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="860.76831"
         y="350.375"
         id="tspan3193-7-0-2-8-3-7-9"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DAC</tspan></text>
    <path
       d="m 550.99996,236.37499 c 0,-38 0,-38 0,-38"
       id="path5884-8-7"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 540.99996,198.37499 c 10,0 10,0 10,0"
       id="path3999-9-3-8-0-6-96-9-2-0-0"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-2.3611049,0,0,7.499998,581.2499,-6300.7984)"
       id="shape256-1500-9-4-5"
       style="stroke:#000000;stroke-width:0.47527152;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-0-5-5">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-6-8-2"
         style="fill:url(#linearGradient3805);stroke:#000000;stroke-width:0.47527152;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 683.99996,70.37499 c 0,48 0,48 0,48"
       id="path3999-9-3-8-0-5-3-11-8"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="-56.625011"
       y="-568"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-8-8-6-4-7-98-1"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="-56.625011"
         y="-568"
         id="tspan5793-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Input Mux</tspan></text>
    <path
       d="m 1224,15.03918 c 60,0 60,0 60,0"
       id="path3999-9-3-8-0-6-96-9-4-7-9-2-1"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:none" />
    <text
       x="431.99997"
       y="285.375"
       id="text3191-1-6-23-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="431.99997"
         y="285.375"
         id="tspan5342"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:1;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">AUX DAC</tspan></text>
    <path
       d="m 639.99999,418.32071 c 0,45.05428 0,45.05428 0,45.05428"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-6-4-3"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="433.59445"
       y="460.375"
       id="text3191-1-6-23-3-4"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="433.59445"
         y="460.375"
         id="tspan5340"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:1;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">AUX ADC</tspan></text>
    <path
       d="m 569.99996,378.37499 c 0,52 0,52 0,52"
       id="path3999-9-3-8-0-6-96-0-6-9-9-8-6-4-8"
       style="fill:none;stroke:#ff0000;stroke-width:2.03850174;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="595.99994"
       y="-24.62501"
       id="text3191-1-6-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="595.99994"
         y="-24.62501"
         id="tspan3193-7-0-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">LNA</tspan></text>
    <text
       x="777.99994"
       y="-76.625008"
       id="text3191-1-6-2-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="777.99994"
         y="-76.625008"
         id="tspan3193-7-0-0-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TIA</tspan></text>
    <text
       x="777.99994"
       y="37.374989"
       id="text3191-1-6-2-6-7"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="777.99994"
         y="37.374989"
         id="tspan3193-7-0-0-8-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TIA</tspan></text>
    <text
       x="601.99994"
       y="411.375"
       id="text3191-1-6-2-6-5"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="601.99994"
         y="411.375"
         id="tspan3193-7-0-0-8-1"
         style="font-size:9px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">ATTN</tspan></text>
    <g
       transform="matrix(-2.3611049,0,0,5.775822,583.99996,-4402.3879)"
       id="shape256-1500-6-4"
       style="stroke:#000000;stroke-width:0.54158354;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-4-8">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-7-1"
         style="fill:url(#linearGradient3814);stroke:#000000;stroke-width:0.54158354;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <text
       x="405.375"
       y="-569.99994"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-8-8-6-4-7-98-1-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="405.375"
         y="-569.99994"
         id="tspan5793-2-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans">Output Mux</tspan></text>
    <rect
       width="160.00014"
       height="130"
       ry="0"
       x="1164"
       y="118.37499"
       id="rect3066-2-5-5-0-5-6-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.43419003;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1244.1575,203.37499 c 39.8425,0 39.8425,0 39.8425,0"
       id="path3999-9-3-8-0-6-96-2-8-4-1-8"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1263,137.37499 c 31,0 31,0 31,0"
       id="path3999-9-3-8-0-6-96-2-8-4"
       style="fill:none;stroke:#0000ff;stroke-width:2.00000215;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1194,153.37499 c 100,0 100,0 100,0"
       id="path3999-9-3-8-0-6-96-2-8-4-1"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1254,233.37499 c 92,0 92,0 92,0"
       id="path3999-9-3-8-0-6-96-2-8-9"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1193,152.37499 c 0,39 0,39 0,39"
       id="path3999-9-3-8-0-6-96-2-8-4-1-1"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1316,151.37499 c 18,0 18,0 18,0"
       id="path3999-9-3-8-0-6-96-2-8-4-1-5"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1263,167.37499 c 33,0 33,0 33,0"
       id="path3999-9-3-8-0-6-96-2-8-4-1-2"
       style="fill:none;stroke:#000000;stroke-width:2.03101087;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <g
       transform="matrix(-2.3611049,0,0,2.8493069,1316,-2221.428)"
       id="shape256-1500"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302"
         style="fill:url(#linearGradient6661);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 1192,213.37499 c 42,0 42,0 42,0"
       id="path3999-9-3-8-0-6-96-9-4-7-9-7-0"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="19.999994"
       height="180"
       ry="0"
       x="1334"
       y="93.374992"
       id="rect3066-2-5-5-0-5-6-3-2"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2.5815618;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:3.5999999;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="101.37498"
       y="-1340"
       transform="matrix(0,1,-1,0,0,0)"
       id="text3191-1-6-23-0-6-3"
       xml:space="preserve"
       style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="101.37498"
         y="-1340"
         id="tspan3193-7-0-4-6-79-5"
         style="font-size:12px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">CMOS / LVDS INTERFACE</tspan></text>
    <g
       transform="translate(121,-43.999999)"
       id="g15626">
      <rect
         width="10"
         height="10"
         x="900"
         y="325"
         transform="translate(337.99996,-100.62501)"
         id="rect15599"
         style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
      <path
         d="m 900,325 c 10,10 10,10 10,10"
         transform="translate(337.99996,-100.62501)"
         id="path15601"
         style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
      <path
         d="m 910,325 c -10,10 -10,10 -10,10"
         transform="translate(337.99996,-100.62501)"
         id="path15603"
         style="fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    </g>
    <text
       x="1246"
       y="259.375"
       id="text3191-1-6-3-4-2-7-4-5-2-2-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1246"
         y="259.375"
         id="tspan3193-7-0-5-7-3-2-6-0-5-9-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">Tx 61.44 MSPS</tspan></text>
    <path
       d="m 1193,168.37499 c 0,45 0,45 0,45"
       id="path3999-9-3-8-0-6-96-9-4-7-9-7-0-7"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <rect
       width="38"
       height="38"
       ry="0"
       x="1173.9999"
       y="165.37497"
       id="rect3066-2-5-5-0-5-6-5"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1192.1952"
       y="182.37497"
       id="text3191-1-6-23-0-6-2-2"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1192.1952"
         y="182.37497"
         id="tspan8619-9"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">LOOP</tspan><tspan
         x="1192.1952"
         y="193.37497"
         id="tspan8650"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">BACK</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="1274"
       y="183.37498"
       id="rect3066-2-5-5-0-5-6-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="1294.0001"
       y="201.37502"
       id="text3191-1-6-23-0-6-2-6"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1294.0001"
         y="201.37502"
         id="tspan8619-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">PN &amp;</tspan><tspan
         x="1294.0001"
         y="212.37502"
         id="tspan3890"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:center;line-height:110.00000238%;writing-mode:lr-tb;text-anchor:middle;font-family:Sans;-inkscape-font-specification:Sans Bold">BIST</tspan></text>
    <g
       transform="matrix(2.3611049,0,0,-2.8493069,1234,2588.2132)"
       id="shape256-1500-6"
       style="stroke:#000000;stroke-width:0.77108586;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none">
      <title
         id="title2300-4">Sheet.256</title>
      <v:userDefs>
        <v:ud
           v:val="VT0(36):26"
           v:nameU="msvThemeColors" />
        <v:ud
           v:val="VT0(16):26"
           v:nameU="msvThemeEffects" />
      </v:userDefs>
      <path
         d="m 9,823.89 0,18 -9,-2.57 0,-12.86 9,-2.57 z"
         id="path2302-7"
         style="fill:url(#linearGradient5179);stroke:#000000;stroke-width:0.77108586;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    </g>
    <path
       d="m 1263.2334,-81.62501 c 0,204.63834 0,220 0,220"
       id="path3999-9-3-8-0-6-96-9-9-5-3-9"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1283.2334,-101.62501 c 0,223.24183 0,240 0,240"
       id="path3999-9-3-8-0-6-96-9-9-5-3-9-5"
       style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1224,213.37499 c 0,251.14708 0,270 0,270"
       id="path3999-9-3-8-0-6-96-9-9-5-3-9-0"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 1204,213.37499 c 0,232.54357 0,250 0,250"
       id="path3999-9-3-8-0-6-96-9-9-5-3-9-0-1"
       style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <path
       d="m 935.99996,33.37499 -0.35383,-176"
       id="path1398-4-1-7-4-3-7"
       style="stroke:#af00af;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendaB)" />
    <path
       d="m 1156,33.37499 -0.3539,-176"
       id="path1398-4-1-7-4-3-50"
       style="stroke:#af00af;stroke-width:1;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:none;marker-mid:none;marker-end:url(#Arrow1MendHS)" />
    <path
       d="m 1264,168.37499 c 0,34 0,34 0,34"
       id="path3999-9-3-8-0-6-96-2-8-4-1-1-8"
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="711.99994"
       y="197.37498"
       id="text3191-1-6-3-4-2-7-4-9"
       xml:space="preserve"
       style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="711.99994"
         y="197.37498"
         id="tspan5013-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">715 MHz - 1430 MHz</tspan></text>
    <rect
       width="38"
       height="38"
       ry="0"
       x="445.99997"
       y="165.37498"
       id="rect3066-2-5-75-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none" />
    <text
       x="447.99997"
       y="187.37498"
       id="text3191-1-6-23-72"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="447.99997"
         y="187.37498"
         id="tspan3193-7-0-4-0"
         style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">DCXO</tspan></text>
    <path
       d="m 569.69492,186.36695 c 14.30504,-29.99196 14.30504,30.00804 26.6755,-1.9671"
       id="path3999-9-3-8-0-6-5-8-7-6-3"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <path
       d="m 569.69492,236.36695 c 14.30504,-29.99196 14.30504,30.00804 26.6755,-1.9671"
       id="path3999-9-3-8-0-6-5-8-7-6-3-6"
       style="fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />
    <text
       x="1304"
       y="-59.625008"
       id="text3191-1-6-3-4-2-7-4-5-1-8-8-0-1"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1304"
         y="-59.625008"
         id="tspan4717-2-8-9-4"
         style="font-size:8px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">VDD_GPO</tspan></text>
    <text
       x="1289"
       y="-119.62501"
       id="text3191-1-6-3-4-2-7-4-5-1-8-8-0-1-1"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1289"
         y="-119.62501"
         id="tspan4717-2-8-9-4-2"
         style="font-size:8px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">VDD_INTERFACE</tspan></text>
    <text
       x="1304"
       y="-179.62502"
       id="text3191-1-6-3-4-2-7-4-5-1-8-8-0-1-1-6"
       xml:space="preserve"
       style="font-size:9px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"><tspan
         x="1304"
         y="-179.62502"
         id="tspan4717-2-8-9-4-2-1"
         style="font-size:8px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:start;line-height:100%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans">VDD_MAIN</tspan></text>
    <text
       x="364.43259"
       y="-128.625"
       id="text3191-1-7-9-3-4"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="364.43259"
         y="-128.625"
         id="tspan3193-7-4-8-2-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2A_P,</tspan><tspan
         x="364.43259"
         y="-116.125"
         id="tspan8637"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2A_N</tspan><tspan
         x="364.43259"
         y="-103.625"
         id="tspan8639"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1A_P,</tspan><tspan
         x="364.43259"
         y="-91.125"
         id="tspan8635"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1A_N</tspan></text>
    <text
       x="364.54977"
       y="-78.625008"
       id="text3191-1-7-9-3-4-2"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="364.54977"
         y="-78.625008"
         id="tspan3193-7-4-8-2-0-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2B_P,</tspan><tspan
         x="364.54977"
         y="-66.125008"
         id="tspan8637-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2B_N</tspan><tspan
         x="364.54977"
         y="-53.625008"
         id="tspan8639-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1B_P,</tspan><tspan
         x="364.54977"
         y="-41.125008"
         id="tspan8635-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1B_N</tspan></text>
    <text
       x="364.05417"
       y="-26.62501"
       id="text3191-1-7-9-3-4-2-0"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="364.05417"
         y="-26.62501"
         id="tspan3193-7-4-8-2-0-3-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2C_P,</tspan><tspan
         x="364.05417"
         y="-14.12501"
         id="tspan8637-0-8"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX2C_N</tspan><tspan
         x="364.05417"
         y="-1.6250095"
         id="tspan8639-0-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1C_P,</tspan><tspan
         x="364.05417"
         y="10.87499"
         id="tspan8701"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX1C_N</tspan></text>
    <text
       x="410.75388"
       y="27.374989"
       id="text3191-1-7-9-3-4-2-07"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.75388"
         y="27.374989"
         id="tspan8635-7-9"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">TXMON2</tspan></text>
    <text
       x="410.57321"
       y="45.374989"
       id="text3191-1-7-9-3-4-2-07-4"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.57321"
         y="45.374989"
         id="tspan8635-7-9-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">TXMON1</tspan></text>
    <text
       x="410.38766"
       y="103.37498"
       id="text3191-1-7-9-3-4-2-07-7"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.38766"
         y="103.37498"
         id="tspan8635-7-9-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">RXLO</tspan></text>
    <text
       x="410.38766"
       y="265.375"
       id="text3191-1-7-9-3-4-2-07-7-2"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.38766"
         y="265.375"
         id="tspan8635-7-9-6-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">TXLO</tspan></text>
    <text
       x="1380.0522"
       y="315.37497"
       id="text3191-1-7-9-3-4-2-07-7-3"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1380.0522"
         y="315.37497"
         id="tspan8635-7-9-6-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">SPI</tspan></text>
    <text
       x="1380.272"
       y="367.375"
       id="text3191-1-7-9-3-4-2-07-7-3-5"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1380.272"
         y="367.375"
         id="tspan8635-7-9-6-4-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">CTRL</tspan></text>
    <text
       x="410.57321"
       y="307.375"
       id="text3191-1-7-9-3-4-2-07-7-7"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.57321"
         y="307.375"
         id="tspan8635-7-9-6-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">AUXDAC1</tspan><tspan
         x="410.57321"
         y="319.875"
         id="tspan8843"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">AUXDAC2</tspan></text>
    <text
       x="366.44235"
       y="353.375"
       id="text3191-1-7-9-3-4-2-0-8"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="366.44235"
         y="353.375"
         id="tspan3193-7-4-8-2-0-3-4-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX2A_P,</tspan><tspan
         x="366.44235"
         y="365.875"
         id="tspan8637-0-8-2"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX2A_N</tspan><tspan
         x="366.44235"
         y="378.375"
         id="tspan8639-0-2-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX1A_P,</tspan><tspan
         x="366.44235"
         y="390.875"
         id="tspan8701-9"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX1A_N</tspan></text>
    <text
       x="366.55954"
       y="409.375"
       id="text3191-1-7-9-3-4-2-0-8-9"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="366.55954"
         y="409.375"
         id="tspan3193-7-4-8-2-0-3-4-2-9"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX2B_P,</tspan><tspan
         x="366.55954"
         y="421.875"
         id="tspan8637-0-8-2-7"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX2B_N</tspan><tspan
         x="366.55954"
         y="434.375"
         id="tspan8639-0-2-4-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX1B_P,</tspan><tspan
         x="366.55954"
         y="446.875"
         id="tspan8701-9-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX1B_N</tspan></text>
    <text
       x="410.53415"
       y="485.375"
       id="text3191-1-7-9-3-4-2-07-7-7-2"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.53415"
         y="485.375"
         id="tspan8843-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">AUXADC</tspan></text>
    <text
       x="410.29489"
       y="177.37498"
       id="text3191-1-7-9-3-4-2-07-7-7-24"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.29489"
         y="177.37498"
         id="tspan8957"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">XTALP</tspan></text>
    <text
       x="410.81735"
       y="199.37498"
       id="text3191-1-7-9-3-4-2-07-7-7-24-5"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="410.81735"
         y="199.37498"
         id="tspan8957-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">XTALN</tspan></text>
    <text
       x="409.99997"
       y="-170.62505"
       id="text3191-1-7-9-3-4-26"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:end;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="409.99997"
         y="-170.62505"
         id="tspan8635-4"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">RADIO</tspan><tspan
         x="409.99997"
         y="-158.12505"
         id="tspan9025"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:end;line-height:125%;writing-mode:lr-tb;text-anchor:end;font-family:Sans;-inkscape-font-specification:Sans Bold">SWITCHING</tspan></text>
    <text
       x="1379.8521"
       y="417.37497"
       id="text3191-1-7-9-3-4-2-07-7-3-5-3"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1379.8521"
         y="417.37497"
         id="tspan8635-7-9-6-4-7-5"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RESETB</tspan></text>
    <text
       x="1380.7212"
       y="161.37495"
       id="text3191-1-7-9-3-4-2-07-7-3-5-3-8"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1380.7212"
         y="161.37495"
         id="tspan8635-7-9-6-4-7-5-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">P0_[D11:D0]/</tspan><tspan
         x="1380.7212"
         y="173.87495"
         id="tspan9069"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">TX_[D5:D0]</tspan><tspan
         x="1380.7212"
         y="186.37495"
         id="tspan9071"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold" /><tspan
         x="1380.7212"
         y="198.87495"
         id="tspan9073"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">P1_[D11:D0]/</tspan><tspan
         x="1380.7212"
         y="211.37495"
         id="tspan9075"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">RX_[D5:D0]</tspan></text>
    <text
       x="1380.272"
       y="27.374962"
       id="text3191-1-7-9-3-4-2-07-7-3-3"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1380.272"
         y="27.374962"
         id="tspan8635-7-9-6-4-0"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">GND</tspan></text>
    <text
       x="1379.6421"
       y="-32.625038"
       id="text3191-1-7-9-3-4-2-07-7-3-1"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1379.6421"
         y="-32.625038"
         id="tspan8635-7-9-6-4-02"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">1.8 - 3.3V</tspan></text>
    <text
       x="1379.6421"
       y="-92.625038"
       id="text3191-1-7-9-3-4-2-07-7-3-1-0"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1379.6421"
         y="-92.625038"
         id="tspan8635-7-9-6-4-02-6"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">1.2V - 2.5V</tspan></text>
    <text
       x="1379.6421"
       y="-152.62505"
       id="text3191-1-7-9-3-4-2-07-7-3-1-7"
       xml:space="preserve"
       style="font-size:11px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans Bold"><tspan
         x="1379.6421"
         y="-152.62505"
         id="tspan8635-7-9-6-4-02-3"
         style="font-size:10px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:125%;writing-mode:lr-tb;text-anchor:start;font-family:Sans;-inkscape-font-specification:Sans Bold">1.3 V</tspan></text>
  </g>
</svg>
</div>


需要考虑的一些事项如下：
- Tx LO 幅值保持不变，因此为接收到最佳信号，尽可能地以最大比特位数运行 DAC，然后调高/调低输出衰减以改变输出信号强度，（不要只减少 DAC 的输入）。DAC 最大比特位数为12位，但实际上使用 ADI 提供的 HDL 需要产生 16-bit 信号，其中低4位 LSB 会被去除。有关这些接口更多信息，请查阅 [AXI_AD9361](https://wiki.analog.com/resources/fpga/docs/axi_ad9361) 文档。  

## 发送器性能

在[性能部分](https://wiki.analog.com/university/tools/pluto/devs/performance)中查询更多相关细节。  
性能包含很多方面，其中最主要的两点为：  

- 输出功率（传输距离）
- 输出保真度（传输精准度）  

### 传输功率
现在多数频谱仪可测量特定频率范围内（即通道带宽）的功率，频谱仪在该频率范围内产生许多小的测量样本 Pi ，计算这些功率测量值的均值并通过以下公式求目标频率范围内的通道功率。  
![](https://wiki.analog.com/lib/plugins/mathpublish/img.php?img=589d50491ef96706093af1cc90a6d8a2)

其中 PCH 是通道功率，BS 是指定带宽（也称为通道带宽），BN 是分辨率带宽（RBW）使用的等效噪声带宽，N 是数据点数总和，Pi 是测量 i 中的功率样本值，单位是 dB（若 Pi 单位是 dBm，则 Pch 单位为毫瓦）。n1 和 n2 是标记 i 在通道带宽之间的端点，因此我们得到：


![](https://wiki.analog.com/lib/plugins/mathpublish/img.php?img=36353f8f660cd8442254fab228362657)  [^1]

在该测试中，设备将用不同 LO 频率发射 LTE10 信号，并测量和记录 9 MHz 通道的功率：


<div width="100%" style="overflow-x: auto;"> 
   <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" style="fill-opacity:1; color-rendering:auto; color-interpolation:auto; stroke:black; text-rendering:auto; stroke-linecap:square; stroke-miterlimit:10; stroke-opacity:1; shape-rendering:auto; fill:black; stroke-dasharray:none; font-weight:normal; stroke-width:1; font-family:'Dialog'; font-style:normal; stroke-linejoin:miter; font-size:12px; stroke-dashoffset:0; image-rendering:auto;" width="100%" height="100%" viewBox="0 0 732 569" preserveAspectRatio="xMidYMid slice"><!--Generated by the Batik Graphics2D SVG Generator--><defs id="genericDefs"/><g><defs id="defs1"><clipPath clipPathUnits="userSpaceOnUse" id="clipPath1"><path d="M0 0 L732 0 L732 569 L0 569 L0 0 Z"/></clipPath><font horiz-adv-x="75.0" id="font1"><font-face ascent="100.53711" descent="21.972656" units-per-em="100" style="font-style:normal; font-family:SansSerif; font-weight:normal;"/><missing-glyph horiz-adv-x="75.0" d="M12.5 0 L12.5 62.5 L62.5 62.5 L62.5 0 L12.5 0 ZM14.0625 1.5625 L60.9375 1.5625 L60.9375 60.9375 L14.0625 60.9375 L14.0625 1.5625 Z"/><glyph unicode="0" horiz-adv-x="55.615234" d="M4.1562 35.2969 Q4.1562 48 6.7656 55.7422 Q9.375 63.4844 14.5234 67.6797 Q19.6719 71.875 27.4844 71.875 Q33.25 71.875 37.5938 69.5547 Q41.9375 67.2344 44.7734 62.8672 Q47.6094 58.5 49.2188 52.2266 Q50.8281 45.9531 50.8281 35.2969 Q50.8281 22.7031 48.2422 14.9688 Q45.6562 7.2344 40.5078 3.0078 Q35.3594 -1.2188 27.4844 -1.2188 Q17.1406 -1.2188 11.2344 6.2031 Q4.1562 15.1406 4.1562 35.2969 ZM13.1875 35.2969 Q13.1875 17.6719 17.3125 11.8359 Q21.4375 6 27.4844 6 Q33.5469 6 37.6719 11.8594 Q41.7969 17.7188 41.7969 35.2969 Q41.7969 52.9844 37.6719 58.7891 Q33.5469 64.5938 27.3906 64.5938 Q21.3438 64.5938 17.7188 59.4688 Q13.1875 52.9375 13.1875 35.2969 Z"/><glyph unicode="1" horiz-adv-x="55.615234" d="M37.25 0 L28.4688 0 L28.4688 56 Q25.2969 52.9844 20.1406 49.9531 Q14.9844 46.9219 10.8906 45.4062 L10.8906 53.9062 Q18.2656 57.375 23.7812 62.3047 Q29.2969 67.2344 31.5938 71.875 L37.25 71.875 L37.25 0 Z"/><glyph unicode="2" horiz-adv-x="55.615234" d="M50.3438 8.4531 L50.3438 0 L3.0312 0 Q2.9375 3.1719 4.0469 6.1094 Q5.8594 10.9375 9.8359 15.625 Q13.8125 20.3125 21.3438 26.4688 Q33.0156 36.0312 37.1172 41.625 Q41.2188 47.2188 41.2188 52.2031 Q41.2188 57.4219 37.4766 61.0078 Q33.7344 64.5938 27.7344 64.5938 Q21.3906 64.5938 17.5781 60.7891 Q13.7656 56.9844 13.7188 50.25 L4.6875 51.1719 Q5.6094 61.2812 11.6641 66.5781 Q17.7188 71.875 27.9375 71.875 Q38.2344 71.875 44.2422 66.1641 Q50.25 60.4531 50.25 52 Q50.25 47.7031 48.4922 43.5547 Q46.7344 39.4062 42.6562 34.8125 Q38.5781 30.2188 29.1094 22.2188 Q21.1875 15.5781 18.9453 13.2109 Q16.7031 10.8438 15.2344 8.4531 L50.3438 8.4531 Z"/><glyph unicode="3" horiz-adv-x="55.615234" d="M4.2031 18.8906 L12.9844 20.0625 Q14.5 12.5938 18.1406 9.2969 Q21.7812 6 27 6 Q33.2031 6 37.4766 10.2969 Q41.75 14.5938 41.75 20.9531 Q41.75 27 37.7969 30.9297 Q33.8438 34.8594 27.7344 34.8594 Q25.25 34.8594 21.5312 33.8906 L22.5156 41.6094 Q23.3906 41.5 23.9219 41.5 Q29.5469 41.5 34.0391 44.4297 Q38.5312 47.3594 38.5312 53.4688 Q38.5312 58.2969 35.2578 61.4766 Q31.9844 64.6562 26.8125 64.6562 Q21.6875 64.6562 18.2656 61.4297 Q14.8438 58.2031 13.875 51.7656 L5.0781 53.3281 Q6.6875 62.1562 12.3984 67.0156 Q18.1094 71.875 26.6094 71.875 Q32.4688 71.875 37.3984 69.3594 Q42.3281 66.8438 44.9453 62.5 Q47.5625 58.1562 47.5625 53.2656 Q47.5625 48.6406 45.0703 44.8281 Q42.5781 41.0156 37.7031 38.7656 Q44.0469 37.3125 47.5625 32.6953 Q51.0781 28.0781 51.0781 21.1406 Q51.0781 11.7656 44.2422 5.25 Q37.4062 -1.2656 26.9531 -1.2656 Q17.5312 -1.2656 11.3047 4.3516 Q5.0781 9.9688 4.2031 18.8906 Z"/><glyph unicode="4" horiz-adv-x="55.615234" d="M32.3281 0 L32.3281 17.1406 L1.2656 17.1406 L1.2656 25.2031 L33.9375 71.5781 L41.1094 71.5781 L41.1094 25.2031 L50.7812 25.2031 L50.7812 17.1406 L41.1094 17.1406 L41.1094 0 L32.3281 0 ZM32.3281 25.2031 L32.3281 57.4688 L9.9062 25.2031 L32.3281 25.2031 Z"/><glyph unicode="5" horiz-adv-x="55.615234" d="M4.1562 18.75 L13.375 19.5312 Q14.4062 12.7969 18.1406 9.3984 Q21.875 6 27.1562 6 Q33.5 6 37.8906 10.7891 Q42.2812 15.5781 42.2812 23.4844 Q42.2812 31 38.0625 35.3516 Q33.8438 39.7031 27 39.7031 Q22.75 39.7031 19.3359 37.7734 Q15.9219 35.8438 13.9688 32.7656 L5.7188 33.8438 L12.6406 70.6094 L48.25 70.6094 L48.25 62.2031 L19.6719 62.2031 L15.8281 42.9688 Q22.2656 47.4688 29.3438 47.4688 Q38.7188 47.4688 45.1641 40.9688 Q51.6094 34.4688 51.6094 24.2656 Q51.6094 14.5469 45.9531 7.4688 Q39.0625 -1.2188 27.1562 -1.2188 Q17.3906 -1.2188 11.2109 4.25 Q5.0312 9.7188 4.1562 18.75 Z"/><glyph unicode="6" horiz-adv-x="55.615234" d="M49.75 54.0469 L41.0156 53.375 Q39.8438 58.5469 37.7031 60.8906 Q34.125 64.6562 28.9062 64.6562 Q24.7031 64.6562 21.5312 62.3125 Q17.3906 59.2812 14.9922 53.4688 Q12.5938 47.6562 12.5 36.9219 Q15.6719 41.75 20.2656 44.0938 Q24.8594 46.4375 29.8906 46.4375 Q38.6719 46.4375 44.8516 39.9688 Q51.0312 33.5 51.0312 23.25 Q51.0312 16.5 48.125 10.7188 Q45.2188 4.9375 40.1406 1.8594 Q35.0625 -1.2188 28.6094 -1.2188 Q17.625 -1.2188 10.6953 6.8594 Q3.7656 14.9375 3.7656 33.5 Q3.7656 54.25 11.4219 63.6719 Q18.1094 71.875 29.4375 71.875 Q37.8906 71.875 43.2891 67.1406 Q48.6875 62.4062 49.75 54.0469 ZM13.875 23.1875 Q13.875 18.6562 15.7969 14.5078 Q17.7188 10.3594 21.1875 8.1797 Q24.6562 6 28.4688 6 Q34.0312 6 38.0391 10.4922 Q42.0469 14.9844 42.0469 22.7031 Q42.0469 30.125 38.0859 34.3984 Q34.125 38.6719 28.125 38.6719 Q22.1719 38.6719 18.0234 34.3984 Q13.875 30.125 13.875 23.1875 Z"/><glyph unicode=")" horiz-adv-x="33.30078" d="M12.3594 -21.0469 L6.0625 -21.0469 Q20.6562 2.3906 20.6562 25.875 Q20.6562 35.0625 18.5625 44.0938 Q16.8906 51.4219 13.9219 58.1562 Q12.0156 62.5469 6.0625 72.7969 L12.3594 72.7969 Q21.5312 60.5469 25.9219 48.1875 Q29.6875 37.5469 29.6875 25.9219 Q29.6875 12.75 24.6328 0.4453 Q19.5781 -11.8594 12.3594 -21.0469 Z"/><glyph unicode="z" horiz-adv-x="50.0" d="M1.9531 0 L1.9531 7.125 L34.9688 45.0156 Q29.3438 44.7344 25.0469 44.7344 L3.9062 44.7344 L3.9062 51.8594 L46.2969 51.8594 L46.2969 46.0469 L18.2188 13.1406 L12.7969 7.125 Q18.7031 7.5625 23.875 7.5625 L47.8594 7.5625 L47.8594 0 L1.9531 0 Z"/><glyph unicode="H" horiz-adv-x="72.2168" d="M8.0156 0 L8.0156 71.5781 L17.4844 71.5781 L17.4844 42.1875 L54.6875 42.1875 L54.6875 71.5781 L64.1562 71.5781 L64.1562 0 L54.6875 0 L54.6875 33.7344 L17.4844 33.7344 L17.4844 0 L8.0156 0 Z"/><glyph unicode="G" horiz-adv-x="77.7832" d="M41.2188 28.0781 L41.2188 36.4688 L71.5312 36.5312 L71.5312 9.9688 Q64.5469 4.3906 57.125 1.5859 Q49.7031 -1.2188 41.8906 -1.2188 Q31.3438 -1.2188 22.7266 3.2969 Q14.1094 7.8125 9.7188 16.3594 Q5.3281 24.9062 5.3281 35.4531 Q5.3281 45.9062 9.6953 54.9609 Q14.0625 64.0156 22.2656 68.4062 Q30.4688 72.7969 41.1562 72.7969 Q48.9219 72.7969 55.1953 70.2891 Q61.4688 67.7812 65.0391 63.2891 Q68.6094 58.7969 70.4531 51.5625 L61.9219 49.2188 Q60.2969 54.6875 57.9062 57.8125 Q55.5156 60.9375 51.0703 62.8203 Q46.625 64.7031 41.2188 64.7031 Q34.7188 64.7031 29.9844 62.7266 Q25.25 60.75 22.3438 57.5234 Q19.4375 54.2969 17.8281 50.4375 Q15.0938 43.7969 15.0938 36.0312 Q15.0938 26.4688 18.3906 20.0234 Q21.6875 13.5781 27.9844 10.4531 Q34.2812 7.3281 41.3594 7.3281 Q47.5156 7.3281 53.375 9.6953 Q59.2344 12.0625 62.25 14.75 L62.25 28.0781 L41.2188 28.0781 Z"/><glyph unicode="(" horiz-adv-x="33.30078" d="M23.3906 -21.0469 Q16.1094 -11.8594 11.0859 0.4453 Q6.0625 12.75 6.0625 25.9219 Q6.0625 37.5469 9.8125 48.1875 Q14.2031 60.5469 23.3906 72.7969 L29.6875 72.7969 Q23.7812 62.6406 21.875 58.2969 Q18.8906 51.5625 17.1875 44.2344 Q15.0938 35.1094 15.0938 25.875 Q15.0938 2.3906 29.6875 -21.0469 L23.3906 -21.0469 Z"/><glyph unicode=" " horiz-adv-x="27.783203" d=""/><glyph unicode="y" horiz-adv-x="50.0" d="M6.2031 -19.9688 L5.2188 -11.7188 Q8.1094 -12.5 10.25 -12.5 Q13.1875 -12.5 14.9453 -11.5234 Q16.7031 -10.5469 17.8281 -8.7969 Q18.6562 -7.4688 20.5156 -2.25 Q20.75 -1.5156 21.2969 -0.0938 L1.6094 51.8594 L11.0781 51.8594 L21.875 21.8281 Q23.9688 16.1094 25.6406 9.8125 Q27.1562 15.875 29.25 21.625 L40.3281 51.8594 L49.125 51.8594 L29.3906 -0.875 Q26.2188 -9.4219 24.4688 -12.6406 Q22.125 -17 19.0938 -19.0234 Q16.0625 -21.0469 11.8594 -21.0469 Q9.3281 -21.0469 6.2031 -19.9688 Z"/><glyph unicode="c" horiz-adv-x="50.0" d="M40.4375 19 L49.0781 17.875 Q47.6562 8.9375 41.8203 3.8828 Q35.9844 -1.1719 27.4844 -1.1719 Q16.8438 -1.1719 10.375 5.7891 Q3.9062 12.75 3.9062 25.7344 Q3.9062 34.125 6.6875 40.4297 Q9.4688 46.7344 15.1562 49.8828 Q20.8438 53.0312 27.5469 53.0312 Q35.9844 53.0312 41.3594 48.7578 Q46.7344 44.4844 48.25 36.625 L39.7031 35.2969 Q38.4844 40.5312 35.3828 43.1641 Q32.2812 45.7969 27.875 45.7969 Q21.2344 45.7969 17.0859 41.0391 Q12.9375 36.2812 12.9375 25.9844 Q12.9375 15.5312 16.9453 10.7969 Q20.9531 6.0625 27.3906 6.0625 Q32.5625 6.0625 36.0312 9.2344 Q39.5 12.4062 40.4375 19 Z"/><glyph unicode="n" horiz-adv-x="55.615234" d="M6.5938 0 L6.5938 51.8594 L14.5 51.8594 L14.5 44.4844 Q20.2188 53.0312 31 53.0312 Q35.6875 53.0312 39.625 51.3438 Q43.5625 49.6562 45.5156 46.9219 Q47.4688 44.1875 48.25 40.4375 Q48.7344 37.9844 48.7344 31.8906 L48.7344 0 L39.9375 0 L39.9375 31.5469 Q39.9375 36.9219 38.9141 39.5781 Q37.8906 42.2344 35.2812 43.8203 Q32.6719 45.4062 29.1562 45.4062 Q23.5312 45.4062 19.4531 41.8438 Q15.375 38.2812 15.375 28.3281 L15.375 0 L6.5938 0 Z"/><glyph unicode="u" horiz-adv-x="55.615234" d="M40.5781 0 L40.5781 7.625 Q34.5156 -1.1719 24.125 -1.1719 Q19.5312 -1.1719 15.5547 0.5859 Q11.5781 2.3438 9.6484 5.0078 Q7.7188 7.6719 6.9375 11.5312 Q6.3906 14.1094 6.3906 19.7344 L6.3906 51.8594 L15.1875 51.8594 L15.1875 23.0938 Q15.1875 16.2188 15.7188 13.8125 Q16.5469 10.3594 19.2344 8.375 Q21.9219 6.3906 25.875 6.3906 Q29.8281 6.3906 33.2969 8.4219 Q36.7656 10.4531 38.2109 13.9453 Q39.6562 17.4375 39.6562 24.0781 L39.6562 51.8594 L48.4375 51.8594 L48.4375 0 L40.5781 0 Z"/><glyph unicode="q" horiz-adv-x="55.615234" d="M39.6562 -19.875 L39.6562 5.5156 Q37.5938 2.6406 33.9062 0.7344 Q30.2188 -1.1719 26.0781 -1.1719 Q16.8438 -1.1719 10.1797 6.2031 Q3.5156 13.5781 3.5156 26.4219 Q3.5156 34.2344 6.2266 40.4297 Q8.9375 46.625 14.0859 49.8281 Q19.2344 53.0312 25.3906 53.0312 Q35.0156 53.0312 40.5312 44.9219 L40.5312 51.8594 L48.4375 51.8594 L48.4375 -19.875 L39.6562 -19.875 ZM12.5469 26.0781 Q12.5469 16.0625 16.75 11.0625 Q20.9531 6.0625 26.8125 6.0625 Q32.4219 6.0625 36.4766 10.8203 Q40.5312 15.5781 40.5312 25.2969 Q40.5312 35.6406 36.2578 40.8672 Q31.9844 46.0938 26.2188 46.0938 Q20.5156 46.0938 16.5312 41.2344 Q12.5469 36.375 12.5469 26.0781 Z"/><glyph unicode="e" horiz-adv-x="55.615234" d="M42.0938 16.7031 L51.1719 15.5781 Q49.0312 7.625 43.2188 3.2266 Q37.4062 -1.1719 28.375 -1.1719 Q17 -1.1719 10.3281 5.8359 Q3.6562 12.8438 3.6562 25.4844 Q3.6562 38.5781 10.3984 45.8047 Q17.1406 53.0312 27.875 53.0312 Q38.2812 53.0312 44.875 45.9531 Q51.4688 38.875 51.4688 26.0312 Q51.4688 25.25 51.4219 23.6875 L12.75 23.6875 Q13.2344 15.1406 17.5781 10.6016 Q21.9219 6.0625 28.4219 6.0625 Q33.25 6.0625 36.6719 8.6016 Q40.0938 11.1406 42.0938 16.7031 ZM13.2344 30.9062 L42.1875 30.9062 Q41.6094 37.4531 38.875 40.7188 Q34.6719 45.7969 27.9844 45.7969 Q21.9219 45.7969 17.7969 41.75 Q13.6719 37.7031 13.2344 30.9062 Z"/><glyph unicode="r" horiz-adv-x="33.30078" d="M6.5 0 L6.5 51.8594 L14.4062 51.8594 L14.4062 44 Q17.4375 49.5156 20 51.2734 Q22.5625 53.0312 25.6406 53.0312 Q30.0781 53.0312 34.6719 50.2031 L31.6406 42.0469 Q28.4219 43.9531 25.2031 43.9531 Q22.3125 43.9531 20.0156 42.2188 Q17.7188 40.4844 16.75 37.4062 Q15.2812 32.7188 15.2812 27.1562 L15.2812 0 L6.5 0 Z"/><glyph unicode="F" horiz-adv-x="61.083984" d="M8.2031 0 L8.2031 71.5781 L56.5 71.5781 L56.5 63.1406 L17.6719 63.1406 L17.6719 40.9688 L51.2656 40.9688 L51.2656 32.5156 L17.6719 32.5156 L17.6719 0 L8.2031 0 Z"/><glyph unicode="7" horiz-adv-x="55.615234" d="M4.7344 62.2031 L4.7344 70.6562 L51.0781 70.6562 L51.0781 63.8125 Q44.2344 56.5469 37.5234 44.4844 Q30.8125 32.4219 27.1562 19.6719 Q24.5156 10.6875 23.7812 0 L14.75 0 Q14.8906 8.4531 18.0625 20.4141 Q21.2344 32.375 27.1719 43.4844 Q33.1094 54.5938 39.7969 62.2031 L4.7344 62.2031 Z"/><glyph unicode="8" horiz-adv-x="55.615234" d="M17.6719 38.8125 Q12.2031 40.8281 9.5703 44.5391 Q6.9375 48.25 6.9375 53.4219 Q6.9375 61.2344 12.5547 66.5547 Q18.1719 71.875 27.4844 71.875 Q36.8594 71.875 42.5781 66.4297 Q48.2969 60.9844 48.2969 53.1719 Q48.2969 48.1875 45.6797 44.5078 Q43.0625 40.8281 37.75 38.8125 Q44.3438 36.6719 47.7812 31.8828 Q51.2188 27.0938 51.2188 20.4531 Q51.2188 11.2812 44.7266 5.0312 Q38.2344 -1.2188 27.6406 -1.2188 Q17.0469 -1.2188 10.5469 5.0547 Q4.0469 11.3281 4.0469 20.7031 Q4.0469 27.6875 7.5938 32.3984 Q11.1406 37.1094 17.6719 38.8125 ZM15.9219 53.7188 Q15.9219 48.6406 19.1953 45.4141 Q22.4688 42.1875 27.6875 42.1875 Q32.7656 42.1875 36.0156 45.3828 Q39.2656 48.5781 39.2656 53.2188 Q39.2656 58.0625 35.9141 61.3594 Q32.5625 64.6562 27.5938 64.6562 Q22.5625 64.6562 19.2422 61.4297 Q15.9219 58.2031 15.9219 53.7188 ZM13.0938 20.6562 Q13.0938 16.8906 14.875 13.375 Q16.6562 9.8594 20.1719 7.9297 Q23.6875 6 27.7344 6 Q34.0312 6 38.1328 10.0547 Q42.2344 14.1094 42.2344 20.3594 Q42.2344 26.7031 38.0156 30.8594 Q33.7969 35.0156 27.4375 35.0156 Q21.2344 35.0156 17.1641 30.9141 Q13.0938 26.8125 13.0938 20.6562 Z"/><glyph unicode="9" horiz-adv-x="55.615234" d="M5.4688 16.5469 L13.9219 17.3281 Q14.9844 11.375 18.0156 8.6875 Q21.0469 6 25.7812 6 Q29.8281 6 32.8828 7.8594 Q35.9375 9.7188 37.8906 12.8203 Q39.8438 15.9219 41.1641 21.1953 Q42.4844 26.4688 42.4844 31.9375 Q42.4844 32.5156 42.4375 33.6875 Q39.7969 29.5 35.2344 26.8828 Q30.6719 24.2656 25.3438 24.2656 Q16.4531 24.2656 10.3047 30.7109 Q4.1562 37.1562 4.1562 47.7031 Q4.1562 58.5938 10.5781 65.2344 Q17 71.875 26.6562 71.875 Q33.6406 71.875 39.4297 68.1172 Q45.2188 64.3594 48.2188 57.3984 Q51.2188 50.4375 51.2188 37.25 Q51.2188 23.5312 48.2422 15.4062 Q45.2656 7.2812 39.3828 3.0312 Q33.5 -1.2188 25.5938 -1.2188 Q17.1875 -1.2188 11.8672 3.4453 Q6.5469 8.1094 5.4688 16.5469 ZM41.4531 48.1406 Q41.4531 55.7188 37.4297 60.1562 Q33.4062 64.5938 27.7344 64.5938 Q21.875 64.5938 17.5312 59.8125 Q13.1875 55.0312 13.1875 47.4062 Q13.1875 40.5781 17.3125 36.3047 Q21.4375 32.0312 27.4844 32.0312 Q33.5938 32.0312 37.5234 36.3047 Q41.4531 40.5781 41.4531 48.1406 Z"/><glyph unicode="m" horiz-adv-x="83.30078" d="M6.5938 0 L6.5938 51.8594 L14.4531 51.8594 L14.4531 44.5781 Q16.8906 48.3906 20.9453 50.7109 Q25 53.0312 30.1719 53.0312 Q35.9375 53.0312 39.625 50.6406 Q43.3125 48.25 44.8281 43.9531 Q50.9844 53.0312 60.8438 53.0312 Q68.5625 53.0312 72.7109 48.7578 Q76.8594 44.4844 76.8594 35.5938 L76.8594 0 L68.1094 0 L68.1094 32.6719 Q68.1094 37.9375 67.2578 40.2578 Q66.4062 42.5781 64.1641 43.9922 Q61.9219 45.4062 58.8906 45.4062 Q53.4219 45.4062 49.8047 41.7734 Q46.1875 38.1406 46.1875 30.125 L46.1875 0 L37.4062 0 L37.4062 33.6875 Q37.4062 39.5469 35.2578 42.4766 Q33.1094 45.4062 28.2188 45.4062 Q24.5156 45.4062 21.3672 43.4531 Q18.2188 41.5 16.7969 37.7422 Q15.375 33.9844 15.375 26.9062 L15.375 0 L6.5938 0 Z"/><glyph unicode="B" horiz-adv-x="66.69922" d="M7.3281 0 L7.3281 71.5781 L34.1875 71.5781 Q42.3906 71.5781 47.3438 69.4062 Q52.2969 67.2344 55.1016 62.7188 Q57.9062 58.2031 57.9062 53.2656 Q57.9062 48.6875 55.4219 44.6328 Q52.9375 40.5781 47.9062 38.0938 Q54.3906 36.1875 57.8828 31.5938 Q61.375 27 61.375 20.75 Q61.375 15.7188 59.25 11.3984 Q57.125 7.0781 54 4.7344 Q50.875 2.3906 46.1641 1.1953 Q41.4531 0 34.625 0 L7.3281 0 ZM16.7969 41.5 L32.2812 41.5 Q38.5781 41.5 41.3125 42.3281 Q44.9219 43.4062 46.75 45.8984 Q48.5781 48.3906 48.5781 52.1562 Q48.5781 55.7188 46.875 58.4297 Q45.1719 61.1406 41.9922 62.1406 Q38.8125 63.1406 31.1094 63.1406 L16.7969 63.1406 L16.7969 41.5 ZM16.7969 8.4531 L34.625 8.4531 Q39.2031 8.4531 41.0625 8.7969 Q44.3438 9.375 46.5391 10.7422 Q48.7344 12.1094 50.1484 14.7188 Q51.5625 17.3281 51.5625 20.75 Q51.5625 24.75 49.5156 27.7109 Q47.4688 30.6719 43.8281 31.8672 Q40.1875 33.0625 33.3438 33.0625 L16.7969 33.0625 L16.7969 8.4531 Z"/><glyph unicode="d" horiz-adv-x="55.615234" d="M40.2344 0 L40.2344 6.5469 Q35.2969 -1.1719 25.7344 -1.1719 Q19.5312 -1.1719 14.3281 2.25 Q9.125 5.6719 6.2734 11.7969 Q3.4219 17.9219 3.4219 25.875 Q3.4219 33.6406 6.0078 39.9688 Q8.5938 46.2969 13.7734 49.6641 Q18.9531 53.0312 25.3438 53.0312 Q30.0312 53.0312 33.6953 51.0547 Q37.3594 49.0781 39.6562 45.9062 L39.6562 71.5781 L48.3906 71.5781 L48.3906 0 L40.2344 0 ZM12.4531 25.875 Q12.4531 15.9219 16.6484 10.9922 Q20.8438 6.0625 26.5625 6.0625 Q32.3281 6.0625 36.3516 10.7734 Q40.375 15.4844 40.375 25.1406 Q40.375 35.7969 36.2734 40.7734 Q32.1719 45.75 26.1719 45.75 Q20.3125 45.75 16.3828 40.9688 Q12.4531 36.1875 12.4531 25.875 Z"/><glyph unicode="w" horiz-adv-x="72.2168" d="M16.1562 0 L0.2969 51.8594 L9.375 51.8594 L17.625 21.9219 L20.7031 10.7969 Q20.9062 11.625 23.3906 21.4844 L31.6406 51.8594 L40.6719 51.8594 L48.4375 21.7812 L51.0312 11.8594 L54 21.875 L62.8906 51.8594 L71.4375 51.8594 L55.2188 0 L46.0938 0 L37.8438 31.0625 L35.8438 39.8906 L25.3438 0 L16.1562 0 Z"/><glyph unicode="o" horiz-adv-x="55.615234" d="M3.3281 25.9219 Q3.3281 40.3281 11.3281 47.2656 Q18.0156 53.0312 27.6406 53.0312 Q38.3281 53.0312 45.1172 46.0234 Q51.9062 39.0156 51.9062 26.6562 Q51.9062 16.6562 48.9062 10.9141 Q45.9062 5.1719 40.1641 2 Q34.4219 -1.1719 27.6406 -1.1719 Q16.75 -1.1719 10.0391 5.8125 Q3.3281 12.7969 3.3281 25.9219 ZM12.3594 25.9219 Q12.3594 15.9688 16.7031 11.0156 Q21.0469 6.0625 27.6406 6.0625 Q34.1875 6.0625 38.5312 11.0391 Q42.875 16.0156 42.875 26.2188 Q42.875 35.8438 38.5 40.7969 Q34.125 45.75 27.6406 45.75 Q21.0469 45.75 16.7031 40.8203 Q12.3594 35.8906 12.3594 25.9219 Z"/><glyph unicode="P" horiz-adv-x="66.69922" d="M7.7188 0 L7.7188 71.5781 L34.7188 71.5781 Q41.8438 71.5781 45.6094 70.9062 Q50.875 70.0156 54.4453 67.5547 Q58.0156 65.0938 60.1875 60.6484 Q62.3594 56.2031 62.3594 50.875 Q62.3594 41.75 56.5469 35.4297 Q50.7344 29.1094 35.5469 29.1094 L17.1875 29.1094 L17.1875 0 L7.7188 0 ZM17.1875 37.5469 L35.6875 37.5469 Q44.875 37.5469 48.7344 40.9688 Q52.5938 44.3906 52.5938 50.5938 Q52.5938 55.0781 50.3203 58.2734 Q48.0469 61.4688 44.3438 62.5 Q41.9375 63.1406 35.5 63.1406 L17.1875 63.1406 L17.1875 37.5469 Z"/></font><font horiz-adv-x="75.0" id="font2"><font-face ascent="100.53711" descent="21.972656" units-per-em="100" style="font-style:normal; font-family:SansSerif; font-weight:bold;"/><missing-glyph horiz-adv-x="75.0" d="M12.5 0 L12.5 62.5 L62.5 62.5 L62.5 0 L12.5 0 ZM14.0625 1.5625 L60.9375 1.5625 L60.9375 60.9375 L14.0625 60.9375 L14.0625 1.5625 Z"/><glyph unicode="4" horiz-adv-x="55.615234" d="M31.1562 0 L31.1562 14.4062 L1.8594 14.4062 L1.8594 26.4219 L32.9062 71.875 L44.4375 71.875 L44.4375 26.4688 L53.3281 26.4688 L53.3281 14.4062 L44.4375 14.4062 L44.4375 0 L31.1562 0 ZM31.1562 26.4688 L31.1562 50.9219 L14.7031 26.4688 L31.1562 26.4688 Z"/><glyph unicode="6" horiz-adv-x="55.615234" d="M50.7344 54.0469 L37.4531 52.5938 Q36.9688 56.6875 34.9141 58.6406 Q32.8594 60.5938 29.5938 60.5938 Q25.25 60.5938 22.2422 56.6875 Q19.2344 52.7812 18.4531 40.4375 Q23.5781 46.4844 31.2031 46.4844 Q39.7969 46.4844 45.9219 39.9453 Q52.0469 33.4062 52.0469 23.0469 Q52.0469 12.0625 45.6016 5.4219 Q39.1562 -1.2188 29.0469 -1.2188 Q18.2188 -1.2188 11.2344 7.2031 Q4.25 15.625 4.25 34.8125 Q4.25 54.5 11.5234 63.1875 Q18.7969 71.875 30.4219 71.875 Q38.5781 71.875 43.9219 67.3125 Q49.2656 62.75 50.7344 54.0469 ZM19.625 24.125 Q19.625 17.4375 22.7031 13.7969 Q25.7812 10.1562 29.7344 10.1562 Q33.5469 10.1562 36.0859 13.1328 Q38.625 16.1094 38.625 22.9062 Q38.625 29.8906 35.8906 33.1328 Q33.1562 36.375 29.0469 36.375 Q25.0938 36.375 22.3594 33.2734 Q19.625 30.1719 19.625 24.125 Z"/><glyph unicode="M" horiz-adv-x="83.30078" d="M7.0781 0 L7.0781 71.5781 L28.7188 71.5781 L41.7031 22.75 L54.5469 71.5781 L76.2188 71.5781 L76.2188 0 L62.7969 0 L62.7969 56.3438 L48.5781 0 L34.6719 0 L20.5156 56.3438 L20.5156 0 L7.0781 0 Z"/><glyph unicode="A" horiz-adv-x="72.2168" d="M71.8281 0 L56.1094 0 L49.8594 16.2656 L21.2344 16.2656 L15.3281 0 L0 0 L27.875 71.5781 L43.1719 71.5781 L71.8281 0 ZM45.2188 28.3281 L35.3594 54.8906 L25.6875 28.3281 L45.2188 28.3281 Z"/><glyph unicode="Q" horiz-adv-x="77.7832" d="M64.8906 9.0781 Q70.2188 5.2812 76.4688 3.0312 L71.1406 -7.1719 Q67.875 -6.2031 64.75 -4.5 Q64.0625 -4.1562 55.125 1.8594 Q48.0938 -1.2188 39.5469 -1.2188 Q23.0469 -1.2188 13.6953 8.5 Q4.3438 18.2188 4.3438 35.7969 Q4.3438 53.3281 13.7188 63.0625 Q23.0938 72.7969 39.1562 72.7969 Q55.0781 72.7969 64.4062 63.0625 Q73.7344 53.3281 73.7344 35.7969 Q73.7344 26.5156 71.1406 19.4844 Q69.1875 14.1094 64.8906 9.0781 ZM53.2656 17.2344 Q56.0625 20.5156 57.4531 25.1484 Q58.8438 29.7812 58.8438 35.7969 Q58.8438 48.1875 53.375 54.3203 Q47.9062 60.4531 39.0625 60.4531 Q30.2188 60.4531 24.7266 54.2969 Q19.2344 48.1406 19.2344 35.7969 Q19.2344 23.25 24.7266 17.0234 Q30.2188 10.7969 38.625 10.7969 Q41.75 10.7969 44.5312 11.8125 Q40.1406 14.7031 35.5938 16.3125 L39.6562 24.5625 Q46.7812 22.125 53.2656 17.2344 Z"/><glyph unicode="0" horiz-adv-x="55.615234" d="M27.4375 71.875 Q37.8438 71.875 43.7031 64.4531 Q50.6875 55.6719 50.6875 35.2969 Q50.6875 14.9844 43.6562 6.1094 Q37.8438 -1.2188 27.4375 -1.2188 Q17 -1.2188 10.6016 6.8125 Q4.2031 14.8438 4.2031 35.4531 Q4.2031 55.6719 11.2344 64.5469 Q17.0469 71.875 27.4375 71.875 ZM27.4375 60.5 Q24.9531 60.5 23 58.9141 Q21.0469 57.3281 19.9688 53.2188 Q18.5625 47.9062 18.5625 35.2969 Q18.5625 22.7031 19.8281 17.9922 Q21.0938 13.2812 23.0234 11.7188 Q24.9531 10.1562 27.4375 10.1562 Q29.9375 10.1562 31.8906 11.7422 Q33.8438 13.3281 34.9062 17.4375 Q36.3281 22.7031 36.3281 35.2969 Q36.3281 47.9062 35.0625 52.6172 Q33.7969 57.3281 31.8672 58.9141 Q29.9375 60.5 27.4375 60.5 Z"/><glyph unicode="1" horiz-adv-x="55.615234" d="M39.3594 0 L25.6406 0 L25.6406 51.7031 Q18.1094 44.6719 7.9062 41.3125 L7.9062 53.7656 Q13.2812 55.5156 19.5781 60.4219 Q25.875 65.3281 28.2188 71.875 L39.3594 71.875 L39.3594 0 Z"/><glyph unicode="-" horiz-adv-x="33.30078" d="M5.6094 19.0938 L5.6094 32.8125 L32.5625 32.8125 L32.5625 19.0938 L5.6094 19.0938 Z"/><glyph unicode="E" horiz-adv-x="66.69922" d="M7.2812 0 L7.2812 71.5781 L60.3594 71.5781 L60.3594 59.4688 L21.7344 59.4688 L21.7344 43.6094 L57.6719 43.6094 L57.6719 31.5469 L21.7344 31.5469 L21.7344 12.0625 L61.7188 12.0625 L61.7188 0 L7.2812 0 Z"/><glyph unicode="T" horiz-adv-x="61.083984" d="M23.3906 0 L23.3906 59.4688 L2.1562 59.4688 L2.1562 71.5781 L59.0312 71.5781 L59.0312 59.4688 L37.8438 59.4688 L37.8438 0 L23.3906 0 Z"/><glyph unicode="L" horiz-adv-x="61.083984" d="M7.6719 0 L7.6719 71 L22.125 71 L22.125 12.0625 L58.0625 12.0625 L58.0625 0 L7.6719 0 Z"/><glyph unicode="f" horiz-adv-x="33.30078" d="M1.1719 51.8594 L8.7969 51.8594 L8.7969 55.7656 Q8.7969 62.3125 10.1875 65.5312 Q11.5781 68.75 15.3125 70.7734 Q19.0469 72.7969 24.75 72.7969 Q30.6094 72.7969 36.2344 71.0469 L34.375 61.4688 Q31.1094 62.25 28.0781 62.25 Q25.0938 62.25 23.8047 60.8594 Q22.5156 59.4688 22.5156 55.5156 L22.5156 51.8594 L32.7656 51.8594 L32.7656 41.0625 L22.5156 41.0625 L22.5156 0 L8.7969 0 L8.7969 41.0625 L1.1719 41.0625 L1.1719 51.8594 Z"/><glyph unicode="y" horiz-adv-x="55.615234" d="M0.6875 51.8594 L15.2812 51.8594 L27.6875 15.0469 L39.7969 51.8594 L54 51.8594 L35.6875 1.9531 L32.4219 -7.0781 Q30.6094 -11.625 28.9766 -14.0156 Q27.3438 -16.4062 25.2188 -17.8984 Q23.0938 -19.3906 19.9922 -20.2188 Q16.8906 -21.0469 12.9844 -21.0469 Q9.0312 -21.0469 5.2188 -20.2188 L4 -9.4688 Q7.2344 -10.1094 9.8125 -10.1094 Q14.5938 -10.1094 16.8906 -7.3047 Q19.1875 -4.5 20.4062 -0.1406 L0.6875 51.8594 Z"/><glyph unicode="c" horiz-adv-x="55.615234" d="M52.3906 36.5312 L38.875 34.0781 Q38.1875 38.1406 35.7656 40.1875 Q33.3438 42.2344 29.5 42.2344 Q24.3594 42.2344 21.3125 38.6953 Q18.2656 35.1562 18.2656 26.8594 Q18.2656 17.625 21.3672 13.8203 Q24.4688 10.0156 29.6875 10.0156 Q33.5938 10.0156 36.0859 12.2344 Q38.5781 14.4531 39.5938 19.875 L53.0781 17.5781 Q50.9844 8.2969 45.0234 3.5625 Q39.0625 -1.1719 29.0469 -1.1719 Q17.6719 -1.1719 10.9141 6.0078 Q4.1562 13.1875 4.1562 25.875 Q4.1562 38.7188 10.9375 45.875 Q17.7188 53.0312 29.2969 53.0312 Q38.7656 53.0312 44.3594 48.9531 Q49.9531 44.875 52.3906 36.5312 Z"/><glyph unicode="n" horiz-adv-x="61.083984" d="M54.3438 0 L40.625 0 L40.625 26.4688 Q40.625 34.8594 39.75 37.3281 Q38.875 39.7969 36.8906 41.1641 Q34.9062 42.5312 32.125 42.5312 Q28.5625 42.5312 25.7344 40.5781 Q22.9062 38.625 21.8516 35.3984 Q20.7969 32.1719 20.7969 23.4844 L20.7969 0 L7.0781 0 L7.0781 51.8594 L19.8281 51.8594 L19.8281 44.2344 Q26.6094 53.0312 36.9219 53.0312 Q41.4531 53.0312 45.2109 51.3906 Q48.9688 49.75 50.8984 47.2109 Q52.8281 44.6719 53.5859 41.4531 Q54.3438 38.2344 54.3438 32.2344 L54.3438 0 Z"/><glyph unicode="u" horiz-adv-x="61.083984" d="M41.3125 0 L41.3125 7.7656 Q38.4844 3.6094 33.8672 1.2188 Q29.25 -1.1719 24.125 -1.1719 Q18.8906 -1.1719 14.7422 1.125 Q10.5938 3.4219 8.7422 7.5703 Q6.8906 11.7188 6.8906 19.0469 L6.8906 51.8594 L20.6094 51.8594 L20.6094 28.0312 Q20.6094 17.0938 21.3672 14.625 Q22.125 12.1562 24.125 10.7188 Q26.125 9.2812 29.2031 9.2812 Q32.7188 9.2812 35.5 11.2109 Q38.2812 13.1406 39.3047 15.9922 Q40.3281 18.8438 40.3281 29.9844 L40.3281 51.8594 L54.0469 51.8594 L54.0469 0 L41.3125 0 Z"/><glyph unicode="q" horiz-adv-x="61.083984" d="M41.0625 -19.7344 L41.0625 6.3438 Q38.375 2.875 34.375 0.8516 Q30.375 -1.1719 25.7344 -1.1719 Q16.8906 -1.1719 11.1875 5.4688 Q4.4375 13.2344 4.4375 26.5156 Q4.4375 39.0156 10.7656 46.0234 Q17.0938 53.0312 26.4688 53.0312 Q31.6406 53.0312 35.4219 50.8359 Q39.2031 48.6406 42.1406 44.1875 L42.1406 51.8594 L54.7812 51.8594 L54.7812 -19.7344 L41.0625 -19.7344 ZM41.5 26.5625 Q41.5 34.5156 38.2578 38.3984 Q35.0156 42.2812 30.125 42.2812 Q25.1406 42.2812 21.7969 38.3281 Q18.4531 34.375 18.4531 25.7812 Q18.4531 17.2344 21.6797 13.4531 Q24.9062 9.6719 29.6406 9.6719 Q34.375 9.6719 37.9375 13.9219 Q41.5 18.1719 41.5 26.5625 Z"/><glyph unicode="F" horiz-adv-x="61.083984" d="M7.375 0 L7.375 71.5781 L56.4531 71.5781 L56.4531 59.4688 L21.8281 59.4688 L21.8281 42.5312 L51.7031 42.5312 L51.7031 30.4219 L21.8281 30.4219 L21.8281 0 L7.375 0 Z"/><glyph unicode="s" horiz-adv-x="55.615234" d="M2.3438 14.7969 L16.1094 16.8906 Q17 12.8906 19.6797 10.8125 Q22.3594 8.7344 27.2031 8.7344 Q32.5156 8.7344 35.2031 10.6875 Q37.0156 12.0625 37.0156 14.3594 Q37.0156 15.9219 36.0312 16.9375 Q35.0156 17.9219 31.4531 18.75 Q14.8438 22.4062 10.4062 25.4375 Q4.25 29.6406 4.25 37.1094 Q4.25 43.8438 9.5703 48.4375 Q14.8906 53.0312 26.0781 53.0312 Q36.7188 53.0312 41.8984 49.5625 Q47.0781 46.0938 49.0312 39.3125 L36.0781 36.9219 Q35.25 39.9375 32.9297 41.5547 Q30.6094 43.1719 26.3125 43.1719 Q20.9062 43.1719 18.5625 41.6562 Q17 40.5781 17 38.875 Q17 37.4062 18.3594 36.375 Q20.2188 35.0156 31.1797 32.5234 Q42.1406 30.0312 46.4844 26.4219 Q50.7812 22.75 50.7812 16.2188 Q50.7812 9.0781 44.8281 3.9531 Q38.875 -1.1719 27.2031 -1.1719 Q16.6094 -1.1719 10.4297 3.125 Q4.25 7.4219 2.3438 14.7969 Z"/><glyph unicode="v" horiz-adv-x="55.615234" d="M21.4375 0 L0.5312 51.8594 L14.9375 51.8594 L24.7031 25.3906 L27.5469 16.5469 Q28.6562 19.9219 28.9531 21 Q29.6406 23.1875 30.4219 25.3906 L40.2812 51.8594 L54.3906 51.8594 L33.7969 0 L21.4375 0 Z"/><glyph unicode=" " horiz-adv-x="27.783203" d=""/><glyph unicode="r" horiz-adv-x="38.916016" d="M20.3125 0 L6.5938 0 L6.5938 51.8594 L19.3438 51.8594 L19.3438 44.4844 Q22.6094 49.7031 25.2188 51.3672 Q27.8281 53.0312 31.1562 53.0312 Q35.8438 53.0312 40.1875 50.4375 L35.9375 38.4844 Q32.4688 40.7188 29.5 40.7188 Q26.6094 40.7188 24.6094 39.1328 Q22.6094 37.5469 21.4609 33.3984 Q20.3125 29.25 20.3125 16.0156 L20.3125 0 Z"/><glyph unicode="e" horiz-adv-x="55.615234" d="M37.2031 16.5 L50.875 14.2031 Q48.25 6.6875 42.5547 2.7578 Q36.8594 -1.1719 28.3281 -1.1719 Q14.7969 -1.1719 8.2969 7.6719 Q3.1719 14.75 3.1719 25.5312 Q3.1719 38.4219 9.9141 45.7266 Q16.6562 53.0312 26.9531 53.0312 Q38.5312 53.0312 45.2188 45.3906 Q51.9062 37.75 51.6094 21.9688 L17.2344 21.9688 Q17.3906 15.875 20.5625 12.4766 Q23.7344 9.0781 28.4688 9.0781 Q31.6875 9.0781 33.8828 10.8359 Q36.0781 12.5938 37.2031 16.5 ZM37.9844 30.375 Q37.8438 36.3281 34.9141 39.4297 Q31.9844 42.5312 27.7812 42.5312 Q23.2969 42.5312 20.3594 39.2656 Q17.4375 35.9844 17.4844 30.375 L37.9844 30.375 Z"/><glyph unicode="w" horiz-adv-x="77.7832" d="M16.8438 0 L0.4375 51.8594 L13.7656 51.8594 L23.4844 17.875 L32.4219 51.8594 L45.6562 51.8594 L54.2969 17.875 L64.2031 51.8594 L77.7344 51.8594 L61.0781 0 L47.9062 0 L38.9688 33.3438 L30.1719 0 L16.8438 0 Z"/><glyph unicode="o" horiz-adv-x="61.083984" d="M4 26.6562 Q4 33.5 7.375 39.8984 Q10.75 46.2969 16.9219 49.6641 Q23.0938 53.0312 30.7188 53.0312 Q42.4844 53.0312 50 45.3906 Q57.5156 37.75 57.5156 26.0781 Q57.5156 14.3125 49.9219 6.5703 Q42.3281 -1.1719 30.8125 -1.1719 Q23.6875 -1.1719 17.2188 2.0547 Q10.75 5.2812 7.375 11.5 Q4 17.7188 4 26.6562 ZM18.0625 25.9219 Q18.0625 18.2188 21.7266 14.1172 Q25.3906 10.0156 30.7656 10.0156 Q36.1406 10.0156 39.7734 14.1172 Q43.4062 18.2188 43.4062 26.0312 Q43.4062 33.6406 39.7734 37.7422 Q36.1406 41.8438 30.7656 41.8438 Q25.3906 41.8438 21.7266 37.7422 Q18.0625 33.6406 18.0625 25.9219 Z"/><glyph unicode="P" horiz-adv-x="66.69922" d="M7.2812 0 L7.2812 71.5781 L30.4688 71.5781 Q43.6562 71.5781 47.6562 70.5156 Q53.8125 68.8906 57.9609 63.5 Q62.1094 58.1094 62.1094 49.5625 Q62.1094 42.9688 59.7188 38.4766 Q57.3281 33.9844 53.6406 31.4219 Q49.9531 28.8594 46.1406 28.0312 Q40.9688 27 31.1562 27 L21.7344 27 L21.7344 0 L7.2812 0 ZM21.7344 59.4688 L21.7344 39.1562 L29.6406 39.1562 Q38.1875 39.1562 41.0703 40.2812 Q43.9531 41.4062 45.5859 43.7969 Q47.2188 46.1875 47.2188 49.3594 Q47.2188 53.2656 44.9219 55.8047 Q42.625 58.3438 39.1094 58.9844 Q36.5312 59.4688 28.7188 59.4688 L21.7344 59.4688 Z"/><glyph unicode="X" horiz-adv-x="66.69922" d="M0 0 L24.4688 37.3594 L2.2969 71.5781 L19.1875 71.5781 L33.5469 48.5781 L47.6094 71.5781 L64.3594 71.5781 L42.0938 36.8125 L66.5469 0 L49.125 0 L33.25 24.75 L17.3281 0 L0 0 Z"/><glyph unicode="t" horiz-adv-x="33.30078" d="M30.9531 51.8594 L30.9531 40.9219 L21.5781 40.9219 L21.5781 20.0156 Q21.5781 13.6719 21.8516 12.625 Q22.125 11.5781 23.0781 10.8906 Q24.0312 10.2031 25.3906 10.2031 Q27.2969 10.2031 30.9062 11.5312 L32.0781 0.875 Q27.2969 -1.1719 21.2344 -1.1719 Q17.5312 -1.1719 14.5547 0.0703 Q11.5781 1.3125 10.1875 3.2969 Q8.7969 5.2812 8.25 8.6406 Q7.8125 11.0312 7.8125 18.3125 L7.8125 40.9219 L1.5156 40.9219 L1.5156 51.8594 L7.8125 51.8594 L7.8125 62.1562 L21.5781 70.1719 L21.5781 51.8594 L30.9531 51.8594 Z"/><glyph unicode="h" horiz-adv-x="61.083984" d="M20.8438 71.5781 L20.8438 45.2656 Q27.4844 53.0312 36.7188 53.0312 Q41.4531 53.0312 45.2656 51.2734 Q49.0781 49.5156 51.0078 46.7812 Q52.9375 44.0469 53.6406 40.7266 Q54.3438 37.4062 54.3438 30.4219 L54.3438 0 L40.625 0 L40.625 27.3906 Q40.625 35.5469 39.8438 37.7422 Q39.0625 39.9375 37.0859 41.2344 Q35.1094 42.5312 32.125 42.5312 Q28.7188 42.5312 26.0312 40.8672 Q23.3438 39.2031 22.0938 35.8594 Q20.8438 32.5156 20.8438 25.9844 L20.8438 0 L7.125 0 L7.125 71.5781 L20.8438 71.5781 Z"/><glyph unicode="g" horiz-adv-x="61.083984" d="M5.9062 -3.4219 L21.5781 -5.3281 Q21.9688 -8.0625 23.3906 -9.0781 Q25.3438 -10.5469 29.5469 -10.5469 Q34.9062 -10.5469 37.5938 -8.9375 Q39.4062 -7.8594 40.3281 -5.4688 Q40.9688 -3.7656 40.9688 0.8281 L40.9688 8.4062 Q34.8125 0 25.4375 0 Q14.9844 0 8.8906 8.8438 Q4.1094 15.8281 4.1094 26.2188 Q4.1094 39.2656 10.3828 46.1484 Q16.6562 53.0312 25.9844 53.0312 Q35.5938 53.0312 41.8438 44.5781 L41.8438 51.8594 L54.6875 51.8594 L54.6875 5.3281 Q54.6875 -3.8594 53.1719 -8.3984 Q51.6562 -12.9375 48.9219 -15.5234 Q46.1875 -18.1094 41.625 -19.5781 Q37.0625 -21.0469 30.0781 -21.0469 Q16.8906 -21.0469 11.375 -16.5312 Q5.8594 -12.0156 5.8594 -5.0781 Q5.8594 -4.3906 5.9062 -3.4219 ZM18.1719 27 Q18.1719 18.75 21.3672 14.9141 Q24.5625 11.0781 29.25 11.0781 Q34.2812 11.0781 37.75 15.0156 Q41.2188 18.9531 41.2188 26.6562 Q41.2188 34.7188 37.8984 38.625 Q34.5781 42.5312 29.5 42.5312 Q24.5625 42.5312 21.3672 38.6953 Q18.1719 34.8594 18.1719 27 Z"/><glyph unicode="i" horiz-adv-x="27.783203" d="M7.1719 58.8906 L7.1719 71.5781 L20.9062 71.5781 L20.9062 58.8906 L7.1719 58.8906 ZM7.1719 0 L7.1719 51.8594 L20.9062 51.8594 L20.9062 0 L7.1719 0 Z"/><glyph unicode="K" horiz-adv-x="72.2168" d="M7.4688 0 L7.4688 71.5781 L21.9219 71.5781 L21.9219 39.7969 L51.125 71.5781 L70.5625 71.5781 L43.6094 43.7031 L72.0156 0 L53.3281 0 L33.6406 33.5938 L21.9219 21.625 L21.9219 0 L7.4688 0 Z"/><glyph unicode="R" horiz-adv-x="72.2168" d="M7.3281 0 L7.3281 71.5781 L37.75 71.5781 Q49.2188 71.5781 54.4219 69.6484 Q59.625 67.7188 62.75 62.7891 Q65.875 57.8594 65.875 51.5156 Q65.875 43.4531 61.1328 38.2031 Q56.3906 32.9531 46.9688 31.5938 Q51.6562 28.8594 54.7109 25.5859 Q57.7656 22.3125 62.9375 13.9688 L71.6875 0 L54.3906 0 L43.9531 15.5781 Q38.375 23.9219 36.3281 26.0938 Q34.2812 28.2656 31.9844 29.0781 Q29.6875 29.8906 24.7031 29.8906 L21.7812 29.8906 L21.7812 0 L7.3281 0 ZM21.7812 41.3125 L32.4688 41.3125 Q42.875 41.3125 45.4609 42.1875 Q48.0469 43.0625 49.5156 45.2109 Q50.9844 47.3594 50.9844 50.5938 Q50.9844 54.2031 49.0547 56.4219 Q47.125 58.6406 43.6094 59.2344 Q41.8438 59.4688 33.0625 59.4688 L21.7812 59.4688 L21.7812 41.3125 Z"/><glyph unicode=";" horiz-adv-x="33.30078" d="M9.4219 38.1406 L9.4219 51.8594 L23.1406 51.8594 L23.1406 38.1406 L9.4219 38.1406 ZM9.4219 13.7188 L23.1406 13.7188 L23.1406 3.9062 Q23.1406 -2.0469 22.1172 -5.4922 Q21.0938 -8.9375 18.2344 -11.6719 Q15.375 -14.4062 10.9844 -15.9688 L8.2969 -10.2969 Q12.4531 -8.9375 14.2109 -6.4922 Q15.9688 -4.0469 16.0625 0 L9.4219 0 L9.4219 13.7188 Z"/><glyph unicode="O" horiz-adv-x="77.7832" d="M4.3438 35.3594 Q4.3438 46.2969 7.625 53.7188 Q10.0625 59.1875 14.2812 63.5312 Q18.5 67.875 23.5312 69.9688 Q30.2188 72.7969 38.9688 72.7969 Q54.7812 72.7969 64.2812 62.9844 Q73.7812 53.1719 73.7812 35.6875 Q73.7812 18.3594 64.3594 8.5703 Q54.9375 -1.2188 39.1562 -1.2188 Q23.1875 -1.2188 13.7656 8.5234 Q4.3438 18.2656 4.3438 35.3594 ZM19.2344 35.8438 Q19.2344 23.6875 24.8516 17.4141 Q30.4688 11.1406 39.1094 11.1406 Q47.75 11.1406 53.2969 17.3594 Q58.8438 23.5781 58.8438 36.0312 Q58.8438 48.3438 53.4453 54.3984 Q48.0469 60.4531 39.1094 60.4531 Q30.1719 60.4531 24.7031 54.3203 Q19.2344 48.1875 19.2344 35.8438 Z"/><glyph unicode="U" horiz-adv-x="72.2168" d="M7.1719 71.5781 L21.625 71.5781 L21.625 32.8125 Q21.625 23.5781 22.1719 20.8438 Q23.0938 16.4531 26.5859 13.7969 Q30.0781 11.1406 36.1406 11.1406 Q42.2812 11.1406 45.4062 13.6484 Q48.5312 16.1562 49.1719 19.8203 Q49.8125 23.4844 49.8125 31.9844 L49.8125 71.5781 L64.2656 71.5781 L64.2656 33.9844 Q64.2656 21.0938 63.0938 15.7734 Q61.9219 10.4531 58.7656 6.7891 Q55.6094 3.125 50.3359 0.9531 Q45.0625 -1.2188 36.5781 -1.2188 Q26.3125 -1.2188 21.0156 1.1484 Q15.7188 3.5156 12.6484 7.2969 Q9.5781 11.0781 8.5938 15.2344 Q7.1719 21.3906 7.1719 33.4062 L7.1719 71.5781 Z"/><glyph unicode="D" horiz-adv-x="72.2168" d="M7.2344 71.5781 L33.6406 71.5781 Q42.5781 71.5781 47.2656 70.2188 Q53.5625 68.3594 58.0547 63.625 Q62.5469 58.8906 64.8906 52.0312 Q67.2344 45.1719 67.2344 35.1094 Q67.2344 26.2656 65.0469 19.875 Q62.3594 12.0625 57.375 7.2344 Q53.6094 3.5625 47.2188 1.5156 Q42.4375 0 34.4219 0 L7.2344 0 L7.2344 71.5781 ZM21.6875 59.4688 L21.6875 12.0625 L32.4688 12.0625 Q38.5312 12.0625 41.2188 12.75 Q44.7344 13.625 47.0469 15.7266 Q49.3594 17.8281 50.8281 22.6328 Q52.2969 27.4375 52.2969 35.75 Q52.2969 44.0469 50.8281 48.4922 Q49.3594 52.9375 46.7266 55.4219 Q44.0938 57.9062 40.0469 58.7969 Q37.0156 59.4688 28.1719 59.4688 L21.6875 59.4688 Z"/><glyph unicode="=" horiz-adv-x="58.398438" d="M4.1562 39.8438 L4.1562 52.4375 L54.2031 52.4375 L54.2031 39.8438 L4.1562 39.8438 ZM4.1562 18.1719 L4.1562 30.8125 L54.2031 30.8125 L54.2031 18.1719 L4.1562 18.1719 Z"/><glyph unicode="x" horiz-adv-x="55.615234" d="M0.5938 0 L19.2812 26.7031 L1.375 51.8594 L18.1094 51.8594 L27.2969 37.5938 L36.9688 51.8594 L53.0781 51.8594 L35.5 27.2969 L54.6875 0 L37.8438 0 L27.2969 16.0625 L16.6562 0 L0.5938 0 Z"/></font></defs><g style="fill:white; stroke:white;"><rect x="0" y="0" width="732" style="clip-path:url(#clipPath1); stroke:none;" height="569"/></g><g style="fill:white; text-rendering:optimizeSpeed; color-rendering:optimizeSpeed; image-rendering:optimizeSpeed; shape-rendering:crispEdges; color-interpolation:sRGB; stroke:white;"><rect x="0" width="732" height="569" y="0" style="stroke:none;"/><path style="stroke:none;" d="M95 506 L662 506 L662 43 L95 43 Z"/></g><g style="fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(38,38,38); stroke-width:0.6667;"><line y2="506" style="fill:none;" x1="95" x2="662" y1="506"/><line y2="43" style="fill:none;" x1="95" x2="662" y1="43"/><line y2="500.33" style="fill:none;" x1="95" x2="95" y1="506"/><line y2="500.33" style="fill:none;" x1="189.5" x2="189.5" y1="506"/><line y2="500.33" style="fill:none;" x1="284" x2="284" y1="506"/><line y2="500.33" style="fill:none;" x1="378.5" x2="378.5" y1="506"/><line y2="500.33" style="fill:none;" x1="473" x2="473" y1="506"/><line y2="500.33" style="fill:none;" x1="567.5" x2="567.5" y1="506"/><line y2="500.33" style="fill:none;" x1="662" x2="662" y1="506"/><line y2="48.67" style="fill:none;" x1="95" x2="95" y1="43"/><line y2="48.67" style="fill:none;" x1="189.5" x2="189.5" y1="43"/><line y2="48.67" style="fill:none;" x1="284" x2="284" y1="43"/><line y2="48.67" style="fill:none;" x1="378.5" x2="378.5" y1="43"/><line y2="48.67" style="fill:none;" x1="473" x2="473" y1="43"/><line y2="48.67" style="fill:none;" x1="567.5" x2="567.5" y1="43"/><line y2="48.67" style="fill:none;" x1="662" x2="662" y1="43"/></g><g transform="translate(95,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">0</text></g><g transform="translate(189.5,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">1</text></g><g transform="translate(284,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">2</text></g><g transform="translate(378.5,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">3</text></g><g transform="translate(473,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">4</text></g><g transform="translate(567.5,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">5</text></g><g transform="translate(662,511.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">6</text></g><g transform="translate(378.5003,529.6667)" style="font-size:15px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-58" xml:space="preserve" y="16" style="stroke:none;">Frequency (GHz)</text></g><g style="fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(38,38,38); stroke-width:0.6667;"><line y2="43" style="fill:none;" x1="95" x2="95" y1="506"/><line y2="43" style="fill:none;" x1="662" x2="662" y1="506"/><line y2="506" style="fill:none;" x1="95" x2="100.67" y1="506"/><line y2="454.5555" style="fill:none;" x1="95" x2="100.67" y1="454.5555"/><line y2="403.1111" style="fill:none;" x1="95" x2="100.67" y1="403.1111"/><line y2="351.6667" style="fill:none;" x1="95" x2="100.67" y1="351.6667"/><line y2="300.2222" style="fill:none;" x1="95" x2="100.67" y1="300.2222"/><line y2="248.7778" style="fill:none;" x1="95" x2="100.67" y1="248.7778"/><line y2="197.3333" style="fill:none;" x1="95" x2="100.67" y1="197.3333"/><line y2="145.8889" style="fill:none;" x1="95" x2="100.67" y1="145.8889"/><line y2="94.4444" style="fill:none;" x1="95" x2="100.67" y1="94.4444"/><line y2="43" style="fill:none;" x1="95" x2="100.67" y1="43"/><line y2="506" style="fill:none;" x1="662" x2="656.33" y1="506"/><line y2="454.5555" style="fill:none;" x1="662" x2="656.33" y1="454.5555"/><line y2="403.1111" style="fill:none;" x1="662" x2="656.33" y1="403.1111"/><line y2="351.6667" style="fill:none;" x1="662" x2="656.33" y1="351.6667"/><line y2="300.2222" style="fill:none;" x1="662" x2="656.33" y1="300.2222"/><line y2="248.7778" style="fill:none;" x1="662" x2="656.33" y1="248.7778"/><line y2="197.3333" style="fill:none;" x1="662" x2="656.33" y1="197.3333"/><line y2="145.8889" style="fill:none;" x1="662" x2="656.33" y1="145.8889"/><line y2="94.4444" style="fill:none;" x1="662" x2="656.33" y1="94.4444"/><line y2="43" style="fill:none;" x1="662" x2="656.33" y1="43"/></g><g transform="translate(89.6667,506)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">2</text></g><g transform="translate(89.6667,454.5555)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">3</text></g><g transform="translate(89.6667,403.1111)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">4</text></g><g transform="translate(89.6667,351.6667)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">5</text></g><g transform="translate(89.6667,300.2222)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">6</text></g><g transform="translate(89.6667,248.7778)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">7</text></g><g transform="translate(89.6667,197.3333)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">8</text></g><g transform="translate(89.6667,145.8889)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-8" xml:space="preserve" y="5.5" style="stroke:none;">9</text></g><g transform="translate(89.6667,94.4444)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-15" xml:space="preserve" y="5.5" style="stroke:none;">10</text></g><g transform="translate(89.6667,43)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-15" xml:space="preserve" y="5.5" style="stroke:none;">11</text></g><g transform="translate(70.6667,274.4998) rotate(-90)" style="font-size:15px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-44" xml:space="preserve" y="-4" style="stroke:none;">Power (dBm)</text></g><g transform="translate(378.5004,40.244)" style="font-size:15px; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; font-weight:bold;"><text x="-143" xml:space="preserve" y="-24" style="stroke:none;">Power vs Frequency for LTE-10 QAM-64</text><text x="-138" xml:space="preserve" y="-4" style="stroke:none;">Tx=ADALM-PLUTO ; Rx=Keysight PXA</text></g><g style="stroke-linecap:butt; fill:rgb(0,114,189); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(0,114,189); stroke-width:0.6667;"><path d="M101.7095 469.0493 L102.6545 416.0925 L103.5995 375.8235 L104.5445 340.4082 L105.4895 307.3824 L106.4345 280.6961 L107.3795 263.2359 L108.3245 249.1729 L109.2695 232.657 L110.2145 214.1068 L111.1595 200.334 L112.1045 191.3787 L113.0495 184.3916 L113.9945 172.9592 L114.9395 160.8348 L115.8845 154.0357 L116.8295 151.2777 L117.7745 148.6163 L118.7195 142.9841 L119.6645 136.3609 L120.6095 132.5713 L121.5545 131.783 L122.4995 129.8379 L123.4445 125.0645 L124.3895 120.4582 L125.3345 117.7782 L126.2795 118.5236 L127.2245 118.4189 L128.1695 115.9439 L129.1145 113.9053 L130.0595 114.2691 L131.0045 114.6722 L131.9495 112.9236 L132.8945 109.9269 L133.8395 106.556 L134.7845 105.6447 L135.7295 104.4467 L136.6745 101.6017 L137.6195 97.7595 L138.5645 93.6579 L139.5095 90.5137 L140.4545 87.9542 L141.3995 84.7378 L142.3445 82.1843 L143.2895 79.5588 L144.2345 80.1851 L145.1795 81.6049 L146.1245 82.4308 L147.0695 81.4617 L148.0145 79.1872 L148.9595 79.2248 L149.9045 81.7277 L150.8495 84.819 L151.7945 83.7544 L152.7395 81.3257 L153.6845 80.0119 L154.6295 79.7983 L155.5745 80.0285 L156.5195 78.6323 L157.4645 76.9357 L158.4095 76.8031 L159.3545 78.3002 L160.2995 79.6664 L161.2445 80.0702 L162.1895 77.7219 L163.1345 76.7042 L164.0795 76.8271 L165.0245 75.9572 L165.9695 75.9663 L166.9145 75.6326 L167.8595 75.549 L168.8045 76.1999 L169.7495 76.2709 L170.6945 74.823 L171.6395 73.6717 L172.5845 73.8979 L173.5295 73.6841 L174.4745 72.9543 L175.4195 70.9683 L176.3645 70.0242 L177.3095 71.0222 L178.2545 72.6933 L179.1995 72.7734 L180.1445 72.8411 L181.0895 72.1028 L182.0345 73.0813 L182.9795 74.7872 L183.9245 74.1593 L184.8695 71.0538 L185.8145 69.5209 L186.7595 71.8063 L187.7045 76.6477 L188.6495 79.287 L189.5945 79.6907 L190.5395 79.5173 L191.4845 80.1253 L192.4295 82.5795 L193.3745 82.2166 L194.3195 79.8632 L195.2645 78.3914 L196.2095 80.0028 L197.1545 83.7272 L198.0995 86.7016 L199.0445 86.7732 L199.9895 88.1414 L200.9345 90.4895 L201.8795 92.5862 L202.8245 93.2034 L203.7695 94.1427 L204.7145 95.0855 L205.6595 97.7218 L206.6045 100.2546 L207.5495 101.405 L208.4945 102.29 L209.4395 104.9666 L210.3845 108.751 L211.3295 110.2992 L212.2745 110.064 L213.2195 109.685 L214.1645 109.9217 L215.1095 111.6866 L216.0545 113.3634 L216.9995 113.5209 L217.9445 114.2138 L218.8895 115.0064 L219.8345 117.1483 L220.7795 118.3097 L221.7245 116.6466 L222.6695 113.4494 L223.6145 111.8698 L224.5595 113.9213 L225.5045 118.2121 L226.4495 121.8818 L227.3945 124.0357 L228.3395 125.9298 L229.2845 128.7691 L230.2295 130.7695 L231.1745 129.6871 L232.1195 126.9923 L233.0645 125.041 L234.0095 126.505 L234.9545 130.0961 L235.8995 133.6111 L236.8445 136.5037 L237.7895 139.4292 L238.7345 144.307 L239.6795 149.1845 L240.6245 153.1985 L241.5695 155.3391 L242.5145 157.3375 L243.4595 159.3266 L244.4045 160.7262 L245.3495 158.629 L246.2945 154.2573 L247.2395 150.7139 L248.1845 149.903 L249.1295 151.0894 L250.0745 150.5261 L251.0195 148.2954 L251.9645 149.2744 L252.9095 152.5242 L253.8545 155.3671 L254.7995 155.9137 L255.7445 154.6425 L256.6895 155.1403 L257.6345 158.8658 L258.5795 162.0959 L259.5245 162.8975 L260.4695 162.1513 L261.4145 162.8873 L262.3595 167.0282 L263.3045 172.2294 L264.2495 174.8682 L265.1945 175.7834 L266.1395 178.9042 L267.0845 184.4425 L268.0295 189.0195 L268.9745 188.6989 L269.9195 184.3463 L270.8645 181.0779 L271.8095 182.1519 L272.7545 185.8642 L273.6995 187.541 L274.6445 185.1772 L275.5895 184.8117 L276.5345 188.7174 L277.4795 193.8064 L278.4245 195.3857 L279.3695 193.328 L280.3145 190.5232 L281.2595 191.4895 L282.2045 193.8546 L283.1495 193.7614 L284.0945 191.0845 L285.0395 189.0807 L285.9845 191.5174 L286.9295 197.1676 L287.8745 201.3027 L288.8195 203.3865 L289.7645 205.0371 L290.7095 208.7045 L291.6545 212.8534 L292.5995 212.4939 L293.5445 207.3765 L294.4895 201.5621 L295.4345 199.8121 L296.3795 202.091 L297.3245 203.9357 L298.2695 203.174 L299.2145 203.0574 L300.1595 204.8796 L301.1045 208.0007 L302.0495 209.2133 L302.9945 207.1457 L303.9395 204.162 L304.8845 204.2472 L305.8295 207.0076 L306.7745 207.4338 L307.7195 205.5774 L308.6645 203.8689 L309.6095 205.3484 L310.5545 209.9876 L311.4995 213.8282 L312.4445 214.8546 L313.3895 214.5947 L314.3345 217.1837 L315.2795 221.2467 L316.2245 223.5056 L317.1695 222.1979 L318.1145 218.9981 L319.0595 219.5518 L320.0045 223.903 L320.9495 227.4229 L321.8945 227.1186 L322.8395 224.6287 L323.7845 224.2219 L324.7295 227.2936 L325.6745 231.3316 L326.6195 231.3467 L327.5645 230.1508 L328.5095 231.4805 L329.4545 236.395 L330.3995 241.3836 L331.3445 243.881 L332.2895 241.4875 L333.2345 241.4315 L334.1795 244.3162 L335.1245 245.5117 L336.0695 243.8765 L337.0145 243.4296 L337.9595 243.6384 L338.9045 246.2375 L339.8495 247.4728 L340.7945 244.6971 L341.7395 238.7461 L342.6845 236.8341 L343.6295 236.5757 L344.5745 236.8475 L345.5195 235.179 L346.4645 233.257 L347.4095 235.198 L348.3545 240.0023 L349.2995 243.1037 L350.2445 242.1782 L351.1895 237.8585 L352.1345 234.9291 L353.0795 235.5843 L354.0245 233.8095 L354.9695 227.8692 L355.9145 225.1393 L356.8595 227.5017 L357.8045 233.0836 L358.7495 236.1616 L359.6945 236.6866 L360.6395 234.3387 L361.5845 234.9788 L362.5295 234.7824 L363.4745 231.7555 L364.4195 227.0937 L365.3645 222.5578 L366.3095 220.3465 L367.2545 221.683 L368.1995 222.5477 L369.1445 222.2538 L370.0895 222.7152 L371.0345 226.6879 L371.9795 230.0909 L372.9245 229.0598 L373.8695 223.0168 L374.8145 219.3004 L375.7595 216.7883 L376.7045 217.5305 L377.6495 215.4203 L378.5945 214.5773 L379.5395 216.8457 L380.4845 220.502 L381.4295 221.9043 L382.3745 222.8373 L383.3195 223.2733 L384.2645 224.799 L385.2095 225.2135 L386.1545 226.3694 L387.0995 224.979 L388.0445 217.557 L388.9895 215.0101 L389.9345 213.5109 L390.8795 212.6429 L391.8245 207.4812 L392.7695 201.107 L393.7145 197.6934 L394.6595 197.7903 L395.6045 202.0253 L396.5495 203.9345 L397.4945 201.5053 L398.4395 199.6224 L399.3845 199.6992 L400.3295 199.2873 L401.2745 195.9281 L402.2195 192.2721 L403.1645 190.136 L404.1095 191.8014 L405.0545 196.1022 L405.9995 201.1444 L406.9445 204.3867 L407.8895 208.6333 L408.8345 213.0899 L409.7795 215.7787 L410.7245 218.4368 L411.6695 216.639 L412.6145 215.8898 L413.5595 215.3506 L414.5045 214.8587 L415.4495 212.9229 L416.3945 209.3554 L417.3395 207.1403 L418.2845 208.5764 L419.2295 208.6557 L420.1745 207.0464 L421.1195 206.746 L422.0645 204.9597 L423.0095 205.2733 L423.9545 205.0453 L424.8995 205.589 L425.8445 206.7157 L426.7895 206.6654 L427.7345 205.2118 L428.6795 205.8333 L429.6245 205.9178 L430.5695 207.6765 L431.5145 208.11 L432.4595 207.1583 L433.4045 208.0681 L434.3495 208.7543 L435.2945 240.3646 L436.2395 232.7201 L437.1845 235.6382 L438.1295 235.9225 L439.0745 234.2761 L440.0195 231.8115 L440.9645 228.3338 L441.9095 225.4059 L442.8545 223.6852 L443.7995 222.3115 L444.7445 219.733 L445.6895 219.3124 L446.6345 219.4272 L447.5795 221.1899 L448.5245 225.978 L449.4695 230.276 L450.4145 234.1737 L451.3595 235.9515 L452.3045 236.6498 L453.2495 237.2335 L454.1945 237.9381 L455.1395 241.1289 L456.0845 245.8839 L457.0295 251.2451 L457.9745 256.4702 L458.9195 258.956 L459.8645 260.5059 L460.8095 260.4212 L461.7545 261.9651 L462.6995 260.9474 L463.6445 261.2312 L464.5895 260.7231 L465.5345 258.9019 L466.4795 258.9936 L467.4245 254.6431 L468.3695 253.2392 L469.3145 253.7394 L470.2595 254.4161 L471.2045 255.9324 L472.1495 255.8105 L473.0945 256.3073 L474.0395 255.399 L474.9845 254.164 L475.9295 254.8486 L476.8745 255.2918 L477.8195 258.2047 L478.7645 261.501 L479.7095 265.2254 L480.6545 268.7527 L481.5995 266.5701 L482.5445 264.766 L483.4895 264.0275 L484.4345 263.55 L485.3795 265.6731 L486.3245 265.9901 L487.2695 266.6156 L488.2145 266.897 L489.1595 266.6901 L490.1045 267.1878 L491.0495 266.5504 L491.9945 265.7944 L492.9395 265.4093 L493.8845 265.8733 L494.8295 268.9005 L495.7745 267.9694 L496.7195 268.6263 L497.6645 268.8241 L498.6095 268.6449 L499.5545 267.8157 L500.4995 268.738 L501.4445 269.31 L502.3895 270.6552 L503.3345 271.6913 L504.2795 271.1521 L505.2245 271.9017 L506.1695 271.3661 L507.1145 271.4152 L508.0595 270.9776 L509.0045 270.4585 L509.9495 270.8384 L510.8945 270.2055 L511.8395 269.2691 L512.7845 267.0996 L513.7295 264.0926 L514.6745 264.7672 L515.6195 265.3577 L516.5645 267.3625 L517.5095 269.2004 L518.4545 269.1219 L519.3995 269.2776 L520.3445 266.3115 L521.2895 260.2659 L522.2345 252.7244 L523.1795 245.162 L524.1245 240.8289 L525.0695 247.4272 L526.0145 256.816 L526.9595 268.1654 L527.9045 267.4738 L528.8495 276.6037 L529.7945 278.5664 L530.7395 280.8394 L531.6845 282.5157 L532.6295 280.5735 L533.5745 281.3792 L534.5195 282.836 L535.4645 281.3097 L536.4095 284.0421 L537.3545 286.8102 L538.2995 287.4611 L539.2445 291.6566 L540.1895 296.5938 L541.1345 299.3575 L542.0795 303.3608 L543.0245 301.7056 L543.9695 296.6631 L544.9145 294.9261 L545.8595 293.7748 L546.8045 293.4847 L547.7495 293.1716 L548.6945 292.2037 L549.6395 291.9926 L550.5845 295.4369 L551.5295 298.164 L552.4745 300.8609 L553.4195 303.29 L554.3645 305.7783 L555.3095 306.2624 L556.2545 310.6638 L557.1995 302.7691 L558.1445 293.4338 L559.0895 289.1907 L560.0345 289.9849 L560.9795 293.5007 L561.9245 299.9702 L562.8695 307.2442 L563.8145 314.6642 L564.7595 320.5412 L565.7045 314.8625 L566.6495 321.5894 L567.5945 321.7566 L568.5395 319.9476 L569.4845 319.4359 L570.4295 315.1922 L571.3745 317.6505 L572.3195 316.4344 L573.2645 315.4548 L574.2095 311.3925 L575.1545 308.5934 L576.0995 307.1082 L577.0445 305.2966 L577.9895 304.4096 L578.9345 304.3325 L579.8795 304.7177 L580.8245 303.9552 L581.7695 304.3089 L582.7145 304.9306 L583.6595 307.1877 L584.6045 312.1634 L585.5495 317.0779 L586.4945 323.3616 L587.4395 329.964 L588.3845 333.761 L589.3295 335.1877 L590.2745 336.9206 L591.2195 341.1283 L592.1645 343.4424 L593.1095 346.8858 L594.0545 356.6354 L594.9995 353.0812 L595.9445 352.9304 L596.8895 352.6891 L597.8345 351.5542 L598.7795 350.0171 L599.7245 349.6892 L600.6695 347.572 L601.6145 346.7239 L602.5595 348.834 L603.5045 349.227 L604.4495 349.6183 L605.3945 349.0184 L606.3395 349.266 L607.2845 347.6082 L608.2295 347.0531 L609.1745 347.203 L610.1195 349.6207 L611.0645 353.7314 L612.0095 359.9931 L612.9545 367.2012 L613.8995 371.6176 L614.8445 375.214 L615.7895 377.611 L616.7345 379.3492 L617.6795 379.5638 L618.6245 375.8839 L619.5695 372.7339 L620.5145 369.0366 L621.4595 365.624 L622.4045 363.2422 L623.3495 361.8694 L624.2945 360.8033 L625.2395 359.8574 L626.1845 359.6523 L627.1295 359.187 L628.0745 357.6624 L629.0195 356.1205 L629.9645 354.7235 L630.9095 354.736 L631.8545 355.0145 L632.7995 353.9734 L633.7445 356.2538 L634.6895 361.059 L635.6345 364.4186 L636.5795 369.6877 L637.5245 371.6249 L638.4695 373.3704 L639.4145 377.9944 L640.3595 381.3954 L641.3045 384.6731 L642.2495 394.6165 L643.1945 397.5948 L644.1395 399.2654 L645.0845 398.5668 L646.0295 389.9613 L646.9745 385.4097 L647.9195 381.9455 L648.8645 380.6092 L649.8095 380.454 L650.7545 383.1424 L651.6995 384.4518 L652.6445 385.7928 L653.5895 386.8206 L654.5345 389.0589 L655.4795 390.6327 L656.4245 392.5291 L657.3695 396.2496 L658.3145 401.3355 L659.2595 406.5949 L660.2045 410.5199 L661.1495 411.6236" style="fill:none; fill-rule:evenodd;"/></g></g></svg>
</div>



这不同于各种 LO 的连续正弦波，若设备扫描 LO 范围从 70 MHz 到 6 GHz，测量的将不是通道功率，而是峰值传输功率（频谱仪设置为峰值保持）。以下两个图表显示了 Tx 衰减设置之间的差异，默认设置 -10dB 可确保模拟输出级完全在线性范围内运行，并且不会饱和或接近 1PdB 点。在此设置下，使用 SMA 电缆将 Tx 直接循环到 Rx 中也是安全的。但注意请勿将 TX 衰减设置为小于 -10dB，以及请勿将 Tx（输出）信号环入 Rx（输入）连接器。在尝试以绝对单位进行任何测量之前，应校准 AD9361 或任何 SDR 设备。因为AD9361提供的数据与ADC的满量程范围有关，而ADC的满量程范围取决于收发器的增益级，所以这一步必不可少。生成的值单位最好用 dBFS 或 ADC 代码描述，而非 dBm 或 伏特。

<div class="method2">

  <img src="https://wiki.analog.com/_media/university/tools/pluto/users/txat0.png?cache=" width="300">

</div>

<div class="method1">

  <img src="https://wiki.analog.com/_media/university/tools/pluto/users/txat-10.png?cache=" width="300">

</div>

当 LO 变化超过 100 MHz 时，-10 dB 衰减设置中的随机峰值是由 Tx 校准引起的随机噪声。  
正如预期的那样，较宽的 LTE10 通道测量比窄 CW 信号具有更大的功率。


### 传输保真度
这是 [Keysight 89600 VSA 软件](http://www.keysight.com/find/89600B)的输出，用于测量信号解调和完整的矢量信号分析。在这种情况下，我们生成 LTE 10（10MHz 宽通道），通过 ADALM-PLUTO 的 Tx 端口发送，并将其捕获到 [PXA N9030A 信号分析仪](http://www.keysight.com/find/N9030A)上。我们可以测量射频偏移（频率误差 = 50Hz）以及创建的 64-QAM 星座图的精度（EVM 为 -46dB，或小于 0.5 RMS 误差）——这对用户来说相当不错。我们还可以看到输出功率（10MHz 信道的平均峰值输出为 -45dBm/Hz）。
![](https://wiki.analog.com/_media/university/tools/pluto/users/rev_b_tx_lte10.png?cache=)
通过改变 LO 频率、输出功率、输出衰减，结果将会出现变化。
<!--EVM_RMS vs Frequency for LTE-10 QAM-64-->


<div width="100%" style="overflow-x: auto;"> 
<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" style="fill-opacity:1; color-rendering:auto; color-interpolation:auto; stroke:black; text-rendering:auto; stroke-linecap:square; stroke-miterlimit:10; stroke-opacity:1; shape-rendering:auto; fill:black; stroke-dasharray:none; font-weight:normal; stroke-width:1; font-family:'Dialog'; font-style:normal; stroke-linejoin:miter; font-size:12px; stroke-dashoffset:0; image-rendering:auto;" width="100%" height="100%" viewBox="0 0 858 608" preserveAspectRatio="xMidYMid slice"><!--Generated by the Batik Graphics2D SVG Generator--><defs id="genericDefs"/><g><defs id="defs1"><clipPath clipPathUnits="userSpaceOnUse" id="clipPath1"><path d="M0 0 L858 0 L858 608 L0 608 L0 0 Z"/></clipPath><font horiz-adv-x="75.0" id="font1"><font-face ascent="100.53711" descent="21.972656" units-per-em="100" style="font-style:normal; font-family:SansSerif; font-weight:normal;"/><missing-glyph horiz-adv-x="75.0" d="M12.5 0 L12.5 62.5 L62.5 62.5 L62.5 0 L12.5 0 ZM14.0625 1.5625 L60.9375 1.5625 L60.9375 60.9375 L14.0625 60.9375 L14.0625 1.5625 Z"/><glyph unicode="0" horiz-adv-x="55.615234" d="M4.1562 35.2969 Q4.1562 48 6.7656 55.7422 Q9.375 63.4844 14.5234 67.6797 Q19.6719 71.875 27.4844 71.875 Q33.25 71.875 37.5938 69.5547 Q41.9375 67.2344 44.7734 62.8672 Q47.6094 58.5 49.2188 52.2266 Q50.8281 45.9531 50.8281 35.2969 Q50.8281 22.7031 48.2422 14.9688 Q45.6562 7.2344 40.5078 3.0078 Q35.3594 -1.2188 27.4844 -1.2188 Q17.1406 -1.2188 11.2344 6.2031 Q4.1562 15.1406 4.1562 35.2969 ZM13.1875 35.2969 Q13.1875 17.6719 17.3125 11.8359 Q21.4375 6 27.4844 6 Q33.5469 6 37.6719 11.8594 Q41.7969 17.7188 41.7969 35.2969 Q41.7969 52.9844 37.6719 58.7891 Q33.5469 64.5938 27.3906 64.5938 Q21.3438 64.5938 17.7188 59.4688 Q13.1875 52.9375 13.1875 35.2969 Z"/><glyph unicode="1" horiz-adv-x="55.615234" d="M37.25 0 L28.4688 0 L28.4688 56 Q25.2969 52.9844 20.1406 49.9531 Q14.9844 46.9219 10.8906 45.4062 L10.8906 53.9062 Q18.2656 57.375 23.7812 62.3047 Q29.2969 67.2344 31.5938 71.875 L37.25 71.875 L37.25 0 Z"/><glyph unicode="2" horiz-adv-x="55.615234" d="M50.3438 8.4531 L50.3438 0 L3.0312 0 Q2.9375 3.1719 4.0469 6.1094 Q5.8594 10.9375 9.8359 15.625 Q13.8125 20.3125 21.3438 26.4688 Q33.0156 36.0312 37.1172 41.625 Q41.2188 47.2188 41.2188 52.2031 Q41.2188 57.4219 37.4766 61.0078 Q33.7344 64.5938 27.7344 64.5938 Q21.3906 64.5938 17.5781 60.7891 Q13.7656 56.9844 13.7188 50.25 L4.6875 51.1719 Q5.6094 61.2812 11.6641 66.5781 Q17.7188 71.875 27.9375 71.875 Q38.2344 71.875 44.2422 66.1641 Q50.25 60.4531 50.25 52 Q50.25 47.7031 48.4922 43.5547 Q46.7344 39.4062 42.6562 34.8125 Q38.5781 30.2188 29.1094 22.2188 Q21.1875 15.5781 18.9453 13.2109 Q16.7031 10.8438 15.2344 8.4531 L50.3438 8.4531 Z"/><glyph unicode="3" horiz-adv-x="55.615234" d="M4.2031 18.8906 L12.9844 20.0625 Q14.5 12.5938 18.1406 9.2969 Q21.7812 6 27 6 Q33.2031 6 37.4766 10.2969 Q41.75 14.5938 41.75 20.9531 Q41.75 27 37.7969 30.9297 Q33.8438 34.8594 27.7344 34.8594 Q25.25 34.8594 21.5312 33.8906 L22.5156 41.6094 Q23.3906 41.5 23.9219 41.5 Q29.5469 41.5 34.0391 44.4297 Q38.5312 47.3594 38.5312 53.4688 Q38.5312 58.2969 35.2578 61.4766 Q31.9844 64.6562 26.8125 64.6562 Q21.6875 64.6562 18.2656 61.4297 Q14.8438 58.2031 13.875 51.7656 L5.0781 53.3281 Q6.6875 62.1562 12.3984 67.0156 Q18.1094 71.875 26.6094 71.875 Q32.4688 71.875 37.3984 69.3594 Q42.3281 66.8438 44.9453 62.5 Q47.5625 58.1562 47.5625 53.2656 Q47.5625 48.6406 45.0703 44.8281 Q42.5781 41.0156 37.7031 38.7656 Q44.0469 37.3125 47.5625 32.6953 Q51.0781 28.0781 51.0781 21.1406 Q51.0781 11.7656 44.2422 5.25 Q37.4062 -1.2656 26.9531 -1.2656 Q17.5312 -1.2656 11.3047 4.3516 Q5.0781 9.9688 4.2031 18.8906 Z"/><glyph unicode="4" horiz-adv-x="55.615234" d="M32.3281 0 L32.3281 17.1406 L1.2656 17.1406 L1.2656 25.2031 L33.9375 71.5781 L41.1094 71.5781 L41.1094 25.2031 L50.7812 25.2031 L50.7812 17.1406 L41.1094 17.1406 L41.1094 0 L32.3281 0 ZM32.3281 25.2031 L32.3281 57.4688 L9.9062 25.2031 L32.3281 25.2031 Z"/><glyph unicode="5" horiz-adv-x="55.615234" d="M4.1562 18.75 L13.375 19.5312 Q14.4062 12.7969 18.1406 9.3984 Q21.875 6 27.1562 6 Q33.5 6 37.8906 10.7891 Q42.2812 15.5781 42.2812 23.4844 Q42.2812 31 38.0625 35.3516 Q33.8438 39.7031 27 39.7031 Q22.75 39.7031 19.3359 37.7734 Q15.9219 35.8438 13.9688 32.7656 L5.7188 33.8438 L12.6406 70.6094 L48.25 70.6094 L48.25 62.2031 L19.6719 62.2031 L15.8281 42.9688 Q22.2656 47.4688 29.3438 47.4688 Q38.7188 47.4688 45.1641 40.9688 Q51.6094 34.4688 51.6094 24.2656 Q51.6094 14.5469 45.9531 7.4688 Q39.0625 -1.2188 27.1562 -1.2188 Q17.3906 -1.2188 11.2109 4.25 Q5.0312 9.7188 4.1562 18.75 Z"/><glyph unicode="6" horiz-adv-x="55.615234" d="M49.75 54.0469 L41.0156 53.375 Q39.8438 58.5469 37.7031 60.8906 Q34.125 64.6562 28.9062 64.6562 Q24.7031 64.6562 21.5312 62.3125 Q17.3906 59.2812 14.9922 53.4688 Q12.5938 47.6562 12.5 36.9219 Q15.6719 41.75 20.2656 44.0938 Q24.8594 46.4375 29.8906 46.4375 Q38.6719 46.4375 44.8516 39.9688 Q51.0312 33.5 51.0312 23.25 Q51.0312 16.5 48.125 10.7188 Q45.2188 4.9375 40.1406 1.8594 Q35.0625 -1.2188 28.6094 -1.2188 Q17.625 -1.2188 10.6953 6.8594 Q3.7656 14.9375 3.7656 33.5 Q3.7656 54.25 11.4219 63.6719 Q18.1094 71.875 29.4375 71.875 Q37.8906 71.875 43.2891 67.1406 Q48.6875 62.4062 49.75 54.0469 ZM13.875 23.1875 Q13.875 18.6562 15.7969 14.5078 Q17.7188 10.3594 21.1875 8.1797 Q24.6562 6 28.4688 6 Q34.0312 6 38.0391 10.4922 Q42.0469 14.9844 42.0469 22.7031 Q42.0469 30.125 38.0859 34.3984 Q34.125 38.6719 28.125 38.6719 Q22.1719 38.6719 18.0234 34.3984 Q13.875 30.125 13.875 23.1875 Z"/><glyph unicode=")" horiz-adv-x="33.30078" d="M12.3594 -21.0469 L6.0625 -21.0469 Q20.6562 2.3906 20.6562 25.875 Q20.6562 35.0625 18.5625 44.0938 Q16.8906 51.4219 13.9219 58.1562 Q12.0156 62.5469 6.0625 72.7969 L12.3594 72.7969 Q21.5312 60.5469 25.9219 48.1875 Q29.6875 37.5469 29.6875 25.9219 Q29.6875 12.75 24.6328 0.4453 Q19.5781 -11.8594 12.3594 -21.0469 Z"/><glyph unicode="z" horiz-adv-x="50.0" d="M1.9531 0 L1.9531 7.125 L34.9688 45.0156 Q29.3438 44.7344 25.0469 44.7344 L3.9062 44.7344 L3.9062 51.8594 L46.2969 51.8594 L46.2969 46.0469 L18.2188 13.1406 L12.7969 7.125 Q18.7031 7.5625 23.875 7.5625 L47.8594 7.5625 L47.8594 0 L1.9531 0 Z"/><glyph unicode="H" horiz-adv-x="72.2168" d="M8.0156 0 L8.0156 71.5781 L17.4844 71.5781 L17.4844 42.1875 L54.6875 42.1875 L54.6875 71.5781 L64.1562 71.5781 L64.1562 0 L54.6875 0 L54.6875 33.7344 L17.4844 33.7344 L17.4844 0 L8.0156 0 Z"/><glyph unicode="G" horiz-adv-x="77.7832" d="M41.2188 28.0781 L41.2188 36.4688 L71.5312 36.5312 L71.5312 9.9688 Q64.5469 4.3906 57.125 1.5859 Q49.7031 -1.2188 41.8906 -1.2188 Q31.3438 -1.2188 22.7266 3.2969 Q14.1094 7.8125 9.7188 16.3594 Q5.3281 24.9062 5.3281 35.4531 Q5.3281 45.9062 9.6953 54.9609 Q14.0625 64.0156 22.2656 68.4062 Q30.4688 72.7969 41.1562 72.7969 Q48.9219 72.7969 55.1953 70.2891 Q61.4688 67.7812 65.0391 63.2891 Q68.6094 58.7969 70.4531 51.5625 L61.9219 49.2188 Q60.2969 54.6875 57.9062 57.8125 Q55.5156 60.9375 51.0703 62.8203 Q46.625 64.7031 41.2188 64.7031 Q34.7188 64.7031 29.9844 62.7266 Q25.25 60.75 22.3438 57.5234 Q19.4375 54.2969 17.8281 50.4375 Q15.0938 43.7969 15.0938 36.0312 Q15.0938 26.4688 18.3906 20.0234 Q21.6875 13.5781 27.9844 10.4531 Q34.2812 7.3281 41.3594 7.3281 Q47.5156 7.3281 53.375 9.6953 Q59.2344 12.0625 62.25 14.75 L62.25 28.0781 L41.2188 28.0781 Z"/><glyph unicode="(" horiz-adv-x="33.30078" d="M23.3906 -21.0469 Q16.1094 -11.8594 11.0859 0.4453 Q6.0625 12.75 6.0625 25.9219 Q6.0625 37.5469 9.8125 48.1875 Q14.2031 60.5469 23.3906 72.7969 L29.6875 72.7969 Q23.7812 62.6406 21.875 58.2969 Q18.8906 51.5625 17.1875 44.2344 Q15.0938 35.1094 15.0938 25.875 Q15.0938 2.3906 29.6875 -21.0469 L23.3906 -21.0469 Z"/><glyph unicode=" " horiz-adv-x="27.783203" d=""/><glyph unicode="y" horiz-adv-x="50.0" d="M6.2031 -19.9688 L5.2188 -11.7188 Q8.1094 -12.5 10.25 -12.5 Q13.1875 -12.5 14.9453 -11.5234 Q16.7031 -10.5469 17.8281 -8.7969 Q18.6562 -7.4688 20.5156 -2.25 Q20.75 -1.5156 21.2969 -0.0938 L1.6094 51.8594 L11.0781 51.8594 L21.875 21.8281 Q23.9688 16.1094 25.6406 9.8125 Q27.1562 15.875 29.25 21.625 L40.3281 51.8594 L49.125 51.8594 L29.3906 -0.875 Q26.2188 -9.4219 24.4688 -12.6406 Q22.125 -17 19.0938 -19.0234 Q16.0625 -21.0469 11.8594 -21.0469 Q9.3281 -21.0469 6.2031 -19.9688 Z"/><glyph unicode="c" horiz-adv-x="50.0" d="M40.4375 19 L49.0781 17.875 Q47.6562 8.9375 41.8203 3.8828 Q35.9844 -1.1719 27.4844 -1.1719 Q16.8438 -1.1719 10.375 5.7891 Q3.9062 12.75 3.9062 25.7344 Q3.9062 34.125 6.6875 40.4297 Q9.4688 46.7344 15.1562 49.8828 Q20.8438 53.0312 27.5469 53.0312 Q35.9844 53.0312 41.3594 48.7578 Q46.7344 44.4844 48.25 36.625 L39.7031 35.2969 Q38.4844 40.5312 35.3828 43.1641 Q32.2812 45.7969 27.875 45.7969 Q21.2344 45.7969 17.0859 41.0391 Q12.9375 36.2812 12.9375 25.9844 Q12.9375 15.5312 16.9453 10.7969 Q20.9531 6.0625 27.3906 6.0625 Q32.5625 6.0625 36.0312 9.2344 Q39.5 12.4062 40.4375 19 Z"/><glyph unicode="n" horiz-adv-x="55.615234" d="M6.5938 0 L6.5938 51.8594 L14.5 51.8594 L14.5 44.4844 Q20.2188 53.0312 31 53.0312 Q35.6875 53.0312 39.625 51.3438 Q43.5625 49.6562 45.5156 46.9219 Q47.4688 44.1875 48.25 40.4375 Q48.7344 37.9844 48.7344 31.8906 L48.7344 0 L39.9375 0 L39.9375 31.5469 Q39.9375 36.9219 38.9141 39.5781 Q37.8906 42.2344 35.2812 43.8203 Q32.6719 45.4062 29.1562 45.4062 Q23.5312 45.4062 19.4531 41.8438 Q15.375 38.2812 15.375 28.3281 L15.375 0 L6.5938 0 Z"/><glyph unicode="u" horiz-adv-x="55.615234" d="M40.5781 0 L40.5781 7.625 Q34.5156 -1.1719 24.125 -1.1719 Q19.5312 -1.1719 15.5547 0.5859 Q11.5781 2.3438 9.6484 5.0078 Q7.7188 7.6719 6.9375 11.5312 Q6.3906 14.1094 6.3906 19.7344 L6.3906 51.8594 L15.1875 51.8594 L15.1875 23.0938 Q15.1875 16.2188 15.7188 13.8125 Q16.5469 10.3594 19.2344 8.375 Q21.9219 6.3906 25.875 6.3906 Q29.8281 6.3906 33.2969 8.4219 Q36.7656 10.4531 38.2109 13.9453 Q39.6562 17.4375 39.6562 24.0781 L39.6562 51.8594 L48.4375 51.8594 L48.4375 0 L40.5781 0 Z"/><glyph unicode="q" horiz-adv-x="55.615234" d="M39.6562 -19.875 L39.6562 5.5156 Q37.5938 2.6406 33.9062 0.7344 Q30.2188 -1.1719 26.0781 -1.1719 Q16.8438 -1.1719 10.1797 6.2031 Q3.5156 13.5781 3.5156 26.4219 Q3.5156 34.2344 6.2266 40.4297 Q8.9375 46.625 14.0859 49.8281 Q19.2344 53.0312 25.3906 53.0312 Q35.0156 53.0312 40.5312 44.9219 L40.5312 51.8594 L48.4375 51.8594 L48.4375 -19.875 L39.6562 -19.875 ZM12.5469 26.0781 Q12.5469 16.0625 16.75 11.0625 Q20.9531 6.0625 26.8125 6.0625 Q32.4219 6.0625 36.4766 10.8203 Q40.5312 15.5781 40.5312 25.2969 Q40.5312 35.6406 36.2578 40.8672 Q31.9844 46.0938 26.2188 46.0938 Q20.5156 46.0938 16.5312 41.2344 Q12.5469 36.375 12.5469 26.0781 Z"/><glyph unicode="e" horiz-adv-x="55.615234" d="M42.0938 16.7031 L51.1719 15.5781 Q49.0312 7.625 43.2188 3.2266 Q37.4062 -1.1719 28.375 -1.1719 Q17 -1.1719 10.3281 5.8359 Q3.6562 12.8438 3.6562 25.4844 Q3.6562 38.5781 10.3984 45.8047 Q17.1406 53.0312 27.875 53.0312 Q38.2812 53.0312 44.875 45.9531 Q51.4688 38.875 51.4688 26.0312 Q51.4688 25.25 51.4219 23.6875 L12.75 23.6875 Q13.2344 15.1406 17.5781 10.6016 Q21.9219 6.0625 28.4219 6.0625 Q33.25 6.0625 36.6719 8.6016 Q40.0938 11.1406 42.0938 16.7031 ZM13.2344 30.9062 L42.1875 30.9062 Q41.6094 37.4531 38.875 40.7188 Q34.6719 45.7969 27.9844 45.7969 Q21.9219 45.7969 17.7969 41.75 Q13.6719 37.7031 13.2344 30.9062 Z"/><glyph unicode="r" horiz-adv-x="33.30078" d="M6.5 0 L6.5 51.8594 L14.4062 51.8594 L14.4062 44 Q17.4375 49.5156 20 51.2734 Q22.5625 53.0312 25.6406 53.0312 Q30.0781 53.0312 34.6719 50.2031 L31.6406 42.0469 Q28.4219 43.9531 25.2031 43.9531 Q22.3125 43.9531 20.0156 42.2188 Q17.7188 40.4844 16.75 37.4062 Q15.2812 32.7188 15.2812 27.1562 L15.2812 0 L6.5 0 Z"/><glyph unicode="F" horiz-adv-x="61.083984" d="M8.2031 0 L8.2031 71.5781 L56.5 71.5781 L56.5 63.1406 L17.6719 63.1406 L17.6719 40.9688 L51.2656 40.9688 L51.2656 32.5156 L17.6719 32.5156 L17.6719 0 L8.2031 0 Z"/><glyph unicode="-" horiz-adv-x="33.30078" d="M3.1719 21.4844 L3.1719 30.3281 L30.1719 30.3281 L30.1719 21.4844 L3.1719 21.4844 Z"/><glyph unicode="8" horiz-adv-x="55.615234" d="M17.6719 38.8125 Q12.2031 40.8281 9.5703 44.5391 Q6.9375 48.25 6.9375 53.4219 Q6.9375 61.2344 12.5547 66.5547 Q18.1719 71.875 27.4844 71.875 Q36.8594 71.875 42.5781 66.4297 Q48.2969 60.9844 48.2969 53.1719 Q48.2969 48.1875 45.6797 44.5078 Q43.0625 40.8281 37.75 38.8125 Q44.3438 36.6719 47.7812 31.8828 Q51.2188 27.0938 51.2188 20.4531 Q51.2188 11.2812 44.7266 5.0312 Q38.2344 -1.2188 27.6406 -1.2188 Q17.0469 -1.2188 10.5469 5.0547 Q4.0469 11.3281 4.0469 20.7031 Q4.0469 27.6875 7.5938 32.3984 Q11.1406 37.1094 17.6719 38.8125 ZM15.9219 53.7188 Q15.9219 48.6406 19.1953 45.4141 Q22.4688 42.1875 27.6875 42.1875 Q32.7656 42.1875 36.0156 45.3828 Q39.2656 48.5781 39.2656 53.2188 Q39.2656 58.0625 35.9141 61.3594 Q32.5625 64.6562 27.5938 64.6562 Q22.5625 64.6562 19.2422 61.4297 Q15.9219 58.2031 15.9219 53.7188 ZM13.0938 20.6562 Q13.0938 16.8906 14.875 13.375 Q16.6562 9.8594 20.1719 7.9297 Q23.6875 6 27.7344 6 Q34.0312 6 38.1328 10.0547 Q42.2344 14.1094 42.2344 20.3594 Q42.2344 26.7031 38.0156 30.8594 Q33.7969 35.0156 27.4375 35.0156 Q21.2344 35.0156 17.1641 30.9141 Q13.0938 26.8125 13.0938 20.6562 Z"/><glyph unicode="M" horiz-adv-x="83.30078" d="M7.4219 0 L7.4219 71.5781 L21.6875 71.5781 L38.625 20.9062 Q40.9688 13.8125 42.0469 10.2969 Q43.2656 14.2031 45.8438 21.7812 L62.9844 71.5781 L75.7344 71.5781 L75.7344 0 L66.6094 0 L66.6094 59.9062 L45.7969 0 L37.25 0 L16.5469 60.9375 L16.5469 0 L7.4219 0 Z"/><glyph unicode="V" horiz-adv-x="66.69922" d="M28.1719 0 L0.4375 71.5781 L10.6875 71.5781 L29.2969 19.5781 Q31.5469 13.3281 33.0625 7.8594 Q34.7188 13.7188 36.9219 19.5781 L56.25 71.5781 L65.9219 71.5781 L37.8906 0 L28.1719 0 Z"/><glyph unicode="E" horiz-adv-x="66.69922" d="M7.9062 0 L7.9062 71.5781 L59.6719 71.5781 L59.6719 63.1406 L17.3906 63.1406 L17.3906 41.2188 L56.9844 41.2188 L56.9844 32.8125 L17.3906 32.8125 L17.3906 8.4531 L61.3281 8.4531 L61.3281 0 L7.9062 0 Z"/><glyph unicode="S" horiz-adv-x="66.69922" d="M4.5 23 L13.4219 23.7812 Q14.0625 18.4062 16.3828 14.9688 Q18.7031 11.5312 23.5859 9.4062 Q28.4688 7.2812 34.5781 7.2812 Q39.9844 7.2812 44.1406 8.8906 Q48.2969 10.5 50.3203 13.3047 Q52.3438 16.1094 52.3438 19.4375 Q52.3438 22.7969 50.3906 25.3125 Q48.4375 27.8281 43.9531 29.5469 Q41.0625 30.6719 31.2031 33.0391 Q21.3438 35.4062 17.3906 37.5 Q12.25 40.1875 9.7422 44.1641 Q7.2344 48.1406 7.2344 53.0781 Q7.2344 58.5 10.3047 63.2109 Q13.375 67.9219 19.2891 70.3594 Q25.2031 72.7969 32.4219 72.7969 Q40.375 72.7969 46.4609 70.2344 Q52.5469 67.6719 55.8125 62.6953 Q59.0781 57.7188 59.3281 51.4219 L50.25 50.7344 Q49.5156 57.5156 45.2891 60.9844 Q41.0625 64.4531 32.8125 64.4531 Q24.2188 64.4531 20.2891 61.3047 Q16.3594 58.1562 16.3594 53.7188 Q16.3594 49.8594 19.1406 47.3594 Q21.875 44.875 33.4219 42.2656 Q44.9688 39.6562 49.2656 37.7031 Q55.5156 34.8125 58.4922 30.3984 Q61.4688 25.9844 61.4688 20.2188 Q61.4688 14.5 58.2031 9.4453 Q54.9375 4.3906 48.8047 1.5859 Q42.6719 -1.2188 35.0156 -1.2188 Q25.2969 -1.2188 18.7266 1.6094 Q12.1562 4.4375 8.4219 10.1328 Q4.6875 15.8281 4.5 23 Z"/><glyph unicode="R" horiz-adv-x="72.2168" d="M7.8594 0 L7.8594 71.5781 L39.5938 71.5781 Q49.1719 71.5781 54.1484 69.6484 Q59.125 67.7188 62.1094 62.8359 Q65.0938 57.9531 65.0938 52.0469 Q65.0938 44.4375 60.1562 39.2109 Q55.2188 33.9844 44.9219 32.5625 Q48.6875 30.7656 50.6406 29 Q54.7812 25.2031 58.5 19.4844 L70.9531 0 L59.0312 0 L49.5625 14.8906 Q45.4062 21.3438 42.7266 24.7578 Q40.0469 28.1719 37.9219 29.5391 Q35.7969 30.9062 33.5938 31.4531 Q31.9844 31.7812 28.3281 31.7812 L17.3281 31.7812 L17.3281 0 L7.8594 0 ZM17.3281 39.9844 L37.7031 39.9844 Q44.1875 39.9844 47.8516 41.3281 Q51.5156 42.6719 53.4219 45.625 Q55.3281 48.5781 55.3281 52.0469 Q55.3281 57.125 51.6406 60.3984 Q47.9531 63.6719 39.9844 63.6719 L17.3281 63.6719 L17.3281 39.9844 Z"/><glyph unicode="B" horiz-adv-x="66.69922" d="M7.3281 0 L7.3281 71.5781 L34.1875 71.5781 Q42.3906 71.5781 47.3438 69.4062 Q52.2969 67.2344 55.1016 62.7188 Q57.9062 58.2031 57.9062 53.2656 Q57.9062 48.6875 55.4219 44.6328 Q52.9375 40.5781 47.9062 38.0938 Q54.3906 36.1875 57.8828 31.5938 Q61.375 27 61.375 20.75 Q61.375 15.7188 59.25 11.3984 Q57.125 7.0781 54 4.7344 Q50.875 2.3906 46.1641 1.1953 Q41.4531 0 34.625 0 L7.3281 0 ZM16.7969 41.5 L32.2812 41.5 Q38.5781 41.5 41.3125 42.3281 Q44.9219 43.4062 46.75 45.8984 Q48.5781 48.3906 48.5781 52.1562 Q48.5781 55.7188 46.875 58.4297 Q45.1719 61.1406 41.9922 62.1406 Q38.8125 63.1406 31.1094 63.1406 L16.7969 63.1406 L16.7969 41.5 ZM16.7969 8.4531 L34.625 8.4531 Q39.2031 8.4531 41.0625 8.7969 Q44.3438 9.375 46.5391 10.7422 Q48.7344 12.1094 50.1484 14.7188 Q51.5625 17.3281 51.5625 20.75 Q51.5625 24.75 49.5156 27.7109 Q47.4688 30.6719 43.8281 31.8672 Q40.1875 33.0625 33.3438 33.0625 L16.7969 33.0625 L16.7969 8.4531 Z"/><glyph unicode="d" horiz-adv-x="55.615234" d="M40.2344 0 L40.2344 6.5469 Q35.2969 -1.1719 25.7344 -1.1719 Q19.5312 -1.1719 14.3281 2.25 Q9.125 5.6719 6.2734 11.7969 Q3.4219 17.9219 3.4219 25.875 Q3.4219 33.6406 6.0078 39.9688 Q8.5938 46.2969 13.7734 49.6641 Q18.9531 53.0312 25.3438 53.0312 Q30.0312 53.0312 33.6953 51.0547 Q37.3594 49.0781 39.6562 45.9062 L39.6562 71.5781 L48.3906 71.5781 L48.3906 0 L40.2344 0 ZM12.4531 25.875 Q12.4531 15.9219 16.6484 10.9922 Q20.8438 6.0625 26.5625 6.0625 Q32.3281 6.0625 36.3516 10.7734 Q40.375 15.4844 40.375 25.1406 Q40.375 35.7969 36.2734 40.7734 Q32.1719 45.75 26.1719 45.75 Q20.3125 45.75 16.3828 40.9688 Q12.4531 36.1875 12.4531 25.875 Z"/><glyph unicode="l" horiz-adv-x="22.216797" d="M6.3906 0 L6.3906 71.5781 L15.1875 71.5781 L15.1875 0 L6.3906 0 Z"/><glyph unicode="s" horiz-adv-x="50.0" d="M3.0781 15.4844 L11.7656 16.8438 Q12.5 11.625 15.8438 8.8438 Q19.1875 6.0625 25.2031 6.0625 Q31.25 6.0625 34.1797 8.5234 Q37.1094 10.9844 37.1094 14.3125 Q37.1094 17.2812 34.5156 19 Q32.7188 20.1719 25.5312 21.9688 Q15.875 24.4219 12.1406 26.2031 Q8.4062 27.9844 6.4766 31.1328 Q4.5469 34.2812 4.5469 38.0938 Q4.5469 41.5469 6.1328 44.5078 Q7.7188 47.4688 10.4531 49.4219 Q12.5 50.9219 16.0391 51.9766 Q19.5781 53.0312 23.6406 53.0312 Q29.7344 53.0312 34.3516 51.2734 Q38.9688 49.5156 41.1641 46.5078 Q43.3594 43.5 44.1875 38.4844 L35.5938 37.3125 Q35.0156 41.3125 32.2031 43.5547 Q29.3906 45.7969 24.2656 45.7969 Q18.2188 45.7969 15.625 43.7969 Q13.0312 41.7969 13.0312 39.1094 Q13.0312 37.4062 14.1094 36.0312 Q15.1875 34.625 17.4844 33.6875 Q18.7969 33.2031 25.25 31.4531 Q34.5781 28.9531 38.2578 27.3672 Q41.9375 25.7812 44.0391 22.7578 Q46.1406 19.7344 46.1406 15.2344 Q46.1406 10.8438 43.5781 6.9609 Q41.0156 3.0781 36.1797 0.9531 Q31.3438 -1.1719 25.25 -1.1719 Q15.1406 -1.1719 9.8438 3.0312 Q4.5469 7.2344 3.0781 15.4844 Z"/><glyph unicode="t" horiz-adv-x="27.783203" d="M25.7812 7.8594 L27.0469 0.0938 Q23.3438 -0.6875 20.4062 -0.6875 Q15.625 -0.6875 12.9922 0.8281 Q10.3594 2.3438 9.2812 4.8125 Q8.2031 7.2812 8.2031 15.1875 L8.2031 45.0156 L1.7656 45.0156 L1.7656 51.8594 L8.2031 51.8594 L8.2031 64.7031 L16.9375 69.9688 L16.9375 51.8594 L25.7812 51.8594 L25.7812 45.0156 L16.9375 45.0156 L16.9375 14.7031 Q16.9375 10.9375 17.4062 9.8672 Q17.875 8.7969 18.9219 8.1562 Q19.9688 7.5156 21.9219 7.5156 Q23.3906 7.5156 25.7812 7.8594 Z"/><glyph unicode="m" horiz-adv-x="83.30078" d="M6.5938 0 L6.5938 51.8594 L14.4531 51.8594 L14.4531 44.5781 Q16.8906 48.3906 20.9453 50.7109 Q25 53.0312 30.1719 53.0312 Q35.9375 53.0312 39.625 50.6406 Q43.3125 48.25 44.8281 43.9531 Q50.9844 53.0312 60.8438 53.0312 Q68.5625 53.0312 72.7109 48.7578 Q76.8594 44.4844 76.8594 35.5938 L76.8594 0 L68.1094 0 L68.1094 32.6719 Q68.1094 37.9375 67.2578 40.2578 Q66.4062 42.5781 64.1641 43.9922 Q61.9219 45.4062 58.8906 45.4062 Q53.4219 45.4062 49.8047 41.7734 Q46.1875 38.1406 46.1875 30.125 L46.1875 0 L37.4062 0 L37.4062 33.6875 Q37.4062 39.5469 35.2578 42.4766 Q33.1094 45.4062 28.2188 45.4062 Q24.5156 45.4062 21.3672 43.4531 Q18.2188 41.5 16.7969 37.7422 Q15.375 33.9844 15.375 26.9062 L15.375 0 L6.5938 0 Z"/><glyph unicode="i" horiz-adv-x="22.216797" d="M6.6406 61.4688 L6.6406 71.5781 L15.4375 71.5781 L15.4375 61.4688 L6.6406 61.4688 ZM6.6406 0 L6.6406 51.8594 L15.4375 51.8594 L15.4375 0 L6.6406 0 Z"/><glyph unicode="h" horiz-adv-x="55.615234" d="M6.5938 0 L6.5938 71.5781 L15.375 71.5781 L15.375 45.9062 Q21.5312 53.0312 30.9062 53.0312 Q36.6719 53.0312 40.9219 50.7578 Q45.1719 48.4844 47 44.4844 Q48.8281 40.4844 48.8281 32.8594 L48.8281 0 L40.0469 0 L40.0469 32.8594 Q40.0469 39.4531 37.1875 42.4531 Q34.3281 45.4531 29.1094 45.4531 Q25.2031 45.4531 21.7578 43.4297 Q18.3125 41.4062 16.8438 37.9375 Q15.375 34.4688 15.375 28.375 L15.375 0 L6.5938 0 Z"/><glyph unicode="a" horiz-adv-x="55.615234" d="M40.4375 6.3906 Q35.5469 2.25 31.0312 0.5391 Q26.5156 -1.1719 21.3438 -1.1719 Q12.7969 -1.1719 8.2031 3 Q3.6094 7.1719 3.6094 13.6719 Q3.6094 17.4844 5.3438 20.6328 Q7.0781 23.7812 9.8906 25.6875 Q12.7031 27.5938 16.2188 28.5625 Q18.7969 29.25 24.0312 29.8906 Q34.6719 31.1562 39.7031 32.9062 Q39.75 34.7188 39.75 35.2031 Q39.75 40.5781 37.25 42.7812 Q33.8906 45.75 27.25 45.75 Q21.0469 45.75 18.0938 43.5781 Q15.1406 41.4062 13.7188 35.8906 L5.125 37.0625 Q6.2969 42.5781 8.9844 45.9688 Q11.6719 49.3594 16.75 51.1953 Q21.8281 53.0312 28.5156 53.0312 Q35.1562 53.0312 39.3047 51.4688 Q43.4531 49.9062 45.4062 47.5391 Q47.3594 45.1719 48.1406 41.5469 Q48.5781 39.3125 48.5781 33.4531 L48.5781 21.7344 Q48.5781 9.4688 49.1406 6.2266 Q49.7031 2.9844 51.375 0 L42.1875 0 Q40.8281 2.7344 40.4375 6.3906 ZM39.7031 26.0312 Q34.9062 24.0781 25.3438 22.7031 Q19.9219 21.9219 17.6797 20.9453 Q15.4375 19.9688 14.2109 18.0938 Q12.9844 16.2188 12.9844 13.9219 Q12.9844 10.4062 15.6484 8.0625 Q18.3125 5.7188 23.4375 5.7188 Q28.5156 5.7188 32.4688 7.9375 Q36.4219 10.1562 38.2812 14.0156 Q39.7031 17 39.7031 22.7969 L39.7031 26.0312 Z"/><glyph unicode="9" horiz-adv-x="55.615234" d="M5.4688 16.5469 L13.9219 17.3281 Q14.9844 11.375 18.0156 8.6875 Q21.0469 6 25.7812 6 Q29.8281 6 32.8828 7.8594 Q35.9375 9.7188 37.8906 12.8203 Q39.8438 15.9219 41.1641 21.1953 Q42.4844 26.4688 42.4844 31.9375 Q42.4844 32.5156 42.4375 33.6875 Q39.7969 29.5 35.2344 26.8828 Q30.6719 24.2656 25.3438 24.2656 Q16.4531 24.2656 10.3047 30.7109 Q4.1562 37.1562 4.1562 47.7031 Q4.1562 58.5938 10.5781 65.2344 Q17 71.875 26.6562 71.875 Q33.6406 71.875 39.4297 68.1172 Q45.2188 64.3594 48.2188 57.3984 Q51.2188 50.4375 51.2188 37.25 Q51.2188 23.5312 48.2422 15.4062 Q45.2656 7.2812 39.3828 3.0312 Q33.5 -1.2188 25.5938 -1.2188 Q17.1875 -1.2188 11.8672 3.4453 Q6.5469 8.1094 5.4688 16.5469 ZM41.4531 48.1406 Q41.4531 55.7188 37.4297 60.1562 Q33.4062 64.5938 27.7344 64.5938 Q21.875 64.5938 17.5312 59.8125 Q13.1875 55.0312 13.1875 47.4062 Q13.1875 40.5781 17.3125 36.3047 Q21.4375 32.0312 27.4844 32.0312 Q33.5938 32.0312 37.5234 36.3047 Q41.4531 40.5781 41.4531 48.1406 Z"/><glyph unicode="D" horiz-adv-x="72.2168" d="M7.7188 0 L7.7188 71.5781 L32.375 71.5781 Q40.7188 71.5781 45.125 70.5625 Q51.2656 69.1406 55.6094 65.4375 Q61.2812 60.6406 64.0859 53.1953 Q66.8906 45.75 66.8906 36.1875 Q66.8906 28.0312 64.9922 21.7344 Q63.0938 15.4375 60.1094 11.3047 Q57.125 7.1719 53.5859 4.8047 Q50.0469 2.4375 45.0469 1.2188 Q40.0469 0 33.5469 0 L7.7188 0 ZM17.1875 8.4531 L32.4688 8.4531 Q39.5469 8.4531 43.5781 9.7656 Q47.6094 11.0781 50 13.4844 Q53.375 16.8438 55.25 22.5312 Q57.125 28.2188 57.125 36.3281 Q57.125 47.5625 53.4375 53.5938 Q49.75 59.625 44.4844 61.6719 Q40.6719 63.1406 32.2344 63.1406 L17.1875 63.1406 L17.1875 8.4531 Z"/><glyph unicode="A" horiz-adv-x="66.69922" d="M-0.1406 0 L27.3438 71.5781 L37.5469 71.5781 L66.8438 0 L56.0625 0 L47.7031 21.6875 L17.7812 21.6875 L9.9062 0 L-0.1406 0 ZM20.5156 29.3906 L44.7812 29.3906 L37.3125 49.2188 Q33.8906 58.25 32.2344 64.0625 Q30.8594 57.1719 28.375 50.3906 L20.5156 29.3906 Z"/></font><font horiz-adv-x="75.0" id="font2"><font-face ascent="100.53711" descent="21.972656" units-per-em="100" style="font-style:normal; font-family:SansSerif; font-weight:bold;"/><missing-glyph horiz-adv-x="75.0" d="M12.5 0 L12.5 62.5 L62.5 62.5 L62.5 0 L12.5 0 ZM14.0625 1.5625 L60.9375 1.5625 L60.9375 60.9375 L14.0625 60.9375 L14.0625 1.5625 Z"/><glyph unicode="M" horiz-adv-x="83.30078" d="M7.0781 0 L7.0781 71.5781 L28.7188 71.5781 L41.7031 22.75 L54.5469 71.5781 L76.2188 71.5781 L76.2188 0 L62.7969 0 L62.7969 56.3438 L48.5781 0 L34.6719 0 L20.5156 56.3438 L20.5156 0 L7.0781 0 Z"/><glyph unicode="V" horiz-adv-x="66.69922" d="M25.5312 0 L-0.0469 71.5781 L15.625 71.5781 L33.7344 18.6094 L51.2656 71.5781 L66.6094 71.5781 L40.9688 0 L25.5312 0 Z"/><glyph unicode="E" horiz-adv-x="66.69922" d="M7.2812 0 L7.2812 71.5781 L60.3594 71.5781 L60.3594 59.4688 L21.7344 59.4688 L21.7344 43.6094 L57.6719 43.6094 L57.6719 31.5469 L21.7344 31.5469 L21.7344 12.0625 L61.7188 12.0625 L61.7188 0 L7.2812 0 Z"/><glyph unicode="S" horiz-adv-x="66.69922" d="M3.6094 23.2969 L17.6719 24.6562 Q18.9531 17.5781 22.8281 14.2578 Q26.7031 10.9375 33.2969 10.9375 Q40.2812 10.9375 43.8203 13.8906 Q47.3594 16.8438 47.3594 20.7969 Q47.3594 23.3438 45.875 25.125 Q44.3906 26.9062 40.6719 28.2188 Q38.1406 29.1094 29.1094 31.3438 Q17.4844 34.2344 12.7969 38.4219 Q6.2031 44.3438 6.2031 52.8281 Q6.2031 58.2969 9.3047 63.0625 Q12.4062 67.8281 18.2422 70.3125 Q24.0781 72.7969 32.3281 72.7969 Q45.7969 72.7969 52.6094 66.8906 Q59.4219 60.9844 59.7656 51.125 L45.3125 50.4844 Q44.3906 56 41.3359 58.4219 Q38.2812 60.8438 32.1719 60.8438 Q25.875 60.8438 22.3125 58.25 Q20.0156 56.5938 20.0156 53.8125 Q20.0156 51.2656 22.1719 49.4688 Q24.9062 47.1719 35.4531 44.6797 Q46 42.1875 51.0547 39.5234 Q56.1094 36.8594 58.9609 32.25 Q61.8125 27.6406 61.8125 20.8438 Q61.8125 14.7031 58.3984 9.3281 Q54.9844 3.9531 48.7344 1.3438 Q42.4844 -1.2656 33.1562 -1.2656 Q19.5781 -1.2656 12.3047 5.0078 Q5.0312 11.2812 3.6094 23.2969 Z"/><glyph unicode="R" horiz-adv-x="72.2168" d="M7.3281 0 L7.3281 71.5781 L37.75 71.5781 Q49.2188 71.5781 54.4219 69.6484 Q59.625 67.7188 62.75 62.7891 Q65.875 57.8594 65.875 51.5156 Q65.875 43.4531 61.1328 38.2031 Q56.3906 32.9531 46.9688 31.5938 Q51.6562 28.8594 54.7109 25.5859 Q57.7656 22.3125 62.9375 13.9688 L71.6875 0 L54.3906 0 L43.9531 15.5781 Q38.375 23.9219 36.3281 26.0938 Q34.2812 28.2656 31.9844 29.0781 Q29.6875 29.8906 24.7031 29.8906 L21.7812 29.8906 L21.7812 0 L7.3281 0 ZM21.7812 41.3125 L32.4688 41.3125 Q42.875 41.3125 45.4609 42.1875 Q48.0469 43.0625 49.5156 45.2109 Q50.9844 47.3594 50.9844 50.5938 Q50.9844 54.2031 49.0547 56.4219 Q47.125 58.6406 43.6094 59.2344 Q41.8438 59.4688 33.0625 59.4688 L21.7812 59.4688 L21.7812 41.3125 Z"/><glyph unicode="4" horiz-adv-x="55.615234" d="M31.1562 0 L31.1562 14.4062 L1.8594 14.4062 L1.8594 26.4219 L32.9062 71.875 L44.4375 71.875 L44.4375 26.4688 L53.3281 26.4688 L53.3281 14.4062 L44.4375 14.4062 L44.4375 0 L31.1562 0 ZM31.1562 26.4688 L31.1562 50.9219 L14.7031 26.4688 L31.1562 26.4688 Z"/><glyph unicode="6" horiz-adv-x="55.615234" d="M50.7344 54.0469 L37.4531 52.5938 Q36.9688 56.6875 34.9141 58.6406 Q32.8594 60.5938 29.5938 60.5938 Q25.25 60.5938 22.2422 56.6875 Q19.2344 52.7812 18.4531 40.4375 Q23.5781 46.4844 31.2031 46.4844 Q39.7969 46.4844 45.9219 39.9453 Q52.0469 33.4062 52.0469 23.0469 Q52.0469 12.0625 45.6016 5.4219 Q39.1562 -1.2188 29.0469 -1.2188 Q18.2188 -1.2188 11.2344 7.2031 Q4.25 15.625 4.25 34.8125 Q4.25 54.5 11.5234 63.1875 Q18.7969 71.875 30.4219 71.875 Q38.5781 71.875 43.9219 67.3125 Q49.2656 62.75 50.7344 54.0469 ZM19.625 24.125 Q19.625 17.4375 22.7031 13.7969 Q25.7812 10.1562 29.7344 10.1562 Q33.5469 10.1562 36.0859 13.1328 Q38.625 16.1094 38.625 22.9062 Q38.625 29.8906 35.8906 33.1328 Q33.1562 36.375 29.0469 36.375 Q25.0938 36.375 22.3594 33.2734 Q19.625 30.1719 19.625 24.125 Z"/><glyph unicode="A" horiz-adv-x="72.2168" d="M71.8281 0 L56.1094 0 L49.8594 16.2656 L21.2344 16.2656 L15.3281 0 L0 0 L27.875 71.5781 L43.1719 71.5781 L71.8281 0 ZM45.2188 28.3281 L35.3594 54.8906 L25.6875 28.3281 L45.2188 28.3281 Z"/><glyph unicode="Q" horiz-adv-x="77.7832" d="M64.8906 9.0781 Q70.2188 5.2812 76.4688 3.0312 L71.1406 -7.1719 Q67.875 -6.2031 64.75 -4.5 Q64.0625 -4.1562 55.125 1.8594 Q48.0938 -1.2188 39.5469 -1.2188 Q23.0469 -1.2188 13.6953 8.5 Q4.3438 18.2188 4.3438 35.7969 Q4.3438 53.3281 13.7188 63.0625 Q23.0938 72.7969 39.1562 72.7969 Q55.0781 72.7969 64.4062 63.0625 Q73.7344 53.3281 73.7344 35.7969 Q73.7344 26.5156 71.1406 19.4844 Q69.1875 14.1094 64.8906 9.0781 ZM53.2656 17.2344 Q56.0625 20.5156 57.4531 25.1484 Q58.8438 29.7812 58.8438 35.7969 Q58.8438 48.1875 53.375 54.3203 Q47.9062 60.4531 39.0625 60.4531 Q30.2188 60.4531 24.7266 54.2969 Q19.2344 48.1406 19.2344 35.7969 Q19.2344 23.25 24.7266 17.0234 Q30.2188 10.7969 38.625 10.7969 Q41.75 10.7969 44.5312 11.8125 Q40.1406 14.7031 35.5938 16.3125 L39.6562 24.5625 Q46.7812 22.125 53.2656 17.2344 Z"/><glyph unicode="0" horiz-adv-x="55.615234" d="M27.4375 71.875 Q37.8438 71.875 43.7031 64.4531 Q50.6875 55.6719 50.6875 35.2969 Q50.6875 14.9844 43.6562 6.1094 Q37.8438 -1.2188 27.4375 -1.2188 Q17 -1.2188 10.6016 6.8125 Q4.2031 14.8438 4.2031 35.4531 Q4.2031 55.6719 11.2344 64.5469 Q17.0469 71.875 27.4375 71.875 ZM27.4375 60.5 Q24.9531 60.5 23 58.9141 Q21.0469 57.3281 19.9688 53.2188 Q18.5625 47.9062 18.5625 35.2969 Q18.5625 22.7031 19.8281 17.9922 Q21.0938 13.2812 23.0234 11.7188 Q24.9531 10.1562 27.4375 10.1562 Q29.9375 10.1562 31.8906 11.7422 Q33.8438 13.3281 34.9062 17.4375 Q36.3281 22.7031 36.3281 35.2969 Q36.3281 47.9062 35.0625 52.6172 Q33.7969 57.3281 31.8672 58.9141 Q29.9375 60.5 27.4375 60.5 Z"/><glyph unicode="1" horiz-adv-x="55.615234" d="M39.3594 0 L25.6406 0 L25.6406 51.7031 Q18.1094 44.6719 7.9062 41.3125 L7.9062 53.7656 Q13.2812 55.5156 19.5781 60.4219 Q25.875 65.3281 28.2188 71.875 L39.3594 71.875 L39.3594 0 Z"/><glyph unicode="-" horiz-adv-x="33.30078" d="M5.6094 19.0938 L5.6094 32.8125 L32.5625 32.8125 L32.5625 19.0938 L5.6094 19.0938 Z"/><glyph unicode="T" horiz-adv-x="61.083984" d="M23.3906 0 L23.3906 59.4688 L2.1562 59.4688 L2.1562 71.5781 L59.0312 71.5781 L59.0312 59.4688 L37.8438 59.4688 L37.8438 0 L23.3906 0 Z"/><glyph unicode="L" horiz-adv-x="61.083984" d="M7.6719 0 L7.6719 71 L22.125 71 L22.125 12.0625 L58.0625 12.0625 L58.0625 0 L7.6719 0 Z"/><glyph unicode="o" horiz-adv-x="61.083984" d="M4 26.6562 Q4 33.5 7.375 39.8984 Q10.75 46.2969 16.9219 49.6641 Q23.0938 53.0312 30.7188 53.0312 Q42.4844 53.0312 50 45.3906 Q57.5156 37.75 57.5156 26.0781 Q57.5156 14.3125 49.9219 6.5703 Q42.3281 -1.1719 30.8125 -1.1719 Q23.6875 -1.1719 17.2188 2.0547 Q10.75 5.2812 7.375 11.5 Q4 17.7188 4 26.6562 ZM18.0625 25.9219 Q18.0625 18.2188 21.7266 14.1172 Q25.3906 10.0156 30.7656 10.0156 Q36.1406 10.0156 39.7734 14.1172 Q43.4062 18.2188 43.4062 26.0312 Q43.4062 33.6406 39.7734 37.7422 Q36.1406 41.8438 30.7656 41.8438 Q25.3906 41.8438 21.7266 37.7422 Q18.0625 33.6406 18.0625 25.9219 Z"/><glyph unicode="f" horiz-adv-x="33.30078" d="M1.1719 51.8594 L8.7969 51.8594 L8.7969 55.7656 Q8.7969 62.3125 10.1875 65.5312 Q11.5781 68.75 15.3125 70.7734 Q19.0469 72.7969 24.75 72.7969 Q30.6094 72.7969 36.2344 71.0469 L34.375 61.4688 Q31.1094 62.25 28.0781 62.25 Q25.0938 62.25 23.8047 60.8594 Q22.5156 59.4688 22.5156 55.5156 L22.5156 51.8594 L32.7656 51.8594 L32.7656 41.0625 L22.5156 41.0625 L22.5156 0 L8.7969 0 L8.7969 41.0625 L1.1719 41.0625 L1.1719 51.8594 Z"/><glyph unicode="y" horiz-adv-x="55.615234" d="M0.6875 51.8594 L15.2812 51.8594 L27.6875 15.0469 L39.7969 51.8594 L54 51.8594 L35.6875 1.9531 L32.4219 -7.0781 Q30.6094 -11.625 28.9766 -14.0156 Q27.3438 -16.4062 25.2188 -17.8984 Q23.0938 -19.3906 19.9922 -20.2188 Q16.8906 -21.0469 12.9844 -21.0469 Q9.0312 -21.0469 5.2188 -20.2188 L4 -9.4688 Q7.2344 -10.1094 9.8125 -10.1094 Q14.5938 -10.1094 16.8906 -7.3047 Q19.1875 -4.5 20.4062 -0.1406 L0.6875 51.8594 Z"/><glyph unicode="c" horiz-adv-x="55.615234" d="M52.3906 36.5312 L38.875 34.0781 Q38.1875 38.1406 35.7656 40.1875 Q33.3438 42.2344 29.5 42.2344 Q24.3594 42.2344 21.3125 38.6953 Q18.2656 35.1562 18.2656 26.8594 Q18.2656 17.625 21.3672 13.8203 Q24.4688 10.0156 29.6875 10.0156 Q33.5938 10.0156 36.0859 12.2344 Q38.5781 14.4531 39.5938 19.875 L53.0781 17.5781 Q50.9844 8.2969 45.0234 3.5625 Q39.0625 -1.1719 29.0469 -1.1719 Q17.6719 -1.1719 10.9141 6.0078 Q4.1562 13.1875 4.1562 25.875 Q4.1562 38.7188 10.9375 45.875 Q17.7188 53.0312 29.2969 53.0312 Q38.7656 53.0312 44.3594 48.9531 Q49.9531 44.875 52.3906 36.5312 Z"/><glyph unicode="n" horiz-adv-x="61.083984" d="M54.3438 0 L40.625 0 L40.625 26.4688 Q40.625 34.8594 39.75 37.3281 Q38.875 39.7969 36.8906 41.1641 Q34.9062 42.5312 32.125 42.5312 Q28.5625 42.5312 25.7344 40.5781 Q22.9062 38.625 21.8516 35.3984 Q20.7969 32.1719 20.7969 23.4844 L20.7969 0 L7.0781 0 L7.0781 51.8594 L19.8281 51.8594 L19.8281 44.2344 Q26.6094 53.0312 36.9219 53.0312 Q41.4531 53.0312 45.2109 51.3906 Q48.9688 49.75 50.8984 47.2109 Q52.8281 44.6719 53.5859 41.4531 Q54.3438 38.2344 54.3438 32.2344 L54.3438 0 Z"/><glyph unicode="u" horiz-adv-x="61.083984" d="M41.3125 0 L41.3125 7.7656 Q38.4844 3.6094 33.8672 1.2188 Q29.25 -1.1719 24.125 -1.1719 Q18.8906 -1.1719 14.7422 1.125 Q10.5938 3.4219 8.7422 7.5703 Q6.8906 11.7188 6.8906 19.0469 L6.8906 51.8594 L20.6094 51.8594 L20.6094 28.0312 Q20.6094 17.0938 21.3672 14.625 Q22.125 12.1562 24.125 10.7188 Q26.125 9.2812 29.2031 9.2812 Q32.7188 9.2812 35.5 11.2109 Q38.2812 13.1406 39.3047 15.9922 Q40.3281 18.8438 40.3281 29.9844 L40.3281 51.8594 L54.0469 51.8594 L54.0469 0 L41.3125 0 Z"/><glyph unicode="q" horiz-adv-x="61.083984" d="M41.0625 -19.7344 L41.0625 6.3438 Q38.375 2.875 34.375 0.8516 Q30.375 -1.1719 25.7344 -1.1719 Q16.8906 -1.1719 11.1875 5.4688 Q4.4375 13.2344 4.4375 26.5156 Q4.4375 39.0156 10.7656 46.0234 Q17.0938 53.0312 26.4688 53.0312 Q31.6406 53.0312 35.4219 50.8359 Q39.2031 48.6406 42.1406 44.1875 L42.1406 51.8594 L54.7812 51.8594 L54.7812 -19.7344 L41.0625 -19.7344 ZM41.5 26.5625 Q41.5 34.5156 38.2578 38.3984 Q35.0156 42.2812 30.125 42.2812 Q25.1406 42.2812 21.7969 38.3281 Q18.4531 34.375 18.4531 25.7812 Q18.4531 17.2344 21.6797 13.4531 Q24.9062 9.6719 29.6406 9.6719 Q34.375 9.6719 37.9375 13.9219 Q41.5 18.1719 41.5 26.5625 Z"/><glyph unicode="e" horiz-adv-x="55.615234" d="M37.2031 16.5 L50.875 14.2031 Q48.25 6.6875 42.5547 2.7578 Q36.8594 -1.1719 28.3281 -1.1719 Q14.7969 -1.1719 8.2969 7.6719 Q3.1719 14.75 3.1719 25.5312 Q3.1719 38.4219 9.9141 45.7266 Q16.6562 53.0312 26.9531 53.0312 Q38.5312 53.0312 45.2188 45.3906 Q51.9062 37.75 51.6094 21.9688 L17.2344 21.9688 Q17.3906 15.875 20.5625 12.4766 Q23.7344 9.0781 28.4688 9.0781 Q31.6875 9.0781 33.8828 10.8359 Q36.0781 12.5938 37.2031 16.5 ZM37.9844 30.375 Q37.8438 36.3281 34.9141 39.4297 Q31.9844 42.5312 27.7812 42.5312 Q23.2969 42.5312 20.3594 39.2656 Q17.4375 35.9844 17.4844 30.375 L37.9844 30.375 Z"/><glyph unicode="r" horiz-adv-x="38.916016" d="M20.3125 0 L6.5938 0 L6.5938 51.8594 L19.3438 51.8594 L19.3438 44.4844 Q22.6094 49.7031 25.2188 51.3672 Q27.8281 53.0312 31.1562 53.0312 Q35.8438 53.0312 40.1875 50.4375 L35.9375 38.4844 Q32.4688 40.7188 29.5 40.7188 Q26.6094 40.7188 24.6094 39.1328 Q22.6094 37.5469 21.4609 33.3984 Q20.3125 29.25 20.3125 16.0156 L20.3125 0 Z"/><glyph unicode="F" horiz-adv-x="61.083984" d="M7.375 0 L7.375 71.5781 L56.4531 71.5781 L56.4531 59.4688 L21.8281 59.4688 L21.8281 42.5312 L51.7031 42.5312 L51.7031 30.4219 L21.8281 30.4219 L21.8281 0 L7.375 0 Z"/><glyph unicode="s" horiz-adv-x="55.615234" d="M2.3438 14.7969 L16.1094 16.8906 Q17 12.8906 19.6797 10.8125 Q22.3594 8.7344 27.2031 8.7344 Q32.5156 8.7344 35.2031 10.6875 Q37.0156 12.0625 37.0156 14.3594 Q37.0156 15.9219 36.0312 16.9375 Q35.0156 17.9219 31.4531 18.75 Q14.8438 22.4062 10.4062 25.4375 Q4.25 29.6406 4.25 37.1094 Q4.25 43.8438 9.5703 48.4375 Q14.8906 53.0312 26.0781 53.0312 Q36.7188 53.0312 41.8984 49.5625 Q47.0781 46.0938 49.0312 39.3125 L36.0781 36.9219 Q35.25 39.9375 32.9297 41.5547 Q30.6094 43.1719 26.3125 43.1719 Q20.9062 43.1719 18.5625 41.6562 Q17 40.5781 17 38.875 Q17 37.4062 18.3594 36.375 Q20.2188 35.0156 31.1797 32.5234 Q42.1406 30.0312 46.4844 26.4219 Q50.7812 22.75 50.7812 16.2188 Q50.7812 9.0781 44.8281 3.9531 Q38.875 -1.1719 27.2031 -1.1719 Q16.6094 -1.1719 10.4297 3.125 Q4.25 7.4219 2.3438 14.7969 Z"/><glyph unicode="v" horiz-adv-x="55.615234" d="M21.4375 0 L0.5312 51.8594 L14.9375 51.8594 L24.7031 25.3906 L27.5469 16.5469 Q28.6562 19.9219 28.9531 21 Q29.6406 23.1875 30.4219 25.3906 L40.2812 51.8594 L54.3906 51.8594 L33.7969 0 L21.4375 0 Z"/><glyph unicode=" " horiz-adv-x="27.783203" d=""/><glyph unicode="X" horiz-adv-x="66.69922" d="M0 0 L24.4688 37.3594 L2.2969 71.5781 L19.1875 71.5781 L33.5469 48.5781 L47.6094 71.5781 L64.3594 71.5781 L42.0938 36.8125 L66.5469 0 L49.125 0 L33.25 24.75 L17.3281 0 L0 0 Z"/><glyph unicode="t" horiz-adv-x="33.30078" d="M30.9531 51.8594 L30.9531 40.9219 L21.5781 40.9219 L21.5781 20.0156 Q21.5781 13.6719 21.8516 12.625 Q22.125 11.5781 23.0781 10.8906 Q24.0312 10.2031 25.3906 10.2031 Q27.2969 10.2031 30.9062 11.5312 L32.0781 0.875 Q27.2969 -1.1719 21.2344 -1.1719 Q17.5312 -1.1719 14.5547 0.0703 Q11.5781 1.3125 10.1875 3.2969 Q8.7969 5.2812 8.25 8.6406 Q7.8125 11.0312 7.8125 18.3125 L7.8125 40.9219 L1.5156 40.9219 L1.5156 51.8594 L7.8125 51.8594 L7.8125 62.1562 L21.5781 70.1719 L21.5781 51.8594 L30.9531 51.8594 Z"/><glyph unicode="h" horiz-adv-x="61.083984" d="M20.8438 71.5781 L20.8438 45.2656 Q27.4844 53.0312 36.7188 53.0312 Q41.4531 53.0312 45.2656 51.2734 Q49.0781 49.5156 51.0078 46.7812 Q52.9375 44.0469 53.6406 40.7266 Q54.3438 37.4062 54.3438 30.4219 L54.3438 0 L40.625 0 L40.625 27.3906 Q40.625 35.5469 39.8438 37.7422 Q39.0625 39.9375 37.0859 41.2344 Q35.1094 42.5312 32.125 42.5312 Q28.7188 42.5312 26.0312 40.8672 Q23.3438 39.2031 22.0938 35.8594 Q20.8438 32.5156 20.8438 25.9844 L20.8438 0 L7.125 0 L7.125 71.5781 L20.8438 71.5781 Z"/><glyph unicode="g" horiz-adv-x="61.083984" d="M5.9062 -3.4219 L21.5781 -5.3281 Q21.9688 -8.0625 23.3906 -9.0781 Q25.3438 -10.5469 29.5469 -10.5469 Q34.9062 -10.5469 37.5938 -8.9375 Q39.4062 -7.8594 40.3281 -5.4688 Q40.9688 -3.7656 40.9688 0.8281 L40.9688 8.4062 Q34.8125 0 25.4375 0 Q14.9844 0 8.8906 8.8438 Q4.1094 15.8281 4.1094 26.2188 Q4.1094 39.2656 10.3828 46.1484 Q16.6562 53.0312 25.9844 53.0312 Q35.5938 53.0312 41.8438 44.5781 L41.8438 51.8594 L54.6875 51.8594 L54.6875 5.3281 Q54.6875 -3.8594 53.1719 -8.3984 Q51.6562 -12.9375 48.9219 -15.5234 Q46.1875 -18.1094 41.625 -19.5781 Q37.0625 -21.0469 30.0781 -21.0469 Q16.8906 -21.0469 11.375 -16.5312 Q5.8594 -12.0156 5.8594 -5.0781 Q5.8594 -4.3906 5.9062 -3.4219 ZM18.1719 27 Q18.1719 18.75 21.3672 14.9141 Q24.5625 11.0781 29.25 11.0781 Q34.2812 11.0781 37.75 15.0156 Q41.2188 18.9531 41.2188 26.6562 Q41.2188 34.7188 37.8984 38.625 Q34.5781 42.5312 29.5 42.5312 Q24.5625 42.5312 21.3672 38.6953 Q18.1719 34.8594 18.1719 27 Z"/><glyph unicode="i" horiz-adv-x="27.783203" d="M7.1719 58.8906 L7.1719 71.5781 L20.9062 71.5781 L20.9062 58.8906 L7.1719 58.8906 ZM7.1719 0 L7.1719 51.8594 L20.9062 51.8594 L20.9062 0 L7.1719 0 Z"/><glyph unicode="K" horiz-adv-x="72.2168" d="M7.4688 0 L7.4688 71.5781 L21.9219 71.5781 L21.9219 39.7969 L51.125 71.5781 L70.5625 71.5781 L43.6094 43.7031 L72.0156 0 L53.3281 0 L33.6406 33.5938 L21.9219 21.625 L21.9219 0 L7.4688 0 Z"/><glyph unicode=";" horiz-adv-x="33.30078" d="M9.4219 38.1406 L9.4219 51.8594 L23.1406 51.8594 L23.1406 38.1406 L9.4219 38.1406 ZM9.4219 13.7188 L23.1406 13.7188 L23.1406 3.9062 Q23.1406 -2.0469 22.1172 -5.4922 Q21.0938 -8.9375 18.2344 -11.6719 Q15.375 -14.4062 10.9844 -15.9688 L8.2969 -10.2969 Q12.4531 -8.9375 14.2109 -6.4922 Q15.9688 -4.0469 16.0625 0 L9.4219 0 L9.4219 13.7188 Z"/><glyph unicode="O" horiz-adv-x="77.7832" d="M4.3438 35.3594 Q4.3438 46.2969 7.625 53.7188 Q10.0625 59.1875 14.2812 63.5312 Q18.5 67.875 23.5312 69.9688 Q30.2188 72.7969 38.9688 72.7969 Q54.7812 72.7969 64.2812 62.9844 Q73.7812 53.1719 73.7812 35.6875 Q73.7812 18.3594 64.3594 8.5703 Q54.9375 -1.2188 39.1562 -1.2188 Q23.1875 -1.2188 13.7656 8.5234 Q4.3438 18.2656 4.3438 35.3594 ZM19.2344 35.8438 Q19.2344 23.6875 24.8516 17.4141 Q30.4688 11.1406 39.1094 11.1406 Q47.75 11.1406 53.2969 17.3594 Q58.8438 23.5781 58.8438 36.0312 Q58.8438 48.3438 53.4453 54.3984 Q48.0469 60.4531 39.1094 60.4531 Q30.1719 60.4531 24.7031 54.3203 Q19.2344 48.1875 19.2344 35.8438 Z"/><glyph unicode="U" horiz-adv-x="72.2168" d="M7.1719 71.5781 L21.625 71.5781 L21.625 32.8125 Q21.625 23.5781 22.1719 20.8438 Q23.0938 16.4531 26.5859 13.7969 Q30.0781 11.1406 36.1406 11.1406 Q42.2812 11.1406 45.4062 13.6484 Q48.5312 16.1562 49.1719 19.8203 Q49.8125 23.4844 49.8125 31.9844 L49.8125 71.5781 L64.2656 71.5781 L64.2656 33.9844 Q64.2656 21.0938 63.0938 15.7734 Q61.9219 10.4531 58.7656 6.7891 Q55.6094 3.125 50.3359 0.9531 Q45.0625 -1.2188 36.5781 -1.2188 Q26.3125 -1.2188 21.0156 1.1484 Q15.7188 3.5156 12.6484 7.2969 Q9.5781 11.0781 8.5938 15.2344 Q7.1719 21.3906 7.1719 33.4062 L7.1719 71.5781 Z"/><glyph unicode="P" horiz-adv-x="66.69922" d="M7.2812 0 L7.2812 71.5781 L30.4688 71.5781 Q43.6562 71.5781 47.6562 70.5156 Q53.8125 68.8906 57.9609 63.5 Q62.1094 58.1094 62.1094 49.5625 Q62.1094 42.9688 59.7188 38.4766 Q57.3281 33.9844 53.6406 31.4219 Q49.9531 28.8594 46.1406 28.0312 Q40.9688 27 31.1562 27 L21.7344 27 L21.7344 0 L7.2812 0 ZM21.7344 59.4688 L21.7344 39.1562 L29.6406 39.1562 Q38.1875 39.1562 41.0703 40.2812 Q43.9531 41.4062 45.5859 43.7969 Q47.2188 46.1875 47.2188 49.3594 Q47.2188 53.2656 44.9219 55.8047 Q42.625 58.3438 39.1094 58.9844 Q36.5312 59.4688 28.7188 59.4688 L21.7344 59.4688 Z"/><glyph unicode="D" horiz-adv-x="72.2168" d="M7.2344 71.5781 L33.6406 71.5781 Q42.5781 71.5781 47.2656 70.2188 Q53.5625 68.3594 58.0547 63.625 Q62.5469 58.8906 64.8906 52.0312 Q67.2344 45.1719 67.2344 35.1094 Q67.2344 26.2656 65.0469 19.875 Q62.3594 12.0625 57.375 7.2344 Q53.6094 3.5625 47.2188 1.5156 Q42.4375 0 34.4219 0 L7.2344 0 L7.2344 71.5781 ZM21.6875 59.4688 L21.6875 12.0625 L32.4688 12.0625 Q38.5312 12.0625 41.2188 12.75 Q44.7344 13.625 47.0469 15.7266 Q49.3594 17.8281 50.8281 22.6328 Q52.2969 27.4375 52.2969 35.75 Q52.2969 44.0469 50.8281 48.4922 Q49.3594 52.9375 46.7266 55.4219 Q44.0938 57.9062 40.0469 58.7969 Q37.0156 59.4688 28.1719 59.4688 L21.6875 59.4688 Z"/><glyph unicode="=" horiz-adv-x="58.398438" d="M4.1562 39.8438 L4.1562 52.4375 L54.2031 52.4375 L54.2031 39.8438 L4.1562 39.8438 ZM4.1562 18.1719 L4.1562 30.8125 L54.2031 30.8125 L54.2031 18.1719 L4.1562 18.1719 Z"/><glyph unicode="x" horiz-adv-x="55.615234" d="M0.5938 0 L19.2812 26.7031 L1.375 51.8594 L18.1094 51.8594 L27.2969 37.5938 L36.9688 51.8594 L53.0781 51.8594 L35.5 27.2969 L54.6875 0 L37.8438 0 L27.2969 16.0625 L16.6562 0 L0.5938 0 Z"/></font></defs><g style="fill:white; stroke:white;"><rect x="0" y="0" width="858" style="clip-path:url(#clipPath1); stroke:none;" height="608"/></g><g style="fill:white; text-rendering:optimizeSpeed; color-rendering:optimizeSpeed; image-rendering:optimizeSpeed; shape-rendering:crispEdges; color-interpolation:sRGB; stroke:white;"><rect x="0" width="858" height="608" y="0" style="stroke:none;"/><path style="stroke:none;" d="M112 541 L776 541 L776 49 L112 49 Z"/></g><g style="fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(38,38,38); stroke-width:0.6667;"><line y2="541" style="fill:none;" x1="112" x2="776" y1="541"/><line y2="49" style="fill:none;" x1="112" x2="776" y1="49"/><line y2="534.36" style="fill:none;" x1="112" x2="112" y1="541"/><line y2="534.36" style="fill:none;" x1="222.6667" x2="222.6667" y1="541"/><line y2="534.36" style="fill:none;" x1="333.3333" x2="333.3333" y1="541"/><line y2="534.36" style="fill:none;" x1="444" x2="444" y1="541"/><line y2="534.36" style="fill:none;" x1="554.6667" x2="554.6667" y1="541"/><line y2="534.36" style="fill:none;" x1="665.3333" x2="665.3333" y1="541"/><line y2="534.36" style="fill:none;" x1="776" x2="776" y1="541"/><line y2="55.64" style="fill:none;" x1="112" x2="112" y1="49"/><line y2="55.64" style="fill:none;" x1="222.6667" x2="222.6667" y1="49"/><line y2="55.64" style="fill:none;" x1="333.3333" x2="333.3333" y1="49"/><line y2="55.64" style="fill:none;" x1="444" x2="444" y1="49"/><line y2="55.64" style="fill:none;" x1="554.6667" x2="554.6667" y1="49"/><line y2="55.64" style="fill:none;" x1="665.3333" x2="665.3333" y1="49"/><line y2="55.64" style="fill:none;" x1="776" x2="776" y1="49"/></g><g transform="translate(112,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">0</text></g><g transform="translate(222.6667,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">1</text></g><g transform="translate(333.3333,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">2</text></g><g transform="translate(444,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">3</text></g><g transform="translate(554.6667,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">4</text></g><g transform="translate(665.3333,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">5</text></g><g transform="translate(776,546.3334)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-4" xml:space="preserve" y="14" style="stroke:none;">6</text></g><g transform="translate(444.0003,564.6667)" style="font-size:15px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-58" xml:space="preserve" y="16" style="stroke:none;">Frequency (GHz)</text></g><g style="fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(38,38,38); stroke-width:0.6667;"><line y2="49" style="fill:none;" x1="112" x2="112" y1="541"/><line y2="49" style="fill:none;" x1="776" x2="776" y1="541"/><line y2="541" style="fill:none;" x1="112" x2="118.64" y1="541"/><line y2="496.2727" style="fill:none;" x1="112" x2="118.64" y1="496.2727"/><line y2="451.5454" style="fill:none;" x1="112" x2="118.64" y1="451.5454"/><line y2="406.8182" style="fill:none;" x1="112" x2="118.64" y1="406.8182"/><line y2="362.0909" style="fill:none;" x1="112" x2="118.64" y1="362.0909"/><line y2="317.3636" style="fill:none;" x1="112" x2="118.64" y1="317.3636"/><line y2="272.6364" style="fill:none;" x1="112" x2="118.64" y1="272.6364"/><line y2="227.9091" style="fill:none;" x1="112" x2="118.64" y1="227.9091"/><line y2="183.1818" style="fill:none;" x1="112" x2="118.64" y1="183.1818"/><line y2="138.4545" style="fill:none;" x1="112" x2="118.64" y1="138.4545"/><line y2="93.7273" style="fill:none;" x1="112" x2="118.64" y1="93.7273"/><line y2="49" style="fill:none;" x1="112" x2="118.64" y1="49"/><line y2="541" style="fill:none;" x1="776" x2="769.36" y1="541"/><line y2="496.2727" style="fill:none;" x1="776" x2="769.36" y1="496.2727"/><line y2="451.5454" style="fill:none;" x1="776" x2="769.36" y1="451.5454"/><line y2="406.8182" style="fill:none;" x1="776" x2="769.36" y1="406.8182"/><line y2="362.0909" style="fill:none;" x1="776" x2="769.36" y1="362.0909"/><line y2="317.3636" style="fill:none;" x1="776" x2="769.36" y1="317.3636"/><line y2="272.6364" style="fill:none;" x1="776" x2="769.36" y1="272.6364"/><line y2="227.9091" style="fill:none;" x1="776" x2="769.36" y1="227.9091"/><line y2="183.1818" style="fill:none;" x1="776" x2="769.36" y1="183.1818"/><line y2="138.4545" style="fill:none;" x1="776" x2="769.36" y1="138.4545"/><line y2="93.7273" style="fill:none;" x1="776" x2="769.36" y1="93.7273"/><line y2="49" style="fill:none;" x1="776" x2="769.36" y1="49"/></g><g transform="translate(106.6667,541)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-52</text></g><g transform="translate(106.6667,496.2727)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-50</text></g><g transform="translate(106.6667,451.5454)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-48</text></g><g transform="translate(106.6667,406.8182)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-46</text></g><g transform="translate(106.6667,362.0909)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-44</text></g><g transform="translate(106.6667,317.3636)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-42</text></g><g transform="translate(106.6667,272.6364)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-40</text></g><g transform="translate(106.6667,227.9091)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-38</text></g><g transform="translate(106.6667,183.1818)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-36</text></g><g transform="translate(106.6667,138.4545)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-34</text></g><g transform="translate(106.6667,93.7273)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-32</text></g><g transform="translate(106.6667,49)" style="font-size:13px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="-19" xml:space="preserve" y="5.5" style="stroke:none;">-30</text></g><g transform="translate(74,342) rotate(-90)" style="font-size:15px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="0" xml:space="preserve" y="0" style="stroke:none;">EVM</text></g><g transform="translate(81,309) rotate(-90)" style="fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="0" xml:space="preserve" y="0" style="stroke:none;">RMS</text></g><g transform="translate(74,282) rotate(-90)" style="font-size:15px; fill:rgb(38,38,38); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; stroke:rgb(38,38,38);"><text x="0" xml:space="preserve" y="0" style="stroke:none;"> (dB)</text></g><g transform="translate(293,16)" style="font-size:15px; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; font-weight:bold;"><text x="0" xml:space="preserve" y="0" style="stroke:none;">EVM</text></g><g transform="translate(326,23)" style="text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; font-weight:bold;"><text x="0" xml:space="preserve" y="0" style="stroke:none;">RMS</text></g><g transform="translate(353,16)" style="font-size:15px; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; font-weight:bold;"><text x="0" xml:space="preserve" y="0" style="stroke:none;"> vs Frequency for LTE-10 QAM-64</text></g><g transform="translate(306,42)" style="font-size:15px; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; font-family:'SansSerif'; color-interpolation:linearRGB; font-weight:bold;"><text x="0" xml:space="preserve" y="0" style="stroke:none;">Tx=ADALM-PLUTO ; Rx=Keysight PXA</text></g><g style="stroke-linecap:butt; fill:rgb(0,114,189); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(0,114,189); stroke-width:0.6667;"><path d="M119.8573 496.2967 L120.964 500.5179 L122.0707 507.6335 L123.1773 511.1353 L124.284 518.013 L125.3907 516.308 L126.4973 513.2936 L127.604 511.4042 L128.7107 516.3908 L129.8173 517.1872 L130.924 518.4495 L132.0307 518.9783 L133.1373 514.108 L134.244 521.3147 L135.3507 524.1782 L136.4573 519.9242 L137.564 529.3629 L138.6707 511.7545 L139.7773 512.1399 L140.884 516.4993 L141.9907 515.4112 L143.0973 517.3177 L144.204 519.2451 L145.3107 520.0739 L146.4173 519.709 L147.524 519.3849 L148.6307 518.6252 L149.7373 523.7907 L150.844 525.3066 L151.9507 530.2446 L153.0573 519.6129 L154.164 518.9709 L155.2707 516.6816 L156.3773 514.84 L157.484 514.8501 L158.5907 516.7237 L159.6973 515.6836 L160.804 516.2992 L161.9107 512.3743 L163.0173 513.2065 L164.124 510.9296 L165.2307 510.6795 L166.3373 507.8516 L167.444 505.5565 L168.5507 504.4404 L169.6573 504.8442 L170.764 505.5177 L171.8707 502.6114 L172.9773 501.9036 L174.084 502.7896 L175.1907 497.652 L176.2973 504.179 L177.404 502.194 L178.5107 500.6237 L179.6173 500.1585 L180.724 497.3471 L181.8307 499.3731 L182.9373 492.1665 L184.044 502.3302 L185.1507 508.2039 L186.2573 502.9777 L187.364 503.3055 L188.4707 505.2599 L189.5773 500.7346 L190.684 505.2883 L191.7907 499.3612 L192.8973 497.8722 L194.004 498.5509 L195.1107 498.8708 L196.2173 495.8452 L197.324 496.2451 L198.4307 495.5419 L199.5373 495.2424 L200.644 491.0202 L201.7507 489.3874 L202.8573 493.054 L203.964 495.1126 L205.0707 496.0113 L206.1773 492.5824 L207.284 487.9875 L208.3907 485.0626 L209.4973 484.6773 L210.604 484.7602 L211.7107 484.442 L212.8173 479.8134 L213.924 481.1182 L215.0307 479.9248 L216.1373 476.5176 L217.244 478.6649 L218.3507 479.1319 L219.4573 472.8506 L220.564 465.5884 L221.6707 471.979 L222.7773 469.865 L223.884 464.8137 L224.9907 462.4751 L226.0973 467.0558 L227.204 459.8623 L228.3107 456.34 L229.4173 461.9289 L230.524 456.9052 L231.6307 459.8646 L232.7373 456.5273 L233.844 452.2941 L234.9507 453.0811 L236.0573 450.2059 L237.164 449.2233 L238.2707 452.181 L239.3773 449.0732 L240.484 450.6562 L241.5907 446.0117 L242.6973 449.8552 L243.804 442.0629 L244.9107 449.5639 L246.0173 444.1937 L247.124 445.4043 L248.2307 445.8134 L249.3373 446.0439 L250.444 447.5879 L251.5507 452.5883 L252.6573 451.118 L253.764 452.4036 L254.8707 460.3098 L255.9773 463.6173 L257.084 461.581 L258.1907 467.8454 L259.2973 468.3096 L260.404 472.2066 L261.5107 468.8549 L262.6173 470.9315 L263.724 470.7164 L264.8307 468.6281 L265.9373 470.5484 L267.044 463.1292 L268.1507 468.4648 L269.2573 466.9526 L270.364 459.6 L271.4707 462.2474 L272.5773 459.9278 L273.684 455.3771 L274.7906 449.402 L275.8973 449.6388 L277.004 446.3013 L278.1107 427.3229 L279.2173 423.2871 L280.324 427.3047 L281.4307 425.3893 L282.5373 421.7247 L283.644 427.8301 L284.7507 434.9739 L285.8573 426.8535 L286.964 421.5748 L288.0706 430.0691 L289.1773 422.3679 L290.284 420.0117 L291.3907 421.1003 L292.4973 420.0091 L293.604 415.851 L294.7107 423.0732 L295.8173 422.4868 L296.924 422.8453 L298.0307 422.2866 L299.1373 424.3285 L300.244 429.1991 L301.3507 422.5218 L302.4573 417.5437 L303.564 424.4706 L304.6707 424.6128 L305.7773 422.8705 L306.884 433.5926 L307.9907 416.3641 L309.0973 416.0209 L310.204 421.7589 L311.3107 419.7895 L312.4173 417.5988 L313.524 417.423 L314.6307 421.3426 L315.7373 424.5588 L316.844 425.6491 L317.9507 419.608 L319.0573 424.9262 L320.164 422.6009 L321.2707 421.7213 L322.3773 426.0806 L323.484 417.5584 L324.5907 419.49 L325.6973 415.1157 L326.804 417.4771 L327.9107 419.0088 L329.0173 418.1469 L330.124 427.7215 L331.2307 418.2081 L332.3373 417.6981 L333.444 411.581 L334.5507 417.4934 L335.6573 409.7655 L336.764 417.4905 L337.8707 410.4446 L338.9774 420.9044 L340.084 416.5161 L341.1907 412.4832 L342.2973 421.4243 L343.404 420.5372 L344.5107 427.1936 L345.6173 413.0559 L346.724 426.1467 L347.8307 414.3234 L348.9373 419.6366 L350.044 409.2933 L351.1507 418.7556 L352.2573 405.126 L353.364 413.8777 L354.4707 419.7633 L355.5773 415.2203 L356.684 409.8204 L357.7906 417.6026 L358.8973 414.5289 L360.004 407.4897 L361.1107 409.778 L362.2173 409.4092 L363.324 411.9708 L364.4307 414.1586 L365.5373 419.5141 L366.644 414.809 L367.7507 405.1147 L368.8573 408.3941 L369.964 400.5248 L371.0707 416.7623 L372.1773 412.5289 L373.284 405.1026 L374.3907 409.4625 L375.4973 395.3315 L376.604 399.6598 L377.7107 401.6653 L378.8173 399.2521 L379.924 398.9407 L381.0307 402.714 L382.1373 395.6109 L383.244 405.7257 L384.3507 397.3635 L385.4573 398.613 L386.564 397.6855 L387.6707 406.0653 L388.7773 394.9383 L389.884 407.1189 L390.9907 386.9612 L392.0973 398.8916 L393.204 400.3624 L394.3107 393.4253 L395.4174 397.2183 L396.524 395.2134 L397.6307 395.9933 L398.7373 389.6768 L399.844 382.2294 L400.9507 387.1637 L402.0573 382.4811 L403.164 382.6585 L404.2707 390.8621 L405.3773 381.2583 L406.484 387.516 L407.5907 393.8163 L408.6973 385.4522 L409.804 380.3832 L410.9107 379.5665 L412.0173 386.056 L413.124 376.7375 L414.2307 375.2094 L415.3373 373.7588 L416.444 376.0249 L417.5507 373.6196 L418.6573 379.3745 L419.764 367.3769 L420.8707 367.3725 L421.9774 376.3321 L423.084 379.2316 L424.1907 377.4238 L425.2973 378.5836 L426.404 379.6615 L427.5107 366.196 L428.6173 376.9113 L429.724 371.2506 L430.8307 369.6497 L431.9373 372.7241 L433.044 370.3577 L434.1507 375.0523 L435.2573 364.3821 L436.364 367.0104 L437.4707 369.6557 L438.5773 366.5369 L439.684 368.819 L440.7906 368.5062 L441.8973 365.0643 L443.004 364.1101 L444.1107 367.2514 L445.2173 351.723 L446.324 353.4754 L447.4307 344.9088 L448.5373 347.887 L449.644 365.5323 L450.7507 345.262 L451.8573 351.9326 L452.964 353.8752 L454.0707 335.9278 L455.1773 344.6204 L456.284 360.5474 L457.3907 360.9051 L458.4973 360.4186 L459.604 355.4577 L460.7107 363.0225 L461.8173 358.7154 L462.924 359.8184 L464.0307 356.8708 L465.1373 351.7896 L466.244 342.8488 L467.3507 344.1937 L468.4573 361.4372 L469.564 359.605 L470.6707 340.9876 L471.7773 343.1794 L472.884 341.6245 L473.9907 340.5519 L475.0973 353.63 L476.204 353.6058 L477.3107 342.9083 L478.4174 359.3872 L479.524 339.4373 L480.6307 357.8796 L481.7373 342.514 L482.844 355.3252 L483.9507 351.8338 L485.0573 361.1694 L486.164 354.9089 L487.2707 365.282 L488.3773 348.3005 L489.484 356.5822 L490.5907 359.2208 L491.6973 358.2031 L492.804 267.4671 L493.9107 363.2767 L495.0173 345.1803 L496.124 353.728 L497.2307 349.9121 L498.3373 357.5479 L499.444 342.3535 L500.5507 351.7536 L501.6573 352.5645 L502.764 338.843 L503.8707 332.585 L504.9774 342.9192 L506.084 330.1601 L507.1907 349.1043 L508.2973 339.6158 L509.404 347.3916 L510.5107 334.4225 L511.6173 343.2194 L512.724 335.5799 L513.8307 343.846 L514.9373 328.141 L516.044 343.9485 L517.1507 344.1501 L518.2573 345.9799 L519.364 345.4448 L520.4706 350.9586 L521.5773 335.5265 L522.684 342.4161 L523.7906 324.0551 L524.8973 345.5575 L526.004 335.5353 L527.1107 355.7975 L528.2173 341.8169 L529.324 344.5384 L530.4307 330.4294 L531.5373 349.7845 L532.644 334.6338 L533.7507 337.6169 L534.8574 340.4503 L535.964 343.7827 L537.0707 327.063 L538.1774 344.0555 L539.284 340.7634 L540.3907 336.9753 L541.4973 322.3337 L542.604 342.6095 L543.7107 326.0498 L544.8173 321.9495 L545.924 336.7861 L547.0306 334.4733 L548.1373 339.8403 L549.244 344.0311 L550.3506 321.7321 L551.4573 339.49 L552.564 318.6175 L553.6707 336.4772 L554.7773 336.2482 L555.884 321.1397 L556.9907 321.8724 L558.0974 336.3484 L559.204 315.6504 L560.3107 337.5241 L561.4173 322.6768 L562.524 333.6847 L563.6307 311.3645 L564.7374 322.7546 L565.844 331.2253 L566.9507 312.7901 L568.0573 317.4188 L569.164 325.6253 L570.2706 316.021 L571.3773 325.7976 L572.4839 328.992 L573.5906 334.8361 L574.6974 317.9397 L575.804 326.1061 L576.9107 324.6696 L578.0173 307.7171 L579.124 314.6333 L580.2307 322.7151 L581.3373 324.5232 L582.444 307.5405 L583.5507 314.6508 L584.6573 318.2513 L585.764 320.7612 L586.8707 320.8162 L587.9774 311.3461 L589.084 313.8449 L590.1907 318.0261 L591.2973 324.2028 L592.404 328.9775 L593.5106 312.2057 L594.6173 311.7303 L595.724 317.3211 L596.8307 314.4138 L597.9373 319.8473 L599.044 315.2233 L600.1506 324.7952 L601.2573 320.461 L602.364 311.1577 L603.4706 312.2097 L604.5773 314.6995 L605.684 313.253 L606.7907 316.8661 L607.8973 293.9323 L609.004 301.2265 L610.1107 303.1344 L611.2173 305.4422 L612.324 296.4654 L613.4307 302.7449 L614.5373 307.1696 L615.644 310.0492 L616.7507 301.8719 L617.8574 308.4758 L618.964 319.0368 L620.0707 315.4873 L621.1773 314.8131 L622.284 308.3566 L623.3906 310.4712 L624.4973 311.1581 L625.604 301.8595 L626.7107 299.5596 L627.8173 300.9536 L628.924 313.3441 L630.0307 309.2993 L631.1373 311.2495 L632.244 311.6889 L633.3506 314.3399 L634.4573 304.5929 L635.564 301.8568 L636.6707 305.8099 L637.7773 296.9121 L638.884 294.5475 L639.9907 309.6837 L641.0974 309.8242 L642.204 306.9789 L643.3107 298.2718 L644.4173 303.4889 L645.524 301.1717 L646.6307 298.2144 L647.7374 297.878 L648.844 303.1431 L649.9507 303.7924 L651.0573 302.6234 L652.164 289.0094 L653.2706 296.5996 L654.3773 302.7406 L655.4839 306.4425 L656.5906 291.818 L657.6974 295.8527 L658.804 299.1635 L659.9107 291.3839 L661.0173 300.0872 L662.124 303.4006 L663.2307 300.4397 L664.3373 297.7625 L665.444 289.8006 L666.5507 304.8547 L667.6573 299.5933 L668.764 300.8569 L669.8707 290.9762 L670.9774 300.5818 L672.084 293.1723 L673.1907 290.107 L674.2973 290.7808 L675.404 294.8365 L676.5106 292.1664 L677.6173 281.2102 L678.724 292.2704 L679.8307 290.1694 L680.9373 289.7549 L682.044 295.8341 L683.1506 282.968 L684.2573 287.2209 L685.364 282.3659 L686.4706 292.5844 L687.5773 283.0433 L688.684 294.2132 L689.7907 293.3681 L690.8973 291.1031 L692.004 280.9604 L693.1107 286.9 L694.2173 288.0406 L695.324 290.4768 L696.4307 279.0677 L697.5373 287.2564 L698.644 293.2762 L699.7507 290.5317 L700.8574 279.6723 L701.964 292.9953 L703.0707 287.6913 L704.1773 283.9456 L705.284 285.4641 L706.3906 281.2361 L707.4973 284.5173 L708.604 286.2225 L709.7107 276.1804 L710.8173 276.3045 L711.924 278.6005 L713.0307 276.9689 L714.1373 278.8358 L715.244 279.8601 L716.3506 275.5712 L717.4573 281.8879 L718.564 270.9279 L719.6707 272.3059 L720.7773 275.2772 L721.884 274.3611 L722.9907 268.7332 L724.0974 271.3393 L725.204 275.7115 L726.3107 271.2633 L727.4173 263.7573 L728.524 271.1733 L729.6307 271.8798 L730.7374 270.9655 L731.844 267.9696 L732.9507 269.8674 L734.0573 269.436 L735.164 271.9706 L736.2706 258.1362 L737.3773 271.0502 L738.4839 273.8819 L739.5906 270.2908 L740.6974 266.0526 L741.804 267.0997 L742.9107 269.3735 L744.0173 271.2995 L745.124 263.2299 L746.2307 264.9106 L747.3373 260.6159 L748.444 258.5764 L749.5507 259.4179 L750.6573 256.1263 L751.764 262.1324 L752.8707 260.7733 L753.9774 256.6758 L755.084 256.996 L756.1907 259.731 L757.2973 252.2646 L758.404 251.733 L759.5106 252.4408 L760.6173 247.9846 L761.724 259.8781 L762.8307 255.5711 L763.9373 258.3609 L765.044 246.4724 L766.1506 247.3117 L767.2573 255.0117 L768.364 253.5911 L769.4706 255.3292 L770.5773 255.1461 L771.684 251.8232 L772.7907 249.0813 L773.8973 253.9596 L775.004 250.6166" style="fill:none; fill-rule:evenodd;"/></g><g transform="translate(200.5333,272.6364)" style="stroke-linecap:butt; fill:red; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; color-interpolation:linearRGB; stroke:red;"><path style="fill:none;" d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284"/><path d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284" style="fill:none; stroke:blue;" transform="translate(0,-134.1818)"/><path d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284" style="fill:none;" transform="translate(177.0667,0)"/><path d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284" style="fill:none;" transform="translate(520.1333,-89.4545)"/><path d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284" style="fill:none; stroke:blue;" transform="translate(177.0667,-134.1818)"/><path d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284" style="fill:none; stroke:blue;" transform="translate(298.8,-134.1818)"/></g><g style="fill:white; text-rendering:optimizeSpeed; color-rendering:optimizeSpeed; image-rendering:optimizeSpeed; shape-rendering:crispEdges; color-interpolation:sRGB; stroke:white;"><path style="stroke:none;" d="M587 116 L587 63 L763 63 L763 116 Z"/></g><g transform="translate(634,73)" style="text-rendering:geometricPrecision; font-family:'SansSerif'; color-interpolation:linearRGB; color-rendering:optimizeQuality; image-rendering:optimizeQuality;"><text x="0" xml:space="preserve" y="5" style="stroke:none;">test results</text></g><g style="stroke-linecap:butt; fill:rgb(0,114,189); text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; stroke-linejoin:round; color-interpolation:linearRGB; stroke:rgb(0,114,189); stroke-width:0.6667;"><line y2="73" style="fill:none;" x1="591" x2="631" y1="73"/></g><g transform="translate(634,89.5)" style="text-rendering:geometricPrecision; font-family:'SansSerif'; color-interpolation:linearRGB; color-rendering:optimizeQuality; image-rendering:optimizeQuality;"><text x="0" xml:space="preserve" y="5" style="stroke:none;">AD9361 datasheet limit</text></g><g transform="translate(611,89.5)" style="stroke-linecap:butt; fill:red; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; color-interpolation:linearRGB; stroke:red;"><path style="fill:none;" d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284"/></g><g transform="translate(634,106)" style="text-rendering:geometricPrecision; font-family:'SansSerif'; color-interpolation:linearRGB; color-rendering:optimizeQuality; image-rendering:optimizeQuality;"><text x="0" xml:space="preserve" y="5" style="stroke:none;">AD9363 datasheet limit</text></g><g transform="translate(611,106)" style="stroke-linecap:butt; fill:blue; text-rendering:geometricPrecision; color-rendering:optimizeQuality; image-rendering:optimizeQuality; color-interpolation:linearRGB; stroke:blue;"><path style="fill:none;" d="M0 -4 L0 4 M-4 0 L4 0 M-2.8284 -2.8284 L2.8284 2.8284 M-2.8284 2.8284 L2.8284 -2.8284"/><path transform="translate(-611,-106)" style="fill:none; stroke-width:0.6667; fill-rule:evenodd; stroke:rgb(38,38,38);" d="M587 116 L587 63 L763 63 L763 116 Z"/></g></g>
</svg>
</div>


<div class="tips" style="display: table; table-layout: fixed; background-color: #e3efff; height: auto; width: 100%; ">
<div class="left-icon" style="display: table-cell; vertical-align: middle; background-color: #a3c7ff; padding-top: 10px; box-sizing: border-box; height: auto; width: 38px; text-align: center;"><img style="width: 26px; vertical-align: middle;" src="https://s3-us-west-2.amazonaws.com/static.seeed.cc/seeed/icon/Note.svg" alt="attention icon" /></div>
<div class="right-desc" style="display: table-cell; vertical-align: middle; padding-left: 15px; box-sizing: border-box; width: calc(95% - 38px);">
<p style="font-weight: bold; margin-top: 10px;">Note</p>
<p style="font-size: 14px;">这是 SMA 的功率而非天线，任何天线（包括套件中提供的天线）都可能产生额外的滤波（更改形状）以及增益/衰减。 </p>
</div>
</div>

 

此测试是在开放式实验室环境中进行的，因此，我们可以观察到某些常见商业频率（如 LTE 和 WiFi）的残留分量。为了消除这些异常值，测试应在 RF 腔室内运行，以确保没有外部噪声，但由于我们需要符合数据表规范，我们不太可能这样做。



**[返回终端用户指南主页](http://wiki.seeedstudio.com/cn/ADALM-PLUTO-for-End-User/)**



[^1]:
https://literature.cdn.keysight.com/litweb/pdf/5966-4008E.pdf







<!--图片位置设置-->
<style>
.method1{
  :center;
  float:right;
}
.method2{
  :center;
  float:left;
}
</style>