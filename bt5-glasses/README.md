# BT5.4 Glasses

## Device : Hyper MZT

### BT device setup

#### Settings > Bluetooth
Paired & Connect : `F16 connected` <br>

#### Settings > Sound
Output <br>
Output Device: `Bluetooth (HFP)-F-16`<br>
Input <br>
Input  Device: `Bluetooth (HFP)-F-16`<br>

---
### BT event test
```
sudo apt install evtest
sudo evtest
```

#### BT device list on Ubuntu PC:
```
No device specified, trying to scan all of /dev/input/event*
Available devices:
/dev/input/event0:	Sleep Button
/dev/input/event1:	Power Button
/dev/input/event10:	HDA NVidia HDMI/DP,pcm=9
/dev/input/event11:	HDA NVidia HDMI/DP,pcm=3
/dev/input/event12:	HDA NVidia HDMI/DP,pcm=7
/dev/input/event13:	HDA NVidia HDMI/DP,pcm=8
/dev/input/event14:	HDA NVidia HDMI/DP,pcm=9
/dev/input/event15:	HDA Intel PCH Rear Mic
/dev/input/event16:	HDA Intel PCH Front Mic
/dev/input/event17:	HDA Intel PCH Line
/dev/input/event18:	HDA Intel PCH Line Out
/dev/input/event19:	HDA Intel PCH Front Headphone
/dev/input/event2:	Power Button
/dev/input/event20:	HDA Intel PCH HDMI/DP,pcm=3
/dev/input/event21:	HDA Intel PCH HDMI/DP,pcm=7
/dev/input/event22:	HDA Intel PCH HDMI/DP,pcm=8
/dev/input/event23:	HDA Intel PCH HDMI/DP,pcm=9
/dev/input/event24:	F-16 (AVRCP)
/dev/input/event25:	F-16
/dev/input/event3:	Logitech Wireless Keyboard PID:4023
/dev/input/event4:	Logitech Wireless Mouse
/dev/input/event5:	Intel HID events
/dev/input/event6:	Video Bus
/dev/input/event7:	HDA NVidia HDMI/DP,pcm=3
/dev/input/event8:	HDA NVidia HDMI/DP,pcm=7
/dev/input/event9:	HDA NVidia HDMI/DP,pcm=8
Select the device event number [0-25]: 25
`````````````````````````````````
Ctrl-C to interrupt<br>

---
#### Event Test: Touch from Glasses
```
sudo python evtest_touch.py
```

Listening for events on /dev/inpu/event25...
Touch/Key Pressed: KEY_VOLUMEUP
Touch/Key Pressed: KEY_VOLUMEUP

---
## Agentic Glasses

### LMM-VTuber
![](https://raw.githubusercontent.com/rkuo2000/Jetson/refs/heads/main/assets/Open_LLM_VTuber.png)

### Hermes + JARVIS
![](https://github.com/rkuo2000/Jetson/blob/main/assets/Hermes_JARVIS.png?raw=true)

---
### [AI虛擬人（Live2D 語音助理）](https://github.com/YuriCrystal/ai-avatar-bot)
![](https://github.com/rkuo2000/Jetson/blob/main/assets/AI_Avatar.png?raw=true)



