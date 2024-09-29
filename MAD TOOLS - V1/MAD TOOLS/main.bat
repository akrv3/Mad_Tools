@echo off
chcp 65001 >nul
title Mad Tools - by AKr
cd files
color B
:start
call :banner

:menu    
for /f %%A in ('"prompt $H £echo on £FOR %%b IN (1) do rem"') do set BS=%%A
echo.
echo.
echo [+] 1- IP INFOS                                [+] 5-  
echo [+] 2- OSINT LINK                              [+] 6- 
echo [+] 3- WEBHOOK SPAM                            [+] 7- MAD TOOLS INFO
echo [+] 4-                                         [+] 8- Exite 
echo.

set /p input=Entre un choix : %BS% 

if /I %input% EQU 1 start ipinfos
if /I %input% EQU 2 start osint.html
if /I %input% EQU 3 start webhook.py
if /I %input% EQU 4 start 
if /I %input% EQU 5 start 
if /I %input% EQU 6 start 
if /I %input% EQU 7 start MADTOOLSINFO.bat
if /I %input% EQU 8 goto :exite


cls
goto :start


:banner
echo.
echo                                                   [I] ΜΔĐ ŦØØŁŞ [I]
echo.
echo                                               ("`-''-/").___..--''"`-._
echo                                                `6_ 6  )   `-.  (    ).`-.__.`)
echo                                                (_Y_.)'  ._   )  `._ `.``-..-'
echo                                                  _..`--'_..-_/  /--'_.' ,'
echo                                                 (il),-''  (li),'  ((!.-'
echo.
pause

:exite