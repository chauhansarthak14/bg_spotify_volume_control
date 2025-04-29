#Requires AutoHotkey v2.0

Volume_Up:: {
    Run("python C:\Bg_Spotifyvc\SpotifyKnobControl_pycaw_i.py", , "Hide")
    sleep 50
    return
}

Volume_Down:: {
    Run("python C:\Bg_Spotifyvc\SpotifyKnobControl_pycaw_d.py", , "Hide")
    sleep 50
    return
}