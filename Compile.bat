@ECHO OFF

title Compile PassGen
echo Compiling PassGen.

pyinstaller.exe --icon=Logo.ico --onefile main.py
move dist\main.exe .\PassGen.exe

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__

del main.spec

cls
if EXIST .\PassGen.exe goto Compiled
if NOT EXIST .\PassGen.exe goto NotCompiled

:Compiled
echo PassGen Compiled Successfully!
echo Get ready to Generate a Strong Password!
echo|set /p="Continue."
pause >nul
exit

:NotCompiled
echo Can't Compile PassGen!
echo|set /p="Continue."
pause >nul
exit
