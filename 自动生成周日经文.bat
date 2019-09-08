@echo off
c:
CALL call %cd%\venv\Scripts\activate.bat
python %cd%\ppt_export.py
CALL %cd%\venv\Scripts\dectivate.bat
exit
