@echo off
rem 源文件夹路径，可根据实际情况修改
set "source_folder=.\"
rem 目标文件夹路径，可根据实际情况修改
set "destination_folder=.\blueflylabor.github.io"

rem 检查源文件夹是否存在
if not exist "%source_folder%" (
    echo 源文件夹不存在。
    pause
    exit /b 1
)

rem 检查目标文件夹是否存在，如果不存在则创建
if not exist "%destination_folder%" (
    mkdir "%destination_folder%"
)

rem 复制源文件夹下的所有文件到目标文件夹
xcopy "%source_folder%\*" "%destination_folder%" /E /Y

echo 文件复制完成。
pause