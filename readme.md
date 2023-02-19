# Multi-Touch-Kit-ProMicro

As the title suggests, this project is trying to reproduce the result of [Multi-Touch kit](https://hci.cs.uni-saarland.de/projects/multi-touch-kit/) with a ProMicro board.

---
## Demo
https://user-images.githubusercontent.com/51289140/219960157-e1035877-1ed2-4f21-ac63-bcd13f59a0d3.mp4
> The demo is using the source code from "experiment" branch (See Note.2)
---
## Preparation
In this repo:
- A python script to create the grid
- A KiCad project for the pcb design
- The source code for the ProMicro
- Clone of [Multi-Touch Kit Processing code](https://github.com/HCI-Lab-Saarland/MultiTouchKitUI)

Not in the repo:
- [PlatformIO](https://platformio.org/)
- [Processing](https://processing.org/)

---
## Procedure
Almost of the procedure is same as the Multi-Touch Kit Project
1. Generate a grid
2. Connect all pin and wire
3. Upload the code through PlatformIO
4. Use Processing to observe the result

---
## Note
1. Readings from R1 seem having a lot of noise and effecting the result, so it is disabled.
2. "Experiment" branch seem to have a better performance. I am trying to figure out the reason, feel free to comment in the [issue](https://github.com/CcydtN/Multi-Touch-Kit-ProMicro/issues/2).

---
Reference:
- [Multi-Touch Kit](https://hci.cs.uni-saarland.de/projects/multi-touch-kit/)
    - The Starting point of this project
- [Sensor Design Guidelines](http://ww1.microchip.com/downloads/en/DeviceDoc/FAQs%20-%20Sensor%20Design%20Guidelines.pdf)
    - More detail about pcb design can be found here.
    - The python script for generating grid is base on this document.
- [Pro Micro & Fio V3 Hookup Guide](https://learn.sparkfun.com/tutorials/pro-micro--fio-v3-hookup-guide/hardware-overview-pro-micro)
    - Pin layout about ProMicro
