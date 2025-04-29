from pycaw.pycaw import AudioUtilities,ISimpleAudioVolume

# Get the Spotify audio session
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    try:session.Process.name()
    except:continue
    if "Spotify" in session.Process.name():
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        #increase volume by defined resolution
        current = volume.GetMasterVolume()
        if(current<0.3):
            inc = 0.01
        else:
            inc = 0.033
        new_volume = max(0.0, min(1.0, current + inc))
        volume.SetMasterVolume(new_volume, None)
        break