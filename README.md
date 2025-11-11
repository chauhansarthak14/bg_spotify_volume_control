The Project is made for 
- people who want to control SPOTIY/YOUTUBE music volume in background while in game or doing other *stuff.
- newer keyboards with knob/roller feature like aula, royal kludge softwares doesn't support these finctionality
of using to knob to control specific app volume.

Must do before runnig
- make sure your knob is in system volume control mode then only this will work
- add path into the .ahk files
- either add .ahk files to your startup folder or
- create .exe from .ahk and then add that .exe to your startup folder
- once done you will be able to control spotify music volume even in the background.

Update for version 1.1 - 
- If you want to control youtube volume, just replace "Spotify" with "chrome.exe" in both .py files.

Update for version 1.2 - 
- Added knob press feature to select switching app control between spotify and chrome.exe
- Now the app has relative paths to all the script so now you can keep the files in any place on your pc
    keeping in mind python is installed in you pc and you have pycaw, winotify libraries.
- The control method is same as exponential control where of volume.