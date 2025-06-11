
# Introduction

 I made this code to Run an RC plane, needless to say it would work on anything.
 This Code Utilizes Pygame library, it sends the inputs from your gamepad to Serial port, which you can receive on your microcontroller, I've attached an example of receiver code for Arduino ide.
 you may tune the code as you see fit.

RC Remotes are Expensive As F$%& and they're kind of prohibited to buy in here, so I had to make do.

This Code can send and receive from Serial port, a serial monitor is available with the ability to send in the small text box at the bottom, make sure to not miss it.
![C2S](<a href="https://ibb.co/GQs7r6yR"><img src="https://i.ibb.co/GQs7r6yR/ss.png" alt="ss" border="0"></a>)
## License
 You can use this code for free, Distribution is prohibited.
## TODO List

- [ ] dynamic window size - important
- [ ] Finish 3D view model, add a quadcopter/airplane model and receive euler angles from serial to display attitude - important
- [ ] make the installer copy what's within dist to the build location - important
- [ ] Fix transparency issues (tkinter) - meh
 ***

# Installation

## Windows

[Download a prebuilt Version](https://github.com/alyayman921/ControllerToSerial/releases/download/V1.0/C2S-prebuilt.zip)

---

or install python 3.12+ then run Dependencies.bat 
after that you should be able to open terminal in C2S folder
``
```cmd
python C2S.py
```
---
You can also build it on your own by using build.bat, then copy /dist content to the original folder and you should be good to go 
## Linux

C2S works on Linux too, You already know what to do most likely.



 

