from winotify import Notification, audio
import os

APP_STATE = "NA"
DEFAULT_APP = "Spotify"

#getting base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(BASE_DIR, "SpotifyKnobControl_pycaw_app.txt")
PNG_DIR = os.path.join(BASE_DIR, "BackgroundKnobImage.png")

#read the current controlled app
try:
    with open(FILE_DIR, "r") as f:
        APP_STATE = f.read().strip()
except FileNotFoundError:
    with open(FILE_DIR, "w") as f:
        f.write(DEFAULT_APP)
        APP_STATE = DEFAULT_APP

#now write the changed app into the file for switching
if(APP_STATE == "Spotify"):
    APP_STATE = "chrome.exe"
    with open(FILE_DIR, "w") as f:
        f.write(APP_STATE)

elif(APP_STATE == "chrome.exe"):
    APP_STATE = "Spotify"
    with open(FILE_DIR, "w") as f:
        f.write(APP_STATE)

#sending notification
toast = Notification(
    app_id="Background Knob",
    title="Controlling",
    msg=APP_STATE,
    icon=PNG_DIR
)
toast.set_audio(audio.SMS, loop=False)
toast.show()