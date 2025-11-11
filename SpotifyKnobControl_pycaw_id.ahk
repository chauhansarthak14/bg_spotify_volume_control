#Requires AutoHotkey v2.0

Volume_Up:: {
    Run('python "' . A_ScriptDir . '\SpotifyKnobControl_pycaw_i.py"', , 'Hide')
    Sleep(50)
    return
}

Volume_Down:: {
    Run('python "' . A_ScriptDir . '\SpotifyKnobControl_pycaw_d.py"', , 'Hide')
    Sleep(50)
    return
}

Volume_Mute:: {
    Run('python "' . A_ScriptDir . '\SpotifyKnobControl_pycaw_c.py"', , 'Hide')
    Sleep(50)
    return
}