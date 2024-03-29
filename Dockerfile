___ python:3.9-slim

# Copying requirements file and installing dependencies
___ requirements.txt /tmp/
___ pip install --no-cache-dir -r /tmp/requirements.txt

# Copying the rest of the application files
___ . .

# Setting the default command to run the application
CMD ["python", "app.py"]