@echo off

SET RUN_DOTPY=python.exe C:\python_tool\CME_Validation\front_end.py
SET PYTHON_PATH=C:\Progra~2\Python36-32



REM Hunt around for python
IF EXIST "python.exe" (
  SET SCRIPT=%RUN_DOTPY%
) ELSE (
  IF EXIST "%PYTHON_PATH%" (
    SET SCRIPT=%PYTHON_PATH%\%RUN_DOTPY%
  ) ELSE (
    IF EXIST %PYTHON% SET SCRIPT=%PYTHON%\%RUN_DOTPY%
  )
)

IF NOT "" == "%SCRIPT%" (
  %SCRIPT%
  pause
) ELSE (
  echo.
  echo Python.exe is not in the path!
  pause
)
:end
