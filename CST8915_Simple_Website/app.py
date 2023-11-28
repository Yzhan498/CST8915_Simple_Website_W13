# To run in VS CTRL + F5
# To run outside VS:
# Set an environment variable for FLASK_APP. On Linux and macOS, use export set FLASK_APP=webapp; on Windows use $env:FLASK_APP=webapp if you're using PowerShell, or set FLASK_APP=webapp if you're using Command Prompt.
# Navigate into the hello_app folder, then launch the program using python -m flask run.

# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
