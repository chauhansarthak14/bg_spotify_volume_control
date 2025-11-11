from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import os

# Get the Spotify audio session
sessions = AudioUtilities.GetAllSessions()

#getting base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(BASE_DIR, "SpotifyKnobControl_pycaw_app.txt")

#function for reading which app to control
def get_state():
    try:
        with open(FILE_DIR, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "Spotify"

#go through the sessions in volume mixer 
for session in sessions:
    #failsafe for no return from process name call
    try:session.Process.name()
    except:continue
    #get the current app to control
    app = get_state()
    #use app to check in the process name
    if app in session.Process.name():
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        #decrease volume by set step
        current = volume.GetMasterVolume()
        if(current<0.3):
            dec = -0.01
        else:
            dec = -0.033
        new_volume = max(0.0, min(1.0, current + dec))
        volume.SetMasterVolume(new_volume, None)
        break