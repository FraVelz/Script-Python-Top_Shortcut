@echo off
Title "Keyboard Shortcut Manager"
color 0a

REM Messagge
echo.
echo Continue Off:

REM Close Apps
taskkill /f /im opera.exe
taskkill /f /im chrome.exe
taskkill /f /im excel.exe
taskkill /f /im notepad.exe
taskkill /f /im Winword.exe
taskkill /f /im powerpnt.exe

REM Turn Off
shutdown /s /t 20

REM Visual show before turn Off

:process
cd %USERPROFILE%/documents && tree
timeout /t 1 /nobreak > nul

cd ../desktop
tree
timeout /t 2 /nobreak > nul
goto process

:: Encoded: FraVelz