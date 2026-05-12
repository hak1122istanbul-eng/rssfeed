@echo off
echo Starting local web server on port 8000...
echo Press Ctrl+C to stop the server.

:: Open the webpage in the default browser safely
start "" "http://localhost:8000"

:: Start the Python HTTP server serving the 'docs' directory
cd docs
python -m http.server 8000
pause
