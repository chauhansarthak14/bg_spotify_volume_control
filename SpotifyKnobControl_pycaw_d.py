from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# Get the Spotify audio session
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    try:session.Process.name()
    except:continue
    if "Spotify" in session.Process.name():
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