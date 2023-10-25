venv:
	@echo "A virtual environment is being created."
	@python -m venv venv
	@echo "Virtual environment created!"

install:
	@pip install -r requirements.txt 2>&1 | findstr /C:"ERROR" /C:"WARNING" > nul
	
	@if %errorlevel%==0 ( \
	    echo An error or warning occurred while installing packages. \
	) else ( \
	    echo Packages installed successfully. \
	)

clean:
	@if exist __pycache__ rd /s /q __pycache__
	@for /d /r . %%i in (__pycache__) do @if exist "%%i" rd /s /q "%%i"
	@timeout 3
	@cls