FROM python:3.9-slim

# Copying requirements file and installing dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copying the rest of the application files
COPY . .

# Setting the default command to run the application
CMD ["python", "app.py"]