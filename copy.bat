@echo off
rem 源文件夹路径，当前脚本所在目录
set "source_folder=.\\"
rem 目标文件夹路径，当前脚本所在目录下的 blueflylabor.github.io 文件夹
set "destination_folder=.\blueflylabor.github.io"

rem 检查源文件夹是否存在
if not exist "%source_folder%" (
    echo 源文件夹不存在，请检查路径。
    pause
    exit /b 1
)

rem 检查目标文件夹是否存在，如果不存在则创建
if not exist "%destination_folder%" (
    mkdir "%destination_folder%"
    echo 已创建目标文件夹：%destination_folder%
)

rem 使用 xcopy 命令复制文件，/E 表示复制所有子文件夹（包括空的），/Y 表示不提示直接覆盖
xcopy "%source_folder%\*" "%destination_folder%" /E /Y

echo 文件复制完成，已覆盖目标文件夹内的所有文件。
pause