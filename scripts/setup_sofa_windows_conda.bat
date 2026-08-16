@echo off
REM Setup SOFA Framework + SofaPython3 for adaptive cushion project on Windows.
REM Run this file from Anaconda Prompt / Miniforge Prompt, not plain cmd.

set ENV_NAME=sofa-velostat

echo ============================================================
echo Creating conda env: %ENV_NAME%
echo ============================================================
call conda create -n %ENV_NAME% python=3.12 -y
if errorlevel 1 (
    echo Python 3.12 env creation failed. Trying Python 3.10...
    call conda create -n %ENV_NAME% python=3.10 -y
)

call conda activate %ENV_NAME%

echo ============================================================
echo Installing SOFA app + SofaPython3
echo ============================================================
call conda install sofa-app sofa-python3 --channel https://prefix.dev/sofa-framework --channel conda-forge -y
if errorlevel 1 (
    echo.
    echo ERROR: SOFA install failed.
    echo Try deleting the env and rerun:
    echo   conda env remove -n %ENV_NAME%
    echo Then rerun this script.
    pause
    exit /b 1
)

echo ============================================================
echo Testing Python imports
echo ============================================================
python -c "import Sofa; import SofaRuntime; print('SofaPython3 OK')"
if errorlevel 1 (
    echo.
    echo WARNING: Python import test failed.
    echo Copy the full error message and send it back.
    pause
    exit /b 1
)

echo ============================================================
echo Testing runSofa path
echo ============================================================
where runSofa

echo.
echo Installation appears OK.
echo Now test GUI manually with:
echo   conda activate %ENV_NAME%
echo   runSofa -l SofaImGui -g imgui -l SofaPython3
echo.
pause
