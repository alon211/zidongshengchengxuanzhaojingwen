@echo off
echo "生成虚拟环境" 

SET curdir=%cd%\venv
echo "%curdir%"
if exist  %curdir% (
 echo "已经有一个虚拟环境"
 TIMEOUT /T 8
) else (
        echo "create new venv finish"
        python -m venv ./venv
        
)

