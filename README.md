# Zanvok CariboSystem 6
v6.11

## What's new in CariboSystem 6 ?
* CUB2022331-CS (Update for CariboSystem 6.0.5), features new features :
    * New App Startup

    * CariboSystem SDK 6 [BETA]

    * Special CariboSystem Installer/Setup

    * Introducing Advanced CariboSystem App Manager [BETA]

    * Revised code for Windows, Unix (macOS) and Linux :
        * The new code uses `os`, `sys` and `subprocess` modules

        * For example, for clearing the screen, the command in Windows is `cls`, whereas the command in Linux/Unix is `clear`. So CariboSystem 6 uses `sys.platform` to identify the system as `win32`(Windows) or `darwin`(macOS) or `xdg-open`(Linux)
    
    * New PY-DOS 8 Integration

    * New Recovery Tool (Not included with this package)

    * New Core Mode Execution

    * Introducing new BSOD (Blue Screen Of Death)

    * New NetGet Download Utility

    * New Calculator App

* UBS2022330-CS (Security Update for CarboSystem)
    * Fixed security issue with internal user data files

## Developers
* Gautham Nair
* Suraj Varma
* Adithya Vijayan
* Akshit Santosh
* Siddharth Sajeev
* Jishnu Harikumar
* Jatin Raj
* Sunil MS

Copyright (c) Zanvok Corporation 2022
