# BAPPR

[![Supported Python Version](https://img.shields.io/badge/Version-3.0-blue)]()

![promo_front.jpg](docs/images/promo_front.jpg)
Version 2.2 ^

Design plans for the BAPPR LED buck converter

Buy them on Tindie: https://www.tindie.com/products/themariday/bappr-v22/

## Operational parameters

Input Voltage: 7v to 17v

Output Voltage: 5v ±1%

Output Current: 5A, (6A for 30 second bursts)

Efficiency:

![efficiency_graph.png](docs/images/efficiency_graph.png)

> [!WARNING]
> The BAPPR gets hot!
> 
> At 3 amps, you can expect around a 15° rise in temperature
> 
> At 5 amps, you can expect around a 36° rise in temperature

> [!IMPORTANT]
> 
> At 7v, the BAPPR struggles to maintain 5v at high current resulting in a drop of around 0.17 volts per amp
> 
> At higher voltages, the BAPPR maintains voltage within ±1%