@echo off
echo Starting Secure AI Web App...
echo.

REM Install required packages silently
python -m pip install flask scikit-learn >nul 2>&1

echo Launching server...
start cmd /k python app.py

REM Wait for server to start
timeout /t 3 >nul

echo Opening browser...
start http://127.0.0.1:5000/

pause