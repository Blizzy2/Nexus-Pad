#Requires AutoHotkey v2.0

^!1:: { ; Ctrl+Alt+1
    Run("discord://")
    Sleep 500
    if FileExist("C:\Users\" A_UserName "\AppData\Local\Medal\Medal.exe")
        Run("C:\Users\" A_UserName "\AppData\Local\Medal\Medal.exe")
}

^!2:: { ; Ctrl+Alt+2
    ; Placeholder for Nexus AI:
    Run("http://localhost:3000")
}

^!3:: { ; Ctrl+Alt+3
    Run("steam://open/main")
}
