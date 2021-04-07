@echo off
color b

set n=^&echo.
set fileName=generate_apk
set finalFile=%fileName%.bat
set currentPathUnformated=%~dp0
set currentPath=%currentPathUnformated:~0,-1%
set finalPath=%currentPath%\bin
set finalPathFile=%finalPath%\%finalFile%
set finalCommand=python %currentPath%\%fileName%.py

mkdir bin
echo @echo off>%finalPathFile%
echo %finalCommand%>>%finalPathFile%
echo Add the %finalPath% to your PATH ^^_^^

echo.
echo.
echo After you've added to path, press any key to scape . . .
pause >nul